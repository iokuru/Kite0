#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import { ZipArchive } from 'archiver';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const EXTENSION_ROOT = path.resolve(__dirname, '..');

const MATCHES = [
  '*://codeforces.com/*',
  '*://leetcode.com/*',
  '*://www.codechef.com/*',
  '*://atcoder.jp/*',
  '*://www.hackerrank.com/*',
  '*://www.geeksforgeeks.org/*',
  '*://www.hackerearth.com/*',
  '*://cses.fi/*',
  '*://www.onlinegdb.com/*',
  '*://www.jdoodle.com/*',
  '*://www.programiz.com/*',
  '*://replit.com/*',
];

function zipDirectory(sourceDir, outputZip) {
  return new Promise((resolve, reject) => {
    const output = fs.createWriteStream(outputZip);
    const archive = new ZipArchive({ zlib: { level: 9 } });

    output.on('close', () => {
      const sizeKb = (archive.pointer() / 1024).toFixed(1);
      console.log(`Created archive: ${outputZip} (${sizeKb} KB)`);
      resolve();
    });

    archive.on('error', (err) => reject(err));
    archive.pipe(output);
    archive.directory(sourceDir, false);
    archive.finalize();
  });
}

function copyDirRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

async function main() {
  console.log('=== Building Kite0 Browser Extension ===');
  execSync('npm run build', { cwd: EXTENSION_ROOT, stdio: 'inherit', shell: true });

  const distDir = path.join(EXTENSION_ROOT, 'dist');
  const packagesDir = path.join(EXTENSION_ROOT, 'dist-packages');
  fs.mkdirSync(packagesDir, { recursive: true });

  const iconsSrc = path.join(EXTENSION_ROOT, 'public', 'icons');
  const pkgData = JSON.parse(fs.readFileSync(path.join(EXTENSION_ROOT, 'package.json'), 'utf-8'));
  const version = pkgData.version || '0.1.1';

  // 1. Chrome MV3
  console.log(`\n--- Packaging Chrome (Manifest V3, v${version}) ---`);
  const chromeDir = path.join(EXTENSION_ROOT, 'dist-chrome');
  if (fs.existsSync(chromeDir)) {
    fs.rmSync(chromeDir, { recursive: true, force: true });
  }
  copyDirRecursive(distDir, chromeDir);
  copyDirRecursive(iconsSrc, path.join(chromeDir, 'icons'));

  const chromeManifest = {
    manifest_version: 3,
    name: 'Kite0 - Static Complexity Analyzer',
    version,
    description:
      'Deterministic local static complexity analyzer for competitive programming. Zero telemetry, 100% offline WebAssembly.',
    icons: {
      16: 'icons/icon-16.png',
      48: 'icons/icon-48.png',
      128: 'icons/icon-128.png',
    },
    permissions: ['activeTab', 'scripting'],
    content_security_policy: {
      extension_pages: "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';",
    },
    background: {
      service_worker: 'background.js',
      type: 'module',
    },
    action: {
      default_popup: 'src/popup/index.html',
      default_title: 'Kite0 Complexity Analyzer',
      default_icon: {
        16: 'icons/icon-16.png',
        48: 'icons/icon-48.png',
        128: 'icons/icon-128.png',
      },
    },
    content_scripts: [
      {
        matches: MATCHES,
        js: ['content.js'],
      },
    ],
    web_accessible_resources: [
      {
        resources: ['*.wasm', 'assets/*', 'icons/*'],
        matches: ['<all_urls>'],
      },
    ],
  };

  fs.writeFileSync(path.join(chromeDir, 'manifest.json'), JSON.stringify(chromeManifest, null, 2));
  const chromeZip = path.join(packagesDir, `kiteo-chrome-v${version}.zip`);
  await zipDirectory(chromeDir, chromeZip);

  // 2. Firefox (Gecko MV3 / Scripts background)
  console.log(`\n--- Packaging Firefox (v${version}) ---`);
  const firefoxDir = path.join(EXTENSION_ROOT, 'dist-firefox');
  if (fs.existsSync(firefoxDir)) {
    fs.rmSync(firefoxDir, { recursive: true, force: true });
  }
  copyDirRecursive(distDir, firefoxDir);
  copyDirRecursive(iconsSrc, path.join(firefoxDir, 'icons'));

  const firefoxManifest = {
    manifest_version: 3,
    name: 'Kite0 - Static Complexity Analyzer',
    version,
    description:
      'Deterministic local static complexity analyzer for competitive programming. Zero telemetry, 100% offline WebAssembly.',
    browser_specific_settings: {
      gecko: {
        id: 'kiteo@iokuru.github.io',
        strict_min_version: '140.0',
        data_collection_permissions: {
          required: ['none'],
        },
      },
      gecko_android: {
        strict_min_version: '142.0',
      },
    },
    icons: {
      16: 'icons/icon-16.png',
      48: 'icons/icon-48.png',
      128: 'icons/icon-128.png',
    },
    permissions: ['activeTab', 'scripting'],
    content_security_policy: {
      extension_pages: "script-src 'self' 'wasm-unsafe-eval'; object-src 'self';",
    },
    background: {
      scripts: ['background.js'],
    },
    action: {
      default_popup: 'src/popup/index.html',
      default_title: 'Kite0 Complexity Analyzer',
      default_icon: {
        16: 'icons/icon-16.png',
        48: 'icons/icon-48.png',
        128: 'icons/icon-128.png',
      },
    },
    content_scripts: [
      {
        matches: MATCHES,
        js: ['content.js'],
      },
    ],
    web_accessible_resources: [
      {
        resources: ['*.wasm', 'assets/*', 'icons/*'],
        matches: ['<all_urls>'],
      },
    ],
  };

  fs.writeFileSync(path.join(firefoxDir, 'manifest.json'), JSON.stringify(firefoxManifest, null, 2));
  const firefoxZip = path.join(packagesDir, `kiteo-firefox-v${version}.zip`);
  await zipDirectory(firefoxDir, firefoxZip);

  console.log('\n=== Extension Packaging Complete ===');
  console.log(`Chrome distribution:  ${chromeDir} -> ${chromeZip}`);
  console.log(`Firefox distribution: ${firefoxDir} -> ${firefoxZip}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
