# 네이버 스마트 스토어 매크로
> 네이버 스마트 스토어 상품을 자동으로 구매해주는 매크로입니다.

품절상품 링크를 입력하면 자동으로 재고 검사 후 재고가 생기면 자동으로 상품을 구매합니다.

## 사용 방법
1. `https://github.com/OneTop4458/smartstore-macro/releases`
> 최신 릴리즈 실행파일을 다운로드 합니다.
2. `압축 해제`
3. `Chrome 다운로드` (이미 시스템에 Chrome 설치 되어 있다면 무시)
4. `https://www.base64encode.org 에서 자신의 네이버 아이디, 비밀번호 Base64 인코딩`
5. `config.json 파일에 Base64로 인코딩된 자신의 네이버 아이디, 비밀번호 입력`
> ※ 네이버 2단계 로그인 설정 시 매크로 사용 불가
6. `매크로 실행`
> SMARTSTORE-MACRO.exe --target 매크로를 돌릴 사이트 주소 [--time 페이지 새고 고침 시간] [--count 매크로 동작 횟수] [--option1 옵션선택] [--option2 옵션선택] [--option3 옵션선택]

## 직접 빌드 하기
[README](README) 파일을 참고 합니다.

### 주의 사항
3. 네이버 2단계 로그인 설정시 매크로 사용 불가

## 기여하기
버그 등이 발생하면 이슈로 등록해 주시거나, 문제가 되는 부분을 수정하신 후 PR해 주시면 감사하겠습니다.

## 라이선스
이 매크로는 [MIT 라이선스](https://github.com/OneTop4458/smartstore-macro/blob/master/LICENSE)를 적용받습니다.

