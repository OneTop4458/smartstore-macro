# 네이버 스마트 스토어 매크로
> 네이버 스마트 스토어 상품을 자동으로 구매해주는 매크로입니다.

품절상품 링크를 입력하면 자동으로 재고 검사 후 재고가 생기면 자동으로 상품을 구매합니다.

## 사용 방법
1. `git clone https://github.com/OneTop4458/smartstore-macro.git`
> 오른쪽 중반 Clone or download 버튼 클릭 > Download Zip을 클릭하여 다운로드 하는 방법도 가능합니다.
2. `압축 해제`
3. `python-3.8.0.exe 설치`
> ※ 설치 시 하단 Add Python 3.8 to PATH 체크
4. `Win + R 키 입력 후 CMD 입력`
5. `pip install selenium 입력`
6. `Chrome 다운로드`
7. `Chrome 실행 후 오른쪽 상단 ... 클릭>도움말(E)>Chrome 정보(G) 클릭 후 Chrome 버전 확인`
8. `https://chromedriver.chromium.org/downloads 에서 자신의 버전과 맞는 Chrome Driver 다운로드`
> ※ Chrome 버전과 Chrome Driver 버전 상이시 에러 발생
9. `다운로드 한 chromedriver.exe 를 매크로가 있는 디렉터리에 복사`
10. `https://www.base64encode.org 에서 자신의 네이버 아이디, 비밀번호 Base64 인코딩`
11. `config.json 파일에 Base64로 인코딩된 자신의 네이버 아이디, 비밀번호 입력`
> ※ 네이버 2단계 로그인 설정 시 매크로 사용 불가
12. `스크립트 실행`
> run_macro.py --target 매크로를 돌릴 사이트 주소 [--time 페이지 새고 고침 시간] [--count 매크로 동작 횟수] [--option1 옵션선택] [--option2 옵션선택] [--option3 옵션선택]

### 주의 사항
1. python-3.8.0.exe 설치 시 설치시 하단 Add Python 3.8 to PATH 체크
2. Chrome 버전과 Chrome Driver 버전 상이시 에러발생
3. 네이버 2단계 로그인 설정시 매크로 사용 불가

## 기여하기
버그 등이 발생하면 이슈로 등록해 주시거나, 문제가 되는 부분을 수정하신 후 PR해 주시면 감사하겠습니다.

## 라이선스
이 라이브러리는 [MIT 라이선스](https://github.com/OneTop4458/smartstore-macro/blob/master/LICENSE)를 따라 자유롭게 이용하실 수 있습니다.

