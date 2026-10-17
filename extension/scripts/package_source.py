import os
import zipfile
import json
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXTENSION_DIR = os.path.join(ROOT_DIR, "extension")
PACKAGES_DIR = os.path.join(EXTENSION_DIR, "dist-packages")
os.makedirs(PACKAGES_DIR, exist_ok=True)

with open(os.path.join(EXTENSION_DIR, "package.json"), "r", encoding="utf-8") as f:
    pkg = json.load(f)
version = pkg.get("version", "0.1.1")

source_zip_path = os.path.join(PACKAGES_DIR, f"kiteo-source-v{version}.zip")

# Reviewer README / Building guide
BUILD_INSTRUCTIONS = f"""# Kite0 v{version} - Source Code & Build Instructions for Mozilla Reviewers

## 1. Environment & Prerequisites
- **Operating System**: Linux (Ubuntu 20.04+ / Debian), macOS (12+), or Windows 10/11
- **Node.js**: >= 18.0.0 (Recommended: v20.x or v22.x LTS)
- **npm**: >= 9.0.0
- **Rust & Cargo**: >= 1.75.0 (Stable toolchain)
- **wasm-pack**: >= 0.12.0 (`cargo install wasm-pack`)
- **Python**: >= 3.8

---

## 2. Step-by-Step Build Instructions

### Step 1: Compile the Rust WebAssembly Core Engine
From the repository root:
```bash
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
cd ..
```
This generates the WebAssembly binary and JavaScript bindings at `extension/src/wasm/pkg/`.

### Step 2: Install Extension Dependencies
```bash
cd extension
npm install
```

### Step 3: Build & Package the Extension
```bash
npm run build
python scripts/package.py
```

### Output:
The exact Firefox distribution package will be generated at:
`extension/dist-packages/kiteo-firefox-v{version}.zip`
and the unpacked directory at:
`extension/dist-firefox/`

---

## 3. Automated Single-Step Build Script
Alternatively, run:
- On Linux/macOS:
  ```bash
  chmod +x build.sh
  ./build.sh
  ```
- On Windows:
  ```cmd
  build.bat
  ```

---

## 4. Notes on Third-Party WebAssembly Binaries
The extension uses standard, open-source tree-sitter wasms (`tree-sitter-cpp.wasm`, `tree-sitter-java.wasm`, and `tree-sitter.wasm`) provided by the audited npm packages `tree-sitter-wasms` (v0.1.13) and `web-tree-sitter` (v0.22.6) for client-side AST parsing.
"""

BUILD_SH = f"""#!/usr/bin/env bash
set -e
echo "=== Building Kite0 v{version} from Source ==="
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
cd ../extension
npm install
npm run build
python scripts/package.py
echo "=== Build Complete! Firefox add-on package: extension/dist-packages/kiteo-firefox-v{version}.zip ==="
"""

BUILD_BAT = f"""@echo off
echo === Building Kite0 v{version} from Source ===
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
if %errorlevel% neq 0 exit /b %errorlevel%
cd ../extension
call npm install
if %errorlevel% neq 0 exit /b %errorlevel%
call npm run build
if %errorlevel% neq 0 exit /b %errorlevel%
python scripts/package.py
if %errorlevel% neq 0 exit /b %errorlevel%
echo === Build Complete! Firefox add-on package: extension/dist-packages/kiteo-firefox-v{version}.zip ===
"""

EXCLUDE_DIRS = {
    "node_modules",
    "target",
    "dist",
    "dist-chrome",
    "dist-firefox",
    "dist-packages",
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".vite",
    ".system_generated",
    "tmp",
}

EXCLUDE_EXTENSIONS = {
    ".pyc",
    ".DS_Store",
    ".log",
}

def should_exclude(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    for p in parts:
        if p in EXCLUDE_DIRS:
            return True
    _, ext = os.path.splitext(rel_path)
    if ext in EXCLUDE_EXTENSIONS:
        return True
    return False

print(f"Creating source archive: {source_zip_path}")
with zipfile.ZipFile(source_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    # Add build documentation and helper scripts
    zf.writestr("BUILDING.md", BUILD_INSTRUCTIONS)
    zf.writestr("README.md", BUILD_INSTRUCTIONS)
    zf.writestr("build.sh", BUILD_SH)
    zf.writestr("build.bat", BUILD_BAT)

    # Add Root Cargo files
    for root_file in ["Cargo.toml", "Cargo.lock"]:
        fp = os.path.join(ROOT_DIR, root_file)
        if os.path.exists(fp):
            zf.write(fp, root_file)

    # Add engine/
    engine_dir = os.path.join(ROOT_DIR, "engine")
    for root, dirs, files in os.walk(engine_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, ROOT_DIR)
            if not should_exclude(rel):
                zf.write(full, rel)

    # Add extension/
    for root, dirs, files in os.walk(EXTENSION_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, ROOT_DIR)
            if not should_exclude(rel):
                zf.write(full, rel)

size_mb = os.path.getsize(source_zip_path) / (1024.0 * 1024.0)
print(f"Successfully generated source zip: {source_zip_path} ({size_mb:.2f} MB)")
