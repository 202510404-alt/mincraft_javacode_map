import re
import hashlib
from pathlib import Path

def extract_symbols(file_path: Path, project_root: Path):
    """
    ⚡ [JavaScript / TypeScript Parser v1.0]
    JS 및 TS 파일을 스캔하여 5대 장부 튜플 규격을 완벽히 생성하여 반환합니다.
    
    반환값 규격: 
    (symbols_list, file_context_dict, definition_map_dict, data_protocols_dict, registry_constants_list)
    """
    symbols = []
    file_context = {}
    definition_map = {}
    data_protocols = {}
    registry_constants = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return symbols, {}, {}, {}, []

    try:
        rel_path_str = file_path.relative_to(project_root).as_posix()
    except ValueError:
        rel_path_str = file_path.resolve().relative_to(project_root.resolve()).as_posix()

    file_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    lines = content.splitlines()

    # 1. 💡 임포트 모듈 포착 (import ... from '...' 또는 require('...'))
    imports = []
    import_matches = re.findall(r'(?:import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]|require\([\'"]([^\'"]+)[\'"]\))', content)
    for m in import_matches:
        imp = m[0] if m[0] else m[1]
        imports.append(imp)
    
    imports_str = f"💡 📦 imp: {', '.join(sorted(list(set(imports))))}" if imports else ""
    symbols_info_strings = []

    # 2. 🧬 클래스 정의 추출 (class ClassName)
    class_pattern = re.compile(r'class\s+([A-Za-z0-9_]+)')
    # 3. 🎯 일반 함수 및 화살표 함수 추출
    # function funcName(...) / const funcName = (...) => / async function ...
    func_pattern = re.compile(r'(?:async\s+)?function\s+([A-Za-z0-9_]+)|(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>')
    # 4. 🔑 데이터 객체/프로토콜 추출 (const DataProtocol = { ... })
    object_pattern = re.compile(r'(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*\{([^}]+)\}')

    # 레지스트리 핵심 키워드 감지 타깃
    KEYWORDS = ["entity", "platform", "camera", "sensor", "agent", "navigator", "indexer", "retriever", "handler", "service", "controller"]

    for idx, line in enumerate(lines, start=1):
        line_str = line.strip()

        # [A] 클래스 스캔
        c_match = class_pattern.search(line_str)
        if c_match:
            c_name = c_match.group(1)
            c_id = f"{rel_path_str}::{c_name}"
            symbols_info_strings.append(f"🧬 class {c_name} [L{idx}]")
            
            symbols.append({
                "symbol_id": c_id, "name": c_name, "full_name": c_name, "type": "class",
                "path": rel_path_str, "start_line": idx, "end_line": idx,
                "calls": [], "used_by": []
            })
            definition_map[c_name] = f"{rel_path_str}:{idx}"

            # 레지스트리 키워드 매칭
            if any(kw in c_name.lower() for kw in KEYWORDS):
                registry_constants.append(c_name)

        # [B] 함수/메서드 스캔
        f_match = func_pattern.search(line_str)
        if f_match:
            f_name = f_match.group(1) or f_match.group(2)
            if f_name and f_name not in ["require", "import"]:
                f_id = f"{rel_path_str}::{f_name}"
                symbols_info_strings.append(f"🎯 def {f_name}() [L{idx}]")
                
                symbols.append({
                    "symbol_id": f_id, "name": f_name, "full_name": f_name, "type": "function",
                    "path": rel_path_str, "start_line": idx, "end_line": idx,
                    "calls": [], "used_by": []
                })
                definition_map[f_name] = f"{rel_path_str}:{idx}"

    # [C] 데이터 프로토콜(객체 리터럴 구조) 스캔
    for obj_match in object_pattern.finditer(content):
        obj_name = obj_match.group(1)
        obj_body = obj_match.group(2)
        
        # 키-값 쌍 파싱
        fields = {}
        kv_pairs = re.findall(r'([A-Za-z0-9_]+)\s*:\s*([^,\n]+)', obj_body)
        for k, v in kv_pairs:
            v_clean = v.strip().strip("'\"")
            fields[k] = f"Any (기본값: {v_clean})"
            
        if fields:
            data_protocols[obj_name] = fields

    # 5. 최종 한줄 요약 문자열 조립
    summary_parts = [imports_str] if imports_str else []
    summary_parts.extend(symbols_info_strings)
    symbols_summary_str = " | ".join(summary_parts)

    file_context[rel_path_str] = {
        "hash": file_hash,
        "symbols_summary": symbols_summary_str,
        "skeleton": content[:500]  # 코드 상단 뼈대 요약
    }

    return symbols, file_context, definition_map, data_protocols, registry_constants