from django.shortcuts import render,redirect
from django.urls import path
import pyodbc
import re
import ast
from funcy import flatten
from collections import OrderedDict,defaultdict 
from .forms import *
import xlwt,openpyxl
from django.contrib import messages
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
import pandas as pd
from django.forms import formset_factory
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe 
from datetime import date
from Rmsstores import models
import json
import decimal
from django.views.decorators.csrf import csrf_exempt
import telepot
import time
import urllib3
import schedule
from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
from django.db import transaction
import simplejson
from apps_aodms.views import login
from dateutil.relativedelta import relativedelta
from django.template.defaulttags import register
import smtplib