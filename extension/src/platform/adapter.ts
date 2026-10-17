import type { SupportedLanguage, ConstraintStatus } from '../shared/types';

export interface PlatformAdapter {
  id: string;
  name: string;
  isMatch(url: string): boolean;
  isEditorAvailable(): boolean;
  getSource(): string | null;
  getLanguage(): SupportedLanguage | null;
  getConstraints?(): string | null;
  evaluateConstraints?(tc: string): ConstraintStatus;
  isLiveContest?(): boolean;
}

export function detectLanguageFromSource(source: string): SupportedLanguage | null {
  if (!source) return null;

  let javaScore = 0;
  let cppScore = 0;

  // C++ strong indicators
  if (source.includes('public:')) cppScore += 5;
  if (source.includes('#include')) cppScore += 5;
  if (source.includes('std::')) cppScore += 5;
  if (source.includes('vector<')) cppScore += 4;
  if (source.includes('cout <<') || source.includes('cin >>')) cppScore += 4;
  if (source.includes('nullptr')) cppScore += 3;
  if (source.includes('unordered_map<') || source.includes('unordered_set<')) cppScore += 3;
  if (source.includes('push_back(') || source.includes('emplace_back(')) cppScore += 3;
  if (source.includes('const auto') || source.includes('auto&')) cppScore += 3;
  if (source.includes('INT_MAX') || source.includes('INT_MIN')) cppScore += 2;
  if (source.includes('pair<') || source.includes('make_pair(')) cppScore += 2;

  // Java strong indicators
  if (source.includes('public class ')) javaScore += 5;
  if (source.includes('System.out')) javaScore += 5;
  if (source.includes('import java.')) javaScore += 5;
  if (/public\s+(int|void|boolean|String|List|int\[\]|long|double|char|TreeNode|ListNode)\s+\w+\s*\(/.test(source)) javaScore += 6;
  if (source.includes('String[]') || source.includes('int[]') || source.includes('int[][]') || source.includes('boolean[]')) javaScore += 4;
  if (source.includes('StringBuilder') || source.includes('StringBuffer')) javaScore += 4;
  if (source.includes('new HashSet') || source.includes('new HashMap') || source.includes('new ArrayList') || source.includes('new int[')) javaScore += 4;
  if (source.includes('Set<') || source.includes('HashSet<') || source.includes('Map<') || source.includes('HashMap<') || source.includes('List<') || source.includes('ArrayList<')) javaScore += 3;
  if (source.includes('.charAt(') || source.includes('.setCharAt(') || source.includes('.length()') || source.includes('.substring(')) javaScore += 3;
  if (source.includes('Math.min(') || source.includes('Math.max(') || source.includes('Math.abs(')) javaScore += 3;
  if (source.includes('Arrays.') || source.includes('Collections.') || source.includes('Integer.')) javaScore += 3;
  if (source.includes('.toString()') || source.includes('.equals(') || source.includes('.equalsIgnoreCase(')) javaScore += 2;
  if (source.includes('.repeat(')) javaScore += 3;

  if (javaScore > cppScore && javaScore >= 3) return 'java';
  if (cppScore > javaScore && cppScore >= 3) return 'cpp';
  return null;
}
