#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { ZipArchive } from 'archiver';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..', '..');
const EXTENSION_DIR = path.join(ROOT_DIR, 'extension');
const PACKAGES_DIR = path.join(EXTENSION_DIR, 'dist-packages');
fs.mkdirSync(PACKAGES_DIR, { recursive: true });

const pkg = JSON.parse(fs.readFileSync(path.join(EXTENSION_DIR, 'package.json'), 'utf-8'));
const version = pkg.version || '0.1.1';
const sourceZipPath = path.join(PACKAGES_DIR, `kiteo-source-v${version}.zip`);

const BUILD_INSTRUCTIONS = `# Kite0 v${version} - Source Code & Build Instructions for Mozilla Reviewers

## 1. Environment & Prerequisites
- **Operating System**: Linux (Ubuntu 20.04+ / Debian), macOS (12+), or Windows 10/11
- **Node.js**: >= 18.0.0 (Recommended: v20.x or v22.x LTS)
- **npm**: >= 9.0.0
- **Rust & Cargo**: >= 1.75.0 (Stable toolchain)
- **wasm-pack**: >= 0.12.0 (\`cargo install wasm-pack\`)

---

## 2. Step-by-Step Build Instructions

### Step 1: Compile the Rust WebAssembly Core Engine
From the repository root:
\`\`\`bash
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
cd ..
\`\`\`
This generates the WebAssembly binary and JavaScript bindings at \`extension/src/wasm/pkg/\`.

### Step 2: Install Extension Dependencies
\`\`\`bash
cd extension
npm install
\`\`\`

### Step 3: Build & Package the Extension
\`\`\`bash
npm run build
node scripts/package.mjs
\`\`\`

### Output:
The exact Firefox distribution package will be generated at:
\`extension/dist-packages/kiteo-firefox-v${version}.zip\`
and the unpacked directory at:
\`extension/dist-firefox/\`

---

## 3. Automated Single-Step Build Script
Alternatively, run:
- On Linux/macOS:
  \`\`\`bash
  chmod +x build.sh
  ./build.sh
  \`\`\`
- On Windows:
  \`\`\`cmd
  build.bat
  \`\`\`

---

## 4. Notes on Third-Party WebAssembly Binaries
The extension uses standard, open-source tree-sitter wasms (\`tree-sitter-cpp.wasm\`, \`tree-sitter-java.wasm\`, and \`tree-sitter.wasm\`) provided by the audited npm packages \`tree-sitter-wasms\` (v0.1.13) and \`web-tree-sitter\` (v0.22.6) for client-side AST parsing.
`;

const BUILD_SH = `#!/usr/bin/env bash
set -e
echo "=== Building Kite0 v${version} from Source ==="
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
cd ../extension
npm install
npm run build
node scripts/package.mjs
echo "=== Build Complete! Firefox add-on package: extension/dist-packages/kiteo-firefox-v${version}.zip ==="
`;

const BUILD_BAT = `@echo off
echo === Building Kite0 v${version} from Source ===
cd engine
wasm-pack build --target web --out-dir ../extension/src/wasm/pkg
if %errorlevel% neq 0 exit /b %errorlevel%
cd ../extension
call npm install
if %errorlevel% neq 0 exit /b %errorlevel%
call npm run build
if %errorlevel% neq 0 exit /b %errorlevel%
node scripts/package.mjs
if %errorlevel% neq 0 exit /b %errorlevel%
echo === Build Complete! Firefox add-on package: extension/dist-packages/kiteo-firefox-v${version}.zip ===
`;

const EXCLUDE_DIRS = new Set([
  'node_modules',
  'target',
  'dist',
  'dist-chrome',
  'dist-firefox',
  'dist-packages',
  '.git',
  '.github',
  '.idea',
  '.vscode',
  '.vite',
  '.cache',
  'tmp',
]);

const EXCLUDE_EXTENSIONS = new Set(['.DS_Store', '.log']);

function walkDir(dir, fileList = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (EXCLUDE_DIRS.has(entry.name)) continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkDir(fullPath, fileList);
    } else {
      const ext = path.extname(entry.name);
      if (!EXCLUDE_EXTENSIONS.has(ext)) {
        fileList.push(fullPath);
      }
    }
  }
  return fileList;
}

async function main() {
  console.log(`Creating source archive: ${sourceZipPath}`);
  const output = fs.createWriteStream(sourceZipPath);
  const archive = new ZipArchive({ zlib: { level: 9 } });

  const done = new Promise((resolve, reject) => {
    output.on('close', () => {
      const sizeMb = (archive.pointer() / (1024 * 1024)).toFixed(2);
      console.log(`Successfully generated source zip: ${sourceZipPath} (${sizeMb} MB)`);
      resolve();
    });
    archive.on('error', (err) => reject(err));
  });

  archive.pipe(output);

  archive.append(BUILD_INSTRUCTIONS, { name: 'BUILDING.md' });
  archive.append(BUILD_INSTRUCTIONS, { name: 'README.md' });
  archive.append(BUILD_SH, { name: 'build.sh' });
  archive.append(BUILD_BAT, { name: 'build.bat' });

  for (const rootFile of ['Cargo.toml', 'Cargo.lock']) {
    const fp = path.join(ROOT_DIR, rootFile);
    if (fs.existsSync(fp)) {
      archive.file(fp, { name: rootFile });
    }
  }

  const engineFiles = walkDir(path.join(ROOT_DIR, 'engine'));
  for (const file of engineFiles) {
    const rel = path.relative(ROOT_DIR, file).replace(/\\/g, '/');
    archive.file(file, { name: rel });
  }

  const extensionFiles = walkDir(EXTENSION_DIR);
  for (const file of extensionFiles) {
    const rel = path.relative(ROOT_DIR, file).replace(/\\/g, '/');
    archive.file(file, { name: rel });
  }

  archive.finalize();
  await done;
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
