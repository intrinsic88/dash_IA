import dash 
import dash_core_components as doc
import dash_html_components as html
import plotly.express as px
import panda as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame(
    {
        "State":["Andaman And Nicobar", "Andhra Pradesh","Arunachal Pradesh","Assam", "Bihar", "Chandigarh", "Chhattisgarh", 
        "Dadra And Nagar Haveli", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu And Kashmir", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh", 
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh", "Uttarakhand",
        "West Bengal"], 
        "Population":[380581, 84580777, 1383727, 31205576, 104099452, 1055450, 25545198, 586956, 16787941, 1458545, 60439692, 25351462, 6864602, 12541302, 32988134, 61095297, 
        33406061, 64473, ]
    }
)