from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import MainTable
from itertools import chain
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from .forms import PageHop



def get_pages(totalpage=1,current_page=1):
    """
    example: get_pages(10,1) result=[1,2,3,4,5]
    example: get_pages(10,9) result=[6,7,8,9,10]
    页码个数由WEB_DISPLAY_PAGE设定
    """
    WEB_DISPLAY_PAGE = 16
    front_offset = int(WEB_DISPLAY_PAGE / 2)
    if WEB_DISPLAY_PAGE % 2 == 1:
        behind_offset=front_offset
    else:
        behind_offset=front_offset -1

    if totalpage < WEB_DISPLAY_PAGE:
        return list(range(1,totalpage+1))
    elif current_page<=front_offset:
        return list(range(1,WEB_DISPLAY_PAGE+1))
    elif current_page>=totalpage-behind_offset:
        start_page=totalpage-WEB_DISPLAY_PAGE+1
        return list(range(start_page,totalpage+1))
    else:
        start_page=current_page-front_offset
        end_page=current_page+behind_offset
        return list(range(start_page,end_page+1))


@login_required
def index(request):
#    if request.method != 'POST':
    return render(request, 'career_find/index.html')
## 未提交数据:创建一个新表单 
#        form = HobbiesForm()
#    else:
#    # POST提交的数据,对数据进行处理
#    else:
##        check_box = request.POST.getlist('check_box_list')
##        print(check_box)
#        return HttpResponseRedirect(reverse('career_find:result'))
#    
##    context = {'form': form}

#@cache_page(60 * 15)
@login_required
def result(request,page_num):
    form = PageHop()
    if request.method == 'POST':
        check_box = request.POST.getlist('check_box_list')
        
        dic_list = MainTable.objects.exclude(科目要求='不提科目要求').values()
        dic_list = list(dic_list)
        dic_list2 = dic_list[:]
#        find_result = dic_list
        check_string = ','.join(check_box)
        
        for dic in dic_list2:
            dic.setdefault('coin', 0)
            sub_string = dic['sub'].replace('，',',')
            
            if dic['sub_type'] == 1 and check_string.find(sub_string) < 0:
                dic_list.remove(dic)
                continue
            
            sub_list = sub_string.split(',')

            for sub in sub_list:
                if sub in check_box:
                    dic['coin'] += 1


            if dic['coin'] == 0:
                dic_list.remove(dic)
                
        find_result = dic_list
        find_result = sorted(dic_list,key = lambda x:(x['coin'],x['sub_type'],-len(x['层次'])),reverse=True)
        
#        find_result1 = MainTable.objects.filter(sub_type=0,sub__regex=r'%s|%s|%s'%(check_box[0],check_box[1],check_box[2])).order_by('科目要求')
#        sql = 'select * from main_table where (sub_type=1 and find_in_set(sub,"%s,%s,%s")) ORDER BY 科目要求 DESC'
#        find_result2 = MainTable.objects.raw(sql,params = check_box)
#        find_result = list(chain(find_result2,find_result1))
#        find_result = MainTable.objects.all()[:1]
        
        paginator = Paginator(find_result, 100)
#        page = request.POST.get('page')
        page = page_num
        contacts = paginator.page(page)
        check_box = ','.join(check_box)
        total_page_number=contacts.paginator.num_pages
        page_list=get_pages(int(total_page_number),int(page))
        context = {'contacts':contacts,'check_box':check_box,'page_list':page_list,'form':form}
        return render(request,'career_find/result.html',context)

        
#        return HttpResponseRedirect(reverse('career_find:result'))
#    
#    context = {'form': form}
#    return render(request, 'career_find/index.html', context)

#@cache_page(60 * 15)
@login_required
def page(request,check_box,page_num):
    form = PageHop()
    if request.method == 'POST':
        form = PageHop(request.POST)
        if form.is_valid():
            page_num = form.cleaned_data['跳页']
            
    if check_box == '不限':
            dic_list = MainTable.objects.filter(科目要求='不提科目要求')
            find_result = dic_list
            paginator = Paginator(find_result, 100)
            page = page_num
            contacts = paginator.page(page)
            total_page_number=contacts.paginator.num_pages
            page_list=get_pages(int(total_page_number),int(page))
            context = {'contacts':contacts,'check_box':check_box,'page_list':page_list,'form':form}
            return render(request,'career_find/result.html',context)
    
            
    else:
        check_box = check_box.split(',')
    #    find_result1 = MainTable.objects.filter(sub_type=0,sub__regex=r'%s|%s|%s'%(check_box[0],check_box[1],check_box[2]))
    #    sql = 'select * from main_table where (sub_type=1 and find_in_set(sub,"%s,%s,%s")) ORDER BY 科目要求 DESC'%(check_box[0],check_box[1],check_box[2])
    #    find_result2 = MainTable.objects.raw(sql)
    #    find_result = list(chain(find_result2,find_result1))
        
        dic_list = MainTable.objects.exclude(科目要求='不提科目要求').values()
        dic_list = list(dic_list)
        dic_list2 = dic_list[:]
        
        check_string = ','.join(check_box)
            
        for dic in dic_list2:
            dic.setdefault('coin', 0)
            sub_string = dic['sub'].replace('，',',')
            
            if dic['sub_type'] == 1 and check_string.find(sub_string) < 0:
                dic_list.remove(dic)
                continue
            
            sub_list = sub_string.split(',')
    
            for sub in sub_list:
                if sub in check_box:
                    dic['coin'] += 1
    
    
            if dic['coin'] == 0:
                dic_list.remove(dic)
                
        find_result = dic_list
        find_result = sorted(dic_list,key = lambda x:(x['coin'],x['sub_type']),reverse=True)
        
        
        paginator = Paginator(find_result, 100)
        page = page_num
        contacts = paginator.page(page)
        check_box = ','.join(check_box)
        total_page_number=contacts.paginator.num_pages
        page_list=get_pages(int(total_page_number),int(page))
        context = {'contacts':contacts,'check_box':check_box,'page_list':page_list,'form':form}
        return render(request,'career_find/result.html',context)
    

    
    
    
    
    
    
    
    