from django import forms  
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Field
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime
class RmsVendormastForm(forms.ModelForm):  
    class Meta:  
        model = RmsVendormast  
        fields = ('plt','vcode',)
    def __init__(self, *args, **kwargs):
        super(RmsVendormastForm, self).__init__(*args, **kwargs)
        self.fields['vcode'].label = "Vendor Code"

class RmsGroupmastForm(forms.ModelForm):  
    class Meta:  
        model = RmsGroupmast  
        fields = ('plt','groupno',)
    def __init__(self, *args, **kwargs):
        super(RmsGroupmastForm, self).__init__(*args, **kwargs)
        self.fields['groupno'].label = "Group No."

class RmsUnitmastForm(forms.ModelForm):  
    class Meta:  
        model = RmsUnitmast  
        fields = ('plt','unit','convamount','convunit','flag','updtby','updton')
    def __init__(self,*args, **kwargs):
        super(RmsUnitmastForm, self).__init__(*args, **kwargs)
        self.fields['unit'].label = "Unit"
          
class RmsItemmastForm(forms.ModelForm):  
    class Meta:  
        model = RmsItemmast  
        fields = ('plt','itemcode','itemdesc','groupno','unit',)
    
class RmsGroupRep(forms.ModelForm):
    flag = forms.ModelChoiceField(required=False,queryset=RmsGroupmast.objects.values_list('flag',flat=True).distinct())
    class Meta:
        model = RmsGroupmast
        fields = ['flag']
    def __init__(self, plt, *args, **kwargs):
        super(RmsGroupRep, self).__init__(*args, **kwargs)
        self.fields['flag'].queryset = RmsGroupmast.objects.values_list('flag',flat=True).distinct().filter(plt=plt)
        self.fields['flag'].label = "Flag"

class RmsVendorRep(forms.ModelForm):
    flag = forms.ModelChoiceField(required=False,queryset=RmsVendormast.objects.values_list('flag',flat=True).distinct())
    class Meta:
        model = RmsVendormast
        fields = ['flag']
    def __init__(self, plt, *args, **kwargs):
        super(RmsVendorRep, self).__init__(*args, **kwargs)
        self.fields['flag'].queryset = RmsVendormast.objects.values_list('flag',flat=True).distinct().filter(plt=plt)
        self.fields['flag'].label = "Flag"

class RmsItemRep(forms.ModelForm):
    itemcode = forms.ModelChoiceField(required=False,queryset=RmsItemmast.objects.values_list('itemcode',flat=True).distinct())
    groupno= forms.ModelChoiceField(required=False,queryset=RmsItemmast.objects.values_list('groupno',flat=True).distinct())
    flag = forms.ModelChoiceField(required=False,queryset=RmsItemmast.objects.values_list('flag',flat=True).distinct())
    class Meta:
        model = RmsItemmast
        fields = ['flag','groupno','itemcode']
    
    def __init__(self, plt, *args, **kwargs):
        super(RmsItemRep, self).__init__(*args, **kwargs)
        self.fields['flag'].queryset = RmsItemmast.objects.values_list('flag',flat=True).distinct().filter(plt=plt)

        self.fields['groupno'].queryset = RmsItemmast.objects.values_list('groupno',flat=True).distinct().filter(plt=plt)
        self.fields['itemcode'].queryset = RmsItemmast.objects.values_list('itemcode',flat=True).distinct().filter(plt=plt)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        

class RmsShelfmastForm(forms.ModelForm):  
    itemcode = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    groupno = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    itemdesc = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    remarks = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    reason = forms.CharField(widget=forms.TextInput())
    class Meta:  
        model = RmsShelfmast  
        fields = ('plt','itemcode','itemdesc','groupno','shelflife','remarks','updton')

class RmsGrnRep(forms.ModelForm):
    type = forms.ChoiceField(widget=forms.Select(attrs={'style': 'font-size:11px; width:88px; height:30px'}),choices = TYPE_CHOICES, required=True,label=False)
    delete = forms.BooleanField(label='',required=False)
    avgqty = forms.DecimalField(widget=forms.NumberInput(attrs={'style':'font-size:11px; width:88px; height:30px; required:true'}),required=False,label=False,min_value=1)
    class Meta:
        model = RmsGrnuploadTemp
        fields = ('type','delete','avgqty')
    def __init__(self, *args, **kwargs):
        super(RmsGrnRep, self).__init__(*args, **kwargs)
        self.layout = Layout(Field('delete', onkeyup="displaydel()",css_class='check'))
TYPE_CHOICES = (
    ("Regular", ("Regular")),
    ("Trial", ("Trial")),
    ("Parked", ("Parked")),
)
class RmsGrnRepFinal(forms.ModelForm):
    type = forms.ChoiceField(widget=forms.Select(attrs={'style': 'font-size:10px; width:88px; height:20px; text-align:center; border: 2px;border-radius: 5px;'}),choices = TYPE_CHOICES, required=True,label=False)
    delete = forms.BooleanField(label='',required=False)
    class Meta:
        model = RmsGrnupload
        fields = ('type','delete',)
    def __init__(self, *args, **kwargs):
        super(RmsGrnRepFinal, self).__init__(*args, **kwargs)
        self.layout = Layout(Field('delete', onkeyup="displaydel()",css_class='check'))
        
class RmsGrnuploadRep(forms.ModelForm):
    itemdoc = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    itemcode = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    itemdesc = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    vcode = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    quantity = forms.CharField()
    class Meta:
        model = RmsGrnupload
        fields = ('itemcode','itemdesc','itemcode','quantity','vcode',)
SHIFT_CHOICES = (
    ("A", ("A")),
    ("B", ("B")),
    ("C", ("C")),
    ("G", ("G"))
)
class RmsGrnuploadEdit(forms.ModelForm):
    itemdoc = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    itemcode = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    itemdesc = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    vcode = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    quantity = forms.DecimalField(min_value=0)
    sled = forms.DateField(widget=forms.TextInput(attrs={'type': 'date','style':'max-height: 2em'}))
    reason = forms.CharField(max_length=100,required=False,initial='NA')
    prevsled = forms.DateField()
    class Meta:
        model = RmsGrnupload
        fields = ('itemcode','itemdesc','itemcode','quantity','vcode',)
class RmsIssueRep(forms.ModelForm):
    shift = forms.ChoiceField(widget=forms.Select(attrs={'style': 'width:auto'}),choices = SHIFT_CHOICES, required=True)
    issuedon = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),initial = datetime.date.today)
    remarks = forms.CharField(initial='NA',widget=forms.TextInput(attrs={'style': 'width:auto'}))
    class Meta:
        model = RmsIssue
        fields = '__all__'
class RmsGrnFinalFilter(forms.ModelForm):
    itemcode = forms.CharField(required=False,widget=forms.TextInput(attrs={'style':'max-height: 2em'}))
    itemdoc = forms.CharField(required=False,widget=forms.TextInput(attrs={'style':'max-height: 2em'}))
    vcode = forms.CharField(required=False,widget=forms.TextInput(attrs={'style':'max-height: 2em'}))
    batch= forms.CharField(required=False,widget=forms.TextInput(attrs={'style':'max-height: 2em'}))
    pstdate__lte = forms.DateField(widget=forms.TextInput(attrs={'type': 'date','style':'max-height: 2em'}),label='To Pstdate:',required=False)
    pstdate__gte = forms.DateField(widget=forms.TextInput(attrs={'type': 'date','style':'max-height: 2em'}),label='From Pstdate:',required=False)             
    sloc = forms.CharField(required=False,widget=forms.TextInput(attrs={'style':'max-height: 2em'}))
    type = forms.ModelChoiceField(required=False,queryset=RmsGrnupload.objects.values_list('type',flat=True).distinct(),widget=forms.Select(attrs={'style':'max-height: 2em'}))
    flag = forms.ModelChoiceField(required=False,queryset=RmsGrnupload.objects.values_list('flag',flat=True).distinct(),widget=forms.Select(attrs={'style':'max-height: 2em'}))
    class Meta:
        model = RmsGrnupload
        fields = ('itemcode','batch','itemcode','pstdate','sloc','vcode','type','flag')
    def __init__(self, plt, *args, **kwargs):
        super(RmsGrnFinalFilter, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = RmsGrnupload.objects.values_list('type',flat=True).distinct().filter(plt=plt)

class RmsRevinterface(forms.ModelForm):
    mrno = forms.CharField(required=True)
    itemcode = forms.CharField(required=False)
    class Meta:
        model = RmsIssue
        fields = '__all__'

class RmsPendingIssueRep(forms.ModelForm):
    shift = forms.ChoiceField(choices = SHIFT_CHOICES, required=True)
    issuedon = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),initial = datetime.date.today)
    remarks = forms.CharField(initial='NA')
    itemcode = forms.CharField(required=False)
    mrno = forms.CharField(initial='NA')
    class Meta:
        model = RmsIssue
        fields = '__all__'

class RmsIssueSummFilter(forms.ModelForm):
    mrno = forms.ModelChoiceField(required=False,queryset=RmsIssueSummary.objects.values_list('mrno',flat=True).distinct())
    itemcode= forms.ModelChoiceField(required=False,queryset=RmsIssueSummary.objects.values_list('itemcode',flat=True).distinct())
    issuedon = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)
    class Meta:
        model = RmsIssueSummary
        fields = ['mrno','issuedon','itemcode']
    
    def __init__(self, plt, *args, **kwargs):
        super(RmsIssueSummFilter, self).__init__(*args, **kwargs)
        self.fields['mrno'].queryset = RmsIssueSummary.objects.values_list('mrno',flat=True).distinct().filter(plt=plt)
        self.fields['itemcode'].queryset = RmsIssueSummary.objects.values_list('itemcode',flat=True).distinct().filter(plt=plt)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
class groupschart(forms.ModelForm):
    groups = forms.ModelChoiceField(widget=forms.Select(attrs={'style':'max-width: 6em','id':'selval'}),required=False,queryset=RmsItemmast.objects.values_list('groupno',flat=True).distinct())
    class Meta:
        model = RmsItemmast
        fields = ['groupno']
    def __init__(self, plt, *args, **kwargs):
        super(groupschart, self).__init__(*args, **kwargs)
        self.fields['groupno'].queryset = RmsItemmast.objects.values_list('groupno',flat=True).distinct().filter(plt=plt)
PLANT_CHOICES = (
    ("Bias", ("Bias")),
    ("PCR", ("PCR")),
    ("MCR", ("MCR")),
    ("MCB", ("MCB")),
    ("OTR", ("OTR")) 
)
class RmsPrintsheet(forms.ModelForm):  
    planttype = forms.ChoiceField(choices=PLANT_CHOICES,required=True)
    shift = forms.ChoiceField(choices = SHIFT_CHOICES, required=True)
    issuedon = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),initial = datetime.date.today)
    mrno = forms.ModelChoiceField(required=False,queryset=RmsIssue.objects.values_list('mrno',flat=True).distinct())
    class Meta:  
        model = RmsIssue  
        fields = ('plt','mrno','issuedon','shift',)
    def __init__(self, plt, *args, **kwargs):
        super(RmsPrintsheet, self).__init__(*args, **kwargs)
        self.fields['mrno'].queryset = RmsIssue.objects.values_list('mrno',flat=True).distinct().filter(plt=plt)

        self.fields['shift'].queryset = RmsIssue.objects.values_list('shift',flat=True).distinct().filter(plt=plt)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )