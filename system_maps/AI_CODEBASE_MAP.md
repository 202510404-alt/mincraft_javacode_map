# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (INTELLIGENT SCAN)

> **[AI 프로토콜 매뉴얼]** 이 문서는 다른 AI 비서들의 경로 오해를 차단하기 위해 파일마다 **실제 하드디스크 상대 경로 `[📂 실제경로]`**를 강제 명시해 둔 특수 지도입니다.
> AI 비서는 절대 눈치로 경로를 추측하지 말고, 파일명 뒤에 박혀있는 `[📂 실제경로]` 규격을 그대로 복사하여 agent_navigator를 호출하십시오.

```markdown
project_root/
├── .gitignore [📂 .gitignore]
├── .idea/
│   ├── .gitignore [📂 .idea/.gitignore]
│   ├── AI_agent.iml [📂 .idea/AI_agent.iml]
│   ├── gradle.xml [📂 .idea/gradle.xml]
│   ├── misc.xml [📂 .idea/misc.xml]
│   ├── modules.xml [📂 .idea/modules.xml]
│   ├── vcs.xml [📂 .idea/vcs.xml]
│   ├── workspace.xml [📂 .idea/workspace.xml]
├── .vscode/
│   ├── settings.json [📂 .vscode/settings.json] -> [💡 📦 json_keys: 17개 포착 | 🔑 "terminal.integrated.sendKeybindingsToShell" [bool] | 🔑 "accessibility.verbosity.terminal" [bool] | 🔑 "git.autofetch" [bool] | 🔑 "explorer.confirmDelete" [bool] | 🔑 "git.openRepositoryInParentFolders" [str] | ...외 12개]
├── a [📂 a]
├── agent_core/
│   ├── __init__.py [📂 agent_core/__init__.py]
│   ├── execution/
│   │   ├── __init__.py [📂 agent_core/execution/__init__.py]
│   ├── memory/
│   │   ├── __init__.py [📂 agent_core/memory/__init__.py]
│   ├── plan/
│   │   ├── __init__.py [📂 agent_core/plan/__init__.py]
│   │   ├── gemini_client.py [📂 agent_core/plan/gemini_client.py]
│   │   ├── planner.py [📂 agent_core/plan/planner.py]
│   │   ├── prompt_builder.py [📂 agent_core/plan/prompt_builder.py]
│   │   ├── schemas.py [📂 agent_core/plan/schemas.py]
│   ├── validation/
│   │   ├── __init__.py [📂 agent_core/validation/__init__.py]
├── agent_plan.md [📂 agent_plan.md]
├── extraction_target_project/
│   ├── .gitignore [📂 extraction_target_project/.gitignore]
│   ├── .gradle/
│   │   ├── 8.5/
│   │   │   ├── checksums/
│   │   │   │   ├── checksums.lock [📂 extraction_target_project/.gradle/8.5/checksums/checksums.lock]
│   │   │   ├── dependencies-accessors/
│   │   │   │   ├── dependencies-accessors.lock [📂 extraction_target_project/.gradle/8.5/dependencies-accessors/dependencies-accessors.lock]
│   │   │   │   ├── gc.properties [📂 extraction_target_project/.gradle/8.5/dependencies-accessors/gc.properties]
│   │   │   ├── fileChanges/
│   │   │   │   ├── last-build.bin [📂 extraction_target_project/.gradle/8.5/fileChanges/last-build.bin]
│   │   │   ├── fileHashes/
│   │   │   │   ├── fileHashes.lock [📂 extraction_target_project/.gradle/8.5/fileHashes/fileHashes.lock]
│   │   │   ├── gc.properties [📂 extraction_target_project/.gradle/8.5/gc.properties]
│   │   ├── 9.3.0/
│   │   │   ├── checksums/
│   │   │   │   ├── checksums.lock [📂 extraction_target_project/.gradle/9.3.0/checksums/checksums.lock]
│   │   │   │   ├── md5-checksums.bin [📂 extraction_target_project/.gradle/9.3.0/checksums/md5-checksums.bin]
│   │   │   │   ├── sha1-checksums.bin [📂 extraction_target_project/.gradle/9.3.0/checksums/sha1-checksums.bin]
│   │   │   ├── executionHistory/
│   │   │   │   ├── executionHistory.bin [📂 extraction_target_project/.gradle/9.3.0/executionHistory/executionHistory.bin]
│   │   │   │   ├── executionHistory.lock [📂 extraction_target_project/.gradle/9.3.0/executionHistory/executionHistory.lock]
│   │   │   ├── fileChanges/
│   │   │   │   ├── last-build.bin [📂 extraction_target_project/.gradle/9.3.0/fileChanges/last-build.bin]
│   │   │   ├── fileHashes/
│   │   │   │   ├── fileHashes.bin [📂 extraction_target_project/.gradle/9.3.0/fileHashes/fileHashes.bin]
│   │   │   │   ├── fileHashes.lock [📂 extraction_target_project/.gradle/9.3.0/fileHashes/fileHashes.lock]
│   │   │   ├── gc.properties [📂 extraction_target_project/.gradle/9.3.0/gc.properties]
│   │   ├── buildOutputCleanup/
│   │   │   ├── buildOutputCleanup.lock [📂 extraction_target_project/.gradle/buildOutputCleanup/buildOutputCleanup.lock]
│   │   │   ├── cache.properties [📂 extraction_target_project/.gradle/buildOutputCleanup/cache.properties]
│   │   │   ├── outputFiles.bin [📂 extraction_target_project/.gradle/buildOutputCleanup/outputFiles.bin]
│   │   ├── configuration-cache/
│   │   │   ├── b1v9tig786iwcqfq7vhp6ewvx/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/.gradle/configuration-cache/b1v9tig786iwcqfq7vhp6ewvx/candidates.bin]
│   │   │   ├── ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/.gradle/configuration-cache/ceaa47c2-fe2b-4f1e-b765-79131ca6ef12/work.bin]
│   │   │   ├── configuration-cache.lock [📂 extraction_target_project/.gradle/configuration-cache/configuration-cache.lock]
│   │   │   ├── gc.properties [📂 extraction_target_project/.gradle/configuration-cache/gc.properties]
│   │   ├── file-system.probe [📂 extraction_target_project/.gradle/file-system.probe]
│   │   ├── vcs-1/
│   │   │   ├── gc.properties [📂 extraction_target_project/.gradle/vcs-1/gc.properties]
│   ├── .idea/
│   │   ├── .gitignore [📂 extraction_target_project/.idea/.gitignore]
│   │   ├── .name [📂 extraction_target_project/.idea/.name]
│   │   ├── compiler.xml [📂 extraction_target_project/.idea/compiler.xml]
│   │   ├── gradle.xml [📂 extraction_target_project/.idea/gradle.xml]
│   │   ├── misc.xml [📂 extraction_target_project/.idea/misc.xml]
│   │   ├── modules/
│   │   │   ├── desertcore.main.iml [📂 extraction_target_project/.idea/modules/desertcore.main.iml]
│   │   ├── vcs.xml [📂 extraction_target_project/.idea/vcs.xml]
│   │   ├── workspace.xml [📂 extraction_target_project/.idea/workspace.xml]
│   ├── .vscode/
│   │   ├── launch.json [📂 extraction_target_project/.vscode/launch.json] -> [💡 📦 json_keys: 2개 포착 | 🔑 "version" [str] | 🔑 "configurations" [list]]
│   ├── bin/
│   │   ├── main/
│   │   │   ├── com/
│   │   │   │   ├── desertcore/
│   │   │   │   │   ├── DesertCore.class [📂 extraction_target_project/bin/main/com/desertcore/DesertCore.class]
│   │   │   │   │   ├── DesertCoreTester.class [📂 extraction_target_project/bin/main/com/desertcore/DesertCoreTester.class]
│   │   │   │   │   ├── legacy/
│   │   │   │   │   │   ├── deathevent$1.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/deathevent$1.class]
│   │   │   │   │   │   ├── deathevent$2.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/deathevent$2.class]
│   │   │   │   │   │   ├── deathevent.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/deathevent.class]
│   │   │   │   │   │   ├── marendumbul.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/marendumbul.class]
│   │   │   │   │   │   ├── samakportal$1.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/samakportal$1.class]
│   │   │   │   │   │   ├── samakportal$2.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/samakportal$2.class]
│   │   │   │   │   │   ├── samakportal.class [📂 extraction_target_project/bin/main/com/desertcore/legacy/samakportal.class]
│   │   │   │   │   ├── lobbycmd.class [📂 extraction_target_project/bin/main/com/desertcore/lobbycmd.class]
│   │   │   │   │   ├── session/
│   │   │   │   │   │   ├── GameSession.class [📂 extraction_target_project/bin/main/com/desertcore/session/GameSession.class]
│   │   │   │   │   │   ├── GameSessionManager.class [📂 extraction_target_project/bin/main/com/desertcore/session/GameSessionManager.class]
│   │   │   │   │   ├── Switch.class [📂 extraction_target_project/bin/main/com/desertcore/Switch.class]
│   │   │   ├── plugin.yml [📂 extraction_target_project/bin/main/plugin.yml]
│   ├── build/
│   │   ├── classes/
│   │   │   ├── java/
│   │   │   │   ├── main/
│   │   │   │   │   ├── com/
│   │   │   │   │   │   ├── desertcore/
│   │   │   │   │   │   │   ├── deathevent$1.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/deathevent$1.class]
│   │   │   │   │   │   │   ├── deathevent$2.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/deathevent$2.class]
│   │   │   │   │   │   │   ├── deathevent.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/deathevent.class]
│   │   │   │   │   │   │   ├── DesertCore.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/DesertCore.class]
│   │   │   │   │   │   │   ├── lobbycmd.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/lobbycmd.class]
│   │   │   │   │   │   │   ├── marendumbul.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/marendumbul.class]
│   │   │   │   │   │   │   ├── samakportal$1.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/samakportal$1.class]
│   │   │   │   │   │   │   ├── samakportal$2.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/samakportal$2.class]
│   │   │   │   │   │   │   ├── samakportal.class [📂 extraction_target_project/build/classes/java/main/com/desertcore/samakportal.class]
│   │   ├── reports/
│   │   │   ├── configuration-cache/
│   │   │   │   ├── 4y709znrotf8jugh2z4hi6yue/
│   │   │   │   │   ├── x0k0q07cpzquldnivxt1q1jv/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/4y709znrotf8jugh2z4hi6yue/x0k0q07cpzquldnivxt1q1jv/configuration-cache-report.html]
│   │   │   │   ├── 776cqg6727pn053kqtq5p5ce4/
│   │   │   │   │   ├── cytukaxbb6g0h4doz1k866sy8/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/776cqg6727pn053kqtq5p5ce4/cytukaxbb6g0h4doz1k866sy8/configuration-cache-report.html]
│   │   │   │   ├── afhxpttqos8i0dfuazsshilma/
│   │   │   │   │   ├── 22cofaq8odi9cdt8kkh6p4etj/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/afhxpttqos8i0dfuazsshilma/22cofaq8odi9cdt8kkh6p4etj/configuration-cache-report.html]
│   │   │   │   ├── b1v9tig786iwcqfq7vhp6ewvx/
│   │   │   │   │   ├── f11a7b60x7i7lemuvsdisliw0/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/b1v9tig786iwcqfq7vhp6ewvx/f11a7b60x7i7lemuvsdisliw0/configuration-cache-report.html]
│   │   │   │   ├── f25fbzom4d1wet9f7w45oash3/
│   │   │   │   │   ├── 9snj33wva79t3v9dlc40h87dt/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/f25fbzom4d1wet9f7w45oash3/9snj33wva79t3v9dlc40h87dt/configuration-cache-report.html]
│   │   │   │   ├── rcufm7m5joetcwnfp0ztcdza/
│   │   │   │   │   ├── 11gtu45fpepa59wo4kw0l56mh/
│   │   │   │   │   │   ├── configuration-cache-report.html [📂 extraction_target_project/build/reports/configuration-cache/rcufm7m5joetcwnfp0ztcdza/11gtu45fpepa59wo4kw0l56mh/configuration-cache-report.html]
│   │   │   ├── problems/
│   │   │   │   ├── problems-report.html [📂 extraction_target_project/build/reports/problems/problems-report.html]
│   │   ├── resources/
│   │   │   ├── main/
│   │   │   │   ├── plugin.yml [📂 extraction_target_project/build/resources/main/plugin.yml]
│   │   ├── tmp/
│   │   │   ├── compileJava/
│   │   │   │   ├── previous-compilation-data.bin [📂 extraction_target_project/build/tmp/compileJava/previous-compilation-data.bin]
│   │   │   ├── jar/
│   │   │   │   ├── MANIFEST.MF [📂 extraction_target_project/build/tmp/jar/MANIFEST.MF]
│   ├── build.gradle.kts [📂 extraction_target_project/build.gradle.kts]
│   ├── gradle/
│   │   ├── 8.5/
│   │   │   ├── checksums/
│   │   │   │   ├── checksums.lock [📂 extraction_target_project/gradle/8.5/checksums/checksums.lock]
│   │   │   │   ├── md5-checksums.bin [📂 extraction_target_project/gradle/8.5/checksums/md5-checksums.bin]
│   │   │   │   ├── sha1-checksums.bin [📂 extraction_target_project/gradle/8.5/checksums/sha1-checksums.bin]
│   │   │   ├── dependencies-accessors/
│   │   │   │   ├── dependencies-accessors.lock [📂 extraction_target_project/gradle/8.5/dependencies-accessors/dependencies-accessors.lock]
│   │   │   │   ├── gc.properties [📂 extraction_target_project/gradle/8.5/dependencies-accessors/gc.properties]
│   │   │   ├── fileChanges/
│   │   │   │   ├── last-build.bin [📂 extraction_target_project/gradle/8.5/fileChanges/last-build.bin]
│   │   │   ├── fileHashes/
│   │   │   │   ├── fileHashes.bin [📂 extraction_target_project/gradle/8.5/fileHashes/fileHashes.bin]
│   │   │   │   ├── fileHashes.lock [📂 extraction_target_project/gradle/8.5/fileHashes/fileHashes.lock]
│   │   │   ├── gc.properties [📂 extraction_target_project/gradle/8.5/gc.properties]
│   │   ├── 9.4.0/
│   │   │   ├── checksums/
│   │   │   │   ├── checksums.lock [📂 extraction_target_project/gradle/9.4.0/checksums/checksums.lock]
│   │   │   │   ├── md5-checksums.bin [📂 extraction_target_project/gradle/9.4.0/checksums/md5-checksums.bin]
│   │   │   │   ├── sha1-checksums.bin [📂 extraction_target_project/gradle/9.4.0/checksums/sha1-checksums.bin]
│   │   │   ├── executionHistory/
│   │   │   │   ├── executionHistory.bin [📂 extraction_target_project/gradle/9.4.0/executionHistory/executionHistory.bin]
│   │   │   │   ├── executionHistory.lock [📂 extraction_target_project/gradle/9.4.0/executionHistory/executionHistory.lock]
│   │   │   ├── fileChanges/
│   │   │   │   ├── last-build.bin [📂 extraction_target_project/gradle/9.4.0/fileChanges/last-build.bin]
│   │   │   ├── fileHashes/
│   │   │   │   ├── fileHashes.bin [📂 extraction_target_project/gradle/9.4.0/fileHashes/fileHashes.bin]
│   │   │   │   ├── fileHashes.lock [📂 extraction_target_project/gradle/9.4.0/fileHashes/fileHashes.lock]
│   │   │   │   ├── resourceHashesCache.bin [📂 extraction_target_project/gradle/9.4.0/fileHashes/resourceHashesCache.bin]
│   │   │   ├── gc.properties [📂 extraction_target_project/gradle/9.4.0/gc.properties]
│   │   ├── buildOutputCleanup/
│   │   │   ├── buildOutputCleanup.lock [📂 extraction_target_project/gradle/buildOutputCleanup/buildOutputCleanup.lock]
│   │   │   ├── cache.properties [📂 extraction_target_project/gradle/buildOutputCleanup/cache.properties]
│   │   │   ├── outputFiles.bin [📂 extraction_target_project/gradle/buildOutputCleanup/outputFiles.bin]
│   │   ├── configuration-cache/
│   │   │   ├── 29a584e6-8812-4ac3-860c-7f4956302415/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/gradle/configuration-cache/29a584e6-8812-4ac3-860c-7f4956302415/work.bin]
│   │   │   ├── 2e50130e-d504-420b-814b-ca43734c0176/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/gradle/configuration-cache/2e50130e-d504-420b-814b-ca43734c0176/work.bin]
│   │   │   ├── 2fb81455-8f38-43f9-bf55-5a1594a31e04/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/gradle/configuration-cache/2fb81455-8f38-43f9-bf55-5a1594a31e04/work.bin]
│   │   │   ├── 4y709znrotf8jugh2z4hi6yue/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/gradle/configuration-cache/4y709znrotf8jugh2z4hi6yue/candidates.bin]
│   │   │   ├── 6a7dc038-c222-4130-932f-de509d6a848f/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/gradle/configuration-cache/6a7dc038-c222-4130-932f-de509d6a848f/work.bin]
│   │   │   ├── 776cqg6727pn053kqtq5p5ce4/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/gradle/configuration-cache/776cqg6727pn053kqtq5p5ce4/candidates.bin]
│   │   │   ├── 9f315c7c-8405-4373-9085-15bac9a32d82/
│   │   │   │   ├── .globals.work.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/.globals.work.bin]
│   │   │   │   ├── .strings.work.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/.strings.work.bin]
│   │   │   │   ├── _.work.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/_.work.bin]
│   │   │   │   ├── buildfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/buildfingerprint.bin]
│   │   │   │   ├── classloaderscopes.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/classloaderscopes.bin]
│   │   │   │   ├── entry.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/entry.bin]
│   │   │   │   ├── projectfingerprint.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/projectfingerprint.bin]
│   │   │   │   ├── work.bin [📂 extraction_target_project/gradle/configuration-cache/9f315c7c-8405-4373-9085-15bac9a32d82/work.bin]
│   │   │   ├── afhxpttqos8i0dfuazsshilma/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/gradle/configuration-cache/afhxpttqos8i0dfuazsshilma/candidates.bin]
│   │   │   ├── configuration-cache.lock [📂 extraction_target_project/gradle/configuration-cache/configuration-cache.lock]
│   │   │   ├── f25fbzom4d1wet9f7w45oash3/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/gradle/configuration-cache/f25fbzom4d1wet9f7w45oash3/candidates.bin]
│   │   │   ├── gc.properties [📂 extraction_target_project/gradle/configuration-cache/gc.properties]
│   │   │   ├── rcufm7m5joetcwnfp0ztcdza/
│   │   │   │   ├── candidates.bin [📂 extraction_target_project/gradle/configuration-cache/rcufm7m5joetcwnfp0ztcdza/candidates.bin]
│   │   ├── file-system.probe [📂 extraction_target_project/gradle/file-system.probe]
│   │   ├── vcs-1/
│   │   │   ├── gc.properties [📂 extraction_target_project/gradle/vcs-1/gc.properties]
│   │   ├── wrapper/
│   │   │   ├── gradle-wrapper.jar [📂 extraction_target_project/gradle/wrapper/gradle-wrapper.jar]
│   │   │   ├── gradle-wrapper.properties [📂 extraction_target_project/gradle/wrapper/gradle-wrapper.properties]
│   ├── gradle.properties [📂 extraction_target_project/gradle.properties]
│   ├── gradlew [📂 extraction_target_project/gradlew]
│   ├── gradlew.bat [📂 extraction_target_project/gradlew.bat]
│   ├── plan.md [📂 extraction_target_project/plan.md]
│   ├── settings.gradle.kts [📂 extraction_target_project/settings.gradle.kts]
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/
│   │   │   │   │   ├── desertcore/
│   │   │   │   │   │   ├── DesertCore.java [📂 extraction_target_project/src/main/java/com/desertcore/DesertCore.java] -> [💡 📦 imp: com.desertcore.session.GameSessionManager, java.io.File, java.net.URL, java.util.ArrayList, java.util.List, org.bukkit.event.Listener, org.bukkit.plugin.java.JavaPlugin | 🎯 def onEnable() [L16-26] | 🎯 def registerAllListenersInPackage("com.desertcore.legacy") [L21-25] | 🎯 def getLogger() [L24-29] | 🎯 def onDisable() [L29-31] | 🎯 def getLogger() [L30-33] | 🎯 def getGameSessionManager() [L33-35] | 🎯 def registerAllListenersInPackage(String) [L40-83] | 🎯 def getServer() [L69-73] | 🎯 def getLogger() [L72-74] | 🎯 def getLogger() [L75-80] | 🎯 def getLogger() [L81-81]]
│   │   │   │   │   │   ├── DesertCoreTester.java [📂 extraction_target_project/src/main/java/com/desertcore/DesertCoreTester.java] -> [💡 📦 imp: java.io.File, java.lang.reflect.Constructor, java.net.URL, org.bukkit.event.Listener | 🧬 class DesertCoreTester [L12-90] | 🎯 def main(String[]) [L14-89]]
│   │   │   │   │   │   ├── legacy/
│   │   │   │   │   │   │   ├── deathevent.java [📂 extraction_target_project/src/main/java/com/desertcore/legacy/deathevent.java] -> [💡 📦 imp: com.desertcore.DesertCore, com.desertcore.Switch, com.desertcore.session.GameSession, java.io.File, java.io.IOException, java.nio.file.FileVisitResult, java.nio.file.Files, java.nio.file.Path, java.nio.file.SimpleFileVisitor, java.nio.file.attribute.BasicFileAttributes, java.util.HashSet, java.util.UUID, net.kyori.adventure.text.Component, net.kyori.adventure.text.event.ClickEvent, net.kyori.adventure.text.format.NamedTextColor, net.kyori.adventure.text.format.TextDecoration, org.bukkit.Bukkit, org.bukkit.GameMode, org.bukkit.Location, org.bukkit.World, org.bukkit.entity.Player, org.bukkit.event.EventHandler, org.bukkit.event.Listener, org.bukkit.event.entity.PlayerDeathEvent, org.bukkit.event.player.PlayerCommandPreprocessEvent, org.bukkit.event.player.PlayerJoinEvent, org.bukkit.event.player.PlayerMoveEvent, org.bukkit.event.player.PlayerRespawnEvent, org.bukkit.scheduler.BukkitRunnable, org.bukkit.scheduler.BukkitTask | 🧬 class deathevent [L35-223] | 🎯 def deathevent(DesertCore) [L40-42] | 🎯 def onPlayerDeath(PlayerDeathEvent) [L45-59] | 🎯 def onPlayerRespawn(PlayerRespawnEvent) [L62-84] | 🎯 def onPlayerMove(PlayerMoveEvent) [L87-149] | 🎯 def run() [L111-138] | 🎯 def onPlayerJoin(PlayerJoinEvent) [L152-173] | 🎯 def unloadAndDeleteInstance(previousWorldName) [L170-175] | 🎯 def unloadAndDeleteInstance(String) [L175-206] | 🎯 def deleteDirectoryNative(instanceDir.toPath() [L196-198] | 🎯 def deleteDirectoryNative(Path) [L208-222] | 🎯 def visitFile(Path, BasicFileAttributes) [L211-214] | 🎯 def postVisitDirectory(Path, IOException) [L217-220]]
│   │   │   │   │   │   │   ├── marendumbul.java [📂 extraction_target_project/src/main/java/com/desertcore/legacy/marendumbul.java] -> [💡 📦 imp: java.util.Random, org.bukkit.Bukkit, org.bukkit.Material, org.bukkit.World, org.bukkit.block.Block, org.bukkit.entity.Player, org.bukkit.event.EventHandler, org.bukkit.event.Listener, org.bukkit.event.player.PlayerJoinEvent | 🧬 class marendumbul [L13-62] | 🎯 def onPlayerJoin(PlayerJoinEvent) [L19-61]]
│   │   │   │   │   │   │   ├── samakportal.java [📂 extraction_target_project/src/main/java/com/desertcore/legacy/samakportal.java] -> [💡 📦 imp: com.desertcore.DesertCore, com.desertcore.Switch, com.desertcore.session.GameSession, java.io.File, java.io.IOException, java.nio.file.*, java.nio.file.attribute.BasicFileAttributes, java.util.logging.Level, net.kyori.adventure.text.Component, net.kyori.adventure.text.format.NamedTextColor, org.bukkit.Bukkit, org.bukkit.GameMode, org.bukkit.Location, org.bukkit.World, org.bukkit.WorldCreator, org.bukkit.entity.Player, org.bukkit.entity.Villager, org.bukkit.event.EventHandler, org.bukkit.event.Listener, org.bukkit.event.player.PlayerInteractEntityEvent | 🧬 class samakportal [L25-155] | 🎯 def samakportal(DesertCore) [L29-31] | 🎯 def onVillagerClick(PlayerInteractEntityEvent) [L34-119] | 🎯 def deleteDirectoryNative(instanceDir.toPath() [L81-89] | 🎯 def copyDirectoryNative(templateDir.toPath() [L85-92] | 🎯 def copyDirectoryNative(Path, Path) [L121-138] | 🎯 def preVisitDirectory(Path, BasicFileAttributes) [L124-130] | 🎯 def visitFile(Path, BasicFileAttributes) [L133-136] | 🎯 def deleteDirectoryNative(Path) [L140-154] | 🎯 def visitFile(Path, BasicFileAttributes) [L143-146] | 🎯 def postVisitDirectory(Path, IOException) [L149-152]]
│   │   │   │   │   │   ├── lobbycmd.java [📂 extraction_target_project/src/main/java/com/desertcore/lobbycmd.java] -> [💡 📦 imp: net.kyori.adventure.text.Component, net.kyori.adventure.text.format.NamedTextColor, org.bukkit.Bukkit, org.bukkit.GameMode, org.bukkit.Location, org.bukkit.World, org.bukkit.command.Command, org.bukkit.command.CommandExecutor, org.bukkit.command.CommandSender, org.bukkit.entity.Player, org.jetbrains.annotations.NotNull | 🧬 class lobbycmd [L15-49] | 🎯 def onCommand(@NotNull, @NotNull, @NotNull, @NotNull) [L18-48]]
│   │   │   │   │   │   ├── session/
│   │   │   │   │   │   │   ├── GameSession.java [📂 extraction_target_project/src/main/java/com/desertcore/session/GameSession.java] -> [💡 📦 imp: java.util.ArrayList, java.util.Collections, java.util.List, java.util.UUID, org.bukkit.Bukkit, org.bukkit.World, org.bukkit.scheduler.BukkitTask | 🧬 class GameSession [L11-71] | 🎯 def GameSession(String, UUID) [L21-26] | 🎯 def getSessionId() [L29-29] | 🎯 def getWorldName() [L30-30] | 🎯 def getPlayers() [L33-33] | 🎯 def getCurrentWave() [L35-35] | 🎯 def incrementWave() [L36-36] | 🎯 def isTerminating() [L38-38] | 🎯 def setTerminating(boolean) [L39-39] | 🎯 def setActiveTimer(BukkitTask) [L46-49] | 🎯 def clearActiveTimer() [L47-54] | 🎯 def clearActiveTimer() [L54-63] | 🎯 def getBukkitWorld() [L68-70]]
│   │   │   │   │   │   │   ├── GameSessionManager.java [📂 extraction_target_project/src/main/java/com/desertcore/session/GameSessionManager.java] -> [💡 📦 imp: java.util.HashMap, java.util.Map, java.util.UUID, org.bukkit.entity.Player, org.bukkit.plugin.java.JavaPlugin | 🧬 class GameSessionManager [L9-63] | 🎯 def GameSessionManager(JavaPlugin) [L16-18] | 🎯 def createSession(String, Player) [L23-31] | 🎯 def getSessionByPlayer(Player) [L36-38] | 🎯 def getSessionByWorld(String) [L43-45] | 🎯 def terminateSession(String) [L50-62]]
│   │   │   │   │   │   ├── Switch.java [📂 extraction_target_project/src/main/java/com/desertcore/Switch.java] -> [🎯 def Switch() [L10-10]]
│   │   │   ├── resources/
│   │   │   │   ├── plugin.yml [📂 extraction_target_project/src/main/resources/plugin.yml]
├── oldplan/
│   ├── agent_plan1.md [📂 oldplan/agent_plan1.md]
│   ├── agent_plan2.md [📂 oldplan/agent_plan2.md]
│   ├── agent_plan3.md [📂 oldplan/agent_plan3.md]
├── prompt.md [📂 prompt.md]
├── scan_debug.txt [📂 scan_debug.txt]
├── start.py [📂 start.py] -> [💡 📦 imp: os, pathlib, shutil, stat, subprocess, sys, time | 🎯 def get_best_python() [L34-50] | 🎯 def auto_install_dependencies() [L59-80] | 🎯 def main() [L82-202]]
├── System Prompt.md [📂 System Prompt.md]
├── tools/
│   ├── universal_indexer/
│   │   ├── agent_navigator.py [📂 tools/universal_indexer/agent_navigator.py] -> [💡 📦 imp: json, pathlib, re, switch, sys, tkinter, traceback | 🧬 class SemanticNavigator [L11-253] |     └─ def __init__() [L12-39] |     └─ def _load_database() [L41-48] |     └─ def extract_multi_slices() [L50-253] | 🧬 class JjapCursorNavigatorGUI [L258-371] |     └─ def __init__() [L259-309] |     └─ def execute_slicing_pipeline() [L311-353] |     └─ def manual_export_file() [L355-371]]
│   │   │     ├── 🔑 [REGISTRY]: "SemanticNavigator"
│   │   │     ├── 🔑 [REGISTRY]: "JjapCursorNavigatorGUI"
│   │   ├── context_builder.py [📂 tools/universal_indexer/context_builder.py] -> [💡 📦 imp: os, pathlib | 🧬 class ContextBuilder [L13-107] |     └─ def __init__() [L16-18] |     └─ def read_and_clean_file() [L20-78] |     └─ def assemble_ai_prompt() [L80-107]]
│   │   ├── core_parsers/
│   │   │   ├── __init__.py [📂 tools/universal_indexer/core_parsers/__init__.py]
│   │   │   ├── cs_parser.py [📂 tools/universal_indexer/core_parsers/cs_parser.py]
│   │   │   ├── java_parser.py [📂 tools/universal_indexer/core_parsers/java_parser.py] -> [💡 📦 imp: hashlib, pathlib, re | 🎯 def log() [L8-10] | 🎯 def _find_matching_curly_brace() [L12-34] | 🎯 def extract_symbols() [L36-193]]
│   │   │   ├── js_parser.py [📂 tools/universal_indexer/core_parsers/js_parser.py]
│   │   │   ├── json_parser.py [📂 tools/universal_indexer/core_parsers/json_parser.py] -> [💡 📦 imp: hashlib, json, pathlib | 🎯 def extract_symbols() [L5-97]]
│   │   │   ├── py_parser.py [📂 tools/universal_indexer/core_parsers/py_parser.py] -> [💡 📦 imp: ast, hashlib, pathlib | 🎯 def extract_symbols() [L5-158]]
│   │   ├── create_ai_map.py [📂 tools/universal_indexer/create_ai_map.py] -> [💡 📦 imp: ast, json, os, pathlib, tools.universal_indexer.switch | 🎯 def load_jjap_context() [L41-60] | 🎯 def collect_target_files() [L63-122] | 🎯 def load_registry() [L125-162] | 🎯 def load_protocols() [L165-187] | 🎯 def parse_protocols_and_registries() [L194-247] | 🎯 def main() [L250-340] | 🎯 def generate_ai_optimized_map() [L346-348]]
│   │   ├── indexer.py [📂 tools/universal_indexer/indexer.py] -> [💡 📦 imp: ast, hashlib, importlib.util, json, os, pathlib, switch, typing | 🎯 def log() [L18-20] | 🧬 class AdvancedIndexerV2 [L32-199] |     └─ def __init__() [L37-47] |     └─ def _auto_load_parsers() [L49-80] |     └─ def scan_project() [L82-121] |     └─ def index_file() [L123-162] |     └─ def save_index_data() [L164-199]]
│   │   │     ├── 🔑 [REGISTRY]: "AdvancedIndexerV2"
│   │   ├── jjap_lookup.py [📂 tools/universal_indexer/jjap_lookup.py] -> [💡 📦 imp: argparse, json, pathlib, sys | 🎯 def load_json() [L17-22] | 🎯 def lookup_symbol() [L24-51] | 🎯 def show_skeleton() [L53-69]]
│   │   ├── jjap_retriever.py [📂 tools/universal_indexer/jjap_retriever.py] -> [💡 📦 imp: json, os, pathlib, sys, typing | 🧬 class JjapRetriever [L9-129] |     └─ def __init__() [L16-21] |     └─ def _load_symbols() [L23-37] |     └─ def retrieve_symbol() [L39-98] |     └─ def _find_best_match() [L100-117] |     └─ def _safe_truncate() [L119-129] | 🎯 def main() [L132-140]]
│   │   │     ├── 🔑 [REGISTRY]: "JjapRetriever"
│   │   ├── jjap_watcher.py [📂 tools/universal_indexer/jjap_watcher.py] -> [💡 📦 imp: importlib.util, os, pathlib, sys, time, traceback, watchdog.observers, watchdog.observers.polling | 🎯 def import_file_directly() [L25-33] | 🎯 def run_pipeline() [L35-78] | 🧬 class CodeChangeHandler [L81-104] |     └─ def __init__() [L82-84] |     └─ def dispatch() [L86-104] | 🎯 def main() [L106-132]]
│   │   │     ├── 🔑 [REGISTRY]: "CodeChangeHandler"
│   │   ├── README.md [📂 tools/universal_indexer/README.md]
│   │   ├── rule.txt [📂 tools/universal_indexer/rule.txt]
│   │   ├── switch.py [📂 tools/universal_indexer/switch.py]
│   │   ├── update_map.py [📂 tools/universal_indexer/update_map.py] -> [💡 📦 imp: json, pathlib | 🎯 def update_map() [L4-94]]
