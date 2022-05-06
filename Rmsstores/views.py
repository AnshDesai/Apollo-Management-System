from .importer import *

global temp,dateval
temp = 0

def rms_store(request):
    if request.session._session:
        user = request.session['Users']
        role = Authorizatn.objects.filter(emp_id=user,plt=request.session['PLT']).values_list('user_type','appl')
        # print(role[0])
        request.session['role'] = role[0]
        # s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # # start TLS for security 
        # s.starttls() 
        
        # # Authentication 
        # s.login("17ce024@charusat.edu.in", "") 
        
        # # message to be sent 
        # message = "Hello! Ansh"
        
        # # sending the mail 
        # s.sendmail("17ce024@charusat.edu.in", "anshdesai20@gmail.com", message) 
        
        # # terminating the session 
        # s.quit() 
        return render(request,'Rms_mainpage.html',{'role':role[0]})
    else:
        return redirect('login') 
def notification():
    proxy_url = "http://172.19.0.121:8080"
    telepot.api._pools = {
        'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
    }
    telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
    bot = telepot.Bot('1643290062:AAEd4OPOLp6BF8ZLb-Ba6Vkma_vyNgDgWxc')
    bot_chatID = '-598594620'
    bot.sendMessage(bot_chatID,"MADAR")



def vendor_master(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
     
    if request.method == 'POST':
        venform  = RmsVendormastForm(data=request.POST,initial={'plt': session_plt,'updtby':request.session['Name'],'updton':date.today}) 
        try:
            with transaction.atomic():
                if venform.is_valid():
                    venform.save()
                    messages.info(request, 'Successfully added') 
                    return HttpResponseRedirect(request.path)
                else:
                    messages.info(request, 'Duplicate values not allowed')
        except Exception as e:
            print(e)    
    else:
        venform =RmsVendormastForm(initial={'plt': session_plt})  
    return render(request,"Rms_vendormast.html",{'form':venform,'role':role})

def ven_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsVendorRep(session_plt)
    if request.method == "POST":
      form = RmsVendorRep(request.POST,session_plt)
      if form.is_valid:
          ven_filter_view(request)
    return render(request, 'Rms_vendormastrep.html',{'form': form,'role':role})

def ven_filter_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsVendormast.objects.values_list('flag','vcode').filter(**filter_params)
    if (request.GET['flag']) is not None and (request.GET['flag'])!="":
        filter_params['flag'] = request.GET['flag']
        query = RmsVendormast.objects.values_list('flag','vcode').filter(**filter_params)
    return render(request,'Rms_vendormastrep_view.html',{'f':query,'role':role})

def group_master(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    if request.method == 'POST':
        try:
            with transaction.atomic(): 
                grpform  = RmsGroupmastForm(data=request.POST,initial={'plt': session_plt,'updtby':request.session['Name'],'updton':date.today})
                if grpform.is_valid():
                    grpform.save()
                    messages.info(request, 'Successfully added') 
                    return HttpResponseRedirect(request.path)
                else:
                    messages.info(request, 'Duplicate values not allowed')
        except Exception as e:
            print(e)
    else:
        grpform =RmsGroupmastForm(initial={'plt': session_plt}) 
    return render(request,"Rms_groupmast.html",{'form':grpform,'role':role})

def grp_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsGroupRep(session_plt)
    if request.method == "POST":
      form = RmsGroupRep(request.POST,session_plt)
      if form.is_valid:
          grp_filter_view(request)
    return render(request, 'Rms_groupmastrep.html',{'form': form,'role':role})

def grp_filter_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsGroupmast.objects.values_list('flag','groupno').filter(**filter_params)
    if (request.GET['flag']) is not None and (request.GET['flag'])!="":
        filter_params['flag'] = request.GET['flag']
        query = RmsGroupmast.objects.values_list('flag','groupno').filter(**filter_params)
    
    return render(request,'Rms_groupmastrep_view.html',{'f':query,'role':role})

def item_master(request):
    role = request.session['role'] 
    session_plt = request.session['PLT'] 
    if request.method == 'POST': 
        itemform  = RmsItemmastForm(data=request.POST,initial={'plt': session_plt,'updtby':request.session['Name'],'updton':date.today})
        if itemform.is_valid():
            itemform.save()
            messages.info(request, 'Successfully added') 
            return HttpResponseRedirect(request.path)
        else:
            messages.info(request, 'Duplicate values not allowed')
    else:
        itemform =RmsItemmastForm(initial={'plt': session_plt})  
    return render(request,"Rms_Itemmast.html",{'form':itemform,'role':role})

def item_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsItemRep(session_plt)
    if request.method == "POST":
      form = RmsItemRep(request.POST,session_plt)
      if form.is_valid:
          item_filter_view(request)
    return render(request, 'Rms_itemmastrep.html',{'form': form,'role':role})

def item_filter_view(request):
    role = request.session['role'] 
    cols = ['flag','itemcode','itemdesc','groupno','unit']
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsItemmast.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['flag']) is not None and (request.GET['flag'])!="":
        filter_params['flag'] = request.GET['flag']
        query = RmsItemmast.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['itemcode']) is not None and (request.GET['itemcode'])!="":
        filter_params['itemcode'] = request.GET['itemcode']
        query = RmsItemmast.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['groupno']) is not None and (request.GET['groupno'])!="":
        filter_params['groupno'] = request.GET['groupno']
        query = RmsItemmast.objects.values_list(*cols).filter(**filter_params)
    # print(filter_params)
    kwar = {k: v for k, v in filter_params.items() if v}
    # print(kwar)
    return render(request,'Rms_itemmastrep_view.html',{'f':query,'role':role})

def unit_master(request):
    role = request.session['role'] 
    updton = date.today
    updtby = request.session['Users']
    plt = request.session['PLT']
    if request.method == 'POST': 
        unitform  = RmsUnitmastForm(data=request.POST,initial={'plt':plt,'updton':updton,'updtby':updtby})
        if unitform.is_valid():
            unitform.save()
            messages.info(request, 'Successfully added') 
            return HttpResponseRedirect(request.path)
        else:
            messages.info(request, 'Duplicate values not allowed')
    else:
        unitform =RmsUnitmastForm(initial={'plt':plt,'updton':updton,'updtby':updtby}) 
    return render(request,"Rms_unitmast.html",{'form':unitform,'role':role})

def shelf_master(request):
    role = request.session['role'] 
    return render(request,'Rms_shelfmast.html',{'role':role})

def autocomplete(request):
    if 'term' in request.GET:
        qs = RmsItemmast.objects.values_list("itemcode","itemdesc","groupno").filter(itemdesc__istartswith=request.GET.get('term'))
        item_desc = list()
        for i in qs:
            item_desc.append(i)
        item_desc = ['-'.join(tups) for tups in item_desc] 
        #print(item_desc)
        return JsonResponse(item_desc,safe=False)

def shelfmasttemp(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    session_uptdby = request.session['Users']
    itemdesc_val =dict(request.GET.lists())
    values = (itemdesc_val['itemdesc'][0]).split('-')
    itemdesc_val = values[1]
    itemcode = values[0]
    groupno = values[2]
    life_remarks = list(RmsShelfmast.objects.values_list("shelflife","remarks","updton","updtby").filter(itemcode=values[0],plt=session_plt))
    prevupddate = life_remarks[0][2].strftime('%Y-%m-%d')
    #print(prevupddate)
    #print(date.today())
    shelfform = RmsShelfmastForm(initial={'shelflife':life_remarks[0][0],'remarks':life_remarks[0][1],'plt': session_plt,'updtby':request.session['Name'],'updton':life_remarks[0][2],'itemdesc':itemdesc_val,'itemcode':itemcode,'groupno':groupno})
    if request.method == 'POST': 
        newshelflife = request.POST['shelflife']
        shelfform  = RmsShelfmastForm(data=request.POST,initial={'plt': session_plt,'updtby':session_uptdby,'itemdesc':itemdesc_val,'itemcode':itemcode,'groupno':groupno})
        RmsShelfmast.objects.filter(itemcode=values[0],plt=session_plt).update(shelflife=newshelflife,updton=date.today(),updtby=session_uptdby)
        RmsShelfMastUpd.objects.create(plt=session_plt,itemcode=values[0],prevshelflife=life_remarks[0][0],newshelflife=newshelflife,groupno=groupno,itemdesc=itemdesc_val,remarks=life_remarks[0][1],updtby=session_uptdby,updton=date.today(),prevupddate=prevupddate,prevupdby=life_remarks[0][3],reason=request.POST["reason"])
        # messages.success(request, 'Successfully updated') 
        return HttpResponseRedirect("Rms_shelfmast",{'form':shelfform,'role':role})
    else:
        return render(request,"Rms_shelfmasttemp.html",{'form':shelfform,'role':role})

def shelfmastrep(request):
    role = request.session['role'] 
    return render(request,"Rms_shelfmastrep.html",{'role':role})

def shelfmastrep_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    session_uptdby = request.session['Name']
    itemdesc_val =dict(request.GET.lists())
    values = (itemdesc_val['itemdesc'][0]).split('-')
    query = RmsShelfmast.objects.values_list('itemcode','groupno','itemdesc','shelflife','remarks').filter(itemcode=values[0],groupno=values[2],itemdesc=values[1],plt=session_plt)
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{"shelfmastrepotrts.xls"}"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Table')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['itemcode','groupno','itemdesc','shelflife','remarks']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            somemodel_filter =RmsShelfmast.objects.values_list('itemcode','groupno','itemdesc','shelflife','remarks').filter(itemcode=values[0],groupno=values[2],itemdesc=values[1],plt=session_plt)
            rows = somemodel_filter
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
    else:
        return render(request,"Rms_shelfmastrep_view.html",{'f':query,'role':role})

def grnupload(request):
    role = request.session['role'] 
    if "GET" == request.method:
        return render(request, 'Rms_grnupload.html',{'role':role})
    else:
        # df_new['Pstng Date'].fillna(None, inplace=True)
            # df_new['Manuf. Dte'].fillna(None, inplace=True)
            # df_new['Doc. Date'].fillna(None, inplace=True)
            # df_new['Entry Date'].fillna(None, inplace=True)
            # df_new['SLED/BBD'].fillna(None, inplace=True)
            # df['date1'] = df['date'].dt.strftime('%d/%m/%y')
        #To check if rows in excel are already uploaded
        df=pd.read_excel(request.FILES["excel_file"].temporary_file_path(),engine='openpyxl',converters={'Material':str,'Mat. Doc.':str,'Vendor':str,})
        itemcode_mas = list(RmsItemmast.objects.filter(plt=request.session['PLT']).values_list('itemcode',flat=True))
        vcode_mas = list(RmsVendormast.objects.filter(plt=request.session['PLT']).values_list('vcode',flat=True))
        convunit_list = list(RmsUnitmast.objects.filter(plt=request.session['PLT']).values_list('convunit',flat=True))        
        unit_list = list(RmsUnitmast.objects.filter(plt=request.session['PLT']).values_list('unit',flat=True))        
        items_main = list(RmsGrnupload.objects.filter(plt=request.session['PLT']).values_list('itemcode','itemdoc'))
        items_main_temp = list(RmsGrnuploadTemp.objects.filter(plt=request.session['PLT']).values_list('itemcode','itemdoc'))
        count = 0
        df = df.dropna(how='all')
        df[['Mat. Doc.', 'Vendor','Material']] = df[['Mat. Doc.', 'Vendor','Material']].fillna(value="null")
        df['Mat. Doc.'] = df['Mat. Doc.'].astype(str)
        df['Vendor'] = df['Vendor'].astype(str)
        df['Material'] = df['Material'].astype(str)
        #df['Manuf. Dte'] = df['Manuf. Dte'].astype(str)
        df['Manuf. Dte'] = pd.to_datetime(df['Manuf. Dte'],format= '%Y-%m-%d',errors='coerce').dt.date
        # df['Entry Date'] = pd.to_datetime(df['Entry Date'],format= '%m/%d/%y' ).dt.date
        # df['SLED/BBD'] = pd.to_datetime(df['SLED/BBD'],format= '%m/%d/%y' ).dt.date
        # df['Pstng Date'] = pd.to_datetime(df['Pstng Date'],format= '%m/%d/%y' ).dt.date
        # print("Recipienttype:",type(df['Recipient'][1]))
        #print("DF",df['Mat. Doc.'])
        #print("DF",df[:25])
        df_new = df
        notfound = list()
        for i in df_new['Vendor']:
            if str(i) not in vcode_mas:         
                count +=1
                #print("ven",str(i))
                notfound.append(count)
                df_new = df_new[df_new.Vendor != i]
        for i in df_new['Material']:
            if str(i) not in itemcode_mas:
                notfound.append(count)
                #print("mat",str(i))
                df_new = df_new[df_new.Material != i]
        for i in df_new['Quantity']:
            print(decimal.Decimal(i))
            if decimal.Decimal(i) <0:
                notfound.append(count)
                #print("mat",str(i))
                df_new = df_new[df_new.Quantity != i]
        df = df[df.index.isin(notfound)]
        d1 = df_new.iloc[:0].copy()
       
        for a,b in zip(df_new['Material'],df_new['Mat. Doc.']):
            if (a,b) in items_main_temp:
                # print('a,b:',(a,b))
                i = df_new[(df_new['Material'] ==a) & (df_new['Mat. Doc.'] == b)].index
                #print("DFINDEX:",df_new[(df_new['Material'] ==a) & (df_new['Mat. Doc.'] == b)].index)
                df_new.drop(i,inplace=True) 
        for a,b in zip(df_new['Material'],df_new['Mat. Doc.']):
            if (a,b) in items_main:
                i = df_new[(df_new['Material'] ==a) & (df_new['Mat. Doc.'] == b)].index
                #print("DFINDEX:",df_new[(df_new['Material'] ==a) & (df_new['Mat. Doc.'] == b)].index)
                df_new.drop(i,inplace=True)                                
        #print('DF_NEW:',df_new)
        #print(convunit_list)
        for i,j,k in zip(df_new['Unit'],df_new['Quantity'],df_new.index):
            #print(i,j)
            if i in convunit_list:
                #print("acc")
                continue 
            if i in unit_list:
                #print("not")
                newunit = list(RmsUnitmast.objects.filter(plt=request.session['PLT'],unit=i).values_list('convunit','convamount'))
                df_new.at[k, 'Unit'] = newunit[0][0]
                j *= float(newunit[0][1]) 
                df_new.at[k, 'Quantity'] = j


        msg = df[['Mat. Doc.', 'Material']]
        msg = msg.to_html(table_id="table")
        
        if df_new.empty:
            messages.info(request,  mark_safe('Successfully added: '+str(len(df_new.index))+' rows' +'<br/>Please update for the following Mat Doc and Itemcode:'))
            request.session['rows'] = 0
            return render(request, 'Rms_grnupload.html',{'table':msg,'role':role})
        #print("DFNEW:",df_new)
        try:
            with transaction.atomic():
                cncontrol = list(RmsCN.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],ctrlno_document='upload').values_list('ctrlno_document',flat=True))
                if not cncontrol:
                    RmsCN.objects.create(plt=request.session['PLT'],finyear=request.session['Finyear'],ctrlno_document='upload',ctrl_next_no=0)
                no = list(RmsCN.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],ctrlno_document='upload').values_list('ctrl_next_no',flat=True))  
                # df_new['Pstng Date'].fillna(None, inplace=True)
                df_new['Manuf. Dte'].fillna('1900-01-01', inplace=True)
                #df_new.where(df_new., None)
                df_new['Doc. Date'].fillna('1900-01-01', inplace=True)
                df_new['Entry Date'].fillna('1900-01-01', inplace=True)
                df_new['SLED/BBD'].fillna('1900-01-01', inplace=True)
                df_new['Batch'].fillna('-', inplace=True)
                fin = request.session['Finyear']
                instances = [
                    models.RmsGrnuploadTemp(
                        serialno=index,
                        updno=no[0],
                        finyear = fin,
                        plt = request.session['PLT'],
                        itemdoc = row['Mat. Doc.'],
                        itemcode = row['Material'],
                        itemdesc = row['Material Description'],
                        sloc = row['SLoc'],
                        batch = row['Batch'],
                        grgi = row['GR/GI Sl'],
                        headertxt = row['HeaderText'],
                        unloadpt = row['Unloading Point'],
                        landbill = row['Bill of Lading'],
                        glacc = row['G/L acct'], 																		
                        recepient = row['Recipient'],
                        mvt = row['MvT'],
                        mttext = row['Movement Type Text'],
                        po = row['PO'],
                        reference = row['Reference'],
                        stobin = row['StorageBin'],
                        usname = row['User name'],
                        valtype = row['Val. Type'],
                        vcode = row['Vendor'],
                        quantity = row['Quantity'],
                        unit = row['Unit'],
                        pstdate = row['Pstng Date'],
                        mandate = row['Manuf. Dte'],  
                        sled = row['SLED/BBD'],
                        amountlc = row['Amount in LC'],
                        curr = row['Crcy'],
                        docdate = row['Doc. Date'],
                        entrydate = row['Entry Date'],
                        oun = row['OUn'],
                        ounqty = row['Qty in OPUn']   
                )
                for index, row in df_new.iterrows()
                ]
                #print(instances)
                models.RmsGrnuploadTemp.objects.bulk_create(instances)
                no= no[0]+1
                RmsCN.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],ctrlno_document='upload').update(ctrl_next_no=no)
                request.session['rows'] = len(df_new.index)
                itemdoc = RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('itemdoc',flat=True)
                batch = list(RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('batch',flat=True))
                itemcode = RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('itemcode',flat=True)
                # print(itemdoc,itemcode,batch)
                # print(batch[1])
                for i in range(len(itemcode)):
                    # print(i)
                    # print(itemcode[i])
                    # print(batch[i])
                    if(batch[i]=="-"):
                        remarks = list(RmsShelfmast.objects.filter(plt=request.session['PLT'],itemcode=itemcode[i]).values_list('remarks'))
                        shelflife = list(RmsShelfmast.objects.filter(plt=request.session['PLT'],itemcode=itemcode[i]).values_list('shelflife'))
                        # print(remarks,shelflife)
                        if(remarks[0]=='From Date of Mfg.'):
                            # print("hekk")
                            mandate = list(RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemdoc=itemdoc[i],itemcode=itemcode[i]).values_list("mandate"))
                            sled = mandate[0] + relativedelta(months=+int(shelflife[0])) 
                            RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=itemdoc[i],itemcode=itemcode[i]).update(sled=sled)
                            # print("continue")        
                        elif(remarks[0]=='From Date of Receipt'):
                            # print("hekk1")
                            pstdate = RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=itemdoc[i],itemcode=itemcode[i]).values_list("pstdate",flat=True)
                            sled = pstdate[0] + relativedelta(months=+int(shelflife[0])) 
                            RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=itemdoc[i],itemcode=itemcode[i]).update(sled=sled)
                # print("hello")
                messages.info(request, mark_safe('Successfully added: '+str(len(df_new.index))+'rows'+'<br/>Please update for the following Mat Doc and Itemcode:')) 
                return render(request, 'Rms_grnupload.html',{'table':msg,'role':role})
        except Exception as e:
            messages.info(request,e)
            messages.info(request,  mark_safe('Duplicates values found:'+'<br/>Please update for the following Mat Doc and Itemcode:'))
            return render(request, 'Rms_grnupload.html',{'table':msg,'role':role})

def grnuploadrep(request):
    role = request.session['role'] 
    count = 0
    cols = ['updno','serialno','plt','finyear','itemdoc','itemcode','itemdesc','batch','sloc','grgi','headertxt','unloadpt','landbill','glacc','recepient','mvt','mttext','po','reference',
    'stobin','usname','valtype','vcode','quantity','unit','pstdate','mandate','sled','amountlc','curr','docdate','entrydate','oun','ounqty','type','avgqty']
    grn_list = RmsGrnuploadTemp.objects.values_list(*cols).filter(plt=request.session['PLT'])
    imastcode = RmsItemmast.objects.filter(plt=request.session["PLT"]).values_list("itemcode",flat=True)
    vmastcode = RmsVendormast.objects.filter(plt=request.session["PLT"]).values_list("vcode",flat=True)
    session_type = list(RmsGrnuploadTemp.objects.filter(plt=request.session["PLT"]).values_list("type","avgqty"))
    type_values = list()
    for i,j in session_type:
        type_values.append({'type':i,'avgqty':j})
    # print(type_values)
    formset = formset_factory(RmsGrnRep,extra=0)
    if request.method == 'POST' and 'delete' in request.POST:
        del_list = list()
        query = formset(request.POST or None)
        # print(query)
        if query.is_valid():
            # print("enterd")
            q = query.cleaned_data
            q = [i for i in q if i]
            # print(q[0]['delete'])
            for i in q:
                # print(i)
                del_list.append(i['delete'])
            # print(del_list)
            itemcode = RmsGrnuploadTemp.objects.values_list('itemcode',flat=True).filter(plt=request.session['PLT'])
            itemdoc = RmsGrnuploadTemp.objects.values_list('itemdoc',flat=True).filter(plt=request.session['PLT'])
            values_dict = list(zip([typeval for typeval in del_list], [icode for icode in itemcode], [doc for doc in itemdoc]))
            # print(values_dict)
            for i in values_dict:
                if i[0]==True:
                    RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1]).delete()
            return HttpResponseRedirect("Rms_grnuploadrep",{'role':role})

    if request.method == 'POST' and 'update' in request.POST:
        formset = formset_factory(RmsGrnRep,extra=request.session['rows'])
        form = formset()    
        dataset = request.POST
        type_list = list()
        avgqty_list = list()
        query = formset(request.POST or None)
        if query.is_valid():
            q = query.cleaned_data 
        q = filter(None, q)
        for i in q:
            type_list.append(i['type'])
            avgqty_list.append(i['avgqty'])
        itemcode = RmsGrnuploadTemp.objects.values_list('itemcode',flat=True).filter(plt=request.session['PLT'])
        itemdoc = RmsGrnuploadTemp.objects.values_list('itemdoc',flat=True).filter(plt=request.session['PLT'])
        vendorcode = RmsGrnuploadTemp.objects.values_list('vcode',flat=True).filter(plt=request.session['PLT'])
        values_dict = list(zip([typeval for typeval in type_list], [icode for icode in itemcode], [doc for doc in itemdoc], [v for v in vendorcode],[a for a in avgqty_list]))
        for i in values_dict:
            RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1]).update(type=i[0])
            RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1]).update(avgqty=i[4]) 
        # print("Values Dict: ",values_dict)
        try:
            with transaction.atomic():
                forloopcounter = 0
                grn_list = list(RmsGrnuploadTemp.objects.values_list(*cols).filter(plt=request.session['PLT']))
                for i in values_dict:
                    # print("i[4]:",i[4])
                    if i[4] !=None:
                        # print("Check complete entered!")
                        # print(grn_list)
                        newobject = grn_list[forloopcounter] 
                        # print(newobject)
                        instances = [models.RmsGrnupload(
                        updno=newobject[0],
                        serialno=newobject[1],
                        plt = newobject[2],
                        finyear = newobject[3],
                        itemdoc = newobject[4],
                        itemcode = newobject[5],
                        itemdesc = newobject[6],
                        sloc = newobject[8],
                        batch = newobject[7],
                        grgi = newobject[9],
                        headertxt = newobject[10],
                        unloadpt = newobject[11],
                        landbill = newobject[12],
                        glacc = newobject[13],            																		
                        recepient = newobject[14],
                        mvt = newobject[15],
                        mttext = newobject[16], 
                        po = newobject[17],
                        reference = newobject[18],
                        stobin = newobject[19],
                        usname = newobject[20],
                        valtype = newobject[21],
                        vcode = newobject[22],
                        quantity = newobject[23],
                        recqty=newobject[23],
                        unit = newobject[24],
                        pstdate = newobject[25],
                        mandate = newobject[26],
                        sled = newobject[27],
                        amountlc = newobject[28],
                        curr = newobject[29],
                        docdate = newobject[30],
                        entrydate = newobject[31],
                        oun = newobject[32],
                        ounqty = newobject[33],
                        type = newobject[34],
                        avgqty=decimal.Decimal(newobject[35]),
                        packets=int(decimal.Decimal(newobject[23])/decimal.Decimal(newobject[35]))
                        )]
                    
                        RmsGrnupload.objects.bulk_create(instances)
                        RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1],updno=newobject[0],serialno=newobject[1]).delete()
        
                        stbatch_tuples = list(RmsStockBatch.objects.filter(plt=request.session['PLT']).values_list('itemcode','batch'))  
                        check = (newobject[5],newobject[7])
                        if check in stbatch_tuples:
                            new_qty = updatequantity(newobject[2],newobject[3],newobject[23],newobject[5],newobject[7])  
                            RmsStockBatch.objects.filter(batch=newobject[7],plt=newobject[2],itemcode=newobject[5],finyear=newobject[3]).update(recqty=new_qty,avaqty=new_qty)
                        else:
                            Stockinstance = [models.RmsStockBatch(
                            plt = newobject[2],
                            finyear = newobject[3],
                            itemcode = newobject[5],
                            itemdesc = newobject[6],
                            batch = newobject[7],
                            unit = newobject[24],
                            opnqty=0,
                            avaqty=newobject[23],
                            recqty = newobject[23],
                            issuedqty=0,
                            clsqty=0,
                            flag='A'
                                )]
                            RmsStockBatch.objects.bulk_create(Stockinstance)
                        stock_summ_list = list(RmsStockSummary.objects.filter(plt=request.session['PLT']).values_list('itemcode',flat=True))
                        item = newobject[5]
                        if item in stock_summ_list:
                            new_qty = updqtysumm(newobject[2],newobject[3],newobject[23],newobject[5])  
                            RmsStockSummary.objects.filter(plt=newobject[2],itemcode=newobject[5],finyear=newobject[3]).update(recqty=new_qty,avaqty=new_qty)
                        else:
                            Stocksumm = [models.RmsStockSummary(
                            plt = newobject[2],
                            finyear = newobject[3],
                            itemcode = newobject[5],
                            itemdesc = newobject[6],
                            unit = newobject[24],
                            opnqty=0,
                            avaqty=newobject[23],
                            recqty = newobject[23],
                            issuedqty=0,
                            clsqty=0,
                            flag='A'
                                )]
                            RmsStockSummary.objects.bulk_create(Stocksumm)
                    forloopcounter+=1        
            return HttpResponseRedirect("Rms_grnupload",{'role':role})
        except Exception as e:
            messages.info(request,mark_safe(e))
            return HttpResponseRedirect("Rms_grnupload",{'role':role})

    elif request.method == 'POST' and 'deleteupd' in request.POST:
        updno = request.POST.get("number")
        RmsGrnuploadTemp.objects.filter(plt=request.session['PLT'],finyear= request.session['Finyear'],updno=updno).delete()
        cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','grgi','headertxt','unloadpt','landbill','glacc','recepient','mvt','mttext','po','reference',
        'stobin','usname','valtype','vcode','quantity','unit','pstdate','mandate','sled','amountlc','curr','docdate','entrydate','oun','ounqty','type']
        grn_list = RmsGrnuploadTemp.objects.values_list(*cols).filter(plt=request.session['PLT'])
        formset = formset_factory(RmsGrnRep,extra=request.session['rows'])
        form = formset()
        l = zip(list(form), grn_list)
        return render(request,'Rms_grnuploadrep.html',{'l':l,'form':form,'role':role}) 
    else:
        formset = formset_factory(RmsGrnRep)
        form = formset(initial=type_values)
        l = zip(list(form), grn_list)
        return render(request,'Rms_grnuploadrep.html',{'l':l,'form':form,'role':role}) 

def grnfinalupload_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsGrnFinalFilter(session_plt)
    return render(request, 'Rms_grnfinalupload_filter.html',{'form': form,'role':role})

def grnfinalupload(request):
    role = request.session['role'] 
    cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','grgi','headertxt','unloadpt','landbill','glacc','recepient','mvt','mttext','po','reference',
    'stobin','usname','valtype','vcode','quantity','recqty','unit','pstdate','mandate','sled','amountlc','curr','docdate','entrydate','oun','ounqty','type','avgqty','packets','issuedmr']
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['type']) is not None and (request.GET['type'])!="":
        filter_params['type'] = request.GET['type']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['batch']) is not None and (request.GET['batch'])!="":
        filter_params['batch'] = request.GET['batch']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['itemcode']) is not None and (request.GET['itemcode'])!="":
        filter_params['itemcode'] = request.GET['itemcode']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['flag']) is not None and (request.GET['flag'])!="":
        filter_params['flag'] = request.GET['flag']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['sloc']) is not None and (request.GET['sloc'])!="":
        filter_params['sloc'] = request.GET['sloc']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['vcode']) is not None and (request.GET['vcode'])!="":
        filter_params['vcode'] = request.GET['vcode']
    if (request.GET['pstdate__lte']) is not None and (request.GET['pstdate__lte'])!="":
        filter_params['pstdate__lte'] = request.GET['pstdate__lte']
    if (request.GET['pstdate__gte']) is not None and (request.GET['pstdate__gte'])!="":
        filter_params['pstdate__gte'] = request.GET['pstdate__gte']        
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    session_type = list(RmsGrnupload.objects.filter(plt=request.session["PLT"]).values_list("type",flat=True))
    type_values = list()

    for i in session_type:
        type_values.append({'type':i})
    formset = formset_factory(RmsGrnRepFinal)
    if request.method == 'POST' and 'update' in request.POST:
        formset = formset_factory(RmsGrnRepFinal,extra=request.session['rows'])
        form = formset()    
        dataset = request.POST
        type_list = list()
        query = formset(request.POST or None)
        print(query)
        if query.is_valid():
            print('inside')
            q = query.cleaned_data
            q = [i for i in q if i]
            q = filter(None, q)
            for i in q:
                type_list.append(i['type'])
          #  # print(dataset)
            itemcode = RmsGrnupload.objects.values_list('itemcode',flat=True).filter(plt=request.session['PLT'])
            itemdoc = RmsGrnupload.objects.values_list('itemdoc',flat=True).filter(plt=request.session['PLT'])
            vendorcode = RmsGrnupload.objects.values_list('vcode',flat=True).filter(plt=request.session['PLT'])
            values_dict = list(zip([typeval for typeval in type_list], [icode for icode in itemcode], [doc for doc in itemdoc], [v for v in vendorcode]))
            #print(values_dict)
            for i in values_dict:
                RmsGrnupload.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1]).update(type=i[0]) 
            return HttpResponseRedirect("Rms_grnfinalupload_filter",{'role':role})
    elif request.method == 'POST' and 'delete' in request.POST:
        del_list = list()
        query = formset(request.POST or None)
        if query.is_valid():
            q = query.cleaned_data
            q = [i for i in q if i]     
            for i in q:
                del_list.append(i['delete'])
            itemcode = RmsGrnupload.objects.values_list('itemcode',flat=True).filter(plt=request.session['PLT'])
            itemdoc = RmsGrnupload.objects.values_list('itemdoc',flat=True).filter(plt=request.session['PLT'])
            values_dict = list(zip([typeval for typeval in del_list], [icode for icode in itemcode], [doc for doc in itemdoc]))
            for i in values_dict:
                if i[0]==True:
                    RmsGrnupload.objects.filter(plt=request.session['PLT'],itemdoc=i[2],itemcode=i[1]).delete()
            return HttpResponseRedirect("Rms_grnfinalupload_filter",{'role':role})
    elif request.method == 'POST' and 'edit' in request.POST:
        itemcode = request.POST.getlist('code')[0]
        itemdoc = request.POST.getlist('doc')[0]
        #print("code",itemcode)
        #print("doc",itemdoc)
        itemdesc = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('itemdesc',flat=True))
        vcode = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('vcode',flat=True))
        quantity = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('quantity',flat=True))
        sled = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('sled',flat=True))
        #print('Sled:',sled)
        form = RmsGrnuploadEdit(initial={'sled':sled[0],'prevsled':sled[0],'quantity':quantity[0],'itemcode':itemcode,'itemdoc':itemdoc,'itemdesc':itemdesc[0],'vcode':vcode[0]})
        return render(request,"Rms_grneditform.html",{'form':form,'role':role,'itemcode':itemcode,'itemdoc':itemdoc})
    elif request.method == 'POST' and 'editqty' in request.POST:
        #print('Entered')
        itemcode = request.POST.get('itemcode')
        itemdoc = request.POST.get('itemdoc')
        quantity = request.POST.get('quantity')
        reason = request.POST.get('reason')
        newsled = request.POST.get('sled')
        prevsled = request.POST.get('prevsled')
        #print('Prevsled:',prevsled)
        RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemdoc=itemdoc,itemcode=itemcode).update(quantity=quantity,sled=newsled)        
        RmsGrnSlifeUPD.objects.create(plt=request.session['PLT'],itemdoc=itemdoc,itemcode=itemcode,reason=reason,updtby=request.session['Users'],updton=date.today(),newsled=newsled,prevsled=prevsled)
        return HttpResponseRedirect("Rms_grnfinalupload_filter",{'role':role})
    else:
        formset = formset_factory(RmsGrnRepFinal,extra=5)
        form = formset(initial=type_values)
        l = zip(list(form), query)
        return render(request,'Rms_grnfinalupload.html',{'l':l,'form':form,'role':role})


def grneditform(request):
    role = request.session['role'] 
    itemcode = request.GET.get('itemcode')
    itemdoc = request.GET.get('itemdoc')
    #print('ITEMSCODE:',itemcode)
    quantity = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('quantity',flat=True))
    itemdesc = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('itemdesc',flat=True))
    vcode = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('vcode',flat=True))
    sled = list(RmsGrnupload.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],itemcode=itemcode,itemdoc=itemdoc).values_list('sled',flat=True))
    form = RmsGrnuploadEdit(initial={'prevsled':sled[0],'sled':sled[0],'quantity':quantity[0],'itemcode':itemcode,'itemdoc':itemdoc,'itemdesc':itemdesc[0],'vcode':vcode[0]})
    return HttpResponseRedirect('Rms_grneditform')

def updatequantity(plt,fin,temp,itmc,bth):

    qty = list(RmsStockBatch.objects.filter(plt=plt,finyear=fin,itemcode=itmc,batch=bth).values_list('recqty',flat=True))
    temp = decimal.Decimal(temp)
    temp += decimal.Decimal(qty[0])
    return temp 
def updqtysumm(plt,fin,temp,itmc):

    qty = list(RmsStockSummary.objects.filter(plt=plt,finyear=fin,itemcode=itmc).values_list('recqty',flat=True))
    temp = decimal.Decimal(temp)
    temp += decimal.Decimal(qty[0])
    return temp 

def stock_filter_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    cols = ['finyear','itemcode','itemdesc','batch','unit','recqty','avaqty','issuedqty','opnqty','clsqty','flag']
    query = RmsStockBatch.objects.values_list(*cols).filter(plt=session_plt)
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{"StockBatchrepotrts.xls"}"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Table')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = cols
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            somemodel_filter =RmsStockBatch.objects.values_list(*cols).filter(plt=session_plt)
            rows = somemodel_filter
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
    else:
        return render(request,'Rms_stockbatchrep_view.html',{'f':query,'role':role})
def stock_summary_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    cols = ['finyear','itemcode','itemdesc','unit','opnqty','recqty','avaqty','issuedqty','clsqty','flag']
    query = RmsStockSummary.objects.values_list(*cols).filter(plt=session_plt)
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{"StockSummaryrepotrts.xls"}"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Table')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = cols
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            somemodel_filter =RmsStockSummary.objects.values_list(*cols).filter(plt=session_plt)
            rows = somemodel_filter
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
    else:
        return render(request,'Rms_stocksummary_view.html',{'f':query,'role':role})
def issue_filter_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    columns = ['finyear','mrno','itemdoc','itemdesc','itemcode','batch','vcode','issuedqty','unit','issuedby','issuedon','shift']
    query = RmsIssue.objects.values_list(*columns).filter(plt=session_plt)
    if request.method == 'POST' and 'export' in request.POST:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{"issuereports.xls"}"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Table')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            somemodel_filter =RmsIssue.objects.values_list(*columns).filter(plt=session_plt,finyear=request.session['Finyear'])
            rows = somemodel_filter
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
    else:
        return render(request,'Rms_issuerep_view.html',{'f':query,'role':role})

def issuerep(request):
    role = request.session['role'] 
    form = RmsIssueRep() 
    if request.method == 'POST' and 'matissue' in request.POST:
        role = request.session['role'] 
        shift = request.POST.get('shift')
        issuedon = request.POST.get('issuedon')
        remarks = request.POST.get('remarks')
        cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','vcode','quantity','unit','mandate','type']
        issue_data = request.POST.get('itemcode')
        grnmain_items = RmsGrnupload.objects.filter(plt=request.session['PLT']).values_list('itemcode',flat=True)
        issue_items = RmsIssue.objects.filter(plt=request.session['PLT']).values_list('mrno','itemcode')
        data = issue_data.split("\n")
        cleaned_data = list()
        gr_list = list()
        itemcode_list = list()
        quant = OrderedDict()
        for i in range(len(data)):
            cleaned_data.append(data[i].replace("\r", "").replace("\t", " ").replace(",", "").split(' '))
        cleaned_data.pop()
        #print('CD:',cleaned_data)
        
        if len(cleaned_data) == 0:
            messages.info(request,mark_safe('Enter MR vs Item details to issue!'))        
            return render(request,'Rms_issuerep.html',{'form':form,'role':role})
        mrno = cleaned_data[0][0] 
       
        if all([cleaned_data[i][0] == mrno  for i in range(len(cleaned_data))]):
            print('Match')
        else: 
            messages.info(request,mark_safe('Issue for one MRNO at a time'))        
            return render(request,'Rms_issuerep.html',{'form':form,'role':role})
        if all([cleaned_data[i][1] in grnmain_items for i in range(len(cleaned_data))]):
            print('present')
        else: 
            messages.info(request,mark_safe('Items are not available in inventory'))
            return render(request,'Rms_issuerep.html',{'form':form,'role':role})
        if all([(mrno,cleaned_data[i][1]) in issue_items for i in range(len(cleaned_data))]):
            messages.info(request,mark_safe('Items are already issued'))
            return render(request,'Rms_issuerep.html',{'form':form,'role':role})  
        if all([decimal.Decimal((cleaned_data[i][2])) > 0 for i in range(len(cleaned_data))]):
            print('present')
        else: 
            messages.info(request,mark_safe('Issue quantity should be more than 0!'))
            return render(request,'Rms_issuerep.html',{'form':form,'role':role})
        for i in range(len(cleaned_data)):
            gr_list.append(list(RmsGrnupload.objects.filter(itemcode=cleaned_data[i][1],quantity__gt=0,plt=request.session['PLT']).order_by('mandate').values_list(*cols)))
            itemcode_list.append((cleaned_data[i][1],cleaned_data[i][2]))
            quant[cleaned_data[i][1]] = float(cleaned_data[i][2])
        #print(itemcode_list)
        #print(quant)
        requiredgrn = requiredgrns(quant)    
        gr_list = zip(gr_list,itemcode_list,requiredgrn[0].values())
        for key,value in (requiredgrn[1]).items():
            requiredgrn[1][key] = [0 if float(i) < 0 else float(i) for i in value]
        #print("RequiredGRN0:",requiredgrn[0])
        #print('Issuedquant',requiredgrn[3])
        return render(request,'Rms_issuerepfinal.html',{'role':role,'remarks':remarks,'mrno':mrno,'shift':shift,'issuedon':issuedon,'gr_list':gr_list,'requiredgrn':requiredgrn,'issued_quant':simplejson.dumps(requiredgrn[3]).replace(u'&', u'\\u0026'),'required':simplejson.dumps(requiredgrn[0]).replace(u'&', u'\\u0026')})
    return render(request,'Rms_issuerep.html',{'form':form,'role':role})

def issuerepfinal(request):
    role = request.session['role'] 
    if request.method =='POST' and 'issue' in request.POST:
        requiredgrn = request.POST.getlist('items')
        mrno = request.POST.get('mrno')
        shift = request.POST.get('shift')
        remarks = request.POST.get('remarks')
        issuedon = request.POST.get('issuedon')
        requiredgrn = list(filter(lambda a: a != '0', requiredgrn)) #Remove empty strings in list
        changedgrn = request.POST.getlist('chng')
        requiredqty = request.POST.getlist('chngreq')
        #print('requiredqty',requiredqty) 
        # #print('requiredqty',request.POST.ge) 
        changedgrn = list(filter(lambda a: a != '', changedgrn)) #Remove empty strings in list
        #print('RequiredGRN:',requiredgrn)
        posted_items = list()  #POSTED ITEMS all
        changed_items = list()  #Changed items and values
        changed_codes = request.POST.getlist('chngitem')
        changed_batch = request.POST.getlist('batchc')
        #print('changed_batch:',changed_batch)
        for i in requiredgrn:
            posted_items.append(i.split('+'))
        for i in changedgrn:
            changed_items.append(i.split('+'))    
        #print('Original:',posted_items)
        
        changed_items = [item for item in changed_items if item[0] not in changed_batch]
        #print('Changed items:',changed_items)
        new = calculateissue(changed_items)
        #print('Issuing qty:',new[4]) 
        changed = list()
        for key,value in new[4].items():
            changed.append([value[0],key,value[1],value[2]])
        combined = list()
        
        changed_codes = [item for item in changed_codes if item not in changed_batch]
        #print('Changed codes:',changed_codes)
        posted_items = [item for item in posted_items if item[2] not in changed_codes]
        #print('Dropped:',posted_items)
        #print('Changed:',changed)
        posted_items += changed
        #print('Combined:',posted_items)
        #print('MR:',mrno)
        count = 0
        try:
            with transaction.atomic():
                mrsrno =  RmsIssue.objects.filter(plt=request.session['PLT'],mrno=mrno).aggregate(Max('mrsrno'))
                #print('MRSRNO:',mrsrno)
                if mrsrno['mrsrno__max'] == None:
                    mrsrno['mrsrno__max'] = 0
                    #print('SR',mrsrno['mrsrno__max'])
                    
                for i in posted_items:
                    #print(i[0])
                    mrsrno['mrsrno__max']+=1
                    issued_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).values_list('issuedqty',flat=True)
                    ava_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).values_list('avaqty',flat=True)
                    quantitiy_grn = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).values_list('quantity',flat=True)
                    issuedmr = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).values_list('issuedmr',flat=True)
                    mrnoapp = ',' + mrno  
                    RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).update(quantity=quantitiy_grn[0]-decimal.Decimal(i[0]))     
                    #print('Updated main')
                    RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).update(issuedqty=issued_qty[0]+decimal.Decimal(i[0]))
                    #print('Updated summary')
                    RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).update(avaqty=ava_qty[0]-decimal.Decimal(i[0]))
                    #print('Updated summary')
                    issued_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).values_list('issuedqty',flat=True)
                    ava_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).values_list('avaqty',flat=True)
                    RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).update(issuedqty=issued_bqty[0]+decimal.Decimal(i[0]))
                    #print('Updated batch')
                    RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).update(avaqty=ava_bqty[0]-decimal.Decimal(i[0]))
                    #print('Updated batch')
                    RmsIssue.objects.create(plt=request.session['PLT'],mrsrno=mrsrno['mrsrno__max'],mrno=mrno,finyear=request.session['Finyear'],itemcode=i[2],batch=i[3],itemdoc=i[1],issuedqty=i[0],shift=shift,issuedon=issuedon,issuedby=request.session['Name'],remarks=remarks)
                    issue_tuples = list(RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('mrno','itemcode'))  
                    check = (mrno,i[2])
                    #print('Issue_Tuples:',issue_tuples)
                    #print('Check:',check)
                    if check in issue_tuples:
                        #print("entered")
                        totissue = RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).values_list('issuedqty',flat=True)
                        pendingqty = RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).values_list('remqty',flat=True)
                        totalrequired = RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).values_list('reqqty',flat=True)
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).update(issuedqty=decimal.Decimal(totissue[0])+decimal.Decimal(i[0]))
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).update(remqty=pendingqty[0]-decimal.Decimal(i[0]))   
                    else:
                        #print(requiredqty[count])
                        #print('else')
                        remqty = decimal.Decimal(requiredqty[count]) - decimal.Decimal(i[0])
                        RmsIssueSummary.objects.create(plt=request.session['PLT'],mrno=mrno,finyear=request.session['Finyear'],itemcode=i[2],issuedqty=decimal.Decimal(i[0]),reqqty=requiredqty[count],remqty=remqty)
                    #print(issuedmr[0])
                    if mrno not in issuedmr[0]:
                        #print('mriss')
                        RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).update(issuedmr=issuedmr[0]+','+mrno)        
                    count+=1
            return HttpResponseRedirect('Rms_issuerep',{'role':role},messages.info(request,mark_safe('Items issued successfully')))
        except Exception as e:
            return HttpResponseRedirect('Rms_issuerep',{'role':role},messages.info(request,mark_safe(e)))
def requiredgrns(quant):
    highlighted = defaultdict(list)
    batch = list()
    changed_values = OrderedDict()
    issuing_qty = OrderedDict()
    issued_values = OrderedDict()
    for key,value in quant.items():
        grns = list(RmsGrnupload.objects.filter(itemcode=key,quantity__gt=0,type="Regular").order_by('mandate').values_list('itemdoc','quantity','batch'))
        values = list()
        for i in range(len(grns)):
            if value>0:
                highlighted[key].append(grns[i][0])
                batch.append(grns[i][2])
                rem = max(0,decimal.Decimal(grns[i][1])- decimal.Decimal(value))
                value =  decimal.Decimal(value) - decimal.Decimal(grns[i][1])
                values.append(rem)
                issuing_qty[grns[i][0]+'-'+key] = decimal.Decimal(grns[i][1])-rem
                changed_values[grns[i][0]] = (decimal.Decimal(grns[i][1])-rem,key,grns[i][2])
        issued_values[key] = values
    issued_values = dict(issued_values)
    issuing_qty = dict(issuing_qty)
    changed_values = dict(changed_values)
    return highlighted,issued_values,batch,issuing_qty,changed_values               

def calculateissue(changed_items):
    # cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','vcode','quantity','unit','mandate']
    cleaned_data = changed_items
    quant = OrderedDict()
    for i in range(len(cleaned_data)):
        quant[cleaned_data[i][0]] = float(cleaned_data[i][1])
    #print(quant)
    requiredgrn = requiredgrns(quant)    
    return requiredgrn


def revinterface(request):
    role = request.session['role'] 
    form = RmsRevinterface()
    if request.method=='POST':
        form = RmsRevinterface(request.POST)
        revinterface_view(request)
    return render(request,'Rms_revinterface.html',{'form':form,'role':role})

def revinterface_view(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    columns = ['mrsrno','mrno','itemdoc','itemdesc','itemcode','batch','vcode','issuedqty','unit','issuedby','issuedon','shift']
    filter_params = {'plt': session_plt}    
    query = RmsIssue.objects.values_list(*columns).filter(plt=session_plt)
    if (request.GET['mrno']) is not None and (request.GET['mrno'])!="":
        filter_params['mrno'] = request.GET['mrno']
        query = RmsIssue.objects.values_list(*columns).filter(**filter_params)
    if (request.GET['itemcode']) is not None and (request.GET['itemcode'])!="":
        filter_params['itemcode'] = request.GET['itemcode']
        query = RmsIssue.objects.values_list(*columns).filter(**filter_params)
    if request.method=='POST' and 'reverse' in request.POST:
        reversal = list()
        reversal = (request.POST.getlist('values'))
        #print(reversal)
        posted_items = [ i.split(',') for i in reversal] 
        #print("Posted items:",posted_items)
        try:
            with transaction.atomic():
                for i in posted_items:
                    if len(i) > 1:
                        ##print('hello')
                        issued_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3]).values_list('issuedqty',flat=True)
                        ava_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3]).values_list('avaqty',flat=True)
                        quantitiy_grn = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[3],itemdoc=i[2]).values_list('quantity',flat=True)
                        issuedmr = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[3],itemdoc=i[2]).values_list('issuedmr',flat=True)     
                        RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[3],itemdoc=i[2]).update(quantity=quantitiy_grn[0]+decimal.Decimal(i[4]))
                        #print('GRNMain quantity updated')
                        RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3]).update(issuedqty=issued_qty[0]-decimal.Decimal(i[4]))
                        #print('Summary: issuedqty,avaqty,quantity_grn,issuedmr',issued_qty[0],ava_qty[0],quantitiy_grn[0],issuedmr[0])
                        #print('Updated summary')
                        RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3]).update(avaqty=ava_qty[0]+decimal.Decimal(i[4]))
                        ##print('Updated summary')
                        issued_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[3],batch=i[5]).values_list('issuedqty',flat=True)
                        ava_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[3],batch=i[5]).values_list('avaqty',flat=True)
                        RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[3],batch=i[5]).update(issuedqty=issued_bqty[0]-decimal.Decimal(i[4]))
                        #print('Updated batch')
                        RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[3],batch=i[5]).update(avaqty=ava_bqty[0]+decimal.Decimal(i[4]))
                        #print('Batch: issuedqty,avaqty',issued_bqty[0],ava_bqty[0])            
                        issuedon = RmsIssue.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],mrsrno=i[0],finyear=request.session['Finyear']).values_list('issuedon',flat=True)
                        #print(issuedon)
                        #print('Issuedon:',issuedon[0])
                        RmsReversal.objects.create(plt=request.session['PLT'],itemcode=i[3],batch=i[5],mrsrno=i[0],mrno=i[1],finyear=request.session['Finyear'],itemdoc=i[2],issuedqty=decimal.Decimal(i[4]),unit=i[7],issuedby=i[8],issuedon=issuedon[0],vcode=i[6],shift=i[9],reversedby=request.session['Users'])
                        #print('Reversal entered')
                        RmsIssue.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],mrsrno=i[0],finyear=request.session['Finyear']).delete()
                        #print('Deleted from issue')
                        issuesumqty = RmsIssueSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).values_list("issuedqty",flat=True)
                        remsumqty = RmsIssueSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).values_list("remqty",flat=True)
                        items = RmsIssue.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).values_list("itemcode",flat=True)
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],mrno=i[1],finyear=request.session['Finyear']).values_list("itemcode",flat=True)
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).update(remqty=remsumqty[0]+decimal.Decimal(i[4]))
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).update(issuedqty=issuesumqty[0]-decimal.Decimal(i[4]))
                        if i[3] not in items:
                            RmsIssueSummary.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],finyear=request.session['Finyear']).delete()
                        itemdocs_issue = RmsIssue.objects.filter(plt=request.session['PLT'],itemcode=i[3],mrno=i[1],mrsrno=i[0],finyear=request.session['Finyear']).values_list('itemdoc',flat=True)
                        #print(itemdocs_issue)
                        if i[2] not in itemdocs_issue:
                            #print(i[2],itemdocs_issue)
                            #print(issuedmr[0].replace(','+i[1],''))
                            RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[3],itemdoc=i[2]).update(issuedmr=issuedmr[0].replace(','+i[1],''))
                #return render(request,'Rms_revinterface_view.html',{'f':query,'role':role})
                return HttpResponseRedirect('Rms_revinterface',messages.info(request,mark_safe('Reversed')),{'f':query,'role':role})
        except Exception as e:
            return HttpResponseRedirect('Rms_revinterface',messages.info(request,mark_safe(e)),{'role':role})
    return render(request,'Rms_revinterface_view.html',{'f':query,'role':role})

def pending_issue(request):    
    role = request.session['role'] 
    form = RmsPendingIssueRep() 
    if request.method == 'POST' and 'matissue' in request.POST:
        gr_list = list()
        itemcode_list = list()
        cleaned_data = list()
        quant = OrderedDict()
        cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','vcode','quantity','unit','mandate','type']
        shift = request.POST.get('shift')        
        issuedon = request.POST.get('issuedon')
        remarks = request.POST.get('remarks')
        itemcode = request.POST.get('itemcode')
        mrno = request.POST.get('mrno')
        filter_params = {'plt': request.session['PLT'],'finyear':request.session['Finyear'],'mrno':mrno}
        if len(itemcode)>0:
            filter_params['itemcode'] = itemcode
        #print(filter_params)
        summ_items =  RmsIssueSummary.objects.values_list('itemcode','remqty','reqqty','issuedqty').filter(**filter_params)
        #print(summ_items)
        if len(summ_items) == 0:
            messages.info(request,mark_safe('Items are not issued against MRNO:'+mrno+'!'))
            return render(request,'Rms_pendingissue.html',{'form':form,'role':role})
        totalreq = list()
        for i in summ_items:
            totalreq.append(i[2])
            cleaned_data.append([mrno,i[0],i[1],i[3]])
        #print(cleaned_data)
        #print('CD:',cleaned_data)
        for i in range(len(cleaned_data)):
            gr_list.append(list(RmsGrnupload.objects.filter(itemcode=cleaned_data[i][1],quantity__gt=0,plt=request.session['PLT']).order_by('mandate').values_list(*cols)))
            itemcode_list.append((cleaned_data[i][1],cleaned_data[i][2],cleaned_data[i][3]))
            quant[cleaned_data[i][1]] = float(cleaned_data[i][2])
        requiredgrn = requiredgrns(quant)    
        gr_list1 = zip(gr_list,itemcode_list,totalreq)
        print(requiredgrn[0].values())
        for key,value in (requiredgrn[1]).items():
            requiredgrn[1][key] = [0 if float(i) < 0 else float(i) for i in value]
        # return render(request,'Rms_issuerepfinal.html',{'remarks':remarks,'mrno':mrno,'shift':shift,'issuedon':issuedon,'gr_list':gr_list,'requiredgrn':requiredgrn,'issued_quant':simplejson.dumps(requiredgrn[3]).replace(u'&', u'\\u0026'),'required':simplejson.dumps(requiredgrn[0]).replace(u'&', u'\\u0026')})
        return render(request,'Rms_pendingissuefinal.html',{'role':role,'remarks':remarks,'mrno':mrno,'shift':shift,'issuedon':issuedon,'gr_list':gr_list1,'requiredgrn':requiredgrn,'issued_quant':simplejson.dumps(requiredgrn[3]).replace(u'&', u'\\u0026'),'required':simplejson.dumps(requiredgrn[0]).replace(u'&', u'\\u0026'),'z':requiredgrn[0].values()})
    return render(request,'Rms_pendingissue.html',{'form':form,'role':role})

def pending_issuefinal(request):
    role = request.session['role'] 
    if request.method =='POST' and 'issue' in request.POST:
        #print('Inside pending')
        requiredgrn = request.POST.getlist('items')
        mrno = request.POST.get('mrno')
        shift = request.POST.get('shift')
        remarks = request.POST.get('remarks')
        issuedon = request.POST.get('issuedon')
        requiredgrn = list(filter(lambda a: a != '0', requiredgrn)) #Remove empty strings in list
        changedgrn = request.POST.getlist('chng')
        requiredqty = request.POST.getlist('chngreq')
        #print('requiredqty',requiredqty) 
        # #print('requiredqty',request.POST.ge) 
        changedgrn = list(filter(lambda a: a != '', changedgrn)) #Remove empty strings in list
        #print('RequiredGRN:',requiredgrn)
        posted_items = list()  #POSTED ITEMS all
        changed_items = list()  #Changed items and values
        changed_codes = request.POST.getlist('chngitem')  #Changed item codes
        for i in requiredgrn:
            posted_items.append(i.split('+'))
        for i in changedgrn:
            changed_items.append(i.split('+'))    
        #print('Original:',posted_items)
        new = calculateissue(changed_items)
        #print('Issuing qty:',new[4]) 
        changed = list()
        for key,value in new[4].items():
            changed.append([value[0],key,value[1],value[2]])
        combined = list()
        #print('Changed codes:',changed_codes)
        posted_items = [item for item in posted_items if item[2] not in changed_codes]
        #print('Dropped:',posted_items)
        #print('Changed:',changed)
        posted_items += changed
        #print('Combined:',posted_items)
        #print('MR:',mrno)
        count = 0
        try:
            with transaction.atomic():
                mrsrno =  RmsIssue.objects.filter(plt=request.session['PLT'],mrno=mrno).aggregate(Max('mrsrno'))
                #print('MRSRNO:',mrsrno)
                if mrsrno['mrsrno__max'] == None:
                    mrsrno['mrsrno__max'] = 0
                    #print('SR',mrsrno['mrsrno__max'])
                    
                for i in posted_items:
                    #print(i[0])
                    mrsrno['mrsrno__max']+=1
                    issued_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).values_list('issuedqty',flat=True)
                    ava_qty = RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).values_list('avaqty',flat=True)
                    quantitiy_grn = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).values_list('quantity',flat=True)
                    issuedmr = RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).values_list('issuedmr',flat=True)
                    mrnoapp = ',' + mrno  
                    RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).update(quantity=quantitiy_grn[0]-decimal.Decimal(i[0]))     
                    #print('Updated main')
                    RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).update(issuedqty=issued_qty[0]+decimal.Decimal(i[0]))
                    #print('Updated summary')
                    RmsStockSummary.objects.filter(plt=request.session['PLT'],itemcode=i[2]).update(avaqty=ava_qty[0]-decimal.Decimal(i[0]))
                    #print('Updated summary')
                    issued_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).values_list('issuedqty',flat=True)
                    ava_bqty = RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).values_list('avaqty',flat=True)
                    RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).update(issuedqty=issued_bqty[0]+decimal.Decimal(i[0]))
                    #print('Updated batch')
                    RmsStockBatch.objects.filter(plt=request.session['PLT'],itemcode=i[2],batch=i[3]).update(avaqty=ava_bqty[0]-decimal.Decimal(i[0]))
                    #print('Updated batch')
                    RmsIssue.objects.create(plt=request.session['PLT'],mrsrno=mrsrno['mrsrno__max'],mrno=mrno,finyear=request.session['Finyear'],itemcode=i[2],batch=i[3],itemdoc=i[1],issuedqty=i[0],shift=shift,issuedon=issuedon,issuedby=request.session['Name'],remarks=remarks)
                    issue_tuples = list(RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('mrno','itemcode'))  
                    check = (mrno,i[2])
                    #print(issue_tuples)
                    #print(check)
                    if check in issue_tuples:
                        #print("entered")
                        totissue = RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).values_list('issuedqty',flat=True)
                        pendingqty = RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).values_list('remqty',flat=True)
                        #print("Pending:",pendingqty)
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).update(issuedqty=decimal.Decimal(totissue[0])+decimal.Decimal(i[0]))
                        RmsIssueSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear'],mrno=mrno,itemcode=i[2]).update(remqty=decimal.Decimal(pendingqty[0])-decimal.Decimal(i[0]))
                    else:
                        remqty = decimal.Decimal(requiredqty[count]) - decimal.Decimal(i[0])
                        RmsIssueSummary.objects.create(plt=request.session['PLT'],mrno=mrno,finyear=request.session['Finyear'],itemcode=i[2],issuedqty=decimal.Decimal(i[0]),reqqty=requiredqty[count],remqty=remqty)
                    if mrno not in issuedmr[0]:
                        RmsGrnupload.objects.filter(plt=request.session['PLT'],itemcode=i[2],itemdoc=i[1]).update(issuedmr=issuedmr[0]+','+mrno)        
                    count+=1
                return HttpResponseRedirect('Rms_pendingissue',{'role':role},messages.info(request,mark_safe('Items reissued successfully')))
        except Exception as e:
            return HttpResponseRedirect('Rms_pendingissue',{'role':role},messages.info(request,mark_safe(e)))

def grnfinaluser_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsGrnFinalFilter(session_plt)
    return render(request, 'Rms_grnfinaluser_filter.html',{'form': form,'role':role})

def grnfinaluser_view(request):
    role = request.session['role'] 
    cols = ['updno','serialno','itemdoc','itemcode','itemdesc','batch','sloc','grgi','headertxt','unloadpt','landbill','glacc','recepient','mvt','mttext','po','reference',
    'stobin','usname','valtype','vcode','quantity','recqty','unit','pstdate','mandate','sled','amountlc','curr','docdate','entrydate','oun','ounqty','type','avgqty','packets']
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['batch']) is not None and (request.GET['batch'])!="":
        filter_params['batch'] = request.GET['batch']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['itemcode']) is not None and (request.GET['itemcode'])!="":
        filter_params['itemcode'] = request.GET['itemcode']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['flag']) is not None and (request.GET['flag'])!="":
        filter_params['flag'] = request.GET['flag']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['sloc']) is not None and (request.GET['sloc'])!="":
        filter_params['sloc'] = request.GET['sloc']
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['vcode']) is not None and (request.GET['vcode'])!="":
        filter_params['vcode'] = request.GET['vcode']
    if (request.GET['pstdate__lte']) is not None and (request.GET['pstdate__lte'])!="":
        filter_params['pstdate__lte'] = request.GET['pstdate__lte']
    if (request.GET['pstdate__gte']) is not None and (request.GET['pstdate__gte'])!="":
        filter_params['pstdate__gte'] = request.GET['pstdate__gte']        
        query = RmsGrnupload.objects.values_list(*cols).filter(**filter_params)
    return render(request,'Rms_grnfinaluser_view.html',{'f':query,'role':role})

def issuesumm_filter(request):
    role = request.session['role'] 
    session_plt = request.session['PLT']
    form = RmsIssueSummFilter(session_plt)
    return render(request,'Rms_issuesumm_filter.html',{'form':form,'role':role})

def issuesumm_view(request):
    role = request.session['role'] 
    cols = ['finyear','mrno','itemcode','itemdesc','issuedon','unit','issuedby','reqqty','remqty']
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsIssueSummary.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['mrno']) is not None and (request.GET['mrno'])!="":
        filter_params['mrno'] = request.GET['mrno']
        query = RmsIssueSummary.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['itemcode']) is not None and (request.GET['itemcode'])!="":
        filter_params['itemcode'] = request.GET['itemcode']
        query = RmsIssueSummary.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['issuedon']) is not None and (request.GET['issuedon'])!="":
        filter_params['issuedon'] = request.GET['issuedon']
        query = RmsIssueSummary.objects.values_list(*cols).filter(**filter_params)
    #print(filter_params)
    kwar = {k: v for k, v in filter_params.items() if v}
    #print(kwar)
    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{"IssueSummaryreports.xls"}"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Table')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = cols
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
            font_style = xlwt.XFStyle()
            somemodel_filter = query
            rows = somemodel_filter
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response
    else:
        return render(request,'Rms_issuesumm_view.html',{'f':query,'role':role})

def printdetails(request):
    role = request.session['role']
    session_plt = request.session['PLT']
    form = RmsPrintsheet(session_plt)
    if request.method == "POST":
        form = RmsPrintsheet(request.POST,session_plt)
        if form.is_valid:
            printsheet(request)    
    return render(request,'Rms_printdetails.html',{'form':form,'role':role})

def printsheet(request):
    plant = request.GET['planttype']
    issuedon = request.GET['issuedon']
    shift = request.GET['shift']
    
    print(plant)
    cols = ['mrno','itemcode','issuedqty','itemdoc','batch']
    session_plt = request.session['PLT']
    filter_params = {'plt': session_plt}
    query = RmsIssue.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['mrno']) is not None and (request.GET['mrno'])!="":
        filter_params['mrno'] = request.GET['mrno']
        query = RmsIssue.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['shift']) is not None and (request.GET['shift'])!="":
        filter_params['shift'] = request.GET['shift']
        query =RmsIssue.objects.values_list(*cols).filter(**filter_params)
    if (request.GET['issuedon']) is not None and (request.GET['issuedon'])!="":
        filter_params['issuedon'] = request.GET['issuedon']
        query = list(RmsIssue.objects.values_list(*cols).filter(**filter_params))
    issue_items = query
    extra = 29- len(issue_items)
    issue_len = len(issue_items)
    if(len(issue_items)>28):
        extra = 0
    return render(request,'Rms_printsheet.html',{'extra':extra,'issue_len':issue_len,'issueitems':issue_items,'planttype':plant,'shift':shift,'issuedon':issuedon})

    from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)