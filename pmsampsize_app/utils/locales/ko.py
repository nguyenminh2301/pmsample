KO = {
        "title": "예후 연구 표본 크기 도구",
        "sidebar_title": "설정",
        "language": "언어 / Language",
        "mode": "방법 선택",
        "mode_riley": "방법 1: Riley 등 (분석적)",
        "mode_bayes": "방법 2: 베이지안 보증 (시뮬레이션)",
        "mode_single": "단일 시나리오",
        "mode_batch": "민감도 분석 (범위)",
        "method1_tab": "방법 1 (Riley)",
        "method2_tab": "방법 2 (Bayesian)",
        "nav_title": "탐색",
        "nav_readme": "상세 문서 (README)",
        "nav_intro": "소개 및 공식",
        "nav_calc": "표본 크기 계산기",
        "intro_heading": "환영합니다",
        "intro_text": "이 도구는 이분형 결과가 있는 임상 예측 모델 개발에 필요한 최소 표본 크기를 계산하는 데 도움을 줍니다.",
        "formula_heading": "수학적 프레임워크 (방법 1)",
        "formula_intro": "방법 1은 Riley 등이 제공한 폐쇄형 솔루션을 사용하고, 방법 2는 베이지안 MCMC 시뮬레이션을 사용합니다.",
        "sens_guide_title": "💡 민감도 분석(배치 모드) 사용법",
        "sens_guide_text": """
        - **범위**: `min-max` 형식으로 입력 (예: `0.05-0.10`). 단계가 자동으로 생성됩니다.
        - **특정 값**: 쉼표로 구분된 목록 입력 (예: `0.05, 0.10, 0.15`).
        """,
        "detail_view": "시나리오별 상세 계산 보기",
        "footer_refs": "참고문헌: Riley et al. (2018, 2020), BayesAssurance.",
        "calc_btn": "계산하기",
        "results": "결과",
        "sanity": "건전성 심사 (EPV 규칙)",
        "download_csv": "CSV 다운로드",
        "download_report": "전체 보고서 다운로드",
        "error_p": "유병률은 0과 1 사이여야 합니다.",
        "error_auc": "AUC는 0.5와 1 사이여야 합니다.",
        "error_parse": "입력을 구문 분석할 수 없습니다.",
        "riley_inputs": "입력 파라미터 (Riley)",
        "prevalence": "결과 유병률 (이벤트 발생률)",
        "prevalence_help": "이벤트가 발생한 참가자의 비율 (0 < p < 1).",
        "parameters": "예측 변수 파라미터 수 (df)",
        "parameters_help": "총 자유도 (절편 제외).",
        "shrinkage": "목표 글로벌 수축 (S)",
        "shrinkage_help": "희망하는 수축 계수 (기본값 0.9).",
        "perf_measure": "예상 성능",
        "perf_auc": "AUC (C-통계량)",
        "perf_r2": "Cox-Snell R-제곱",
        "perf_cons": "보수적 점수 (최대 R2의 15%)",
        "bayes_inputs": "시뮬레이션 설정 (베이지안 보증)",
        "dgm_settings": "데이터 생성 매커니즘",
        "sim_settings": "시뮬레이션 및 MCMC",
        "eval_settings": "평가 기준",
        "n_candidates": "후보 표본 크기 (쉼표로 구분)",
        "n_candidates_help": "테스트할 N 값 목록, 예: 500, 1000, 1500.",
        "correlation": "예측 변수 상관관계 (rho)",
        "n_sims": "N당 시뮬레이션 횟수",
        "assurance_threshold": "보증 임계값 (목표 확률)",
        "run_simulation": "베이지안 시뮬레이션 실행",
        "simulation_running": "시뮬레이션 실행 중... 시간이 걸릴 수 있습니다.",
        "assurance_result": "보증 분석",
        "mode_dev_sim": "방법 6: 개발 시뮬레이션 (빈도주의)",
        "method6_tab": "방법 6 (시뮬레이션)",
        "dev_sim_intro": "모델 개발을 위한 시뮬레이션 기반 표본 크기 (samplesizedev와 유사한 빈도주의 접근법).",
        "dev_mode_simple": "모드 A: 단순 (AUC 기반)",
        "dev_mode_custom": "모드 B: 사용자 정의 DGM",
        "target_auc": "목표 평균 AUC (C-통계량)",
        "target_auc_help": "알고리즘이 이 AUC를 달성하기 위한 베타 계수를 찾습니다.",
        "criteria_settings": "성능 기준 (통과/실패)",
        "crit_slope_mean": "평균 교정 기울기 >= 0.9",
        "crit_slope_ci": "Pr(0.9 <= 기울기 <= 1.1) >= 80%",
        "crit_auc": "평균 AUC >= 목표",
        "audit_trail": "RNG 감사 추적 (JSON)",
        "future_methods": "향후 버전에서 제공 예정...",
        "method_quick_tab": "A. 신속 / 기본",
        "quick_mode_epv": "A1: EPV / EPP 규칙 (경험적)",
        "quick_mode_risk": "A2: 기본 위험 정밀도 (CI 너비)",
        "target_epv": "목표 파라미터당 이벤트 수 (EPP)",
        "target_epv_help": "일반적인 경험적 수치는 10, 15, 20입니다. EPP가 EPV보다 선호됩니다.",
        "epv_warning_title": "⚠️ 중요 경고",
        "epv_warning_text": "EPV/EPP는 대략적인 경험적 규칙입니다. 교정, 판별을 보장하거나 낙관주의를 방지하지 않습니다. 변수 선택 및 비선형 항에 민감합니다.",
        "ci_level": "신뢰 수준",
        "ci_half_width": "목표 반-너비 (오차 한계)",
        "ci_method": "CI 방법",
        "ci_method_wilson": "Wilson Score (권장)",
        "ci_method_wald": "Wald (단순)",
        "ci_method_cp": "Clopper-Pearson (보수적)",
        "risk_help": "특정 정밀도로 이벤트 발생률 p를 추정하기 위한 N을 계산합니다. 예측 모델 성능을 보장하지 않습니다.",
        "title_b3": "B3: 로지스틱 검정력 (Hsieh)",
        "title_b4": "B4: Cox 검정력 (Schoenfeld)",
        "interpretation": "결과 해석",
        "d8_assumptions": "**가정**: Hanley & McNeil (1982) 분산 근사치를 사용합니다. AUC에 대해 대칭적 정규 분포를 가정합니다.",
        "d8_mode_n_to_width": "N으로부터 CI 너비 계산",
        "d8_mode_width_to_n": "CI 너비로부터 필요한 N 계산",
        "d8_opt_settings": "고급 최적화 설정",
        "d8_practical_rounding": "실용적인 정수 반올림 표시",
        "d8_n_input": "표본 크기 (N)",
        "d8_width_input": "CI 너비 (합계)",
        "d8_opt_bound": "탐색 상한선",
        "d8_opt_tol": "허용 오차",
        "title_d8": "D8: AUC 정밀도 (Hanley-McNeil)",
        "d8_desc": "희망하는 정밀도(CI 너비)로 AUC를 추정하기 위한 표본 크기를 계산합니다.",
        "auc_expected": "예상 AUC (C-통계량)",
        "formulas_header": "📚 공식 및 기술적 세부 사항",
        "title_d9": "D9: 외부 검증 (맞춤형)",
        "common_inputs": "공통 파라미터",
        "search_placeholder": "방법 검색...",
        "settings": "설정",
        "footer_copyright": "© 2026 Prognostic Research Sample Size Tool. 학술/연구용 전용.",
        "footer_author": "저자 및 유지관리: Minh Nguyen (minhnt@ump.edu.vn)",
        "footer_disclaimer": "면책 조항: 임상적 보증 없음. 사용자는 결과 검증 및 해석에 대한 책임이 있습니다.",

        "intro_complete_md": """
### 환영합니다

이 앱은 임상의와 연구자가 예후 연구를 위한 최소 표본 크기를 계획하는 데 도움을 줍니다:
* 예후 인자 연구 (연관성 검출을 위한 검정력),
* 임상 예측 모델 개발 (위험 예측), 및
* 모델 검증 / 업데이트 (외부 검증, 재보정).

이 도구는 이분형 결과 (예: 사건 발생 vs 미발생) 및 일부 모듈에서는 생존 시간 결과 (Cox 비례위험)를 위해 설계되었습니다.

소스 코드 (다운로드): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)

### 시작 가이드 (신규 사용자용)

#### 1. 연구 목표 명확화
* 단일 예후 인자 (연관성)를 검정하시나요?
* 예측 모델을 개발하시나요?
* 새로운 집단에서 기존 모델을 검증하시나요?

#### 2. 사건 발생률 $p$ 추정 (또는 생존분석을 위한 사건 분율)
* 가능하면 지역 병원 데이터를 우선 사용하세요 (가장 좋음).
* 불확실한 경우, 범위를 입력하고 민감도 분석을 실행하세요.

#### 3. 모델 복잡도 정확히 계산 (파라미터 / 자유도)
"변수 수"가 아닌 파라미터 (자유도)를 사용하세요.
* 이분형 예측변수: 1 df
* $L$ 수준 범주형: $L-1$ df
* 스플라인 (RCS, $K$ 매듭): $K-1$ df
* 상호작용: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. 아래 카탈로그에서 방법 선택
* **"빠른 도구"**는 대략적인 계획에만 사용하세요.
* 예측 모델 개발 시 **Riley / 시뮬레이션 / 보증** 방법을 사용하세요.

---

### 이 앱을 사용해야 할 때 (그리고 사용하지 말아야 할 때)

**다음 경우에 이 앱을 사용하세요:**
* 예후/예측 분야에서 후향적 또는 전향적 코호트 연구 계획
* 위험 예측 모델 개발 또는 검증
* 유병률 또는 AUC의 정밀도 (신뢰구간 너비)에 따른 표본 크기 추정
* 보정 및 판별력 목표를 가진 외부 검증 설계

**다음 경우에는 주요 도구로 이 앱을 사용하지 마세요:**
* 무작위 대조 시험 (RCT) 설계 (RCT 전용 검정력/표본 크기 방법 사용)
* 예측 모델링 없이 민감도/특이도에 대한 진단 정확도 연구 계획
* 단일 "정확한" 숫자를 기대하는 경우: 표본 크기 계획은 가정에 의존하며 민감도 분석을 포함해야 함

---

### 이용 가능한 방법 (개요)

#### A. 빠른 / 기본 (신속, 근사)

**A1 — 경험적 규칙 (EPV/EPP) (휴리스틱)**
* **사용 시점:** 계획된 모델 크기에 대해 사건 수가 "대략 충분한지" 빠르게 확인할 때.
* **사용하지 말아야 할 경우:** 모델에 스플라인/상호작용/변수 선택이 포함되거나 사건 발생률이 낮은 경우—EPV/EPP는 좋은 보정 또는 낮은 낙관주의를 보장하지 않음.
* **주요 입력:** 사건 발생률 $p$, 파라미터 수 $P$ (df), 목표 EPP (예: 10/15/20)
* **핵심 출력:** 필요 사건 수 $E=t \\cdot P$, 필요 표본 크기 $N=\\lceil E/p \\rceil$
* **장점:** 매우 간단함; 초기 타당성 검토에 적합
* **단점:** 오해의 소지가 있음; 성능 기반이 아님

**A2 — 기준 위험 정밀도 (유병률에 대한 CI 너비)**
* **사용 시점:** 목표가 원하는 CI 반폭 (예: ±2%)으로 사건 발생률 $p$를 추정하는 것일 때.
* **사용하지 말아야 할 경우:** 예측 모델 성능 보장 (AUC/보정 기울기)을 원할 때.
* **주요 입력:** 예상 $p$, CI 방법 (Wilson 권장), 신뢰 수준, 목표 반폭 $d$
* **핵심 출력:** CI 반폭 $\\le d$를 충족하는 최소 $N$
* **장점:** 직접적인 정밀도 목표; 투명한 가정
* **단점:** 유병률에만 해당, 모델 성능은 아님

#### B. 예후 인자 (검정력) (연관성 중심, 예측 모델 크기 결정 아님)

**B3 — 로지스틱 OR 검정력 (Hsieh)**
* **사용 시점:** 로지스틱 회귀에서 예후 인자에 대한 목표 오즈비 (OR) 검출 검정력이 필요할 때.
* **사용하지 말아야 할 경우:** 주요 목표가 예측 모델 개발 (보정/판별력)일 때, 가설 검정이 아닐 때.
* **주요 입력:** 기준 위험 $p_0$, 목표 OR, 알파, 검정력, 노출 유병률 (이분형) 또는 SD (연속형), 선택적 공변량과의 $R^2$
* **핵심 출력:** OR 검출에 필요한 $N$ (및 암시된 사건 수)
* **장점:** 연관성에 대한 고전적 검정력 프레임워크
* **단점:** 예측 모델 성능을 다루지 않음; 입력 가정에 민감

**B4 — Cox HR 검정력 (Schoenfeld)**
* **사용 시점:** 생존 시간 결과; Cox 비례위험 하에서 위험비 (HR) 검출 검정력이 필요할 때.
* **사용하지 말아야 할 경우:** 비례위험 가정이 위반될 가능성이 높거나, 사건 분율이 매우 불확실하여 합리적으로 추정할 수 없을 때.
* **주요 입력:** HR, 알파, 검정력, 배분 비율 (이분형) 또는 SD (연속형), 추적 기간 동안 예상 사건 분율
* **핵심 출력:** 필요 사건 수; 사건 분율을 사용하여 $N$으로 변환
* **장점:** 널리 인정됨; 사건 기반 계획이 직관적
* **단점:** 사건 분율 및 추적/중도절단 가정에 강하게 의존

#### C. 예측 모델 개발 (위험 모델 구축에 권장)

**C5 — Riley 등 (분석적; pmsampsize 유사)**
* **사용 시점:** 다변량 예측 모델 개발; 과적합 제어 및 적절한 정밀도 보장이 필요할 때.
* **사용하지 말아야 할 경우:** 유병률 및 예상 모델 성능 (AUC 또는 $R^2$)에 대한 합리적인 가정을 제공할 수 없을 때; 이 경우 민감도 분석 또는 시뮬레이션 사용.
* **주요 입력:** 사건 발생률 $p$, 파라미터 $P$ (df), 목표 수축 (예: 0.90), 예상 모델 성능 (AUC 또는 Cox–Snell $R^2$)
* **핵심 출력:** 여러 기준 충족 최소 $N$ (과적합 제어 + 정밀도)
* **장점:** 원칙에 기반, 성능 인식, 널리 인용됨
* **단점:** 성능 가정에 의존; 신중한 자유도 계산 필요

**C6 — 개발 시뮬레이션 (빈도주의; samplesizedev/사용자 정의 DGM)**
* **사용 시점:** "수행할 것을 시뮬레이션"하는 것을 선호, 특히 비선형성/상호작용 및 사용자 정의 데이터 구조가 있을 때.
* **사용하지 말아야 할 경우:** 그럴듯한 데이터 생성 메커니즘을 지정할 수 없거나 즉각적인 결과가 필요할 때.
* **주요 입력:** 후보 $N$ 그리드, DGM 가정, 성능 목표 (예: 보정 기울기 범위, AUC 임계값), 시뮬레이션 반복, 시드
* **핵심 출력:** 허용 가능한 확률/정밀도로 목표 달성하는 최소 $N$
* **장점:** 유연함; 복잡한 모델링과 일치
* **단점:** 가정에 크게 의존; 계산 비용

**C7 — 베이지안 보증 (MCMC)**
* **사용 시점:** 최종 모델이 베이지안 MCMC로 추정되고, 보증 기반 표본 크기가 필요할 때.
* **사용하지 말아야 할 경우:** 사전분포를 정당화할 수 없거나 계산 예산이 제한적일 때.
* **주요 입력:** DGM, 사전분포, 후보 $N$, MCMC 설정, 보증 임계값 (예: 80%/90%), 성능/정밀도 목표
* **핵심 출력:** 보증 임계값 충족 최소 $N$
* **장점:** 베이지안 워크플로우와 일관됨; 사후 기준 직접 목표
* **단점:** 계산 집약적; 사전분포 사양 필요

#### D. 검증 / 업데이트 (기존 모델용)

**D8 — AUC 정밀도 (Hanley–McNeil / presize)**
* **사용 시점:** 검증 목표가 AUC의 정밀도 (CI 너비)일 때.
* **사용하지 말아야 할 경우:** 보정 (기울기/CITL)이 주요 관심사일 때—이 방법은 AUC만 목표.
* **주요 입력:** 예상 AUC, 유병률 또는 환자-대조군 비율, 신뢰 수준, 목표 CI 너비
* **핵심 출력:** 원하는 AUC CI 너비 달성을 위한 최소 $N$
* **장점:** 간단함; 판별력 정밀도에 대한 빠른 계획
* **단점:** 근사 분산; 보정 무시

**D9 — 외부 검증 (맞춤형; pmvalsampsize / sampsizeval)**
* **사용 시점:** 여러 성능 측정을 목표로 하는 검증 크기 결정, 종종 LP 분포 가정 필요.
* **사용하지 말아야 할 경우:** LP 분포 가정을 정당화할 수 없을 때.
* **주요 입력:** 유병률, 예상 AUC, 보정 기울기/CITL 목표, CI 너비 또는 SE 목표, LP 분포 가정
* **핵심 출력:** 여러 측정에 대한 정밀도 기준 충족 권장 $N$
* **장점:** 맞춤형; 보정 인식
* **단점:** 추가 가정 필요; 더 복잡함

**D10 — 외부 검증 (시뮬레이션; LP 기반)**
* **사용 시점:** 목표 검증 집단에서 LP 분포를 지정/추정할 수 있고 시뮬레이션 기반 정밀도 계획을 원할 때.
* **사용하지 말아야 할 경우:** LP 분포가 알려지지 않고 근사할 수 없을 때.
* **주요 입력:** LP 분포 (정규/베타/경험적), 오보정 파라미터, 측정값에 대한 CI 너비 목표, 반복, 시드
* **핵심 출력:** 시뮬레이션 하에 정밀도 목표 달성 최소 $N$
* **장점:** 매우 유연함; "예상하는 것을 시뮬레이션"과 일치
* **단점:** 가정에 크게 의존; 계산 비용

**D11 — 업데이트 / 재보정 (절편/기울기)**
* **사용 시점:** 기존 모델을 재보정하고 적절한 정밀도가 필요할 때.
* **사용하지 말아야 할 경우:** 완전히 새로운 모델을 개발할 때 (C5–C7 사용).
* **주요 입력:** 업데이트 유형, 사건 발생률, 정밀도 목표
* **핵심 출력:** 안정적인 업데이트에 충분한 $N$
* **장점:** 실제 배포에 실용적
* **단점:** 지역 케이스 믹스 및 모델 이동성 가정에 의존

---

#### 면책 조항

임상적 보증 없음; 사용자는 검증 및 해석에 책임이 있습니다. 항상 가정을 문서화하고 민감도 분석을 수행하세요.

#### 연락처

저자 및 유지관리: Minh Nguyen (minhnt@ump.edu.vn)
""",

        "a2_content_md": """
### 이것은 무엇입니까

이 모듈은 **원하는 정밀도**(신뢰 구간(CI) 반폭 또는 오차 한계로 표현됨)로 **기본 위험 / 사건 발생률**(p)(즉, 결과의 유병률)을 추정하는 데 필요한 **최소 표본 크기(n)**를 추정합니다.

다음과 같은 경우에 유용합니다:
* 지정된 정밀도로 코호트 내 결과 유병률 설명,
* 타당성 계획 및 기본 위험 보고,
* 교정 관련 계획 지원 (예: calibration-in-the-large는 사건 발생률에 의존).

**중요한 제한 사항:** 이 계산은 예측 모델 성능(AUC, 교정 기울기, 낙관주의)을 **보장하지 않습니다**. 오직 (p) 추정의 정밀도만을 목표로 합니다.

---

### 입력 값 (의미)

1. **결과 유병률 / 사건 발생률** (p)
   대상 모집단에서 예상되는 사건 비율 (예: 0.10).
   * 알 수 없는 경우, 타당한 범위를 고려하여 민감도 분석을 실행하십시오.
   * 유병률 정밀도에 대해 보수적인 "최악의 경우"를 원한다면 (p=0.50)을 사용하십시오 (분산 최대화).

2. **목표 반폭 (오차 한계)** (d)
   CI가 대략 다음과 같도록 하는 원하는 정밀도:
   $p \pm d$
   예: (d = 0.01, 0.02, 0.03) (즉, ±1%, ±2%, ±3%).

3. **신뢰 수준** (1-$\\alpha$)
   일반적인 값: 0.95 또는 0.99.

4. **CI 방법**
* **Wilson score (권장):** Wald보다 커버리지가 좋으며, 특히 (p)가 0이나 1에 가깝거나 표본 크기가 적당할 때 좋습니다.
* **Wald (정규 근사):** 간단한 폐쇄형이지만 (n)이 작거나 (p)가 극단적일 때 성능이 떨어질 수 있습니다.
* **Clopper–Pearson (정확):** 보수적입니다 (종종 더 넓은 CI를 산출하므로 더 큰 (n)이 필요함).

---

### 핵심 계산 (원리)

$X \sim \\text{Binomial}(n,p)$, $\hat p = X/n$이라고 합시다. 목표는 선택한 CI 방법이 다음을 산출하도록 하는 가장 작은 (n)을 찾는 것입니다:
$$
\\frac{\\text{Upper}(n) - \\text{Lower}(n)}{2} \le d
$$

#### A) Wald (폐쇄형 근사)
$$ n \\approx \\frac{z^2 p(1-p)}{d^2} $$
**참고:** 빠르지만 (n)이 작거나 (p)가 극단적일 때는 권장되지 않습니다.

#### B) Wilson score 구간 (권장)
Wilson score 구간 공식을 사용합니다.

#### C) Clopper–Pearson “정확” 구간
Beta 분위수를 사용합니다. 보수적인 방법입니다.

---

### 실용적인 기본값

* **신뢰 수준:** 95%가 표준입니다.
* **반폭 (d):** ±0.01 ~ ±0.03 (1%–3%)이 일반적인 목표입니다.
* **방법:** Wilson이 강력한 기본값입니다.

### 주요 참고 문헌
1. **Wilson EB.** Probable inference... *JASA.* 1927.
2. **Newcombe RG.** Two-sided confidence intervals... *Stat Med.* 1998.
""",

        "b3_content_md": """
### Purpose (what this method is)

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

## Statistical model and parameters

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

## Inputs (what each value means)

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
### What this method is

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
R^2_{CS} = 1-\\exp\\left(\\frac{2}{n}(\\ell_0-\\ell_1)\\right),
$$
where $\\ell_0$ is the intercept-only log-likelihood and $\\ell_1$ is the model log-likelihood.

For binary outcomes, $R^2_{CS}$ cannot reach 1. Its maximum depends on the outcome prevalence:
$$
\\ell_0 = n\\Big[p\\ln(p) + (1-p)\\ln(1-p)\\Big],
$$
$$
R^2_{CS,\\max}=1-\\exp\\left(\\frac{2\\ell_0}{n}\\right)
=1-\\exp\\Big(2[p\\ln(p) + (1-p)\\ln(1-p)]\\Big).
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
\\frac{P}{(S-1)\\ln\\left(1-\\frac{R^2_{CS}}{S}\\right)}
\\right\\rceil.
$$

### Criterion 2 — Limit optimism in ($R^2$) (default absolute difference 0.05)

This criterion targets a small absolute difference (default $\\delta=0.05$) between apparent and adjusted **Nagelkerke** ($R^2$). The required shrinkage implied by this constraint is:
$$
S_{\\delta}=\\frac{R^2_{CS}}{R^2_{CS}+\\delta R^2_{CS,\\max}}.
$$
Then:
$$
n_2=\\left\\lceil
\\frac{P}{(S_{\\delta}-1)\\ln\\left(1-\\frac{R^2_{CS}}{S_{\\delta}}\\right)}
\\right\\rceil.
$$

### Criterion 3 — Precise estimation of the overall outcome risk (intercept)

This targets precision of the **average outcome risk** ($p$) (baseline risk) within ($\\pm d$) on the probability scale (default $d=0.05$ at 95% CI):
$$
n_3=\\left\\lceil
\\left(\\frac{z_{1-\\alpha/2}}{d}\\right)^2 p(1-p)
\\right\\rceil,
\\quad \\text{default } z_{0.975}=1.96,; d=0.05.
$$

### Final recommendation

$$
n_{\\min}=\\max(n_1,n_2,n_3),\\qquad
E = n_{\\min}p,\\qquad
EPP=\\frac{E}{P}.
$$

---

## Practical guidance (typical choices)

* **Shrinkage (S)**: use **0.90** as a standard target; consider **0.95** if you want stronger overfitting control or if the model is complex.
* **$\\delta=0.05$** for Criterion 2: commonly kept at the default.
* **Intercept precision (d=0.05)**: default corresponds to estimating baseline risk within ±5%. If baseline risk must be estimated more precisely, you would need a smaller ($d$) (larger ($n$)).
* **Anticipated ($R^2_{CS}$)**:

  * Prefer **optimism-adjusted** values from related studies (or apparent values from external validation data).
  * If only AUC is available, use the published AUC→$R^2_{CS}$ approximation method.
  * If neither is available, the **15% of $R^2_{CS,\\max}$** option is a conservative fallback for exploratory planning—always run sensitivity analyses.

---

## Key references (2–5)

1. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: PART II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
2. Riley RD, Ensor J, Snell KIE, et al. *Calculating the sample size required for developing a clinical prediction model.* BMJ. 2020.
3. Riley RD, Van Calster B, Collins GS. *A note on estimating the Cox–Snell ($R^2$) from a reported C statistic (AUROC) to inform sample size calculations for developing a prediction model with a binary outcome.* Statistics in Medicine. 2021.
4. Harrell FE Jr, Lee KL, Mark DB. *Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors.* Statistics in Medicine. 1996.
""",
        "c6_content_md": """
## C6: Development Simulation (Frequentist; custom DGM)

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
[
Y \mid X \sim \\text{Bernoulli}(\\pi), \\qquad
\\pi = \\text{logit}^{-1}(\\eta),
]
[
\\eta = \\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_j),
]
where:

* (P) is the **number of parameters/df** used in the fitted model,
* (f_j(\\cdot)) represent coding choices (linear term, spline basis, dummy coding, etc.).

To achieve a target event rate (p), choose (\\beta_0) so that:
[
\\mathbb{E}[\\pi] = p.
]
In practice, (\\beta_0) is found by numerical root-finding using Monte Carlo draws from (X).

### Step 2 — Generate a development dataset

For replicate (r):

* Simulate (X^{(r)}) of size (N) from the chosen predictor distribution (with specified correlations).
* Simulate (Y^{(r)}) from the Bernoulli model above.

### Step 3 — Fit the development model

Fit the planned logistic regression model:
[
\\widehat{\\eta} = \\widehat{\\beta}*0 + \\sum*{j=1}^{P}\\widehat{\\beta}_j f_j(X_j).
]
**Important:** Simulation must match your intended development strategy (e.g., penalization, pre-specified terms). If separation/non-convergence occurs, a ridge-penalized fallback is often used (and should be counted and reported).

### Step 4 — Evaluate on new data

Generate an independent test set (size (N_{\\text{test}}), often large such as 5000–10000) from the same DGM and compute:

**(a) Discrimination (AUC / C-statistic)**
[
\\mathrm{AUC}=\\Pr(\\widehat{\\eta}_1 > \\widehat{\\eta}_0),
]
the probability that a randomly selected case has a higher predicted risk than a non-case.

**(b) Calibration slope**
Estimate (b) from a calibration model on the test set:
[
\\text{logit}(Y) = a + b \\cdot \\text{logit}(\\widehat{p}),
]
or equivalently using the linear predictor:
[
\\text{logit}(Y) = a + b \\cdot \\widehat{\\eta}.
]
Here, (b\\approx 1) indicates good calibration; (b<1) suggests overfitting (predictions too extreme).

### Step 5 — Define pass/fail criteria and compute success rates

Across (R) simulations for each (N), compute:

* Mean calibration slope:
  [
  \\overline{b} = \\frac{1}{R}\\sum_{r=1}^R b^{(r)}.
  ]
* Probability slope is within an acceptable range:
  [
  \\widehat{\\Pr}(b \\in [L,U]) = \\frac{1}{R}\\sum_{r=1}^R \\mathbf{1}{b^{(r)}\\in[L,U]}.
  ]
* Mean AUC:
  [
  \\overline{\\mathrm{AUC}}=\\frac{1}{R}\\sum_{r=1}^R \\mathrm{AUC}^{(r)}.
  ]

A candidate (N) is “acceptable” if all selected criteria are met, e.g.:

* (\\overline{b} \\ge 0.90)
* (\\widehat{\\Pr}(0.9 \\le b \\le 1.1) \\ge 0.80)
* (\\overline{\\mathrm{AUC}} \\ge \\mathrm{AUC}_{\\text{target}})

Choose the **smallest** (N) that passes.

---

# Inputs in the app (where to find them, typical values)

### 1) Outcome prevalence / event rate (p)

**What it is:** expected proportion of events in the development cohort.
**Where to get it:** local hospital incidence/prevalence (best), registry data, or prior studies in similar settings.
**Typical planning ranges:** 5%–15% are common in many clinical contexts (but vary widely).
**Tip:** If uncertain, run **sensitivity analysis** over a plausible range.

### 2) Number of predictor parameters (df) (P)

**What it is:** total degrees of freedom (excluding intercept), including:

* categorical dummies,
* spline bases,
* interactions,
* any additional engineered terms.
  **Where to get it:** your *final* planned model specification (TRIPOD-style pre-specification).
  **Typical values:** 10–30 df are common; higher requires stronger evidence and larger samples.

### 3) Target mean AUC (Mode A)

**What it is:** expected discrimination on new data (optimism-adjusted).
**Where to get it:** prior models in similar populations, pilot data, or published AUCs (prefer externally validated AUC).
**Typical values:** 0.70–0.85 are common; >0.90 is unusual and often optimistic.

### 4) Candidate sample sizes (N)

Provide a grid (e.g., 1000, 1500, 2000, 3000, 5000).
**Tip:** include a smaller and larger value to ensure the pass/fail threshold is crossed.

### 5) Number of simulations per (N): (R)

**Interpretation:** Monte Carlo replications.

* Demo: (R \\approx 200) (fast, higher Monte Carlo error)
* Final: (R \\ge 1000) (more stable)
  Monte Carlo standard error for a pass probability (\\hat{p}) is:
  [
  \\mathrm{MCSE}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{R}}.
  ]
  Example: if (\\hat{p}=0.8) and (R=200), MCSE ≈ 0.028.

### 6) Performance criteria (Pass/Fail)

* **Mean calibration slope ≥ 0.9**
  (typical overfitting control threshold)
* **Pr(0.9 ≤ slope ≤ 1.1) ≥ 80%**
  (typical “acceptable calibration” probability threshold)
* **Mean AUC ≥ target**
  (discrimination target)

**Where to get thresholds:** practice guidelines, prior studies, and what is clinically acceptable.
**Common conventions:** slope range 0.90–1.10 and assurance 0.80 are frequently used for planning; use 0.90 assurance for higher certainty.

---

# Strengths and weaknesses

**Strengths**

* Flexible: accommodates correlations, non-linear terms, and realistic modeling choices.
* Directly targets new-data performance and calibration behavior.
* Naturally supports sensitivity analyses.

**Weaknesses**

* Results depend on DGM assumptions (garbage in → garbage out).
* Computationally intensive.
* Must simulate the full intended modeling pipeline; otherwise results can be misleading.

---

## Key references (2–5)

1. Pavlou M, Ambler G, Seaman SR, et al. *How to develop a more accurate risk prediction model when there are few events.* BMJ. 2015.
2. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
3. Pavlou M, et al. *Methodology and software for simulation-based sample size calculation in prediction modeling* (sampsize development/related work). Statistics in Medicine. 2021.
4. Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating.* 2nd ed. Springer. 2019.
""",
    "c7_content_md": """
## C7: Bayesian Assurance (MCMC)

### What this method is
**Bayesian assurance** is a simulation-based approach to sample size planning for **Bayesian model development** (here: Bayesian logistic regression for a binary outcome).  
Instead of targeting "power" (frequentist), assurance targets the **unconditional probability** that your study will meet **pre-specified success criteria** (e.g., calibration and discrimination thresholds, and/or posterior precision).

In plain terms:
> "If we repeat the whole study many times (data generation + Bayesian MCMC fitting), what is the probability that the fitted model will be good enough?"

---

### When to use
Use C7 when:
- Your final analysis is **Bayesian** and will be estimated by **MCMC**.
- You want sample size chosen to achieve **a target probability of success** (e.g., ≥80% or ≥90%).
- You can specify reasonable assumptions for:
  - event rate in your hospital cohort,
  - predictor correlation structure and distributions,
  - plausible effect sizes (from local pilot data or literature),
  - priors for regression coefficients.

### When NOT to use (or use with caution)
Avoid relying on C7 alone when:
- You cannot justify priors or a plausible **data-generating mechanism (DGM)**.
- You do not have the compute budget (MCMC is slow; results can be sensitive to MCMC settings).
- Your real development pipeline includes substantial data-adaptive steps (feature selection, heavy tuning) that you are **not** simulating.
- Data are clustered/multicenter but the DGM ignores clustering (may underestimate required N).

---

## Core model and DGM

### Bayesian logistic regression (analysis model)
\[
Y_i \sim \\text{Bernoulli}(\\pi_i), \\qquad
\\text{logit}(\\pi_i)=\\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_{ij})
\]
- \(P\) = number of predictor parameters (degrees of freedom; **exclude intercept**).
- \(f_j(\\cdot)\) represents your coding choices (linear term, dummies, spline bases, interactions).

**Example priors (typical weakly informative defaults):**
\[
\\beta_j \sim \\mathcal{N}(0,\\sigma_\\beta^2),\\quad \\sigma_\\beta \\in [1, 2.5],
\\qquad \\beta_0 \sim \\mathcal{N}(0, 5^2)
\]
(Your app may use fixed priors; users should run sensitivity analyses over plausible priors.)

### DGM for predictors (example equicorrelation)
If the app uses a single correlation parameter \\(\\rho\\) (equicorrelation):
\[
\\mathrm{Corr}(X_j, X_k)=\\rho \\quad (j\\neq k),
\\qquad
\\Sigma_{jk}=
\\begin{cases}
1,& j=k\\\\
\\rho,& j\\neq k
\\end{cases}
\]
Predictors are then generated from a correlated mechanism (e.g., Gaussian copula / multivariate normal core), and transformed into continuous/binary predictors as needed.

### Setting the event rate
The intercept (or a calibration constant) is chosen so that the marginal event rate matches the target prevalence:
\[
\\mathbb{E}[\\pi_i]=p
\]
This is typically solved numerically using Monte Carlo draws of \(X\).

---

## What "assurance" means (key formula)
Let:
- \\(\\theta\\) denote the "true" parameters under the DGM (effect sizes, correlation structure, etc.).
- \\(y\\) denote the observed dataset of size \\(N\\).
- \\(S(y)\\) be a **success indicator** that equals 1 if performance/precision criteria are met.

**Assurance at sample size \\(N\\):**
\[
\\mathcal{A}(N)=\\Pr(\\text{Success at }N)
=\\mathbb{E}_{\\theta}\\left[\\mathbb{E}_{y\\mid \\theta,N}\\left\\{S(y)\\right\\}\\right]
\]

**Monte Carlo estimate used in the app (for each candidate \\(N\\)):**
\[
\\widehat{\\mathcal{A}}(N)=\\frac{1}{R}\\sum_{r=1}^{R} S\\!\\left(y^{(r)}\right)
\]
where each replicate \\(r\\) simulates a dataset, fits the Bayesian model with MCMC, and evaluates success criteria.

Monte Carlo standard error (helpful for interpreting stability):
\[
\\mathrm{MCSE}\\left(\\widehat{\\mathcal{A}}(N)\\right)
=\\sqrt{\\frac{\\widehat{\\mathcal{A}}(N)\\left[1-\\widehat{\\mathcal{A}}(N)\\right]}{R}}
\]

**Decision rule:**
Choose the smallest \\(N\\) such that:
\[
\\widehat{\\mathcal{A}}(N)\\ge \\mathcal{A}_\\text{target}
\]
(e.g., 0.80 or 0.90).

---

## Success criteria (typical examples)
Your app may implement one or more of the following (user-selectable):
- **Calibration slope** in an acceptable range:
  \[
  0.90 \le b \le 1.10
  \]
  where \\(b\\) is estimated from a calibration model on validation/test data:
  \[
  \\text{logit}(Y)=a + b\\cdot \\text{logit}(\\widehat{p})
  \]
- **Discrimination** threshold:
  \[
  \\mathrm{AUC} \\ge 0.75 \\;(\\text{or your chosen target})
  \]
- **Posterior precision** target, e.g. 95% credible interval width for calibration slope:
  \[
  \\mathrm{Width}\\left(\\text{CrI}_{95\\%}(b)\\right) \\le w
  \\quad (\\text{e.g., } w=0.20)
  \]

---

## Input guide (where to find values; typical choices)

### 1) Outcome prevalence (event rate) \\(p\\)
**Where to get it:** local hospital cohort/registry; recent retrospective data.  
**Typical planning ranges:** 0.05–0.15 are common in many clinical settings, but use your disease context.  
**Tip:** If uncertain, run a sensitivity analysis over a plausible range.

### 2) Number of predictor parameters (df) \\(P\\)
**Where to get it:** your finalized model specification (count **parameters**, not variables).  
Include dummies, spline bases, interactions. Exclude intercept.  
**Typical range:** 10–30 df is common; larger df demands much larger \\(N\\) and stronger prior justification.

### 3) Predictor correlation \\(\\rho\\)
**Where to get it:** estimate from pilot/hospital data (correlation matrix of candidate predictors).  
If unknown, use sensitivity analysis (e.g., \\(\\rho=0, 0.1, 0.3\\)).  
**Typical:** mild-to-moderate correlations (0–0.3) are common; higher correlations increase instability and may increase required \\(N\\).

### 4) Candidate sample sizes \\(N\\)
Choose a grid wide enough to cross the pass/fail boundary (e.g., 500, 1000, 1500, 2000, …).  
Start from feasibility constraints (available charts/records) and expand upward.

### 5) Number of simulations per \\(N\\) (replicates) \\(R\\)
- **Demo:** 50–200 (fast; higher MC error)  
- **Final planning:** ≥500–1000 (more stable assurance estimate)  
Use MCSE to judge stability.

### 6) Assurance threshold \\(\\mathcal{A}_\\text{target}\\)
- **0.80**: common for feasibility-driven planning  
- **0.90**: preferred when you want higher confidence in meeting criteria

---

## Strengths and weaknesses
**Strengths**
- Fully aligned with Bayesian workflows; directly targets **posterior** success/precision.
- Flexible: accommodates complex DGM, correlations, and performance-based criteria.
- Can incorporate prior knowledge and realistically handle rare events with regularizing priors.

**Weaknesses**
- Computationally intensive; results can depend on MCMC settings and convergence.
- Sensitive to DGM and prior assumptions → requires sensitivity analyses.
- Must simulate the actual planned pipeline to avoid under/over-estimation.

---

## Key references (2–5)
1) O'Hagan A. Assurance in clinical trial design. *Pharmaceutical Statistics.* 2005.  
2) Pan J, Banerjee S. bayesassurance: An R Package for Calculating Sample Size and Bayesian Assurance. *The R Journal.* 2023.  
3) Gelman A, Jakulin A, Pittau MG, Su Y-S. A weakly informative default prior distribution for logistic and other regression models. *The Annals of Applied Statistics.* 2008.  
4) Sahu SK, Smith TMF. Bayesian methods of sample size determination. *Statistical Methodology / related Bayesian SSD literature.* 2006.
""",
}
