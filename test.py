##########
# RAPTOR #
##########

#KVlang to HTML Compiler
import re

#main function
def main():
    #list of widgets and layouts to refer to later in this script
    #important to use the ':' symbol incase these keywords are used elsewhere
    parents = ['BoxLayout:', 'Button:']

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
                <v-sheet style="height: 95vh;"
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
    lastTabCount = 0
    tabCount = 0
    for line in open(kvFile, 'r').readlines():
        lines.append(line)
    print(lines)
    for line in lines:
        print(len(lines))
        print(count)
        if count > len(lines):
            break
        else:
            print(line)
            #getting current amount of tabs
            tabCount = line.count('\t')
            #checks for parent tabs amount for reference later
            if tabCount < lastTabCount:
                parentTabCount = line.count('\t')
            for x in parents:
                if x in line:
                    parentTabCount = line.count('\t')
            #looping through potential parents
            for item in parents:
                if item in line:
                    if item == 'Button:':
                        text = list(re.findall("'([^']*)'", lines[count+1]))
                        print(text)
                        outFile.write(f'\n<v-btn elevation="2" style="height: 100%; width: 100%;"> {text[0]} </v-btn>')
                        break
            count += 1

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