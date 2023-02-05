###########################################
# Generate automated monthly report
###########################################

# import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import datetime
from datetime import date
from datetime import timedelta
import shutil
# from pptx import Presentation
# from pptx.util import Inches
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image, ImageFont, ImageDraw

# get dates
todays_date = date.today()
current_month = todays_date.strftime('%b-%y')
print("Today's date is ", todays_date)
print('Current month is ', current_month)

# data directory
full_file_path = os.path.realpath(__file__)
file_base_dir = '/'.join(full_file_path.split('/')[:-2])
print('Root directory is ', file_base_dir)
data_dir = os.path.join(file_base_dir, 'data')
reports_dir = os.path.join(file_base_dir, 'reports')
templates_dir = os.path.join(file_base_dir, 'templates')
images_dir = os.path.join(file_base_dir, 'images')
data_file = os.path.join(data_dir, 'automation.csv')
print('Data file used is ', data_file)
report_template_file = os.path.join(templates_dir, 'template.pptx')
print('Template file used is ', report_template_file)

# read data
df = pd.read_csv(data_file)
print('Total records found is ', df.shape[0])
project_name = 'Aurora'
df = df.query('project == @project_name').groupby(['date'], as_index=True).sum().sort_values('date',
                                                                                             ascending=True)
print(df)
# print(df.shape[0])

# generate plot
fig = plt.figure(figsize=(20, 10))
fig.tight_layout()
month_value = df.iloc[-1, df.columns.get_loc('date')]
