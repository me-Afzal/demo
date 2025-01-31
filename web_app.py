# %%
import plotly.express as px
import dash
from dash import dcc,html
from dash.dependencies import Output,Input

# %%
df=px.data.tips()
df.head()

# %%
app=dash.Dash()
#Day dictionary
day={
    'Sun':'SUNDAY',
    'Sat':'SATURDAY',
    'Thur':'THURSDAY',
    'Fri':'FRIDAY'
}
app.layout=html.Div([
    dcc.RadioItems(
        id='dropdown',
        options=[
            {'label':'Sunday','value':'Sun'},
            {'label':'Saturday','value':'Sat'},
            {'label':'Thursday','value':'Thur'},
            {'label':'Friday','value':'Fri'}
        ],
        value='Sun'
    ),
    html.Br(),
    dcc.Graph(id='graph')
])
@app.callback(
    Output('graph','figure'),
    Input('dropdown','value')
)
def grapg_creation(value):
    filter_df=df.loc[df['day']==value]
    fig=px.scatter(filter_df,x='total_bill',y='tip',trendline='ols',
                   title=f'Realtion between Total Bill and tips in {day[value]}')
    return fig

if __name__=='__main__':
    app.run_server(debug=True,use_reloader=False)

# %%



