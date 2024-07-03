import imp
from re import T
from this import s
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
from Bleuprints.db_routes import db, client, get_current_db

import os
from dotenv import load_dotenv
load_dotenv()

activityanalysis_bp = Blueprint('activityanalysis', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["activityanalysis"]

@activityanalysis_bp.route('/activityanalysis', methods=['GET', 'POST'])
@login_required
def activityanalysis():

    """
    Create new collection in the database
    """    
    current_db = get_current_db()
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)

    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["ActivityAnalysis_Header1"] = (int(ref["basic_year"])) 
    x["ActivityAnalysis_Header2"] = (int(ref["basic_year"]) + 1 )
    x["ActivityAnalysis_Header3"] = (int(ref["basic_year"]) + 2 )
    x["ActivityAnalysis_Header4"] = (int(ref["basic_year"]) + 3 )
    x["ActivityAnalysis_Header5"] = (int(ref["basic_year"]) + 4 ) 
    i = 1
    lst = []
    while(i <5000):
        lst.append(("ActivityAnalysis_Input" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)                                   

    current_db.activityanalysis.insert_one(x)
    x = current_db.activityanalysis.find_one({"GlobalId": "global"})
    return render_template("activity-analysis.html", data=x, user=user) 
  


####################################################################################



@activityanalysis_bp.route('/activityanalysis/update', methods=['POST'])
@login_required
def activityanalysis_update():

    """
    Update a company in the database
    """
    current_db = get_current_db()    
    dic = db["users"].find_one({"_id": session['user_id']})
    user = User(dic)

    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        #Needed Collections:
        vehicle = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        parts = current_db.turnoverpart.find_one({"GlobalId": "global"})
        services = current_db.turnoverservices.find_one({"GlobalId": "global"})
        costs = current_db.costofsale.find_one({"GlobalId": "global"})
        salaries = current_db.salaries.find_one({"GlobalId": "global"})                 
        selling = current_db.sellingoper.find_one({"GlobalId": "global"})
        activity = current_db.activitycontribution.find_one({"GlobalId": "global"})
        inv = current_db.invdepr.find_one({"GlobalId": "global"})
        fin = current_db.financialincome.find_one({"GlobalId": "global"})
        finreq = current_db.financialrequirements.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["ActivityAnalysis_Header1"] = (int(ref["basic_year"])) 
        x["ActivityAnalysis_Header2"] = (int(ref["basic_year"]) + 1 )
        x["ActivityAnalysis_Header3"] = (int(ref["basic_year"]) + 2 )
        x["ActivityAnalysis_Header4"] = (int(ref["basic_year"]) + 3 )
        x["ActivityAnalysis_Header5"] = (int(ref["basic_year"]) + 4 ) 

        # 1 -Turnover DAF:

        x["ActivityAnalysis_Input11"] = round(float(vehicle["TurnoverVehicle_Input_A"]))
        x["ActivityAnalysis_Input12"] = round(float(vehicle["TurnoverVehicle_Input_B"]))
        x["ActivityAnalysis_Input13"] = round(float(vehicle["TurnoverVehicle_Input_C"]))
        x["ActivityAnalysis_Input14"] = round(float(vehicle["TurnoverVehicle_Input_E"]))
        x["ActivityAnalysis_Input15"] = round(float(vehicle["TurnoverVehicle_Input_F"]))              

                #######################################################################

        # 2 Total turnover: 
        input = 31
        DAF = 11
        Oil = 16
        Outsourced_WA = 21
        Internal = 26

        while input in range(30, 36) and DAF in range(10, 16) and Oil in range(15, 21) \
            and Outsourced_WA in range(20, 26) and Internal in range(25, 31):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(DAF)]) \
                 + float(x['ActivityAnalysis_Input' + str(Oil)]) + float(x['ActivityAnalysis_Input' + str(Outsourced_WA)]) \
                    + float(x['ActivityAnalysis_Input' + str(Internal)]),3)

            input += 1
            DAF += 1
            Oil += 1
            Outsourced_WA += 1
            Internal += 1

        
        # 3 Costs - DAF:
        input = 46
        Costs = 131

        while input in range(45, 51) and Costs in range(130, 136):

            x['ActivityAnalysis_Input' + str(input)] = round(float(costs['CostOFSales_Input' + str(Costs)]),3)

            input += 1
            Costs += 1

        x['ActivityAnalysis_Input46'] = round(float(costs['CostOFSales_Input131']) -1)
        x['ActivityAnalysis_Input47'] = round(float(costs['CostOFSales_Input132']) -2)
        x['ActivityAnalysis_Input48'] = round(float(costs['CostOFSales_Input133']) -4)
        x['ActivityAnalysis_Input49'] = round(float(costs['CostOFSales_Input134']) -5)
        x['ActivityAnalysis_Input50'] = round(float(costs['CostOFSales_Input135']) -6)

        # 4 Bonus supplier on sales:
        input = 61
        Costs = 137               

        while input in range(60, 66) and Costs in range(136, 146):

            x['ActivityAnalysis_Input' + str(input)] = round(float(costs['CostOFSales_Input' + str(Costs)]),3)

            input += 1
            Costs += 2

        # 5 Internal:
        input = 71 
        Services = 78
        Parts = 41

        while input in range(70, 76) and Parts in range(40, 46) and Services in range(77, 83):

            x['ActivityAnalysis_Input' + str(input)] = round(float(services['TurnoverServices_Input' + str(Services)]) + float(parts['TurnoverParts_Input' + str(Parts)]),3)

            input += 1
            Services += 1
            Parts += 1


        # 6 Total Cost of Sales:
        input = 76 
        DAF = 46
        Oil = 51
        Salaries = 56
        Bonus = 61
        Outsourced_WA = 66
        Internal = 71

        while input in range(75, 81) and DAF in range(45, 51) and Oil in range(50, 56) and Salaries in range(55, 61) \
            and Bonus in range(60, 66) and Outsourced_WA in range(65, 71) and Internal in range(70, 76):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(DAF)]) + float(x['ActivityAnalysis_Input' + str(Oil)]) \
                + float(x['ActivityAnalysis_Input' + str(Salaries)]) + float(x['ActivityAnalysis_Input' + str(Bonus)]) + \
                    float(x['ActivityAnalysis_Input' + str(Outsourced_WA)]) + float(x['ActivityAnalysis_Input' + str(Internal)]),3)

            input += 1
            DAF += 1
            Oil += 1
            Salaries += 1
            Bonus += 1
            Outsourced_WA += 1
            Internal += 1  
            
        # 7 Gross Profit/Loss:
        input = 81 
        turnover = 31
        costs = 76

        while input in range(80, 86) and turnover in range(30, 36) and costs in range(75, 81):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(turnover)]) \
                - float(x['ActivityAnalysis_Input' + str(costs)]),3)

            input += 1
            turnover += 1
            costs += 1  

        # 8 Margin :
        input = 86 
        turnover = 31
        gross_pl = 81

        while input in range(85, 91) and turnover in range(30, 36) and gross_pl in range(80, 86):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(gross_pl)]) / float(x['ActivityAnalysis_Input' + str(turnover)]),3)
                x['ActivityAnalysis_Input' + str(input)] = Round

            input += 1
            turnover += 1
            gross_pl += 1 

        # 9 Selling expenses: 
        input = 100 
        Vehicle = 126
        salesmen_vb = 13136 
        salesmen_ss = 231
        policy_expenses_1 = 5
        policy_expenses_2 = 159 

        while input in range(99, 105) and Vehicle in range(125, 131) and salesmen_vb in range(13135, 13141) \
            and policy_expenses_1 in range(4, 10):

            x['ActivityAnalysis_Input' + str(input)] = round(float(vehicle['TurnoverVehicle_Input' + str(input)]) * \
                float(salaries['Salaries_Input' + str(salesmen_vb)]) * ( 1 + float(salaries['Salaries_Input' + str(salesmen_ss)]))\
                    + (float(selling['SellingOperation_Input' + str(policy_expenses_1)]) * float(selling['SellingOperation_Input' + str(policy_expenses_2)])),3)

            input += 1
            Vehicle += 1
            salesmen_vb += 1
            policy_expenses_1 += 1

            x['ActivityAnalysis_Input100'] = round(float(activity['ActivityContribution_Input103']))     
            x['ActivityAnalysis_Input101'] = round(float(activity['ActivityContribution_Input391']))  
            x['ActivityAnalysis_Input102'] = round(float(activity['ActivityContribution_Input772']))
            x['ActivityAnalysis_Input103'] = round(float(activity['ActivityContribution_Input1063']))
            x['ActivityAnalysis_Input104'] = round(float(activity['ActivityContribution_Input1341'])) 


        # 10 Salaries & Wages: 
            x['ActivityAnalysis_Input105'] = round(float(activity['ActivityContribution_Input109']))     
            x['ActivityAnalysis_Input106'] = round(float(activity['ActivityContribution_Input397']))  
            x['ActivityAnalysis_Input107'] = round(float(activity['ActivityContribution_Input778']))
            x['ActivityAnalysis_Input108'] = round(float(activity['ActivityContribution_Input1069']))
            x['ActivityAnalysis_Input109'] = round(float(activity['ActivityContribution_Input1347']))
            

        # 11 Other Operating expenses:
        input_1 = 115
        input_2 = 116
        input_3 = 117
        input_4 = 118
        input_5 = 119

        i = 121
        j = 499
        k = 790
        l = 1081
        m = 1359

        while input_1 in range(114, 201) and input_2 in range(115, 202) and input_3 in range(116, 203) \
            and input_4 in range(117, 204) and input_5 in range(118, 205) and i in range(120, 224) and \
                j in range(498, 602) and k in range(789, 894) and l in range(1080, 1184) and m in range(1358, 1462):

            x['ActivityAnalysis_Input' + str(input_1)] = round(float(activity['ActivityContribution_Input' + str(i)]),3)
            x['ActivityAnalysis_Input' + str(input_2)] = round(float(activity['ActivityContribution_Input' + str(j)]) ,3)
            x['ActivityAnalysis_Input' + str(input_3)] = round(float(activity['ActivityContribution_Input' + str(k)]),3)
            x['ActivityAnalysis_Input' + str(input_4)] = round(float(activity['ActivityContribution_Input' + str(l)]),3) 
            x['ActivityAnalysis_Input' + str(input_5)] = round(float(activity['ActivityContribution_Input' + str(m)]),3)                                                                                      
        
            input_1 += 5
            input_2 += 5
            input_3 += 5
            input_4 += 5
            input_5 += 5

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6

        # 12 Total other operating expenses:

        i = 115
        j = 116
        k = 117
        l = 118
        m = 119

        n = 205
        o = 206
        p = 207
        q = 208
        r = 209

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []        


        while i in range(114, 201) and j in range(115, 202) and k in range(116, 203) and l in range(117, 204) and m in range(118, 205):

            total_i.append(float(x['ActivityAnalysis_Input' + str(i)]))
            total_j.append(float(x['ActivityAnalysis_Input' + str(j)]))
            total_k.append(float(x['ActivityAnalysis_Input' + str(k)]))
            total_l.append(float(x['ActivityAnalysis_Input' + str(l)]))
            total_m.append(float(x['ActivityAnalysis_Input' + str(m)]))            

            x['ActivityAnalysis_Input' + str(n)] = round(sum(total_i))
            x['ActivityAnalysis_Input' + str(o)] = round(sum(total_j))          
            x['ActivityAnalysis_Input' + str(p)] = round(sum(total_k))
            x['ActivityAnalysis_Input' + str(q)] = round(sum(total_l)) 
            x['ActivityAnalysis_Input' + str(r)] = round(sum(total_m)) 

            i += 5
            j += 5
            k += 5
            l += 5
            m += 5

        # 13 Depreciations & Amortization:
        x['ActivityAnalysis_Input210'] = round(float(activity['ActivityContribution_Input235']),3)   
        x['ActivityAnalysis_Input211'] = round(float(activity['ActivityContribution_Input615']),3)    
        x['ActivityAnalysis_Input212'] = round(float(activity['ActivityContribution_Input904']),3)    
        x['ActivityAnalysis_Input213'] = round(float(activity['ActivityContribution_Input1196']),3)                    
        x['ActivityAnalysis_Input214'] = round(float(activity['ActivityContribution_Input1473']),3) 

        # 14 Operating profit/loss per activity:
        input = 215

        i = 81
        j = 100
        k = 105
        l = 205
        m = 210

        while input in range(214, 220) and i in range(80, 86) and j in range(99, 105) and \
            k in range(104, 110) and l in range(204, 210) and m in range(209, 215):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) \
                 - float(x['ActivityAnalysis_Input' + str(j)]) - float(x['ActivityAnalysis_Input' + str(k)]) \
                    - float(x['ActivityAnalysis_Input' + str(l)]) - float(x['ActivityAnalysis_Input' + str(m)]),3)

            input += 1

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1

        # 15 Margin:
        input = 220 
        turnover = 31
        operating_pl = 215

        while input in range(219, 225) and turnover in range(30, 36) and operating_pl in range(214, 220):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(operating_pl)]) / float(x['ActivityAnalysis_Input' + str(turnover)]),3)
                x['ActivityAnalysis_Input' + str(input)] = Round

            input += 1
            turnover += 1
            operating_pl += 1                    

        # 16 Truck inventory financing:
        #input = 240

        #i = 92
        #j = 116
        #k = 133

       # while input in range(239, 245) and i in range(91, 101) and j in range(115, 121):
            #x['ActivityAnalysis_Input' + str(input)] = float(finreq['FinancialRequirement_Input' + str(i)]) * float(fin['FinancialExp_Input' + str(j)]) \
                #* float(fin['FinancialExp_Input' + str(k)])
        #input += 1
        #i += 2
        #j += 1

        x['ActivityAnalysis_Input240'] = - round(float(finreq['FinancialRequirement_Input92']) * (float(fin['FinancialExp_Input116']) /100)* (float(fin['FinancialExp_Input182'])/100))
        x['ActivityAnalysis_Input241'] = - round(float(finreq['FinancialRequirement_Input94']) * (float(fin['FinancialExp_Input117']) /100)* (float(fin['FinancialExp_Input182'])/100))
        x['ActivityAnalysis_Input242'] = - round(float(finreq['FinancialRequirement_Input96']) * (float(fin['FinancialExp_Input118']) /100)* (float(fin['FinancialExp_Input182'])/100))
        x['ActivityAnalysis_Input243'] = - round(float(finreq['FinancialRequirement_Input98']) * (float(fin['FinancialExp_Input119']) /100)* (float(fin['FinancialExp_Input182'])/100))
        x['ActivityAnalysis_Input244'] = - round(float(finreq['FinancialRequirement_Input100'])* (float(fin['FinancialExp_Input120']) /100)* (float(fin['FinancialExp_Input182'])/100))      

        # 17 Financial Expenses:
        input = 245

        i = 225
        j = 230
        k = 235
        l = 240

        while input in range(244, 250) and i in range(224, 230) and j in range(229, 235) and k in range(234, 240) \
            and l in range(239, 250):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) + float(x['ActivityAnalysis_Input' + str(j)]) \
                + float(x['ActivityAnalysis_Input' + str(k)])  + float(x['ActivityAnalysis_Input' + str(l)]),3)

            input += 1

            i += 1
            j += 1
            k += 1
            l += 1  


        # 18 Profit before tax & ex-ord income/loss:
        #input = 252
        #i = 215
        #j = 245
        #k = 2500


        #while input in range(251, 257) and i in range(214, 220) and j in range(244, 250) and k in range(2599, 2505):

            #x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) + float(x['ActivityAnalysis_Input' + str(j)]) \
                #+ float(x['ActivityAnalysis_Input' + str(k)]),3)

            #input += 1

            #i += 1
            #j += 1
            #k += 1


        x['ActivityAnalysis_Input252'] = round(float(x['ActivityAnalysis_Input215']) + float(x['ActivityAnalysis_Input245']) + float(x['ActivityAnalysis_Input2500']),3)
        x['ActivityAnalysis_Input253'] = round(float(x['ActivityAnalysis_Input216']) + float(x['ActivityAnalysis_Input246']) + float(x['ActivityAnalysis_Input2501']),3)
        x['ActivityAnalysis_Input254'] = round(float(x['ActivityAnalysis_Input217']) + float(x['ActivityAnalysis_Input247']) + float(x['ActivityAnalysis_Input2502']),3)
        x['ActivityAnalysis_Input255'] = round(float(x['ActivityAnalysis_Input218']) + float(x['ActivityAnalysis_Input248']) + float(x['ActivityAnalysis_Input2503']),3)
        x['ActivityAnalysis_Input256'] = round(float(x['ActivityAnalysis_Input219']) + float(x['ActivityAnalysis_Input249']) + float(x['ActivityAnalysis_Input2504']),3)
                    
        # 19 Margin:
        input = 257 
        turnover = 31
        Profit = 252

        while input in range(256, 262) and turnover in range(30, 36) and Profit in range(251, 257):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(Profit)]) / float(x['ActivityAnalysis_Input' + str(turnover)]),3)
                x['ActivityAnalysis_Input' + str(input)] = Round

            input += 1
            turnover += 1
            Profit += 1  

            #################################################################################
            #Table 2

        # 1 DAF:
        input_1 = 292
        input_2 = 297

        i = 20
        j = 36

        k = 73

        while input_1 in range(291, 297) and input_2 in range(296, 302) and i in range(19, 25)\
            and j in range(35, 41) and k in range(72, 78):

            x['ActivityAnalysis_Input' + str(input_1)] = round(float(parts['TurnoverParts_Input' + str(i)]) \
                -  float(parts['TurnoverParts_Input' + str(j)]),3)
            
            x['ActivityAnalysis_Input' + str(input_2)] = round(float(services['TurnoverServices_Input' + str(k)]),3)
        
            input_1 += 1
            input_2 += 1

            i += 1
            j += 1

            k += 1

        # 2 OIL:

        x['ActivityAnalysis_Input307'] =  round(float(parts['TurnoverParts_Input25']),3)
        x['ActivityAnalysis_Input308'] =  round(float(parts['TurnoverParts_Input26']),3)
        x['ActivityAnalysis_Input309'] =  round(float(parts['TurnoverParts_Input27']),3)
        x['ActivityAnalysis_Input310'] =  round(float(parts['TurnoverParts_Input28']),3)
        x['ActivityAnalysis_Input311'] =  round(float(parts['TurnoverParts_Input29']),3)                               
  

        # 3 Outsourced workshop activities:

        x['ActivityAnalysis_Input327'] =  round(float(services['TurnoverServices_Input93']),3)
        x['ActivityAnalysis_Input328'] =  round(float(services['TurnoverServices_Input94']),3)
        x['ActivityAnalysis_Input329'] =  round(float(services['TurnoverServices_Input96']),3)
        x['ActivityAnalysis_Input330'] =  round(float(services['TurnoverServices_Input97']),3)
        x['ActivityAnalysis_Input331'] =  round(float(services['TurnoverServices_Input98']),3)

        # 4 Internal:
        input_1 = 337
        input_2 = 342

        i = 78
        j = 41

        while input_1 in range(336, 342) and input_2 in range(341, 347) and i in range \
            (77, 83) and j in range(40, 46):

            x['ActivityAnalysis_Input' + str(input_2)] =  round(float(services['TurnoverServices_Input' + str(i)]),3) 
            x['ActivityAnalysis_Input' + str(input_1)] =  round(float(parts['TurnoverParts_Input' + str(j)]),3)

            input_1 += 1
            input_2 += 1

            i += 1
            j += 1

        # 4 Total turnover:
        input = 352

        i = 292
        j = 307
        k = 322
        l = 337
 


        while input in range(351, 367) and i in range(291, 307) and j in range (306, 322) and k in range(321, 337)\
            and l in range(336, 352):

            x['ActivityAnalysis_Input' + str(input)] =  round(float(x['ActivityAnalysis_Input' + str(i)]) + float(x['ActivityAnalysis_Input' + str(j)]) + \
                float(x['ActivityAnalysis_Input' + str(k)]) + float(x['ActivityAnalysis_Input' + str(l)]))


            input += 1

            i += 1
            j += 1
            k += 1
            l += 1

        # 5 DAF: Daf parts activity contribution

        x["ActivityAnalysis_Input397"] = round(float(activity["ActivityContribution_Input56"]) ,3) 
        x["ActivityAnalysis_Input398"] = round(float(activity["ActivityContribution_Input338"]),3) 
        x["ActivityAnalysis_Input399"] = round(float(activity["ActivityContribution_Input725"]),3) 
        x["ActivityAnalysis_Input400"] = round(float(activity["ActivityContribution_Input1016"]),3) 
        x["ActivityAnalysis_Input401"] = round(float(activity["ActivityContribution_Input1294"]),3)   

        #input = 397

        #i = 157
        #j = 177
        #k = 1870

        #while input in range(396, 402) and i in range(156, 166) and j in range(176, 186):
            #x['ActivityAnalysis_Input' + str(input)] = float(costs['CostOFSales_Input' + str(i)]) + float(costs['CostOFSales_Input' + str(j)])  

        #input += 1
        #i += 2
        #j += 2 
        #k += 2

        # 6 Oil: Oil parts activity contribution
        x["ActivityAnalysis_Input412"] = round(float(activity["ActivityContribution_Input62"]),3)  
        x["ActivityAnalysis_Input413"] = round(float(activity["ActivityContribution_Input344"]),3)
        x["ActivityAnalysis_Input414"] = round(float(activity["ActivityContribution_Input731"]),3)
        x["ActivityAnalysis_Input415"] = round(float(activity["ActivityContribution_Input1022"]),3)
        x["ActivityAnalysis_Input416"] = round(float(activity["ActivityContribution_Input1300"]) ,3)

        #input = 412

        #i = 197 

        #while input in range(411, 417) and i in range(196, 206):
            #x['ActivityAnalysis_Input' + str(input)] = float(costs['CostOFSales_Input' + str(i)]) 

        #input += 1
        #i += 2

        # 7 Salaries Re-check:

        x["ActivityAnalysis_Input432"] = round(float(activity["ActivityContribution_Input69"])  *  float(services['TurnoverServices_Input109'])/100,3) 
        x["ActivityAnalysis_Input433"] = round(float(activity["ActivityContribution_Input351"])  *  float(services['TurnoverServices_Input110'])/100,3)  
        x["ActivityAnalysis_Input434"] = round(float(activity["ActivityContribution_Input738"])  *  float(services['TurnoverServices_Input111'])/100,3)  
        x["ActivityAnalysis_Input435"] = round(float(activity["ActivityContribution_Input1029"])  *  float(services['TurnoverServices_Input112'])/100,3)  
        x["ActivityAnalysis_Input436"] = round(float(activity["ActivityContribution_Input1307"])  *  float(services['TurnoverServices_Input113'])/100,3)   


        #input = 432

        #i = 88
        #j = 109


        #while input in range(431, 437) and i in range(87, 93) and j in range(108, 114):
            #x['ActivityAnalysis_Input' + str(input)] = float(services['TurnoverServices_Input' + str(i)]) * float(services['TurnoverServices_Input' + str(j)]) 

        #input += 1
        #i += 1
        #j += 1  
        

              

        # 8 Bonus:

        x["ActivityAnalysis_Input442"] = round(float(activity["ActivityContribution_Input75"]) ,3)
        x["ActivityAnalysis_Input443"] = round(float(activity["ActivityContribution_Input357"]),3)
        x["ActivityAnalysis_Input444"] = round(float(activity["ActivityContribution_Input743"]) ,3)
        x["ActivityAnalysis_Input445"] = round(float(activity["ActivityContribution_Input1035"]) ,3)
        x["ActivityAnalysis_Input446"] = round(float(activity["ActivityContribution_Input1313"]),3)

        #input = 442

        #i = 237
        #j = 247


        #while input in range(441, 447) and i in range(236, 236) and j in range(246, 256):
            #x['ActivityAnalysis_Input' + str(input)] = float(costs['CostOFSales_Input' + str(i)]) + float(costs['CostOFSales_Input' + str(j)])  

        #input += 1
        #i += 2
        #j += 2  

        # 9 Outsourced:
        x["ActivityAnalysis_Input462"] = round(float(activity["ActivityContribution_Input81"]),3) 
        x["ActivityAnalysis_Input463"] = round(float(activity["ActivityContribution_Input363"]),3) 
        x["ActivityAnalysis_Input464"] = round(float(activity["ActivityContribution_Input750"]) ,3) 
        x["ActivityAnalysis_Input465"] = round(float(activity["ActivityContribution_Input1041"]),3)  
        x["ActivityAnalysis_Input466"] = round(float(activity["ActivityContribution_Input1319"]),3) 

        #input = 462

        #i = 267


        #while input in range(461, 467) and i in range(266, 276):
            #x['ActivityAnalysis_Input' + str(input)] = float(costs['CostOFSales_Input' + str(i)])  

        #input += 1
        #i += 2

        # Selling expenses:
        input_parts = 547
        input_services = 552
        input_admin = 557

        i = 109
        j = 110
        k = 11


        while input_parts in range(546, 552) and input_services in range(551, 557) and input_admin in range(556, 562) \
            and i in range(108, 1348) and j in range(109, 1349) and k in range(110, 1350):

            x['ActivityAnalysis_Input' + str(input_parts)] = round(float(activity['ActivityContribution_Input' + str(i)]),3)
            x['ActivityAnalysis_Input' + str(input_services)] = round(float(activity['ActivityContribution_Input' + str(j)]),3)
            x['ActivityAnalysis_Input' + str(input_admin)] = round(float(activity['ActivityContribution_Input' + str(k)]),3)

            input_parts += 1
            input_services += 1
            input_admin += 1

            i += 1

        # Total Cost of Sales:

        input = 487
        i = 397
        j = 412
        k = 427
        l = 442
        m = 457
        n = 472

        while input in range(486, 502) and i in range(396, 412) and j in range(411, 427) and k in range(426, 442)\
            and l in range(441, 457) and m in range(456, 472) and n in range(471, 487):

            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) + \
                float(x['ActivityAnalysis_Input' + str(j)]) + float(x['ActivityAnalysis_Input' + str(k)]) + \
                    float(x['ActivityAnalysis_Input' + str(l)]) + float(x['ActivityAnalysis_Input' + str(m)]) + \
                        float(x['ActivityAnalysis_Input' + str(n)]))

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1                       


        # Gross Profit/Loss :
        input = 502
        turnover = 352
        costs = 487

        while input in range(501, 517) and turnover in range(351, 367) and costs in range(486, 502):
            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(turnover)]) - float(x['ActivityAnalysis_Input' + str(costs)]),3)

            input += 1
            turnover += 1
            costs += 1

        # Margin :
        input = 517
        turnover = 352
        gross_pl = 502

        while input in range(516, 532) and turnover in range(351, 367) and gross_pl in range(501, 517):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(gross_pl)]) / float(x['ActivityAnalysis_Input' + str(turnover)]),3)
                x['ActivityAnalysis_Input' + str(input)] = Round

            input += 1
            turnover += 1
            gross_pl += 1  


        # Salaries & wages:
        input_parts = 532
        input_services = 537
        input_admin = 542

        i = 5
        j = 160
        k = 161
        l = 162

        while input_parts in range(531, 537) and input_services in range(536, 542) and input_admin in range(541, 547) \
            and i in range(4, 10):

            x['ActivityAnalysis_Input' + str(input_parts)] = round(float(selling['SellingOperation_Input' + str(i)]) * float(selling['SellingOperation_Input' + str(j)]),3)
            x['ActivityAnalysis_Input' + str(input_services)] = round(float(selling['SellingOperation_Input' + str(i)]) * float(selling['SellingOperation_Input' + str(k)]),3)
            x['ActivityAnalysis_Input' + str(input_admin)] = round(float(selling['SellingOperation_Input' + str(i)]) * float(selling['SellingOperation_Input' + str(l)]),3)

            input_parts += 1
            input_services += 1
            input_admin += 1

            i += 1  

        
        #salaire:
        x['ActivityAnalysis_Input547'] = round(float(activity['ActivityContribution_Input110']))
        x['ActivityAnalysis_Input548'] = round(float(activity['ActivityContribution_Input398']))  
        x['ActivityAnalysis_Input549'] = round(float(activity['ActivityContribution_Input779']))
        x['ActivityAnalysis_Input550'] = round(float(activity['ActivityContribution_Input1070']))
        x['ActivityAnalysis_Input551'] = round(float(activity['ActivityContribution_Input1348']))

        #salaire:
        x['ActivityAnalysis_Input552'] = round(float(activity['ActivityContribution_Input111']))
        x['ActivityAnalysis_Input553'] = round(float(activity['ActivityContribution_Input399']))  
        x['ActivityAnalysis_Input554'] = round(float(activity['ActivityContribution_Input780']))
        x['ActivityAnalysis_Input555'] = round(float(activity['ActivityContribution_Input1071']))
        x['ActivityAnalysis_Input556'] = round(float(activity['ActivityContribution_Input1349']))

        x['ActivityAnalysis_Input557'] = round(float(activity['ActivityContribution_Input112']))
        x['ActivityAnalysis_Input558'] = round(float(activity['ActivityContribution_Input400']))  
        x['ActivityAnalysis_Input559'] = round(float(activity['ActivityContribution_Input781']))
        x['ActivityAnalysis_Input560'] = round(float(activity['ActivityContribution_Input1072']))
        x['ActivityAnalysis_Input561'] = round(float(activity['ActivityContribution_Input1350']))

        # other operating expenses:
 
        # parts:

        input_1 = 578
        input_2 = 579
        input_3 = 580
        input_4 = 581
        input_5 = 582

        i = 122
        j = 500
        k = 791
        l = 1082
        m = 1360

        while input_1 in range(577, 834) and input_2 in range(578, 835) and input_3 in range(579, 836) \
            and input_4 in range(580, 837) and input_5 in range(581, 838) and i in range(121, 225) and \
                j in range(499, 603) and k in range(790, 895) and l in range(1081, 1185) and m in range(1359, 1463):

            x['ActivityAnalysis_Input' + str(input_1)] = round(float(activity['ActivityContribution_Input' + str(i)]),3)
            x['ActivityAnalysis_Input' + str(input_2)] = round(float(activity['ActivityContribution_Input' + str(j)]) ,3)
            x['ActivityAnalysis_Input' + str(input_3)] = round(float(activity['ActivityContribution_Input' + str(k)]),3)
            x['ActivityAnalysis_Input' + str(input_4)] = round(float(activity['ActivityContribution_Input' + str(l)]) ,3)
            x['ActivityAnalysis_Input' + str(input_5)] = round(float(activity['ActivityContribution_Input' + str(m)]),3)                                                                                      
        
            input_1 += 15
            input_2 += 15
            input_3 += 15
            input_4 += 15
            input_5 += 15

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6 

        # services:

        input_1 = 583
        input_2 = 584
        input_3 = 585
        input_4 = 586
        input_5 = 587

        i = 123
        j = 501
        k = 792
        l = 1083
        m = 1361

        while input_1 in range(582, 839) and input_2 in range(583, 840) and input_3 in range(584, 841) \
            and input_4 in range(585, 842) and input_5 in range(586, 843) and i in range(122, 226) and \
                j in range(500, 604) and k in range(791, 896) and l in range(1082, 1186) and m in range(1360, 1464):

            x['ActivityAnalysis_Input' + str(input_1)] = round(float(activity['ActivityContribution_Input' + str(i)]),3)
            x['ActivityAnalysis_Input' + str(input_2)] = round(float(activity['ActivityContribution_Input' + str(j)]),3)
            x['ActivityAnalysis_Input' + str(input_3)] = round(float(activity['ActivityContribution_Input' + str(k)]),3)
            x['ActivityAnalysis_Input' + str(input_4)] = round(float(activity['ActivityContribution_Input' + str(l)]),3)
            x['ActivityAnalysis_Input' + str(input_5)] = round(float(activity['ActivityContribution_Input' + str(m)]),3)                                                                                      
        
            input_1 += 15
            input_2 += 15
            input_3 += 15
            input_4 += 15
            input_5 += 15

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6 

        # admin:

        input_1 = 588
        input_2 = 589
        input_3 = 590
        input_4 = 591
        input_5 = 592

        i = 124
        j = 502
        k = 793
        l = 1084
        m = 1362

        while input_1 in range(587, 844) and input_2 in range(588, 845) and input_3 in range(589, 846) \
            and input_4 in range(590, 847) and input_5 in range(591, 848) and i in range(123, 227) and \
                j in range(501, 605) and k in range(792, 896) and l in range(1083, 1187) and m in range(1361, 1465):

            x['ActivityAnalysis_Input' + str(input_1)] = round(float(activity['ActivityContribution_Input' + str(i)]),3)
            x['ActivityAnalysis_Input' + str(input_2)] = round(float(activity['ActivityContribution_Input' + str(j)]),3) 
            x['ActivityAnalysis_Input' + str(input_3)] = round(float(activity['ActivityContribution_Input' + str(k)]),3)
            x['ActivityAnalysis_Input' + str(input_4)] = round(float(activity['ActivityContribution_Input' + str(l)]),3) 
            x['ActivityAnalysis_Input' + str(input_5)] = round(float(activity['ActivityContribution_Input' + str(m)]),3)                                                                                      
        
            input_1 += 15
            input_2 += 15
            input_3 += 15
            input_4 += 15
            input_5 += 15

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6

        # Total other operating expenses:
        # parts:

        i = 578
        j = 579
        k = 580
        l = 581
        m = 582

        n = 848
        o = 849
        p = 850
        q = 851
        r = 852

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []        


        while i in range(577, 834) and j in range(578, 835) and k in range(579, 836) and l in range(580, 837) and m in range(581, 838):

            total_i.append(float(x['ActivityAnalysis_Input' + str(i)]))
            total_j.append(float(x['ActivityAnalysis_Input' + str(j)]))
            total_k.append(float(x['ActivityAnalysis_Input' + str(k)]))
            total_l.append(float(x['ActivityAnalysis_Input' + str(l)]))
            total_m.append(float(x['ActivityAnalysis_Input' + str(m)]))            

            x['ActivityAnalysis_Input' + str(n)] = round(sum(total_i))
            x['ActivityAnalysis_Input' + str(o)] = round(sum(total_j))           
            x['ActivityAnalysis_Input' + str(p)] = round(sum(total_k))
            x['ActivityAnalysis_Input' + str(q)] = round(sum(total_l))
            x['ActivityAnalysis_Input' + str(r)] = round(sum(total_m)) 

            i += 15
            j += 15
            k += 15
            l += 15
            m += 15 

        #  services:

      
        i = 583
        j = 584
        k = 585
        l = 586
        m = 587

        n = 853
        o = 854
        p = 855
        q = 856
        r = 857

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []        


        while i in range(582, 839) and j in range(583, 840) and k in range(584, 841) and l in range(585, 842) and m in range(586, 843):

            total_i.append(float(x['ActivityAnalysis_Input' + str(i)]))
            total_j.append(float(x['ActivityAnalysis_Input' + str(j)]))
            total_k.append(float(x['ActivityAnalysis_Input' + str(k)]))
            total_l.append(float(x['ActivityAnalysis_Input' + str(l)]))
            total_m.append(float(x['ActivityAnalysis_Input' + str(m)]))            

            x['ActivityAnalysis_Input' + str(n)] = round(sum(total_i),3)
            x['ActivityAnalysis_Input' + str(o)] = round(sum(total_j),3)           
            x['ActivityAnalysis_Input' + str(p)] = round(sum(total_k),3)
            x['ActivityAnalysis_Input' + str(q)] = round(sum(total_l),3) 
            x['ActivityAnalysis_Input' + str(r)] = round(sum(total_m) ,3)

            i += 15
            j += 15
            k += 15
            l += 15
            m += 15  


        #  admin:

      
        i = 588
        j = 589
        k = 590
        l = 591
        m = 592   

        n = 858
        o = 859
        p = 860
        q = 861
        r = 862

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []        


        while i in range(582, 844) and j in range(583, 845) and k in range(584, 846) and l in range(585, 847) and m in range(586, 848):

            total_i.append(float(x['ActivityAnalysis_Input' + str(i)]))
            total_j.append(float(x['ActivityAnalysis_Input' + str(j)]))
            total_k.append(float(x['ActivityAnalysis_Input' + str(k)]))
            total_l.append(float(x['ActivityAnalysis_Input' + str(l)]))
            total_m.append(float(x['ActivityAnalysis_Input' + str(m)]))            

            x['ActivityAnalysis_Input' + str(n)] = round(sum(total_i),3)
            x['ActivityAnalysis_Input' + str(o)] = round(sum(total_j),3)           
            x['ActivityAnalysis_Input' + str(p)] = round(sum(total_k),3)
            x['ActivityAnalysis_Input' + str(q)] = round(sum(total_l),3) 
            x['ActivityAnalysis_Input' + str(r)] = round(sum(total_m) ,3)

            i += 15
            j += 15
            k += 15
            l += 15
            m += 15   

        # Depreciations & Amortization:
        # Parts:

        x['ActivityAnalysis_Input863'] = round(float(inv['InvDep_Input302']),3)
        x['ActivityAnalysis_Input864'] = round(float(inv['InvDep_Input303']),3)
        x['ActivityAnalysis_Input865'] = round(float(inv['InvDep_Input304']),3)
        x['ActivityAnalysis_Input866'] = round(float(inv['InvDep_Input305']),3)
        x['ActivityAnalysis_Input867'] = round(float(inv['InvDep_Input306']),3)                                

        # Admin:

        x['ActivityAnalysis_Input873'] = round(float(inv['InvDep_Input230']) + float(inv['InvDep_Input278']) + float(inv['InvDep_Input284']) + float(inv['InvDep_Input314']),3)
        x['ActivityAnalysis_Input874'] = round(float(inv['InvDep_Input231']) + float(inv['InvDep_Input279']) + float(inv['InvDep_Input285']) + float(inv['InvDep_Input315']),3)
        x['ActivityAnalysis_Input875'] = round(float(inv['InvDep_Input232']) + float(inv['InvDep_Input280']) + float(inv['InvDep_Input286']) + float(inv['InvDep_Input316']),3)
        x['ActivityAnalysis_Input876'] = round(float(inv['InvDep_Input233']) + float(inv['InvDep_Input281']) + float(inv['InvDep_Input287']) + float(inv['InvDep_Input317']),3)
        x['ActivityAnalysis_Input877'] = round(float(inv['InvDep_Input234']) + float(inv['InvDep_Input282']) + float(inv['InvDep_Input288']) + float(inv['InvDep_Input318']),3)        

        # Operating profit/loss per activity:
        input = 878
        i = 502
        j = 532
        k = 547
        l = 848
        m = 863

        while input in range(877, 893) and i in range(501, 517) and j in range(531, 547) and k in range(546, 562) and l in range(847, 863) and m in range(862, 878):
            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) - float(x['ActivityAnalysis_Input' + str(j)]) \
                - float(x['ActivityAnalysis_Input' + str(k)]) - float(x['ActivityAnalysis_Input' + str(l)]) - float(x['ActivityAnalysis_Input' + str(m)]),3)

            input += 1 
            i += 1 
            j += 1 
            k += 1 
            l += 1 
            m += 1 

        #margin:

        input = 893 
        turnover = 352
        gross_pl = 878

        while input in range(892, 908) and turnover in range(351, 367) and gross_pl in range(877, 893):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(gross_pl)]) / float(x['ActivityAnalysis_Input' + str(turnover)]),3)
                x['ActivityAnalysis_Input' + str(input)] = Round

            input += 1
            turnover += 1
            gross_pl += 1

        #ST loans
        x['ActivityAnalysis_Input918'] = -round(float(fin['FinancialExp_Input152']),3)     
        x['ActivityAnalysis_Input919'] = -round(float(fin['FinancialExp_Input154']),3)   
        x['ActivityAnalysis_Input920'] = -round(float(fin['FinancialExp_Input156']),3)  
        x['ActivityAnalysis_Input921'] = -round(float(fin['FinancialExp_Input158']),3)  
        x['ActivityAnalysis_Input922'] = -round(float(fin['FinancialExp_Input160']),3)  

        #LT loans
        x['ActivityAnalysis_Input933'] = -round(float(fin['FinancialExp_Input162']),3)       
        x['ActivityAnalysis_Input934'] = -round(float(fin['FinancialExp_Input164']) ,3)  
        x['ActivityAnalysis_Input935'] = -round(float(fin['FinancialExp_Input166']),3)  
        x['ActivityAnalysis_Input936'] = -round(float(fin['FinancialExp_Input168']),3)  
        x['ActivityAnalysis_Input937'] = -round(float(fin['FinancialExp_Input170']),3)    

        #Subordinated loans
        x['ActivityAnalysis_Input948'] = round(float(fin['FinancialExp_Input173']) ,3)      
        x['ActivityAnalysis_Input949'] = round(float(fin['FinancialExp_Input175']) ,3)  
        x['ActivityAnalysis_Input950'] = round(float(fin['FinancialExp_Input177']),3)  
        x['ActivityAnalysis_Input951'] = round(float(fin['FinancialExp_Input179']),3)  
        x['ActivityAnalysis_Input952'] = round(float(fin['FinancialExp_Input181']),3)    

        #Financial Expenses:

        input = 968
        i = 908
        j = 923
        k = 938
        l = 953

        while input in range(967, 983) and i in range(907, 923) and j in range(922, 938) and k in range(937, 953)and l in range(952, 968):
            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) + float(x['ActivityAnalysis_Input' + str(j)]) \
                + float(x['ActivityAnalysis_Input' + str(k)]) + float(x['ActivityAnalysis_Input' + str(l)]),3)

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1

        # Profit/loss before tax & extra-ord :
        input = 998
        i = 878
        j = 968
        k = 983


        while input in range(997, 1013) and i in range(877, 893) and j in range(967, 983) and k in range(982, 998):
            x['ActivityAnalysis_Input' + str(input)] = round(float(x['ActivityAnalysis_Input' + str(i)]) + float(x['ActivityAnalysis_Input' + str(j)]) \
                + float(x['ActivityAnalysis_Input' + str(k)]),3)

            input += 1
            i += 1
            j += 1
            k += 1

        # Margin :
        input = 1013
        turnover = 352
        gross_pl = 998

        while input in range(1012, 1028) and turnover in range(351, 367) and gross_pl in range(997, 1013):

            if  float(x['ActivityAnalysis_Input' + str(turnover)]) == 0:
                x['ActivityAnalysis_Input' + str(input)] = 0
            else:
                Round = round(float(x['ActivityAnalysis_Input' + str(gross_pl)]) / float(x['ActivityAnalysis_Input' + str(turnover)])*100,1)
                x['ActivityAnalysis_Input' + str(input)] = Round
            input += 1
            turnover += 1
            gross_pl += 1 


        
        current_db.activityanalysis.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.activityanalysis.find_one({"GlobalId": "global"})
    return redirect(url_for('activityanalysis.activityanalysis')) 
    return render_template("activity-analysis.html", data=x, user=user) 




####################################################################################

@activityanalysis_bp.route('/activityanalysis/delete',  methods=['POST'])
@login_required
def activityanalysis_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.activityanalysis.delete_many({})
    return redirect(url_for('activityanalysis.activityanalysis'))    
    return render_template("activity-analysis.html", data=x) 
