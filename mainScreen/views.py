from django.shortcuts import render
import requests
import json
from .forms import ReviewFields
import os

# Create your views here.
def index(request):
    form =ReviewFields()
    if request.method == 'POST':
        form = ReviewFields(request.POST)
        if form.is_valid():
            print('form is valid')
            print("json",form.cleaned_data['jsonfield'])
    return render(request,'index.html',{'form':form})

def result(request):
    json_string = request.POST.get('jsonfield')

    header = {
            'Content-Type': 'application/json',
            'Control': 'no-cache',
        }

    username = os.getenv("USERNAME")
    password : os.getenv("PASSWORD")
    
    auth = (username,password)

    data = json_string
    print(data)
    res = requests.post('https://192.86.32.113:19443/zosConnect/services/ONNX?action=invoke', auth=auth, data=data, headers=header,verify=False)
    json_out = (json.loads(res.text))
    json_out = json_out['FRAUDRES']['FRAUDRES']['XDATA2'][:2]
    return render(request, 'result.html',{"res":json_out})