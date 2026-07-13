# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] SRC
# ==========================================================================
# 📄 [요청 1] TARGET: src/main/java/com/desertcore/deathevent.java (140-223라인)
# ----------------------------------------------------------
```python
            player.setGameMode(GameMode.SURVIVAL);
            Location lobbyLocation = new Location(lobbyWorld, 0.0, -43.0, 0.0, 0f, 0f);
            player.teleport(lobbyLocation);

            if (previousWorldName.startsWith("desert_")) {
                unloadAndDeleteInstance(previousWorldName);
            }
        }
    }

    @EventHandler
    public void onPlayerCommand(PlayerCommandPreprocessEvent event) {
        Player player = event.getPlayer();
        String message = event.getMessage();
        String currentWorldName = player.getWorld().getName();

        if (message.equalsIgnoreCase("/lobby_confirm")) {
            event.setCancelled(true);
            World lobbyWorld = Bukkit.getWorld("world");
            if (lobbyWorld != null) {
                promptActive.remove(player.getUniqueId());
                cancelTimer(player.getUniqueId());
                player.setGameMode(GameMode.SURVIVAL);

                Location lobbyLocation = new Location(lobbyWorld, 0.0, -43.0, 0.0, 0f, 0f);
                player.teleport(lobbyLocation);
                player.sendMessage(Component.text("[!] 안전하게 로비로 복귀했습니다.").color(NamedTextColor.GREEN));

                if (currentWorldName.startsWith("desert_")) {
                    unloadAndDeleteInstance(currentWorldName);
                }
            }
        } else if (message.equalsIgnoreCase("/lobby_cancel")) {
            event.setCancelled(true);
            promptActive.remove(player.getUniqueId());
            cancelTimer(player.getUniqueId());
            player.sendMessage(Component.text("[!] 전장을 계속 관전합니다. (다시 나가려면 Shift를 3초간 유지)").color(NamedTextColor.GRAY));
        }
    }

    // ★ [오류 해결] FileUtils 대신 자바 순정 내장 API로 월드 사본 폴더 제거
    private void unloadAndDeleteInstance(String instanceName) {
        var plugin = Bukkit.getPluginManager().getPlugin("desertcore");
        if (plugin == null) return;

        Bukkit.getScheduler().runTaskLater(plugin, () -> {
            World instanceWorld = Bukkit.getWorld(instanceName);
            if (instanceWorld != null) {
                if (instanceWorld.getPlayers().isEmpty()) {
                    Bukkit.unloadWorld(instanceWorld, false);

                    // 비동기로 폴더 트리 삭제 수행
                    Bukkit.getScheduler().runTaskAsynchronously(plugin, () -> {
                        File instanceDir = new File(Bukkit.getWorldContainer(), instanceName);
                        if (instanceDir.exists()) {
                            try {
                                deleteDirectoryNative(instanceDir.toPath());
                            } catch (IOException e) {
                                plugin.getLogger().warning(instanceName + " 사본 월드 폴더 삭제 중 예외 발생");
                            }
                        }
                    });
                }
            }
        }, 20L);
    }

    // 자바 내장 폴더 삭제용 헬퍼 메소드
    private void deleteDirectoryNative(Path path) throws IOException {
        Files.walkFileTree(path, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                Files.delete(file);
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
                Files.delete(dir);
                return FileVisitResult.CONTINUE;
            }
        });
    }
}
```

# 📄 [요청 2] TARGET: src/main/java/com/desertcore/lobbycmd.java (18-48라인)
# ----------------------------------------------------------
```python
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) {

        // 1. 명령어를 친 대상이 플레이어인지 확인 (콘솔창 입력 방지)
        if (!(sender instanceof Player)) {
            sender.sendMessage(Component.text("이 명령어는 인게임 플레이어만 사용할 수 있습니다.").color(NamedTextColor.RED));
            return true;
        }

        Player player = (Player) sender;

        // 2. [핵심] 오퍼레이터(OP) 권한이 있는지 체크
        if (!player.isOp()) {
            player.sendMessage(Component.text("❌ 이 명령어를 사용할 권한이 없습니다. (OP 전용)").color(NamedTextColor.RED));
            return true;
        }

        // 3. 로비 월드("world") 정보 가져오기
        World lobbyWorld = Bukkit.getWorld("world");
        if (lobbyWorld != null) {
            // 서바이벌 모드로 안전하게 변경 후 지정된 로비 좌표로 텔레포트
            player.setGameMode(GameMode.SURVIVAL);
            Location lobbyLocation = new Location(lobbyWorld, 0.0, -44.0, 17.0, 180f, 0f);
            player.teleport(lobbyLocation);

            player.sendMessage(Component.text("[!] 관리자 권한으로 로비에 강제 복귀했습니다.").color(NamedTextColor.GREEN));
        } else {
            player.sendMessage(Component.text("❌ 'world' 월드를 찾을 수 없습니다. 월드 이름을 확인해 주세요.").color(NamedTextColor.RED));
        }

        return true;
    }
```
