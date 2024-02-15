from django.http import HttpResponse
from items.models import Item
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("items!")


def createItem(request, userid):
    itemName = request.POST['项目名称'],
    itemDetails = request.POST['具体内容'],
    itemEleConsume = request.POST['消耗电量'],
    itemDdl = request.POST['截止日期']
    thisItemUser = userid
    Item.objects.create(name=itemName, ddl=itemDdl, details=itemDetails, electricityConsume=itemEleConsume[0],
                        itemUser_id=thisItemUser)
    return HttpResponse("createItem")
