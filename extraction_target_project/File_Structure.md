# 파일 구조 개정안 — "이름만 보고 유추 가능"한 구조로 재설계

> 원본 plan.md의 4장(리소스 구조)·5장(패키지 구조)·6~23장에 흩어져 있던 모든 클래스를
> **누락 없이** 모아 하나의 트리로 통합했습니다. 기능을 바꾸거나 뺀 것은 없고,
> **① 이름 충돌 해소 ② 트리↔본문 불일치 해소 ③ 애매한 이름 구체화**만 수행했습니다.

---

## 1. 무엇을, 왜 바꿨는가 (요약)

| 문제 | 원본 | 수정 | 이유 |
|---|---|---|---|
| 이름 충돌 | `job/`(플레이어 직업) vs `npc/job/`(NPC 직업) | `playerclass/`(플레이어) vs `npc/vocation/`(NPC) | 둘 다 "job"이라 코드/경로만 보고 구분 불가. 문서 5.1에도 "혼동 방지를 위해 분리"라고 직접 언급했을 정도로 원본부터 모호했던 지점 |
| 트리 누락 | `resonance_thresholds.yml`, `core_visual_stages.yml`, `npc_job_promotions.yml`이 21장 표에만 등장, 4장 트리에는 없음 | 4장 트리에 전부 반영 | 트리만 보고 "이 파일이 존재하는지" 판단하는 AI가 놓치게 됨 |
| 본문에만 있고 트리엔 없는 클래스 다수 | `CoreLevelUpService`, `CombatDamageService`, `NpcStateMachine`, `SafeZoneService`, `WeaponVfxService`, `MiningEfficiencyPolicy`, `CoreVisualFeedbackService`, `SchematicPasteService`, `WaveScalingPolicy`, `TurretTargeting` 구현체 9종(포탑) 등 40여 개 | 전부 5장 트리에 편입 | 6~23장 "상세 설계"에서 처음 등장한 클래스가 5장 스켈레톤 트리에는 빠져 있어, 트리만 읽는 AI는 이들의 존재 자체를 모름 |
| 범용/모호 이름 | `SessionState` (Session인지 다른 도메인 State인지 접두어 없음) | `GameSessionState` | 다른 State들(`CoreState`,`WaveState`,`NpcState`)과 명명 패턴 통일 |
| 소속 불명확 | `Healable`, `EnergyConsumer` — 코어/NPC/구조물/직업이 전부 구현하는데 `core/`에만 있음 | `common/contract/`로 이동 | "여러 도메인이 구현하는 공용 계약"은 특정 도메인 폴더에 두면 그 도메인 소유처럼 보여 AI가 참조 관계를 잘못 유추함 |
| 로봇(드론) 소속 불명 | 메카닉 전문화 설명(6.8) 속에만 등장, 별도 패키지 없음 | 최상위 `drone/` 신설 | `GameNpc`와 별개의 엔티티라고 원문에 명시되어 있어 `npc/`나 `playerclass/mechanic/` 어디에도 넣으면 오해 소지 |
| 모델링 파이프라인 누락 | Blockbench(.bbmodel) + Animated Java로 제작한 모델/애니메이션을 어디서 어떻게 관리하는지 트리에 전혀 없음 (plan.md 24장 신설분) | 최상위 `render/` 패키지 + 리소스 트리에 `models/raw/`(원본 보관, 빌드 산출물 아님) · `assets/`(리소스팩 빌드용) · `animations/`(런타임 파싱용) 신설 | 도메인(Core/Turret/Npc/Mob)과 렌더링을 `ModelAnchor` 계약으로 분리해야, 새 모델 추가 시 도메인 코드를 건드리지 않고 에셋+YAML만 추가하면 되는 구조가 트리에서도 보임 |

---

## 2. 리소스 디렉터리 구조 (4장 개정 — 본문 21.2 표와 100% 동기화)

```
core-defense-plugin/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── gradle/wrapper/
├── README.md
├── docs/
│   └── design/
├── models/                                        ← ★ 신설: Blockbench/Animated Java 원본 (빌드 산출물 아님, 버전관리용 원본 보관)
│   └── raw/
│       ├── core/
│       │   └── core.bbmodel                        (Animated Java 애니메이션 데이터 내장)
│       ├── turret/
│       │   ├── arrow_sentry.bbmodel
│       │   ├── minigun.bbmodel
│       │   └── ...                                 (18.3의 9개 포탑 각각)
│       ├── drone/
│       │   └── combat_drone.bbmodel
│       ├── npc/
│       │   └── npc_base.bbmodel
│       └── mob/
│           └── ...                                 (몬스터 종류별)
├── tools/
│   └── resourcepack-build/                          ← ★ 신설: Animated Java export 산출물을 src/main/resources/assets·animations로 동기화하는 빌드 스크립트 (24.5, ResourcePackBuildTask 연동)
├── src/
│   ├── main/
│   │   ├── java/com/yourstudio/coredefense/   (3장 참고)
│   │   └── resources/
│   │       ├── plugin.yml
│   │       ├── config/
│   │       │   ├── core.yml                        (코어 레벨 곡선/에너지 총량/해금 매핑)
│   │       │   ├── core_visual_stages.yml          (코어 레벨별 외형 스키매틱 매핑)   ← 누락분 반영
│   │       │   ├── waves/
│   │       │   │   ├── wave_definitions.yml
│   │       │   │   └── boss_waves.yml
│   │       │   ├── weapons/
│   │       │   │   ├── guns.yml
│   │       │   │   └── melee.yml
│   │       │   ├── player_classes/                  ← "classes"→"player_classes"로 명확화 (npc 쪽과 이름 겹치지 않게)
│   │       │   │   ├── classes.yml
│   │       │   │   └── specializations.yml
│   │       │   ├── npc/
│   │       │   │   ├── npc_traits.yml
│   │       │   │   ├── npc_recruit_pool.yml
│   │       │   │   ├── npc_job_promotions.yml       (14.4 전직 데이터)                ← 누락분 반영
│   │       │   │   └── resonance_thresholds.yml     (14.3 공명 레벨별 협업 해금 기준)  ← 누락분 반영
│   │       │   ├── mining/
│   │       │   │   └── ores.yml
│   │       │   ├── structures/
│   │       │   │   ├── walls.yml
│   │       │   │   └── turrets.yml
│   │       │   ├── progression/
│   │       │   │   ├── meta_upgrades.yml
│   │       │   │   └── score_weights.yml            (19.1 점수 가중치)               ← 누락분 반영
│   │       │   └── models/                          ← ★ 신설: 렌더링 시스템 Config (24.4)
│   │       │       └── animation_triggers.yml        (게임 이벤트 → animId 매핑)
│   │       ├── animations/                          ← ★ 신설: Animated Java export의 (b) 키프레임 JSON — 플러그인이 런타임 파싱 (24.2, AnimatedJavaAssetLoader)
│   │       │   ├── core/
│   │       │   ├── turret/
│   │       │   ├── drone/
│   │       │   ├── npc/
│   │       │   └── mob/
│   │       ├── assets/                              ← ★ 신설: Animated Java export의 (a) 뼈대별 아이템 모델/텍스처 — 리소스팩 빌드 원본 (24.5)
│   │       │   └── minecraft/
│   │       │       ├── models/item/
│   │       │       └── textures/item/
│   │       ├── lang/
│   │       │   ├── en_US.yml
│   │       │   └── ko_KR.yml
│   │       └── schematics/
│   └── test/
│       └── java/
└── libs/
```

**변경 근거**
- `config/classes/` → `config/player_classes/` : 트리만 보고도 "이건 플레이어 직업, npc 쪽 트레잇/모집과는 다른 카테고리"라는 걸 파일 경로만으로 구분 가능하게 함.
- `npc/npc_job_promotions.yml`, `npc/resonance_thresholds.yml`, `core_visual_stages.yml`, `progression/score_weights.yml`는 21.2 표에는 있었지만 4장 트리에는 빠져 있던 파일 — 전부 편입해 **본문 설명과 트리가 항상 1:1로 대응**하도록 함.
- `models/raw/`는 프로젝트 최상위(=`src/main/resources` 밖)에 둔다: `.bbmodel`은 컴파일/패키징 대상이 아닌 디자이너 원본이므로, 빌드 산출물인 `assets/`·`animations/`와 물리적으로 분리해야 "이 폴더는 빌드에 안 들어간다"는 걸 경로만으로 유추 가능.
- `assets/`(리소스팩용)와 `animations/`(플러그인 런타임 파싱용)를 분리한 이유: 전자는 유저 클라이언트에 배포되는 산출물, 후자는 서버만 읽는 데이터로 소비 주체가 완전히 다름 (24.1).

---

## 3. Java 패키지 구조 (5장 전면 개정 — 6~23장 등장 클래스 전수 반영)

```
com.yourstudio.coredefense
├── CoreDefensePlugin.java
├── bootstrap/
│   ├── ModuleInitializer.java
│   ├── ListenerRegistrar.java
│   └── CommandRegistrar.java
│
├── api/
│   ├── event/
│   └── service/
│
├── common/
│   ├── event/
│   │   ├── AbstractGameEvent.java
│   │   └── GameListener.java
│   ├── registry/
│   │   ├── Registry.java
│   │   ├── AbstractRegistry.java
│   │   └── RegistryKey.java
│   ├── config/
│   │   ├── ConfigService.java
│   │   ├── ConfigLoader.java
│   │   ├── ConfigParser.java
│   │   └── ReloadableConfig.java
│   ├── contract/                              ← 신설: "여러 도메인이 함께 구현하는 인터페이스" 전용 폴더
│   │   ├── EnergyConsumer.java                (core/npc/structure/playerclass가 공동 구현 — core 소유 아님)
│   │   ├── EnergyPriority.java
│   │   ├── Healable.java                      (core/npc/structure 공동 피회복 대상)
│   │   └── ModelAnchor.java                   (core/turret/npc/mob/drone이 공동 구현 — render 패키지 소유 아님, plan.md 24.2)
│   ├── util/
│   │   ├── MathUtils.java
│   │   ├── ParticleUtils.java
│   │   ├── CooldownTracker.java
│   │   └── RayTraceUtil.java                  (9.1 시퀀스에서만 언급 → 유틸로 명시 편입)
│   ├── scheduling/
│   │   └── GameScheduler.java                 (22.3 Folia 대응 RegionizedScheduler 래퍼)
│   ├── perf/
│   │   └── PerformanceMonitor.java            (23.6 계측 유틸)
│   └── result/
│       └── ActionResult.java
│
├── session/
│   ├── GameSession.java
│   ├── GameSessionManager.java
│   ├── GameTeam.java
│   ├── GameSessionState.java                  ← 개명: SessionState → GameSessionState (CoreState/WaveState/NpcState와 명명 통일)
│   └── event/
│       └── GameSessionEndedEvent.java         (원본 progression 폴더에만 언급되던 이벤트 → 발행 주체인 session으로 이동)
│
├── core/
│   ├── CoreEntity.java
│   ├── CoreLevel.java
│   ├── CoreLevelRegistry.java
│   ├── CoreLevelUpService.java                ← 9.2 시퀀스에서만 언급 → 트리에 명시 편입
│   ├── CoreEnergyManager.java
│   ├── CoreUnlockManager.java
│   ├── CoreUnlockConfig.java                  (2.3 표의 코어레벨→해금 매핑 모델)
│   ├── CoreState.java
│   ├── CoreStateMachine.java                  ← 6.1에서 "전이 로직은 CoreStateMachine 전담" → 트리에 명시 편입
│   ├── CoreVisualFeedbackService.java         ← 16.3에서만 언급 → 편입
│   ├── SchematicPasteService.java             ← 16.4에서만 언급 → 편입
│   ├── CoreLevelListener.java                 (마커 인터페이스)
│   └── event/
│       ├── CoreDamagedEvent.java
│       ├── CoreLeveledUpEvent.java
│       ├── CoreDestroyedEvent.java
│       └── CoreSystemUnlockedEvent.java
│
├── wave/
│   ├── WaveManager.java
│   ├── WaveState.java
│   ├── WaveDefinition.java
│   ├── BossWaveDefinition.java                ← 15.1에서만 언급 → 편입 (WaveDefinition 서브클래스)
│   ├── MonsterSpawnEntry.java                 ← WaveDefinition 내부 참조 타입 → 명시 편입
│   ├── WaveSpawnScheduler.java
│   ├── WaveScalingPolicy.java                 ← 15.1에서만 언급 → 편입
│   ├── ReadyVoteService.java                  ← 15.4에서만 언급 → 편입
│   ├── spawn/
│   │   └── SpawnPointGroup.java               ← 15.2에서만 언급 → 편입
│   ├── condition/                             ← WaveClearCondition 및 구현체를 묶는 하위 패키지 신설
│   │   ├── WaveClearCondition.java
│   │   ├── AllMonstersClearedCondition.java
│   │   └── BossDefeatedCondition.java
│   ├── state/                                 ← 6.2에서 언급된 "switch 대신 Handler 리스트" 구조를 트리에 명시
│   │   ├── WaveStateHandler.java
│   │   ├── WaitingStateHandler.java
│   │   ├── SpawningStateHandler.java
│   │   ├── InProgressStateHandler.java
│   │   ├── ClearedStateHandler.java
│   │   └── RewardStateHandler.java
│   ├── boss/
│   │   └── BossWaveHandler.java
│   └── event/
│       ├── WaveStartedEvent.java
│       ├── WaveSpawnEvent.java
│       └── WaveClearedEvent.java
│
├── combat/
│   ├── weapon/
│   │   ├── Weapon.java
│   │   ├── AbstractFirearm.java
│   │   ├── SingleShotFirearm.java
│   │   ├── BurstFireFirearm.java
│   │   ├── SniperRifle.java
│   │   ├── WeaponDefinition.java
│   │   ├── WeaponInputHandler.java            ← 9.1에서만 언급 → 편입
│   │   ├── WeaponRegistry.java
│   │   ├── WeaponFactory.java
│   │   ├── WeaponAttachment.java              ← 13.5 확장방향에서만 언급 → 편입
│   │   ├── WeaponAcquisitionPolicy.java       ← 13.5에서만 언급 → 편입
│   │   ├── strategy/
│   │   │   ├── FireModeStrategy.java
│   │   │   ├── SingleShotStrategy.java
│   │   │   ├── BurstFireStrategy.java
│   │   │   ├── SniperShotStrategy.java
│   │   │   └── SpreadPolicy.java              ← 13.2에서만 언급 → 편입
│   │   ├── projectile/
│   │   │   ├── ProjectileType.java
│   │   │   ├── BulletProjectile.java
│   │   │   ├── ArcProjectile.java             ← 13.4(궁사 계열)에서만 언급 → 편입
│   │   │   └── ProjectileFactory.java
│   │   └── ammo/
│   │       ├── AmmoType.java
│   │       └── AmmoInventory.java
│   ├── melee/
│   │   ├── MeleeWeapon.java
│   │   └── MeleeAttackHandler.java
│   ├── damage/
│   │   ├── DamageCalculator.java
│   │   ├── DamageSource.java
│   │   ├── DamageModifier.java
│   │   └── CombatDamageService.java           ← 9.1에서만 언급 → 편입
│   ├── vfx/
│   │   └── WeaponVfxService.java              ← 13.2에서만 언급 → 편입 (판정-연출 분리 원칙의 실체)
│   └── event/
│       ├── WeaponFiredEvent.java
│       └── EntityDamagedByGameEvent.java
│
├── mob/
│   ├── MonsterDefinition.java
│   ├── MonsterFactory.java
│   ├── MonsterAI.java
│   ├── MonsterRegistry.java
│   ├── ai/
│   │   ├── TargetSelector.java
│   │   └── PathingStrategy.java
│   └── event/
│       └── MonsterKilledEvent.java
│
├── npc/
│   ├── GameNpc.java
│   ├── NpcRole.java
│   ├── NpcState.java
│   ├── NpcStateMachine.java                   ← 14.1에서만 언급 → 편입
│   ├── NpcStatSheet.java
│   ├── NpcCapacityPolicy.java                 ← 14.5에서만 언급 → 편입
│   ├── NpcOwnershipPolicy.java                ← 14.6 확장방향에서만 언급 → 편입
│   ├── safezone/                              ← 14.2에서만 언급된 안전지대 로직을 하위 패키지로 명시
│   │   ├── SafeZoneService.java
│   │   └── event/
│   │       └── SafeZoneBreachedEvent.java
│   ├── trait/
│   │   ├── NpcTrait.java
│   │   ├── TraitRegistry.java
│   │   ├── ResonanceCalculator.java
│   │   └── NpcCollaborationUnlockService.java ← 14.3에서만 언급 → 편입
│   ├── vocation/                              ← ★ 개명: npc/job/ → npc/vocation/ (플레이어 쪽 playerclass와 이름 완전 분리)
│   │   ├── NpcVocation.java                   ← ★ 개명: NpcJob → NpcVocation
│   │   ├── NpcVocationSkillTree.java          ← ★ 개명: JobSkillTree → NpcVocationSkillTree (플레이어의 SkillTree와 구분)
│   │   └── NpcVocationPromotion.java          ← 14.4 전직 데이터 모델, npc_job_promotions.yml과 대응
│   ├── recruit/
│   │   ├── RecruitPool.java
│   │   ├── RecruitOffer.java
│   │   ├── RecruitPoolWeightTable.java        ← 14.5에서만 언급 → 편입
│   │   └── RecruitmentService.java
│   ├── death/
│   │   ├── NpcDeathHandler.java
│   │   ├── ReviveService.java
│   │   └── LegacyTransferService.java
│   └── event/
│       ├── NpcRecruitedEvent.java
│       ├── NpcLeveledUpEvent.java
│       └── NpcDiedEvent.java
│
├── mining/
│   ├── MiningSession.java
│   ├── OreType.java
│   ├── OreRegistry.java
│   ├── ClickMiningHandler.java
│   ├── AutoMiningTicker.java
│   ├── MiningEfficiencyPolicy.java            ← 6.6/17.3에서만 언급 → 편입
│   └── event/
│       ├── OreMinedEvent.java
│       └── OreUnlockedEvent.java              ← 17.2에서만 언급 → 편입
│
├── structure/
│   ├── StructureRegistry.java
│   ├── StructurePlacementService.java
│   ├── BuildableZoneService.java              ← 18.5에서만 언급 → 편입
│   ├── BuildPermissionPolicy.java             ← 18.5에서만 언급 → 편입
│   ├── wall/
│   │   ├── WallDefinition.java
│   │   ├── WallMaterialTier.java
│   │   ├── WallInstance.java
│   │   └── WallModule.java
│   ├── turret/
│   │   ├── Turret.java
│   │   ├── TurretDefinition.java
│   │   ├── TurretFactory.java
│   │   ├── TurretAmmoSupply.java
│   │   ├── targeting/                         ← TurretTargeting 및 3개 전략 구현체를 하위 패키지로 명시
│   │   │   ├── TurretTargeting.java
│   │   │   ├── NearestTargetStrategy.java
│   │   │   ├── LowestHpTargetStrategy.java
│   │   │   └── HighestThreatTargetStrategy.java
│   │   └── types/                             ← 18.3 표의 9개 포탑 구현체 (원본엔 트리에 없이 본문에만 나열) → 편입
│   │       ├── ArrowSentryTurret.java
│   │       ├── SlingshotTurret.java
│   │       ├── FlamethrowerTurret.java
│   │       ├── MinigunTurret.java
│   │       ├── BuffTowerTurret.java
│   │       ├── LightGunTurret.java
│   │       ├── AutoCannonTurret.java
│   │       ├── MissileTurret.java
│   │       └── NukeMissileTurret.java
│   └── event/
│       ├── StructurePlacedEvent.java
│       └── StructureDestroyedEvent.java
│
├── drone/                                     ← ★ 신설: 메카닉 전문화 설명(6.8) 안에만 있던 CombatDrone을 독립 도메인으로 분리
│   ├── CombatDrone.java                       (GameNpc와 별개의 엔티티, EnergyConsumer 구현)
│   └── DroneCapacityPolicy.java
│
├── render/                                    ← ★ 신설: Blockbench+Animated Java 모델/애니메이션 렌더링 (plan.md 24장)
│   ├── model/
│   │   ├── ModelDefinition.java
│   │   ├── BoneDefinition.java
│   │   ├── ModelRegistry.java
│   │   └── AnimatedJavaAssetLoader.java       (resources/animations/ 파싱 → Registry 적재, ReloadableConfig 구현)
│   ├── animation/
│   │   ├── AnimationDefinition.java
│   │   ├── BoneKeyframeTrack.java
│   │   ├── Keyframe.java
│   │   ├── InterpolationType.java
│   │   ├── AnimationRegistry.java
│   │   ├── AnimationPlayer.java
│   │   ├── AnimationTicker.java               (GameScheduler 기반 분산 틱 재생, 23.1 원칙 재사용)
│   │   ├── AnimationLodPolicy.java            (거리 기반 갱신주기 저하, 23.3 VfxLodPolicy와 동일 패턴)
│   │   ├── TransformInterpolator.java         (순수 함수: 키프레임 간 보간)
│   │   ├── BoneTransformComposer.java         (순수 함수: 부모-자식 Transformation 행렬 합성)
│   │   └── trigger/                           ← 게임 이벤트 → 애니메이션 매핑을 하위 패키지로 명시 (24.4)
│   │       ├── AnimationTriggerMapping.java
│   │       └── AnimationTriggerListener.java  (GameListener 구현, 도메인 이벤트 구독 후 재생 위임)
│   ├── display/
│   │   ├── DisplayModelInstance.java          (ItemDisplay 묶음 + 현재 AnimationPlayer 보유)
│   │   └── DisplayModelFactory.java
│   ├── asset/
│   │   └── ModelAssetValidator.java           (itemModelId/boneId 참조 무결성 검증, 21.1 validate() 원칙 재사용)
│   └── event/
│       ├── ModelSpawnedEvent.java
│       └── AnimationStateChangedEvent.java
│
├── playerclass/                               ← ★ 개명: job/ → playerclass/ (npc/vocation과 이름 충돌 해소)
│   ├── PlayerClass.java
│   ├── ClassDefinition.java
│   ├── ClassRegistry.java
│   ├── specialization/
│   │   └── Specialization.java
│   ├── skill/
│   │   ├── Skill.java
│   │   ├── ActiveSkill.java
│   │   ├── PassiveSkill.java
│   │   ├── UltimateSkill.java
│   │   ├── UltimateCooldownPool.java          ← 12.4에서만 언급 → 편입
│   │   ├── SkillTree.java
│   │   ├── SkillNode.java                     ← 6.8에서만 언급 → 편입
│   │   └── SkillInputHandler.java             ← 9.4 시퀀스에서만 언급 → 편입
│   ├── heal/                                  ← 메딕 전문화 관련 요소를 하위 패키지로 명시
│   │   └── HealStrategy.java
│   ├── builder/                               ← 빌더 전문화(오버클럭) 관련 요소를 하위 패키지로 명시
│   │   ├── OverclockSkill.java                (ActiveSkill 구현체 예시)
│   │   ├── OverclockPenaltyHandler.java
│   │   └── event/
│   │       ├── OverclockActivatedEvent.java   ← 9.4에서만 언급 → 편입
│   │       └── OverheatTriggeredEvent.java    ← 9.4에서만 언급 → 편입
│   └── event/
│       ├── ClassSelectedEvent.java
│       └── SkillUsedEvent.java
│
├── progression/
│   ├── MetaCurrency.java
│   ├── PlayerProgressionData.java
│   ├── MetaUpgrade.java
│   ├── MetaUpgradeTree.java
│   ├── MetaUpgradeNode.java                   ← 19.2에서만 언급 → 편입
│   ├── UpgradeEffectType.java                 ← 19.2에서만 언급 → 편입
│   ├── ScoreCalculator.java
│   ├── ProgressionService.java
│   └── ProgressionStatsCollector.java         ← 9.1에서만 언급 → 편입
│
├── persistence/
│   ├── Repository.java
│   ├── DataStoreType.java
│   ├── PersistenceService.java
│   ├── PlayerDataLock.java                    ← 20.4에서만 언급 → 편입
│   ├── FailedSaveRetryQueue.java              ← 20.4에서만 언급 → 편입
│   ├── file/
│   │   ├── YamlPlayerRepository.java
│   │   └── JsonSessionSnapshotRepository.java
│   └── sql/
│       ├── SqlPlayerRepository.java
│       └── SqlSchemaMigrator.java
│
├── gui/
│   ├── GameMenu.java
│   ├── MenuFactory.java
│   └── menus/
│       ├── RecruitMenu.java
│       ├── SkillTreeMenu.java
│       ├── MetaUpgradeMenu.java
│       └── NpcReplaceMenu.java                ← 14.5에서만 언급 → 편입
│
└── command/
    ├── CoreDefenseCommand.java
    └── sub/
        ├── StartGameSubcommand.java
        └── AdminReloadSubcommand.java
```

---

## 4. 이름 규칙 정리 (AI가 이름만으로 100% 유추할 수 있도록)

| 접미사/접두사 | 의미 | 예 |
|---|---|---|
| `Xxx` (도메인 루트 엔티티) | 그 도메인의 핵심 상태 보유 객체 | `CoreEntity`, `GameNpc`, `CombatDrone` |
| `XxxDefinition` | YAML에서 역직렬화되는 불변 데이터(Record) | `WeaponDefinition`, `MonsterDefinition` |
| `XxxRegistry` | ID → Definition 조회 저장소 | `WeaponRegistry`, `OreRegistry` |
| `XxxFactory` | 반복 생성되는 객체의 생성 책임 | `MonsterFactory`, `TurretFactory` |
| `XxxStrategy` | 같은 계약 하에 동작 방식이 갈리는 구현체 | `SniperShotStrategy` |
| `XxxState` / `XxxStateMachine` | State 패턴 상태값 / 전이 전담 클래스 | `CoreState` + `CoreStateMachine` |
| `XxxPolicy` | 수치·규칙 계산을 캡슐화한 순수 로직 | `MiningEfficiencyPolicy`, `WaveScalingPolicy` |
| `XxxService` | 상태 변경을 수반하는 절차적 책임(파사드) | `RecruitmentService`, `PersistenceService` |
| `XxxEvent` | 과거형 동사, 상태 변화의 결과 | `MonsterKilledEvent` |
| `event/` 하위 패키지 | 해당 도메인의 "공개 계약" | 모든 도메인 동일 규칙 |

이 표 자체를 `docs/design/naming-convention.md`로 별도 분리해 두면, 이후 신규 클래스를 추가하는 사람(또는 AI)도 트리를 보지 않고 이름 규칙만으로 올바른 패키지 위치를 유추할 수 있습니다.

---

## 5. 이번 개정에서 손대지 않은 것

- 클래스의 책임, 메서드 시그니처, 이벤트 발행-구독 관계, 데이터 흐름(9~11장), 밸런스 수치(12~19장), 성능 전략(23장) — **전부 원본 그대로**입니다.
- 바뀐 것은 오직 **패키지 경로, 일부 클래스/파일 이름, 트리에 빠져 있던 항목의 편입**뿐입니다. 즉 "설계 내용"은 100% 유지하면서 "그 설계를 가리키는 이름표"만 AI 친화적으로 다듬었습니다.
