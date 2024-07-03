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

ratiobalance_bp = Blueprint('ratiobalance', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["ratiobalance"]

@ratiobalance_bp.route('/ratiobalance', methods=['GET', 'POST'])
@login_required
def ratiobalance():
    """
    Create new collection in the database
    """    
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["RatioBalance_Header1"] = (int(ref["basic_year"])) 
    x["RatioBalance_Header2"] = (int(ref["basic_year"]) + 1 )
    x["RatioBalance_Header3"] = (int(ref["basic_year"]) + 2 )
    x["RatioBalance_Header4"] = (int(ref["basic_year"]) + 3 )
    x["RatioBalance_Header5"] = (int(ref["basic_year"]) + 4 )

    i = 1
    lst = []
    while(i <405):
        lst.append(("RatioBalance" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x)                                   

    current_db.ratiobalance.insert_one(x)
    x = current_db.ratiobalance.find_one({"GlobalId": "global"})
    return render_template("ratio-balance.html", data=x)       



####################################################################################

@ratiobalance_bp.route('/ratiobalance/update', methods=['GET', 'POST'])
@login_required
def ratiobalance_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        #needed collections
        pl = current_db.pl.find_one({"GlobalId": "global"})
        balance = current_db.balanceliabilities.find_one({"GlobalId": "global"})
        finreq = current_db.financialrequirements.find_one({"GlobalId": "global"}) 
        costs = current_db.costofsale.find_one({"GlobalId": "global"})
        fin = current_db.financialincome.find_one({"GlobalId": "global"})  
        salaries = current_db.salaries.find_one({"GlobalId": "global"})
        services = current_db.turnoverservices.find_one({"GlobalId": "global"})      
        parts = current_db.turnoverpart.find_one({"GlobalId": "global"})
        activity = current_db.activitycontribution.find_one({"GlobalId": "global"})
        income = current_db.financialincome.find_one({"GlobalId": "global"})
        balance_assets = current_db.balanceassets.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})
        dealerbench = current_db.dealerbenchmark.find_one({"GlobalId": "global"})

        x["RatioBalance_Header1"] = (int(ref["basic_year"])) 
        x["RatioBalance_Header2"] = (int(ref["basic_year"]) + 1 )
        x["RatioBalance_Header3"] = (int(ref["basic_year"]) + 2 )
        x["RatioBalance_Header4"] = (int(ref["basic_year"]) + 3 )
        x["RatioBalance_Header5"] = (int(ref["basic_year"]) + 4 )        

        #1. Change of turnover:
        input = 2
        i = 1
        j = 2

        while input in range(1, 6) and i in range(0, 6) and j in range(1, 6):
            if float(pl["PL_Input" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round((float(pl["PL_Input" + str(j)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)

            input += 1
            i += 1
            j += 1

        #2. Margins:
        input_1 = 11
        input_2 = 16
        input_3 = 21 
        input_4 = 26
        input_5 = 31


        i = 1
        j = 11
        k = 36
        l = 46
        m = 66
        n = 76


        while input_1 in range(10, 16) and input_2 in range(15, 21) and input_3 in range(20, 26) and input_4 in range(25, 31) and input_5 in range(30, 36) \
            and i in range(0, 6) and j in range(10, 16) and k in range(35, 41) and l in range(45, 51) and m in range(65, 71) and n in range(75, 81):

            if float(pl["PL_Input" + str(i)]) == 0:

                x["RatioBalance" + str(input_1)] = 0
                x["RatioBalance" + str(input_2)] = 0
                x["RatioBalance" + str(input_3)] = 0
                x["RatioBalance" + str(input_4)] = 0
                x["RatioBalance" + str(input_5)] = 0

            else:
                #x["RatioBalance" + str(input_1)] = round((float(pl["PL_Input" + str(j)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)
                #x["RatioBalance" + str(input_2)] = round((float(pl["PL_Input" + str(k)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)
                #x["RatioBalance" + str(input_3)] = round((float(pl["PL_Input" + str(l)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)
                #x["RatioBalance" + str(input_4)] = round((float(pl["PL_Input" + str(m)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)
                #x["RatioBalance" + str(input_5)] = round((float(pl["PL_Input" + str(n)]) - float(pl["PL_Input" + str(i)])) / float(pl["PL_Input" + str(i)]),3)

                x["RatioBalance" + str(input_1)] = round((float(pl["PL_Input" + str(j)]) ) / float(pl["PL_Input" + str(i)]),3)
                x["RatioBalance" + str(input_2)] = round((float(pl["PL_Input" + str(k)]) ) / float(pl["PL_Input" + str(i)]),3)
                x["RatioBalance" + str(input_3)] = round((float(pl["PL_Input" + str(l)]) ) / float(pl["PL_Input" + str(i)]),3)
                x["RatioBalance" + str(input_4)] = round((float(pl["PL_Input" + str(m)]) ) / float(pl["PL_Input" + str(i)]),3)
                x["RatioBalance" + str(input_5)] = round((float(pl["PL_Input" + str(n)]) ) / float(pl["PL_Input" + str(i)]),3)

            input_1 += 1
            input_2 += 1
            input_3 += 1
            input_4 += 1
            input_5 += 1


            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1   

        # 3.1 Profit before tax / Equity (= ROE or ROI):
        input = 41
        i = 401
        j = 66

        while input in range(40, 46) and i in range(400, 406) and j in range(65, 71):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(float(pl["PL_Input"+ str(j)]) / float(balance["BalanceLiabilitiesInput" + str(i)]),3)
            input += 1
            i += 1
            j += 1 
        

        # 3.2 Net profit / Equity:
        input = 46
        i = 401
        j = 76

        while input in range(45, 51) and i in range(400, 406) and j in range(75, 81):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(float(pl["PL_Input"+ str(j)]) / float(balance["BalanceLiabilitiesInput" + str(i)]),3)

            input += 1
            i += 1
            j += 1  
           
        # 3.3 Bénéfice avant intérêts et impôts / Fonds permanents (= ROCE ou ROA):
        input = 51
        i = 62
        j = 66
        k = 193       

        while input in range(50, 56) and i in range(61, 67) and j in range(65, 71) and k in range(192, 202):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(((float(pl["PL_Input"+ str(j)]) - float(income["FinancialExp_Input" + str(k)])) / float(balance["BalanceLiabilitiesInput" + str(i)])),3)   
            input += 1
            i += 1
            j += 1
            k += 2

        # 4.1 Rapport actuel:
        input = 61
        i = 92
        j = 104

        while input in range(60, 66) and i in range(91, 97) and j in range(103, 109):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(float(balance_assets["BalanceAssetsInput" + str(j)]) / float(balance["BalanceLiabilitiesInput" + str(i)]),3)

            input += 1
            i += 1
            j += 1

        #4.2 Rapport rapide:
        input = 66
        i = 92
        j = 104
        k = 80

        while input in range(65, 71) and i in range(91, 97) and j in range(103, 109) and k in range(79, 85):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(((float(balance_assets["BalanceAssetsInput" + str(j)])) - (float(balance_assets["BalanceAssetsInput" + str(k)]))) / float(balance["BalanceLiabilitiesInput" + str(i)]),3)

            input += 1
            i += 1
            j += 1  
            k += 1

        #4.3 Fonds de roulement:
        input = 71
        i = 92
        j = 104

        while input in range(70, 76) and i in range(91, 97) and j in range(103, 109):
            x["RatioBalance" + str(input)] = round((float(balance_assets["BalanceAssetsInput" + str(j)])) - (float(balance["BalanceLiabilitiesInput" + str(i)])),3)  

            input += 1
            i += 1
            j += 1  

        # 5.1.3 Pièces: 
        #input = 91
        #i = 74
        #j = 281

        #while input in range(90, 96) and i in range(73, 79) and j in range(280, 286):
            #if float(costs["CostOFSales_Input" + str(j)]) == 0:
                #x["RatioBalance" + str(input)] = 0
            #else:
                #x["RatioBalance" + str(input)] = round(float(balance_assets["BalanceAssetsInput" + str(i)]) / float(costs["CostOFSales_Input"+ str(j)] * 365),3)


            #input += 1
            #i += 1
            #j += 1

        if float(balance_assets["BalanceAssetsInput74"]) == 0:
            x["RatioBalance91"] = 0
        else:
            x["RatioBalance91"] = round((float(balance_assets["BalanceAssetsInput74"]) / (float(costs["CostOFSales_Input281"])) * 365)) 

        if float(balance_assets["BalanceAssetsInput75"]) == 0:
            x["RatioBalance92"] = 0  
        else:           
            x["RatioBalance92"] = round((float(balance_assets["BalanceAssetsInput75"]) / (float(costs["CostOFSales_Input282"])) * 365))    

        if float(balance_assets["BalanceAssetsInput76"]) == 0:
            x["RatioBalance93"] = 0  
        else:                 
            x["RatioBalance93"] = round((float(balance_assets["BalanceAssetsInput76"]) / (float(costs["CostOFSales_Input283"])) * 365))

        if float(balance_assets["BalanceAssetsInput77"]) == 0:
            x["RatioBalance94"] = 0  
        else:               
            x["RatioBalance94"] = round((float(balance_assets["BalanceAssetsInput77"]) / (float(costs["CostOFSales_Input284"])) * 365))  

        if float(balance_assets["BalanceAssetsInput78"]) == 0:
            x["RatioBalance95"] = 0  
        else:               
            x["RatioBalance95"] = round((float(balance_assets["BalanceAssetsInput78"]) / (float(costs["CostOFSales_Input285"])) * 365))                          

        # 5.2 Jours d'encours des ventes (DSO): 
        #input = 96
        #i = 1
        #j = 86

        #while input in range(95, 101) and i in range(0, 6) and j in range(95, 101):
            #if float(pl["PL_Input" + str(i)]) == 0:
                #x["RatioBalance" + str(input)] = 0
            #else:
                #x["RatioBalance" + str(input)] = round(float(balance_assets["BalanceAssetsInput" + str(j)]) / float(pl["PL_Input"+ str(i)] * 365),3)
            #input += 1
            #i += 1
            #j += 1   

          

        if float(pl["PL_Input1"]) == 0:
            x["RatioBalance96"] = 0
        else:   
            x["RatioBalance96"] = round((float(balance_assets["BalanceAssetsInput86"])) / float(pl["PL_Input1"]) * 365)  

        if float(balance_assets["BalanceAssetsInput87"]) == 0 or float(pl["PL_Input2"]) == 0:
            x["RatioBalance97"] = 0  
        else:   
            x["RatioBalance97"] = round((float(balance_assets["BalanceAssetsInput87"])) / float(pl["PL_Input2"]) * 365)  

        if float(balance_assets["BalanceAssetsInput88"]) == 0 or float(pl["PL_Input3"]) == 0:
            x["RatioBalance98"] = 0  
        else:   
            x["RatioBalance98"] = round((float(balance_assets["BalanceAssetsInput88"])) / float(pl["PL_Input3"]) * 365)

        if float(balance_assets["BalanceAssetsInput89"]) == 0 or float(pl["PL_Input4"]) == 0:
            x["RatioBalance99"] = 0  
        else:             
            x["RatioBalance99"] = round((float(balance_assets["BalanceAssetsInput89"])) / float(pl["PL_Input5"]) * 365)

        if float(balance_assets["BalanceAssetsInput90"]) == 0 or float(pl["PL_Input5"]) == 0:
            x["RatioBalance100"] = 0  
        else:             
            x["RatioBalance100"] = round((float(balance_assets["BalanceAssetsInput90"])) / float(pl["PL_Input5"]) * 365)


        #5.1.1 New trucks:

        x["RatioBalance86"] = round(float(finreq["FinancialRequirement_Input91"]),3)
        x["RatioBalance87"] = round(float(finreq["FinancialRequirement_Input93"]),3)
        x["RatioBalance88"] = round(float(finreq["FinancialRequirement_Input95"]),3)
        x["RatioBalance89"] = round(float(finreq["FinancialRequirement_Input97"]),3)
        x["RatioBalance90"] = round(float(finreq["FinancialRequirement_Input99"]),3)

        #5.3 Days payables outstanding (DPO):
        input = 101

        i = 131
        j = 141
        k = 151
        l = 171

        m = 132
        n = 142
        o = 152
        p = 172

        while input in range(100, 106) and i in range(130, 140) and j in range(140, 150) and k in range(150, 160) and l in range(170, 180) and m in range(131, 141) and n in range(141, 151)\
            and o in range(151, 161) and p in range(171, 181):

            x["RatioBalance" + str(input)] = round(((float(finreq["FinancialRequirement_Input" + str(i)]) * float(finreq["FinancialRequirement_Input" + str(m)])) \
                + (float(finreq["FinancialRequirement_Input" + str(j)]) * float(finreq["FinancialRequirement_Input" + str(n)])) + \
                    (float(finreq["FinancialRequirement_Input" + str(k)]) * float(finreq["FinancialRequirement_Input" + str(o)])) + \
                        (float(finreq["FinancialRequirement_Input" + str(l)]) * float(finreq["FinancialRequirement_Input" + str(p)]))),3)
        
            input += 1

            i += 2
            j += 2
            k += 2
            l += 2

            m += 2
            n += 2
            o += 2
            p += 2  

        x["RatioBalance101"] = round((float(dealerbench["DealerBenchmarkInput62"])))
        x["RatioBalance102"] = round((float(dealerbench["DealerBenchmarkInput63"])))
        x["RatioBalance103"] = round((float(dealerbench["DealerBenchmarkInput64"])))
        x["RatioBalance104"] = round((float(dealerbench["DealerBenchmarkInput65"])))    
        x["RatioBalance105"] = round((float(dealerbench["DealerBenchmarkInput66"])))                

        #6. Solvency:
        input = 106
        i = 401
        j = 104

        while input in range(105, 111) and i in range(400, 406) and j in range(103, 109):
            if float(balance["BalanceLiabilitiesInput" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(float(balance["BalanceLiabilitiesInput" + str(i)]) / float(balance["BalanceLiabilitiesInput" + str(j)]),3)
        
            input += 1
            i += 1
            j += 1

        #7. Interest coverage:
        input = 121
        i = 193
        j = 66

        while input in range(120, 126) and i in range(192, 202) and j in range(65, 71):
            if float(fin["FinancialExp_Input" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round((float(pl["PL_Input" + str(j)]) + float(fin["FinancialExp_Input" + str(i)])) / float(fin["FinancialExp_Input" + str(i)]),3)
        
            input += 1
            i += 2
            j += 1  

        #8. Salaries & Wages / Gross margin:


            if (float(pl["PL_Input11"]) + float(activity["ActivityContribution_Input72"]) ) == 0:
                x["RatioBalance126"] = 0
            else:
                x["RatioBalance126"] = round(float(salaries["Salaries_Input490"]) / ( (float(pl["PL_Input11"]) + float(activity["ActivityContribution_Input72"]) )),3)                         


            if (float(pl["PL_Input12"]) + float(activity["ActivityContribution_Input354"]) ) == 0:
                x["RatioBalance127"] = 0
            else:
                x["RatioBalance127"] = round(float(salaries["Salaries_Input491"]) / ( (float(pl["PL_Input12"]) + float(activity["ActivityContribution_Input354"]) )),3)  

            if (float(pl["PL_Input13"]) + float(activity["ActivityContribution_Input741"]) ) == 0:
                x["RatioBalance128"] = 0
            else:
                x["RatioBalance128"] = round(float(salaries["Salaries_Input492"]) / ( (float(pl["PL_Input13"]) + float(activity["ActivityContribution_Input741"]) )),3)

            if (float(pl["PL_Input14"]) + float(activity["ActivityContribution_Input1032"]) ) == 0:
                x["RatioBalance129"] = 0
            else:
                x["RatioBalance129"] = round(float(salaries["Salaries_Input493"]) / ( (float(pl["PL_Input14"]) + float(activity["ActivityContribution_Input1032"]) )),3) 

            if (float(pl["PL_Input15"]) + float(activity["ActivityContribution_Input1310"]) ) == 0:
                x["RatioBalance130"] = 0
            else:
                x["RatioBalance130"] = round(float(salaries["Salaries_Input494"]) / ( (float(pl["PL_Input15"]) + float(activity["ActivityContribution_Input1310"]) )),3)                                                            

        # B. Operational ratios:
        #1. Service retention:
        input = 131
        i = 21

        while input in range(130, 136) and i in range(20, 26):
            x["RatioBalance" + str(input)] = round(float(services["TurnoverServices_Input" + str(i)]),3)
            input += 1
            i += 1        

        #2. Rétention de pièces:
        input = 136
        i = 15

        while input in range(135, 141) and i in range(14, 20):
            x["RatioBalance" + str(input)] = round(float(parts["TurnoverParts_Input" + str(i)]),3)
            input += 1
            i += 1  

        #3. Atelier productivité:
        input = 141
        i = 114

        while input in range(140, 145) and i in range(113, 118):
            x["RatioBalance" + str(input)] = round(float(services["TurnoverServices_Input" + str(i)]),3)
            input += 1
            i += 1 

        x["RatioBalance145"] = round(float(services["TurnoverServices_Input119"]),3)
        #Bénéfice / perte brut total:

        x["RatioBalance151"] = round(float(activity["ActivityContribution_Input102"]),3)
        x["RatioBalance152"] = round(float(activity["ActivityContribution_Input390"]),3)
        x["RatioBalance153"] = round(float(activity["ActivityContribution_Input771"]),3)
        x["RatioBalance154"] = round(float(activity["ActivityContribution_Input1062"]),3)
        x["RatioBalance155"] = round(float(activity["ActivityContribution_Input1340"]),3)

        #Bénéfice brut corrigé des ventes de véhicules
        x["RatioBalance156"] = round(float(activity["ActivityContribution_Input97"]),3)
        x["RatioBalance157"] = round(float(activity["ActivityContribution_Input385"]),3)
        x["RatioBalance158"] = round(float(activity["ActivityContribution_Input766"]),3)
        x["RatioBalance159"] = round(float(activity["ActivityContribution_Input1057"]),3)
        x["RatioBalance160"] = round(float(activity["ActivityContribution_Input1335"]),3)
                                
        #Marge de correction préparation véhicules neufs:
        input = 400
        i = 120
        j = 41
        k = 78
        l = 177
        m = 231
        n = 43

        while input in range(399, 405) and i in range(119, 125) and j in range(40, 46)\
            and k in range(77, 83) and l in range(176, 187) and m in range(231, 237) and n in range(42, 48):
       
            if float(services["TurnoverServices_Input" + str(i)]) == 0:
                x["RatioBalance" + str(input)] = 0
            else:
                x["RatioBalance" + str(input)] = round(((float(parts["TurnoverParts_Input" + str(j)])) + float(services["TurnoverServices_Input" + str(k)])) \
                    - ((float(costs["CostOFSales_Input" + str(l)]))) - (( float(salaries["Salaries_Input" + str(m)])/ float(services["TurnoverServices_Input" + str(i)])) * float(services["TurnoverServices_Input" + str(n)])),3)

            input += 1
            i += 1
            j += 1
            k += 1
            l += 2
            m += 1
            n += 1

        #Marge brute totale hors ventes de véhicules (1):
        i = 161
        j = 151
        k = 156
        l = 400

        while i in range(160, 166) and j in range(150, 156) and k in range(155, 161) and l in range(399, 405):
            x["RatioBalance" + str(i)] = round(float(x["RatioBalance" + str(j)]) - float(x["RatioBalance" + str(k)]) - float(x["RatioBalance" + str(l)]),3)
            i += 1
            j += 1
            k += 1
        #Frais de vente:
        input = 166
        i = 108

        while input in range(165, 171) and i in range(107, 120):
            x["RatioBalance" + str(input)] = round(float(services["TurnoverServices_Input" + str(i)]),3)
            input += 1
            i += 1 

        x["RatioBalance166"] = round(float(activity["ActivityContribution_Input108"]),3)
        x["RatioBalance167"] = round(float(activity["ActivityContribution_Input396"]),3)
        x["RatioBalance168"] = round(float(activity["ActivityContribution_Input777"]),3)
        x["RatioBalance169"] = round(float(activity["ActivityContribution_Input1068"]),3)
        x["RatioBalance170"] = round(float(activity["ActivityContribution_Input1346"]),3)

        #Salaires et rémunerations:
        x["RatioBalance171"] = round(float(activity["ActivityContribution_Input113"]),3)
        x["RatioBalance172"] = round(float(activity["ActivityContribution_Input401"]),3)
        x["RatioBalance173"] = round(float(activity["ActivityContribution_Input782"]),3)
        x["RatioBalance174"] = round(float(activity["ActivityContribution_Input1073"]),3)
        x["RatioBalance175"] = round(float(activity["ActivityContribution_Input1351"]),3)

        #autres charges:
        x["RatioBalance176"] = round(float(activity["ActivityContribution_Input233"]),3)
        x["RatioBalance177"] = round(float(activity["ActivityContribution_Input611"]),3)
        x["RatioBalance178"] = round(float(activity["ActivityContribution_Input902"]),3)
        x["RatioBalance179"] = round(float(activity["ActivityContribution_Input1194"]),3)
        x["RatioBalance180"] = round(float(activity["ActivityContribution_Input1471"]),3)

        #Depreciation et amortissement:
        x["RatioBalance181"] = round(float(activity["ActivityContribution_Input239"]),3)
        x["RatioBalance182"] = round(float(activity["ActivityContribution_Input619"]),3)
        x["RatioBalance183"] = round(float(activity["ActivityContribution_Input908"]),3)
        x["RatioBalance184"] = round(float(activity["ActivityContribution_Input1200"]),3)
        x["RatioBalance185"] = round(float(activity["ActivityContribution_Input1477"]),3) 

        #dépenses de totaux:
        #i = 186
        #j = 166
        #k = 171
        #l = 176
        #m = 181

        #while i in range(185, 191) and j in range(165, 171) and k in range(170, 176) and l in range(175, 181) and m in range(180, 186):
            #x["RatioBalance" + str(i)] = (round(float(x["RatioBalance" + str(j)]) + float(x["RatioBalance" + str(k)]) + float(x["RatioBalance" + str(l)]) + float(x["RatioBalance" + str(m)])),3)
            #i += 1
            #j += 1
            #k += 1
            #l += 1
            #m += 1

        x["RatioBalance186"] = round(float(x["RatioBalance166"]) + float(x["RatioBalance171"]) + float(x["RatioBalance176"]) + float(x["RatioBalance181"]))
        x["RatioBalance187"] = round(float(x["RatioBalance167"]) + float(x["RatioBalance172"]) + float(x["RatioBalance177"]) + float(x["RatioBalance182"]))
        x["RatioBalance188"] = round(float(x["RatioBalance168"]) + float(x["RatioBalance173"]) + float(x["RatioBalance178"]) + float(x["RatioBalance183"]))
        x["RatioBalance189"] = round(float(x["RatioBalance169"]) + float(x["RatioBalance174"]) + float(x["RatioBalance179"]) + float(x["RatioBalance184"]))
        x["RatioBalance190"] = round(float(x["RatioBalance170"]) + float(x["RatioBalance175"]) + float(x["RatioBalance180"]) + float(x["RatioBalance185"]))
        #Bénéfice net:
        i = 191
        j = 166
        k = 186

        while i in range(190, 196) and j in range(165, 171) and k in range(185, 191):
            x["RatioBalance" + str(i)] = round(float(x["RatioBalance" + str(k)]) - float(x["RatioBalance" + str(j)]),3)
            i += 1
            j += 1
            k += 1   

       #Truck inventory:
        x["RatioBalance196"] = round(float(activity["ActivityContribution_Input265"]),3)
        x["RatioBalance197"] = round(float(activity["ActivityContribution_Input645"]),3)
        x["RatioBalance198"] = round(float(activity["ActivityContribution_Input934"]),3)
        x["RatioBalance199"] = round(float(activity["ActivityContribution_Input1227"]),3)
        x["RatioBalance200"] = round(float(activity["ActivityContribution_Input1503"]),3)   

        #Taux d'absorption hors financement (1) / (2):
        i = 201
        j = 161
        k = 191

        while i in range(200, 206) and j in range(160, 166) and k in range(190, 196):
            if float(x["RatioBalance" + str(k)]) == 0:
                x["RatioBalance" + str(i)] = 0
            else:
                x["RatioBalance" + str(i)] = round(float(x["RatioBalance" + str(j)]) / float(x["RatioBalance" + str(k)]),3)
                i += 1
                j += 1
                k += 1   

        # Financement taux d'absorption inclus (1) / (2) + (3)
        i = 206
        j = 161
        k = 191
        l = 196

        while i in range(205, 211) and j in range(160, 166) and k in range(190, 196) and l in range(195, 201):
            if (float(x["RatioBalance" + str(k)]) + float(float(x["RatioBalance" + str(l)]))) == 0:
                x["RatioBalance" + str(i)] = 0
            else:
                x["RatioBalance" + str(i)] = round( float(x["RatioBalance" + str(j)] / ((float(x["RatioBalance" + str(k)]) + float(x["RatioBalance" + str(l)])))),3)
                i += 1
                j += 1
                k += 1
                l += 1   
                 
                                 

        current_db.ratiobalance.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.ratiobalance.find_one({"GlobalId": "global"})
    return redirect(url_for('ratiobalance.ratiobalance')) 
    return render_template("ratio-balance.html", data=x)


####################################################################################


@ratiobalance_bp.route('/ratiobalance/delete', methods=['GET', 'POST'])
@login_required
def ratiobalance_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.ratiobalance.delete_many({})
    return redirect(url_for('ratiobalance.ratiobalance'))    
    return render_template("ratio-balance.html", data=x)