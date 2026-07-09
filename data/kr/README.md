# Online-Mind2Web KR Extension

한국 웹사이트를 포함하도록 Online-Mind2Web 벤치마크를 확장한 브랜치입니다.

## 개요

원본 Online-Mind2Web이 영어권 136개 글로벌 웹사이트 300개 태스크로 구성되어 있는 것과 달리, 이 확장은 한국 사용자가 실제로 사용하는 주요 웹사이트들을 추가하여 웹 에이전트의 한국 환경 대응 능력을 평가합니다.

- **태스크 수**: 222개
- **고유 웹사이트 수**: 104개
- **도메인**: 원본 12개 도메인 분류를 그대로 따름
- **Baryon 꾸러미 매핑**: [Baryon Desktop](https://desktop.baryon.ai/packages.html)의 19개 업무별 꾸러미에 대응 (`baryon_bundle` 필드로 추적)
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
| Education | 36 |
| Government & Services | 32 |
| Technology | 28 |
| Other | 23 |
| Shopping & E-Commerce | 23 |
| Travel & Transportation | 18 |
| Jobs & Careers | 15 |
| Finance & Investment | 15 |
| Entertainment & Media | 11 |
| Housing & Real Estate | 8 |
| Health & Medical | 7 |
| Food & Recipes | 6 |

### 난이도별
| 난이도 | 태스크 수 | 기준 |
|---|---|---|
| easy | 47 | reference_length ≤ 5 |
| medium | 156 | 6 ≤ reference_length ≤ 10 |
| hard | 19 | reference_length ≥ 11 |

### 웹사이트별 (상위)
| 웹사이트 | 태스크 수 | 도메인 |
|---|---|---|
| finance.naver.com | 7 | Finance & Investment |
| 10000recipe.com | 6 | Food & Recipes |
| coupang.com | 6 | Shopping & E-Commerce |
| inflearn.com | 5 | Education |
| movie.naver.com | 4 | Entertainment & Media |
| saramin.co.kr | 4 | Jobs & Careers |
| nts.go.kr | 4 | Government & Services |
| jobkorea.co.kr | 4 | Jobs & Careers |
| flight.naver.com | 4 | Travel & Transportation |
| law.go.kr | 3 | Government & Services |
| ... | ... | ... |

### Baryon 꾸러미 매핑
[Baryon Desktop](https://desktop.baryon.ai/packages.html)의 업무별 꾸러미에 대응하는 태스크들. 각 태스크의 `baryon_bundle` 필드로 원본 꾸러미 slug를 추적.

| Baryon 꾸러미 | 태스크 수 | 사이트 수 | 대표 사이트 |
|---|---|---|---|
| data (데이터분석) | 8 | 4 | data.go.kr, kosis.kr, bigdata.go.kr |
| design (디자인) | 7 | 6 | figma.com, coolors.co, behance.net |
| dev (개발) | 6 | 5 | github.com, stackoverflow.com, docs.python.org |
| docs (사내문서분석) | 4 | 4 | law.go.kr, archives.go.kr, kyobobook.co.kr |
| ecommerce (이커머스운영) | 9 | 6 | coupang.com, sell.smartstore.naver.com, selling.kakao.com |
| education (교육/이러닝) | 6 | 3 | kmooc.kr, edwith.org, inflearn.com |
| finance (재무) | 7 | 4 | bok.or.kr, fss.or.kr, kidi.or.kr |
| hr (인사) | 6 | 4 | saramin.co.kr, jobkorea.co.kr, indeed.com |
| legal (법무) | 8 | 3 | law.go.kr, court.go.kr, klri.re.kr |
| logistics (물류) | 8 | 4 | cjlogistics.com, lottelogistics.com, epost.go.kr |
| marketing (마케팅) | 8 | 6 | ads.google.com, business.facebook.com, tistory.com |
| operator (운영자) | 8 | 5 | cloudflare.com, amazonaws.com, vercel.com |
| product (제품기획) | 6 | 5 | figma.com, producthunt.com, betterworks.com |
| research (연구) | 9 | 5 | riss.kr, dbpia.co.kr, scienceon.kr |
| sales (영업) | 6 | 4 | tripadvisor.co.kr, mangoplate.com, crm.withncorp.com |
| student (학생) | 8 | 4 | acmicpc.net, inflearn.com, programmers.co.kr |
| support (고객지원) | 8 | 6 | kt.com, skt.com, help.coupang.com |
| tax (세무) | 7 | 3 | nts.go.kr, hometax.go.kr, elinf.co.kr |
| translation (번역) | 7 | 3 | dict.naver.com, terms.naver.com, dict.daum.net |

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
- cjlogistics.com (CJ대한통운) — 물류
- lottelogistics.com (롯데글로벌로지스틱스) — 물류

### 금융 (Finance & Investment)
- finance.naver.com (네이버 증권)
- kbanknow.com (카카오뱅크)
- bok.or.kr (한국은행) — 재무
- fss.or.kr (금융감독원) — 재무

### 건강/의료 (Health & Medical)
- amc.seoul.kr (서울아산병원)
- samsunghospital.com (삼성서울병원)
- naver.com 건강 (네이버 건강)
- nihcm.go.kr (국립보건연구원)

### 식품/레시피 (Food & Recipes)
- 10000recipe.com (만개의 레시피)
- mangoplate.com (망고플레이트) — 영업

### 엔터테인먼트 (Entertainment & Media)
- movie.naver.com (네이버 영화)
- comic.naver.com (네이버 웹툰)
- behance.net (비핸스) — 디자인
- unsplash.com (언스플래시) — 디자인

### 정부/공공서비스 (Government & Services)
- gov.kr (정부24)
- nts.go.kr (국세청 홈택스) — 세무
- hometax.go.kr (홈택스) — 세무
- epeople.go.kr (국민신문고)
- law.go.kr (국가법령정보센터) — 법무
- kosis.kr (국가통계포털) — 데이터분석
- data.go.kr (공공데이터포털) — 데이터분석

### 기술 (Technology)
- samsung.com/sec (삼성전자)
- lge.co.kr (LG전자)
- figma.com (피그마) — 디자인/제품기획
- aws.amazon.com (AWS) — 운영자
- cloudflare.com (Cloudflare) — 운영자
- vercel.com (Vercel) — 운영자
- betterworks.com (BetterWorks) — 제품기획

### 교육 (Education)
- inflearn.com (인프런)
- credu.com (크레듀)
- riss.kr (RISS 학술연구정보서비스) — 연구
- dbpia.co.kr (DBpia) — 연구
- scienceon.kr (ScienceON) — 연구
- kmooc.kr (K-MOOC) — 교육/이러닝
- acmicpc.net (백준 온라인 저지) — 학생
- dict.naver.com (네이버 사전) — 번역

### 기타 (Other)
- map.naver.com (네이버 지도)
- news.naver.com (네이버 뉴스)
- terms.naver.com (네이버 용어사전) — 번역
- search.naver.com (네이버 검색)
- kt.com (KT 고객지원) — 고객지원
- skt.com (SKT 고객지원) — 고객지원
- help.naver.com (네이버 고객센터) — 고객지원
- ads.google.com (Google Ads) — 마케팅
- business.facebook.com (Meta Business Suite) — 마케팅
- sell.smartstore.naver.com (네이버 스마트스토어 판매자센터) — 이커머스운영

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