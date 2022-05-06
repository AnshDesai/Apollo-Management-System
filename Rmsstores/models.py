# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authorizatn(models.Model):
    plt = models.IntegerField(db_column='PLT', primary_key=True)  # Field name made lowercase.
    emp_id = models.DecimalField(db_column='EMP_ID', max_digits=18, decimal_places=0)  # Field name made lowercase.
    appl = models.CharField(db_column='APPL', max_length=25)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHORIZATN'
        unique_together = (('plt', 'emp_id', 'appl'),)


class EmpInfo(models.Model):
    plt = models.IntegerField(db_column='PLT', primary_key=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='EMP_ID')  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=30)  # Field name made lowercase.
    passwd = models.CharField(db_column='PASSWD', max_length=10)  # Field name made lowercase.
    sect = models.CharField(db_column='SECT', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gate_dept = models.CharField(db_column='GATE_DEPT', max_length=26, blank=True, null=True)  # Field name made lowercase.
    desg = models.CharField(db_column='DESG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fgsdev_dept = models.CharField(db_column='FGSDEV_DEPT', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMP_INFO'
        unique_together = (('plt', 'emp_id'),)


class Finyear(models.Model):
    fin_year = models.IntegerField(db_column='FIN_YEAR', primary_key=True)  # Field name made lowercase.
    seq_number = models.IntegerField(db_column='SEQ_NUMBER')  # Field name made lowercase.
    fin = models.CharField(db_column='FIN', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FINYEAR'


class RmsGroupmast(models.Model):

    class Meta:
        db_table = 'Rms_GROUPMAST'
        unique_together = (('plt', 'groupno'),)
    # def __str__(self):
    #     return self.flag
    plt = models.CharField(max_length=5)
    groupno = models.CharField(max_length=5)
    flag = models.CharField(max_length=1, blank=True,)

class RmsItemmast(models.Model):
    plt = models.CharField(max_length=5)
    itemcode = models.CharField(max_length=9)
    itemdesc = models.CharField(max_length=50)
    groupno = models.CharField(max_length=5)
    unit = models.CharField(max_length=10)
    flag = models.CharField(max_length=1)
    updtby = models.CharField(max_length=50)
    updton = models.DateTimeField()

    class Meta:
        unique_together = (('plt', 'itemcode'),)
        db_table = 'Rms_ITEMMAST'


class RmsVendormast(models.Model):
    plt = models.CharField(max_length=5)
    vcode = models.CharField(max_length=15)
    flag = models.CharField(max_length=80)
    updtby = models.CharField(max_length=50)
    updton = models.DateTimeField()

    class Meta:
        unique_together = (('plt', 'vcode'),)
        db_table = 'Rms_VENDORMAST'
TYPE_CHOICES = (
    ("Regular", ("Regular")),
    ("Trial", ("Trial")),
    ("Parked", ("Parked"))
)
FLAG_CHOICES = (
    ("Active", ("Active")),
    ("Blocked", ("Blocked"))
)

SHIFT_CHOICES = (
    ("A", ("A")),
    ("B", ("B")),
    ("C", ("C")),
    ("G", ("G"))
)
class RmsGrnupload(models.Model):
    updno = models.IntegerField()
    serialno = models.IntegerField()
    batch = models.CharField(max_length=20, null=True)
    finyear = models.CharField(max_length=5)
    itemdoc = models.CharField(max_length=15)
    itemcode = models.CharField(max_length=9, null=True)
    itemdesc = models.CharField(max_length=200, null=True)
    sloc = models.CharField(max_length=6, null=True)
    grgi = models.CharField(max_length=15, null=True)
    headertxt = models.CharField(max_length=100, null=True)
    unloadpt = models.CharField(max_length=15, null=True)
    landbill = models.CharField(max_length=50, null=True)
    glacc = models.CharField(max_length=50, null=True)
    recepient = models.CharField(max_length=10, null=True)
    mvt = models.CharField(max_length=5, blank=True, null=True)
    mttext = models.CharField(max_length=50, blank=True, null=True)
    plt = models.CharField(max_length=5)
    po = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    stobin = models.CharField(max_length=50, blank=True, null=True)
    usname = models.CharField(max_length=20, blank=True, null=True)
    valtype = models.CharField(max_length=50, blank=True, null=True)
    vcode = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.DecimalField(decimal_places=4,max_digits=18)
    recqty = models.DecimalField(decimal_places=4,max_digits=18)
    unit = models.CharField(max_length=10, blank=True, null=True)
    pstdate = models.DateField(default=False,blank=True,null=True)
    mandate = models.DateField(default=False,blank=True,null=True)
    sled = models.DateField(default=False,blank=True, null=True)
    amountlc = models.DecimalField(decimal_places=4,max_digits=18)
    curr = models.CharField(max_length=5, blank=True, null=True)
    docdate = models.DateField(default=False,blank=True,null=True)
    entrydate = models.DateField(default=False,blank=True,null=True)
    oun = models.CharField(max_length=5, blank=True, null=True)
    ounqty = models.DecimalField(decimal_places=4,max_digits=18, blank=True, null=True)
    avgqty = models.DecimalField(decimal_places=4,max_digits=18)
    packets = models.IntegerField()
    type = models.CharField(max_length=10,choices=TYPE_CHOICES,default="Regular")
    flag = models.CharField(max_length=10,choices=FLAG_CHOICES,default="Active")
    issuedmr = models.CharField(max_length=500)
    
    class Meta:
        unique_together = (('plt','itemdoc','itemcode'),)
        db_table = 'Rms_GRNUPLOAD'


class RmsGrnuploadTemp(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    itemdoc = models.CharField(max_length=15)
    itemcode = models.CharField(max_length=9, null=True)
    updno = models.IntegerField()
    serialno = models.IntegerField()
    batch = models.CharField(max_length=20, null=True)
    itemdesc = models.CharField(max_length=200, null=True)
    sloc = models.CharField(max_length=6, null=True)
    grgi = models.CharField(max_length=15, null=True)
    headertxt = models.CharField(max_length=100, null=True)
    unloadpt = models.CharField(max_length=15, null=True)
    landbill = models.CharField(max_length=50, null=True)
    glacc = models.CharField(max_length=50, null=True)
    recepient = models.CharField(max_length=10, null=True)
    mvt = models.CharField(max_length=5, blank=True, null=True)
    mttext = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    stobin = models.CharField(max_length=50, blank=True, null=True)
    usname = models.CharField(max_length=20, blank=True, null=True)
    valtype = models.CharField(max_length=50, blank=True, null=True)
    vcode = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.DecimalField(decimal_places=4,max_digits=18)
    unit = models.CharField(max_length=10, blank=True, null=True)
    pstdate = models.DateField(default=False,blank=True,null=True)
    mandate = models.DateField(blank=True,null=True)
    sled = models.DateField(default=False,blank=True, null=True)
    amountlc = models.DecimalField(decimal_places=4,max_digits=18)
    curr = models.CharField(max_length=5, blank=True, null=True)
    docdate = models.DateField(default=False,blank=True,null=True)
    entrydate = models.DateField(default=False,blank=True,null=True)
    oun = models.CharField(max_length=5, blank=True, null=True)
    ounqty = models.CharField(max_length=20, blank=True, null=True)
    avgqty = models.DecimalField(decimal_places=4,max_digits=18)
    type = models.CharField(max_length=10,choices=TYPE_CHOICES,default="Regular")
    class Meta:
        unique_together = (('plt','finyear','itemdoc','itemcode',),)
        db_table = 'Rms_GRNUPLOADTEMP'

class RmsShelfmast(models.Model):
    plt = models.CharField(max_length=5)
    itemcode = models.CharField(max_length=9)
    itemdesc = models.CharField(max_length=200, null=True)
    groupno = models.CharField(max_length=5)
    shelflife = models.CharField(max_length=10)
    remarks = models.CharField(max_length=30)
    updtby = models.CharField(max_length=5, blank=True, null=True)
    updton = models.DateField()
    class Meta:
        unique_together = (('plt', 'itemcode'),)
        db_table = 'Rms_SHELFMAST'

class RmsCN(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=4)
    ctrlno_document = models.CharField(max_length=50)
    ctrl_next_no = models.DecimalField(max_digits=18,decimal_places=0)
    class Meta:
        unique_together = (('plt', 'finyear','ctrlno_document'),)
        db_table = 'Rms_CNCONTROL'

class RmsStockBatch(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    itemdesc = models.CharField(max_length=15)    
    itemcode = models.CharField(max_length=9, null=True)
    batch = models.CharField(max_length=20, null=True)
    opnqty = models.DecimalField(max_digits=18,decimal_places=4)
    recqty = models.DecimalField(max_digits=18,decimal_places=4)
    avaqty = models.DecimalField(max_digits=18,decimal_places=4)
    issuedqty = models.DecimalField(max_digits=18,decimal_places=4)
    clsqty = models.DecimalField(max_digits=18,decimal_places=4)
    unit = models.CharField(max_length=5, blank=True, null=True)
    flag = models.CharField(max_length=5, blank=True, null=True)
    class Meta:
        unique_together = (('plt','finyear','itemcode','batch'),)
        db_table = 'Rms_STOCKBATCH'

class RmsStockSummary(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    itemdesc = models.CharField(max_length=15)    
    itemcode = models.CharField(max_length=9, null=True)
    opnqty = models.DecimalField(max_digits=18,decimal_places=4)
    recqty = models.DecimalField(max_digits=18,decimal_places=4)
    avaqty = models.DecimalField(max_digits=18,decimal_places=4)
    issuedqty = models.DecimalField(max_digits=18,decimal_places=4)
    clsqty = models.DecimalField(max_digits=18,decimal_places=4)
    unit = models.CharField(max_length=5, blank=True, null=True)
    flag = models.CharField(max_length=5, blank=True, null=True)
    groupno = models.CharField(max_length=5)
    class Meta:
        unique_together = (('plt','finyear','itemcode',),)
        db_table = 'Rms_STOCKSUMMARY'


class RmsIssue(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    mrno = models.CharField(max_length=20)
    mrsrno = models.IntegerField()
    itemdoc = models.CharField(max_length=15)
    itemdesc = models.CharField(max_length=15)    
    itemcode = models.CharField(max_length=9, null=True)
    batch = models.CharField(max_length=20, null=True)
    vcode = models.CharField(max_length=15, blank=True, null=True)
    issuedqty = models.DecimalField(max_digits=18,decimal_places=4)
    unit = models.CharField(max_length=5, blank=True, null=True)
    issuedby = models.CharField(max_length=15)
    issuedon = models.DateField(default=False,blank=True,null=True)
    shift = models.CharField(max_length=10,choices=SHIFT_CHOICES,null=False)
    remarks =models.CharField(max_length=500)
    class Meta:
        unique_together = (('plt','finyear','mrno','itemcode'),)
        db_table = 'Rms_ISSUE'

class RmsUnitmast(models.Model):
    plt = models.CharField(max_length=5)
    unit = models.CharField(max_length=3)
    convamount = models.DecimalField(decimal_places=2,max_digits=18)
    convunit = models.CharField(max_length=5)
    flag = models.CharField(max_length=1)
    updton  = models.DateField()
    updtby = models.CharField(max_length=20)
    class Meta:
        db_table = 'Rms_UNITMAST'
        unique_together = (('plt', 'unit'),)


class RmsReversal(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    mrno = models.CharField(max_length=20)
    mrsrno = models.IntegerField()
    itemdoc = models.CharField(max_length=15)    
    itemcode = models.CharField(max_length=9, null=True)
    batch = models.CharField(max_length=20, null=True)
    vcode = models.CharField(max_length=15, blank=True, null=True)
    issuedqty = models.DecimalField(max_digits=18,decimal_places=4)
    unit = models.CharField(max_length=5, blank=True, null=True)
    issuedby = models.CharField(max_length=15)
    issuedon = models.DateField(default=False,blank=True,null=True)
    shift = models.CharField(max_length=10,choices=SHIFT_CHOICES,null=False)
    remarks =models.CharField(max_length=500)
    reversedby = models.CharField(max_length=50)
    class Meta:
        unique_together = (('plt','finyear','mrno','itemcode','mrsrno'),)
        db_table = 'Rms_REVERSAL'

class RmsIssueSummary(models.Model):
    plt = models.CharField(max_length=5)
    finyear = models.CharField(max_length=5)
    mrno = models.CharField(max_length=20)
    itemdesc = models.CharField(max_length=15,blank=True, null=True)    
    itemcode = models.CharField(max_length=9, null=True)
    issuedqty = models.DecimalField(max_digits=18,decimal_places=4)
    unit = models.CharField(max_length=5, blank=True, null=True)
    issuedby = models.CharField(max_length=15)
    issuedon = models.DateField()
    reqqty = models.DecimalField(max_digits=18,decimal_places=4)
    remqty = models.DecimalField(max_digits=18,decimal_places=4)
    class Meta:
        unique_together = (('plt','finyear','mrno','itemcode'),)
        db_table = 'Rms_ISSUESUMMARY'

class RmsShelfMastUpd(models.Model):
    plt = models.CharField(max_length=5)
    itemcode = models.CharField(max_length=20)
    itemdesc = models.CharField(max_length=500, null=True)
    groupno = models.CharField(max_length=5)
    prevshelflife = models.CharField(max_length=10)
    newshelflife = models.CharField(max_length=10)
    remarks = models.CharField(max_length=50)
    updtby = models.CharField(max_length=5, blank=True, null=True)
    updton = models.DateField()
    prevupddate = models.DateField()
    prevupdby = models.CharField(max_length=5, blank=True, null=True)
    reason = models.CharField(max_length=100,default="NA")
    class Meta:
        db_table = 'Rms_SHELFLIFEUPD'

class RmsGrnSlifeUPD(models.Model):
    plt = models.CharField(max_length=5)
    itemcode = models.CharField(max_length=20)
    itemdoc = models.CharField(max_length=15)
    prevsled = models.CharField(max_length=10)
    newsled = models.CharField(max_length=10)
    updtby = models.CharField(max_length=5, blank=True, null=True)
    updton = models.DateField()
    reason = models.CharField(max_length=100,default="NA")
    class Meta:
        db_table = 'Rms_GRNSLIFEUPD'