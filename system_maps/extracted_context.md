# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] ROOT
# ==========================================================================
# 📄 [요청 1] TARGET: start.py (82-202라인)
# ----------------------------------------------------------
```python
def main():
    print("======================================================================")
    print("🔥 [Jjap-Cursor Launchpad] 짭커서 통합 마스터 사령탑 기동 시작!")
    print(f"📂 프로젝트 루트: {ROOT_DIR}")
    print(f"🤖 매칭된 파이썬 사령관: {TARGET_PYTHON}")
    print("======================================================================")

    # 🚚 [0단계 이전] 원샷 폴더 이전 마이그레이션 선제 가동
    # (cline_tools/ 가 이미 없다면 내부에서 자동으로 조용히 스킵됩니다)
    print("----------------------------------------------------------------------")

    # 🛠️ watchdog 자동 검사 및 누락 시 핀포인트 자동 설치
    auto_install_dependencies()
    print("----------------------------------------------------------------------")

    # 🚀 [0-A단계: 선제 청소 및 동적 복제 리빌드 발동]
    print("----------------------------------------------------------------------")

    # 환경변수 세팅 복사 및 조립 (import 크래시 방지 및 실시간 무버퍼 강제)
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.pathsep.join([str(ROOT_DIR), str(CLINE_TOOLS_DIR), env.get("PYTHONPATH", "")])
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"

    # 🔥 [0-B단계: 최신 코드로 완벽 채워진 src/ 폴더 순정 인덱싱 메커니즘 가동]
    print("➡️ 0단계: 기동 전 AI 초경량 요약 지도(AI_CODEBASE_MAP.md) 선제 강제 빌드...")
    if CREATE_AI_MAP_SCRIPT.exists():
        try:
            # 1단계 인덱서 선제 요격 가동 (이제 src/ 내부에 최신 복제본들이 다 들어있으므로 완벽하게 추출됩니다)
            indexer_script = CLINE_TOOLS_DIR / "indexer.py"
            if indexer_script.exists():
                subprocess.run(
                    [TARGET_PYTHON, "-c", "from indexer import AdvancedIndexerV2; from pathlib import Path; AdvancedIndexerV2(Path('.')).scan_project()"],
                    cwd=str(ROOT_DIR),
                    env=env,
                    check=True,
                    stdout=subprocess.DEVNULL
                )
            
            # 2단계 AI 마스터 지도 제작 실행
            subprocess.run(
                [TARGET_PYTHON, str(CREATE_AI_MAP_SCRIPT)],
                cwd=str(ROOT_DIR),
                env=env,
                check=True
            )
        except Exception as e:
            print(f"⚠️ [경고] 초도 AI 맵 생산 중 경미한 지연 또는 예외 발생 (워처 가동 시 자동 회복 예정): {e}")
    else:
        print(f"⚠️ [경고] {CREATE_AI_MAP_SCRIPT.name} 스크립트를 찾을 수 없어 0단계를 건너뜁니다.")
    print("----------------------------------------------------------------------")

    # 📡 1단계: 실시간 백그라운드 워처(jjap_watcher.py) 가동
    print("➡️ 1단계: 실시간 백그라운드 자동 감시망(Watcher) 투입 중...")
    
    if not WATCHER_SCRIPT.exists():
        print(f"❌ [경로 에러] 워처 스크립트가 지정된 궤도에 존재하지 않습니다: {WATCHER_SCRIPT}")
        return

    # stdout과 stderr를 부모 터미널 화면으로 다이렉트 중계 바느질
    watcher_process = subprocess.Popen(
        [TARGET_PYTHON, str(WATCHER_SCRIPT)],
        cwd=str(ROOT_DIR),
        env=env,
        stdout=sys.stdout if DEBUG_MODE else subprocess.DEVNULL,
        stderr=sys.stderr if DEBUG_MODE else subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
    )
    
    time.sleep(1.0)  # 워처 안착용 시동 대기 타임 보정
    
    if watcher_process.poll() is None:
        print("✅ [SUCCESS] 감시망이 백그라운드 메모리에 안착 후 정상 실시간 중계 중입니다.")
    else:
        print(f"❌ [기동 즉사] 감시망 프로세스가 실행 즉시 사망했습니다. (리턴코드: {watcher_process.poll()})")
        print("💡 상단에 출력된 파이썬 문법/모듈 에러 내역을 추적하십시오.")
        return

    # 🧠 2단계: 에이전트 네비게이터(agent_navigator.py) GUI 창 띄우기
    print("➡️ 2단계: 세맨틱 네비게이터 검색기(GUI) 전면 배치 중...")
    if not NAVIGATOR_SCRIPT.exists():
        print(f"❌ [경로 에러] 네비게이터 GUI 스크립트가 없습니다: {NAVIGATOR_SCRIPT}")
        watcher_process.terminate()
        return
        
    print("💡 [안내] 검색기 창을 닫으면 백그라운드 감시망도 함께 안전하게 종료됩니다.")
    print("----------------------------------------------------------------------")
    
    try:
        subprocess.run(
            [TARGET_PYTHON, str(NAVIGATOR_SCRIPT)],
            cwd=str(ROOT_DIR),
            env=env,
            check=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 [사용자 중단] 터미널에서 종료 신호를 수신했습니다.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ [런타임 사고] 검색기(GUI) 내부에서 무단 크래시 예외 발생! 리턴코드: {e.returncode}")
    except Exception as e:
        print(f"\n❌ [런타임 사고] 검색기 실행 중 치명적 시스템 오류 발생: {e}")
    finally:
        # 🧼 3단계: 청소 작전
        print("----------------------------------------------------------------------")
        print("🧼 3단계: 검색기 종료 감지 -> 백그라운드 감시망 자원 회수(종료) 중...")
        try:
            if watcher_process.poll() is None:
                watcher_process.terminate()
                watcher_process.wait(timeout=3)
                print("✅ [CLEANUP] 백그라운드 프로세스가 안전하게 전원 종료되었습니다.")
            else:
                print("ℹ️ [CLEANUP] 백그라운드 감시망 프로세스가 이미 종료되어 있습니다.")
        except Exception as ex:
            if DEBUG_MODE:
                print(f"🔍 [디버그] 자원 정리 중 내부 예외 유출: {ex}")
            watcher_process.kill()
            print("⚡ [FORCE KILL] 프로세스를 강제 종료 처리했습니다.")
            
    print("======================================================================")
    print("🏁 [Jjap-Cursor] 마스터 사령탑 철수 완료. 깔끔하게 정리되었습니다!")
    print("======================================================================")
```

# 📄 [요청 2] TARGET: extraction_target_project/build.gradle.kts (1-34라인)
# ----------------------------------------------------------
```python
plugins {
    id("java-library")
    id("xyz.jpenilla.run-paper") version "3.0.2"
}

repositories {
    mavenCentral()
    maven("https://repo.papermc.io/repository/maven-public/")
}

dependencies {
   
    compileOnly("io.papermc.paper:paper-api:1.21.11-R0.1-SNAPSHOT")
}

java {
    
    toolchain.languageVersion = JavaLanguageVersion.of(21)
}

tasks {
    runServer {
        // ⭕ 여기도 1.21.1로 수정
        minecraftVersion("1.21.11")
        jvmArgs("-Xms2G", "-Xmx2G")
    }

    processResources {
        val props = mapOf("version" to version)
        filesMatching("plugin.yml") {
            expand(props)
        }
    }
}
```

# 📄 [요청 3] TARGET: tools/universal_indexer/create_ai_map.py (63-122라인)
# ----------------------------------------------------------
```python
def collect_target_files():
    """[수정] .py 제한을 해제하고, 제외 키워드가 없는 프로젝트 내의 '모든 파일'을 수집합니다."""
    print("=" * 80)
    print("[DEBUG] collect_target_files() 시작")
    print(f"[DEBUG] PROJECT_ROOT = {PROJECT_ROOT}")
    print(f"[DEBUG] SCAN_MODE    = {SCAN_MODE}")
    print("=" * 80)
    if SCAN_MODE == "ROOT":
        scan_target = PROJECT_ROOT
        print("🎯 [create_ai_map] Mode: ROOT (프로젝트 전체 경로를 직접 스캔합니다)")
    else:
        # 레거시 src 지칭을 완전히 청산하고, 새로운 타깃 폴더명으로 단일화
        scan_target = PROJECT_ROOT / "extraction_target_project"
        print("🎯 [create_ai_map] Mode: EXTRACTION_TARGET_PROJECT (extraction_target_project/ 폴더 내부만 정밀 스캔합니다)")

    if not scan_target.exists():
        print(f"❌ [오류] 스캔 대상 경로가 존재하지 않습니다: {scan_target}")
        return []

    print(f"[DEBUG] SCAN_TARGET  = {scan_target}")

    target_files = []
    for root, dirs, files in os.walk(scan_target, followlinks=True):
        normalized_root = root.replace("\\", "/")

        print("\n------------------------------------------------------")
        print(f"[DEBUG] WALK ROOT : {root}")
        print(f"[DEBUG] DIR COUNT : {len(dirs)}")
        print(f"[DEBUG] FILE COUNT: {len(files)}")

        if "src/project_root/src" in normalized_root:
            print(f"[SKIP] duplicated path : {normalized_root}")
            continue
        if any(kw in normalized_root for kw in EXCLUDE_KEYWORDS):
            print(f"[SKIP] excluded keyword : {normalized_root}")
            continue

        print("[DIRS]")
        for d in dirs:
            print("   ", d)

        print("[FILES]")
        for file in files:
            print("   ", file)

        for file in files:
            if file == "start.py" and SCAN_MODE == "SRC":
                continue
            
            # 💡 [교정] 특정 확장자 차단 해제 -> 모든 파일을 수집 대상으로 포함
            full_path = Path(root) / file
            print(f"[ADD] {full_path}")
            target_files.append(full_path)

    print("=" * 80)
    print("[DEBUG] collect_target_files END")
    print(f"[DEBUG] TOTAL FILES = {len(target_files)}")
    print("=" * 80)

    return sorted(target_files)
```

# 📄 [요청 4] TARGET: extraction_target_project/src/main/java/com/desertcore/DesertCore.java (40-83라인)
# ----------------------------------------------------------
```python
    private void registerAllListenersInPackage(String packageName) {
        try {
            String path = packageName.replace('.', '/');
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            URL resource = classLoader.getResource(path);
            
            if (resource == null) return;

            // 팩트 교정: String에서 getAbsoluteFile()을 호출하던 결함을 java.io.File 변환으로 정밀 수정
            File directory = new File(resource.toURI());
            if (!directory.exists()) return;

            // 폴더 내부의 모든 파일명을 가져옴
            File[] files = directory.listFiles();
            if (files == null) return;

            for (File file : files) {
                // .class 파일만 검열
                if (file.getName().endsWith(".class")) {
                    String className = packageName + '.' + file.getName().substring(0, file.getName().length() - 6);
                    Class<?> clazz = Class.forName(className);

                    // 해당 클래스가 마인크래프트 Listener 인터페이스를 구현했는지 확인
                    if (Listener.class.isAssignableFrom(clazz) && !clazz.isInterface()) {
                        try {
                            // 생성자에 DesertCore 플러그인을 주입하며 동적으로 인스턴스 생성
                            Listener listener = (Listener) clazz.getConstructor(DesertCore.class).newInstance(this);
                            
                            // 버킷에 최종 자동 등록
                            getServer().getPluginManager().registerEvents(listener, this);
                            
                            if (Switch.DEBUG_MODE) {
                                getLogger().info("[DEBUG] 자동 로드 성공: " + className);
                            }
                        } catch (Exception e) {
                            getLogger().warning("클래스 동적 생성 실패 (생성자 규격 확인 필요): " + className);
                        }
                    }
                }
            }
        } catch (Exception e) {
            getLogger().severe("패키지 스캔 중 치명적 오류 발생: " + e.getMessage());
        }
    }
```

# 📄 [요청 5] TARGET: tools/universal_indexer/indexer.py (82-162라인)
# ----------------------------------------------------------
```python
    def scan_project(self):
        """설정된 SCAN_MODE에 따라 프로젝트 내의 모든 등록된 언어 파일을 스캔합니다."""
        # 🛠️ 레거시 "src" 하드코딩을 청산하고, switch.py의 새로운 물리 폴더명("extraction_target_project")과 완벽 매핑
        scan_target = self.project_root if SCAN_MODE == "ROOT" else self.project_root / "extraction_target_project"
        log(f"🚀 [디버깅 레이더 가동] 모드: {SCAN_MODE} | 물리 스캔 범위: {scan_target}")

        EXCLUDE_KEYWORDS = [".venv", ".git", "__pycache__", "system_memory", "system_maps"]
        log(f"🛡️ 고유 스캔 제외 키워드 목록: {EXCLUDE_KEYWORDS}")
        
        if not scan_target.exists():
            log(f"❌ [치명적 오류] 지정된 스캔 타깃 경로가 디스크에 존재하지 않습니다: {scan_target}")
            return

        total_scanned_count = 0
        total_ignored_count = 0

        for root, dirs, files in os.walk(scan_target, followlinks=True):
            normalized_root = root.replace("\\", "/")
            
            # 제외 폴더 조건 검사 및 로깅
            if any(kw in normalized_root for kw in EXCLUDE_KEYWORDS):
                log(f"🚫 [패스] 제외 필터 경로 스킵: {normalized_root}")
                continue

            for file in files:
                file_path = Path(root) / file
                ext = file_path.suffix.lower()

                # 동적으로 로드된 파서 대상 확장자 범위에 포함되는지 확인
                if ext in self.parsers:
                    log(f"🔍 [타깃 포착] 파일 발견: {file_path.name} (확장자: {ext})")
                    self.index_file(file_path, ext)
                    total_scanned_count += 1
                else:
                    total_ignored_count += 1

        log(f"🏁 스캔 타임라인 종료 -> 분석 통계 [처리 완료: {total_scanned_count}개 | 미지원/패스: {total_ignored_count}개]")

        # 🗂️ 수집 완료 후 디스크 정밀 장부 보관소로 직행 쓰기
        self.save_index_data()

    def index_file(self, file_path: Path, ext: str):
        """개별 파일을 파서를 통해 쪼개어 마스터 장부에 바느질합니다."""
        try:
            rel_path_str = file_path.relative_to(self.project_root).as_posix()
        except ValueError:
            rel_path_str = file_path.resolve().relative_to(self.project_root.resolve()).as_posix()

        log(f"🧵 [장부 바느질 개시] 상대 경로 키: '{rel_path_str}'")
        parser_func = self.parsers[ext]
        
        try:
            log(f"   📡 플러그인 함수 {parser_func.__name__} 원격 연산 제어권 이양 중...")
            res = parser_func(file_path, self.project_root)
            
            if not res or len(res) < 5:
                log(f"   ⚠️ [규격 위반] '{rel_path_str}' 파서의 반환 데이터가 5대 규격을 충족하지 못해 드롭합니다.")
                return

            f_symbols, f_context, f_def_map, f_protocols, f_registry = res

            # 데이터 적재 현황 세부 체크 로그
            log(f"   📥 수집 결과 피드백 받음 -> 심볼: {len(f_symbols)}개, 정의 매핑: {len(f_def_map)}개, 프로토콜: {len(f_protocols)}개, 레지스트리: {len(f_registry)}개")

            # 1. 글로벌 심볼 리스트 누적
            self.symbols.extend(f_symbols)
            
            # 2. 파일 요약 정보 컨텍스트 병합
            self.files_context.update(f_context)
            
            # 3. 정의 맵 및 레지스트리 병합
            self.definition_map.update(f_def_map)
            self.data_protocols.update(f_protocols)
            
            for item in f_registry:
                if item not in self.registry_constants:
                    self.registry_constants.append(item)

            log(f"   📈 [바느질 완료] 마스터 메모리 장부 적재 성공: '{rel_path_str}'")
        except Exception as e:
            log(f"   💥 [인덱싱 내부 크래시] 파일 처리 중 예외 발생: {rel_path_str} | 에러 내용: {e}")
```

# 📄 [요청 6] TARGET: extraction_target_project/src/main/resources/plugin.yml (1-10라인)
# ----------------------------------------------------------
```python
name: desertcore
version: '${version}'

main: com.desertcore.DesertCore
api-version: '1.21'
load: POSTWORLD
commands:
  로비:
    description: "오퍼레이터 전용 로비 복귀 명령어"
    permission: "desertcore.op"
```

# 📄 [요청 7] TARGET: tools/universal_indexer/switch.py (1-13라인)
# ----------------------------------------------------------
```python
"""Jjap-Cursor Path Targeting Toggle Controller.

[switch.py]
형님이 프로젝트 소스코드를 수색할 때, 실제 디스크 경로와 1대1로 일치시킬지("ROOT"),
아니면 기존 격리 구조 내부만 스캔할지("EXTRACTION_TARGET_PROJECT") 딸깍 결정하는 영문 마스터 콘솔 스위치입니다.
"""

# 🎛️ 마스터 토글 스위치 
# "ROOT" -> 프로젝트 전체 원본 경로 직접 징집 (경로 불일치 에러 완벽 해결! 실제 경로 유지)
# "EXTRACTION_TARGET_PROJECT"  -> 기존 방식 (오직 extraction_target_project/ 폴더 내부만 검사)
SCAN_MODE = "ROOT"

SYSTEM_EXCLUDES = ["system_memory", "system_maps"]
```
