# WebClaw Patches for Online-Mind2Web KR Benchmark

WebClaw의 roadmap에 있는 `[SCREENSHOT]` 기능과 KR 사이트 최적화를 위한 추가 마커를 구현하는 패치들입니다.

## 패치 1: [SCREENSHOT] 마커 추가

Online-Mind2Web 평가는 각 스텝별 스크린샷이 필수입니다. WebClaw의 core.js에 `[SCREENSHOT]` 마커를 추가하고 background.js에서 `chrome.tabs.captureVisibleTab` API를 호출합니다.

### core.js 패치

`runTask` 함수의 marker 분기에 다음을 추가:

```javascript
      // [SCREENSHOT] — capture the target tab's visible viewport.
      // Returns a data: URL (PNG) capped at CAP bytes.
      // WebClaw roadmap item, implemented here for Online-Mind2Web.
      if (name === "SCREENSHOT" && hooks.screenshot) {
        return await hooks.screenshot(urlMatch);
      }
```

### background.js 패치

hooks 객체에 screenshot 함수 추가:

```javascript
screenshot: async (urlMatch) => {
  const tab = await findTargetTab(urlMatch);
  if (!tab) return "[screenshot] no target tab";
  const dataUrl = await new Promise((resolve) => {
    chrome.tabs.captureVisibleTab(tab.windowId, { format: "png" }, resolve);
  });
  return dataUrl || "[screenshot] capture failed";
},
```

## 패치 2: [SCROLL] 마커 추가

원본 Online-Mind2Web action dictionary에 SCROLL이 있지만 WebClaw에 없습니다:

```javascript
      // [SCROLL] <direction> <amount> — scroll the page or a container.
      if (name === "SCROLL" && hooks.act) {
        return await hooks.act({ action: "scroll", value: rest.trim(), urlMatch });
      }
```

background.js:

```javascript
if (msg.action === "scroll") {
  const [direction, amount] = (msg.value || "down 400").split(/\s+/);
  await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: (dir, amt) => {
      const dy = dir === "up" ? -parseInt(amt) : parseInt(amt);
      window.scrollBy(0, dy);
    },
    args: [direction, amount],
  });
  return "scrolled";
}
```

## 패치 3: [WAIT_SEL] 마커 — SPA 준비 대기

한국 사이트들(네이버, 쿠팡, 직방 등)은 SPA가 많아 DOM 업데이트 대기가 필요합니다:

```javascript
      // [WAIT_SEL] <css> — wait for a selector to appear (SPA readiness).
      if (name === "WAIT_SEL" && hooks.act) {
        return await hooks.act({ action: "wait_sel", selector: rest.trim(), urlMatch });
      }
```

background.js:

```javascript
if (msg.action === "wait_sel") {
  const timeout = 10000;
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const [result] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: (sel) => !!document.querySelector(sel),
      args: [msg.selector],
    });
    if (result.result) return "ready";
    await new Promise(r => setTimeout(r, 200));
  }
  return "[wait_sel] timeout";
}
```

## 패치 적용 방법

1. WebClaw 저장소 클론: `git clone https://github.com/DureClaw/webclaw`
2. 위 패치들을 core.js와 background.js에 적용
3. Chrome 확장 프로그램 새로고침
4. 이 저장소의 `script/run_webclaw_kr.py`로 태스크 실행

## WebClaw 도구 → 한국 사이트 최적 매핑

| 한국 사이트 특성 | WebClaw 도구 | 이유 |
|---|---|---|
| React 기반 모달/드롭다운 (네이버, 쿠팡) | `[CLICKTEXT]` | CSS 셀렉터 없이 텍스트로 클릭 |
| SPA 동적 렌더링 (직방, 다방) | `[WAIT_SEL]` + `[DOM]` | 렌더링 대기 후 DOM 확인 |
| 로그인 필요 (쿠팡, SSG) | `[TABS]` + `@<url>` | 로그인된 탭 타겟팅 |
| CORS 제한 (금융 API) | `[FETCH]` | 확장 프로그램 권한으로 우회 |
| 검색 결과 확인 | `[SNAP]` → `[DIFF]` | 액션 전후 DOM 변화로 성공 판정 |
| 폼 제출 (정부24, 홈택스) | `[FILL]` + `[SUBMIT]` | 실제 폼 입력 및 제출 |
| 스크린샷 (평가용) | `[SCREENSHOT]` | 매 스텝 캡처하여 trajectory 생성 |
| 복잡한 페이지 조작 | `[JS]` | 직접 JS 실행으로 한계 돌파 |