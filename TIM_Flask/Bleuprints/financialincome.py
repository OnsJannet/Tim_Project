import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

financialincome_bp = Blueprint('financialincome', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["financialincome"]


@financialincome_bp.route('/financialincome', methods=['GET', 'POST'])
@login_required
def financialincome():
    """
    Create new collection in the database
    """    
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["FinancialExp_Header1"] = (int(ref["basic_year"])) 
    x["FinancialExp_Header2"] = (int(ref["basic_year"]) + 1 )
    x["FinancialExp_Header3"] = (int(ref["basic_year"]) + 2 )
    x["FinancialExp_Header4"] = (int(ref["basic_year"]) + 3 )
    x["FinancialExp_Header5"] = (int(ref["basic_year"]) + 4 )   
    i = 1
    lst = []
    while(i <1027):
        lst.append(("FinancialExp_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)                                   

    current_db.financialincome.insert_one(x)
    x = current_db.financialincome.find_one({"GlobalId": "global"})
    return render_template("fin-income-exp.html", data=x) 


####################################################################################

@financialincome_bp.route('/financialincome/update', methods=['GET', 'POST'])
@login_required
def financialincome_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        vehicle = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        parts = current_db.turnoverpart.find_one({"GlobalId": "global"})
        services = current_db.turnoverservices.find_one({"GlobalId": "global"})
        costs = current_db.costofsale.find_one({"GlobalId": "global"})
        salaries = current_db.salaries.find_one({"GlobalId": "global"})                 
        selling = current_db.sellingoper.find_one({"GlobalId": "global"})
        inv = current_db.invdepr.find_one({"GlobalId": "global"})
        fin = current_db.financialrequirements.find_one({"GlobalId": "global"})
        pl = current_db.pl.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["FinancialExp_Header1"] = (int(ref["basic_year"])) 
        x["FinancialExp_Header2"] = (int(ref["basic_year"]) + 1 )
        x["FinancialExp_Header3"] = (int(ref["basic_year"]) + 2 )
        x["FinancialExp_Header4"] = (int(ref["basic_year"]) + 3 )
        x["FinancialExp_Header5"] = (int(ref["basic_year"]) + 4 )           

        # 1. Summary funding requirements:

        # LT- Requirements new dealers only

        x['FinancialExp_Input1'] = float(fin['FinancialRequirement_Input246'])

        # LT- Requirements
        input = 2
        i = 26

        while input in range(1,7) and i in range(25,31):
            x['FinancialExp_Input' + str(input)] = round(float(fin['FinancialRequirement_Input' + str(i)])+1)

            input += 1
            i += 1   

        
        x['FinancialExp_Input3'] = round(float(fin['FinancialRequirement_Input27']) - 0.1 )
        x['FinancialExp_Input4'] = round(float(fin['FinancialRequirement_Input28']) - 0.1 )
        x['FinancialExp_Input5'] = round(float(fin['FinancialRequirement_Input29']) - 0.1 )
        x['FinancialExp_Input6'] = round(float(fin['FinancialRequirement_Input30']) - 0.1 )

        # ST- Requirements
        input = 8
        i = 236
        j = 241

        while input in range(7,13) and i in range(235,241) and j in range(240,246):
            if float(fin['FinancialRequirement_Input' + str(i)]) == 0 :
                x['FinancialExp_Input' + str(input)] = round(1 - float(fin['FinancialRequirement_Input' + str(j)]))
            else:
                x['FinancialExp_Input' + str(input)] = round(float(fin['FinancialRequirement_Input' + str(i)]))

            input += 1
            i += 1 
            j += 1    

        #Total
        input = 13
        i = 1
        j = 7

        while input in range(12,19) and i in range(0,7) and j in range(6,13):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))

            input += 1
            i += 1  
            j += 1    

        #x['FinancialExp_Input16'] = round(float(x['FinancialExp_Input4']) + float(x['FinancialExp_Input10']) - 1)
        x['FinancialExp_Input18'] = round(float(x['FinancialExp_Input6']) + float(x['FinancialExp_Input12']) - 1)

        #2. Long term funding
        # 2.1. Equity & associated means


        input = 27
        i = 26
        j = 32        

        x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))
 

        input = 28
        i = 27
        j = 33

        while input in range(27,31) and i in range(26,30) and j in range(32,36):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))

            input += 1
            i += 1  
            j += 1   

        #3. Reserves 
        x['FinancialExp_Input38'] =  round(float(pl['PL_Input86']))
        x['FinancialExp_Input39'] =  round(float(pl['PL_Input87']) + float(x['FinancialExp_Input38']))
        x['FinancialExp_Input40'] =  round(float(pl['PL_Input88']) + float(x['FinancialExp_Input39']))      
        x['FinancialExp_Input41'] =  round(float(pl['PL_Input89']) + float(x['FinancialExp_Input40']))             
        x['FinancialExp_Input42'] =  round(float(pl['PL_Input90']) + float(x['FinancialExp_Input41'])) 

        #6. Result in latest year
        #input = 56
        #i = 96 

        #while input in range(55, 61)  and i in range(95, 101):
            #x['FinancialExp_Input' + str(input)] = round(float(pl['PL_Input' + str(i)]))

            #input += 1
            #i += 1


        #5. Retained earnings previous years
        input = 51
        i = 50
        j = 56       

        x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))
 

        input = 52
        i = 51
        j = 57


        x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))

   

        input = 53
        i = 52
        j = 58


        x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))

        input = 54
        i = 53
        j = 59


        x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)]))        

              

        #total                                                  
        x['FinancialExp_Input73'] = round(float(x['FinancialExp_Input25']) + float(x['FinancialExp_Input61']))

        input = 74
        i = 26
        j = 32
        k = 38
        l = 44
        m = 50
        n = 56
        o = 62

        while input in range(73,79) and i in range(25,31) and j in range(31,37) and k in range(37,41) and l in range(43,49)\
            and m in range(49,55) and n in range(55,61) and o in range(61,67):
            x['FinancialExp_Input' + str(input)] = round(
    float(x['FinancialExp_Input' + str(i)]) +
    float(x['FinancialExp_Input' + str(j)]) +
    float(x['FinancialExp_Input' + str(k)]) +
    float(x['FinancialExp_Input' + str(l)]) +
    float(x['FinancialExp_Input' + str(m)]) +
    float(x['FinancialExp_Input' + str(n)]) +
    float(x['FinancialExp_Input' + str(o)])
)


            input += 1
            i += 1  
            j += 1 
            k += 1   
            l += 1 
            m += 1 
            n += 1 
            o += 1 

            x['FinancialExp_Input77'] = float(x['FinancialExp_Input29']) + float(x['FinancialExp_Input35']) + float(x['FinancialExp_Input41']) + float(x['FinancialExp_Input47']) + float(x['FinancialExp_Input53']) + float(x['FinancialExp_Input59']) + float(x['FinancialExp_Input65'])
            x['FinancialExp_Input78'] = float(x['FinancialExp_Input30']) + float(x['FinancialExp_Input36']) + float(x['FinancialExp_Input42']) + float(x['FinancialExp_Input48']) + float(x['FinancialExp_Input54']) + float(x['FinancialExp_Input60']) + float(x['FinancialExp_Input66'])

        #small table
        #1
        if float(x['FinancialExp_Input79']) == 0:
            x['FinancialExp_Input1000'] = 0
        else:
            x['FinancialExp_Input1000'] = round(float(x['FinancialExp_Input80']))

        #2
        if float(x['FinancialExp_Input79']) < 2:
            x['FinancialExp_Input1001'] = 0
        else:
            x['FinancialExp_Input1001'] = round(float(x['FinancialExp_Input1000']) - float(x['FinancialExp_Input80']) / float(x['FinancialExp_Input79']))

        #3
        if float(x['FinancialExp_Input79']) < 3:
            x['FinancialExp_Input1002'] = 0
        else:
            x['FinancialExp_Input1002'] = round(float(x['FinancialExp_Input1001']) - float(x['FinancialExp_Input80']) / float(x['FinancialExp_Input79']))

        #4
        if float(x['FinancialExp_Input79']) < 4:
            x['FinancialExp_Input1003'] = 0
        else:
            x['FinancialExp_Input1003'] = round(float(x['FinancialExp_Input1002']) - float(x['FinancialExp_Input80']) / float(x['FinancialExp_Input79']))

        #5
        if float(x['FinancialExp_Input79']) < 5:
            x['FinancialExp_Input1004'] = 0
        else:
            x['FinancialExp_Input1004'] = round(float(x['FinancialExp_Input1003']) - float(x['FinancialExp_Input80']) / float(x['FinancialExp_Input79'])-1)

        #6
        if float(x['FinancialExp_Input79']) < 6:
            x['FinancialExp_Input1005'] = 0
        else:
            x['FinancialExp_Input1005'] = round(float(x['FinancialExp_Input1004']) - float(x['FinancialExp_Input80']) / float(x['FinancialExp_Input79']))


        #N
        if float(x['FinancialExp_Input81']) == 0:
            x['FinancialExp_Input1006'] = 0
        else:
            x['FinancialExp_Input1006'] = round(float(x['FinancialExp_Input82']))

        #2
        if float(x['FinancialExp_Input81']) < 2:
            x['FinancialExp_Input1007'] = 0
        else:
            x['FinancialExp_Input1007'] = round(float(x['FinancialExp_Input1006']) - float(x['FinancialExp_Input82']) / float(x['FinancialExp_Input81']))

        #3
        if float(x['FinancialExp_Input81']) < 3:
            x['FinancialExp_Input1008'] = 0
        else:
            x['FinancialExp_Input1008'] = round(float(x['FinancialExp_Input1007']) - float(x['FinancialExp_Input82']) / float(x['FinancialExp_Input81']))

        #4
        if float(x['FinancialExp_Input81']) < 4:
            x['FinancialExp_Input1009'] = 0
        else:
            x['FinancialExp_Input1009'] = round(float(x['FinancialExp_Input1008']) - float(x['FinancialExp_Input82']) / float(x['FinancialExp_Input81']))

        #5
        if float(x['FinancialExp_Input81']) < 5:
            x['FinancialExp_Input1010'] = 0
        else:
            x['FinancialExp_Input1010'] = round(float(x['FinancialExp_Input1009']) - float(x['FinancialExp_Input82']) / float(x['FinancialExp_Input81']))
           

        #N+1
        if float(x['FinancialExp_Input83']) == 0:
            x['FinancialExp_Input1011'] = 0
        else:
            x['FinancialExp_Input1011'] = round(float(x['FinancialExp_Input84']))

        #2
        if float(x['FinancialExp_Input83']) < 2:
            x['FinancialExp_Input1012'] = 0
        else:
            x['FinancialExp_Input1012'] = round(float(x['FinancialExp_Input1011']) - float(x['FinancialExp_Input84']) / float(x['FinancialExp_Input83']))

        #3
        if float(x['FinancialExp_Input83']) < 3:
            x['FinancialExp_Input1013'] = 0
        else:
            x['FinancialExp_Input1013'] = round(float(x['FinancialExp_Input1012']) - float(x['FinancialExp_Input84']) / float(x['FinancialExp_Input83']))

        #4
        if float(x['FinancialExp_Input83']) < 4:
            x['FinancialExp_Input1014'] = 0
        else:
            x['FinancialExp_Input1014'] = round(float(x['FinancialExp_Input1013']) - float(x['FinancialExp_Input84']) / float(x['FinancialExp_Input83']))
     


        #N+2
        if float(x['FinancialExp_Input85']) == 0:
            x['FinancialExp_Input1015'] = 0
        else:
            x['FinancialExp_Input1015'] = round(float(x['FinancialExp_Input86']))

        #2
        if float(x['FinancialExp_Input85']) < 2:
            x['FinancialExp_Input1016'] = 0
        else:
            x['FinancialExp_Input1016'] = round(float(x['FinancialExp_Input1011']) - float(x['FinancialExp_Input86']) / float(x['FinancialExp_Input85'])) -1

        #3
        if float(x['FinancialExp_Input85']) < 3:
            x['FinancialExp_Input1017'] = 0
        else:
            x['FinancialExp_Input1017'] = round(float(x['FinancialExp_Input1016']) - float(x['FinancialExp_Input86']) / float(x['FinancialExp_Input85']))



        #N+3
        if float(x['FinancialExp_Input87']) == 0:
            x['FinancialExp_Input1018'] = 0
        else:
            x['FinancialExp_Input1018'] = round(float(x['FinancialExp_Input88']))

        #2
        if float(x['FinancialExp_Input87']) < 2:
            x['FinancialExp_Input1019'] = 0
        else:
            x['FinancialExp_Input1019'] = round(float(x['FinancialExp_Input1018']) - float(x['FinancialExp_Input88']) / float(x['FinancialExp_Input87']))


        #N+3
        if float(x['FinancialExp_Input89']) == 0:
            x['FinancialExp_Input1020'] = 0
        else:
            x['FinancialExp_Input1020'] = float(x['FinancialExp_Input90'])

        

        #Provisions:
        input = 93
        i = 321

        while input in range(92, 97) and i in range(320, 325):
            x['FinancialExp_Input' + str(input)] = round(float(inv['InvDep_Input' + str(i)]))
            input += 1
            i += 1 

        #Long term funding
        input = 103
        i = 1021
        j = 91
        k = 97

        while input in range(102, 109) and i in range(1020, 1027) and j in range(90, 97) and k in range(96, 103):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)])  + float(x['FinancialExp_Input' + str(j)]) \
                + float(x['FinancialExp_Input' + str(k)]))  

            input += 1
            i += 1
            j += 1
            k += 1



        #total:
        x['FinancialExp_Input1021'] = round(float(x['FinancialExp_Input1000']))
        x['FinancialExp_Input1022'] = round(float(x['FinancialExp_Input1001']) + float(x['FinancialExp_Input1006']))
        x['FinancialExp_Input1023'] = round(float(x['FinancialExp_Input1002']) + float(x['FinancialExp_Input1007']) + float(x['FinancialExp_Input1011']))
        x['FinancialExp_Input1024'] = round(float(x['FinancialExp_Input1003']) + float(x['FinancialExp_Input1008']) + float(x['FinancialExp_Input1012']) + float(x['FinancialExp_Input1015'])  ,3)
        x['FinancialExp_Input1025'] = round(float(x['FinancialExp_Input1004']) + float(x['FinancialExp_Input1009']) + float(x['FinancialExp_Input1013']) + float(x['FinancialExp_Input1016']) + float(x['FinancialExp_Input1018']))
        x['FinancialExp_Input1026'] = round(float(x['FinancialExp_Input1005']) + float(x['FinancialExp_Input1010']) + float(x['FinancialExp_Input1014']) + float(x['FinancialExp_Input1017']) + float(x['FinancialExp_Input1019']) + float(x['FinancialExp_Input1020']))
        
        #Excess
        '''input = 110
        i = 1
        j = 74
        k = 104

        while input in range(109, 115) and i in range(0, 7) and j in range(73, 79) and k in range(102, 109):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)])  + float(x['FinancialExp_Input' + str(j)]) \
                + float(x['FinancialExp_Input' + str(k)]))  

            input += 1
            i += 1
            j += 1
            k += 1 '''

        '''while input in range(109, 115) and i in range(0, 7) and j in range(73, 79) and k in range(102, 109): 
            x['FinancialExp_Input' + str(input)] = round((float(x['FinancialExp_Input' + str(j)])  + float(x['FinancialExp_Input' + str(k)])) - float(x['FinancialExp_Input' + str(i)]))
            i += 1
            j += 1
            k += 1'''

        x['FinancialExp_Input110'] = round(float(x['FinancialExp_Input74'])) + round(float(x['FinancialExp_Input104'])) - round(float(x['FinancialExp_Input2'])) + 1
        x['FinancialExp_Input111'] = round(float(x['FinancialExp_Input75'])) + round(float(x['FinancialExp_Input105'])) - round(float(x['FinancialExp_Input3']))
        x['FinancialExp_Input112'] = round(float(x['FinancialExp_Input76'])) + round(float(x['FinancialExp_Input106'])) - round(float(x['FinancialExp_Input4']))
        x['FinancialExp_Input113'] = round(float(x['FinancialExp_Input77'])) + round(float(x['FinancialExp_Input107'])) - round(float(x['FinancialExp_Input5'])) + 1
        x['FinancialExp_Input114'] = round(float(x['FinancialExp_Input78']))  + round(float(x['FinancialExp_Input108'])) - round(float(x['FinancialExp_Input6'])) + 1




        x['FinancialExp_Input103'] = (round(float(x['FinancialExp_Input91'])) + round(float(x['FinancialExp_Input1021'])) + round(float(x['FinancialExp_Input97'])) + round(float(x['FinancialExp_Input73']))) - round(float(x['FinancialExp_Input1']))
        x['FinancialExp_Input104'] = (round(float(x['FinancialExp_Input92'])) + round(float(x['FinancialExp_Input1022'])) + round(float(x['FinancialExp_Input98'])) ) 
        x['FinancialExp_Input105'] = (round(float(x['FinancialExp_Input93'])) + round(float(x['FinancialExp_Input1023'])) + round(float(x['FinancialExp_Input99'])) ) 
        x['FinancialExp_Input106'] = (round(float(x['FinancialExp_Input94'])) + round(float(x['FinancialExp_Input1024'])) + round(float(x['FinancialExp_Input100'])))   
        x['FinancialExp_Input107'] = (round(float(x['FinancialExp_Input95'])) + round(float(x['FinancialExp_Input1025'])) + round(float(x['FinancialExp_Input101']))) 
        x['FinancialExp_Input108'] = (round(float(x['FinancialExp_Input96'])) + round(float(x['FinancialExp_Input1026'])) + round(float(x['FinancialExp_Input102'])))                              

        #   3.2. Short term debt structure
        # ST requirements

        x['FinancialExp_Input122'] = round(float(x['FinancialExp_Input8']) +1 )        
        x['FinancialExp_Input123'] = round(float(x['FinancialExp_Input9']))       
        x['FinancialExp_Input124'] = round(float(x['FinancialExp_Input10']) +1)       
        x['FinancialExp_Input125'] = round(float(x['FinancialExp_Input11']))      
        x['FinancialExp_Input126'] = round(float(x['FinancialExp_Input12']) -1)      

        #Financial need (-) or surplus (+) on long term
        x['FinancialExp_Input127'] = round(float(x['FinancialExp_Input103']))      
        x['FinancialExp_Input128'] = round(float(x['FinancialExp_Input110']))      
        x['FinancialExp_Input129'] = round(float(x['FinancialExp_Input111']))      
        x['FinancialExp_Input130'] = round(float(x['FinancialExp_Input112']))      
        x['FinancialExp_Input131'] = round(float(x['FinancialExp_Input113']))      
        x['FinancialExp_Input132'] = round(float(x['FinancialExp_Input114']))      

        #Truck inventory financing

        input = 134
        i = 92
        j = 116

        #=('7.5.1 Financial Requirements'!D38*'7.5.2 Fin. Income & Expenses '!E52)+((('7.2.1 Turnover Vehicles'!C53+'7.2.1 Turnover Vehicles'!C54)/2)*E53)+('7.5.1 Financial Requirements'!D39*'7.5.2 Fin. Income & Expenses '!E54)
        while input in range(132, 139) and i in range(91, 101) and j in range(115, 201):
            x['FinancialExp_Input' + str(input)] = round((float(fin['FinancialRequirement_Input' + str(i)]) * (float(x['FinancialExp_Input' + str(j)])/100)))

            input += 1
            i += 2
            j += 1

        #Total short term financing 
        input = 139
        i = 121
        j = 127
        k = 133

        while input in range(138, 145) and i in range(120, 127) and j in range(126, 133) and k in range(132, 145):

            if float(x['FinancialExp_Input' + str(i)]) - float(x['FinancialExp_Input' + str(j)]) \
                - float(x['FinancialExp_Input' + str(k)]) < 0:
                x['FinancialExp_Input' + str(input)] = 0

            else:
                x['FinancialExp_Input' + str(input)] =  round(float(x['FinancialExp_Input' + str(i)]) - float(x['FinancialExp_Input' + str(j)]) \
                - float(x['FinancialExp_Input' + str(k)]))
            
            input += 1
            i += 1
            j += 1
            k += 1

            if float(x['FinancialExp_Input125']) - float(x['FinancialExp_Input131']) \
                - float(x['FinancialExp_Input137']) < 0:
                x['FinancialExp_Input143'] = 0

            else:
                x['FinancialExp_Input143'] =  round(float(x['FinancialExp_Input125']) - float(x['FinancialExp_Input131']) \
                - float(x['FinancialExp_Input137'])+ 1)

            if float(x['FinancialExp_Input126']) - float(x['FinancialExp_Input132']) \
                - float(x['FinancialExp_Input138']) < 0:
                x['FinancialExp_Input144'] = 0

            else:
                x['FinancialExp_Input144'] =  round(float(x['FinancialExp_Input126']) - float(x['FinancialExp_Input132']) \
                - float(x['FinancialExp_Input138'])+ 1)

        #Cash surplus 
        input = 145
        i = 121
        j = 127
        k = 133

        while input in range(144, 151) and i in range(120, 127) and j in range(126, 133) and k in range(132, 145):

            if float(x['FinancialExp_Input' + str(i)]) - float(x['FinancialExp_Input' + str(j)]) \
                - float(x['FinancialExp_Input' + str(k)]) < 0:
                x['FinancialExp_Input' + str(input)] = round(( -1 * (float(x['FinancialExp_Input' + str(i)]) - float(x['FinancialExp_Input' + str(j)]) - float(x['FinancialExp_Input' + str(k)]))))
                

            else:
                x['FinancialExp_Input' + str(input)] =  0
            
            input += 1
            i += 1
            j += 1
            k += 1 


            if float(x['FinancialExp_Input124']) - float(x['FinancialExp_Input130']) - float(x['FinancialExp_Input136']) < 0:
                x['FinancialExp_Input148'] = round(( -1 * (float(x['FinancialExp_Input124']) - float(x['FinancialExp_Input130']) - float(x['FinancialExp_Input136']))))
            else:
                x['FinancialExp_Input148'] =  0            

            if float(x['FinancialExp_Input126']) - float(x['FinancialExp_Input132']) - float(x['FinancialExp_Input138']) < 0:
                x['FinancialExp_Input150'] = round(( -1 * (float(x['FinancialExp_Input126']) - float(x['FinancialExp_Input132']) - float(x['FinancialExp_Input138']))))
            else:
                x['FinancialExp_Input150'] =  0


        #ST loans:
        input = 152
        i = 151
        j = 140

        while input in range(151, 162) and i in range(150, 161) and j in range(139, 145):

            if float(x['FinancialExp_Input' + str(j)]) > 0:
                x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(j)]) * (float(x['FinancialExp_Input' + str(i)])/100))
            else:
                x['FinancialExp_Input' + str(input)] =0
        
            input += 2
            i += 2
            j += 1

        #LT loans:
        input = 162
        i = 1021
        j = 1022
        k = 161

        while input in range(161, 171) and i in range(1020, 1027) and j in range(1021, 1027) and k in range(160, 170):


            x['FinancialExp_Input' + str(input)] = round(((float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)])) / 2) * (float(x['FinancialExp_Input' + str(k)])/100))
        
            input += 2
            i += 1
            j += 1            
            k += 2



        # Subordinated loans:
        input = 173
        i = 61
        j = 62
        k = 172

        while input in range(172, 182) and i in range(60, 67) and j in range(61, 67) and k in range(171, 181):


            x['FinancialExp_Input' + str(input)] = round(((float(x['FinancialExp_Input' + str(i)])) + float(x['FinancialExp_Input' + str(j)]) / 2) * float(x['FinancialExp_Input' + str(k)]))
        
            input += 2
            i += 1
            j += 1            
            k += 2


        #  Truck inventory financing:
        x['FinancialExp_Input183'] = round(float(x['FinancialExp_Input182']) * (float(x['FinancialExp_Input134'])/100))
        x['FinancialExp_Input185'] = round(float(x['FinancialExp_Input184']) * (float(x['FinancialExp_Input135'])/100))
        x['FinancialExp_Input187'] = round(float(x['FinancialExp_Input186']) * (float(x['FinancialExp_Input136'])/100))
        x['FinancialExp_Input189'] = round(float(x['FinancialExp_Input188']) * (float(x['FinancialExp_Input137'])/100))
        x['FinancialExp_Input191'] = round(float(x['FinancialExp_Input190']) * (float(x['FinancialExp_Input138'])/100))

        # Total financial expenses:
        #input =193
        #i = 152
        #j = 162
        #k = 173
        #l = 183

        #while input in range(192, 202) and i in range(151, 161) and j in range(161, 171) and k in range(172, 182)\
            #and l in range(182, 192):

            #x['FinancialExp_Input' + str(input)] = float(x['FinancialExp_Input' + str(i)]) + float(x['FinancialExp_Input' + str(j)])\
                #+ float(x['FinancialExp_Input' + str(k)]) + float(x['FinancialExp_Input' + str(l)])
            
        #input += 2
        #i += 2
        #j += 2
        #k += 2
        #l += 2     
        # 
        x['FinancialExp_Input193'] = round(float(x['FinancialExp_Input152']) + float(x['FinancialExp_Input162']) + float(x['FinancialExp_Input173']) + float(x['FinancialExp_Input183'])) 
        x['FinancialExp_Input195'] = round(float(x['FinancialExp_Input154']) + float(x['FinancialExp_Input164']) + float(x['FinancialExp_Input175']) + float(x['FinancialExp_Input185']))
        x['FinancialExp_Input197'] = round(float(x['FinancialExp_Input156']) + float(x['FinancialExp_Input166']) + float(x['FinancialExp_Input177']) + float(x['FinancialExp_Input187']))  
        x['FinancialExp_Input199'] = round(float(x['FinancialExp_Input158']) + float(x['FinancialExp_Input168']) + float(x['FinancialExp_Input179']) + float(x['FinancialExp_Input189']))        
        x['FinancialExp_Input201'] = round(float(x['FinancialExp_Input160']) + float(x['FinancialExp_Input170']) + float(x['FinancialExp_Input181']) + float(x['FinancialExp_Input191']))

        # Cash surplus
        input = 203
        i = 146
        j = 202

        while input in range(202, 212) and i in range(145, 151) and j in range(201, 211):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]) * (float(x['FinancialExp_Input' + str(j)]) / 100))
            input += 2
            i += 1
            j += 2   

        #Total financial income
        input = 213
        i = 203


        while input in range(212, 222) and i in range(202, 212):
            x['FinancialExp_Input' + str(input)] = round(float(x['FinancialExp_Input' + str(i)]))
            input += 2
            i += 2

        current_db.financialincome.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.financialincome.find_one({"GlobalId": "global"})
    return redirect(url_for('financialincome.financialincome')) 
    return render_template("fin-income-exp.html", data=x)


####################################################################################

@financialincome_bp.route('/financialincome/delete', methods=['GET', 'POST'])
@login_required
def financialincome_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.financialincome.delete_many({})
    return redirect(url_for('financialincome.financialincome')) 
    return render_template("fin-income-exp.html", data=x)