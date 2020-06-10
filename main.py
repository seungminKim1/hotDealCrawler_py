from bs4 import BeautifulSoup
import requests
import time
import json

URL = "https://www.fmkorea.com/hotdeal"
KAKAO_TOKEN = "5_I9M6kqEOOhkA3WbQOOLjNIi2bo9M9cK7o_UwopyV4AAAFymNKkZA"
INFO_LISTS = []

# 카카오톡 나에게 보내기 API


def send_to_kakao(info):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    t_object = {
        "object_type": "text",
        "text": info,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }

    data = {"template_object": json.dumps(t_object)}
    return requests.post(url, headers=header, data=data)


def get_hotdeal():
    get_url = requests.get(URL)
    bs = BeautifulSoup(get_url.content, "lxml")
    div = bs.find("div", {"class": "fm_best_widget"})
    lis = div.find_all("li", {"class": "li"})
    # li요소 가져오기
    for li in lis:
        send_flag = True
        a = li.find("h3", {"class": "title"})
        link = a.find("a")["href"]
        title = a.find("a").get_text(strip=True)[0:-4]
        info = li.find("div", {"class": "hotdeal_info"}
                       ).find_all("span")
        mall = info[0].find("a").get_text()
        price = info[1].find("a").get_text()
        delivery = info[2].find("a").get_text()
        crawl_info = f"*핫딜정보* 상품명:{title}, 쇼핑몰:{mall},가격:{price},배송:{delivery},링크:https://www.fmkorea.com{link}"
        # 핫딜 정보 가져오기
        for infos in INFO_LISTS:
            if infos["title"] == title:
                print(f"보낸적 있음 {infos}")
                send_flag =
                # 중복 테스트
        if send_flag:
            INFO_LISTS.append({
                "title": title,
                "mall": mall,
                "price": price,
                "delivery": delivery,
                "link": link
            })
            result = send_to_kakao(crawl_info)
            # 중복이 아니면 보낸목록에 object 형태로 저장하고 카카오톡 API 실행
            print(result.text)


if __name__ == "__main__":
    while True:
        get_hotdeal()
        time.sleep(60)
        # 1분마다 새로운 게시글 탐색
