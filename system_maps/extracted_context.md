# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] SRC
# ==========================================================================
# 📄 [요청 1] TARGET: src/main/java/com/desertcore/deathevent.java (32-60라인)
# ----------------------------------------------------------
```python
public class deathevent implements Listener {

    private final HashSet<UUID> promptActive = new HashSet<>();
    private final HashMap<UUID, BukkitRunnable> activeTimers = new HashMap<>();

    @EventHandler
    public void onPlayerDeath(PlayerDeathEvent event) {
        Player player = event.getEntity();
        String currentWorld = player.getWorld().getName();

        if (currentWorld.startsWith("desert_")) {
            event.setKeepInventory(true);
            event.getDrops().clear();

            var plugin = Bukkit.getPluginManager().getPlugin("desertcore");
            if (plugin != null) {
                Bukkit.getScheduler().runTaskLater(plugin, () -> player.spigot().respawn(), 1L);
            }
        }
    }

    @EventHandler
    public void onPlayerRespawn(PlayerRespawnEvent event) {
        Player player = event.getPlayer();
        String currentWorld = player.getWorld().getName();

        if (currentWorld.startsWith("desert_")) {
            event.setRespawnLocation(player.getLocation());
```
