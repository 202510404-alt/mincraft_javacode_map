# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] EXTRACTION_TARGET_PROJECT
# ==========================================================================
# 📄 [요청 1] TARGET: extraction_target_project/client/src/Canvas.js (1-120라인)
# ----------------------------------------------------------
```python
import React, { useRef, useEffect, useState } from "react";
import UploadFile from './UploadFile';
import './style.css';
import './styleCanvas.css';
import { initSocket } from "./socket";
import { useNavigate, useLocation, useParams } from "react-router-dom";
import toast from "react-hot-toast";
import Button from "./Button";
import { AiOutlineClear } from "react-icons/ai";
import { FaImage, FaRegSquareMinus } from "react-icons/fa6";
import {
  FaRegPlusSquare,
  FaMicrophone,
  FaMicrophoneSlash,
  FaUndoAlt,
  FaPhone,
  FaPhoneSlash,
  FaCopy,
  FaSignOutAlt,
  FaUserFriends
} from "react-icons/fa";
import { useWebRTC } from "./hooks/useWebRTC";

function RemoteAudio({ stream }) {
  const audioRef = useRef(null);
  useEffect(() => {
    if (audioRef.current && stream) {
      audioRef.current.srcObject = stream;
    }
  }, [stream]);
  return <audio ref={audioRef} autoPlay playsInline />;
}

function Canvas(props) {
  const [clients, setClients] = useState([]);
  const socketRef = useRef(null);
  const location = useLocation();
  const { boardId } = useParams();
  const navigate = useNavigate();

  const [width, setWidth] = useState(1.0);
  const [drawing, setDrawing] = useState(false);
  const canvasRef = useRef(null);
  const [imageDraw, setImageDraw] = useState(null);
  const [shapeColor, setShapeColor] = useState("#000000");
  const [linesHistory, setLinesHistory] = useState([]);
  const [currentLine, setCurrentLine] = useState([]);

  // WebRTC Hook Integration
  const userName = location.state?.userName || "익명 유저";
  const {
    remoteStreams,
    voiceUsers,
    isVoiceConnected,
    isMuted,
    joinVoice,
    leaveVoice,
    toggleMute,
  } = useWebRTC(socketRef, boardId, userName);

  function changeColour(event) {
    let color = event.target.value;
    setShapeColor(color);
  }

  function lineWidth(event) {
    let name = event.target.name;
    if (name === 'increase')
      setWidth((prev) => (prev < 10 ? prev + 1 : prev));
    else if (name === 'decrease')
      setWidth((prev) => (prev > 1 ? prev - 1 : prev));
  }

  const handleImageUploadSuccess = (imageUrl) => {
    setImageDraw(imageUrl);
    if (socketRef.current) {
      socketRef.current.emit("image_update", {
        boardId,
        imageUrl,
      });
    }
  };

  useEffect(() => {
    const init = async () => {
      if (!location.state?.userName) {
        toast.error("사용자 이름이 필요합니다.");
        navigate("/");
        return;
      }

      socketRef.current = await initSocket();
      socketRef.current.on('connect_error', (err) => handleError(err));
      socketRef.current.on('connect_failed', (err) => handleError(err));

      const handleError = (err) => {
        console.log('socket error', err);
        toast.error("소켓 연결에 실패했습니다");
        navigate("/");
      };

      socketRef.current.emit('join', {
        boardId,
        userName: location.state.userName,
      });

      socketRef.current.on('joined', ({ clients, userName, socketId }) => {
        if (userName !== location.state.userName) {
          toast.success(`${userName}님이 참가했습니다`);
        }
        setClients(clients);
      });

      socketRef.current.on("disconnected", ({ socketId, userName }) => {
        toast.success(`${userName}님이 보드를 나갔습니다`);
        setClients((prev) => prev.filter((client) => client.socketId !== socketId));
      });

      socketRef.current.on("board_change", ({ code }) => {
        if (code !== null) {
```

# 📄 [요청 2] TARGET: extraction_target_project/client/src/hooks/useWebRTC.js (1-160라인)
# ----------------------------------------------------------
```python
import { useState, useRef, useCallback, useEffect } from "react";
import toast from "react-hot-toast";

const ICE_SERVERS = {
  iceServers: [
    { urls: "stun:stun.l.google.com:19302" },
    { urls: "stun:stun1.l.google.com:19302" },
  ],
};

export function useWebRTC(socketRef, boardId, userName) {
  const [localStream, setLocalStream] = useState(null);
  const [remoteStreams, setRemoteStreams] = useState({}); // { [socketId]: MediaStream }
  const [voiceUsers, setVoiceUsers] = useState([]); // [{ socketId, userName, isMuted }]
  const [isVoiceConnected, setIsVoiceConnected] = useState(false);
  const [isMuted, setIsMuted] = useState(false);

  const peerConnections = useRef(new Map()); // Map<socketId, RTCPeerConnection>
  const localStreamRef = useRef(null);
  const isMutedRef = useRef(false);

  // Helper to create RTCPeerConnection for a remote peer
  const createPeerConnection = useCallback((targetSocketId) => {
    if (peerConnections.current.has(targetSocketId)) {
      return peerConnections.current.get(targetSocketId);
    }

    const pc = new RTCPeerConnection(ICE_SERVERS);
    peerConnections.current.set(targetSocketId, pc);

    // Add local tracks to peer connection
    if (localStreamRef.current) {
      localStreamRef.current.getTracks().forEach((track) => {
        pc.addTrack(track, localStreamRef.current);
      });
    }

    // Handle incoming ICE candidate
    pc.onicecandidate = (event) => {
      if (event.candidate && socketRef.current) {
        socketRef.current.emit("ice-candidate", {
          targetSocketId,
          candidate: event.candidate,
        });
      }
    };

    // Handle incoming remote stream
    pc.ontrack = (event) => {
      if (event.streams && event.streams[0]) {
        const stream = event.streams[0];
        setRemoteStreams((prev) => ({
          ...prev,
          [targetSocketId]: stream,
        }));
      }
    };

    pc.onconnectionstatechange = () => {
      if (
        pc.connectionState === "disconnected" ||
        pc.connectionState === "failed" ||
        pc.connectionState === "closed"
      ) {
        // Handle disconnect if needed
      }
    };

    return pc;
  }, [socketRef]);

  // Clean up a specific peer connection
  const closePeerConnection = useCallback((targetSocketId) => {
    const pc = peerConnections.current.get(targetSocketId);
    if (pc) {
      pc.onicecandidate = null;
      pc.ontrack = null;
      pc.close();
      peerConnections.current.delete(targetSocketId);
    }
    setRemoteStreams((prev) => {
      const next = { ...prev };
      delete next[targetSocketId];
      return next;
    });
  }, []);

  // Leave Voice Call & Cleanup
  const leaveVoice = useCallback(() => {
    if (socketRef.current && isVoiceConnected) {
      socketRef.current.emit("leave-voice", { boardId });
    }

    // Stop local stream tracks
    if (localStreamRef.current) {
      localStreamRef.current.getTracks().forEach((track) => track.stop());
      localStreamRef.current = null;
    }
    setLocalStream(null);

    // Close all PeerConnections
    peerConnections.current.forEach((pc, sid) => {
      pc.onicecandidate = null;
      pc.ontrack = null;
      pc.close();
    });
    peerConnections.current.clear();

    setRemoteStreams({});
    setVoiceUsers([]);
    setIsVoiceConnected(false);
    setIsMuted(false);
    isMutedRef.current = false;

    // Remove socket listeners
    if (socketRef.current) {
      socketRef.current.off("voice-users");
      socketRef.current.off("user-joined-voice");
      socketRef.current.off("offer");
      socketRef.current.off("answer");
      socketRef.current.off("ice-candidate");
      socketRef.current.off("user-left-voice");
      socketRef.current.off("user-mute-changed");
    }
  }, [socketRef, boardId, isVoiceConnected]);

  // Join Voice Call
  const joinVoice = useCallback(async () => {
    if (!socketRef.current) {
      toast.error("소켓 연결이 완료되지 않았습니다.");
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
        video: false,
      });
      localStreamRef.current = stream;
      setLocalStream(stream);
      setIsVoiceConnected(true);
      toast.success("음성 채널에 연결되었습니다.");

      const socket = socketRef.current;

      // Socket Listeners for Signaling
      socket.on("voice-users", async (users) => {
        setVoiceUsers(users);

        // Initiate connection to existing users
        for (const user of users) {
          if (user.socketId !== socket.id) {
            const pc = createPeerConnection(user.socketId);
            try {
              const offer = await pc.createOffer();
              await pc.setLocalDescription(offer);
              socket.emit("offer", {
                targetSocketId: user.socketId,
                offer,
              });
```

# 📄 [요청 3] TARGET: extraction_target_project/client/src/socket.js (1-19라인)
# ----------------------------------------------------------
```python
import { io } from "socket.io-client";

export const initSocket = async () => {
  const options = {
    "force new connection": true,
    reconnectionAttempt: "infinity",
    timeout: 10000,
    transports: ["websocket"],
  };

  // 개발: React(3000) → 서버(7605) / 빌드 후: 같은 서버 origin 사용
  const serverUrl =
    process.env.REACT_APP_SOCKET_URL ||
    (process.env.NODE_ENV === "production"
      ? window.location.origin
      : "http://localhost:7605");

  return io(serverUrl, options);
};
```

# 📄 [요청 4] TARGET: extraction_target_project/client/src/Canvas.js (121-270라인)
# ----------------------------------------------------------
```python
          if (canvasRef.current) {
            const context = canvasRef.current.getContext('2d');
            const image = new Image();
            image.src = code;
            image.onload = () => context.drawImage(image, 0, 0);
          }
        }
      });

      socketRef.current.on("image_update", ({ imageUrl }) => {
        setImageDraw(imageUrl);
      });
    };

    init();

    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
        socketRef.current.off("joined");
        socketRef.current.off("disconnected");
      }
    };
  }, [boardId, location.state, navigate]);

  useEffect(() => {
    const imageContext = canvasRef.current?.getContext('2d');
    if (imageContext && imageDraw) {
      const image = new Image();
      image.src = imageDraw;
      image.onload = () => {
        imageContext.drawImage(image, 90, 90, 650, 500);
      };
    }
  }, [imageDraw]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const context = canvas.getContext('2d');
      redrawCanvas(context);
    }
  }, []);

  const handleDraw = (e) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const context = canvas.getContext('2d');
    const rect = canvas.getBoundingClientRect();
    setDrawing(true);
    setCurrentLine([{ x: e.clientX - rect.left, y: e.clientY - rect.top, color: shapeColor, size: width }]);
    context.beginPath();
    context.moveTo(e.clientX - rect.left, e.clientY - rect.top);
    canvas.dispatchEvent(new CustomEvent('canvasChange'));
  };

  const handleMoveDraw = (e) => {
    if (!drawing) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const context = canvas.getContext('2d');
    const rect = canvas.getBoundingClientRect();
    const newPoint = { x: e.clientX - rect.left, y: e.clientY - rect.top, color: shapeColor, size: width };
    setCurrentLine([...currentLine, newPoint]);

    context.lineTo(newPoint.x, newPoint.y);
    context.strokeStyle = shapeColor;
    context.lineWidth = width;
    context.stroke();
    canvas.dispatchEvent(new CustomEvent('canvasChange'));
  };

  const handleNotDraw = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    setDrawing(false);
    setLinesHistory([...linesHistory, currentLine]);
    setCurrentLine([]);
    canvas.dispatchEvent(new CustomEvent('canvasChange'));
  };

  const undo = () => {
    if (linesHistory.length > 0) {
      const newHistory = linesHistory.slice(0, -1);
      setLinesHistory(newHistory);

      const context = canvasRef.current.getContext('2d');
      redrawCanvas(context);
    }
  };

  const redrawCanvas = (context) => {
    if (!canvasRef.current) return;
    context.clearRect(0, 0, canvasRef.current.width, canvasRef.current.height);
    const canvas = canvasRef.current;
    linesHistory.forEach(line => {
      context.beginPath();
      line.forEach((point, index) => {
        if (index === 0) {
          context.moveTo(point.x, point.y);
        } else {
          context.lineTo(point.x, point.y);
        }
      });
      context.strokeStyle = line[0].color;
      context.lineWidth = line[0].size;
      context.stroke();
      canvas.dispatchEvent(new CustomEvent('canvasChange'));
    });
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const handleCanvasChange = () => {
      const code = canvas.toDataURL();
      if (socketRef.current) {
        socketRef.current.emit('board_change', { boardId, code });
      }
    };

    canvas.addEventListener('canvasChange', handleCanvasChange);

    return () => {
      canvas.removeEventListener('canvasChange', handleCanvasChange);
    };
  }, [boardId]);

  function clearCanvas() {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
    setLinesHistory([]);
    canvas.dispatchEvent(new CustomEvent('canvasChange'));
  }

  const copyBoardId = () => {
    navigator.clipboard.writeText(boardId);
    toast.success("보드 ID가 클립보드에 복사되었습니다!");
  };

  const leaveBoard = () => {
    navigate("/");
  };

  return (
    <div className="canvasPage">
      {/* Remote Audio Players */}
```

# 📄 [요청 5] TARGET: extraction_target_project/client/src/hooks/useWebRTC.js (161-230라인)
# ----------------------------------------------------------
```python
            } catch (err) {
              console.error("Error creating offer:", err);
            }
          }
        }
      });

      socket.on("user-joined-voice", ({ socketId, userName: remoteName, isMuted: remoteMuted }) => {
        toast.info(`${remoteName}님이 음성 채널에 입장하셨습니다.`);
        setVoiceUsers((prev) => [
          ...prev.filter((u) => u.socketId !== socketId),
          { socketId, userName: remoteName, isMuted: remoteMuted },
        ]);
      });

      socket.on("offer", async ({ callerSocketId, offer }) => {
        const pc = createPeerConnection(callerSocketId);
        try {
          await pc.setRemoteDescription(new RTCSessionDescription(offer));
          const answer = await pc.createAnswer();
          await pc.setLocalDescription(answer);
          socket.emit("answer", {
            targetSocketId: callerSocketId,
            answer,
          });
        } catch (err) {
          console.error("Error handling offer:", err);
        }
      });

      socket.on("answer", async ({ responderSocketId, answer }) => {
        const pc = peerConnections.current.get(responderSocketId);
        if (pc) {
          try {
            await pc.setRemoteDescription(new RTCSessionDescription(answer));
          } catch (err) {
            console.error("Error setting remote description from answer:", err);
          }
        }
      });

      socket.on("ice-candidate", async ({ senderSocketId, candidate }) => {
        const pc = peerConnections.current.get(senderSocketId);
        if (pc) {
          try {
            await pc.addIceCandidate(new RTCIceCandidate(candidate));
          } catch (err) {
            console.error("Error adding ice candidate:", err);
          }
        }
      });

      socket.on("user-left-voice", ({ socketId }) => {
        closePeerConnection(socketId);
        setVoiceUsers((prev) => prev.filter((u) => u.socketId !== socketId));
      });

      socket.on("user-mute-changed", ({ socketId, isMuted: remoteMuted }) => {
        setVoiceUsers((prev) =>
          prev.map((u) => (u.socketId === socketId ? { ...u, isMuted: remoteMuted } : u))
        );
      });

      // Join voice channel on server
      socket.emit("join-voice", { boardId, userName });

    } catch (err) {
      console.error("Mic permission error:", err);
      toast.error("마이크 접근 권한이 없거나 마이크를 찾을 수 없습니다.");
      leaveVoice();
```

# 📄 [요청 6] TARGET: extraction_target_project/index.js (1-120라인)
# ----------------------------------------------------------
```python
import express from "express";
import { createServer } from "http";
import { Server } from "socket.io";
import path from "path";
import { extractDate } from "dateuuidv2";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const clientBuildPath = path.join(__dirname, "client", "build");
const PORT = process.env.PORT || 7605;

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer);
const userSocketMap = {};
const boardUsersMap = {};
const voiceUsersMap = {};

app.use(express.static(clientBuildPath));

function getAllConnectedClients(boardId) {
  const usernames = boardUsersMap[boardId] || [];
  return usernames.map(userName => ({
    socketId: userSocketMap[userName],
    userName,
  }));
}

io.on("connection", (socket) => {
  socket.on("join", ({ boardId, userName }) => {
    if (boardUsersMap[boardId]?.includes(userName)) {
      return;
    }

    userSocketMap[userName] = socket.id;
    boardUsersMap[boardId] = boardUsersMap[boardId] || [];
    boardUsersMap[boardId].push(userName);

    console.log("User joined:", userName, "Socket ID:", socket.id);
    socket.join(boardId);

    const clients = getAllConnectedClients(boardId);

    clients.forEach(({ socketId }) => {
      io.to(socketId).emit("joined", {
        clients,
        userName,
        socketId: socket.id,
      });
    });
  });

  socket.on("board_change", ({ boardId, code }) => {
    socket.in(boardId).emit("board_change", { code });
  });

  socket.on("image_update", ({ boardId, imageUrl }) => {
    socket.in(boardId).emit("image_update", { imageUrl });
  });

  // WebRTC Voice Signaling Events
  socket.on("join-voice", ({ boardId, userName }) => {
    if (!voiceUsersMap[boardId]) {
      voiceUsersMap[boardId] = {};
    }
    voiceUsersMap[boardId][socket.id] = { userName, isMuted: false };

    // Send existing voice users list to the joining user
    const voiceUsersList = Object.keys(voiceUsersMap[boardId]).map((sid) => ({
      socketId: sid,
      userName: voiceUsersMap[boardId][sid].userName,
      isMuted: voiceUsersMap[boardId][sid].isMuted,
    }));
    socket.emit("voice-users", voiceUsersList);

    // Notify other users in the board about the new voice user
    socket.in(boardId).emit("user-joined-voice", {
      socketId: socket.id,
      userName,
      isMuted: false,
    });
  });

  socket.on("leave-voice", ({ boardId }) => {
    if (voiceUsersMap[boardId] && voiceUsersMap[boardId][socket.id]) {
      delete voiceUsersMap[boardId][socket.id];
      if (Object.keys(voiceUsersMap[boardId]).length === 0) {
        delete voiceUsersMap[boardId];
      }
    }
    socket.in(boardId).emit("user-left-voice", { socketId: socket.id });
  });

  socket.on("offer", ({ targetSocketId, offer }) => {
    io.to(targetSocketId).emit("offer", {
      callerSocketId: socket.id,
      offer,
    });
  });

  socket.on("answer", ({ targetSocketId, answer }) => {
    io.to(targetSocketId).emit("answer", {
      responderSocketId: socket.id,
      answer,
    });
  });

  socket.on("ice-candidate", ({ targetSocketId, candidate }) => {
    io.to(targetSocketId).emit("ice-candidate", {
      senderSocketId: socket.id,
      candidate,
    });
  });

  socket.on("mute-changed", ({ boardId, isMuted }) => {
    if (voiceUsersMap[boardId] && voiceUsersMap[boardId][socket.id]) {
      voiceUsersMap[boardId][socket.id].isMuted = isMuted;
    }
    socket.in(boardId).emit("user-mute-changed", {
```
