from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.
def imgn(request):
    return render(request,'image.html')


@csrf_exempt
def upload_img(request):
    print("호출 성공")
    if request.method == 'POST':
        if request.is_ajax():
            img = request.FILES.get('chooseFile')  # 이미지를 request에서 받아옴
            path = default_storage.save(user_id +"/img.jpg", ContentFile(img.read()))
            now_kst = time_now()
            UPLOAD(user_id, user_id + "/img.jpg", "MEDIA"+now_kst.strftime("/%Y%m%d%H%M%S"))
            os.remove(user_id+"/img.jpg") # 장고에서 중복된 이름의 파일에는 임의로 이름을 변경하기 때문에 임시파일은 제거
            return redirect('image.html')
    else:
        print("POST 호출 실패!")
        return redirect('image.html')
