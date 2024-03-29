##########
# RAPTOR #
##########

#KVlang to HTML Compiler
import re

#main function
def main():
    #list of widgets and layouts to refer to later in this script
    #important to use the ':' symbol incase these keywords are used elsewhere
    parents = ['MDBoxLayout:', 'MDCard:']

    #determine desired kv file to compile to html
    kvFile = input('enter name of .kv file to compile: ')

    #determine desired output html file and create it in current dir
    htmlFile = input('enter name of output html file: ')
    outFile = open(htmlFile, "w+")
    outFile.write('''
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
            <v-container>
                <v-sheet style="height: 100vh;"
                color="white"
                elevation="5"
                >
    ''')
    #create temp file for parsing to before adding to html file
    # tempFile = open('temp.html', 'w')

    
    #loop through kv file line by line
    count = 0
    lines = []
    parentTabCount = 0
    parentLineNum = 0
    endWidgetLineNum = 0
    lastTabCount = 0
    tabCount = 0
    lineCount = 0
    orientation = 'horizontal'
    for line in open(kvFile, 'r').readlines():
        lines.append(line)
    for line in lines:
        if ('<Main>:' in line):
            mainLineNum = count
            print(line)
            #getting current amount of tabs
            tabCount = int((len(line) - len(line.lstrip()))/4)
            print('tabcount'+str(tabCount))
            #checks for parent tabs amount for reference later
            if tabCount < lastTabCount:
                parentTabCount = int((len(line) - len(line.lstrip()))/4)
                
            for x in parents:
                if x in line:
                    parentTabCount = int((len(line) - len(line.lstrip()))/4)
            tabLines = []
            widgetClosingTags = []
            #checking if a line contains a widget
            for item in parents:
                if item in line:
                    lastTabCount = tabCount
                    widgetCount = 0
                    if item == 'Button:':
                        parentTabCount = tabCount
                        firstLine = True
                        lineCountTotal = len(lines[lineCount:])
                        lineNum = lineCount
                        print(lines[lineCount:])
                        for line in lines[lineCount:]:
                            currentTab = int((len(line) - len(line.lstrip()))/4)
                            if currentTab == tabCount + 1:
                                if 'orientation:' in line:
                                    orientation = re.findall("'([^']*)'", line)
                                if 'text:' in line:
                                    text = re.findall("'([^']*)'", line)
                                    print(text)
                                    outFile.write(f'\n<v-btn elevation="2" style="height: 100%; width: 100%;"> {text[0]}')
                                    widgetClosingTags.append('</v-btn>')
                            elif currentTab == tabCount and firstLine != True:
                                widgetClosingTags.reverse()
                                for item in widgetClosingTags:
                                    outFile.write('\n' + item)
                            elif lineNum == lineCountTotal - 1:
                                widgetClosingTags.reverse()
                                for item in widgetClosingTags:
                                    outFile.write('\n' + item)
                            # elif currentTab < tabCount:
                            #     for item in widgetClosingTags.reverse():
                            #         outFile.write(item)
                                lastTabCount = currentTab
                            firstLine = False

                            
            count += 1

            lastTabCount = lastTabCount + tabCount
            lineCount += 1

    outFile.write('''\n
                
                </v-sheet>
            </v-container>
        </v-main>
        </v-app>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
    <script>
        new Vue({
        el: '#app',
        vuetify: new Vuetify(),
        })
    </script>
    </body>
    </html>
    ''')

#checking if main script
if __name__ == "__main__":
    main()