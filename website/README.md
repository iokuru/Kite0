# Kite0 Website & Documentation

The official website and interactive documentation portal for **Kite0** — the 100% offline, deterministic static complexity analyzer.

---

## Overview

Built with [Astro](https://astro.build), this website provides:
- **Interactive Complexity Visualizer**: Real-time browser demo powered by the Kite0 WebAssembly engine.
- **Algorithm Taxonomy & Catalog Explorer**: Searchable reference of all 68 canonical algorithmic patterns and suppression rules.
- **Architecture & ADR Viewer**: Interactive reader for Architecture Decision Records.
- **One-Click Extension Download**: Pre-packaged distribution archives for Chrome, Brave, Edge, and Firefox.

---

## Project Structure

```
website/
├── public/                  # Static assets (favicons, banners, illustrations)
├── src/
│   ├── components/          # Reusable Astro & UI widgets
│   ├── layouts/             # Page layouts
│   └── pages/               # Route endpoints (index.astro, docs, etc.)
└── package.json
```

---

## Local Development Commands

All commands are run from `website/`:

| Command | Action |
| :--- | :--- |
| `npm install` | Install website dependencies |
| `npm run dev` | Start local development server at `http://localhost:4321` |
| `npm run build` | Build static production site to `dist/` |
| `npm run preview` | Preview production build locally |

---

## License

Part of Kite0 and licensed under the [MIT License](../LICENSE).
