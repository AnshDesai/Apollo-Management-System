import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from django.shortcuts import render,redirect
from django.urls import path
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe 
import pandas as pd
from datetime import date
from Rmsstores import models
from .forms import *
import json
import decimal
from datetime import datetime
from collections import Counter,OrderedDict
from django_plotly_dash import DjangoDash
import json
from dash.dependencies import Input, Output
@csrf_exempt
def dashboard(request):

    form = groupschart(request.session['PLT'])
    today = datetime.today()
    grnmodel = list(RmsStockSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('itemcode','recqty'))    
    count_items = dict()
    for i in range(len(grnmodel)):
        count_items[grnmodel[i][0]] = grnmodel[i][1]
    timeseries = list(RmsIssue.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('itemcode','issuedon','issuedqty'))
    issue_items = dict()    
    for i in range(len(timeseries)):
        issue_items[timeseries[i][1]] = timeseries[i][2]
    issueditems = Counter([i[0] for i in timeseries])
    print('Issueitems',issue_items)
    print('Issueitems',issueditems)
    template = 'Rms_charts.html'
    if request.method=='POST':
        request_getdata = request.POST.get('data', None)
        groups  = list(RmsItemmast.objects.filter(plt=request.session['PLT'],groupno=request_getdata).values_list('itemcode',flat=True).distinct())
        grnmodel = list(RmsStockSummary.objects.filter(plt=request.session['PLT'],finyear=request.session['Finyear']).values_list('itemcode','recqty'))
        grnmodel = [i for i in grnmodel if i[0] in groups]
        new_items = dict()
        for i in range(len(grnmodel)):
            new_items[grnmodel[i][0]] = grnmodel[i][1]
        color ="rgb(53,135,164,0.7)"
        barcolor =[]
        for i in range(len(new_items)):
            barcolor.append(color)
        chartdata = {
            'labels':list(new_items.keys()),
            'datasets':[{
                'label': "Amount in KG",
                "data": list(new_items.values()),
                "backgroundColor":barcolor
            }]
        }
        data_dict = {
            "chartdata":chartdata
        }
        return JsonResponse(data=data_dict,safe=False)
    if request.is_ajax():
        color ="rgb(53,135,164,0.7)"
        barcolor =[]
        for i in range(len(count_items)):
            barcolor.append(color)
        chartdata = {
            'labels':list(count_items.keys()),
            'datasets':[{
                'label': "Amount in KG",
                "data": list(count_items.values()),
                "backgroundColor":barcolor
            }]
        }
        
        barcolor =[]
        for i in range(len(issue_items)):
            barcolor.append(color)
        time = {
            'labels':list(issue_items.keys()),
            'datasets':[{
                'label': list(issueditems),
                "data": list(issue_items.values()),
                "backgroundColor":barcolor
            }]
        }
        data_dict = {
            "timeseries":time,
            "chartdata":chartdata
        }
        return JsonResponse(data=data_dict,safe=False)
    return render(request,template,{'form':form})
app = DjangoDash('example')

def dash1(request):
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

    items = list(RmsStockSummary.objects.filter(plt=request.session['PLT']).values_list('itemcode',flat=True).order_by('groupno'))
    recqty = list(RmsStockSummary.objects.filter(plt=request.session['PLT']).values_list('recqty',flat=True).order_by('groupno'))
    groups = list(RmsStockSummary.objects.filter(plt=request.session['PLT']).values_list('groupno',flat=True).order_by('groupno'))
    
    items1 = list(RmsStockBatch.objects.filter(plt=request.session['PLT']).values_list('itemcode',flat=True).order_by('batch'))
    recqty1 = list(RmsStockBatch.objects.filter(plt=request.session['PLT']).values_list('recqty',flat=True).order_by('batch'))
    batch1 = list(RmsStockBatch.objects.filter(plt=request.session['PLT']).values_list('batch',flat=True).order_by('batch'))
    df1 = pd.DataFrame({
        "Items": items1,
        "Quantity": recqty1,
        "Batch":batch1
    })

    df = pd.DataFrame({
        "Items": items,
        "Quantity": recqty,
        "Groups":groups
    })
    fig = px.scatter(df, x="Items", y="Quantity", color="Groups")    
    fig.update_layout(clickmode='event+select')
    fig.update_traces(marker_size=20)

    fig1 = px.bar(df1, x="Items", y="Quantity", color="Batch")    
    fig1.update_layout(clickmode='event+select')

    app.layout = html.Div(children=[
    html.H3('Items in inventory per group'),
            dcc.Graph(
            id='basic-interactions',
            figure=fig, config= {'displaylogo': False}), 
            html.H3('Items in inventory per batch'),
            dcc.Graph(
            id='graph2',
            figure=fig1, config= {'displaylogo': False}
        )
])
           
    app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
    })
    role = request.session['role']
    return render(request,'Rms_dash.html',{'role':role})

@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)
@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)
@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)
@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)
