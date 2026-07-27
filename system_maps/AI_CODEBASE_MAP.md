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
│   │   │   │   ├── yourstudio/
│   │   │   │   │   ├── coredefense/
│   │   │   │   │   │   ├── bootstrap/
│   │   │   │   │   │   │   ├── ModuleInitializer.class [📂 extraction_target_project/bin/main/com/yourstudio/coredefense/bootstrap/ModuleInitializer.class]
│   │   │   │   │   │   ├── common/
│   │   │   │   │   │   │   ├── contract/
│   │   │   │   │   │   │   │   ├── EnergyConsumer.class [📂 extraction_target_project/bin/main/com/yourstudio/coredefense/common/contract/EnergyConsumer.class]
│   │   │   │   │   │   │   │   ├── EnergyPriority.class [📂 extraction_target_project/bin/main/com/yourstudio/coredefense/common/contract/EnergyPriority.class]
│   │   │   ├── config/
│   │   │   │   ├── core.yml [📂 extraction_target_project/bin/main/config/core.yml]
│   │   │   │   ├── core_visual_stages.yml [📂 extraction_target_project/bin/main/config/core_visual_stages.yml]
│   │   │   │   ├── models/
│   │   │   │   │   ├── animation_triggers.yml [📂 extraction_target_project/bin/main/config/models/animation_triggers.yml]
│   │   │   │   ├── npc/
│   │   │   │   │   ├── npc_job_promotions.yml [📂 extraction_target_project/bin/main/config/npc/npc_job_promotions.yml]
│   │   │   │   │   ├── npc_traits.yml [📂 extraction_target_project/bin/main/config/npc/npc_traits.yml]
│   │   │   │   │   ├── resonance_thresholds.yml [📂 extraction_target_project/bin/main/config/npc/resonance_thresholds.yml]
│   │   │   │   ├── player_classes/
│   │   │   │   │   ├── classes.yml [📂 extraction_target_project/bin/main/config/player_classes/classes.yml]
│   │   │   │   │   ├── specializations.yml [📂 extraction_target_project/bin/main/config/player_classes/specializations.yml]
│   │   │   │   ├── progression/
│   │   │   │   │   ├── score_weights.yml [📂 extraction_target_project/bin/main/config/progression/score_weights.yml]
│   │   │   │   ├── waves/
│   │   │   │   │   ├── boss_waves.yml [📂 extraction_target_project/bin/main/config/waves/boss_waves.yml]
│   │   │   │   │   ├── wave_definitions.yml [📂 extraction_target_project/bin/main/config/waves/wave_definitions.yml]
│   │   │   ├── editor_objects.json [📂 extraction_target_project/bin/main/editor_objects.json]
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
│   ├── checklist.md [📂 extraction_target_project/checklist.md]
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
│   ├── mincraft_javacode_map.code-workspace [📂 extraction_target_project/mincraft_javacode_map.code-workspace]
│   ├── plan.md [📂 extraction_target_project/plan.md]
│   ├── settings.gradle.kts [📂 extraction_target_project/settings.gradle.kts]
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/
│   │   │   │   │   ├── yourstudio/
│   │   │   │   │   │   ├── coredefense/
│   │   │   │   │   │   │   ├── bootstrap/
│   │   │   │   │   │   │   │   ├── CommandRegistrar.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/bootstrap/CommandRegistrar.java]
│   │   │   │   │   │   │   │   ├── ListenerRegistrar.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/bootstrap/ListenerRegistrar.java]
│   │   │   │   │   │   │   │   ├── ModuleInitializer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/bootstrap/ModuleInitializer.java] -> [🧬 class ModuleInitializer [L2-2]]
│   │   │   │   │   │   │   ├── combat/
│   │   │   │   │   │   │   │   ├── damage/
│   │   │   │   │   │   │   │   │   ├── CombatDamageService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/damage/CombatDamageService.java]
│   │   │   │   │   │   │   │   │   ├── DamageCalculator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/damage/DamageCalculator.java]
│   │   │   │   │   │   │   │   │   ├── DamageModifier.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/damage/DamageModifier.java]
│   │   │   │   │   │   │   │   │   ├── DamageSource.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/damage/DamageSource.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── EntityDamagedByGameEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/event/EntityDamagedByGameEvent.java]
│   │   │   │   │   │   │   │   │   ├── WeaponFiredEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/event/WeaponFiredEvent.java]
│   │   │   │   │   │   │   │   ├── melee/
│   │   │   │   │   │   │   │   │   ├── MeleeAttackHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/melee/MeleeAttackHandler.java]
│   │   │   │   │   │   │   │   │   ├── MeleeWeapon.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/melee/MeleeWeapon.java]
│   │   │   │   │   │   │   │   ├── vfx/
│   │   │   │   │   │   │   │   │   ├── WeaponVfxService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/vfx/WeaponVfxService.java]
│   │   │   │   │   │   │   │   ├── weapon/
│   │   │   │   │   │   │   │   │   ├── AbstractFirearm.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/AbstractFirearm.java]
│   │   │   │   │   │   │   │   │   ├── ammo/
│   │   │   │   │   │   │   │   │   │   ├── AmmoInventory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/ammo/AmmoInventory.java]
│   │   │   │   │   │   │   │   │   │   ├── AmmoType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/ammo/AmmoType.java]
│   │   │   │   │   │   │   │   │   ├── BurstFireFirearm.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/BurstFireFirearm.java]
│   │   │   │   │   │   │   │   │   ├── projectile/
│   │   │   │   │   │   │   │   │   │   ├── ArcProjectile.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/projectile/ArcProjectile.java]
│   │   │   │   │   │   │   │   │   │   ├── BulletProjectile.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/projectile/BulletProjectile.java]
│   │   │   │   │   │   │   │   │   │   ├── ProjectileFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/projectile/ProjectileFactory.java]
│   │   │   │   │   │   │   │   │   │   ├── ProjectileType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/projectile/ProjectileType.java]
│   │   │   │   │   │   │   │   │   ├── SingleShotFirearm.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/SingleShotFirearm.java]
│   │   │   │   │   │   │   │   │   ├── SniperRifle.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/SniperRifle.java]
│   │   │   │   │   │   │   │   │   ├── strategy/
│   │   │   │   │   │   │   │   │   │   ├── BurstFireStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/strategy/BurstFireStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── FireModeStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/strategy/FireModeStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── SingleShotStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/strategy/SingleShotStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── SniperShotStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/strategy/SniperShotStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── SpreadPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/strategy/SpreadPolicy.java]
│   │   │   │   │   │   │   │   │   ├── Weapon.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/Weapon.java]
│   │   │   │   │   │   │   │   │   ├── WeaponAcquisitionPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponAcquisitionPolicy.java]
│   │   │   │   │   │   │   │   │   ├── WeaponAttachment.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponAttachment.java]
│   │   │   │   │   │   │   │   │   ├── WeaponDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponDefinition.java]
│   │   │   │   │   │   │   │   │   ├── WeaponFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponFactory.java]
│   │   │   │   │   │   │   │   │   ├── WeaponInputHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponInputHandler.java]
│   │   │   │   │   │   │   │   │   ├── WeaponRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/combat/weapon/WeaponRegistry.java]
│   │   │   │   │   │   │   ├── command/
│   │   │   │   │   │   │   │   ├── CoreDefenseCommand.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/command/CoreDefenseCommand.java]
│   │   │   │   │   │   │   │   ├── sub/
│   │   │   │   │   │   │   │   │   ├── AdminReloadSubcommand.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/command/sub/AdminReloadSubcommand.java]
│   │   │   │   │   │   │   │   │   ├── StartGameSubcommand.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/command/sub/StartGameSubcommand.java]
│   │   │   │   │   │   │   ├── common/
│   │   │   │   │   │   │   │   ├── config/
│   │   │   │   │   │   │   │   │   ├── ConfigLoader.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/config/ConfigLoader.java]
│   │   │   │   │   │   │   │   │   ├── ConfigParser.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/config/ConfigParser.java]
│   │   │   │   │   │   │   │   │   ├── ConfigService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/config/ConfigService.java]
│   │   │   │   │   │   │   │   │   ├── ReloadableConfig.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/config/ReloadableConfig.java]
│   │   │   │   │   │   │   │   ├── contract/
│   │   │   │   │   │   │   │   │   ├── EnergyConsumer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/contract/EnergyConsumer.java] -> [🧬 class EnergyConsumer [L3-6] | 🎯 def getEnergyDemand() [L4-4] | 🎯 def onEnergyAllocated(int) [L5-5]]
│   │   │   │   │   │   │   │   │   ├── EnergyPriority.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/contract/EnergyPriority.java] -> [🧬 class EnergyPriority [L3-8]]
│   │   │   │   │   │   │   │   │   ├── Healable.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/contract/Healable.java]
│   │   │   │   │   │   │   │   │   ├── ModelAnchor.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/contract/ModelAnchor.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── AbstractGameEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/event/AbstractGameEvent.java]
│   │   │   │   │   │   │   │   │   ├── GameListener.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/event/GameListener.java]
│   │   │   │   │   │   │   │   ├── interfaces/
│   │   │   │   │   │   │   │   │   ├── Identifiable.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/interfaces/Identifiable.java]
│   │   │   │   │   │   │   │   ├── perf/
│   │   │   │   │   │   │   │   │   ├── PerformanceMonitor.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/perf/PerformanceMonitor.java]
│   │   │   │   │   │   │   │   ├── registry/
│   │   │   │   │   │   │   │   │   ├── AbstractRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/registry/AbstractRegistry.java]
│   │   │   │   │   │   │   │   │   ├── Registry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/registry/Registry.java]
│   │   │   │   │   │   │   │   │   ├── RegistryKey.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/registry/RegistryKey.java]
│   │   │   │   │   │   │   │   ├── result/
│   │   │   │   │   │   │   │   │   ├── ActionResult.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/result/ActionResult.java]
│   │   │   │   │   │   │   │   ├── scheduling/
│   │   │   │   │   │   │   │   │   ├── GameScheduler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/scheduling/GameScheduler.java]
│   │   │   │   │   │   │   │   ├── util/
│   │   │   │   │   │   │   │   │   ├── CooldownTracker.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/util/CooldownTracker.java]
│   │   │   │   │   │   │   │   │   ├── MathUtils.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/util/MathUtils.java]
│   │   │   │   │   │   │   │   │   ├── ParticleUtils.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/util/ParticleUtils.java]
│   │   │   │   │   │   │   │   │   ├── RayTraceUtil.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/util/RayTraceUtil.java]
│   │   │   │   │   │   │   │   │   ├── VfxThrottleService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/common/util/VfxThrottleService.java]
│   │   │   │   │   │   │   ├── core/
│   │   │   │   │   │   │   │   ├── CoreEnergyManager.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreEnergyManager.java]
│   │   │   │   │   │   │   │   ├── CoreEntity.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreEntity.java]
│   │   │   │   │   │   │   │   ├── CoreLevel.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreLevel.java]
│   │   │   │   │   │   │   │   ├── CoreLevelListener.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreLevelListener.java]
│   │   │   │   │   │   │   │   ├── CoreLevelRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreLevelRegistry.java]
│   │   │   │   │   │   │   │   ├── CoreLevelUpService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreLevelUpService.java]
│   │   │   │   │   │   │   │   ├── CoreState.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreState.java]
│   │   │   │   │   │   │   │   ├── CoreStateMachine.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreStateMachine.java]
│   │   │   │   │   │   │   │   ├── CoreUnlockConfig.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreUnlockConfig.java]
│   │   │   │   │   │   │   │   ├── CoreUnlockManager.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreUnlockManager.java]
│   │   │   │   │   │   │   │   ├── CoreVisualFeedbackService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/CoreVisualFeedbackService.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── CoreDamagedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/event/CoreDamagedEvent.java]
│   │   │   │   │   │   │   │   │   ├── CoreDestroyedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/event/CoreDestroyedEvent.java]
│   │   │   │   │   │   │   │   │   ├── CoreLeveledUpEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/event/CoreLeveledUpEvent.java]
│   │   │   │   │   │   │   │   │   ├── CoreSystemUnlockedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/event/CoreSystemUnlockedEvent.java]
│   │   │   │   │   │   │   │   ├── SchematicPasteService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/core/SchematicPasteService.java]
│   │   │   │   │   │   │   ├── CoreDefensePlugin.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/CoreDefensePlugin.java]
│   │   │   │   │   │   │   ├── data/
│   │   │   │   │   │   │   │   ├── pipeline/
│   │   │   │   │   │   │   │   │   ├── JsonSerializationPipeline.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/data/pipeline/JsonSerializationPipeline.java]
│   │   │   │   │   │   │   │   ├── storage/
│   │   │   │   │   │   │   │   │   ├── VariableStorage.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/data/storage/VariableStorage.java]
│   │   │   │   │   │   │   ├── drone/
│   │   │   │   │   │   │   │   ├── CombatDrone.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/drone/CombatDrone.java]
│   │   │   │   │   │   │   │   ├── DroneCapacityPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/drone/DroneCapacityPolicy.java]
│   │   │   │   │   │   │   │   ├── DroneEntity.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/drone/DroneEntity.java]
│   │   │   │   │   │   │   ├── entity/
│   │   │   │   │   │   │   │   ├── base/
│   │   │   │   │   │   │   │   │   ├── BaseEntity.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/entity/base/BaseEntity.java]
│   │   │   │   │   │   │   │   │   ├── EntityRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/entity/base/EntityRegistry.java]
│   │   │   │   │   │   │   ├── gui/
│   │   │   │   │   │   │   │   ├── GameMenu.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/GameMenu.java]
│   │   │   │   │   │   │   │   ├── MenuFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/MenuFactory.java]
│   │   │   │   │   │   │   │   ├── menus/
│   │   │   │   │   │   │   │   │   ├── MetaUpgradeMenu.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/menus/MetaUpgradeMenu.java]
│   │   │   │   │   │   │   │   │   ├── NpcReplaceMenu.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/menus/NpcReplaceMenu.java]
│   │   │   │   │   │   │   │   │   ├── RecruitMenu.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/menus/RecruitMenu.java]
│   │   │   │   │   │   │   │   │   ├── SkillTreeMenu.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/gui/menus/SkillTreeMenu.java]
│   │   │   │   │   │   │   ├── mining/
│   │   │   │   │   │   │   │   ├── AutoMiningTicker.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/AutoMiningTicker.java]
│   │   │   │   │   │   │   │   ├── ClickMiningHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/ClickMiningHandler.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── OreMinedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/event/OreMinedEvent.java]
│   │   │   │   │   │   │   │   │   ├── OreUnlockedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/event/OreUnlockedEvent.java]
│   │   │   │   │   │   │   │   ├── MiningEfficiencyPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/MiningEfficiencyPolicy.java]
│   │   │   │   │   │   │   │   ├── MiningSession.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/MiningSession.java]
│   │   │   │   │   │   │   │   ├── MiningSessionManager.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/MiningSessionManager.java]
│   │   │   │   │   │   │   │   ├── OreRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/OreRegistry.java]
│   │   │   │   │   │   │   │   ├── OreType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mining/OreType.java]
│   │   │   │   │   │   │   ├── mob/
│   │   │   │   │   │   │   │   ├── ai/
│   │   │   │   │   │   │   │   │   ├── PathingStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/ai/PathingStrategy.java]
│   │   │   │   │   │   │   │   │   ├── TargetSelector.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/ai/TargetSelector.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── MonsterKilledEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/event/MonsterKilledEvent.java]
│   │   │   │   │   │   │   │   ├── MonsterAI.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/MonsterAI.java]
│   │   │   │   │   │   │   │   ├── MonsterDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/MonsterDefinition.java]
│   │   │   │   │   │   │   │   ├── MonsterFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/MonsterFactory.java]
│   │   │   │   │   │   │   │   ├── MonsterRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/mob/MonsterRegistry.java]
│   │   │   │   │   │   │   ├── npc/
│   │   │   │   │   │   │   │   ├── death/
│   │   │   │   │   │   │   │   │   ├── LegacyTransferService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/death/LegacyTransferService.java]
│   │   │   │   │   │   │   │   │   ├── NpcDeathHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/death/NpcDeathHandler.java]
│   │   │   │   │   │   │   │   │   ├── ReviveService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/death/ReviveService.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── NpcDiedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/event/NpcDiedEvent.java]
│   │   │   │   │   │   │   │   │   ├── NpcLeveledUpEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/event/NpcLeveledUpEvent.java]
│   │   │   │   │   │   │   │   │   ├── NpcRecruitedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/event/NpcRecruitedEvent.java]
│   │   │   │   │   │   │   │   ├── GameNpcFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/GameNpcFactory.java]
│   │   │   │   │   │   │   │   ├── NpcCapacityPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcCapacityPolicy.java]
│   │   │   │   │   │   │   │   ├── NpcEntity.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcEntity.java]
│   │   │   │   │   │   │   │   ├── NpcOwnershipPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcOwnershipPolicy.java]
│   │   │   │   │   │   │   │   ├── NpcRole.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcRole.java]
│   │   │   │   │   │   │   │   ├── NpcState.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcState.java]
│   │   │   │   │   │   │   │   ├── NpcStateMachine.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcStateMachine.java]
│   │   │   │   │   │   │   │   ├── NpcStatSheet.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/NpcStatSheet.java]
│   │   │   │   │   │   │   │   ├── recruit/
│   │   │   │   │   │   │   │   │   ├── RecruitmentService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/recruit/RecruitmentService.java]
│   │   │   │   │   │   │   │   │   ├── RecruitOffer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/recruit/RecruitOffer.java]
│   │   │   │   │   │   │   │   │   ├── RecruitPool.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/recruit/RecruitPool.java]
│   │   │   │   │   │   │   │   │   ├── RecruitPoolWeightTable.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/recruit/RecruitPoolWeightTable.java]
│   │   │   │   │   │   │   │   ├── safezone/
│   │   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   │   ├── SafeZoneBreachedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/safezone/event/SafeZoneBreachedEvent.java]
│   │   │   │   │   │   │   │   │   ├── SafeZoneService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/safezone/SafeZoneService.java]
│   │   │   │   │   │   │   │   ├── trait/
│   │   │   │   │   │   │   │   │   ├── NpcCollaborationUnlockService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/trait/NpcCollaborationUnlockService.java]
│   │   │   │   │   │   │   │   │   ├── NpcTrait.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/trait/NpcTrait.java]
│   │   │   │   │   │   │   │   │   ├── ResonanceCalculator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/trait/ResonanceCalculator.java]
│   │   │   │   │   │   │   │   │   ├── TraitRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/trait/TraitRegistry.java]
│   │   │   │   │   │   │   │   ├── vocation/
│   │   │   │   │   │   │   │   │   ├── NpcVocation.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/vocation/NpcVocation.java]
│   │   │   │   │   │   │   │   │   ├── NpcVocationPromotion.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/vocation/NpcVocationPromotion.java]
│   │   │   │   │   │   │   │   │   ├── NpcVocationSkillTree.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/npc/vocation/NpcVocationSkillTree.java]
│   │   │   │   │   │   │   ├── persistence/
│   │   │   │   │   │   │   │   ├── DataStoreType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/DataStoreType.java]
│   │   │   │   │   │   │   │   ├── FailedSaveRetryQueue.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/FailedSaveRetryQueue.java]
│   │   │   │   │   │   │   │   ├── file/
│   │   │   │   │   │   │   │   │   ├── JsonSessionSnapshotRepository.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/file/JsonSessionSnapshotRepository.java]
│   │   │   │   │   │   │   │   │   ├── YamlPlayerRepository.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/file/YamlPlayerRepository.java]
│   │   │   │   │   │   │   │   ├── PersistenceService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/PersistenceService.java]
│   │   │   │   │   │   │   │   ├── PlayerDataLock.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/PlayerDataLock.java]
│   │   │   │   │   │   │   │   ├── Repository.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/Repository.java]
│   │   │   │   │   │   │   │   ├── sql/
│   │   │   │   │   │   │   │   │   ├── SqlPlayerRepository.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/sql/SqlPlayerRepository.java]
│   │   │   │   │   │   │   │   │   ├── SqlSchemaMigrator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/persistence/sql/SqlSchemaMigrator.java]
│   │   │   │   │   │   │   ├── playerclass/
│   │   │   │   │   │   │   │   ├── builder/
│   │   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   │   ├── OverclockActivatedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/builder/event/OverclockActivatedEvent.java]
│   │   │   │   │   │   │   │   │   │   ├── OverheatTriggeredEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/builder/event/OverheatTriggeredEvent.java]
│   │   │   │   │   │   │   │   │   ├── OverclockPenaltyHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/builder/OverclockPenaltyHandler.java]
│   │   │   │   │   │   │   │   │   ├── OverclockSkill.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/builder/OverclockSkill.java]
│   │   │   │   │   │   │   │   ├── ClassDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/ClassDefinition.java]
│   │   │   │   │   │   │   │   ├── ClassRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/ClassRegistry.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── ClassSelectedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/event/ClassSelectedEvent.java]
│   │   │   │   │   │   │   │   │   ├── SkillUsedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/event/SkillUsedEvent.java]
│   │   │   │   │   │   │   │   ├── heal/
│   │   │   │   │   │   │   │   │   ├── HealStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/heal/HealStrategy.java]
│   │   │   │   │   │   │   │   ├── PlayerClass.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/PlayerClass.java]
│   │   │   │   │   │   │   │   ├── skill/
│   │   │   │   │   │   │   │   │   ├── ActiveSkill.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/ActiveSkill.java]
│   │   │   │   │   │   │   │   │   ├── PassiveSkill.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/PassiveSkill.java]
│   │   │   │   │   │   │   │   │   ├── Skill.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/Skill.java]
│   │   │   │   │   │   │   │   │   ├── SkillInputHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/SkillInputHandler.java]
│   │   │   │   │   │   │   │   │   ├── SkillNode.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/SkillNode.java]
│   │   │   │   │   │   │   │   │   ├── SkillTree.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/SkillTree.java]
│   │   │   │   │   │   │   │   │   ├── UltimateCooldownPool.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/UltimateCooldownPool.java]
│   │   │   │   │   │   │   │   │   ├── UltimateSkill.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/skill/UltimateSkill.java]
│   │   │   │   │   │   │   │   ├── specialization/
│   │   │   │   │   │   │   │   │   ├── Specialization.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/playerclass/specialization/Specialization.java]
│   │   │   │   │   │   │   ├── progression/
│   │   │   │   │   │   │   │   ├── MetaCurrency.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/MetaCurrency.java]
│   │   │   │   │   │   │   │   ├── MetaUpgrade.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/MetaUpgrade.java]
│   │   │   │   │   │   │   │   ├── MetaUpgradeNode.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/MetaUpgradeNode.java]
│   │   │   │   │   │   │   │   ├── MetaUpgradeTree.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/MetaUpgradeTree.java]
│   │   │   │   │   │   │   │   ├── PlayerProgressionData.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/PlayerProgressionData.java]
│   │   │   │   │   │   │   │   ├── ProgressionService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/ProgressionService.java]
│   │   │   │   │   │   │   │   ├── ProgressionStatsCollector.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/ProgressionStatsCollector.java]
│   │   │   │   │   │   │   │   ├── ScoreCalculator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/ScoreCalculator.java]
│   │   │   │   │   │   │   │   ├── UpgradeEffectType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/progression/UpgradeEffectType.java]
│   │   │   │   │   │   │   ├── render/
│   │   │   │   │   │   │   │   ├── animation/
│   │   │   │   │   │   │   │   │   ├── AnimationDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/AnimationDefinition.java]
│   │   │   │   │   │   │   │   │   ├── AnimationLodPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/AnimationLodPolicy.java]
│   │   │   │   │   │   │   │   │   ├── AnimationPlayer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/AnimationPlayer.java]
│   │   │   │   │   │   │   │   │   ├── AnimationRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/AnimationRegistry.java]
│   │   │   │   │   │   │   │   │   ├── AnimationTicker.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/AnimationTicker.java]
│   │   │   │   │   │   │   │   │   ├── BoneKeyframeTrack.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/BoneKeyframeTrack.java]
│   │   │   │   │   │   │   │   │   ├── BoneTransformComposer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/BoneTransformComposer.java]
│   │   │   │   │   │   │   │   │   ├── InterpolationType.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/InterpolationType.java]
│   │   │   │   │   │   │   │   │   ├── Keyframe.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/Keyframe.java]
│   │   │   │   │   │   │   │   │   ├── TransformInterpolator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/TransformInterpolator.java]
│   │   │   │   │   │   │   │   │   ├── trigger/
│   │   │   │   │   │   │   │   │   │   ├── AnimationTriggerListener.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/trigger/AnimationTriggerListener.java]
│   │   │   │   │   │   │   │   │   │   ├── AnimationTriggerMapping.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/animation/trigger/AnimationTriggerMapping.java]
│   │   │   │   │   │   │   │   ├── asset/
│   │   │   │   │   │   │   │   │   ├── ModelAssetValidator.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/asset/ModelAssetValidator.java]
│   │   │   │   │   │   │   │   ├── display/
│   │   │   │   │   │   │   │   │   ├── DisplayModelFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/display/DisplayModelFactory.java]
│   │   │   │   │   │   │   │   │   ├── DisplayModelInstance.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/display/DisplayModelInstance.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── AnimationStateChangedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/event/AnimationStateChangedEvent.java]
│   │   │   │   │   │   │   │   │   ├── ModelSpawnedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/event/ModelSpawnedEvent.java]
│   │   │   │   │   │   │   │   ├── model/
│   │   │   │   │   │   │   │   │   ├── AnimatedJavaAssetLoader.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/model/AnimatedJavaAssetLoader.java]
│   │   │   │   │   │   │   │   │   ├── BoneDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/model/BoneDefinition.java]
│   │   │   │   │   │   │   │   │   ├── ModelDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/model/ModelDefinition.java]
│   │   │   │   │   │   │   │   │   ├── ModelRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/model/ModelRegistry.java]
│   │   │   │   │   │   │   │   ├── ModelRenderer.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/render/ModelRenderer.java]
│   │   │   │   │   │   │   ├── session/
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── GameSessionEndedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/session/event/GameSessionEndedEvent.java]
│   │   │   │   │   │   │   │   ├── GameSession.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/session/GameSession.java]
│   │   │   │   │   │   │   │   ├── GameSessionManager.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/session/GameSessionManager.java]
│   │   │   │   │   │   │   │   ├── GameSessionState.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/session/GameSessionState.java]
│   │   │   │   │   │   │   │   ├── GameTeam.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/session/GameTeam.java]
│   │   │   │   │   │   │   ├── structure/
│   │   │   │   │   │   │   │   ├── BuildableZoneService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/BuildableZoneService.java]
│   │   │   │   │   │   │   │   ├── BuildPermissionPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/BuildPermissionPolicy.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── StructureDestroyedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/event/StructureDestroyedEvent.java]
│   │   │   │   │   │   │   │   │   ├── StructurePlacedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/event/StructurePlacedEvent.java]
│   │   │   │   │   │   │   │   ├── StructurePlacementService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/StructurePlacementService.java]
│   │   │   │   │   │   │   │   ├── StructureRegistry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/StructureRegistry.java]
│   │   │   │   │   │   │   │   ├── turret/
│   │   │   │   │   │   │   │   │   ├── targeting/
│   │   │   │   │   │   │   │   │   │   ├── HighestThreatTargetStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/targeting/HighestThreatTargetStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── LowestHpTargetStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/targeting/LowestHpTargetStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── NearestTargetStrategy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/targeting/NearestTargetStrategy.java]
│   │   │   │   │   │   │   │   │   │   ├── SpatialIndex.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/targeting/SpatialIndex.java]
│   │   │   │   │   │   │   │   │   │   ├── TurretTargeting.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/targeting/TurretTargeting.java]
│   │   │   │   │   │   │   │   │   ├── Turret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/Turret.java]
│   │   │   │   │   │   │   │   │   ├── TurretAmmoSupply.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/TurretAmmoSupply.java]
│   │   │   │   │   │   │   │   │   ├── TurretDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/TurretDefinition.java]
│   │   │   │   │   │   │   │   │   ├── TurretFactory.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/TurretFactory.java]
│   │   │   │   │   │   │   │   │   ├── types/
│   │   │   │   │   │   │   │   │   │   ├── ArrowSentryTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/ArrowSentryTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── AutoCannonTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/AutoCannonTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── BuffTowerTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/BuffTowerTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── FlamethrowerTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/FlamethrowerTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── LightGunTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/LightGunTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── MinigunTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/MinigunTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── MissileTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/MissileTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── NukeMissileTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/NukeMissileTurret.java]
│   │   │   │   │   │   │   │   │   │   ├── SlingshotTurret.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/turret/types/SlingshotTurret.java]
│   │   │   │   │   │   │   │   ├── wall/
│   │   │   │   │   │   │   │   │   ├── WallDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/wall/WallDefinition.java]
│   │   │   │   │   │   │   │   │   ├── WallInstance.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/wall/WallInstance.java]
│   │   │   │   │   │   │   │   │   ├── WallMaterialTier.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/wall/WallMaterialTier.java]
│   │   │   │   │   │   │   │   │   ├── WallModule.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/structure/wall/WallModule.java]
│   │   │   │   │   │   │   ├── wave/
│   │   │   │   │   │   │   │   ├── boss/
│   │   │   │   │   │   │   │   │   ├── BossWaveHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/boss/BossWaveHandler.java]
│   │   │   │   │   │   │   │   ├── BossWaveDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/BossWaveDefinition.java]
│   │   │   │   │   │   │   │   ├── condition/
│   │   │   │   │   │   │   │   │   ├── AllMonstersClearedCondition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/condition/AllMonstersClearedCondition.java]
│   │   │   │   │   │   │   │   │   ├── BossDefeatedCondition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/condition/BossDefeatedCondition.java]
│   │   │   │   │   │   │   │   │   ├── WaveClearCondition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/condition/WaveClearCondition.java]
│   │   │   │   │   │   │   │   ├── event/
│   │   │   │   │   │   │   │   │   ├── WaveClearedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/event/WaveClearedEvent.java]
│   │   │   │   │   │   │   │   │   ├── WaveSpawnEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/event/WaveSpawnEvent.java]
│   │   │   │   │   │   │   │   │   ├── WaveStartedEvent.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/event/WaveStartedEvent.java]
│   │   │   │   │   │   │   │   ├── MonsterSpawnEntry.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/MonsterSpawnEntry.java]
│   │   │   │   │   │   │   │   ├── ReadyVoteService.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/ReadyVoteService.java]
│   │   │   │   │   │   │   │   ├── spawn/
│   │   │   │   │   │   │   │   │   ├── SpawnPointGroup.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/spawn/SpawnPointGroup.java]
│   │   │   │   │   │   │   │   ├── state/
│   │   │   │   │   │   │   │   │   ├── ClearedStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/ClearedStateHandler.java]
│   │   │   │   │   │   │   │   │   ├── InProgressStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/InProgressStateHandler.java]
│   │   │   │   │   │   │   │   │   ├── RewardStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/RewardStateHandler.java]
│   │   │   │   │   │   │   │   │   ├── SpawningStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/SpawningStateHandler.java]
│   │   │   │   │   │   │   │   │   ├── WaitingStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/WaitingStateHandler.java]
│   │   │   │   │   │   │   │   │   ├── WaveStateHandler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/state/WaveStateHandler.java]
│   │   │   │   │   │   │   │   ├── WaveDefinition.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/WaveDefinition.java]
│   │   │   │   │   │   │   │   ├── WaveManager.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/WaveManager.java]
│   │   │   │   │   │   │   │   ├── WaveScalingPolicy.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/WaveScalingPolicy.java]
│   │   │   │   │   │   │   │   ├── WaveSpawnScheduler.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/WaveSpawnScheduler.java]
│   │   │   │   │   │   │   │   ├── WaveState.java [📂 extraction_target_project/src/main/java/com/yourstudio/coredefense/wave/WaveState.java]
│   │   │   ├── resources/
│   │   │   │   ├── config/
│   │   │   │   │   ├── core.yml [📂 extraction_target_project/src/main/resources/config/core.yml]
│   │   │   │   │   ├── core_visual_stages.yml [📂 extraction_target_project/src/main/resources/config/core_visual_stages.yml]
│   │   │   │   │   ├── models/
│   │   │   │   │   │   ├── animation_triggers.yml [📂 extraction_target_project/src/main/resources/config/models/animation_triggers.yml]
│   │   │   │   │   ├── npc/
│   │   │   │   │   │   ├── npc_job_promotions.yml [📂 extraction_target_project/src/main/resources/config/npc/npc_job_promotions.yml]
│   │   │   │   │   │   ├── npc_traits.yml [📂 extraction_target_project/src/main/resources/config/npc/npc_traits.yml]
│   │   │   │   │   │   ├── resonance_thresholds.yml [📂 extraction_target_project/src/main/resources/config/npc/resonance_thresholds.yml]
│   │   │   │   │   ├── player_classes/
│   │   │   │   │   │   ├── classes.yml [📂 extraction_target_project/src/main/resources/config/player_classes/classes.yml]
│   │   │   │   │   │   ├── specializations.yml [📂 extraction_target_project/src/main/resources/config/player_classes/specializations.yml]
│   │   │   │   │   ├── progression/
│   │   │   │   │   │   ├── score_weights.yml [📂 extraction_target_project/src/main/resources/config/progression/score_weights.yml]
│   │   │   │   │   ├── waves/
│   │   │   │   │   │   ├── boss_waves.yml [📂 extraction_target_project/src/main/resources/config/waves/boss_waves.yml]
│   │   │   │   │   │   ├── wave_definitions.yml [📂 extraction_target_project/src/main/resources/config/waves/wave_definitions.yml]
│   │   │   │   ├── editor_objects.json [📂 extraction_target_project/src/main/resources/editor_objects.json]
│   │   │   │   ├── plugin.yml [📂 extraction_target_project/src/main/resources/plugin.yml]
│   ├── tools/
│   │   ├── resourcepack-build/
│   │   │   ├── build_pack.py [📂 extraction_target_project/tools/resourcepack-build/build_pack.py]
├── oldplan/
│   ├── agent_plan1.md [📂 oldplan/agent_plan1.md]
│   ├── agent_plan2.md [📂 oldplan/agent_plan2.md]
│   ├── agent_plan3.md [📂 oldplan/agent_plan3.md]
├── prompt.md [📂 prompt.md]
├── README.md [📂 README.md]
├── scan_debug.txt [📂 scan_debug.txt]
├── setup_architecture.bat [📂 setup_architecture.bat]
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
│   │   ├── create_ai_map.py [📂 tools/universal_indexer/create_ai_map.py] -> [💡 📦 imp: ast, json, os, pathlib, tools.universal_indexer.switch | 🎯 def load_jjap_context() [L41-60] | 🎯 def collect_target_files() [L63-122] | 🎯 def load_registry() [L125-162] | 🎯 def load_protocols() [L165-187] | 🎯 def parse_protocols_and_registries() [L194-247] | 🎯 def main() [L250-345] | 🎯 def generate_ai_optimized_map() [L351-353]]
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
