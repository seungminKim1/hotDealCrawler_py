# hotDealCrawler_py
hotDealCrawler with Python
# Info
* Language
  * Python
* Framework  
  * Visual Studio Code
* Image

핫딜 정보를 크롤링 해올 대상 페이지의 모습

![Web](https://github.com/seungminKim1/hotDealCrawler_py/blob/master/images/웹페이지.PNG)

크롤링해온 정보를 Object에 담아 JSON형태로 카카오톡 나에게로 메시지 보내기 API서비스를 이용해 전송한 모습

![sendToKakao](https://github.com/seungminKim1/hotDealCrawler_py/blob/master/images/카카오.PNG)

1분 주기로 대상의 웹페이지를 확인해 정보를 가져오고 수정사항이나 새로운 정보를 확인해 다시 보내준 모습

![routine](https://github.com/seungminKim1/hotDealCrawler_py/blob/master/images/카카오%20중복%20제거.PNG)
 
 
 
 ------
 * 작업한 기능
   * requests를 이용해 웹페이지의 데이터를 가져옴
   * BeautifulSoup을 이용해 html의 형태로 parsing함
   * 카카오 API를 이용해 메시지를 통해 정보를 전달 해줌
   
