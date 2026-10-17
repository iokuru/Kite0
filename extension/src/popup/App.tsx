import { useEffect, useState } from 'preact/hooks';
import browser from 'webextension-polyfill';
import { analyzeCode } from '../shared/analyzer';
import type { AnalysisResult } from '../shared/types';

interface PageState {
  loading: boolean;
  supported: boolean;
  platformName?: string;
  problemTitle?: string;
  contestMode?: boolean;
  editorAvailable?: boolean;
  source?: string;
  language?: string;
  error?: string;
}

const FONT_FAMILY = "'Mona Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif";
const MONO_FONT = "'SF Mono', 'JetBrains Mono', 'Fira Code', Menlo, monospace";

// Colors matched directly from reference mockup
const THEME = {
  cardBg: '#353c42',          // Visible lighter slate-grey base
  tileWellBg: '#23292e',      // Sunken tile well inside metric cards
  buttonBg: '#444d54',        // Tactile button grey
  buttonHover: '#4e5860',     // Button hover state
  buttonText: '#d8e1e7',      // Button label text
  activeYellow: '#fdb267',    // Mockup warm apricot-yellow for Time tile
  activeGreen: '#6bd5a6',     // Mockup pastel mint-green for toggle & logo
  textPrimary: '#f0f4f7',     // Off-white text
  textMuted: '#9aa8b2',       // Secondary labels
  unknownMuted: '#9aa8b2',    // Unknown status text
  borderSubtle: 'rgba(255, 255, 255, 0.08)',
};

// Flying Green Kite Logo matching reference illustration
function Kite0GreenLogo({ size = 26 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" fill="none" style={{ flexShrink: 0 }}>
      {/* Left String */}
      <path d="M 37 49 C 35 62, 25 76, 8 92" stroke="#94a3b8" strokeWidth="2.5" strokeLinecap="round" />

      {/* Right Ribbon Tail */}
      <path d="M 66 58 C 69 67, 72 73, 69 79 C 65 84, 70 89, 80 90 C 88 90, 92 91, 94 93" stroke="#0f172a" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" />
      <path d="M 66 58 C 69 67, 72 73, 69 79 C 65 84, 70 89, 80 90 C 88 90, 92 91, 94 93" stroke="#10b981" strokeWidth="4.2" strokeLinecap="round" strokeLinejoin="round" />

      {/* Kite Facets */}
      <path d="M 42 7 Q 57 14 71 18 L 48 28 Z" fill="#6ee7b7" stroke="#0f172a" strokeWidth="1.5" strokeLinejoin="round" />
      <path d="M 71 18 Q 69 38 65 57 L 48 28 Z" fill="#10b981" stroke="#0f172a" strokeWidth="1.5" strokeLinejoin="round" />
      <path d="M 65 57 Q 47 51 30 42 L 48 28 Z" fill="#059669" stroke="#0f172a" strokeWidth="1.5" strokeLinejoin="round" />
      <path d="M 30 42 Q 35 23 42 7 L 48 28 Z" fill="#34d399" stroke="#0f172a" strokeWidth="1.5" strokeLinejoin="round" />

      {/* Inner Bridle */}
      <line x1="38" y1="36" x2="65" y2="57" stroke="#0f172a" strokeWidth="1.5" strokeLinecap="round" />

      {/* Cross Spars */}
      <line x1="42" y1="7" x2="65" y2="57" stroke="#0f172a" strokeWidth="3.2" strokeLinecap="round" />
      <line x1="30" y1="42" x2="71" y2="18" stroke="#0f172a" strokeWidth="3.2" strokeLinecap="round" />

      {/* Outer Perimeter Frame */}
      <path d="M 42 6 Q 57 14 72 17 Q 69 38 66 58 Q 47 51 29 43 Q 35 23 42 6 Z" stroke="#0f172a" strokeWidth="3.6" strokeLinejoin="round" fill="none" />

      {/* Center Pin Knot */}
      <circle cx="48" cy="28" r="2.2" fill="#ffffff" stroke="#0f172a" strokeWidth="1" />
    </svg>
  );
}

export function App() {
  const [activeToggle, setActiveToggle] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'settings' | 'help'>('overview');
  
  const [pageState, setPageState] = useState<PageState>({
    loading: true,
    supported: false,
  });

  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [isScanning, setIsScanning] = useState(false);

  // User controls for settings screen
  const [settings, setSettings] = useState({
    pauseOnContest: true,
    useCache: true,
    auxiliarySpaceOnly: true,
    autoKeystroke: true,
  });

  async function analyzeTab() {
    setIsScanning(true);
    setPageState(prev => ({ ...prev, loading: true, error: undefined }));

    try {
      const tabs = await browser.tabs.query({ active: true, currentWindow: true });
      const activeTabObj = tabs[0];
      if (!activeTabObj || !activeTabObj.id) {
        setPageState({
          loading: false,
          supported: false,
          error: 'No active editor tab found.'
        });
        setIsScanning(false);
        return;
      }

      let response: any = null;
      try {
        response = await browser.tabs.sendMessage(activeTabObj.id, { type: 'EXTRACT_SOURCE' });
      } catch {
        // Fallback injection
      }

      if (!response && (browser as any).scripting?.executeScript) {
        try {
          await (browser as any).scripting.executeScript({
            target: { tabId: activeTabObj.id },
            files: ['content.js']
          });
          response = await browser.tabs.sendMessage(activeTabObj.id, { type: 'EXTRACT_SOURCE' });
        } catch {
          // Injection failed
        }
      }

      if (!response || !response.supported) {
        setPageState({
          loading: false,
          supported: false,
          error: 'Open LeetCode, Codeforces, HackerRank, AtCoder, CSES, or CodeChef.',
        });
        setIsScanning(false);
        return;
      }

      if (response.contestMode) {
        setPageState({
          loading: false,
          supported: true,
          platformName: response.platformName,
          contestMode: true,
        });
        setIsScanning(false);
        return;
      }

      if (!response.editorAvailable || !response.source) {
        setPageState({
          loading: false,
          supported: true,
          platformName: response.platformName,
          editorAvailable: false,
          error: 'No solution code found in active editor.',
        });
        setIsScanning(false);
        return;
      }

      setPageState({
        loading: false,
        supported: true,
        platformName: response.platformName,
        problemTitle: activeTabObj.title ? activeTabObj.title.split('-')[0].trim() : 'Solution',
        editorAvailable: true,
        source: response.source,
        language: response.language || 'cpp',
      });

      let analysis: AnalysisResult;
      try {
        analysis = await analyzeCode(response.source, response.language || 'cpp');
      } catch {
        analysis = await browser.runtime.sendMessage({
          type: 'ANALYZE_REQUEST',
          payload: {
            source: response.source,
            language: response.language || 'cpp',
          },
        });
      }

      setResult(analysis);
    } catch (err: any) {
      setPageState({
        loading: false,
        supported: false,
        error: String(err?.message || 'Failed to scan editor.'),
      });
    } finally {
      setIsScanning(false);
    }
  }

  useEffect(() => {
    analyzeTab();
  }, []);

  function handleToggleClick() {
    const next = !activeToggle;
    setActiveToggle(next);
    if (next) {
      analyzeTab();
    }
  }

  const activeTc = result?.tc || '--';
  const activeSc = result?.sc || '--';
  const activeAlgo = result?.algorithms && result.algorithms.length > 0
    ? result.algorithms.join(', ')
    : 'Unknown';

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      width: '320px',
      background: THEME.cardBg,
      color: THEME.textPrimary,
      fontFamily: FONT_FAMILY,
      userSelect: 'none',
      boxSizing: 'border-box',
      padding: '14px 16px',
      gap: '11px'
    }}>
      {/* Top Header: Mint-Green Logo + Title + Mockup Green Pill Toggle */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Kite0GreenLogo size={22} />
          <span style={{
            fontSize: '17px',
            fontWeight: 700,
            letterSpacing: '-0.3px',
            color: THEME.textPrimary
          }}>
            Kite0
          </span>
        </div>

        {/* Toggle Switch */}
        <div
          onClick={handleToggleClick}
          title={activeToggle ? 'Active (Auto-Scan on)' : 'Paused'}
          style={{
            width: '42px',
            height: '22px',
            borderRadius: '11px',
            background: activeToggle ? THEME.activeGreen : '#262d33',
            position: 'relative',
            cursor: 'pointer',
            transition: 'background 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
            flexShrink: 0
          }}
        >
          <div style={{
            width: '16px',
            height: '16px',
            borderRadius: '50%',
            background: '#ffffff',
            position: 'absolute',
            top: '3px',
            left: activeToggle ? '23px' : '3px',
            transition: 'left 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
            boxShadow: '0 1px 3px rgba(0, 0, 0, 0.35)'
          }} />
        </div>
      </div>

      {/* SCREEN 1: OVERVIEW DASHBOARD */}
      {activeTab === 'overview' && (
        <>
          {/* Hero Metric Counter Tiles (Hours & Minutes layout from Reloader mockup) */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: '10px'
          }}>
            {/* TIME BOX: Active Apricot-Yellow Glowing Border (#fdb267) & Yellow Text */}
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center'
            }}>
              <div style={{
                width: '100%',
                background: THEME.tileWellBg,
                border: `2px solid ${THEME.activeYellow}`,
                borderRadius: '14px',
                padding: '14px 8px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: '0 0 14px rgba(253, 178, 103, 0.16)',
                boxSizing: 'border-box'
              }}>
                <span style={{
                  fontFamily: MONO_FONT,
                  fontSize: '22px',
                  fontWeight: 800,
                  color: THEME.activeYellow,
                  letterSpacing: '-0.5px',
                  lineHeight: 1
                }}>
                  {activeTc}
                </span>
              </div>
              <span style={{
                fontSize: '11px',
                fontWeight: 700,
                color: THEME.activeYellow,
                letterSpacing: '0.6px',
                textTransform: 'uppercase',
                marginTop: '6px'
              }}>
                Time
              </span>
            </div>

            {/* SPACE BOX: Inactive Dark Tile Well & Inactive Sublabel */}
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center'
            }}>
              <div style={{
                width: '100%',
                background: THEME.tileWellBg,
                border: `1px solid ${THEME.borderSubtle}`,
                borderRadius: '14px',
                padding: '14px 8px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxSizing: 'border-box'
              }}>
                <span style={{
                  fontFamily: MONO_FONT,
                  fontSize: '22px',
                  fontWeight: 800,
                  color: THEME.textPrimary,
                  letterSpacing: '-0.5px',
                  lineHeight: 1
                }}>
                  {activeSc}
                </span>
              </div>
              <span style={{
                fontSize: '11px',
                fontWeight: 700,
                color: THEME.textMuted,
                letterSpacing: '0.6px',
                textTransform: 'uppercase',
                marginTop: '6px'
              }}>
                Space
              </span>
            </div>
          </div>

          {/* ALGORITHM CARD: Presents detected algo or "Unknown" */}
          <div style={{
            background: THEME.tileWellBg,
            border: `1px solid ${THEME.borderSubtle}`,
            borderRadius: '11px',
            padding: '10px 12px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between'
          }}>
            <span style={{
              fontSize: '11px',
              fontWeight: 700,
              color: THEME.textMuted,
              textTransform: 'uppercase',
              letterSpacing: '0.5px'
            }}>
              Algorithm
            </span>
            <span style={{
              fontSize: '12px',
              fontWeight: 700,
              color: activeAlgo !== 'Unknown' ? THEME.activeGreen : THEME.unknownMuted,
              letterSpacing: '-0.1px'
            }}>
              {activeAlgo}
            </span>
          </div>

          {/* TARGET CARD: Clean text WITHOUT any circle dot */}
          <div style={{
            background: THEME.tileWellBg,
            border: `1px solid ${THEME.borderSubtle}`,
            borderRadius: '11px',
            padding: '10px 12px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            overflow: 'hidden'
          }}>
            <div style={{
              fontSize: '11.5px',
              fontWeight: 600,
              color: THEME.textPrimary,
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap'
            }}>
              {pageState.platformName
                ? `${pageState.platformName} · ${pageState.problemTitle || 'Connected'}`
                : (pageState.error || 'Open LeetCode, Codeforces, HackerRank...')}
            </div>
          </div>

          {/* SCAN ACTION BUTTON: Prominent button with Magnifying Glass */}
          <button
            onClick={() => analyzeTab()}
            title="Scan editor complexity"
            style={{
              width: '100%',
              background: THEME.buttonBg,
              color: THEME.textPrimary,
              border: `1px solid ${THEME.borderSubtle}`,
              borderRadius: '11px',
              padding: '10px 14px',
              fontSize: '12.5px',
              fontWeight: 700,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '7px',
              transition: 'background 0.15s ease'
            }}
            onMouseEnter={(e) => { (e.currentTarget as HTMLElement).style.background = THEME.buttonHover; }}
            onMouseLeave={(e) => { (e.currentTarget as HTMLElement).style.background = THEME.buttonBg; }}
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8" />
              <line x1="21" y1="21" x2="16.65" y2="16.65" />
            </svg>
            <span>{isScanning ? 'Scanning...' : 'Scan'}</span>
          </button>
        </>
      )}

      {/* SCREEN 2: USER CONTROLS (Mockup's Middle Screen, without orphan code box) */}
      {activeTab === 'settings' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{
            fontSize: '11px',
            fontWeight: 700,
            color: THEME.textMuted,
            textTransform: 'uppercase',
            letterSpacing: '0.4px'
          }}>
            Analysis Controls
          </div>

          {/* Checklist with Green Checkmarks */}
          <div style={{
            background: THEME.tileWellBg,
            border: `1px solid ${THEME.borderSubtle}`,
            borderRadius: '11px',
            padding: '12px',
            display: 'flex',
            flexDirection: 'column',
            gap: '10px'
          }}>
            {[
              { key: 'pauseOnContest', label: 'Do not analyze during live contest' },
              { key: 'useCache', label: 'Use cache while analyzing' },
              { key: 'auxiliarySpaceOnly', label: 'Auxiliary space mode (ignore inputs)' },
              { key: 'autoKeystroke', label: 'Run analysis on editor keystroke' }
            ].map(item => {
              const isChecked = (settings as any)[item.key];
              return (
                <div
                  key={item.key}
                  onClick={() => setSettings(prev => ({ ...prev, [item.key]: !isChecked }))}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '9px',
                    cursor: 'pointer'
                  }}
                >
                  <div style={{
                    width: '16px',
                    height: '16px',
                    borderRadius: '4px',
                    background: isChecked ? THEME.activeGreen : '#293036',
                    border: isChecked ? `1px solid ${THEME.activeGreen}` : '1px solid rgba(255, 255, 255, 0.1)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0
                  }}>
                    {isChecked && (
                      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#181e22" strokeWidth="3.5">
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    )}
                  </div>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: THEME.textPrimary }}>
                    {item.label}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* SCREEN 3: HELP & PRIVACY */}
      {activeTab === 'help' && (
        <div style={{
          background: THEME.tileWellBg,
          border: `1px solid ${THEME.borderSubtle}`,
          borderRadius: '11px',
          padding: '12px',
          display: 'flex',
          flexDirection: 'column',
          gap: '6px',
          fontSize: '11.5px',
          color: THEME.textPrimary
        }}>
          <div style={{ fontWeight: 700, fontSize: '12px', color: THEME.activeYellow }}>
            About Kite0 Engine
          </div>
          <div style={{ color: THEME.buttonText, lineHeight: '1.4' }}>
            100% offline WebAssembly static analyzer for C++ and Java complexity verification. Zero code leaves your browser.
          </div>
          <div style={{ color: THEME.activeGreen, fontWeight: 600, marginTop: '2px' }}>
            ✓ LeetCode, Codeforces, HackerRank, CSES
          </div>
        </div>
      )}

      {/* BOTTOM DOCK (Directly matching media_1791900008055_706d2af1.png from mockup) */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        paddingTop: '4px'
      }}>
        {/* Left: Active/Inactive Screen Navigation Pills */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          {/* Sliders Icon (Screen 1: Overview) */}
          <button
            onClick={() => setActiveTab('overview')}
            title="Analysis Overview"
            style={{
              background: activeTab === 'overview' ? THEME.tileWellBg : 'transparent',
              border: 'none',
              borderRadius: '7px',
              padding: '6px 10px',
              color: activeTab === 'overview' ? THEME.textPrimary : THEME.textMuted,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'all 0.15s ease'
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round">
              <line x1="4" y1="21" x2="4" y2="14" />
              <line x1="4" y1="10" x2="4" y2="3" />
              <line x1="12" y1="21" x2="12" y2="12" />
              <line x1="12" y1="8" x2="12" y2="3" />
              <line x1="20" y1="21" x2="20" y2="16" />
              <line x1="20" y1="12" x2="20" y2="3" />
              <line x1="1" y1="14" x2="7" y2="14" />
              <line x1="9" y1="8" x2="15" y2="8" />
              <line x1="17" y1="16" x2="23" y2="16" />
            </svg>
          </button>

          {/* Activity/Pulse Icon (Screen 2: Controls & Inspector) */}
          <button
            onClick={() => setActiveTab('settings')}
            title="Analysis Controls"
            style={{
              background: activeTab === 'settings' ? THEME.tileWellBg : 'transparent',
              border: 'none',
              borderRadius: '7px',
              padding: '6px 10px',
              color: activeTab === 'settings' ? THEME.textPrimary : THEME.textMuted,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'all 0.15s ease'
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
            </svg>
          </button>
        </div>

        {/* Right: Question Mark Icon (Screen 3: Help) */}
        <button
          onClick={() => setActiveTab(activeTab === 'help' ? 'overview' : 'help')}
          title="About & Privacy"
          style={{
            background: activeTab === 'help' ? THEME.tileWellBg : 'transparent',
            border: 'none',
            borderRadius: '7px',
            padding: '5px 10px',
            color: activeTab === 'help' ? THEME.textPrimary : THEME.textMuted,
            cursor: 'pointer',
            fontSize: '15px',
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            transition: 'color 0.15s'
          }}
        >
          ?
        </button>
      </div>
    </div>
  );
}
