from django.shortcuts import render
import datetime
def home(request):
    d={'Name':'Asif','list':[2,5,4,1,3,4],'val':'jai','Birthday':datetime.datetime.now(),'con':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},

    ],'title':'Phitron','kb':5485456465,'fir':['a','b','c'],"now":datetime.datetime.now(),
    'li':['start',['kansas',['koulik','tourik'],'likon']],'num':56,'data':99
    }
    return render(request,'home.html',d)
