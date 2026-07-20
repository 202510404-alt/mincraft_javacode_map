# 🏗️ 짭커서 프로젝트 CODEBASE MAP

현재 인덱싱된 총 파일 수: **10개**

## 🗂️ [Module Index]
- `extraction_target_project/.vscode/launch.json`
- `extraction_target_project/src/main/java/com/desertcore/DesertCore.java`
- `extraction_target_project/src/main/java/com/desertcore/DesertCoreTester.java`
- `extraction_target_project/src/main/java/com/desertcore/Switch.java`
- `extraction_target_project/src/main/java/com/desertcore/legacy/DeathEvent.java`
- `extraction_target_project/src/main/java/com/desertcore/legacy/DesertPortal.java`
- `extraction_target_project/src/main/java/com/desertcore/legacy/LobbyCommand.java`
- `extraction_target_project/src/main/java/com/desertcore/legacy/Marendumbul.java`
- `extraction_target_project/src/main/java/com/desertcore/session/GameSession.java`
- `extraction_target_project/src/main/java/com/desertcore/session/GameSessionManager.java`

## 💀 [Skeleton & Dependency 명세서]
### 📄 extraction_target_project/.vscode/launch.json
#### 🧱 Code Skeleton:
```python
📦 [JSON STRUCTURE MAP]
  ├── "version": str (val: 0.2.0)
  ├── "configurations": List (len: 2)
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/DesertCore.java
#### 🧱 Code Skeleton:
```python
public void onEnable() { // L15-30
registerAllListenersInPackage("com.desertcore.legacy"); // L20-25
getCommand("로비").setExecutor(new LobbyCommand()); // L24-27
getLogger().info("[DEBUG] 패키지 자동 스캔 및 리스너 일괄 등록 프로세스 완료."); // L28-33
public void onDisable() { // L33-35
getLogger().info("DesertCore가 비활성화되었습니다."); // L34-37
public GameSessionManager getGameSessionManager() { // L37-39
private void registerAllListenersInPackage(String packageName) { // L41-78
getServer().getPluginManager().registerEvents(listener, this); // L64-68
getLogger().info("[DEBUG] 자동 로드 성공: " + className); // L67-69
getLogger().warning("클래스 동적 생성 실패 (생성자 규격 확인 필요): " + className); // L70-75
getLogger().severe("패키지 스캔 중 치명적 오류 발생: " + e.getMessage()); // L76-76
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/DesertCoreTester.java
#### 🧱 Code Skeleton:
```python
class DesertCoreTester { // L12-90
    public static void main(String[] args) { // L14-89
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/Switch.java
#### 🧱 Code Skeleton:
```python
private Switch() {} // 인스턴스화 방지 // L10-10
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/legacy/DeathEvent.java
#### 🧱 Code Skeleton:
```python
class DeathEvent { // L35-223
    public DeathEvent(DesertCore plugin) { // L40-42
    public void onPlayerDeath(PlayerDeathEvent event) { // L45-59
    public void onPlayerRespawn(PlayerRespawnEvent event) { // L62-84
    public void onPlayerMove(PlayerMoveEvent event) { // L87-149
    public void run() { // L111-138
    public void onPlayerJoin(PlayerJoinEvent event) { // L152-173
    unloadAndDeleteInstance(previousWorldName); // L170-175
    private void unloadAndDeleteInstance(String instanceName) { // L175-206
    deleteDirectoryNative(instanceDir.toPath()); // L196-198
    private void deleteDirectoryNative(Path path) throws IOException { // L208-222
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException { // L211-214
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException { // L217-220
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/legacy/DesertPortal.java
#### 🧱 Code Skeleton:
```python
class DesertPortal { // L24-135
    public DesertPortal(DesertCore plugin) { // L29-31
    public void onVillagerClick(PlayerInteractEntityEvent event) { // L34-99
    deleteDirectoryNative(instanceDir.toPath()); // L69-75
    copyDirectoryNative(templateDir.toPath(), instanceDir.toPath()); // L72-77
    private void copyDirectoryNative(Path source, Path target) throws IOException { // L101-118
    public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException { // L104-110
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException { // L113-116
    private void deleteDirectoryNative(Path path) throws IOException { // L120-134
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException { // L123-126
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException { // L129-132
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/legacy/LobbyCommand.java
#### 🧱 Code Skeleton:
```python
class LobbyCommand { // L15-46
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) { // L18-45
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/legacy/Marendumbul.java
#### 🧱 Code Skeleton:
```python
class Marendumbul { // L14-68
    public Marendumbul(DesertCore plugin) { // L20-22
    public void onPlayerJoin(PlayerJoinEvent event) { // L25-67
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/session/GameSession.java
#### 🧱 Code Skeleton:
```python
class GameSession { // L11-71
    public GameSession(String worldName, UUID hostPlayerUuid) { // L21-26
    public UUID getSessionId() { return sessionId; } // L29-29
    public String getWorldName() { return worldName; } // L30-30
    public List<UUID> getPlayers() { return Collections.unmodifiableList(players); } // L33-33
    public int getCurrentWave() { return currentWave; } // L35-35
    public void incrementWave() { this.currentWave++; } // L36-36
    public boolean isTerminating() { return isTerminating; } // L38-38
    public void setTerminating(boolean terminating) { this.isTerminating = terminating; } // L39-39
    public void setActiveTimer(BukkitTask newTimer) { // L46-49
    clearActiveTimer(); // L47-54
    public void clearActiveTimer() { // L54-63
    public World getBukkitWorld() { // L68-70
```

--------------------------------------------------

### 📄 extraction_target_project/src/main/java/com/desertcore/session/GameSessionManager.java
#### 🧱 Code Skeleton:
```python
class GameSessionManager { // L9-63
    public GameSessionManager(JavaPlugin plugin) { // L16-18
    public GameSession createSession(String worldName, Player host) { // L23-31
    public GameSession getSessionByPlayer(Player player) { // L36-38
    public GameSession getSessionByWorld(String worldName) { // L43-45
    public void terminateSession(String worldName) { // L50-62
```

--------------------------------------------------

