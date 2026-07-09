# Online-Mind2Web KR Extension

한국 웹사이트를 포함하도록 Online-Mind2Web 벤치마크를 확장한 브랜치입니다.

## 개요

원본 Online-Mind2Web이 영어권 136개 글로벌 웹사이트 300개 태스크로 구성되어 있는 것과 달리, 이 확장은 한국 사용자가 실제로 사용하는 주요 웹사이트들을 추가하여 웹 에이전트의 한국 환경 대응 능력을 평가합니다.

- **태스크 수**: 86개
- **고유 웹사이트 수**: 34개
- **도메인**: 원본 12개 도메인 분류를 그대로 따름
- **스키마**: 원본 v2 스키마(`online-mind2web-v2`)와 호환

## 디렉토리 구조

```
data/kr/
├── README.md            # 이 파일
├── tasks/               # 태스크 정의 (task_id.json per task)
│   ├── 056ca7....json
│   └── ...
└── example_kr/          # 예시 trajectory (에이전트 실행 결과)
    ├── result.json
    └── trajectory/
```

각 태스크 JSON 파일의 필드:
| 필드 | 설명 |
|---|---|
| `task_id` | `md5(website|task_description)` 해시 |
| `website` | 시작 URL (에이전트는 여기서 시작해야 함, Google Search 금지) |
| `task_description` | 한국어 자연어 태스크 지시문 |
| `reference_length` | 인간 annotator 기준 예상 스텝 수 |
| `domain` | 12개 도메인 중 하나 |
| `difficulty` | `easy` (≤5스텝) / `medium` (6-10) / `hard` (≥11) |

## 태스크 분포

### 도메인별
| 도메인 | 태스크 수 |
|---|---|
| Shopping & E-Commerce | 10 |
| Housing & Real Estate | 8 |
| Travel & Transportation | 8 |
| Finance & Investment | 8 |
| Jobs & Careers | 8 |
| Other | 8 |
| Entertainment & Media | 7 |
| Food & Recipes | 6 |
| Government & Services | 6 |
| Education | 6 |
| Health & Medical | 6 |
| Technology | 5 |

### 난이도별
| 난이도 | 태스크 수 | 기준 |
|---|---|---|
| easy | 17 | reference_length ≤ 5 |
| medium | 58 | 6 ≤ reference_length ≤ 10 |
| hard | 11 | reference_length ≥ 11 |

### 웹사이트별 (상위)
| 웹사이트 | 태스크 수 | 도메인 |
|---|---|---|
| finance.naver.com | 7 | Finance & Investment |
| 10000recipe.com | 6 | Food & Recipes |
| coupang.com | 4 | Shopping & E-Commerce |
| movie.naver.com | 4 | Entertainment & Media |
| flight.naver.com | 4 | Travel & Transportation |
| inflearn.com | 4 | Education |
| letskorail.com | 3 | Travel & Transportation |
| land.naver.com | 3 | Housing & Real Estate |
| saramin.co.kr | 3 | Jobs & Careers |
| jobkorea.co.kr | 3 | Jobs & Careers |
| ... | ... | ... |

분포 통계 실행:
```bash
python3 script/kr_stats.py
```

## 포함된 한국 웹사이트 목록

### 부동산 (Housing & Real Estate)
- zigbang.com (직방)
- dabangapp.com (다방)
- land.naver.com (네이버 부동산)

### 채용 (Jobs & Careers)
- saramin.co.kr (사람인)
- jobkorea.co.kr (잡코리아)
- wanted.co.kr (원티드)

### 쇼핑 (Shopping & E-Commerce)
- coupang.com (쿠팡)
- 11st.co.kr (11번가)
- browse.gmarket.co.kr (G마켓)
- ssg.com (SSG)

### 여행/교통 (Travel & Transportation)
- letskorail.com (레츠코레일)
- flight.naver.com (네이버 항공권)
- bustago.or.kr (버스타고)

### 금융 (Finance & Investment)
- finance.naver.com (네이버 증권)
- kbanknow.com (카카오뱅크)

### 건강/의료 (Health & Medical)
- amc.seoul.kr (서울아산병원)
- samsunghospital.com (삼성서울병원)
- naver.com 건강 (네이버 건강)

### 식품/레시피 (Food & Recipes)
- 10000recipe.com (만개의 레시피)

### 엔터테인먼트 (Entertainment & Media)
- movie.naver.com (네이버 영화)
- comic.naver.com (네이버 웹툰)

### 정부/공공서비스 (Government & Services)
- gov.kr (정부24)
- nts.go.kr (국세청 홈택스)
- epeople.go.kr (국민신문고)

### 기술 (Technology)
- samsung.com/sec (삼성전자)
- lge.co.kr (LG전자)

### 교육 (Education)
- inflearn.com (인프런)
- credu.com (크레듀)

### 기타 (Other)
- map.naver.com (네이버 지도)
- news.naver.com (네이버 뉴스)
- terms.naver.com (네이버 사전)
- search.naver.com (네이버 검색)

## 사용 방법

### 1. 태스크 ID 생성 (이미 완료됨)
```bash
python3 script/gen_kr_task_ids.py --write
```

### 2. 에이전트로 태스크 실행
각 태스크의 `website` URL에서 시작하여 `task_description`을 수행. 결과를 아래 구조로 저장:
```
<task_id>/
├── result.json          # v2 스키마
└── trajectory/
    ├── 0000.png
    ├── 0001.png
    └── ...
```

`result.json` 포맷은 `data/schema_v2/README.md` 참고.

### 3. 평가 실행
```bash
# 환경 변수로 API 키와 모델 지정
export API_KEY=sk-...
export MODEL_NAME=o4-mini    # 권장

# 기본 예시로 평가
bash ./script/eval_kr.sh

# 커스텀 trajectory 디렉토리로 평가
bash ./script/eval_kr.sh /path/to/trajectories

# 특정 평가 모드 지정
MODE=WebJudge_Online_Mind2Web_eval bash ./script/eval_kr.sh /path/to/traj
```

## WebClaw 연동

이 KR 벤치마크는 [WebClaw](https://github.com/DureClaw/webclaw) 브라우저 노드를 활용하여 태스크를 실행하는 것을 목표로 합니다. WebClaw는 Chrome MV3 확장 프로그램으로, 실제 브라우저 세션을 fleet node로 사용하여 CORS-free fetch, DOM 조작, 클릭, 폼 입력 등을 수행합니다.

### WebClaw가 KR 사이트에서 유리한 점

1. **실제 브라우저 세션**: 로그인이 필요한 한국 사이트(직방, 다방, 쿠팡 등)에서 사용자 세션 활용 가능
2. **CORS-free fetch**: 한국 금융 사이트의 API 호출 시 CORS 제한 우회
3. **`[CLICKTEXT]`**: React/모달 기반 한국 사이트에서 CSS 셀렉터 없이 텍스트로 클릭
4. **`[TABS]` + `@<url>`**: 여러 탭 중 로그인된 세션 타겟팅
5. **`[SNAP]`/`[DIFF]`**: DOM 변화 감지로 액션 성공 여부 판정 (스크린샷 없이도 가능)

### WebClaw 실행 파이프라인

```
KR 태스크 정의 (data/kr/tasks/)
        │
        ▼
script/run_webclaw_kr.py  ←── master brain (LLM)
        │
        ▼  (WebSocket bus)
WebClaw Chrome 확장 (browser node)
        │
        ▼  (task frames)
src/kr/webclaw_adapter.py  ←── 변환
        │
        ▼  (v2 result.json + trajectory/)
WebJudge 평가 (src/run.py)
        │
        ▼
평가 결과 (성공률)
```

### 실행 순서

1. **WebClaw 확장 설치 및 패치 적용**:
   - [WebClaw 패치 가이드](./webclaw_patches/README.md) 참고
   - `[SCREENSHOT]`, `[SCROLL]`, `[WAIT_SEL]` 마커 추가 필요

2. **WebClaw 노드 실행**:
   - Chrome에서 WebClaw 확장 로드
   - Bus, Token, Work Key, Brain URL 설정 후 fleet 연결

3. **KR 태스크 실행**:
   ```bash
   python3 script/run_webclaw_kr.py \
       --bus ws://localhost:4000 \
       --token <secret> \
       --work-key <key> \
       --node-name webclaw@chrome-1 \
       --brain-url http://localhost:8000 \
       --brain-token <token> \
       --output-dir ./data/kr/trajectories
   ```

4. **WebJudge 평가**:
   ```bash
   export API_KEY=sk-...
   export MODEL_NAME=o4-mini
   bash ./script/eval_kr.sh ./data/kr/trajectories
   ```

### WebClaw 도구 → v2 ActionStep 매핑

| WebClaw 마커 | v2 Action verb | 설명 |
|---|---|---|
| `[OPEN] <url>` | NAVIGATE | URL로 이동 |
| `[CLICK] <sel>` | CLICK | 셀렉터로 클릭 |
| `[CLICKTEXT] <label>` | CLICK | 텍스트로 클릭 (한국 사이트 모달에 유리) |
| `[FILL]`/`[TYPE]` sel=val | TYPE | 입력 필드 채우기 |
| `[SUBMIT] <sel>` | PRESS_KEY | 폼 제출 |
| `[DOM]`/`[LINKS]`/`[ATTR]` | WAIT | 관찰 단계 (액션 아님) |
| `[JS] <code>` | WAIT | JS 실행 (관찰) |
| `[SNAP]`/`[DIFF]` | WAIT/action | DOM 스냅샷/비교 |
| `[SCREENSHOT]` | (캡처) | trajectory 스크린샷 생성 |
| `TASK_COMPLETE` | TASK_COMPLETE | 태스크 완료 |

변환 어댑터: `src/kr/webclaw_adapter.py`

## 주의사항

- **시작 URL 준수**: 각 태스크는 지정된 `website` URL에서 시작해야 함 (Google Search 금지)
- **실제 사이트**: 모든 웹사이트는 live 실제 사이트임. 웹사이트 변경 시 태스크가 무효화될 수 있음
- **한국어 처리**: 에이전트와 WebJudge 평가 모델 모두 한국어 처리 능력이 필요함. o4-mini는 한국어 처리에 우수한 성능을 보임
- **로그인 필요 사이트**: 일부 사이트(직방, 다방 등)는 일부 기능에 로그인이 필요할 수 있음. 에이전트 실행 시 이를 고려해야 함
- **CAPTCHA**: 일부 한국 사이트는 봇 탐지가 활성화되어 있을 수 있음. 실행 불가능한 태스크는 `human_label`에서 `2`(Not Executable)로 표시

## 원본 벤치마크와의 관계

이 확장은 원본 Online-Mind2Web 벤치마크와 **독립적으로** 실행됩니다. 원본 300개 태스크와 KR 86개 태스크를 합쳐 386개 태스크로 평가하거나, KR 태스크만 별도로 평가할 수 있습니다.

원본 벤치마크 정보: [README.md](../../README.md)