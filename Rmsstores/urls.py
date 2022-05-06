from django.contrib import admin
from django.urls import path
from Rmsstores import views as v2
from apps_aodms import views as v1
from Rmsstores import charts as c2
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from ajax_select import urls as ajax_select_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', v2.rms_store),
    path('Rms_groupmast', v2.group_master),
    path('Rms_groupmastrep',v2.grp_filter),
    path('Rms_groupmastrep_view',v2.grp_filter_view),
    
    path('Rms_unitmast', v2.unit_master),


    path('Rms_vendormast', v2.vendor_master),
    path('Rms_vendormastrep',v2.ven_filter),
    path('Rms_vendormastrep_view',v2.ven_filter_view),

    path('Rms_Itemmast', v2.item_master),
    path('Rms_itemmastrep',v2.item_filter),
    path('Rms_itemmastrep_view',v2.item_filter_view),
    path('autocomplete',v2.autocomplete,name= 'autocomplete'),
    path('Rms_shelfmast', v2.shelf_master),
    path('Rms_shelfmasttemp', v2.shelfmasttemp,name="Rms_shelfmasttemp"),
    
    path('Rms_shelfmastrep', v2.shelfmastrep,name="shelfmastrep"),
    path('Rms_shelfmastrep_view', v2.shelfmastrep_view,name="shelfmastrep_view"),
    
    path('Rms_grnupload',v2.grnupload),
    path('Rms_grnfinalupload',v2.grnfinalupload,name='Rms_grnfinalupload'),
    path('Rms_grnfinalupload_filter',v2.grnfinalupload_filter),

    path('Rms_grnuploadrep',v2.grnuploadrep,name='grnuploadrep'),
    path('Rms_grneditform',v2.grneditform,name='Rms_grneditform'),

    path('Rms_stockbatchrep_view', v2.stock_filter_view,name="stockbatchrep_view"),
    path('Rms_stocksummary_view', v2.stock_summary_view),

    path('Rms_issuerep', v2.issuerep,name="issuerep"),
    path('Rms_issuerepfinal', v2.issuerepfinal,name="issuerepfinal"),
    path('Rms_issuerep_view', v2.issue_filter_view,name="issuerep_view"),

    path('Rms_pendingissue', v2.pending_issue,name="pendingissue"),
    path('Rms_pendingissuefinal', v2.pending_issuefinal),

    #path('updqty',v2.updqty,name='updqty'),
    path('Rms_revinterface', v2.revinterface,name="revinterface"),
    path('Rms_revinterface_view', v2.revinterface_view,name="revinterface_view"),

    path('logout',v1.logout),
    path('Rms_grnfinaluser_view',v2.grnfinaluser_view,name='Rms_grnfinaluser_view'),
    path('Rms_grnfinaluser_filter',v2.grnfinaluser_filter,name='Rms_grnfinaluser_filter'),
    
    path('Rms_issuesumm_filter', v2.issuesumm_filter,name="issuesumm_filter"),
    path('Rms_issuesumm_view', v2.issuesumm_view,name="issuesumm_view"),
    
    path('Rms_charts',c2.dashboard,name='Rms_charts'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('Rms_dash',c2.dash1),
    
    path('Rms_printsheet',v2.printsheet),
    path('Rms_printdetails',v2.printdetails)



    ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

