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
        "Dadra And Nagar Haveli", "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu And Kashmir", ]
    }
)