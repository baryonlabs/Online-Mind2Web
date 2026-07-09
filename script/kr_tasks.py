"""Online-Mind2Web KR extension — task definitions for Korean websites.

Each task follows the same schema as the original Online-Mind2Web dataset:
    - website: starting URL (agents must start here, not from Google Search)
    - task_description: natural-language task instruction (Korean)
    - reference_length: estimated number of steps for a human annotator
    - domain: one of the 12 original domains + "kr-specific" for KR-only categories
    - difficulty: "easy" | "medium" | "hard"  (consistent with original: <=5 / 6-10 / >=11)
"""

KR_TASKS = [

    # ====================================================================
    # Housing & Real Estate (부동산)
    # ====================================================================
    {
        "website": "https://www.zigbang.com",
        "task_description": "직방에서 서울특별시 강남구 역삼동에 있는 월세 방 중 보증금 1000만원 이하, 월세 80만원 이하 조건의 원룸을 찾아 가장 저렴한 매물 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://www.dabangapp.com",
        "task_description": "다방에서 서울특별시 송파구 잠실동 근처 오피스텔 매물 중 전세 2억 이하인 매물을 검색하고, 검색 결과 중 첫 번째 매물의 상세 정보 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://land.naver.com",
        "task_description": "네이버 부동산에서 서울특별시 마포구 합정동 아파트 매매 검색 결과를 보고, 검색 결과 중 평당가가 가장 낮은 아파트 단지의 상세 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Housing & Real Estate",
        "difficulty": "hard",
    },
    {
        "website": "https://land.naver.com",
        "task_description": "네이버 부동산에서 현재 서울특별시 용산구 이촌동의 실거래가 조회 페이지를 열어, 최근 3개월간 아파트 실거래가 거래 내역을 확인하라.",
        "reference_length": 9,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://www.zigbang.com",
        "task_description": "직방에서 부산광역시 해운대구 중동 원룸 매물을 검색하여, 보증금 500만원 이하, 월세 50만원 이하 조건으로 필터링한 결과를 보여라.",
        "reference_length": 7,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://land.naver.com",
        "task_description": "네이버 부동산에서 경기도 수원시 영통구 원천동 아파트 매물 중 10억 이하, 84㎡ 이상 조건으로 검색 결과를 보여라.",
        "reference_length": 8,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://www.dabangapp.com",
        "task_description": "다방에서 인천광역시 연수구 송도동 원룸 매물 중 도보 5분 이내 지하철역 조건으로 필터링하여 검색 결과를 보여라.",
        "reference_length": 7,
        "domain": "Housing & Real Estate",
        "difficulty": "medium",
    },
    {
        "website": "https://www.zigbangapp.com",
        "task_description": "직방에서 서울특별시 성동구 성수동 근처 오피스텔 월세 매물 중 관리비 10만원 이하인 매물을 검색하여 보여주고, 그중 첫 번째 매물 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Housing & Real Estate",
        "difficulty": "hard",
    },

    # ====================================================================
    # Jobs & Careers (채용)
    # ====================================================================
    {
        "website": "https://www.saramin.co.kr",
        "task_description": "사람인에서 서울특별시 지역의 '파이썬 개발자' 정규직 채용 공고를 검색하고, 검색 결과 중 최근 7일 이내에 등록된 공고의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },
    {
        "website": "https://www.jobkorea.co.kr",
        "task_description": "잡코리아에서 경기도 성남시 분당구 지역의 '프론트엔드 개발자' 채용 공고를 검색하고, 검색 결과 중 연봉 4000만원 이상 공고의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },
    {
        "website": "https://www.saramin.co.kr",
        "task_description": "사람인에서 '데이터 분석가' 직무 채용 공고를 검색하고, 그중 신입 가능한 공고를 필터링하여 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },
    {
        "website": "https://www.jobkorea.co.kr",
        "task_description": "잡코리아에서 '마케팅' 직무 채용 공고 중 서울특별시 강남구 소재, 경력 3년 이상 조건으로 검색하고, 검색 결과의 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },
    {
        "website": "https://www.wanted.co.kr",
        "task_description": "원티드에서 '머신러닝 엔지니어' 직군 채용 공고를 검색하고, 그중 서울 근무 가능 공고를 필터링하여 첫 번째 공고의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Jobs & Careers",
        "difficulty": "easy",
    },
    {
        "website": "https://www.wanted.co.kr",
        "task_description": "원티드에서 '프로덕트 매니저' 직군 채용 공고 중 경력 5년 이상, 서울 근무 조건으로 검색하여 검색 결과를 보여주고, 그중 가장 최근에 등록된 공고의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },
    {
        "website": "https://www.saramin.co.kr",
        "task_description": "사람인에서 부산광역시 지역의 '영업직' 채용 공고를 검색하고, 검색 결과 중 대졸 이상, 경력 2년 이상 조건으로 필터링한 결과의 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Jobs & Careers",
        "difficulty": "hard",
    },
    {
        "website": "https://www.jobkorea.co.kr",
        "task_description": "잡코리아에서 '회계' 직무 채용 공고 중 인천광역시 지역, 경력 무관 조건으로 검색하여 검색 결과를 보여주고, 그중 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
    },

    # ====================================================================
    # Shopping & E-Commerce (쇼핑)
    # ====================================================================
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '무선 이어폰'을 검색하고, 검색 결과 중 가격 5만원 이하, 배송 무료인 상품 중 가장 별점이 높은 상품의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.11st.co.kr",
        "task_description": "11번가에서 '삼성 갤럭시 탭'을 검색하고, 검색 결과 중 64GB 이상 저장 용량인 태블릿 상품 중 가장 저렴한 상품의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '치약'을 검색하고, 검색 결과 중 로켓배송 가능한 상품 중 가격이 가장 낮은 상품을 장바구니에 추가하라.",
        "reference_length": 6,
        "domain": "Shopping & E-Commerce",
        "difficulty": "easy",
    },
    {
        "website": "https://browse.gmarket.co.kr",
        "task_description": "G마켓에서 '남성 구두'를 검색하고, 검색 결과 중 가격 5만원 이상 10만원 이하, 스티치 상품 중 가장 인기 있는(구매수 많은) 상품의 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.ssg.com",
        "task_description": "SSG에서 '냉동 피자'를 검색하고, 검색 결과 중 SSG 배송 가능한 상품 중 가격이 1만원 이하인 상품을 장바구니에 추가하라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '등산 배낭 30L'을 검색하고, 검색 결과 중 별점 4점 이상, 가격 3만원 이하인 상품 중 가장 리뷰가 많은 상품의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://browse.gmarket.co.kr",
        "task_description": "G마켓에서 '여성 여름 원피스'를 검색하고, 검색 결과 중 가격 2만원 이하, 무료배송 상품 중 가장 최근에 등록된 상품의 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.11st.co.kr",
        "task_description": "11번가에서 '공기청정기'를 검색하고, 검색 결과 중 적용 면적 33㎡ 이상, 가격 20만원 이하인 상품 중 가장 별점이 높은 상품의 상세 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Shopping & E-Commerce",
        "difficulty": "hard",
    },
    {
        "website": "https://www.ssg.com",
        "task_description": "SSG에서 '한우 1++등급 소고기'를 검색하고, 검색 결과 중 200g 이상 패키지 상품 중 가격이 가장 낮은 상품의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
    },
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '아이패드 10세대'를 검색하고, 검색 결과 중 256GB 모델 중 로켓배송 가능한 상품의 가장 저렴한 상품 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Shopping & E-Commerce",
        "difficulty": "easy",
    },

    # ====================================================================
    # Travel & Transportation (여행/교통)
    # ====================================================================
    {
        "website": "https://www.letskorail.com",
        "task_description": "레츠코레일에서 서울역에서 부산역까지 내일 출발하는 KTX 표준열차 편도 승차권의 예약 페이지를 열어 잔여 좌석을 확인하라.",
        "reference_length": 11,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://flight.naver.com",
        "task_description": "네이버 항공권에서 인천에서 제주행 항공권을 검색하고, 다음 주 금요일 출발, 일요일 귀국 편도 항공권 중 가장 저렴한 항공편의 예약 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
    },
    {
        "website": "https://www.letskorail.com",
        "task_description": "레츠코레일에서 서울역에서 동대구역까지 이번 주 토요일 출발하는 KTX 승차권 중 일반실 예약 가능한 시간대를 확인하라.",
        "reference_length": 10,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://flight.naver.com",
        "task_description": "네이버 항공권에서 김포에서 제주행 왕복 항공권을 검색하고, 다음 달 1일 출발, 3일 귀국 편 중 제주항공 항공권 중 가장 저렴한 것의 예약 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://www.bustago.or.kr",
        "task_description": "버스타고에서 서울경부 터미널에서 부산 터미널까지 내일 출발하는 고속버스 일반 등급 편도 표의 예약 가능 시간대를 확인하라.",
        "reference_length": 11,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://flight.naver.com",
        "task_description": "네이버 항공권에서 인천에서 도쿄행 항공권을 검색하고, 다음 달 15일 출발, 20일 귀국 왕복 항공권 중 가장 저렴한 항공편의 예약 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://www.letskorail.com",
        "task_description": "레츠코레일에서 용산역에서 목포역까지 다음 주 수요일 출발하는 KTX 승차권 중 일반실, 어른 1명 기준 예약 가능 시간대를 확인하라.",
        "reference_length": 11,
        "domain": "Travel & Transportation",
        "difficulty": "hard",
    },
    {
        "website": "https://flight.naver.com",
        "task_description": "네이버 항공권에서 인천에서 방콕행 항공권을 검색하고, 3개월 이내 출발하는 편도 항공권 중 가격이 30만원 이하인 가장 저렴한 항공편의 예약 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
    },

    # ====================================================================
    # Finance & Investment (금융/투자)
    # ====================================================================
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 삼성전자(005930)의 현재 주가와 최근 5일간의 일봉 차트를 보여주는 페이지를 열어라.",
        "reference_length": 5,
        "domain": "Finance & Investment",
        "difficulty": "easy",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 코스피 지수의 현재 값과 최근 1개월 일봉 차트를 보여주는 페이지를 열고, 거래대금 상위 종목 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 시가총액 상위 10개 종목 목록 페이지를 열고, 그중 첫 번째 종목의 재무제표 요약 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 SK하이닉스(000660)의 최근 분기 실적 정보와 외국인 보유율을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 현재 코스닥 지수와 등락률을 확인하고, 코스닥 시장에서 거래량이 가장 많은 종목의 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },
    {
        "website": "https://www.kbanknow.com",
        "task_description": "카카오뱅크 웹사이트에서 현재 정기예금 금리 정보 페이지를 열어, 12개월 만기 정기예금 금리를 확인하라.",
        "reference_length": 6,
        "domain": "Finance & Investment",
        "difficulty": "easy",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 최근 1주일간 외국인이 코스피 시장에서 순매수한 종목 순위 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },
    {
        "website": "https://finance.naver.com",
        "task_description": "네이버 증권에서 현대차(005380)의 최근 3년간 연간 배당금 지급 내역을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Finance & Investment",
        "difficulty": "medium",
    },

    # ====================================================================
    # Health & Medical (건강/의료)
    # ====================================================================
    {
        "website": "https://www.amc.seoul.kr",
        "task_description": "서울아산병원 웹사이트에서 강남 지역 내과 전문의 진료 예약 페이지를 열어, 내일 오전 예약 가능 시간대를 확인하라.",
        "reference_length": 10,
        "domain": "Health & Medical",
        "difficulty": "hard",
    },
    {
        "website": "https://www.samsunghospital.com",
        "task_description": "삼성서울병원 웹사이트에서 진료과별 소개 페이지를 열어, 내과(소화기내과) 전문의 명단을 확인하라.",
        "reference_length": 7,
        "domain": "Health & Medical",
        "difficulty": "medium",
    },
    {
        "website": "https://www.naver.com",
        "task_description": "네이버 건강에서 서울특별시 강남구 소재 피부과 의원을 검색하고, 검색 결과 중 별점 4점 이상인 의원 중 첫 번째의 상세 정보 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Health & Medical",
        "difficulty": "medium",
    },
    {
        "website": "https://www.amc.seoul.kr",
        "task_description": "서울아산병원 웹사이트에서 건강검진 프로그램 안내 페이지를 열어, 기본 건강검진 비용과 포함 항목을 확인하라.",
        "reference_length": 8,
        "domain": "Health & Medical",
        "difficulty": "medium",
    },
    {
        "website": "https://www.samsunghospital.com",
        "task_description": "삼성서울병원 웹사이트에서 오늘 진료 가능한 진료과 목록을 확인하고, 그중 정형외과 예약 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Health & Medical",
        "difficulty": "medium",
    },
    {
        "website": "https://www.naver.com",
        "task_description": "네이버 건강에서 부산광역시 소재 치과 의원 중 야간 진료 가능한 의원을 검색하고, 검색 결과의 첫 번째 의원 상세 정보 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Health & Medical",
        "difficulty": "medium",
    },

    # ====================================================================
    # Food & Recipes (식품/레시피)
    # ====================================================================
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '김치찌개' 레시피를 검색하고, 검색 결과 중 조회수가 가장 높은 레시피의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Food & Recipes",
        "difficulty": "easy",
    },
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '돈까스' 레시피를 검색하고, 검색 결과 중 3인분 이상 기준의 레시피 중 별점이 가장 높은 레시피의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Food & Recipes",
        "difficulty": "medium",
    },
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '된장찌개' 레시피를 검색하고, 검색 결과 중 조리시간 30분 이하 레시피의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Food & Recipes",
        "difficulty": "medium",
    },
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '제육볶음' 레시피를 검색하고, 그중 재료가 5개 이하인 간단 레시피의 상세 페이지를 열어 조리 단계를 확인하라.",
        "reference_length": 8,
        "domain": "Food & Recipes",
        "difficulty": "medium",
    },
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '차돌박이'를 활용한 레시피를 검색하고, 검색 결과 중 별점 4점 이상인 레시피의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Food & Recipes",
        "difficulty": "easy",
    },
    {
        "website": "https://www.10000recipe.com",
        "task_description": "만개의 레시피에서 '비건' 태그가 달린 레시피를 검색하고, 검색 결과 중 최근 1개월 이내에 등록된 레시피의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Food & Recipes",
        "difficulty": "medium",
    },

    # ====================================================================
    # Entertainment & Media (엔터테인먼트/미디어)
    # ====================================================================
    {
        "website": "https://movie.naver.com",
        "task_description": "네이버 영화에서 현재 박스오피스 1위 영화의 상세 정보 페이지를 열어, 영화 줄거리와 평점을 확인하라.",
        "reference_length": 5,
        "domain": "Entertainment & Media",
        "difficulty": "easy",
    },
    {
        "website": "https://movie.naver.com",
        "task_description": "네이버 영화에서 현재 예매율 순위 상위 5개 영화 목록을 확인하고, 그중 예매율 1위 영화의 네티즌 평점과 관람객 리뷰 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
    },
    {
        "website": "https://comic.naver.com",
        "task_description": "네이버 웹툰에서 이번 주 요일별 웹툰 중 월요일 연재작 중 조회수가 가장 높은 웹툰의 첫 화 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
    },
    {
        "website": "https://comic.naver.com",
        "task_description": "네이버 웹툰에서 '일진'이라는 제목의 웹툰을 검색하고, 그 웹툰의 최신 회차 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Entertainment & Media",
        "difficulty": "easy",
    },
    {
        "website": "https://movie.naver.com",
        "task_description": "네이버 영화에서 장르별 랭킹 페이지에서 '스릴러' 장르 1위 영화의 상세 페이지를 열어, 감독과 출연진을 확인하라.",
        "reference_length": 8,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
    },
    {
        "website": "https://comic.naver.com",
        "task_description": "네이버 웹툰에서 '화산귀환' 웹툰의 전체 회차 목록 페이지를 열어, 최신 3개 회차의 제목을 확인하라.",
        "reference_length": 6,
        "domain": "Entertainment & Media",
        "difficulty": "easy",
    },
    {
        "website": "https://movie.naver.com",
        "task_description": "네이버 영화에서 2024년 개봉한 한국 영화 중 평점 9점 이상인 영화 목록을 확인하고, 그중 첫 번째 영화의 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
    },

    # ====================================================================
    # Government & Services (정부/공공서비스)
    # ====================================================================
    {
        "website": "https://www.gov.kr",
        "task_description": "정부24에서 '주민등록등본' 발급 신청 페이지를 열어, 온라인 발급 절차의 첫 단계 화면을 확인하라.",
        "reference_length": 7,
        "domain": "Government & Services",
        "difficulty": "medium",
    },
    {
        "website": "https://www.gov.kr",
        "task_description": "정부24에서 '가족관계증명서' 발급 신청 페이지를 열어, 발급 수수료와 필요 서류를 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
    },
    {
        "website": "https://www.nts.go.kr",
        "task_description": "국세청 홈택스에서 종합소득세 신고 안내 페이지를 열어, 근로소득자 신고 기간과 필요 서류를 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
    },
    {
        "website": "https://www.epeople.go.kr",
        "task_description": "국민신문고에서 '미세먼지' 관련 민원 검색 결과를 확인하고, 최근 1개월 이내 접수된 민원 중 첫 번째의 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
    },
    {
        "website": "https://www.gov.kr",
        "task_description": "정부24에서 '운전면허증 진위확인' 서비스 페이지를 열어, 서비스 이용 방법을 확인하라.",
        "reference_length": 6,
        "domain": "Government & Services",
        "difficulty": "easy",
    },
    {
        "website": "https://www.nts.go.kr",
        "task_description": "국세청 홈택스에서 부가가치세 예정신고 안내 페이지를 열어, 신고 기한과 신고 방법을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
    },

    # ====================================================================
    # Technology (기술)
    # ====================================================================
    {
        "website": "https://www.samsung.com/sec",
        "task_description": "삼성전자 한국 웹사이트에서 갤럭시 S24 울트라 256GB 모델의 스펙 상세 페이지를 열어, 가격과 저장 용량을 확인하라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
    },
    {
        "website": "https://www.lge.co.kr",
        "task_description": "LG전자 웹사이트에서 OLED TV 65인치 모델 중 가장 저렴한 제품의 상세 스펙 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Technology",
        "difficulty": "medium",
    },
    {
        "website": "https://www.samsung.com/sec",
        "task_description": "삼성전자 한국 웹사이트에서 갤럭시 북4 Pro 14인치 모델의 상세 스펙 페이지를 열어, 최소 RAM과 저장 용량을 확인하라.",
        "reference_length": 8,
        "domain": "Technology",
        "difficulty": "medium",
    },
    {
        "website": "https://www.lge.co.kr",
        "task_description": "LG전자 웹사이트에서 울트라파인 스크린 27인치 모니터 중 4K 해상도 지원 모델의 상세 스펙 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Technology",
        "difficulty": "medium",
    },
    {
        "website": "https://www.samsung.com/sec",
        "task_description": "삼성전자 한국 웹사이트에서 갤럭시 워치6 44mm 블루투스 모델의 가격과 배터리 용량을 확인할 수 있는 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
    },

    # ====================================================================
    # Education (교육)
    # ====================================================================
    {
        "website": "https://www.credu.com",
        "task_description": "크레듀에서 '파이썬' 기초 강좌를 검색하고, 검색 결과 중 수강생 평점 4점 이상인 강좌의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 '머신러닝' 강의를 검색하고, 검색 결과 중 무료 강의 중 수강생이 가장 많은 강의의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 'Docker' 강의를 검색하고, 검색 결과 중 가격 5만원 이하인 강의 중 평점이 가장 높은 강의의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
    },
    {
        "website": "https://www.credu.com",
        "task_description": "크레듀에서 '데이터 분석' 강좌를 검색하고, 검색 결과 중 입문자용 강좌 중 수강 기간 4주 이하인 강좌의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 'Spring Boot' 강의를 검색하고, 검색 결과 중 최근 6개월 이내에 업데이트된 강의 중 평점 4.5 이상인 강의의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 'React' 태그가 달린 강의를 검색하고, 검색 결과 중 무료이면서 한국어 자막이 있는 강의의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Education",
        "difficulty": "medium",
    },

    # ====================================================================
    # Other (기타 한국 특화)
    # ====================================================================
    {
        "website": "https://search.naver.com/search.naver?query=날씨",
        "task_description": "네이버에서 서울특별시 오늘 날씨 정보를 검색하고, 현재 기온과 미세먼지 농도를 확인할 수 있는 페이지를 열어라.",
        "reference_length": 4,
        "domain": "Other",
        "difficulty": "easy",
    },
    {
        "website": "https://map.naver.com",
        "task_description": "네이버 지도에서 서울특별시 강남구 역삼동 주변 '카페'를 검색하고, 검색 결과 중 별점 4점 이상인 카페의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
    },
    {
        "website": "https://map.naver.com",
        "task_description": "네이버 지도에서 서울특별시 중구 명동 근처 '주차장'을 검색하고, 검색 결과 중 현재 이용 가능한 주차장의 첫 번째 상세 페이지(요금 정보 포함)를 열어라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
    },
    {
        "website": "https://terms.naver.com",
        "task_description": "네이버 사전에서 '인공지능' 백과사전 검색 결과를 확인하고, 그중 첫 번째 항목의 상세 페이지를 열어 정의를 확인하라.",
        "reference_length": 5,
        "domain": "Other",
        "difficulty": "easy",
    },
    {
        "website": "https://news.naver.com",
        "task_description": "네이버 뉴스에서 '부동산' 토픽의 최신 기사 목록을 확인하고, 가장 최신 기사의 상세 페이지를 열어라.",
        "reference_length": 5,
        "domain": "Other",
        "difficulty": "easy",
    },
    {
        "website": "https://news.naver.com",
        "task_description": "네이버 뉴스에서 IT/과학 섹션의 헤드라인 기사 중 최근 24시간 이내에 게시된 기사의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Other",
        "difficulty": "easy",
    },
    {
        "website": "https://map.naver.com",
        "task_description": "네이버 지도에서 부산광역시 해운대구 해운대 해수욕장 주변 '식당'을 검색하고, 검색 결과 중 현재 영업 중인 식당 중 별점이 가장 높은 식당의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
    },
    {
        "website": "https://search.naver.com",
        "task_description": "네이버에서 '다이어트 운동'을 검색하고, 검색 결과의 뷰 섹션에서 최근 1주일 이내에 작성된 블로그 포스트 중 첫 번째의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Other",
        "difficulty": "easy",
    },
]