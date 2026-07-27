import re
import hashlib
import sys
from pathlib import Path

# ==========================================
# 🚨 [DEBUG CONFIG] 디버깅 로그 ON / OFF 스위치
# ==========================================
DEBUG = True  # True로 설정하면 디버깅 로그가 터미널에 쏟아집니다. (OFF 하려면 False)

def debug_log(message: str):
    """DEBUG 플래그가 True일 때만 콘솔에 로그를 도배하는 헬퍼 함수"""
    if DEBUG:
        print(f"[🐛 DEBUG_JS_PARSER] {message}", file=sys.stderr)


def find_end_line_by_braces(lines: list, start_line_idx: int) -> int:
    """
    start_line_idx(0-based)부터 아래로 내려가며 중괄호('{', '}')의 짝을 맞아 0이 되는 지점(end_line)을 추적합니다.
    """
    brace_count = 0
    found_first_open = False
    
    debug_log(f"  └── 🔍 [Trace Scope Start] L{start_line_idx + 1}부터 스코프 추적 시작...")

    for i in range(start_line_idx, len(lines)):
        line = lines[i]
        
        # 주석이나 문자열 내 중괄호 예외처리를 위한 단순화 카운터
        # (필요 시 더 정밀하게 다듬을 수 있습니다)
        opens = line.count('{')
        closes = line.count('}')

        if opens > 0 and not found_first_open:
            found_first_open = True
            
        if found_first_open:
            brace_count += (opens - closes)
            debug_log(f"      [L{i + 1}] Line Brace Delta: +{opens}/-{closes} => Current Balance Depth: {brace_count}")
            
            # 괄호 짝이 다 맞아떨어져 스코프가 종료된 순간
            if brace_count <= 0:
                debug_log(f"  └── 🎯 [Trace Scope Complete] 함수/클래스 종료 지점 발견: L{i + 1}")
                return i + 1  # 1-based line number

    debug_log(f"  └── ⚠️ [Trace Scope Fail] 닫히는 중괄호를 찾지 못함 -> 시작 라인(L{start_line_idx + 1}) 반환")
    return start_line_idx + 1


def extract_symbols(file_path: Path, project_root: Path):
    """
    ⚡ [JavaScript / TypeScript Parser v1.1 - Debug Mode Supported]
    """
    symbols = []
    file_context = {}
    definition_map = {}
    data_protocols = {}
    registry_constants = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        debug_log(f"❌ 파일 읽기 실패: {file_path} - 에러: {e}")
        return symbols, {}, {}, {}, []

    try:
        rel_path_str = file_path.relative_to(project_root).as_posix()
    except ValueError:
        rel_path_str = file_path.resolve().relative_to(project_root.resolve()).as_posix()

    debug_log("=" * 80)
    debug_log(f"📂 [File Start] 파일 스캔 시작: {rel_path_str}")
    debug_log("=" * 80)

    file_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    lines = content.splitlines()

    # 1. 💡 임포트 모듈 포착
    imports = []
    import_matches = re.findall(r'(?:import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]|require\([\'"]([^\'"]+)[\'"]\))', content)
    for m in import_matches:
        imp = m[0] if m[0] else m[1]
        imports.append(imp)
    
    debug_log(f"📦 발견된 임포트 모듈 ({len(imports)}개): {imports}")
    imports_str = f"💡 📦 imp: {', '.join(sorted(list(set(imports))))}" if imports else ""
    symbols_info_strings = []

    # 정규식 패턴 지정
    class_pattern = re.compile(r'class\s+([A-Za-z0-9_]+)')
    func_pattern = re.compile(r'(?:async\s+)?function\s+([A-Za-z0-9_]+)|(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>')
    object_pattern = re.compile(r'(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*\{([^}]+)\}')

    KEYWORDS = ["entity", "platform", "camera", "sensor", "agent", "navigator", "indexer", "retriever", "handler", "service", "controller"]

    for idx, line in enumerate(lines, start=1):
        line_str = line.strip()

        # [A] 클래스 스캔
        c_match = class_pattern.search(line_str)
        if c_match:
            c_name = c_match.group(1)
            c_id = f"{rel_path_str}::{c_name}"
            
            debug_log(f"\n🧬 [Class Found] '{c_name}' detected at Line {idx}")
            end_line = find_end_line_by_braces(lines, idx - 1)
            debug_log(f"    결과: Class '{c_name}' Scope -> [L{idx} ~ L{end_line}]")

            symbols_info_strings.append(f"🧬 class {c_name} [L{idx}~L{end_line}]")
            symbols.append({
                "symbol_id": c_id, "name": c_name, "full_name": c_name, "type": "class",
                "path": rel_path_str, "start_line": idx, "end_line": end_line,
                "calls": [], "used_by": []
            })
            definition_map[c_name] = f"{rel_path_str}:{idx}"

            if any(kw in c_name.lower() for kw in KEYWORDS):
                registry_constants.append(c_name)

        # [B] 함수/메서드 스캔
        f_match = func_pattern.search(line_str)
        if f_match:
            f_name = f_match.group(1) or f_match.group(2)
            if f_name and f_name not in ["require", "import"]:
                f_id = f"{rel_path_str}::{f_name}"
                
                debug_log(f"\n🎯 [Function Found] '{f_name}()' detected at Line {idx}")
                end_line = find_end_line_by_braces(lines, idx - 1)
                debug_log(f"    결과: Function '{f_name}()' Scope -> [L{idx} ~ L{end_line}]")

                symbols_info_strings.append(f"🎯 def {f_name}() [L{idx}~L{end_line}]")
                symbols.append({
                    "symbol_id": f_id, "name": f_name, "full_name": f_name, "type": "function",
                    "path": rel_path_str, "start_line": idx, "end_line": end_line,
                    "calls": [], "used_by": []
                })
                definition_map[f_name] = f"{rel_path_str}:{idx}"

    # [C] 데이터 프로토콜 스캔
    for obj_match in object_pattern.finditer(content):
        obj_name = obj_match.group(1)
        obj_body = obj_match.group(2)
        
        fields = {}
        kv_pairs = re.findall(r'([A-Za-z0-9_]+)\s*:\s*([^,\n]+)', obj_body)
        for k, v in kv_pairs:
            v_clean = v.strip().strip("'\"")
            fields[k] = f"Any (기본값: {v_clean})"
            
        if fields:
            debug_log(f"🔑 [Protocol Found] '{obj_name}' Protocol Keys: {list(fields.keys())}")
            data_protocols[obj_name] = fields

    # 5. 요약 문자열 조립
    summary_parts = [imports_str] if imports_str else []
    summary_parts.extend(symbols_info_strings)
    symbols_summary_str = " | ".join(summary_parts)

    file_context[rel_path_str] = {
        "hash": file_hash,
        "symbols_summary": symbols_summary_str,
        "skeleton": content[:500]
    }

    debug_log(f"\n✅ [File Scan Finished] {rel_path_str} - 추출된 심볼 수: {len(symbols)}개\n")
    return symbols, file_context, definition_map, data_protocols, registry_constants