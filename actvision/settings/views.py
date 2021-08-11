
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *

import cgitb; cgitb.enable()



# Create your views here.
def settings(request):
    return render(request,'settings.html')


@csrf_exempt
def update_Brightness(request): # 밝기 업데이트2
    print("========= 시작 ===========")
    if request != "":

        print("요청 방식 = " + request.method)
        print("input = " + value_of_request_body(request.body))
########################################################
        change = value_of_request_body(request.body) # input값 받아옴
        recently_file_name = list_blobs(user_id) # 버켓안에 최신파일 이름 받아옴
        print("버켓 최신 파일 이름 ->")
        print(recently_file_name)
        createDirectory(user_id) # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
        DOWNLOAD(user_id,"JSON/READALL/"+ recently_file_name, user_id +"/temp") # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
        setting = read_json() # 임시파일에서 불러온 json
        setting['Brightness_Control']['Brightness'] = str(change)
        now_kst = time_now()  # 현재시간 받아옴
        setting["Time"] = [now_kst.strftime("%Y"), now_kst.strftime("%m"), now_kst.strftime("%d"),
                           now_kst.strftime("%H"), now_kst.strftime("%M"), now_kst.strftime("%S")]
        save_file(setting)
        UPLOAD(user_id, user_id+"/send" , "JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################
        print("========= 종료 ===========")
        return redirect('settings.html')
    else:
        #return HttpResponse("ERROR: POST방식으로 전송됨")
        return redirect('settings.html')


@csrf_exempt
def update_min_max(request):
    change = value_of_request_body_list(request.body) # 4개의 input 값
########################################################
    recently_file_name = list_blobs(user_id)  # 버켓안에 최신파일 이름 받아옴
    print("버켓 최신 파일 이름 ->")
    print(recently_file_name)
    createDirectory(user_id)  # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
    DOWNLOAD(user_id, "JSON/READALL/" + recently_file_name, user_id + "/temp")  # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
    setting = read_json()  # 임시파일에서 불러온 json
    setting['Brightness_Control']['Auto_Brightness'] = [str(change[0]) , str(change[1])]
    setting['Brightness_Control']['Auto_CDS'] = [str(change[2]), str(change[3])]
    now_kst = time_now()  # 현재시간 받아옴
    setting["Time"] = [now_kst.strftime("%Y"), now_kst.strftime("%m"), now_kst.strftime("%d"), now_kst.strftime("%H"),
                       now_kst.strftime("%M"), now_kst.strftime("%S")]
    save_file(setting)
    UPLOAD(user_id, user_id + "/send", "JSON/READALL" + now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################

    return redirect('settings.html')


@csrf_exempt
def update_on_off(request):
    change = value_of_request_body_list(request.body) # 4개의 input 값
########################################################
    recently_file_name = list_blobs(user_id)  # 버켓안에 최신파일 이름 받아옴
    print("버켓 최신 파일 이름 ->")
    print(recently_file_name)
    createDirectory(user_id)  # user_id (시리얼포트)로 디렉토리로 만들고 temp 파일 생성, 이미 생성시 패스
    DOWNLOAD(user_id, "JSON/READALL/" + recently_file_name, user_id + "/temp")  # 버켓 속 최신파일 -> user_id/temp 임시파일로 불러옴
    setting = read_json()  # 임시파일에서 불러온 json
    setting['Power_Control']['Auto_ON'] = [str(change[0]) , str(change[1])]
    setting['Power_Control']['Auto_OFF'] = [str(change[2]), str(change[3])]
    now_kst = time_now()  # 현재시간 받아옴
    setting["Time"] = [now_kst.strftime("%Y"), now_kst.strftime("%m"), now_kst.strftime("%d"), now_kst.strftime("%H"),
                       now_kst.strftime("%M"), now_kst.strftime("%S")]
    save_file(setting)
    UPLOAD(user_id, user_id + "/send", "JSON/READALL" +  now_kst.strftime("/%Y%m%d%H%M%S"))
#######################################################

    return redirect('settings.html')

