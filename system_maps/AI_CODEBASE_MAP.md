# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (INTELLIGENT SCAN)

> **[AI 프로토콜 매뉴얼]** 이 문서는 다른 AI 비서들의 경로 오해를 차단하기 위해 파일마다 **실제 하드디스크 상대 경로 `[📂 실제경로]`**를 강제 명시해 둔 특수 지도입니다.
> AI 비서는 절대 눈치로 경로를 추측하지 말고, 파일명 뒤에 박혀있는 `[📂 실제경로]` 규격을 그대로 복사하여 agent_navigator를 호출하십시오.

```markdown
extraction_target_project/
├── .gitignore [📂 .gitignore]
├── client/
│   ├── .gitignore [📂 client/.gitignore]
│   ├── package-lock.json [📂 client/package-lock.json] -> [💡 📦 json_keys: 5개 포착 | 🔑 "name" [str] | 🔑 "version" [str] | 🔑 "lockfileVersion" [int] | 🔑 "requires" [bool] | 🔑 "packages" [dict]]
│   ├── package.json [📂 client/package.json] -> [💡 📦 json_keys: 7개 포착 | 🔑 "name" [str] | 🔑 "version" [str] | 🔑 "private" [bool] | 🔑 "dependencies" [dict] | 🔑 "scripts" [dict] | ...외 2개]
│   ├── public/
│   │   ├── favicon.ico [📂 client/public/favicon.ico]
│   │   ├── favicon.svg [📂 client/public/favicon.svg]
│   │   ├── index.html [📂 client/public/index.html]
│   │   ├── logo.svg [📂 client/public/logo.svg]
│   │   ├── logo192.png [📂 client/public/logo192.png]
│   │   ├── logo512.png [📂 client/public/logo512.png]
│   │   ├── manifest.json [📂 client/public/manifest.json] -> [💡 📦 json_keys: 7개 포착 | 🔑 "short_name" [str] | 🔑 "name" [str] | 🔑 "icons" [list] | 🔑 "start_url" [str] | 🔑 "display" [str] | ...외 2개]
│   ├── src/
│   │   ├── App.css [📂 client/src/App.css]
│   │   ├── App.js [📂 client/src/App.js] -> [💡 📦 imp: ./Canvas, ./Home, react, react-hot-toast, react-router-dom | 🎯 def App() [L11]]
│   │   ├── App.test.js [📂 client/src/App.test.js] -> [💡 📦 imp: ./App, @testing-library/react]
│   │   ├── Button.js [📂 client/src/Button.js] -> [💡 📦 imp: react | 🎯 def Button() [L4]]
│   │   ├── Canvas.js [📂 client/src/Canvas.js] -> [💡 📦 imp: ./Button, ./UploadFile, ./hooks/useWebRTC, ./socket, react, react-hot-toast, react-icons/ai, react-icons/fa6, react-router-dom | 🎯 def RemoteAudio() [L24] | 🎯 def Canvas() [L34] | 🎯 def changeColour() [L61] | 🎯 def lineWidth() [L66] | 🎯 def handleImageUploadSuccess() [L74] | 🎯 def init() [L85] | 🎯 def handleError() [L96] | 🎯 def handleDraw() [L165] | 🎯 def handleMoveDraw() [L177] | 🎯 def handleNotDraw() [L193] | 🎯 def undo() [L202] | 🎯 def redrawCanvas() [L212] | 🎯 def handleCanvasChange() [L236] | 🎯 def clearCanvas() [L250] | 🎯 def copyBoardId() [L259] | 🎯 def leaveBoard() [L264]]
│   │   ├── Home.js [📂 client/src/Home.js] -> [💡 📦 imp: react, react-hot-toast, react-router-dom, uuid | 🎯 def Home() [L8] | 🎯 def writeId() [L14] | 🎯 def writeUserName() [L20] | 🎯 def generateUniqueId() [L24] | 🎯 def joinBoard() [L31]]
│   │   ├── hooks/
│   │   │   ├── useWebRTC.js [📂 client/src/hooks/useWebRTC.js] -> [💡 📦 imp: react, react-hot-toast | 🎯 def useWebRTC() [L11]]
│   │   ├── index.css [📂 client/src/index.css]
│   │   ├── index.js [📂 client/src/index.js] -> [💡 📦 imp: ./App, ./reportWebVitals, react, react-dom/client]
│   │   ├── Input.js [📂 client/src/Input.js] -> [💡 📦 imp: react | 🎯 def Input() [L3]]
│   │   ├── reportWebVitals.js [📂 client/src/reportWebVitals.js]
│   │   ├── setupTests.js [📂 client/src/setupTests.js]
│   │   ├── socket.js [📂 client/src/socket.js] -> [💡 📦 imp: socket.io-client | 🎯 def initSocket() [L3]]
│   │   ├── style.css [📂 client/src/style.css]
│   │   ├── styleCanvas.css [📂 client/src/styleCanvas.css]
│   │   ├── UploadFile.js [📂 client/src/UploadFile.js] -> [💡 📦 imp: react, react-icons/fa6 | 🎯 def UploadFile() [L5] | 🎯 def upload() [L8]]
├── index.js [📂 index.js] -> [💡 📦 imp: dateuuidv2, express, http, path, socket.io, url | 🎯 def getAllConnectedClients() [L22]]
├── package-lock.json [📂 package-lock.json] -> [💡 📦 json_keys: 5개 포착 | 🔑 "name" [str] | 🔑 "version" [str] | 🔑 "lockfileVersion" [int] | 🔑 "requires" [bool] | 🔑 "packages" [dict]]
├── package.json [📂 package.json] -> [💡 📦 json_keys: 8개 포착 | 🔑 "name" [str] | 🔑 "version" [str] | 🔑 "description" [str] | 🔑 "type" [str] | 🔑 "main" [str] | ...외 3개]
├── prompt.md [📂 prompt.md]
├── README.md [📂 README.md]
