from numpy.linalg import matrix_rank
import numpy as np
import altair as alt
import pandas as pd
alt.renderers.enable('altair_viewer')

df = pd.read_csv("data08.csv")
df_beng = pd.read_csv("beng08.csv")

chart_20003 = alt.Chart(df[df['sensorId']== 20003]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Outdoor weather temperature')
chart_6830 = alt.Chart(df_beng[df_beng['sensorId']==  6830]).mark_bar().encode(x='hour:O',y='value').properties(width = 2500, title = 'Secondary chilled water pump 1 - Power consumption')
chart_6838 = alt.Chart(df_beng[df_beng['sensorId']==  6838]).mark_bar().encode(x='hour:O',y='value').properties(width = 2500, title = 'Secondary chilled water pump 2 - Power consumption')
chart_6846 = alt.Chart(df_beng[df_beng['sensorId']==  6846]).mark_bar().encode(x='hour:O',y='value').properties(width = 2500, title = 'Secondary chilled water pump 3 - Power consumption')
chart_4372 = alt.Chart(df[df['sensorId']==  4372]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Central of the building heating pump (normally open) - Water supply temperature')
chart_4373 = alt.Chart(df[df['sensorId']==  4373]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'High levels of the building heating pump (normally open) - Water supply temperature')
chart_4374 = alt.Chart(df[df['sensorId']==  4374]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Low levels of the building heating pump (normally open) - Water supply temperature')
chart_4366 = alt.Chart(df[df['sensorId']==  4366]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0.5,0.8]))).properties(width = 2500, title = 'Central of the building heating pump (normally open) - Water supply pressure')
chart_4368 = alt.Chart(df[df['sensorId']==  4368]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0.2,0.4]))).properties(width = 2500, title = 'Low levels of the building heating pump (normally open) - Water supply pressure')
chart_4370 = alt.Chart(df[df['sensorId']==  4370]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [1,1.2]))).properties(width = 2500, title = 'High levels of the building heating pump (normally open) - Water supply temperature')
chart_4250 = alt.Chart(df[df['sensorId']==  4250]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0.5,0.7]))).properties(width = 2500, title = 'Central of the building water distributor - Water supply pressure')
chart_4252 = alt.Chart(df[df['sensorId']==  4252]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0.2,0.4]))).properties(width = 2500, title = 'Low levels of the building water distributor - Water supply pressure')
chart_4254 = alt.Chart(df[df['sensorId']==  4254]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Central of the building water distributor - Water supply temperature')
chart_4255 = alt.Chart(df[df['sensorId']==  4255]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Low levels of the building water distributor - Water supply temperature')
chart_4597 = alt.Chart(df[df['sensorId']==  4597]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Plate heat exchanger - Water supply pressure')
chart_4607 = alt.Chart(df[df['sensorId']==  4607]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'Plate heat exchanger - Water supply temperature')

chart_4576 = alt.Chart(df[df['sensorId']==  4576]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'AC Water distributor - Water supply pressure')
chart_4575 = alt.Chart(df[df['sensorId']==  4575]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'AC water collector - Water return pressure')
chart_4603 = alt.Chart(df[df['sensorId']==  4603]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'AC Water distributor - Water supply temperature')
chart_4602 = alt.Chart(df[df['sensorId']==  4602]).mark_line().encode(x='createTime:T',y='value').properties(width = 2500, title = 'AC water collector - Water return temperature')


chart_4444 = alt.Chart(df[df['sensorId']==  4444]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '10th floor Temperature')
chart_4446 = alt.Chart(df[df['sensorId']==  4446]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '1st floor Temperature')
chart_4448 = alt.Chart(df[df['sensorId']==  4448]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '2nd floor Temperature')
chart_4450 = alt.Chart(df[df['sensorId']==  4450]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '3rd floor Temperature')
chart_4452 = alt.Chart(df[df['sensorId']==  4452]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '4th floor Temperature')
chart_4454 = alt.Chart(df[df['sensorId']==  4454]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '5th floor Temperature')
chart_4456 = alt.Chart(df[df['sensorId']==  4456]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '6th floor Temperature')
chart_4458 = alt.Chart(df[df['sensorId']==  4458]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '7th floor Temperature')
chart_4460 = alt.Chart(df[df['sensorId']==  4460]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '8th floor Temperature')
chart_4462 = alt.Chart(df[df['sensorId']==  4462]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '9th floor Temperature')
chart_4464 = alt.Chart(df[df['sensorId']==  4464]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '10th floor 2 Temperature')
chart_4466 = alt.Chart(df[df['sensorId']==  4466]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '11th floor Temperature')
chart_4468 = alt.Chart(df[df['sensorId']==  4468]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '12th floor Temperature')
chart_4470 = alt.Chart(df[df['sensorId']==  4470]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '13th floor Temperature')
chart_4472 = alt.Chart(df[df['sensorId']==  4472]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '14th floor Temperature')
chart_4474 = alt.Chart(df[df['sensorId']==  4474]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '15h floor Temperature')
chart_4476 = alt.Chart(df[df['sensorId']==  4476]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '16th floor Temperature')

chart_4412 = alt.Chart(df[df['sensorId']==  4412]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '1st floor 2 Temperature')
chart_4420 = alt.Chart(df[df['sensorId']==  4420]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '2nd floor 2 Temperature')
chart_4422 = alt.Chart(df[df['sensorId']==  4422]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '3rd floor 2 Temperature')
chart_4424 = alt.Chart(df[df['sensorId']==  4424]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '4th floor 2 Temperature')
chart_4430 = alt.Chart(df[df['sensorId']==  4430]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '5th floor 2 Temperature')
chart_4432 = alt.Chart(df[df['sensorId']==  4432]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '6th floor 2 Temperature')
chart_4434 = alt.Chart(df[df['sensorId']==  4434]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '7th floor 2 Temperature')
chart_4436 = alt.Chart(df[df['sensorId']==  4436]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '8th floor 2 Temperature')

chart_4478 = alt.Chart(df[df['sensorId']==  4478]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '17th floor 2 Temperature')
chart_4480 = alt.Chart(df[df['sensorId']==  4480]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '18th floor 2 Temperature')
chart_4482 = alt.Chart(df[df['sensorId']==  4482]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '19th floor 2 Temperature')
chart_4484 = alt.Chart(df[df['sensorId']==  4484]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '20th floor 2 Temperature')
chart_4491 = alt.Chart(df[df['sensorId']==  4491]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '11th floor 2 Temperature')
chart_4493 = alt.Chart(df[df['sensorId']==  4493]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '12th floor 2 Temperature')
chart_4495 = alt.Chart(df[df['sensorId']==  4495]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '13th floor 2 Temperature')
chart_4497 = alt.Chart(df[df['sensorId']==  4497]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '14th floor 2 Temperature')
chart_4499 = alt.Chart(df[df['sensorId']==  4499]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '15th floor 2 Temperature')
chart_4501 = alt.Chart(df[df['sensorId']==  4501]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '16th floor 2 Temperature')
chart_4503 = alt.Chart(df[df['sensorId']==  4503]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '17th floor 3 Temperature')
chart_4505 = alt.Chart(df[df['sensorId']==  4505]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '18th floor 3 Temperature')
chart_4507 = alt.Chart(df[df['sensorId']==  4507]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '19th floor 3 Temperature')
chart_4509 = alt.Chart(df[df['sensorId']==  4509]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '20th floor 3 Temperature')
chart_4511 = alt.Chart(df[df['sensorId']==  4511]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '20th floor 4 Temperature')
chart_4513 = alt.Chart(df[df['sensorId']==  4513]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [15,30]))).properties(width = 2500, title = '20th floor 5 Temperature')

chart_7154 = alt.Chart(df[df['sensorId']==  7154]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0,50]))).properties(width = 2500, title = 'Central of the building Feed water collector - Water return temperature')
chart_7155= alt.Chart(df[df['sensorId']==  7155]).mark_line().encode(x='createTime:T',y=alt.Y('value', scale = alt.Scale(domain = [0,50]))).properties(width = 2500, title = 'Low levels of the building Feed water collector - Water return temperature')

chart = alt.vconcat(chart_20003, chart_6830, chart_6838, chart_6846,chart_4576, chart_4575, chart_4603, chart_4602, chart_4372 ,chart_4373 ,chart_4374 ,chart_4366 ,chart_4368 ,chart_4370 ,chart_4250 ,chart_4252 ,chart_4254 ,chart_7154,chart_7154, chart_4255 ,chart_4597 ,chart_4607,
        chart_4444,chart_4446,chart_4448,chart_4450,chart_4452,chart_4454,chart_4456,chart_4458,chart_4460,chart_4462,chart_4464,chart_4466,chart_4468,chart_4470,chart_4472,chart_4474,chart_4476,
        chart_4412,chart_4420,chart_4422,chart_4424,chart_4430,chart_4432,chart_4434,chart_4436,chart_4436,
        chart_4478,chart_4480,chart_4482,chart_4484,chart_4491,chart_4493,chart_4495,chart_4497,chart_4499,chart_4501,chart_4503,chart_4505,chart_4507,chart_4509,chart_4511,chart_4513)

chart.save('dataAuguest.html')