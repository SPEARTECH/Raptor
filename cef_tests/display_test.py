# Imports
from tracemalloc import start
from flask import Flask, render_template
from cefpython3 import cefpython as cef
import platform
import sys
from os import path
import time
import multiprocessing
from flaskwebgui import FlaskUI

# Settings
b_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
app = Flask(__name__)
ui = FlaskUI(app, start_server='flask', browser_path=b_path)#width=500, height=500)

# Routes
@app.route('/')
def home():
    return home_html

@app.route('/new_page')
def new_page():
    return new_page_html
    
# HTML
home_html = '''

<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
</head>
<body>
<div id="app">
    <v-app>
    <v-main>
        <!-- optional webpage container -->
        <v-container>
            <!-- app background color -->
            <div style="height: 95vh; width: 100%;padding-left: 1.5%; background-color: white;">
            <!-- row == orientation: horizontal -->
            <v-row style="height: 100%; width: 100%; padding: 0%;">
                <div style="height: 100%; width: 25%; padding: 5px;">
                    <!-- card (unclickable button), elevation, % size -->
                    <v-card elevation="2" style="height: 100%; width: 100%;"> 
                        <!-- col == orientation: vertical -->
                        <v-col style="height: 100%; width: 100%; padding:0px;">
                            <!-- height = 100 / # of vertical widgets , padding, centered-->
                            <div style="height: 50%; width: 100%; padding: 5px;" class="d-flex justify-center">
                                <!-- centered button, icon, background color, elevation, padding -->
                                <a href="/new_page"> click this link </a>
                            </div>
                            <!-- position center of parent, padding -->
                            <div style="height: 50%; width: 100%; padding: 5px;">
                                <v-btn elevation="2" style="height: 100%; width: 100%;"> Testing 1</v-btn>
                            </div>
                        </v-col>
                    </v-card>
                </div>  
                <!-- Boxlayout, size % based on # of widgets in parent boxlayout -->
                <div style="height: 100%; width: 25%; padding: 5px;">
                    <!-- align-end + justify-end == bottom right of parent (for v-cards) -->
                    <v-card elevation="2" style="height: 100%; width: 100%; background-color: red; padding: 15px; flex-direction: row;" class="d-flex align-start"><div class="d-flex align-self-end">Testing 2</div></v-card>
                </div>  
                <!-- boxlayout orientation: vertical -->
                <v-col style="height: 100%; width: 100%; padding:0%;">
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position left of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;" class="d-flex align-start"><div class="d-flex align-self-end"> Testing 3</div> </v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position right of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px;" class="d-flex justify-end"> Testing 4 </v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position top of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;"><div class="d-flex align-self-start">Testing 5</div></v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position bottom of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;" ><div class="d-flex align-self-end">Testing 6</div></v-btn>
                    </div>
                </v-col>
            </v-row>
            <!-- centered to the left or right or top or bottom could be box layouts with centered widget content -->
            <!-- stack layouts can be used with d-flex flex-row and flex-row-reverse with justify-start,end,center OR flex-column and flex-column-verse with justify-start,end,center-->

            </div>
        </v-container>
    </v-main>
    </v-app>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
<script>
    new Vue({
    delimiters: ["[[","]]"],
    el: '#app',
    vuetify: new Vuetify(),
    })
</script>
</body>
</html>
'''
new_page_html = '''

<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
</head>
<body>
<div id="app">
    <v-app>
    <v-main>
        <!-- optional webpage container -->
        <v-container>
            <!-- app background color -->
            <div style="height: 95vh; width: 100%;padding-left: 1.5%; background-color: white;">
            <!-- row == orientation: horizontal -->
            <v-row style="height: 100%; width: 100%; padding: 0%;">
                <div style="height: 100%; width: 25%; padding: 5px;">
                    <!-- card (unclickable button), elevation, % size -->
                    <v-card elevation="2" style="height: 100%; width: 100%;"> 
                        <!-- col == orientation: vertical -->
                        <v-col style="height: 100%; width: 100%; padding:0px;">
                            <!-- height = 100 / # of vertical widgets , padding, centered-->
                            <div style="height: 50%; width: 100%; padding: 5px;" class="d-flex justify-center">
                                <!-- centered button, icon, background color, elevation, padding -->
                                <v-btn elevation="0" class="d-flex align-self-center" style="background-color: white; height: 50%; width: 50%;"> <v-icon>mdi-thumb-up</v-icon> </v-btn>
                            </div>
                            <!-- position center of parent, padding -->
                            <div style="height: 50%; width: 100%; padding: 5px;">
                                <v-btn elevation="2" style="height: 100%; width: 100%;"> Testing 1</v-btn>
                            </div>
                        </v-col>
                    </v-card>
                </div>  
                <!-- Boxlayout, size % based on # of widgets in parent boxlayout -->
                <div style="height: 100%; width: 25%; padding: 5px;">
                    <!-- align-end + justify-end == bottom right of parent (for v-cards) -->
                    <v-card elevation="2" style="height: 100%; width: 100%; background-color: red; padding: 15px; flex-direction: row;" class="d-flex align-start"><div class="d-flex align-self-end">Testing 2</div></v-card>
                </div>  
                <!-- boxlayout orientation: vertical -->
                <v-col style="height: 100%; width: 100%; padding:0%;">
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position left of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;" class="d-flex align-start"><div class="d-flex align-self-end"> Testing 3</div> </v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position right of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px;" class="d-flex justify-end"> Testing 4 </v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position top of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;"><div class="d-flex align-self-start">Testing 5</div></v-btn>
                    </div>
                    <div style="height: 25%; width: 100%; padding: 5px;">
                        <!-- position bottom of parent -->
                        <v-btn elevation="2" style="height: 100%; width: 100%; padding: 15px; flex-direction: column;" ><div class="d-flex align-self-end">THIS IS THE NEW PAGE</div></v-btn>
                    </div>
                </v-col>
            </v-row>
            <!-- centered to the left or right or top or bottom could be box layouts with centered widget content -->
            <!-- stack layouts can be used with d-flex flex-row and flex-row-reverse with justify-start,end,center OR flex-column and flex-column-verse with justify-start,end,center-->

            </div>
        </v-container>
    </v-main>
    </v-app>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
<script>
    new Vue({
    delimiters: ["[[","]]"],
    el: '#app',
    vuetify: new Vuetify(),
    })
</script>
</body>
</html>
    
'''
    

if __name__ == '__main__':
    cef.Initialize()
    cef.CreateBrowserSync(url="http://127.0.0.1:5000/",
                        window_title="Hello World!")
    app.run()
    cef.MessageLoop()
    cef.Shutdown()
    
    # ui.run()
