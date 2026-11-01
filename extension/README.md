# Kite0 Browser Extension

The official browser extension for **Kite0** — a non-generative, 100% offline static complexity analyzer designed for competitive programmers, software engineers, and technical interview candidates.

---

## Supported Browsers & Platforms

### Browsers
- **Google Chrome, Brave, Microsoft Edge, Opera, Vivaldi** (Chromium Manifest V3)
- **Mozilla Firefox, LibreWolf** (Gecko Manifest V3)

### Competitive Platforms & Web Editors
- **Competitive Platforms**: LeetCode, Codeforces, HackerRank, CodeChef, AtCoder, GeeksforGeeks, HackerEarth, CSES
- **Web IDEs & Sandboxes**: OnlineGDB, JDoodle, Programiz, Replit
- **Editor Engines Supported**: Monaco Editor, CodeMirror (v5 and v6), ACE Editor, and native text areas

---

## Non-Terminal Installation (No Coding or CLI Required)

### 1. Chromium Browsers (Chrome, Brave, Edge, Opera)
1. Download **[`kiteo-chrome-v0.1.1.zip`](dist-packages/kiteo-chrome-v0.1.1.zip)** directly from [`dist-packages/`](dist-packages/).
2. Right-click the `.zip` file and extract it to a folder on your computer.
3. Open your browser and navigate to:
   - Chrome / Brave / Opera: `chrome://extensions/`
   - Edge: `edge://extensions/`
4. In the top-right corner, switch the **Developer mode** toggle to **ON**.
5. Click **Load unpacked** (top-left) and select the extracted folder containing `manifest.json`.
6. Click the extension puzzle icon in your browser toolbar and pin **Kite0**.

### 2. Mozilla Firefox
1. Download **[`kiteo-firefox-v0.1.1.zip`](dist-packages/kiteo-firefox-v0.1.1.zip)** directly from [`dist-packages/`](dist-packages/).
2. Extract the `.zip` archive.
3. In Firefox, navigate to `about:debugging#/runtime/this-firefox`.
4. Click **Load Temporary Add-on...**.
5. Select the `manifest.json` file inside the extracted directory.

---

## Non-Terminal Offline Playground (Zero Install)

You can run static analysis without installing any browser extension or using a terminal:
1. Double-click or open [`test-page.html`](test-page.html) directly in any web browser.
2. Select your language (**C++** or **Java**).
3. Paste any problem solution or code snippet.
4. Click **Analyze Code** — Time Complexity, Space Complexity, and Detected Algorithms are displayed immediately on the page.

---

## Extension Architecture

The extension is engineered with strict privacy isolation and zero telemetry:

```
extension/
├── dist-packages/           # Pre-built, ready-to-load ZIP bundles
│   ├── kiteo-chrome-v0.1.1.zip
│   ├── kiteo-firefox-v0.1.1.zip
│   └── kiteo-source-v0.1.1.zip (Reproducible source for Mozilla AMO)
├── public/                  # Icons and compiled WebAssembly binaries
│   ├── icons/               # 16px, 48px, 128px Kite icons
│   ├── tree-sitter.wasm
│   ├── tree-sitter-cpp.wasm
│   └── tree-sitter-java.wasm
├── scripts/                 # Packaging and verification scripts
│   ├── package.mjs          # Cross-browser zip packager
│   └── package_source.mjs   # Mozilla AMO reproducible source packager
└── src/
    ├── background/          # Minimal service worker
    ├── content/             # Passive DOM reader & floating assistant
    ├── platform/            # Platform-specific editor adapters
    ├── popup/               # Preact UI popup panel
    └── wasm/                # WebAssembly analyzer bridge
```

### Key Privacy & Performance Guarantees:
- **Zero Network Calls**: Does not make `fetch`, `XMLHttpRequest`, or `WebSocket` connections. All analysis executes locally in WebAssembly.
- **Passive Read-Only DOM**: Inspects code text without dispatching synthetic keyboard events, mutating contest timers, or triggering anti-cheat mechanisms.
- **Instant Response**: Analyses complete in under 5 milliseconds on consumer hardware.

---

## Building from Source (Developer Mode)

If you are modifying or compiling the extension from source:

### Prerequisites
- **Node.js** $\ge 20$
- **npm** $\ge 10$

### Build & Package Commands
```bash
# Install dependencies
npm install

# Build production bundles
npm run build

# Package Chrome and Firefox distribution archives
npm run package

# Package reproducible source bundle for Mozilla AMO submission
npm run package:source

# Run Playwright E2E and privacy audit tests
npm test
```

---

## License

This browser extension is part of Kite0 and licensed under the [MIT License](../LICENSE).
