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

    # ====================================================================
    # Baryon Desktop 꾸러미 매핑 — 추가 업무 영역
    # (https://desktop.baryon.ai/packages.html)
    # 아래는 기존 12개 도메인에 없던 Baryon 꾸러미 업무들을
    # 실제 한국 웹사이트에서 수행할 수 있는 태스크로 정의한 것.
    # domain 필드는 원본 12개 분류 중 가장 가까운 것을 사용하되,
    # baryon_bundle 필드로 원본 꾸러미 slug를 추적한다.
    # ====================================================================

    # --- 법무 (legal) ---
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '주택임대차보호법'을 검색하여, 제8조(임대차기간)의 조문 본문을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '근로기준법'을 검색하여, 최근 개정일과 개정 이유를 확인할 수 있는 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '전자상거래법' 시행령 중 제20조의 조문과 관련 판례 목록을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Government & Services",
        "difficulty": "hard",
        "baryon_bundle": "legal",
    },

    # --- 세무 (tax) ---
    {
        "website": "https://www.nts.go.kr",
        "task_description": "국세청 홈택스에서 부가가치세 일반과세자 신고 기한과 납부 방법 안내 페이지를 열어, 신고서 작성 시 필요 항목을 확인하라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },
    {
        "website": "https://www.hometax.go.kr",
        "task_description": "홈택스에서 연말정산 간소화 서비스 페이지를 열어, 근로소득자가 조회할 수 있는 소득공제 항목 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },
    {
        "website": "https://www.nts.go.kr",
        "task_description": "국세청 홈택스에서 세금계산서 진위확인 서비스 페이지를 열어, 확인 절차의 첫 단계 입력 항목을 확인하라.",
        "reference_length": 7,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },

    # --- 재무 (finance) ---
    {
        "website": "https://www.bok.or.kr",
        "task_description": "한국은행 경제통계시스템에서 최근 1년간 소비자물가상승률(CPI) 월별 데이터 조회 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Finance & Investment",
        "difficulty": "medium",
        "baryon_bundle": "finance",
    },
    {
        "website": "https://www.fss.or.kr",
        "task_description": "금융감독원 웹사이트에서 '예금자보호법' 안내 페이지를 열어, 보호한도와 보호대상 예금의 종류를 확인하라.",
        "reference_length": 8,
        "domain": "Finance & Investment",
        "difficulty": "medium",
        "baryon_bundle": "finance",
    },
    {
        "website": "https://www.bok.or.kr",
        "task_description": "한국은행 경제통계시스템에서 최근 분기 GDP 성장률(전기대비) 데이터를 조회할 수 있는 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Finance & Investment",
        "difficulty": "hard",
        "baryon_bundle": "finance",
    },

    # --- 영업 / CRM (sales) ---
    {
        "website": "https://crm.withncorp.com",
        "task_description": "영업관리 CRM에서 '보고서' 메뉴를 열어, 최근 1주일 이내에 작성된 영업활동 보고서 목록을 확인하라.",
        "reference_length": 7,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "sales",
    },
    {
        "website": "https://www.mangoplate.com",
        "task_description": "망고플레이트에서 서울특별시 강남구 삼성동 근처 식당 중 평점 4점 이상인 식당의 첫 번째 상세 페이지를 열어, 리뷰와 영업시간을 확인하라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "sales",
    },

    # --- 마케팅 (marketing) ---
    {
        "website": "https://ads.google.com",
        "task_description": "Google Ads에서 새 캠페인 만들기 페이지를 열어, 검색 광고 캠페인의 첫 설정 단계(목표 선택) 화면을 확인하라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://business.facebook.com",
        "task_description": "Meta Business Suite에서 인스타그램 계정의 최근 7일간 도달 수와 참여 수를 확인할 수 있는 인사이트 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://www.nihcm.go.kr",
        "task_description": "국립보건연구원 웹사이트에서 보건의료 데이터 통계 조회 페이지를 열어, 최근 연도별 건강검진 수검률 데이터를 확인하라.",
        "reference_length": 10,
        "domain": "Health & Medical",
        "difficulty": "hard",
        "baryon_bundle": "marketing",
    },

    # --- 고객지원 / CS (support) ---
    {
        "website": "https://www.kt.com",
        "task_description": "KT 고객지원 페이지에서 인터넷 장애 신고 접수 페이지를 열어, 장애 신고 시 입력해야 할 필수 항목을 확인하라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "support",
    },
    {
        "website": "https://www.skt.com",
        "task_description": "SKT 고객지원 페이지에서 휴대폰 요금제 변경 안내 페이지를 열어, 현재 가장 저렴한 5G 요금제의 월정액을 확인하라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "support",
    },
    {
        "website": "https://help.naver.com",
        "task_description": "네이버 고객센터에서 '아이디 찾기' 관련 도움말 페이지를 열어, 아이디 찾기 절차의 첫 단계를 확인하라.",
        "reference_length": 6,
        "domain": "Other",
        "difficulty": "easy",
        "baryon_bundle": "support",
    },

    # --- 이커머스 운영 (ecommerce) ---
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '스마트워치'를 검색하고, 검색 결과 중 로켓배송 가능한 상품 중 가격 5만원 이하, 별점 4점 이상인 상품의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://sell.smartstore.naver.com",
        "task_description": "네이버 스마트스토어 판매자 센터에서 '상품 등록' 페이지를 열어, 상품 등록 시 필수 입력 항목 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '아기 기저귀'를 검색하고, 검색 결과 중 정기배송 가능한 상품 중 가장 저렴한 상품을 장바구니에 추가하라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://browse.gmarket.co.kr",
        "task_description": "G마케이트에서 '가습기'를 검색하고, 검색 결과 중 무료배송 상품 중 가격이 3만원 이하이고 스티치 등급이 높은 상품의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },

    # --- 물류 / 유통 (logistics) ---
    {
        "website": "https://www.cjlogistics.com",
        "task_description": "CJ대한통운 웹사이트에서 운송장 조회 페이지를 열어, 운송장 번호 입력 필드와 배송 추적 절차를 확인하라.",
        "reference_length": 6,
        "domain": "Travel & Transportation",
        "difficulty": "easy",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.cjlogistics.com",
        "task_description": "CJ대한통운 웹사이트에서 택배 요금 계산 페이지를 열어, 서울에서 부산까지 3kg 소포의 배송 요금을 조회하는 화면을 확인하라.",
        "reference_length": 8,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.lottelogistics.com",
        "task_description": "롯데글로벌로지스틱스 웹사이트에서 화물 추적 서비스 페이지를 열어, 화물 추적 시 필요한 입력 항목을 확인하라.",
        "reference_length": 7,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },

    # --- 번역 / 현지화 (translation) ---
    {
        "website": "https://dict.naver.com",
        "task_description": "네이버 사전에서 'artificial intelligence'를 영한 사전으로 검색하고, 첫 번째 검색 결과의 상세 정의와 예문 페이지를 열어라.",
        "reference_length": 5,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },
    {
        "website": "https://dict.naver.com",
        "task_description": "네이버 사전에서 '미안하다'를 한영 사전으로 검색하고, 검색 결과 중 가장 많은 추천을 받은 번역 예문의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },
    {
        "website": "https://terms.naver.com",
        "task_description": "네이버 용어사전에서 '블록체인'을 검색하고, IT/컴퓨터 분야 사전 중 첫 번째 항목의 상세 정의 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },

    # --- 제품기획 (product) ---
    {
        "website": "https://www.betterworks.com",
        "task_description": "BetterWorks 웹사이트에서 OKR(목표 및 핵심결과) 관리 제품의 기능 소개 페이지를 열어, 핵심 기능 3가지를 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "product",
    },
    {
        "website": "https://www.figma.com",
        "task_description": "Figma 웹사이트에서 '디자인 시스템' 템플릿 갤러리 페이지를 열어, 가장 인기 있는 무료 UI 킷의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "product",
    },

    # --- 연구 (research) ---
    {
        "website": "https://www.riss.kr",
        "task_description": "RISS(학술연구정보서비스)에서 '대형언어모델'을 검색하고, 최근 2년 이내에 출간된 학위논문 중 첫 번째 논문의 상세 정보 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.riss.kr",
        "task_description": "RISS에서 '부동산 가격 예측'을 검색하고, 검색 결과 중 학술논문 탭의 첫 번째 논문 상세 페이지를 열어, 초록과 저자 정보를 확인하라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.dbpia.co.kr",
        "task_description": "DBpia에서 '강화학습'을 검색하고, 검색 결과 중 최근 1년 이내에 등록된 논문 중 첫 번째 논문의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.scienceon.kr",
        "task_description": "ScienceON에서 '탄소중립'을 검색하고, 검색 결과 중 연구보고서 탭의 첫 번째 항목 상세 페이지를 열어, 연구기관과 발행일을 확인하라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },

    # --- 인사 / HR (hr) ---
    {
        "website": "https://www.saramin.co.kr",
        "task_description": "사람인에서 '인사담당자' 직무 채용 공고를 검색하고, 검색 결과 중 서울 근무, 경력 5년 이상 조건으로 필터링한 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "hr",
    },
    {
        "website": "https://www.jobkorea.co.kr",
        "task_description": "잡코리아에서 '인사팀' 직무 채용 공고 중 대기업, 경력 3년 이상 조건으로 검색하고, 검색 결과의 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Jobs & Careers",
        "difficulty": "hard",
        "baryon_bundle": "hr",
    },

    # --- 디자인 (design) ---
    {
        "website": "https://www.behance.net",
        "task_description": "Behance에서 '모바일 앱 UI'를 검색하고, 검색 결과 중 최근 1개월 이내에 게시된 프로젝트 중 가장 추천수가 많은 프로젝트의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
        "baryon_bundle": "design",
    },
    {
        "website": "https://www.figma.com",
        "task_description": "Figma 커뮤니티에서 '아이콘 세트'를 검색하고, 검색 결과 중 무료 다운로드 가능한 파일 중 가장 인기 있는(복제수 많은) 파일의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "design",
    },
    {
        "website": "https://www.unsplash.com",
        "task_description": "Unsplash에서 '서울 도시'를 검색하고, 검색 결과 중 가장 다운로드 수가 많은 사진의 상세 페이지를 열어, 작가 정보와 해상도를 확인하라.",
        "reference_length": 6,
        "domain": "Entertainment & Media",
        "difficulty": "easy",
        "baryon_bundle": "design",
    },

    # --- 데이터 분석 (data) ---
    {
        "website": "https://kosis.kr",
        "task_description": "국가통계포털(KOSIS)에서 '인구총조사' 메뉴를 열어, 최근 조사 기준 서울특별시 인구수 데이터 조회 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },
    {
        "website": "https://kosis.kr",
        "task_description": "국가통계포털(KOSIS)에서 '경제활동인구조사' 통계표 중 최근 분기 실업률 데이터 조회 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Government & Services",
        "difficulty": "hard",
        "baryon_bundle": "data",
    },
    {
        "website": "https://www.data.go.kr",
        "task_description": "공공데이터포털에서 '부동산 실거래가' 데이터셋을 검색하고, 검색 결과 중 가장 최근에 업데이트된 데이터셋의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },
    {
        "website": "https://www.data.go.kr",
        "task_description": "공공데이터포털에서 '대기오염' 키워드로 API를 검색하고, 검색 결과 중 조회수가 가장 높은 API의 상세 페이지를 열어, 제공 기관을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },

    # --- 학생 (student) ---
    {
        "website": "https://www.acmicpc.net",
        "task_description": "백준 온라인 저지에서 'DP' 태그가 달린 문제 중 난이도 골드 1인 문제 중 가장 정답 수가 많은 문제의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.acmicpc.net",
        "task_description": "백준 온라인 저지에서 '그래프 탐색' 태그가 달린 문제 중 난이도 실버 2 이하인 문제의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 '코딩테스트' 강의를 검색하고, 검색 결과 중 무료 강의 중 평점 4.5 이상인 강의의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "student",
    },

    # --- 교육 / 이러닝 (education) ---
    {
        "website": "https://www.kmooc.kr",
        "task_description": "K-MOOC에서 '인공지능' 강좌를 검색하고, 검색 결과 중 현재 수강 신청 가능한 강좌의 첫 번째 상세 페이지를 열어, 강의 개요를 확인하라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },
    {
        "website": "https://www.kmooc.kr",
        "task_description": "K-MOOC에서 '데이터 과학' 강좌를 검색하고, 검색 결과 중 자막이 한국어인 강좌 중 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },

    # --- 운영자 (operator) ---
    {
        "website": "https://www.amazonaws.com",
        "task_description": "AWS 웹사이트에서 EC2 요금 페이지를 열어, 서울 리전의 t3.medium 인스턴스 온디맨드 시간당 요금을 확인하라.",
        "reference_length": 8,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.cloudflare.com",
        "task_description": "Cloudflare 웹사이트에서 'Pages' 제품의 기능 소개 페이지를 열어, 무료 플랜에서 제공되는 기능 목록을 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.vercel.com",
        "task_description": "Vercel 웹사이트에서 요금제 페이지를 열어, Pro 플랜의 월별 가격과 포함된 대역폭 한도를 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "operator",
    },

    # ====================================================================
    # 꾸러미별 사이트 다양화 — 2차 추가
    # 각 baryon_bundle에 새로운 한국 사이트를 추가하여 사이트 다양성 확대
    # ====================================================================

    # --- 법무 (legal) 추가 사이트 ---
    {
        "website": "https://www.court.go.kr",
        "task_description": "대법원 종합법률정보에서 '가사소송법'을 검색하고, 검색 결과 중 현행 법률의 조문 목록 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.court.go.kr",
        "task_description": "대법원 웹사이트에서 판례 검색 페이지를 열어, '부동산 임대차' 키워드로 최근 1년 이내 확정 판례 중 첫 번째 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.klri.re.kr",
        "task_description": "한국법제연구원 웹사이트에서 '전자문서법'을 검색하고, 검색 결과 중 현행 법령의 상세 페이지를 열어, 최근 개정 내용을 확인하라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '개인정보보호법'을 검색하여, 제15조(개인정보의 수집·이용)의 조문 본문과 관련 부령을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "legal",
    },
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '상법' 중 회사편 주식회사의 이사회 규정이 포함된 조문 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Government & Services",
        "difficulty": "hard",
        "baryon_bundle": "legal",
    },

    # --- 세무 (tax) 추가 사이트 ---
    {
        "website": "https://www.hometax.go.kr",
        "task_description": "홈택스에서 '종합소득세' 신고 페이지를 열어, 프리랜서/사업소득자 신고 시 필요한 필수 입력 항목을 확인하라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },
    {
        "website": "https://www.hometax.go.kr",
        "task_description": "홈택스에서 '지방세' 안내 페이지를 열어, 취득세율과 납부 기한을 확인할 수 있는 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },
    {
        "website": "https://www.nts.go.kr",
        "task_description": "국세청 웹사이트에서 '세금 납부' 안내 페이지를 열어, 근로소득 세액공제 항목 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },
    {
        "website": "https://www.elinf.co.kr",
        "task_description": "전자세금계산서 포털(e신고인포)에서 세금계산서 발급 안내 페이지를 열어, 전자세금계산서 발급 절차를 확인하라.",
        "reference_length": 7,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "tax",
    },

    # --- 재무 (finance) 추가 사이트 ---
    {
        "website": "https://www.fss.or.kr",
        "task_description": "금융감독원 웹사이트에서 '금융사고 피해구제' 안내 페이지를 열어, 피해구제 신청 절차와 필요 서류를 확인하라.",
        "reference_length": 8,
        "domain": "Finance & Investment",
        "difficulty": "medium",
        "baryon_bundle": "finance",
    },
    {
        "website": "https://www.bok.or.kr",
        "task_description": "한국은행 경제통계시스템에서 '가계부채' 관련 통계 중 최근 분기 가계대출잔액 데이터 조회 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Finance & Investment",
        "difficulty": "hard",
        "baryon_bundle": "finance",
    },
    {
        "website": "https://fsc.go.kr",
        "task_description": "금융위원회 웹사이트에서 '디지털 금융' 관련 최근 보도자료 중 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Finance & Investment",
        "difficulty": "medium",
        "baryon_bundle": "finance",
    },
    {
        "website": "https://www.kidi.or.kr",
        "task_description": "보험개발원 웹사이트에서 '자동차보험료 산출' 안내 페이지를 열어, 보험료 산정 기준을 확인하라.",
        "reference_length": 8,
        "domain": "Finance & Investment",
        "difficulty": "medium",
        "baryon_bundle": "finance",
    },

    # --- 영업 / CRM (sales) 추가 사이트 ---
    {
        "website": "https://www.mangoplate.com",
        "task_description": "망고플레이트에서 서울특별시 마포구 홍대 근처 '카페'를 검색하고, 검색 결과 중 평점 4점 이상인 카페의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "sales",
    },
    {
        "website": "https://www.tripadvisor.co.kr",
        "task_description": "트립어드바이저에서 제주특별자치도 제주시 '관광명소'를 검색하고, 검색 결과 중 평점 4.5점 이상인 명소의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "sales",
    },
    {
        "website": "https://www.tripadvisor.co.kr",
        "task_description": "트립어드바이저에서 서울 '호텔' 중 5성급 호텔의 리뷰 중 가장 추천수가 많은 리뷰의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "sales",
    },
    {
        "website": "https://www.kyobobook.co.kr",
        "task_description": "교보문고 웹사이트에서 '영업' 관련 도서를 검색하고, 검색 결과 중 베스트셀러 순위 1위 도서의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Shopping & E-Commerce",
        "difficulty": "easy",
        "baryon_bundle": "sales",
    },

    # --- 마케팅 (marketing) 추가 사이트 ---
    {
        "website": "https://ads.google.com",
        "task_description": "Google Ads 키워드 플래너 페이지를 열어, '온라인 쇼핑' 키워드의 월간 검색량과 경쟁 강도를 확인하라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://business.facebook.com",
        "task_description": "Meta Business Suite에서 '광고 만들기' 페이지를 열어, 인스타그램 피드 광고의 첫 설정 단계를 확인하라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://www.naver.com",
        "task_description": "네이버广告(넥서치 광고) 웹사이트에서 '검색광고' 상품 소개 페이지를 열어, 광고 타겟팅 옵션을 확인하라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://www.tistory.com",
        "task_description": "티스토리 블로그 플랫폼에서 '마케팅' 태그가 달린 인기 포스트 중 최근 7일 이내에 작성된 첫 번째 포스트의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },
    {
        "website": "https://www.branod.com",
        "task_description": "브랜드보드 웹사이트에서 '인플루언서 마케팅' 캠페인 목록 중 최근 등록된 캠페인의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "marketing",
    },

    # --- 고객지원 / CS (support) 추가 사이트 ---
    {
        "website": "https://www.lguplus.com",
        "task_description": "LG유플러스 고객지원 페이지에서 '요금제 변경' 안내 페이지를 열어, 5G 프리미엄 요금제의 월정액과 포함 데이터를 확인하라.",
        "reference_length": 8,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "support",
    },
    {
        "website": "https://www.kt.com",
        "task_description": "KT 고객지원 페이지에서 '인터넷 속도 테스트' 서비스 페이지를 열어, 현재 다운로드/업로드 속도 측정 화면을 확인하라.",
        "reference_length": 6,
        "domain": "Other",
        "difficulty": "easy",
        "baryon_bundle": "support",
    },
    {
        "website": "https://www.skt.com",
        "task_description": "SKT 고객지원 페이지에서 '휴대폰 분실 신고' 안내 페이지를 열어, 분실 신고 절차의 첫 단계를 확인하라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "support",
    },
    {
        "website": "https://help.toss.im",
        "task_description": "토스 고객지원 페이지에서 '송금 취소' 관련 도움말 페이지를 열어, 송금 취소 조건과 절차를 확인하라.",
        "reference_length": 6,
        "domain": "Other",
        "difficulty": "easy",
        "baryon_bundle": "support",
    },
    {
        "website": "https://help.coupang.com",
        "task_description": "쿠팡 고객센터에서 '반품 신청' 안내 페이지를 열어, 반품 절차와 반품 가능 기간을 확인하라.",
        "reference_length": 7,
        "domain": "Other",
        "difficulty": "medium",
        "baryon_bundle": "support",
    },

    # --- 이커머스 운영 (ecommerce) 추가 사이트 ---
    {
        "website": "https://sell.smartstore.naver.com",
        "task_description": "네이버 스마트스토어 판매자 센터에서 '주문 관리' 페이지를 열어, 최근 7일 이내 결제 완료된 주문 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://www.coupang.com",
        "task_description": "쿠팡에서 '스마트플러스 스토어' 입점 안내 페이지를 열어, 입점 자격 요건을 확인하라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://selling.kakao.com",
        "task_description": "카카오스타일(선물하기/쇼핑하기) 판매자 센터에서 '상품 등록 가이드' 페이지를 열어, 필수 입력 항목을 확인하라.",
        "reference_length": 8,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://admin.shopify.com",
        "task_description": "Shopify 관리자 도움말에서 '결제 설정' 안내 페이지를 열어, 한국 결제 게이트웨이 연동 방법을 확인하라.",
        "reference_length": 9,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },
    {
        "website": "https://www.11st.co.kr",
        "task_description": "11번가에서 '판매자 입점' 안내 페이지를 열어, 입점 절차와 수수료율을 확인하라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "ecommerce",
    },

    # --- 물류 / 유통 (logistics) 추가 사이트 ---
    {
        "website": "https://www.cjlogistics.com",
        "task_description": "CJ대한통운 웹사이트에서 '물류센터 위치' 검색 페이지를 열어, 경기도 김포시 소재 물류센터 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.klogistics.com",
        "task_description": "한진웹사이트에서 운송장 조회 페이지를 열어, 운송장 번호 입력 필드를 확인하고 배송 추적 화면을 열어라.",
        "reference_length": 7,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.epost.go.kr",
        "task_description": "우체국 웹사이트에서 '국제 우편 요금' 조회 페이지를 열어, 한국에서 미국까지 1kg 소포의 요금을 확인하라.",
        "reference_length": 9,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.epost.go.kr",
        "task_description": "우체국 웹사이트에서 '우편물 추적' 서비스 페이지를 열어, 추적 시 필요한 입력 항목을 확인하라.",
        "reference_length": 6,
        "domain": "Travel & Transportation",
        "difficulty": "easy",
        "baryon_bundle": "logistics",
    },
    {
        "website": "https://www.lottelogistics.com",
        "task_description": "롯데글로벌로지스틱스 웹사이트에서 '배송 예정 시간 조회' 페이지를 열어, 도착 예정 시간 확인 절차를 확인하라.",
        "reference_length": 7,
        "domain": "Travel & Transportation",
        "difficulty": "medium",
        "baryon_bundle": "logistics",
    },

    # --- 번역 / 현지화 (translation) 추가 사이트 ---
    {
        "website": "https://dict.naver.com",
        "task_description": "네이버 사전에서 '한자 사전'을 열어, '愛'의 음과 뜻, 관련 단어를 확인할 수 있는 상세 페이지를 열어라.",
        "reference_length": 5,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },
    {
        "website": "https://dict.daum.net",
        "task_description": "다음 사전에서 '일본어 사전'을 열어, 'ありがとう'의 번역과 예문 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },
    {
        "website": "https://dict.daum.net",
        "task_description": "다음 사전에서 '중국어 사전'을 열어, '你好'의 병음과 번역, 예문이 포함된 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "translation",
    },
    {
        "website": "https://terms.naver.com",
        "task_description": "네이버 용어사전에서 '클라우드 컴퓨팅'을 검색하고, IT/컴퓨터 분야 사전 중 가장 추천수가 많은 항목의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "translation",
    },

    # --- 제품기획 (product) 추가 사이트 ---
    {
        "website": "https://www.figma.com",
        "task_description": "Figma 커뮤니티에서 '와이어프레임 킷'을 검색하고, 검색 결과 중 무료 파일 중 가장 인기 있는 파일의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "product",
    },
    {
        "website": "https://www.notion.so",
        "task_description": "Notion 웹사이트에서 '제품 로드맵 템플릿' 페이지를 열어, 무료 템플릿의 기능과 구성을 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "product",
    },
    {
        "website": "https://www.atlassian.com",
        "task_description": "Atlassian(Jira) 웹사이트에서 '스프린트 플래닝' 기능 소개 페이지를 열어, Agile 스프린트 계획 기능을 확인하라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "product",
    },
    {
        "website": "https://www.producthunt.com",
        "task_description": "Product Hunt에서 'AI 도구' 카테고리의 오늘의 1위 프로덕트 상세 페이지를 열어, 기능과 평점을 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "product",
    },

    # --- 연구 (research) 추가 사이트 ---
    {
        "website": "https://www.riss.kr",
        "task_description": "RISS에서 '자율주행'을 검색하고, 검색 결과 중 학술지 논문 탭의 첫 번째 논문 상세 페이지를 열어, DOI와 인용 수를 확인하라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.dbpia.co.kr",
        "task_description": "DBpia에서 '자연어 처리'를 검색하고, 검색 결과 중 최근 6개월 이내에 등록된 논문 중 가장 다운로드 수가 많은 논문의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.scienceon.kr",
        "task_description": "ScienceON에서 '양자컴퓨팅'을 검색하고, 검색 결과 중 특허 탭의 첫 번째 항목 상세 페이지를 열어, 출원인과 출원일을 확인하라.",
        "reference_length": 9,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://arxiv.org",
        "task_description": "arXiv에서 'large language model'을 검색하고, 검색 결과 중 최근 1개월 이내에 게시된 논문 중 첫 번째 논문의 abstract 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },
    {
        "website": "https://www.kci.go.kr",
        "task_description": "한국학술지인용색인(KCI)에서 '디지털 마케팅'을 검색하고, 검색 결과 중 등재지 논문의 첫 번째 상세 페이지를 열어, 피인용수를 확인하라.",
        "reference_length": 9,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "research",
    },

    # --- 인사 / HR (hr) 추가 사이트 ---
    {
        "website": "https://www.saramin.co.kr",
        "task_description": "사람인에서 'HRD 담당자' 직무 채용 공고를 검색하고, 검색 결과 중 경력 3년 이상, 서울 근무 조건으로 필터링한 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "hr",
    },
    {
        "website": "https://www.wanted.co.kr",
        "task_description": "원티드에서 '인사팀' 직군 채용 공고 중 경력 5년 이상, 서울 근무 조건으로 검색하고, 검색 결과 중 첫 번째 공고의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "hr",
    },
    {
        "website": "https://www.jobkorea.co.kr",
        "task_description": "잡코리아에서 '인재 채용' 관련 컨설팅 서비스 안내 페이지를 열어, 서비스 내용과 요금을 확인하라.",
        "reference_length": 7,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "hr",
    },
    {
        "website": "https://www.indeed.com",
        "task_description": "Indeed에서 '채용 담당자' 직무 채용 공고를 검색하고, 검색 결과 중 서울 근무, 정규직 조건의 첫 번째 공고 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Jobs & Careers",
        "difficulty": "medium",
        "baryon_bundle": "hr",
    },

    # --- 디자인 (design) 추가 사이트 ---
    {
        "website": "https://dribbble.com",
        "task_description": "Dribbble에서 '모바일 앱 디자인'을 검색하고, 검색 결과 중 최근 1주일 이내에 게시된 작품 중 가장 조회수가 많은 작품의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Entertainment & Media",
        "difficulty": "medium",
        "baryon_bundle": "design",
    },
    {
        "website": "https://www.iconfinder.com",
        "task_description": "Iconfinder에서 '날씨 아이콘'을 검색하고, 검색 결과 중 무료 다운로드 가능한 아이콘 세트 중 가장 다운로드 수가 많은 세트의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "design",
    },
    {
        "website": "https://www.figma.com",
        "task_description": "Figma 커뮤니티에서 '타이포그래피'를 검색하고, 검색 결과 중 무료 파일 중 가장 추천수가 많은 파일의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "design",
    },
    {
        "website": "https://coolors.co",
        "task_description": "Coolors에서 '한국 전통 색상' 팔레트를 검색하고, 검색 결과 중 가장 인기 있는 팔레트의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Entertainment & Media",
        "difficulty": "easy",
        "baryon_bundle": "design",
    },

    # --- 데이터 분석 (data) 추가 사이트 ---
    {
        "website": "https://kosis.kr",
        "task_description": "국가통계포털(KOSIS)에서 '주택가격동향조사' 통계표 중 최근 분기 서울 아파트 가격 동향 데이터 조회 페이지를 열어라.",
        "reference_length": 10,
        "domain": "Government & Services",
        "difficulty": "hard",
        "baryon_bundle": "data",
    },
    {
        "website": "https://www.data.go.kr",
        "task_description": "공공데이터포털에서 '코로나19 확진자' 데이터셋을 검색하고, 검색 결과 중 가장 조회수가 높은 데이터셋의 상세 페이지를 열어, 제공 형식을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },
    {
        "website": "https://www.bigdata.go.kr",
        "task_description": "데이터포털 빅데이터 플랫폼에서 '소상공인' 관련 데이터셋을 검색하고, 검색 결과 중 첫 번째 데이터셋의 상세 페이지를 열어라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },
    {
        "website": "https://www.index.go.kr",
        "task_description": "국가지표체계에서 '청년 실업률' 지표를 검색하고, 최근 5년간 연도별 청년 실업률 추이 데이터 조회 페이지를 열어라.",
        "reference_length": 9,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "data",
    },

    # --- 학생 (student) 추가 사이트 ---
    {
        "website": "https://www.acmicpc.net",
        "task_description": "백준 온라인 저지에서 '정렬' 태그가 달린 문제 중 난이도 브론즈 1인 문제 중 가장 정답 수가 많은 문제의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.programmers.co.kr",
        "task_description": "프로그래머스에서 '해시' 알고리즘 문제 중 Lv.1 난이도인 문제의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.programmers.co.kr",
        "task_description": "프로그래머스에서 'SQL' 문제 중 Lv.2 난이도인 문제의 첫 번째 상세 페이지를 열어, 문제 설명을 확인하라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.hackerrank.com",
        "task_description": "HackerRank에서 'Python' 트랙의 Basic Data Types 챌린지 중 첫 번째 문제의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Education",
        "difficulty": "easy",
        "baryon_bundle": "student",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 '알고리즘' 강의를 검색하고, 검색 결과 중 입문자용 무료 강의 중 평점이 가장 높은 강의의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "student",
    },

    # --- 교육 / 이러닝 (education) 추가 사이트 ---
    {
        "website": "https://www.kmooc.kr",
        "task_description": "K-MOOC에서 '경제학' 강좌를 검색하고, 검색 결과 중 무료 수강 가능한 강좌의 첫 번째 상세 페이지를 열어, 수강 기간을 확인하라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },
    {
        "website": "https://www.edwith.org",
        "task_description": "edwith(이듬)에서 '웹 프로그래밍' 강좌를 검색하고, 검색 결과 중 무료 강좌 중 가장 수강생이 많은 강좌의 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },
    {
        "website": "https://www.edwith.org",
        "task_description": "edwith에서 '데이터 분석' 강좌를 검색하고, 검색 결과 중 부스트코스 태그가 달린 강좌의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },
    {
        "website": "https://www.inflearn.com",
        "task_description": "인프런에서 'Spring Boot 입문' 강의를 검색하고, 검색 결과 중 무료 강의 중 평점 4.5 이상인 강의의 첫 번째 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Education",
        "difficulty": "medium",
        "baryon_bundle": "education",
    },

    # --- 운영자 (operator) 추가 사이트 ---
    {
        "website": "https://www.amazonaws.com",
        "task_description": "AWS 웹사이트에서 S3 요금 페이지를 열어, 서울 리전의 표준 스토리지 100GB 월별 요금을 확인하라.",
        "reference_length": 8,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.cloudflare.com",
        "task_description": "Cloudflare 웹사이트에서 'WAF' 제품의 기능 소개 페이지를 열어, 무료 플랜에서 지원하는 보안 규칙 수를 확인하라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.vercel.com",
        "task_description": "Vercel 웹사이트에서 'Edge Functions' 문서 페이지를 열어, 지원 리전 목록을 확인하라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.netlify.com",
        "task_description": "Netlify 웹사이트에서 요금제 페이지를 열어, Starter 플랜의 월별 대역폭 한도와 빌드 시간을 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "operator",
    },
    {
        "website": "https://www.docker.com",
        "task_description": "Docker 웹사이트에서 'Docker Hub' 요금제 페이지를 열어, Personal 플랜에서 제공하는 비공개 저장소 개수를 확인하라.",
        "reference_length": 7,
        "domain": "Technology",
        "difficulty": "medium",
        "baryon_bundle": "operator",
    },

    # --- 개발 (dev) — 새 꾸러미 ---
    {
        "website": "https://github.com",
        "task_description": "GitHub에서 'web-agent' 키워드로 퍼블릭 저장소를 검색하고, 검색 결과 중 가장 star 수가 많은 저장소의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },
    {
        "website": "https://github.com",
        "task_description": "GitHub에서 'DureClaw/webclaw' 저장소의 README 페이지를 열어, 최근 커밋 5개를 확인하라.",
        "reference_length": 5,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },
    {
        "website": "https://stackoverflow.com",
        "task_description": "Stack Overflow에서 'pandas dataframe merge'를 검색하고, 검색 결과 중 가장 추천수가 많은 질문의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },
    {
        "website": "https://www.npmjs.com",
        "task_description": "npm에서 'websocket' 패키지를 검색하고, 검색 결과 중 가장 주간 다운로드 수가 많은 패키지의 상세 페이지를 열어라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },
    {
        "website": "https://pypi.org",
        "task_description": "PyPI에서 'fastapi' 패키지의 상세 페이지를 열어, 최신 버전과 의존성을 확인하라.",
        "reference_length": 5,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },
    {
        "website": "https://docs.python.org",
        "task_description": "Python 공식 문서에서 'asyncio' 모듈 페이지를 열어, 비동기 I/O 관련 API 목록을 확인하라.",
        "reference_length": 6,
        "domain": "Technology",
        "difficulty": "easy",
        "baryon_bundle": "dev",
    },

    # --- 사내문서 분석 (docs) — 새 꾸러미 ---
    {
        "website": "https://www.law.go.kr",
        "task_description": "국가법령정보센터에서 '근로기준법' 전문을 열어, 제5장(임금)의 전체 조문 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "docs",
    },
    {
        "website": "https://www.kogl.or.kr",
        "task_description": "공공누리(KOGL) 웹사이트에서 '이용허락' 안내 페이지를 열어, 공공저작물 이용 조건을 확인하라.",
        "reference_length": 7,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "docs",
    },
    {
        "website": "https://www.archives.go.kr",
        "task_description": "국가기록원 웹사이트에서 '정부 기록물 검색' 페이지를 열어, '행정' 카테고리의 최근 등록 기록물 목록을 확인하라.",
        "reference_length": 8,
        "domain": "Government & Services",
        "difficulty": "medium",
        "baryon_bundle": "docs",
    },
    {
        "website": "https://www.kyobobook.co.kr",
        "task_description": "교보문고에서 '계약서 작성' 관련 도서를 검색하고, 검색 결과 중 베스트셀러 1위 도서의 목차를 확인할 수 있는 상세 페이지를 열어라.",
        "reference_length": 7,
        "domain": "Shopping & E-Commerce",
        "difficulty": "medium",
        "baryon_bundle": "docs",
    },
]