from random import randint

global DEBUG
global VARS
DEBUG=False

ListOfPromptIf=["Aie", "Ouille", "Outch", "AAAAAAAAAHHHHHHHH", "It's a trap!!!!", "Run Forest, run !", "Mayday mayday !", "Paaaaff"]

def DebugON(var):
    global DEBUG
    global VARS
    DEBUG = True
    VARS=var

# def DebugON():
#     global DEBUG
#     global VARS
#     DEBUG = True
#     VARS=dict()
#     print("You can use DebugOn(vars()) to see details of your variables")


def DebugOFF():
    global DEBUG
    DEBUG = False


def Dprint(var):
    if DEBUG:
        if type(var) == str and var in VARS.keys():
            print(f"{var} : {VARS[var]}")
        else:
            print(var)

def Dif(condition):
    if DEBUG:
        if not condition:
            print(ListOfPromptIf[randint(0,len(ListOfPromptIf)-1)])

def Dfor(varOfTheLoop,maxOfTheVar=""):
    if DEBUG:
        if type(varOfTheLoop) == str and varOfTheLoop in VARS.keys():
            if maxOfTheVar=="":
                print(f"{varOfTheLoop} : {VARS[varOfTheLoop]}",end='\r')
            else:
                print(f"{varOfTheLoop} : {VARS[varOfTheLoop]} / {maxOfTheVar}",end='\r')
        else:
            print(varOfTheLoop,end='\r')
    
def Danalyse(var):
    text = ""
    var2 = var
    if DEBUG:
        if type(var) == str and var in VARS.keys():
            text+= f"{var} : {type(VARS[var])}"
            var2 = VARS[var]
        if type(var2) in [int,float]:
            if var2 < 0:
                text+= f"{var} is negative"
            if var2 == 0:
                text+= f"{var} is equal to 0"
            if var2 > 0:
                text+= f"{var} is positive"
        if type(var2) in [list,dict,set]:
            if len(var2) == 0:
                text+= f"{var} is empty"
        print(text)



if __name__=='__main__':

    print(vars())
    print(DEBUG)
    DebugON(vars())
    print(DEBUG)
    Dprint(DEBUG)
    Dprint('DEBUG')
    Dprint('VARS')
    DebugOFF()
    print(DEBUG)


