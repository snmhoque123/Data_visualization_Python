{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cb06ab0c-accf-4777-aaf0-8c7a3cdcaa42",
   "metadata": {},
   "source": [
    "# Dash – An Overview\n",
    "\n",
    "- Open-source User Interface Python library from Plotly\n",
    "- Easy to build GUI\n",
    "- Declarative and Reactive\n",
    "- Rendered in a web browser and can be deployed to servers\n",
    "- Inherently cross-platform and mobile ready\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ce89463-cf71-4b6c-b1f5-a8588e499c9e",
   "metadata": {},
   "source": [
    "## Dash App Layout With Figure and Slider"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "766e8805-b490-44c6-b943-6f73ec805b24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f293c34200>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#For first time dash user, install dash\n",
    "#!pip install dash\n",
    "from dash import Dash, dcc, html, Input, Output, callback\n",
    "import plotly.express as px\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')\n",
    "\n",
    "app = Dash(__name__)\n",
    "\n",
    "app.layout = html.Div([\n",
    "    dcc.Graph(id='graph-with-slider'),\n",
    "    dcc.Slider(\n",
    "        df['year'].min(),\n",
    "        df['year'].max(),\n",
    "        step=None,\n",
    "        value=df['year'].min(),\n",
    "        marks={str(year): str(year) for year in df['year'].unique()},\n",
    "        id='year-slider'\n",
    "    )\n",
    "])\n",
    "\n",
    "\n",
    "@callback(\n",
    "    Output('graph-with-slider', 'figure'),\n",
    "    Input('year-slider', 'value'))\n",
    "def update_figure(selected_year):\n",
    "    filtered_df = df[df.year == selected_year]\n",
    "\n",
    "    fig = px.scatter(filtered_df, x=\"gdpPercap\", y=\"lifeExp\",\n",
    "                     size=\"pop\", color=\"continent\", hover_name=\"country\",\n",
    "                     log_x=True, size_max=55)\n",
    "\n",
    "    fig.update_layout(transition_duration=500)\n",
    "\n",
    "    return fig\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca7bc51c-469c-4702-96e5-6b4575fdc33c",
   "metadata": {},
   "source": [
    "## Slider Component on Dash Core"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "48fb5561-12d1-47ba-82ed-4f4826dfba74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f294064d10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from dash import Dash, dcc, html\n",
    "\n",
    "app = Dash(__name__)\n",
    "\n",
    "app.layout = html.Div([\n",
    "    dcc.Slider(-5, 10, 1, value=-3)\n",
    "])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5f701f70-c234-4eb7-adf6-a8d0a40a7095",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: httpx==0.20 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (0.20.0)\n",
      "Requirement already satisfied: dash in c:\\users\\snmho\\anaconda3\\lib\\site-packages (2.17.1)\n",
      "Requirement already satisfied: plotly in c:\\users\\snmho\\anaconda3\\lib\\site-packages (5.22.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from httpx==0.20) (2024.7.4)\n",
      "Requirement already satisfied: charset-normalizer in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from httpx==0.20) (3.3.2)\n",
      "Requirement already satisfied: sniffio in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from httpx==0.20) (1.3.1)\n",
      "Requirement already satisfied: rfc3986<2,>=1.3 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from rfc3986[idna2008]<2,>=1.3->httpx==0.20) (1.5.0)\n",
      "Requirement already satisfied: httpcore<0.14.0,>=0.13.3 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from httpx==0.20) (0.13.7)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (3.0.3)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (3.0.3)\n",
      "Requirement already satisfied: dash-html-components==2.0.0 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: dash-core-components==2.0.0 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (2.0.0)\n",
      "Requirement already satisfied: dash-table==5.0.0 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (5.0.0)\n",
      "Requirement already satisfied: importlib-metadata in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (7.0.1)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (4.11.0)\n",
      "Requirement already satisfied: requests in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from dash) (2.32.3)\n",
      "Requirement already satisfied: retrying in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from dash) (1.3.4)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from dash) (1.6.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from dash) (72.1.0)\n",
      "Requirement already satisfied: tenacity>=6.2.0 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from plotly) (8.2.2)\n",
      "Requirement already satisfied: packaging in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from plotly) (24.1)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (1.6.2)\n",
      "Requirement already satisfied: h11<0.13,>=0.11 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from httpcore<0.14.0,>=0.13.3->httpx==0.20) (0.12.0)\n",
      "Requirement already satisfied: anyio==3.* in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from httpcore<0.14.0,>=0.13.3->httpx==0.20) (3.7.1)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from anyio==3.*->httpcore<0.14.0,>=0.13.3->httpx==0.20) (3.7)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from Werkzeug<3.1->dash) (2.1.5)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\snmho\\anaconda3\\lib\\site-packages (from importlib-metadata->dash) (3.17.0)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from requests->dash) (2.2.2)\n",
      "Requirement already satisfied: six>=1.7.0 in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from retrying->dash) (1.16.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\snmho\\appdata\\roaming\\python\\python312\\site-packages (from click>=8.1.3->Flask<3.1,>=1.0.4->dash) (0.4.6)\n"
     ]
    }
   ],
   "source": [
    "!pip3 install httpx==0.20 dash plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0bce2b75-1b8e-43ec-b891-b2a4ae5e8a1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "d45ca72f-e8c1-4026-a68f-9b094ec1c379",
   "metadata": {},
   "outputs": [],
   "source": [
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "66d74004-d036-4ca5-9488-87514d59f844",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n",
    "\n",
    "# Read the airline data into the pandas dataframe\n",
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "eb86d1bf-64ed-4966-9a43-e717d5c7c2f1",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'dash_interactivity' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[52], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mdash_interactivity\u001b[49m\u001b[38;5;241m.\u001b[39mpy\n",
      "\u001b[1;31mNameError\u001b[0m: name 'dash_interactivity' is not defined"
     ]
    }
   ],
   "source": [
    "dash_interactivity.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "49cbf1ea-cb4f-49d0-bca1-0c5b7a77f261",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a dash application layout\n",
    "app = dash.Dash(__name__)\n",
    "# Get the layout of the application and adjust it.\n",
    "# Create an outer division using html.Div and add title to the dashboard using html.H1 component\n",
    "# Add a html.Div and core input text component\n",
    "# Finally, add graph component.\n",
    "app.layout = html.Div(children=[html.H1(),\n",
    "                                html.Div([\"Input Year\", dcc.Input(),], \n",
    "                                style={}),\n",
    "                                html.Br(),\n",
    "                                html.Br(),\n",
    "                                html.Div(),\n",
    "                                ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "37334d09-4bfa-4118-9b06-ea15bdb879e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f295104170>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n",
    "# Read the airline data into pandas dataframe\n",
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})\n",
    "                                   \n",
    "# Create a dash application\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "app.layout = html.Div(children=[html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),\n",
    "                                html.Div([\"Input Year\", dcc.Input(),], \n",
    "                                style={}),\n",
    "                                html.Br(),\n",
    "                                html.Br(),\n",
    "                                html.Div(),\n",
    "                                ])\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "45a40ee5-72ec-43fd-bc66-b281a6c44d2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f294ee5730>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n",
    "# Read the airline data into pandas dataframe\n",
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})\n",
    "# Create a dash application\n",
    "app = dash.Dash(__name__)\n",
    "                               \n",
    "app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),\n",
    "                                html.Div([\"Input Year: \", dcc.Input(id='input-year', value='2010', \n",
    "                                type='number', style={'height':'50px', 'font-size': 35}),], \n",
    "                                style={'font-size': 40}),\n",
    "                                html.Br(),\n",
    "                                html.Br(),\n",
    "                                html.Div(dcc.Graph(id='line-plot')),\n",
    "                                ])\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "b09919f0-ed94-41c4-8188-7c2b753df9df",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "expected argument value expression (3436646727.py, line 15)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[66], line 15\u001b[1;36m\u001b[0m\n\u001b[1;33m    fig = go.Figure(data=)\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m expected argument value expression\n"
     ]
    }
   ],
   "source": [
    "# add callback decorator\n",
    "import plotly.graph_objects as go\n",
    "@app.callback(Output(),\n",
    "               Input())\n",
    "\n",
    "# Add computation to callback function and return graph\n",
    "def get_graph(entered_year):\n",
    "    # Select data based on the entered year\n",
    "    df =  airline_data[airline_data['Year']==int(entered_year)]\n",
    "    \n",
    "    # Group the data by Month and compute the average over arrival delay time.\n",
    "    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()\n",
    "    \n",
    "    # \n",
    "    fig = go.Figure(data=)\n",
    "    fig.update_layout()\n",
    "    return fig\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "0165c0a2-1d09-4205-857e-c311a3a112a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f2942e3620>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import required libraries\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "from dash import dcc\n",
    "from dash import html\n",
    "from dash.dependencies import Input, Output\n",
    "\n",
    "# Read the airline data into the pandas dataframe\n",
    "airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                            encoding = \"ISO-8859-1\",\n",
    "                            dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                                   'Div2Airport': str, 'Div2TailNum': str})\n",
    "# Create a dash application\n",
    "app = dash.Dash(__name__)\n",
    "                               \n",
    "app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),\n",
    "                                html.Div([\"Input Year: \", dcc.Input(id='input-year', value='2010', \n",
    "                                type='number', style={'height':'50px', 'font-size': 35}),], \n",
    "                                style={'font-size': 40}),\n",
    "                                html.Br(),\n",
    "                                html.Br(),\n",
    "                                html.Div(dcc.Graph(id='line-plot')),\n",
    "                                ])\n",
    "\n",
    "# add callback decorator\n",
    "@app.callback( Output(component_id='line-plot', component_property='figure'),\n",
    "               Input(component_id='input-year', component_property='value'))\n",
    "\n",
    "# Add computation to callback function and return graph\n",
    "def get_graph(entered_year):\n",
    "    # Select 2019 data\n",
    "    df =  airline_data[airline_data['Year']==int(entered_year)]\n",
    "    \n",
    "    # Group the data by Month and compute average over arrival delay time.\n",
    "    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()\n",
    "\n",
    "    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))\n",
    "    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')\n",
    "    return fig\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d4f7456-f4b0-4dc6-bc47-78374577a433",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "6e02a9de-77a3-45d3-9992-13f482e520ec",
   "metadata": {},
   "source": [
    "## Bar Plot of Airline Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "adde49bb-4d03-4091-b221-7187c93afba2",
   "metadata": {},
   "outputs": [],
   "source": [
    "   # Import required libraries\n",
    "   import pandas as pd\n",
    "   import plotly.graph_objects as go\n",
    "   import plotly.express as px\n",
    "   import dash\n",
    "   from dash import dcc\n",
    "   from dash import html\n",
    "   from dash.dependencies import Input, Output\n",
    "   # Read the airline data into pandas dataframe\n",
    "   airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', \n",
    "                       encoding = \"ISO-8859-1\",\n",
    "                       dtype={'Div1Airport': str, 'Div1TailNum': str, \n",
    "                              'Div2Airport': str, 'Div2TailNum': str})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "0b9f9d6d-cce0-407b-98fc-2ef761fe1eaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = dash.Dash(__name__)\n",
    "app.layout = html.Div(children=[ html.H1('Total number of flights to the destination state split by reporting airline',\n",
    "                            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),\n",
    "                            html.Div([\"Input Year: \", dcc. Input(id='input-year',value='2010',\n",
    "                            type='number', style={'height':'50px', 'font-size': 35}),], \n",
    "                            style={'font-size': 40}),html.Br(), html.Br(),\n",
    "                            html.Div(dcc.Graph(id='bar-plot')),]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "27fe0e93-378e-491a-9eca-f5882e34625d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1f294545c10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "@app.callback( Output(component_id='bar-plot',component_property='figure'),\n",
    "             Input(component_id='input-year', component_property='value'))\n",
    "def get_graph(entered_year):\n",
    "    df =  airline_data[airline_data['Year']==int(entered_year)]\n",
    "    bar_data = df.groupby('DestState')['Flights'].sum().reset_index()\n",
    "    fig = px.bar(bar_data, x= \"DestState\", y= \"Flights\", title='Total number of flights to the destination state split by reporting airline') \n",
    "    fig.update_layout(title='Flights to Destination State', xaxis_title='DestState', yaxis_title='Flights')\n",
    "    return fig   \n",
    "if __name__ == '__main__':\n",
    "    app.run_server() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39c7573a-cac5-4fff-8502-3fdf21d2700a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e05eeeca-d49d-4696-83e4-f752f1c33139",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
