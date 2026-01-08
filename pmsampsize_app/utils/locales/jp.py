
JP = {
    "title": "予後研究サンプルサイズツール (Prognostic Research Sample Size Tool)",
    "sidebar_title": "設定 (Configuration)",
    "language": "言語 / Language",
    "mode": "手法の選択 (Method Selection)",
    "mode_riley": "手法 C5: Riley 等 (解析的)",
    "mode_bayes": "手法 C6: ベイズ主導 (シミュレーション)",
    "mode_single": "単一シナリオ (Single Scenario)",
    "mode_batch": "感度分析 (Sensitivity Analysis)",
    "method1_tab": "手法 C5 (Riley)",
    "method2_tab": "手法 C6 (Bayesian)",
    "nav_title": "ナビゲーション (Navigation)",
    "nav_readme": "詳細ドキュメント (README)",
    "nav_intro": "概要と数式 (Introduction & Formulas)",
    "nav_calc": "サンプルサイズ計算機 (Calculator)",
    "intro_heading": "ようこそ (Welcome)",
    "intro_text": "このツールは、二値アウトカムの臨床予測モデル開発に必要な最小サンプルサイズを計算するのに役立ちます。",
    "formula_heading": "数学的枠組み (手法 C5)",
    "formula_intro": "手法 C5 は Riley 等による解析解を使用し、手法 C6 はベイズ MCMC シミュレーションを使用します。",
    "sens_guide_title": "💡 感度分析の使い方 (バッチモード)",
    "sens_guide_text": """
    - **範囲**: `min-max` を入力 (例: `0.05-0.10`)。ステップは自動生成されます。
    - **特定の値**: カンマ区切りのリストを入力 (例: `0.05, 0.10, 0.15`)。
    """,
    "detail_view": "シナリオの詳細計算を表示",
    "footer_refs": "参考文献: Riley et al. (2018, 2020), BayesAssurance.",
    "calc_btn": "計算 (Calculate)",
    "results": "結果 (Results)",
    "sanity": "妥当性チェック (Sanity Check - EPV Rules)",
    "download_csv": "CSV をダウンロード",
    "download_report": "完全なレポートをダウンロード",
    "error_p": "有病率は 0 と 1 の間でなければなりません。",
    "error_auc": "AUC は 0.5 と 1 の間でなければなりません。",
    "error_parse": "入力を解析できませんでした。",
    
    # Riley specific
    "riley_inputs": "入力パラメータ (Riley)",
    "prevalence": "アウトカム有病率 / イベント発生率 (Outcome Prevalence / Event Rate)",
    "prevalence_help": "イベントが発生する参加者の割合 (0 < p < 1)。",
    "parameters": "予測パラメータ数 (Number of Predictor Parameters/df)",
    "parameters_help": "総自由度 (切片を除く)。",
    "shrinkage": "目標グローバル収縮率 (Target Global Shrinkage, S)",
    "shrinkage_help": "希望する収縮係数 (デフォルト 0.9)。",
    "perf_measure": "予想されるパフォーマンス (Anticipated Performance)",
    "perf_auc": "AUC (C統計量)",
    "perf_r2": "Cox-Snell R二乗",
    "perf_cons": "保守的 (最大 R2 の 15%)",
    
    # Bayesian specific 
    "perf_cons_help": "保守的 (最大 R2 の 15%)",
    "perf_auc_help": "予想される AUC (C統計量)",
    "perf_r2_help": "予想される Cox-Snell R二乗",
    
    # Bayesian specific
    "bayes_inputs": "シミュレーション設定 (ベイズ保証)",
    "dgm_settings": "データ生成メカニズム (Data Generating Mechanism)",
    "sim_settings": "シミュレーションと MCMC (Simulation & MCMC)",
    "eval_settings": "評価基準 (Evaluation Criteria)",
    "n_candidates": "候補サンプルサイズ (カンマ区切り)",
    "n_candidates_help": "テストする N のリスト。例: 500, 1000, 1500。",
    "correlation": "予測因子の相関 (rho)",
    "n_sims": "N ごとのシミュレーション回数",
    "assurance_threshold": "保証しきい値 (目標確率, Assurance Threshold)",
    "run_simulation": "ベイズシミュレーションを実行",
    "simulation_running": "シミュレーションを実行中... 時間がかかる場合があります。",
    "assurance_result": "保証分析 (Assurance Analysis)",
    
    # Method 6 (Dev Sim)
    "mode_dev_sim": "手法 6: 開発シミュレーション (頻度論)",
    "method6_tab": "手法 6 (Simulation)",
    "dev_sim_intro": "シミュレーションに基づくモデル開発サンプルサイズ計算 (頻度論的手法, `samplesizedev` に類似)。",
    "dev_mode_simple": "モード A: シンプル (AUC 駆動)",
    "dev_mode_custom": "モード B: カスタム DGM",
    "target_auc": "目標平均 AUC (C統計量)",
    "target_auc_help": "アルゴリズムはこの AUC を達成するための Beta 係数を検索します。",
    "criteria_settings": "パフォーマンス基準 (合格/不合格)",
    "crit_slope_mean": "平均キャリブレーション勾配 (Calibration Slope) >= 0.9",
    "crit_slope_ci": "Pr(0.9 <= Slope <= 1.1) >= 80%",
    "crit_auc": "平均 AUC >= 目標値",
    "audit_trail": "RNG 監査証跡 (JSON)",
    "future_methods": "今後のバージョンで公開予定...",
    
    # Quick Methods
    "method_quick_tab": "A. クイック / 基本 (Quick / Basic)",
    "quick_mode_epv": "A1: EPV / EPP ルール (ヒューリスティック)",
    "quick_mode_risk": "A2: ベースラインリスク精度 (CI 幅)",
    "target_epv": "目標パラメータあたりイベント数 (EPP)",
    "target_epv_help": "一般的なヒューリスティック値は 10, 15, 20 です。EPV よりも EPP が推奨されます。",
    "epv_warning_title": "⚠️ 重要な警告",
    "epv_warning_text": "EPV/EPP は単なる大まかなヒューリスティックルールです。これは、良好なキャリブレーションや識別能を保証するものではなく、楽観的バイアスを防ぐものでもありません。変数選択や非線形項に対して敏感です。",
    "ci_level": "信頼水準 (Confidence Level)",
    "ci_half_width": "目標半値幅 (許容誤差, Margin of Error)",
    "ci_method": "CI 手法",
    "ci_method_wilson": "Wilson Score (推奨)",
    "ci_method_wald": "Wald (単純)",
    "ci_method_cp": "Clopper-Pearson (保守的)",
    "risk_help": "特定の精度でイベント発生率 p を推定するために必要な N を計算します。予測モデルのパフォーマンスは保証しません。",
    
    # Power Methods (B)
    "title_b3": "B3: Logistic 検出力 (Hsieh)",
    "title_b4": "B4: Cox 検出力 (Schoenfeld)",
    "interpretation": "解釈 (Interpretation)",
    
    # UI Basics
    "d8_assumptions": "**仮定**: Hanley & McNeil (1982) の分散近似を使用。AUC の対称正規性を仮定。N を見つけるための数値最適化。",
    "d8_mode_n_to_width": "N から CI 幅を計算",
    "d8_mode_width_to_n": "CI 幅から必要な N を計算",
    "d8_opt_settings": "高度なオプティマイザ設定",
    "d8_practical_rounding": "実際の丸めを表示",
    "d8_n_input": "サンプルサイズ (N)",
    "d8_width_input": "CI 幅 (合計)",
    "d8_opt_bound": "検索上限",
    "d8_opt_tol": "許容誤差",
    
    # Validations (D)
    "title_d8": "D8: AUC 精度 (Hanley-McNeil)",
    "d8_desc": "AUC を所望の精度 (CI 幅) で推定するためのサンプルサイズを計算します。",
    "auc_expected": "予想される AUC (C統計量)",
    "formulas_header": "📚 数式と技術詳細 (Formulas & Technical Details)",
    "d8_assumptions": "**仮定**: Hanley & McNeil (1982) の分散近似を使用。AUC の対称正規性を仮定。N を見つけるための数値最適化。",
    "d8_mode_n_to_width": "N から CI 幅を計算",
    "d8_mode_width_to_n": "CI 幅から N を計算",
    "d8_opt_settings": "高度なオプティマイザ設定",
    "d8_practical_rounding": "実際の丸めを表示",
    "d8_n_input": "サンプルサイズ (N)",
    "d8_width_input": "CI 幅 (合計)",
    "d8_opt_bound": "検索上限",
    "d8_opt_tol": "許容誤差",
    
    # D9
    "title_d9": "D9: 外部検証 (Tailored)",
    "common_inputs": "共通パラメータ",
    
    # UI Basics
    "search_placeholder": "手法を検索...",
    "settings": "設定 (Settings)",
    
    # Footer
    "footer_copyright": "© 2026 予後研究サンプルサイズツール。学術/研究利用のみ。",
    "footer_author": "作成者と管理者: Minh Nguyen (minhnt@ump.edu.vn) - Dept. of Epidemiology, Faculty of Public Health, UMP Ho Chi Minh City",
    "footer_disclaimer": "免責事項: 臨床的な保証はありません。ユーザーは検証と解釈に責任を負います。",

    "intro_complete_md": """
### ようこそ (Welcome)

このアプリケーションは、臨床医や研究者が以下を含む予後研究の最小サンプルサイズを計画するのに役立ちます：
* 予後因子研究 (関連性の検出力)、
* 臨床予測モデルの開発 (リスク予測)、および
* モデル検証 / 更新 (外部検証、再キャリブレーション)。

これは二値アウトカム (例：イベント vs イベントなし) 用に設計されており、一部のモジュールは生存時間アウトカム (Cox PH) にも適応します。

ソースコード (ダウンロード): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
または [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)    

### はじめに (新規ユーザー)

#### 1. 研究の目的を明確にする
* 単一の予後因子 (関連性) をテストしていますか？
* 予測モデルを構築していますか？
* 既存のモデルを新しい集団で検証していますか？

#### 2. イベント発生率 $p$ (または生存分析のイベント割合) を推定する
* 地元の病院のデータが望ましいです (ベスト)。
* 不確かな場合は、範囲を入力して感度分析を実行してください。

#### 3. モデルの複雑さ (パラメータ / 自由度) を正しく数える
単なる「変数の数」ではなく、パラメータ (自由度) を使用してください。
* 二値予測子: 1 df
* $L$ レベルのカテゴリ変数: $L-1$ df
* スプライン ($K$ ノットの RCS): $K-1$ df
* 交互作用: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. 下記のカタログから手法を選択する
* **"クイックツール" (Quick tools)** は大まかな計画にのみ使用してください。
* 予測モデルの開発には **Riley / シミュレーション / 保証 (Assurance)** 手法を使用してください。

---

### このアプリを使用する場面 (および使用しない場面)

**以下の場合に使用してください:**
* 予後/予測に関する後ろ向きまたは前向きコホート研究を計画する場合
* リスク予測モデルの開発または検証
* 有病率または AUC の精度 (CI 幅) に基づくサンプルサイズの推定
* キャリブレーションと識別能の目標を持つ外部検証の設計

**以下の場合、このアプリを主要ツールとして使用しないでください:**
* ランダム化比較試験の設計 (RCT 固有の検出力/サンプルサイズ手法を使用)
* 予測モデリングを伴わない感度/特異度の診断精度研究の計画
* 単一の「正しい」数値を期待する場合：サンプルサイズ計画には仮定が必要であり、感度分析を含めるべきです

---

### 利用可能な手法 (概要)

#### A. クイック / 基本 (高速、近似)

**A1 — 経験則 (EPV/EPP) (ヒューリスティック)**
* **適用:** 計画しているモデルサイズに対してイベントが「大まかに十分」かどうかを素早く確認する必要がある場合。
* **不適用:** モデルにスプライン/交互作用/変数選択が含まれる場合、またはイベント発生率が低い場合——EPV/EPP は良好なキャリブレーションや低い楽観的バイアスを保証しません。
* **主な入力:** イベント発生率 $p$, パラメータ数 $P$ (df), 目標 EPP (例: 10/15/20)
* **主な出力:** 必要なイベント数 $E=t \\cdot P$, 必要なサンプルサイズ $N=\\lceil E/p \\rceil$
* **長所:** 非常にシンプル。初期の実現可能性調査に適している
* **短所:** 誤解を招く可能性がある。パフォーマンスに基づいていない

**A2 — ベースラインリスク精度 (有病率の CI 幅)**
* **適用:** 所望の CI 半値幅 (例: ±2%) でイベント発生率 $p$ を推定することを目的とする場合。
* **不適用:** 予測モデルのパフォーマンス保証 (AUC/キャリブレーション勾配) を求める場合。
* **主な入力:** 予想される $p$, CI 手法 (Wilson 推奨), 信頼水準, 目標半値幅 $d$
* **主な出力:** CI 半値幅 $\\le d$ を満たす最小 $N$
* **長所:** 直接的な精度の目標。透明な仮定
* **短所:** 有病率のみに関係し、モデルのパフォーマンスではない

#### B. 予後因子 (検出力) (予測モデルサイズではなく関連性に焦点)

**B3 — Logistic OR 検出力 (Hsieh)**
* **適用:** Logistic 回帰における予後因子の目標オッズ比 (OR) を検出するための検出力を希望する場合。
* **不適用:** 主な目的が仮説検定ではなく、予測モデルの開発 (キャリブレーション/識別能) である場合。
* **主な入力:** ベースラインリスク $p_0$, 目標 OR, Alpha, 検出力, 暴露有病率 (二値) または SD (連続), 共変量との $R^2$ (オプション)
* **主な出力:** OR を検出するために必要な $N$ (および暗黙のイベント数)
* **長所:** 関連性のための古典的な検出力フレームワーク
* **短所:** 予測モデルのパフォーマンスを扱わない。入力の仮定に敏感

**B4 — Cox HR 検出力 (Schoenfeld)**
* **適用:** 生存時間アウトカム; Cox PH 下でハザード比 (HR) を検出するための検出力を希望する場合。
* **不適用:** PH の仮定が満たされない可能性がある場合、またはイベント割合が非常に不確実で合理的に推定できない場合。
* **主な入力:** HR, Alpha, 検出力, 割り当て比率 (二値) または SD (連続), 追跡期間中の予想イベント割合
* **主な出力:** 必要なイベント数; イベント割合を使用して $N$ に変換
* **長所:** 広く受け入れられている。イベントベースの計画は直感的
* **短所:** イベント割合と追跡/打ち切りの仮定に強く依存する

#### C. 予測モデル開発 (リスクモデル構築に推奨)

**C5 — Riley 等 (解析法; pmsampsize に類似)**
* **適用:** 多変量予測モデルの開発; 過学習を制御し、十分な精度を確保したい場合。
* **不適用:** 有病率と予想されるモデルパフォーマンス (AUC または $R^2$) の合理的な仮定を提供できない場合。この場合は感度分析またはシミュレーションを使用してください。
* **主な入力:** イベント発生率 $p$, パラメータ $P$ (df), 目標収縮率 (例: 0.90), 予想されるモデルパフォーマンス (AUC または Cox–Snell $R^2$)
* **主な出力:** 複数の基準 (過学習制御 + 精度) を満たす最小 $N$
* **長所:** 原則に基づいている。パフォーマンスに焦点を当てている。広く引用されている
* **短所:** パフォーマンスの仮定に依存する。慎重な df のカウントが必要

**C6 — 開発シミュレーション (頻度論; samplesizedev/カスタム DGM)**
* **適用:** 特に非線形性/交互作用やカスタムデータ構造がある場合に、「実際に行うことをシミュレーションする」ことを好む場合。
* **不適用:** 合理的なデータ生成メカニズム (DGM) を指定できない場合、または即時の結果が必要な場合 (計算集約的)。
* **主な入力:** 候補 $N$ グリッド, DGM の仮定 (予測因子の分布/相関/効果), パフォーマンス目標 (例: キャリブレーション勾配の範囲, AUC しきい値), シミュレーション繰り返し回数, シード
* **主な出力:** 許容可能な確率/精度で目標を達成する最小 $N$
* **長所:** 柔軟。複雑なモデリングと整合する
* **短所:** 仮定が重い。計算コストが高い

**C7 — ベイズ保証 (MCMC)**
* **適用:** 最終モデルがベイズ MCMC で推定される予定であり、保証 (事後パフォーマンス/精度目標を満たす確率) に基づくサンプルサイズを希望する場合。
* **不適用:** 事前分布を正当化できない、または計算予算が限られている場合。
* **主な入力:** DGM, 事前分布, 候補 $N$, MCMC 設定, 保証しきい値 (例: 80%/90%), パフォーマンス/精度目標
* **主な出力:** 保証しきい値を満たす最小 $N$
* **長所:** ベイズワークフローと整合する。事後基準を直接ターゲットにする
* **短所:** 計算集約的。事前分布の指定が必要

#### D. 検証 / 更新 (既存モデル用)

**D8 — AUC 精度 (Hanley–McNeil / presize)**
* **適用:** 検証の目標が AUC の精度 (CI 幅) である場合。
* **不適用:** キャリブレーション (勾配/CITL) が主な関心事である場合——この方法は AUC のみを対象とします。
* **主な入力:** 予想される AUC, 有病率またはケースコントロール比, 信頼水準, 目標 CI 幅
* **主な出力:** 所望の AUC CI 幅を達成する最小 $N$
* **長所:** シンプル。識別能精度のための迅速な計画
* **短所:** 近似分散。キャリブレーションを無視する

**D9 — 外部検証 (Tailored; pmvalsampsize / sampsizeval)**
* **適用:** 複数のパフォーマンス指標 (キャリブレーション + 識別能) に対して検証規模を決定したい場合で、通常は LP 分布に関する仮定が必要です。
* **不適用:** LP 分布の仮定や予想されるパフォーマンスを正当化できない場合。
* **主な入力:** 有病率, 予想される AUC, キャリブレーション勾配/CITL 目標, CI 幅または SE 目標, LP 分布の仮定
* **主な出力:** 各指標の精度基準を満たす推奨 $N$
* **長所:** カスタマイズされている。キャリブレーションに焦点を当てている
* **短所:** 追加の仮定が必要。より複雑

**D10 — 外部検証 (シミュレーション; LP ベース)**
* **適用:** 目標検証集団における線形予測子 (LP) の分布を指定/推定でき、シミュレーションに基づく精度計画を希望する場合。
* **不適用:** LP 分布が不明で近似できない場合。
* **主な入力:** LP 分布 (正規/Beta/経験的), 誤キャリブレーションパラメータ, 指標の CI 幅目標, 繰り返し回数, シード
* **主な出力:** シミュレーション下で精度目標を達成する最小 $N$
* **長所:** 非常に柔軟。「予想される状況をシミュレーションする」ことに一致する
* **短所:** 仮定が重い。計算コストが高い

**D11 — 更新 / 再キャリブレーション (Intercept/Slope)**
* **適用:** 既存のモデルを再キャリブレーション (切片および/または勾配の更新) し、十分な精度を必要とする場合。
* **不適用:** 完全に新しいモデルを開発している場合 (C5–C7 を使用)。
* **主な入力:** 更新タイプ (切片のみ vs 切片+勾配), イベント発生率, 精度目標
* **主な出力:** 安定した更新を行うのに十分な $N$
* **長所:** 実際の展開に実用的
* **短所:** 地域のケースミックスとモデルの移植性の仮定に依存する

---

#### 免責事項

臨床的な保証はありません。ユーザーは検証と解釈に責任を負います。常に仮定を記録し、感度分析を実行してください。

#### 連絡先

作成者と管理者: Minh Nguyen (minhnt@ump.edu.vn)
""",

    "a2_content_md": """
### What this is (English - Technical Details)

This module estimates the **minimum sample size (n)** needed to estimate the **baseline risk / event rate** (p) (i.e., prevalence of the outcome) with a **desired precision**, expressed as a **confidence interval (CI) half-width** (margin of error).

It is useful for:
* describing the outcome prevalence in a cohort with a specified precision,
* planning feasibility and reporting baseline risk,
* supporting calibration-related planning (e.g., calibration-in-the-large relies on the event rate).

**Important limitation:** This calculation **does not** ensure prediction model performance (AUC, calibration slope, optimism). It only targets precision for estimating (p).

---

### Inputs (what they mean)

1. **Outcome prevalence / event rate** (p)
   Expected proportion of events in the target population (e.g., 0.10).
   * If unknown, consider a plausible range and run a sensitivity analysis.
   * If you want a conservative “worst-case” for prevalence precision, use (p=0.50) (maximizes variance).

2. **Target half-width (margin of error)** (d)
   Desired precision such that the CI is approximately:
   $p \pm d$
   Examples: (d = 0.01, 0.02, 0.03) (i.e., ±1%, ±2%, ±3%).

3. **Confidence level** (1-$\\alpha$)
   Typical values: 0.95 or 0.99.

4. **CI Method**
* **Wilson score (recommended):** better coverage than Wald, especially when (p) is near 0 or 1 or sample size is modest.
* **Wald (normal approximation):** simple closed form but can perform poorly for small (n) or extreme (p).
* **Clopper–Pearson (exact):** conservative (often yields wider CIs; thus larger (n)).

---

### Core calculation

Let $X \sim \\text{Binomial}(n,p)$, $\hat p = X/n$. The goal is to find the smallest (n) such that the chosen CI method yields:
$$
\\frac{\\text{Upper}(n) - \\text{Lower}(n)}{2} \le d
$$

#### A) Wald (closed-form approximation)
$$ n \\approx \\frac{z^2 p(1-p)}{d^2} $$
**Note:** Fast but not recommended for small n or extreme p.

#### B) Wilson score interval (recommended)
Uses the Wilson score interval formula to find n. Since the interval depends on the observed count x, we iterate to find the smallest n where the half-width constraint is met for expected outcomes.

#### C) Clopper–Pearson “exact” interval
Uses Beta quantiles to form conservative intervals. Typically yields larger sample sizes.

---

### Practical defaults

* **Confidence level:** 95% is standard.
* **Half-width (d):** ±0.01 to ±0.03 (1%–3%) are common targets.
* **Method:** Wilson is a strong default.

### Key references
1. **Wilson EB.** Probable inference, the law of succession, and statistical inference. *JASA.* 1927.
2. **Newcombe RG.** Two-sided confidence intervals for the single proportion. *Stat Med.* 1998.
""",

    "b3_content_md": """
### Purpose (English - Technical Details)

This module estimates the **minimum sample size** needed to detect an association between a predictor (X) and a **binary outcome** (Y) using **logistic regression**, targeting a specified **odds ratio (OR)**, **two-sided ($\\alpha$)**, and **power**.

This is a **prognostic factor / association-focused** power calculation (testing a regression coefficient), **not** a prediction-model performance method. It does **not** guarantee good calibration or discrimination of a multivariable prediction model.

---

### When to use

Use B3 when:

* You want power to detect a **clinically meaningful OR** for a **single predictor** (binary or continuous) in logistic regression.
* Your primary goal is **hypothesis testing** (is the predictor associated with the outcome?), not building a risk prediction model.

### When NOT to use

Do not use B3 as your main approach when:

* Your goal is **prediction model development** (use Riley/pmsampsize or simulation/assurance methods).
* You plan **data-driven variable selection**, many interactions/splines, or complex machine-learning tuning (power for a single coefficient is not the right target).
* Data are **clustered** (multicenter/ward-level correlation) or strongly dependent without adjusting the design effect.
* You have a **case–control** design with fixed case/control sampling (baseline risks ($p_0$) may not represent the source population).

---

### Statistical model and parameters

Logistic regression model:
$$
\\text{logit}{P(Y=1\\mid X)}=\\beta_0+\\beta_1 X
$$

* For **binary** ($X\\in\\{0,1\\}$):
  $$
  \\mathrm{OR}=\\exp(\\beta_1)
  $$
* For **continuous** ($X$): OR must be defined for a specific change in ($X$), commonly **1 SD increase**.

Hypothesis test:
$$
H_0:\\beta_1=0 \\quad \\text{vs}\\quad H_1:\\beta_1\\neq 0
$$

---

### Inputs (what each value means)

1. **Alpha (two-sided)** ($\\alpha$)
   Common choices: 0.05 (standard), 0.01 (more stringent).

2. **Power** ($1-\\beta$)
   Common choices: 0.80 (standard), 0.90 (more conservative).

3. **Baseline event rate** ($p_0$)

   * For **binary predictor**: ($p_0 = P(Y=1\\mid X=0)$) (event rate in the reference group).
   * For **continuous predictor**: ($p_0$) is typically interpreted as the event rate at the **mean** of ($X$) (after centering).

4. **Target odds ratio** ($\\mathrm{OR}$)
   The smallest OR that is clinically meaningful and worth detecting.

5. **Predictor type**

* **Binary predictor**: requires **prevalence of (X=1)**, denoted ($q=P(X=1)$).
* **Continuous predictor**: typically requires the OR for a **1 SD increase** (or you must convert using SD).

6. **($R^2$) with other covariates**
   ($R^2$) is the squared multiple correlation from regressing ($X$) on other covariates in a multivariable model.

   * If ($X$) is correlated with other predictors, the effective information about ($\\beta_1$) decreases, so the required sample size increases.

---

# Calculation

## Step 1 — Convert OR and baseline risk to ($p_1$) (binary ($X$))

If ($X$) is binary, compute the event rate in the exposed group ($p_1=P(Y=1\\mid X=1)$) from ($p_0$) and OR:

$$
\\text{odds}_0=\\frac{p_0}{1-p_0},\\quad \\text{odds}_1=\\mathrm{OR}\\cdot \\text{odds}_0,\\quad
p_1=\\frac{\\text{odds}_1}{1+\\text{odds}_1}
$$

Overall event rate:
$$
p=(1-q)p_0+q p_1
$$

## Step 2 — Z-scores

Let:
$$
z_{\\alpha}=z_{1-\\alpha/2}, \\qquad z_{\\beta}=z_{1-\\beta}=z_{\\text{power}}
$$

## A) Binary predictor sample size (Hsieh approach)

With ($q=P(X=1)$), ($p_0=P(Y=1\\mid X=0)$), ($p_1=P(Y=1\\mid X=1)$), and ($p$) as above:

$$
n_0=
\\frac{
\\left[
z_{\\alpha}\\sqrt{\\frac{p(1-p)}{q(1-q)}}
+
z_{\\beta}\\sqrt{\\frac{p_1(1-p_1)}{q}+\\frac{p_0(1-p_0)}{1-q}}
\\right]^2
}
{(p_1-p_0)^2}
$$

### Adjustment for correlation with other covariates

If you plan a multivariable model and the predictor of interest ($X$) correlates with other covariates, inflate the sample size using:

$$
n=\\frac{n_0}{1-R^2}
$$

### Expected number of events

$$
E \\approx n\\cdot p
$$

---

## B) Continuous predictor sample size (Hsieh approach)

Assume a logistic model with a continuous predictor ($X$) and define OR for a **1 SD increase** in ($X$), denoted ($\\mathrm{OR}_{SD}$). Let ($p_0$) be the event rate at the mean of ($X$):

$$
n_0=\\frac{(z_{\\alpha}+z_{\\beta})^2}{p_0(1-p_0) [\\log(\\mathrm{OR}_{SD})]^2}
$$

If the user has an OR per 1-unit increase, ($\\mathrm{OR}_{unit}$), and SD of ($X$) is ($\\sigma_X$), convert:
$$
\\log(\\mathrm{OR}_{SD})=\\log(\\mathrm{OR}_{unit})\\cdot \\sigma_X
$$

Then apply the same multivariable correlation inflation:
$$
n=\\frac{n_0}{1-R^2}
$$

---

## Practical guidance: what values to choose (common conventions)

* **($\\alpha$)**: 0.05 (two-sided) is typical; use smaller ($\\alpha$) if multiple testing is expected.
* **Power**: 0.80 is common; 0.90 is preferred when missing the effect would be costly.
* **OR**: choose the **minimum clinically meaningful** OR (often in the 1.2–2.0 range depending on context).
* **Baseline risk ($p_0$)**: use local hospital/cohort data if available; otherwise use literature estimates and run sensitivity analyses.
* **Binary predictor prevalence ($q$)**: use local prevalence; note ($q$) near 0.5 gives the **largest information** (smaller ($n$)); very small/large ($q$) increases required ($n$).
* **($R^2$)**: if uncertain, run a sensitivity range (e.g., 0, 0.1, 0.25, 0.5). Even moderate correlation can inflate ($n$) substantially via ($1/(1-R^2)$).
* **Continuous predictors**: consider standardizing ($X$) to mean 0, SD 1 so ($\\mathrm{OR}_{SD}$) is easy to interpret.

---

## Key references (2–5)

1. Hsieh FY, Bloch DA, Larsen MD. *A simple method of sample size calculation for linear and logistic regression.* Statistics in Medicine. 1998;17(14):1623–1634.
2. Hsieh FY. *Sample size tables for logistic regression.* Statistics in Medicine. 1989;8(7):795–802.
3. Whittemore AS. *Sample size for logistic regression with small response probability.* Journal of the American Statistical Association. 1981;76:27–32.
""",
    "c5_content_md": """
### What this method is (English - Technical Details)

C5 implements the **Riley et al. analytical minimum sample size criteria** for **developing a multivariable clinical prediction model** with a **binary outcome** (logistic regression). The goal is to ensure the development dataset is large enough to:

1. **Limit overfitting** (via a target global shrinkage / calibration slope),
2. Achieve **adequate precision** for model performance (via a bound on optimism in $R^2$), and
3. Estimate the **overall outcome risk** (intercept/baseline risk) with acceptable precision.

This is a **model development** method (not external validation). It is particularly suitable when you plan a **pre-specified model form** (predictors and coding defined in advance) and want a **principled alternative to EPV rules**.

---

### When to use

Use C5 when:

* You are **developing** a new prediction model for a **binary outcome**.
* You can specify (even approximately) the **event rate** and an anticipated **overall model performance** (Cox–Snell $R^2$ or AUC).
* You want to target **low overfitting** (e.g., shrinkage $S \\ge 0.90$) and reasonable precision.

### When NOT to use (or use with caution)

Do not rely on C5 alone when:

* You will do extensive **data-driven variable selection**, multiple interactions/splines, or heavy ML tuning without adjusting the **effective number of parameters (df)**.
* Your data are strongly **clustered** (multicenter) without accounting for design effects.
* The intended modeling approach is not standard logistic regression (e.g., complex ML) unless you map complexity to an appropriate **effective df** or switch to simulation-based sizing.
* You cannot justify any plausible performance input (AUC/$R^2$); in that case run wide sensitivity analyses and consider simulation-based methods.

---

## Key inputs (what each means)

1. **Outcome prevalence / event rate** (p)
   Expected proportion with (Y=1) in the development dataset.

2. **Number of predictor parameters (df)** (P)
   Total degrees of freedom for all candidate predictors **excluding the intercept**.
   Include: dummy variables, spline bases, interactions (and any other basis expansions).

3. **Anticipated performance** (choose one)

* **Cox–Snell ($R^2_{CS}$)**: preferred if available from related prior studies (ideally optimism-adjusted).
* **AUC (C-statistic)**: if $R^2_{CS}$ is unavailable, the tool can approximate $R^2_{CS}$ from AUC and ($p$) using a published approach.
* **Conservative (15% of max $R^2$)**: a fallback when neither AUC nor $R^2$ is available; use with caution.

4. **Target global shrinkage** (S)
   A target for **overall overfitting control** (often interpreted similarly to an expected calibration slope after internal validation).

* Common default: $S = 0.90$ ($\\approx$ 10% shrinkage of predictor effects).
* More conservative: $S = 0.95$ (requires larger sample size).

---

## Core concepts and formulas

### Cox–Snell ($R^2$) and its maximum

Cox–Snell ($R^2$) for a fitted logistic model can be written as:
$$
R^2_{CS} = 1-\\exp!\\left(\\frac{2}{n}(\\ell_0-\\ell_1)\\right),
$$
where (\\ell_0) is the intercept-only log-likelihood and (\\ell_1) is the model log-likelihood.

For binary outcomes, ($R^2_{CS}$) cannot reach 1. Its maximum depends on the outcome prevalence:
$$
\\ell_0 = n\\Big[p\\ln(p) + (1-p)\\ln(1-p)\\Big],
$$
$$
R^2_{CS,\\max}=1-\\exp!\\left(\\frac{2\\ell_0}{n}\\right)
=1-\\exp!\\Big(2[p\\ln(p) + (1-p)\\ln(1-p)]\\Big).
$$

Nagelkerke ($R^2$) rescales Cox–Snell ($R^2$) to ([0,1]):
$$
R^2_{Nag}=\\frac{R^2_{CS}}{R^2_{CS,\\max}}.
$$

---

## The three Riley criteria (binary outcome)

### Criterion 1 — Control overfitting via target shrinkage (S)

Minimum sample size to target global shrinkage (S):
$$
n_1=\\left\\lceil
\\frac{P}{(S-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S}\\right)}
\\right\\rceil.
$$

### Criterion 2 — Limit optimism in ($R^2$) (default absolute difference 0.05)

This criterion targets a small absolute difference (default (\\delta=0.05)) between apparent and adjusted **Nagelkerke** ($R^2$). The required shrinkage implied by this constraint is:
$$
S_{\\delta}=\\frac{R^2_{CS}}{R^2_{CS}+\\delta,R^2_{CS,\\max}}.
$$
Then:
$$
n_2=\\left\\lceil
\\frac{P}{(S_{\\delta}-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S_{\\delta}}\\right)}
\\right\\rceil.
$$

### Criterion 3 — Precise estimation of the overall outcome risk (intercept)

This targets precision of the **average outcome risk** (p) (baseline risk) within (\\pm d) on the probability scale (default (d=0.05) at 95% CI):
$$
n_3=\\left\\lceil
\\left(\\frac{z_{1-\\alpha/2}}{d}\\right)^2 p(1-p)
\\right\\rceil,
\\quad \\text{default } z_{0.975}=1.96,; d=0.05.
$$

### Final recommendation

$$
n_{\\min}=\\max(n_1,n_2,n_3),\\qquad
E = n_{\\min},p,\\qquad
EPP=\\frac{E}{P}.
$$

---

## Practical guidance (typical choices)

* **Shrinkage (S)**: use **0.90** as a standard target; consider **0.95** if you want stronger overfitting control or if the model is complex.
* **(\\delta=0.05)** for Criterion 2: commonly kept at the default.
* **Intercept precision (d=0.05)**: default corresponds to estimating baseline risk within ±5%. If baseline risk must be estimated more precisely, you would need a smaller (d) (larger (n)).
* **Anticipated ($R^2_{CS}$)**:

  * Prefer **optimism-adjusted** values from related studies (or apparent values from external validation data).
  * If only AUC is available, use the published AUC→($R^2_{CS}$) approximation method.
  * If neither is available, the **15% of ($R^2_{CS,\\max}$)** option is a conservative fallback for exploratory planning—always run sensitivity analyses.

---

## Key references (2–5)

1. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: PART II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
2. Riley RD, Ensor J, Snell KIE, et al. *Calculating the sample size required for developing a clinical prediction model.* BMJ. 2020.
3. Riley RD, Van Calster B, Collins GS. *A note on estimating the Cox–Snell ($R^2$) from a reported C statistic (AUROC) to inform sample size calculations for developing a prediction model with a binary outcome.* Statistics in Medicine. 2021.
4. Harrell FE Jr, Lee KL, Mark DB. *Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors.* Statistics in Medicine. 1996.
""",
    "c6_content_md": """
## C6: Development Simulation (Frequentist; custom DGM) (English - Technical Details)

### What this method is

C6 is a **simulation-based sample size planning** approach for **prediction model development** (binary outcome), inspired by the philosophy of **samplesizedev** and broader simulation-based design principles.

Instead of relying on a single analytical formula, C6 asks:

> “If we repeatedly develop the model using the planned approach on datasets of size (N), how often will the model meet pre-specified performance criteria on new data?”

It therefore targets **expected performance** (and/or probability of acceptable performance) under a **data-generating mechanism (DGM)** that represents your anticipated clinical population.

---

## When to use

Use C6 when:

* You want a planning method aligned with “**simulate what you will do**,” especially when:

  * predictors may be correlated,
  * you include non-linear terms or interactions,
  * event rates are modest or uncertain,
  * you want criteria based on **calibration** and **discrimination**.
* You can specify a reasonable DGM using local data or the literature.
* You are comfortable with simulation and want a more flexible alternative to purely analytical sizing.

## When NOT to use (or use with caution)

Avoid relying on C6 alone when:

* You cannot justify a plausible DGM (predictor distribution, correlations, effect sizes).
* You do not have computational budget (simulation can be expensive).
* You plan highly data-adaptive ML pipelines (feature selection, complex tuning) without explicitly simulating the full pipeline (C6 must reflect the actual pipeline to be valid).
* The target population is heterogeneous across hospitals/centers and you are not simulating clustering/case-mix shifts.

---

# Overview of the algorithm

For each candidate sample size (N), simulate (R) development datasets, fit the planned model, evaluate it on “new data,” and summarize performance.

### Step 1 — Choose a DGM

Define how predictors (X) and outcomes (Y) are generated.

Typical binary-outcome DGM:
$$
Y \mid X \sim \\text{Bernoulli}(\\pi), \\qquad
\\pi = \\text{logit}^{-1}(\\eta),
$$
$$
\\eta = \\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_j),
$$
where:

* (P) is the **number of parameters/df** used in the fitted model,
* (f_j(\\cdot)) represent coding choices (linear term, spline basis, dummy coding, etc.).

To achieve a target event rate (p), choose (\\beta_0) so that:
$$
\\mathbb{E}[\\pi] = p.
$$
In practice, (\\beta_0) is found by numerical root-finding using Monte Carlo draws from (X).

### Step 2 — Generate a development dataset

For replicate (r):

* Simulate (X^{(r)}) of size (N) from the chosen predictor distribution (with specified correlations).
* Simulate (Y^{(r)}) from the Bernoulli model above.

### Step 3 — Fit the development model

Fit the planned logistic regression model:
$$
\\widehat{\\eta} = \\widehat{\\beta}*0 + \\sum*{j=1}^{P}\\widehat{\\beta}_j f_j(X_j).
$$
**Important:** Simulation must match your intended development strategy (e.g., penalization, pre-specified terms). If separation/non-convergence occurs, a ridge-penalized fallback is often used (and should be counted and reported).

### Step 4 — Evaluate on new data

Generate an independent test set (size (N_{\\text{test}}), often large such as 5000–10000) from the same DGM and compute:

**(a) Discrimination (AUC / C-statistic)**
$$
\\mathrm{AUC}=\\Pr(\\widehat{\\eta}_1 > \\widehat{\\eta}_0),
$$
the probability that a randomly selected case has a higher predicted risk than a non-case.

**(b) Calibration slope**
Estimate (b) from a calibration model on the test set:
$$
\\text{logit}(Y) = a + b \\cdot \\text{logit}(\\widehat{p}),
$$
or equivalently using the linear predictor:
$$
\\text{logit}(Y) = a + b \\cdot \\widehat{\\eta}.
$$
Here, (b\\approx 1) indicates good calibration; (b<1) suggests overfitting (predictions too extreme).

### Step 5 — Define pass/fail criteria and compute success rates

Across (R) simulations for each (N), compute:

* Mean calibration slope:
  $$
  \\overline{b} = \\frac{1}{R}\\sum_{r=1}^R b^{(r)}.
  $$
* Probability slope is within an acceptable range:
  $$
  \\widehat{\\Pr}(b \\in [L,U]) = \\frac{1}{R}\\sum_{r=1}^R \\mathbf{1}{b^{(r)}\\in[L,U]}.
  $$
* Mean AUC:
  $$
  \\overline{\\mathrm{AUC}}=\\frac{1}{R}\\sum_{r=1}^R \\mathrm{AUC}^{(r)}.
  $$

A candidate (N) is “acceptable” if all selected criteria are met, e.g.:

* (\\overline{b} \\ge 0.90)
* (\\widehat{\\Pr}(0.9 \\le b \\le 1.1) \\ge 0.80)
* (\\overline{\\mathrm{AUC}} \\ge \\mathrm{AUC}_{\\text{target}})

Choose smallest (N) that passes.

---

# Key inputs (where to find, what to pick)

### 1) Event rate (p)

**Where:** local hospital/cohort data; literature default.
**Planning range:** 5%–15% (fluctuates by disease).
**Recommendation:** run sensitivity on plausible range.

### 2) Parameters (df) (P)

**Where:** intended model specification (including dummies, splines, interactions).
**Typical:** 10–30 df common; more df demands much larger N.

### 3) Target AUC (Mode A)

**Where:** similar published models (ideally external validation); pilot data.
**Typical:** 0.70–0.85 common; >0.90 rare/often optimistic.

### 4) Candidates (N)

Choose a range wide enough to see the pass/fail transition (e.g., 1000–5000).

### 5) Simulations per N (R)

* Demo: (R \\approx 200)
* Final: (R \\ge 1000)
  Monte Carlo Error for success probability:
  $$
  \\mathrm{MCSE}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{R}}.
  $$

### 6) Pass/Fail Criteria

* Mean calibration slope ≥ 0.9
* Pr(0.9 ≤ slope ≤ 1.1) ≥ 80%
* Mean AUC ≥ target

**Convention:** slope 0.90-1.10 and 0.80 probability threshold often used for planning; 0.90 for stricter requirements.

---

# Strengths & Weaknesses

**Strengths**

* Flexible (correlation, non-linearity, interactions).
* Targets performance on new data directly, specifically calibration.
* Easy to do sensitivity analysis.

**Weaknesses**

* Strong dependence on DGM assumptions.
* Computationally expensive.
* Must simulate the exact intended pipeline; mismatches lead to invalid N.

---

## Key references (2–5)

1. Pavlou M, Ambler G, Seaman SR, et al. *How to develop a more accurate risk prediction model when there are few events.* BMJ. 2015.
2. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
3. Pavlou M, et al. *Simulation-based sample size calculation for prediction model performance targets* (validation/development methodology). Statistics in Medicine. 2021.
4. Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating.* 2nd ed. Springer. 2019.
""",
    "c7_content_md": """
## C7: Bayesian Assurance (MCMC) (English - Technical Details)

### What this method is
**Bayesian assurance** is a simulation-based sample size planning method for **Bayesian model building** (here: Bayesian logistic regression for binary outcomes).
Unlike "power" (frequentist), assurance targets the **unconditional probability** that the study will yield a **successful outcome** given the priors.

Simply put:
> "If we repeat the full study many times (generate data + fit Bayes via MCMC), what is the probability the model meets requirements?"

---

### When to use
Use C7 when:
- The final analysis will be **Bayesian** estimated via **MCMC**.
- You want to sample size for a target **success probability** (e.g., ≥80% or ≥90%).
- You can make reasonable assumptions about:
  - event rates,
  - predictor correlations,
  - plausible effect sizes (pilot/literature),
  - priors for regression coefficients.

### When NOT to use (or use with caution)
- You are doing frequentist analysis (use C5 or C6).
- Computational resources are very limited (MCMC inside simulation is slow).
- You have no idea about priors.
"""
}
