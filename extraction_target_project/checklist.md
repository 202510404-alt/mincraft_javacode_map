# 🛠️ 마인크래프트 FPS 타워디펜스 플러그인 — 구현 현황판

> 기준 문서: `plan.md` (기술 설계) + `파일구조_AI친화적_개정안.md` (파일구조 개정판)
> 상태 기호: `[x]` 구현 완료 · `[-]` 구현 중 · `[ ]` 미구현
> 최근 갱신: 파일구조 개정안에 렌더링(모델·애니메이션) 시스템 트리가 추가 반영됨에 따라 `render/` 패키지 및 관련 리소스 항목 신설

---

## 📂 프로젝트 루트

- [ ] **`core-defense-plugin/`**
    - [-] `build.gradle.kts`
        - 📌 **상태:** 구현 중
        - 📝 **변경 내역:** 마인크래프트 및 Paper API 버전을 1.21.1로 수정하고 툴체인 벤더 제약을 완화함.
    - [ ] `settings.gradle.kts`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] `gradle.properties`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] `gradle/wrapper/`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] `README.md`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] `docs/design/`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [권장 추가] `naming-convention.md`(4장 이름 규칙 표)를 이 폴더에 별도 분리 보관 권장
    - [ ] `libs/`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] **`models/`** ← ★ 신설
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [구조 변경] 신설(plan.md 24장). Blockbench/Animated Java 원본(.bbmodel) 보관 전용, `src/main/resources` 밖에 위치 (빌드 산출물 아님)
        - [ ] **`raw/core/`**
            - [ ] `core.bbmodel` — 📌 미구현 / 📝 없음 (Animated Java 애니메이션 데이터 내장)
        - [ ] **`raw/turret/`**
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 18.3의 9개 포탑 각각의 `.bbmodel` (예: `arrow_sentry.bbmodel`, `minigun.bbmodel` 등)
        - [ ] **`raw/drone/`**
            - [ ] `combat_drone.bbmodel` — 📌 미구현 / 📝 없음
        - [ ] **`raw/npc/`**
            - [ ] `npc_base.bbmodel` — 📌 미구현 / 📝 없음
        - [ ] **`raw/mob/`**
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 몬스터 종류별 `.bbmodel`
    - [ ] **`tools/resourcepack-build/`** ← ★ 신설
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [구조 변경] 신설(24.5). Animated Java export 산출물을 `src/main/resources/assets`·`animations`로 동기화하는 빌드 스크립트. `ResourcePackBuildTask`(Gradle task) 연동 지점

---

## 📂 src/main/resources

- [ ] **`plugin.yml`**
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** 없음

- [ ] **`config/`**
    - [ ] `core.yml`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음 (코어 레벨 곡선/에너지 총량/해금 매핑)
    - [ ] `core_visual_stages.yml`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 원본 21.2 표에만 존재 → 개정안에서 4장 트리에 편입
    - [ ] **`waves/`**
        - [ ] `wave_definitions.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `boss_waves.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
    - [ ] **`weapons/`**
        - [ ] `guns.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `melee.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
    - [ ] **`player_classes/`**
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [경로명 변경] `classes/` → `player_classes/` (NPC `vocation` 계열과 카테고리 혼동 방지)
        - [ ] `classes.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `specializations.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
    - [ ] **`npc/`**
        - [ ] `npc_traits.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `npc_recruit_pool.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `npc_job_promotions.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.4 전직 데이터, 원본 트리엔 없었으나 편입
        - [ ] `resonance_thresholds.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.3 공명 레벨별 협업 해금 기준, 편입
    - [ ] **`mining/`**
        - [ ] `ores.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
    - [ ] **`structures/`**
        - [ ] `walls.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `turrets.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
    - [ ] **`progression/`**
        - [ ] `meta_upgrades.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 없음
        - [ ] `score_weights.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 19.1 점수 가중치, 편입
    - [ ] **`models/`** ← ★ 신설 (config 하위)
        - [ ] `animation_triggers.yml`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [구조 변경] 신설(24.4). 게임 이벤트 → animId 매핑 (`AnimationTriggerMapping`이 역직렬화)

- [ ] **`animations/`** ← ★ 신설
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** [구조 변경] 신설(24.2/24.5). Animated Java export의 뼈대별 키프레임 JSON — 플러그인이 런타임 파싱(`AnimatedJavaAssetLoader`), 유저에게 배포되지 않고 서버만 읽음
    - [ ] `core/`
    - [ ] `turret/`
    - [ ] `drone/`
    - [ ] `npc/`
    - [ ] `mob/`

- [ ] **`assets/`** ← ★ 신설
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** [구조 변경] 신설(24.5). Animated Java export의 뼈대별 아이템 모델/텍스처 — 리소스팩 빌드 원본(유저 클라이언트 배포용)
    - [ ] `minecraft/models/item/`
    - [ ] `minecraft/textures/item/`

- [ ] **`lang/`**
    - [ ] `en_US.yml`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음
    - [ ] `ko_KR.yml`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** 없음

- [ ] **`schematics/`**
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** 없음

---

## 📂 src/main/java/com/yourstudio/coredefense

- [ ] `CoreDefensePlugin.java`
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** 없음

- [ ] **`bootstrap/`**
    - [ ] `ModuleInitializer.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `ListenerRegistrar.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (리플렉션 없이 명시적 리스트로 리스너 등록)
    - [ ] `CommandRegistrar.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

- [ ] **`api/`**
    - [ ] `event/`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `service/`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### common/

- [ ] **`common/event/`**
    - [ ] `AbstractGameEvent.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (GameSession 참조, 발생시각, Cancellable 공통 보유)
    - [ ] `GameListener.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (마커 인터페이스)
- [ ] **`common/registry/`**
    - [ ] `Registry.java` / `AbstractRegistry.java` / `RegistryKey.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
- [ ] **`common/config/`**
    - [ ] `ConfigService.java` / `ConfigLoader.java` / `ConfigParser.java` / `ReloadableConfig.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
- [ ] **`common/contract/`** ← 신설 패키지
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** [구조 변경] 신설. 여러 도메인이 공동 구현하는 인터페이스 전용 폴더로 분리
    - [x] `EnergyConsumer.java`
        - 📌 **상태:** 구현 완료
        - 📝 **변경 내역:** [위치 이동] `core/` → `common/contract/` (core/npc/structure/playerclass가 공동 구현하므로 core 전속 아님)
    - [x] `EnergyPriority.java`
        - 📌 **상태:** 구현 완료 / 📝 변경 내역: 없음
    - [ ] `Healable.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [위치 이동] `core/` → `common/contract/` (core/npc/structure 공동 피회복 대상)
    - [ ] `ModelAnchor.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [구조 변경] 신설(24.2). core/turret/npc/mob/drone이 공동 구현하는 렌더링 앵커 계약(`getAnchorLocation()`/`getYaw()`/`getModelId()`/`getCurrentAnimationId()`) — `render/` 패키지 소유가 아니라 공용 계약이므로 `common/contract/`에 위치
- [ ] **`common/util/`**
    - [ ] `MathUtils.java` / `ParticleUtils.java` / `CooldownTracker.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `RayTraceUtil.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 9.1 시퀀스에만 언급 → 유틸로 명시 편입
- [ ] **`common/scheduling/`**
    - [ ] `GameScheduler.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 22.3 Folia 대응 RegionizedScheduler 래퍼, 편입
- [ ] **`common/perf/`**
    - [ ] `PerformanceMonitor.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 23.6 계측 유틸, 편입
- [ ] **`common/result/`**
    - [ ] `ActionResult.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### session/

- [ ] **`session/`**
    - [ ] `GameSession.java` / `GameSessionManager.java` / `GameTeam.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `GameSessionState.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [명칭 변경] `SessionState` → `GameSessionState` (CoreState/WaveState/NpcState와 명명 규칙 통일)
    - [ ] `session/event/GameSessionEndedEvent.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [위치 이동] `progression/` → `session/event/` (발행 주체인 session으로 이동)

### core/

- [ ] **`core/`**
    - [ ] `CoreEntity.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (damage/heal/addExperience/getLevel/getState 보유)
    - [ ] `CoreLevel.java` (Record) / `CoreLevelRegistry.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `CoreLevelUpService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 9.2 시퀀스에서만 언급 → 편입
    - [ ] `CoreEnergyManager.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `CoreUnlockManager.java` / `CoreUnlockConfig.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (2.3 표: 코어레벨→해금 매핑 모델)
    - [ ] `CoreState.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `CoreStateMachine.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 6.1 "전이 로직은 CoreStateMachine 전담" → 편입
    - [ ] `CoreVisualFeedbackService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 16.3에서만 언급 → 편입
    - [ ] `SchematicPasteService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 16.4에서만 언급 → 편입
    - [ ] `CoreLevelListener.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (마커 인터페이스)
    - [ ] **`core/event/`**
        - [ ] `CoreDamagedEvent.java` / `CoreLeveledUpEvent.java` / `CoreDestroyedEvent.java` / `CoreSystemUnlockedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### wave/

- [ ] **`wave/`**
    - [ ] `WaveManager.java` / `WaveState.java` / `WaveDefinition.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `BossWaveDefinition.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 15.1에서만 언급 (WaveDefinition 서브클래스) → 편입
    - [ ] `MonsterSpawnEntry.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] WaveDefinition 내부 참조 타입 → 명시 편입
    - [ ] `WaveSpawnScheduler.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `WaveScalingPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 15.1에서만 언급 → 편입
    - [ ] `ReadyVoteService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 15.4에서만 언급 → 편입
    - [ ] **`wave/spawn/`**
        - [ ] `SpawnPointGroup.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 15.2에서만 언급 → 편입
    - [ ] **`wave/condition/`** ← 신설 하위 패키지
        - 📝 **변경 내역:** [구조 변경] WaveClearCondition 및 구현체를 묶는 하위 패키지 신설
        - [ ] `WaveClearCondition.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `AllMonstersClearedCondition.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (기본 조건)
        - [ ] `BossDefeatedCondition.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (보스전용 Strategy 구현체)
    - [ ] **`wave/state/`** ← 신설 하위 패키지
        - 📝 **변경 내역:** [구조 변경] 6.2 "switch 대신 Handler 리스트" 구조를 트리에 명시
        - [ ] `WaveStateHandler.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `WaitingStateHandler.java` / `SpawningStateHandler.java` / `InProgressStateHandler.java` / `ClearedStateHandler.java` / `RewardStateHandler.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`wave/boss/`**
        - [ ] `BossWaveHandler.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`wave/event/`**
        - [ ] `WaveStartedEvent.java` / `WaveSpawnEvent.java` / `WaveClearedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### combat/

- [ ] **`combat/weapon/`**
    - [ ] `Weapon.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (use/toItemStack/getDefinition)
    - [ ] `AbstractFirearm.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (탄창/재장전/반동/조준선 공통 로직)
    - [ ] `SingleShotFirearm.java` / `BurstFireFirearm.java` / `SniperRifle.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (상속+전략 혼합 구조)
    - [ ] `WeaponDefinition.java` / `WeaponRegistry.java` / `WeaponFactory.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `WeaponInputHandler.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 9.1에서만 언급 → 편입
    - [ ] `WeaponAttachment.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 13.5 확장방향에서만 언급 → 편입
    - [ ] `WeaponAcquisitionPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 13.5에서만 언급 → 편입
    - [ ] **`combat/weapon/strategy/`**
        - [ ] `FireModeStrategy.java` / `SingleShotStrategy.java` / `BurstFireStrategy.java` / `SniperShotStrategy.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `SpreadPolicy.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 13.2에서만 언급 → 편입
    - [ ] **`combat/weapon/projectile/`**
        - [ ] `ProjectileType.java` / `BulletProjectile.java` / `ProjectileFactory.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `ArcProjectile.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 13.4(궁사 계열)에서만 언급 → 편입
    - [ ] **`combat/weapon/ammo/`**
        - [ ] `AmmoType.java` / `AmmoInventory.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
- [ ] **`combat/melee/`**
    - [ ] `MeleeWeapon.java` / `MeleeAttackHandler.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
- [ ] **`combat/damage/`**
    - [ ] `DamageCalculator.java` / `DamageSource.java` / `DamageModifier.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `CombatDamageService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 9.1에서만 언급 → 편입
- [ ] **`combat/vfx/`**
    - [ ] `WeaponVfxService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 13.2에서만 언급 → 편입 (판정-연출 분리 원칙의 실체)
- [ ] **`combat/event/`**
    - [ ] `WeaponFiredEvent.java` / `EntityDamagedByGameEvent.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### mob/

- [ ] **`mob/`**
    - [ ] `MonsterDefinition.java` / `MonsterFactory.java` / `MonsterAI.java` / `MonsterRegistry.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`mob/ai/`**
        - [ ] `TargetSelector.java` / `PathingStrategy.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`mob/event/`**
        - [ ] `MonsterKilledEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (배치 집계 대상 이벤트, 23.2 참고)

### npc/

- [ ] **`npc/`**
    - [ ] `GameNpc.java` / `NpcRole.java` / `NpcState.java` / `NpcStatSheet.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `NpcStateMachine.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 14.1에서만 언급 → 편입
    - [ ] `NpcCapacityPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 14.5에서만 언급 → 편입
    - [ ] `NpcOwnershipPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 14.6 확장방향에서만 언급 → 편입
    - [ ] **`npc/safezone/`** ← 신설 하위 패키지
        - 📝 **변경 내역:** [구조 변경] 14.2에서만 언급된 안전지대 로직을 하위 패키지로 명시
        - [ ] `SafeZoneService.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `safezone/event/SafeZoneBreachedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`npc/trait/`**
        - [ ] `NpcTrait.java` / `TraitRegistry.java` / `ResonanceCalculator.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `NpcCollaborationUnlockService.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.3에서만 언급 → 편입
    - [ ] **`npc/vocation/`** ← 개명된 패키지
        - 📝 **변경 내역:** [명칭 변경] `npc/job/` → `npc/vocation/` (플레이어 쪽 `playerclass`와 이름 완전 분리, "job" 중복 충돌 해소)
        - [ ] `NpcVocation.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [명칭 변경] `NpcJob` → `NpcVocation`
        - [ ] `NpcVocationSkillTree.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [명칭 변경] `JobSkillTree` → `NpcVocationSkillTree` (플레이어의 SkillTree와 구분)
        - [ ] `NpcVocationPromotion.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.4 전직 데이터 모델, `npc_job_promotions.yml`과 대응하도록 편입
    - [ ] **`npc/recruit/`**
        - [ ] `RecruitPool.java` / `RecruitOffer.java` / `RecruitmentService.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `RecruitPoolWeightTable.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.5에서만 언급 → 편입
    - [ ] **`npc/death/`**
        - [ ] `NpcDeathHandler.java` / `ReviveService.java` / `LegacyTransferService.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`npc/event/`**
        - [ ] `NpcRecruitedEvent.java` / `NpcLeveledUpEvent.java` / `NpcDiedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### mining/

- [ ] **`mining/`**
    - [ ] `MiningSession.java` / `OreType.java` / `OreRegistry.java` / `ClickMiningHandler.java` / `AutoMiningTicker.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `MiningEfficiencyPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 6.6/17.3에서만 언급 → 편입
    - [ ] **`mining/event/`**
        - [ ] `OreMinedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `OreUnlockedEvent.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 17.2에서만 언급 → 편입

### structure/

- [ ] **`structure/`**
    - [ ] `StructureRegistry.java` / `StructurePlacementService.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `BuildableZoneService.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 18.5에서만 언급 → 편입
    - [ ] `BuildPermissionPolicy.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 18.5에서만 언급 → 편입 (인터페이스로 설계, boolean 아님)
    - [ ] **`structure/wall/`**
        - [ ] `WallDefinition.java` / `WallMaterialTier.java` / `WallInstance.java` / `WallModule.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`structure/turret/`**
        - [ ] `Turret.java` / `TurretDefinition.java` / `TurretFactory.java` / `TurretAmmoSupply.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] **`structure/turret/targeting/`** ← 신설 하위 패키지
            - 📝 **변경 내역:** [구조 변경] TurretTargeting 및 3개 전략 구현체를 하위 패키지로 명시
            - [ ] `TurretTargeting.java`
                - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
            - [ ] `NearestTargetStrategy.java` / `LowestHpTargetStrategy.java` / `HighestThreatTargetStrategy.java`
                - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] **`structure/turret/types/`** ← 신설 하위 패키지 (9종)
            - 📝 **변경 내역:** [트리 누락분 반영] 18.3 표의 9개 포탑 구현체, 원본엔 트리 없이 본문에만 나열 → 편입
            - [ ] `ArrowSentryTurret.java` (활포탑) — 📌 미구현 / 📝 없음
            - [ ] `SlingshotTurret.java` (슬링샷) — 📌 미구현 / 📝 없음
            - [ ] `FlamethrowerTurret.java` (화염방사기) — 📌 미구현 / 📝 없음
            - [ ] `MinigunTurret.java` (미니건) — 📌 미구현 / 📝 없음
            - [ ] `BuffTowerTurret.java` (버프타워) — 📌 미구현 / 📝 없음
            - [ ] `LightGunTurret.java` (경량탄총) — 📌 미구현 / 📝 없음
            - [ ] `AutoCannonTurret.java` (기관포) — 📌 미구현 / 📝 없음
            - [ ] `MissileTurret.java` (미사일) — 📌 미구현 / 📝 없음
            - [ ] `NukeMissileTurret.java` (핵미사일) — 📌 미구현 / 📝 없음
    - [ ] **`structure/event/`**
        - [ ] `StructurePlacedEvent.java` / `StructureDestroyedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### drone/ ← 신설 최상위 도메인

- [ ] **`drone/`**
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** [구조 변경] 신설. 메카닉 전문화 설명(6.8) 안에만 있던 `CombatDrone`을 `GameNpc`와 별개 엔티티로서 독립 도메인으로 분리
    - [ ] `CombatDrone.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (EnergyConsumer 구현)
    - [ ] `DroneCapacityPolicy.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### render/ ← 신설 최상위 도메인

- [ ] **`render/`**
    - 📌 **상태:** 미구현
    - 📝 **변경 내역:** [구조 변경] 신설(plan.md 24장). Blockbench+Animated Java로 제작한 모델/애니메이션을 순수 Paper Display Entity API(ItemDisplay)로 매 틱 제어하는 렌더링 엔진. 도메인 로직을 전혀 모르는 순수 계산/재생 계층으로 격리
    - [ ] **`render/model/`**
        - [ ] `ModelDefinition.java` (Record: modelId, List\<BoneDefinition\>, rootBoneId)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `BoneDefinition.java` (Record: boneId, parentBoneId, pivot, itemModelId, baseTransform)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `ModelRegistry.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `AnimatedJavaAssetLoader.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** `resources/animations/` 파싱 → Registry 적재, `ReloadableConfig` 구현(핫리로드)
    - [ ] **`render/animation/`**
        - [ ] `AnimationDefinition.java` (Record: animId, lengthTicks, loop, List\<BoneKeyframeTrack\>)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `BoneKeyframeTrack.java` (Record: boneId, List\<Keyframe\>)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `Keyframe.java` (Record: tick, position, rotation, scale, InterpolationType)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `InterpolationType.java` (Enum: LINEAR/CATMULLROM/STEP)
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `AnimationRegistry.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (모델별 네임스페이스, 예: "core.idle")
        - [ ] `AnimationPlayer.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (play/stop/isPlaying, 재생 큐 보유)
        - [ ] `AnimationTicker.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** `GameScheduler` 기반 분산 틱 재생(23.1 원칙 재사용)
        - [ ] `AnimationLodPolicy.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** 거리 기반 갱신주기 저하(23.3 `VfxLodPolicy`와 동일 패턴)
        - [ ] `TransformInterpolator.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (순수 함수: 키프레임 간 보간)
        - [ ] `BoneTransformComposer.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (순수 함수: 부모-자식 Transformation 행렬 합성)
        - [ ] **`render/animation/trigger/`** ← 신설 하위 패키지
            - 📝 **변경 내역:** [구조 변경] 게임 이벤트 → 애니메이션 매핑을 하위 패키지로 명시(24.4)
            - [ ] `AnimationTriggerMapping.java`
                - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (`animation_triggers.yml` 역직렬화)
            - [ ] `AnimationTriggerListener.java`
                - 📌 **상태:** 미구현
                - 📝 **변경 내역:** `GameListener` 구현, 도메인 이벤트(예: `CoreDamagedEvent`, `WeaponFiredEvent`)를 구독해 해당 `ModelAnchor`의 `AnimationPlayer.play()` 호출
    - [ ] **`render/display/`**
        - [ ] `DisplayModelInstance.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** ItemDisplay 엔티티 묶음(Map\<boneId, ItemDisplay\>) + 현재 AnimationPlayer 보유. `setAnchor()`/`dispose()` 제공
        - [ ] `DisplayModelFactory.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`render/asset/`**
        - [ ] `ModelAssetValidator.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** itemModelId/boneId 참조 무결성 검증, 21.1 `validate()` 원칙 재사용
    - [ ] **`render/event/`**
        - [ ] `ModelSpawnedEvent.java` / `AnimationStateChangedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### playerclass/ ← 개명된 패키지

- [ ] **`playerclass/`**
    - 📝 **변경 내역:** [명칭 변경] `job/` → `playerclass/` (NPC `vocation`과 이름 충돌 해소)
    - [ ] `PlayerClass.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [명칭 변경] `Job.java` → `PlayerClass.java` (NPC 직업 `Vocation`과 네이밍 충돌 방지)
    - [ ] `ClassDefinition.java` / `ClassRegistry.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`playerclass/specialization/`**
        - [ ] `Specialization.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`playerclass/skill/`**
        - [ ] `Skill.java` / `ActiveSkill.java` / `PassiveSkill.java` / `UltimateSkill.java` / `SkillTree.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `UltimateCooldownPool.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 12.4에서만 언급 → 편입
        - [ ] `SkillNode.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 6.8에서만 언급 → 편입
        - [ ] `SkillInputHandler.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 9.4 시퀀스에서만 언급 → 편입
    - [ ] **`playerclass/heal/`** ← 신설 하위 패키지 (메딕 전문화)
        - [ ] `HealStrategy.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`playerclass/builder/`** ← 신설 하위 패키지 (빌더/오버클럭)
        - [ ] `OverclockSkill.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음 (ActiveSkill 구현체 예시)
        - [ ] `OverclockPenaltyHandler.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] **`playerclass/builder/event/`**
            - [ ] `OverclockActivatedEvent.java`
                - 📌 **상태:** 미구현
                - 📝 **변경 내역:** [트리 누락분 반영] 9.4에서만 언급 → 편입
            - [ ] `OverheatTriggeredEvent.java`
                - 📌 **상태:** 미구현
                - 📝 **변경 내역:** [트리 누락분 반영] 9.4에서만 언급 → 편입
    - [ ] **`playerclass/event/`**
        - [ ] `ClassSelectedEvent.java` / `SkillUsedEvent.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### progression/

- [ ] **`progression/`**
    - [ ] `MetaCurrency.java` / `PlayerProgressionData.java` / `MetaUpgrade.java` / `MetaUpgradeTree.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `MetaUpgradeNode.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 19.2에서만 언급 → 편입
    - [ ] `UpgradeEffectType.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 19.2에서만 언급 → 편입 (Strategy 패턴으로 효과 적용 분리)
    - [ ] `ScoreCalculator.java` / `ProgressionService.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `ProgressionStatsCollector.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 9.1에서만 언급 → 편입

### persistence/

- [ ] **`persistence/`**
    - [ ] `Repository.java` / `DataStoreType.java` / `PersistenceService.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] `PlayerDataLock.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 20.4에서만 언급 → 편입
    - [ ] `FailedSaveRetryQueue.java`
        - 📌 **상태:** 미구현
        - 📝 **변경 내역:** [트리 누락분 반영] 20.4에서만 언급 → 편입
    - [ ] **`persistence/file/`**
        - [ ] `YamlPlayerRepository.java` / `JsonSessionSnapshotRepository.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`persistence/sql/`**
        - [ ] `SqlPlayerRepository.java` / `SqlSchemaMigrator.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

### gui/

- [ ] **`gui/`**
    - [ ] `GameMenu.java` / `MenuFactory.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`gui/menus/`**
        - [ ] `RecruitMenu.java` / `SkillTreeMenu.java` / `MetaUpgradeMenu.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
        - [ ] `NpcReplaceMenu.java`
            - 📌 **상태:** 미구현
            - 📝 **변경 내역:** [트리 누락분 반영] 14.5에서만 언급 → 편입

### command/

- [ ] **`command/`**
    - [ ] `CoreDefenseCommand.java`
        - 📌 **상태:** 미구현 / 📝 변경 내역: 없음
    - [ ] **`command/sub/`**
        - [ ] `StartGameSubcommand.java` / `AdminReloadSubcommand.java`
            - 📌 **상태:** 미구현 / 📝 변경 내역: 없음

---

## 📊 진행률 요약

| 구분 | 완료 | 진행중 | 미구현 | 합계 |
|---|---|---|---|---|
| 리소스(config/yml 등) | 0 | 0 | 27 | 27 |
| 리소스 디렉터리(모델/에셋 파이프라인, 파일 수 미확정) | 0 | 0 | `models/raw/*`, `animations/*`, `assets/*`, `tools/resourcepack-build/` | - |
| Java 클래스/인터페이스 | 0 | 0 | 약 170+ | 약 170+ |

> 현재 초기 상태로 전 항목 미구현입니다. 실제 개발 착수 후 각 항목의 `[ ]`를 `[-]`(구현 중)/`[x]`(완료)로 갱신하고, 설계와 다르게 구현된 부분은 📝 변경 내역에 사유를 기록하세요.
>
> **이번 갱신 요약 (파일구조_AI친화적_개정안.md 반영):** 렌더링 시스템(plan.md 24장, Blockbench+Animated Java 파이프라인)이 파일구조 개정안에 새로 편입되어, `render/` 패키지(model/animation/display/asset/event, 총 20개 클래스) · `common/contract/ModelAnchor.java` · 리소스 트리의 `models/raw/`, `tools/resourcepack-build/`, `src/main/resources/animations/`, `src/main/resources/assets/`, `config/models/animation_triggers.yml`을 신규 항목으로 추가했습니다. 그 외 이미 반영되어 있던 기존 항목(playerclass/vocation 개명, common/contract 이동, drone/ 신설 등)은 변경 없이 유지했습니다.
