import random
import re
import sys

import requests

requests = requests.Session()


def getcookies():
    headers = {
        'authority': 'wrggk.whvcse.edu.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'http://wrggk.whvcse.edu.cn/web/Login.aspx',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get('http://wrggk.whvcse.edu.cn/web/Index5m.aspx', headers=headers)


def login(username, password):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'http://wrggk.whvcse.edu.cn/web/Login.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.get(
        f'http://wrggk.whvcse.edu.cn/auth.aspx?action=login&username={username}&password={password}&callback=?&random={random.random()}',
        headers=headers,
        verify=False,
    )
    if "学生" in response.text:
        print("登录成功")
    else:
        print("登录失败")
        input("Press Enter To Exit ")
        sys.exit()



def getcoursenameandurl():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'http://wrggk.whvcse.edu.cn/web/Index5m.aspx',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get('http://wrggk.whvcse.edu.cn/web/MyCourse.aspx', headers=headers,
                            verify=False)

    coursename = re.findall(
        r'<div class="coursera-dashboard-course-listing-box-main c2"><div class="coursera-dashboard-course-listing-box-name"><a href="/web/CourseDetail.aspx\?courseId=(.*?)&type=(.*?)">(.*?)</a></div>',
        response.text)
    courseurl = re.findall(
        r'<a class="enter coursera-dashboard-course-listing-box-go-button btn-flat btn-flat-success" href="/Web/CourseInfo.aspx\?id=(.*?)&cid=(.*?)" data-tooltip="" title=',
        response.text)
    if len(coursename) == 0:
        print("该账号没有选择课程")
    return coursename, courseurl


def tapstartstudy(id, cid):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'http://wrggk.whvcse.edu.cn/web/MyCourse.aspx',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'id': f'{id}',
        'cid': f'{cid}',
    }

    response = requests.get('http://wrggk.whvcse.edu.cn/Web/CourseInfo.aspx', params=params, verify=False,
                            headers=headers)

    couresevideos = re.findall(
        rf'<a  href="/Viewer/CoursePlay.aspx\?class=0&id={id}&sid=(.*?)&mid=(.*?)&courseClassId={cid}&chapterId=(.*?)" target="_blank"  >',
        response.text)
    examurl1 = re.findall(
        rf"<a href='/Viewer/CourseExam.aspx\?id={id}&sid=(.*?)&mid=(.*?)&courseClassId={cid}&chapterId=(.*?)&pid=(.*?)' target=",
        response.text)

    
    examurl2 = re.findall(
        rf'<a  href="/Viewer/CourseExam.aspx\?id={id}&sid=(.*?)&mid=(.*?)&courseClassId={cid}&chapterId=(.*?)&pid=(.*?)" target=',
        response.text)
    courseexamurl = re.findall(
        rf'<a href="/Viewer/CourseExam.aspx\?id={id}&sid=(.*?)&mid=(.*?)&courseClassId={cid}&chapterId=(.*?)&pid=(.*?)">课程考试',
        response.text)

    return couresevideos, examurl1, examurl2, courseexamurl


def startcourse(coursename, courseid, cpid, courseClassId):
    headers = {
        'authority': 'wrggk.whvcse.edu.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'http://wrggk.whvcse.edu.cn',
        'referer': 'http://wrggk.whvcse.edu.cn/Viewer/CoursePlay.aspx?class=0&id=1081&sid=14223&mid=63387&courseClassId=832&chapterId=14219',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'cpid': f'{cpid}',
        'bjtime': '500.452302',
        'courseid': f'{courseid}',
        'stepid': f'{cpid}',
        'courseClassId': f'{courseClassId}',
        't': '60',
    }

    response = requests.post('http://wrggk.whvcse.edu.cn/Viewer/timetop.aspx', params=params, verify=False,
                             headers=headers)

    if response.json()["BaseType"] == "1":
        print(coursename + "刷课中")
    else:
        print(coursename + "刷课失败")


def tapstartexam(id, sid, mid, courseClassId, chapterId, pid):
    headers = {
        'authority': 'wrggk.whvcse.edu.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://wrggk.whvcse.edu.cn/Web/CourseInfo.aspx?id=1081&cid=832',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'id': f'{id}',
        'sid': f'{sid}',
        'mid': f'{mid}',
        'courseClassId': f'{courseClassId}',
        'chapterId': f'{chapterId}',
        'pid': f'{pid}',
    }

    response = requests.get('http://wrggk.whvcse.edu.cn/Viewer/CourseExam.aspx', params=params, verify=False,
                            headers=headers)
    userid = re.findall(
        rf'<iframe src="http://wrggkk.whvcse.edu.cn//excute/DoPaper.aspx\?classid={courseClassId}&stepid={sid}&paperid={pid}&courseid={id}&userid=(.*?)&examCountId=&times=1&username=(.*?)&t=1" style=',
        response.text)
    return userid


def viewanswer(classid, stepid, paperid, courseid, userid, username):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'classid': f'{classid}',
        'stepid': f'{stepid}',
        'paperid': f'{paperid}',
        'courseid': f'{courseid}',
        'userid': f'{userid}',
        'examCountId': '',
        'times': '1',
        'username': f'{username}',
        'view': '1',
    }

    response = requests.get(
        'http://wrggkk.whvcse.edu.cn//excute/DoPaper.aspx',
        params=params,
        headers=headers,
        verify=False,
    )
    answer = re.findall(rf'正确答案为：(.* ?)\n', response.text)
    answerid = re.findall(rf'id="result(.*?)"', response.text)
    answervalue = re.findall(rf'(A|B|C|D|E|F|).<input name="questionInfoID_(.*?)" value="(.*?)"', response.text)
    endexamurl = re.findall(rf'<form name="form1" action="checkpaper.aspx(.*?)"', response.text)
    jiandati = re.findall(r"简答题", response.text)

    return answer, answerid, answervalue, endexamurl, jiandati


def endexam(url, data):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://wrggkk.whvcse.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    data = data

    response = requests.post(
        url,
        headers=headers,
        data=data,
        verify=False,
    )
    print(response.url + "刷测验成功")


def cheyanshuji(count, k):

    userid = tapstartexam(count[1], k[0], k[1], count[2], k[2], k[3])

    if len(userid) == 0:
        return

    answer, answerid, answervalue, endexamurl, jiandati = viewanswer(count[2], k[0], k[3],
                                                                     count[1],
                                                                     userid[0][0],
                                                                     userid[0][1])

    new_list = [item.replace('\r', '') for item in answer]
    if len(jiandati) != 0:
        has_answer = False
        for w, element in enumerate(new_list):
            if element == '正确' or element == '错误':
                new_list.insert(w, '简答题')
                has_answer = True
                break

    paired_lists = list(zip(new_list, answerid))

    grouped_data_set2 = {}
    for item in answervalue:
        option, question, answer = item
        if question not in grouped_data_set2:
            grouped_data_set2[question] = [(option, answer)]
        else:
            grouped_data_set2[question].append((option, answer))


    matched_data = []
    for data in paired_lists:
        for key, value in grouped_data_set2.items():
            if data[1] == key:
                matched_data.append((data, value))
    newdata = {}
    newdata["LastTime"] = 2
    for i in matched_data:

        if ',' in i[0][0]:
            selected_answers = i[0][0].split(',')
            shuzhu = []
            for k in selected_answers:
                for j in i[1]:
                    if k == j[0]:
                        shuzhu.append(j[1])
            newdata["questionInfoID_" + i[0][1]] = shuzhu
            newdata["unsure_pad_" + i[0][1]] = 0
        else:
            if i[0][0] == 'A':
                newdata["questionInfoID_" + i[0][1]] = i[1][0][1]
                newdata["unsure_pad_" + i[0][1]] = 0
            if i[0][0] == 'B':
                newdata["questionInfoID_" + i[0][1]] = i[1][1][1]
                newdata["unsure_pad_" + i[0][1]] = 0
            if i[0][0] == 'C':
                newdata["questionInfoID_" + i[0][1]] = i[1][2][1]
                newdata["unsure_pad_" + i[0][1]] = 0
            if i[0][0] == 'D':
                newdata["questionInfoID_" + i[0][1]] = i[1][3][1]
                newdata["unsure_pad_" + i[0][1]] = 0
            if i[0][0] == 'E':
                newdata["questionInfoID_" + i[0][1]] = i[1][4][1]
                newdata["unsure_pad_" + i[0][1]] = 0

        if '正确' == i[0][0]:
            newdata["questionInfoID_" + i[0][1]] = i[1][0][1]
            newdata["unsure_pad_" + i[0][1]] = 0
        if '错误' == i[0][0]:
            newdata["questionInfoID_" + i[0][1]] = i[1][1][1]
            newdata["unsure_pad_" + i[0][1]] = 0
    endexam("http://wrggkk.whvcse.edu.cn/excute/checkpaper.aspx" + endexamurl[0], newdata)


if __name__ == '__main__':
    try:
        print("1.仅用于学习交流，严禁大规模传播，禁止商业用途，否则自行承担后果。")
        print("2.所有资源请于下载后24小时内删除，如需更好体验，请购买正版。")
        print("""3技术原理请看【python】requests库 让世界再无难看的课（上）
                    https://www.52pojie.cn/thread-1900832-1-1.html
                    (出处: 吾爱破解论坛)""")
        getcookies()
        login(input("账号"), input("密码"))
        coursename, courseurl = getcoursenameandurl()
        new_tuples = []
        for tup1, tup2 in zip(coursename, courseurl):
            new_tup = (tup1[2], tup2[0], tup2[1])
            new_tuples.append(new_tup)
        for count, i in enumerate(new_tuples):
            print(str(count + 1) + i[0])
        for count in new_tuples:
            couresevideos, examurl, examurl2, courseexamurl = tapstartstudy(count[1], count[2])

            for k in examurl:
                cheyanshuji(count, k)

            for d in courseexamurl:
                cheyanshuji(count, d)

            for f in examurl2:
                cheyanshuji(count, f)
            for i in couresevideos:
                startcourse(count[0], count[1], i[1], count[2])
    except Exception as e:
        print("An error occurred:", e)
    finally:
        requests.close()
        input("Press Enter to exit...")
