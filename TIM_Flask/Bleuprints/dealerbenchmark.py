from cProfile import label
import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import math
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

dealerbenchmark_bp = Blueprint('dealerbenchmark', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["dealerbenchmark"]

@dealerbenchmark_bp.route('/dealerbenchmark', methods=['GET'])
@login_required
def dealerbenchmark():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["DealerBenchmark_Header1"] = (int(ref["basic_year"])) 
    x["DealerBenchmark_Header2"] = (int(ref["basic_year"]) + 1 )
    x["DealerBenchmark_Header3"] = (int(ref["basic_year"]) + 2 )
    x["DealerBenchmark_Header4"] = (int(ref["basic_year"]) + 3 )
    x["DealerBenchmark_Header5"] = (int(ref["basic_year"]) + 4 ) 
    i = 1
    lst = []
    while(i < 406):
        lst.append(("DealerBenchmarkInput" + str(i)))
        i += 1
    print(lst)
    for entry in lst:
        x[entry] = 0                  
    print(x) 

    current_db.dealerbenchmark.insert_one(x)
    x = current_db.dealerbenchmark.find_one({"GlobalId": "global"})
    return render_template("dealer-benchmark.html", data=x)
    
####################################################################################


@dealerbenchmark_bp.route('/dealerbenchmark/update', methods=['GET', 'POST'])
@login_required
def dealerbenchmark_update():
    """
    Update a company in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        pl = current_db.pl.find_one({"GlobalId": "global"})
        balanceassets = current_db.balanceassets.find_one({"GlobalId": "global"})
        ratiobalance = current_db.ratiobalance.find_one({"GlobalId": "global"})
        balanceliabilities = current_db.balanceliabilities.find_one({"GlobalId": "global"})
        activitycontribution = current_db.activitycontribution.find_one({"GlobalId": "global"})
        activityanalysis = current_db.activityanalysis.find_one({"GlobalId": "global"})
        turnoverpart = current_db.turnoverpart.find_one({"GlobalId": "global"})
        turnoverservices = current_db.turnoverservices.find_one({"GlobalId": "global"})
        turnovervehicle = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        dealerarea = current_db.dealerarea.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})
        finreq = current_db.financialrequirements.find_one({"GlobalId": "global"})

        x["DealerBenchmark_Header1"] = (int(ref["basic_year"])) 
        x["DealerBenchmark_Header2"] = (int(ref["basic_year"]) + 1 )
        x["DealerBenchmark_Header3"] = (int(ref["basic_year"]) + 2 )
        x["DealerBenchmark_Header4"] = (int(ref["basic_year"]) + 3 )
        x["DealerBenchmark_Header5"] = (int(ref["basic_year"]) + 4 )          

        #1. Générale:
        #Chiffre D'affaires:
        i = 2
        j = 1

        while i in range(1, 7) and j in range(0, 6):
            x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(j)]),0) 
            i += 1
            j += 1

        #marge brute:
        i = 8
        j = 1
        k = 11

        while i in range(7, 13) and j in range(0, 6) and k in range(10, 16):
            if float(pl["PL_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(k)]) / float(pl["PL_Input" + str(j)]),3)
            i += 1
            j += 1  
            k += 1 

        #marge brute:
        i = 14
        j = 1
        k = 36

        while i in range(13, 19) and j in range(0, 6) and k in range(35, 41):
            if float(pl["PL_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(k)]) / float(pl["PL_Input" + str(j)]),3)
            i += 1
            j += 1  
            k += 1 



        # retour aux ventes:
        i = 401
        j = 1
        k = 76

        while i in range(400, 406) and j in range(0, 6) and k in range(75, 81):
            if float(pl["PL_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(k)]) / float(pl["PL_Input" + str(j)]),3)
            i += 1
            j += 1  
            k += 1  


        i = 20
        j = 1
        k = 76

        while i in range(19, 25) and j in range(0, 6) and k in range(75, 81):
            if float(pl["PL_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(k)]) / float(pl["PL_Input" + str(j)]),3)
            i += 1
            j += 1  
            k += 1  




        # le rendement des actifs:
        i = 26
        j = 76
        k = 110
        

        while i in range(25, 31) and j in range(75, 81) and k in range(109, 115):
            if float(balanceassets["BalanceAssetsInput" + str(k)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(j)]) / float(balanceassets["BalanceAssetsInput" + str(k)]),3)
            i += 1
            j += 1  
            k += 1   


        # Rendement des capitaux propres:
        i = 210
        j = 76
        k = 401
        

        while i in range(209, 215) and j in range(75, 81) and k in range(400, 406):
            if float(balanceliabilities["BalanceLiabilitiesInput" + str(k)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(pl["PL_Input" + str(j)]) / float(balanceliabilities["BalanceLiabilitiesInput" + str(k)]),3)
            i += 1
            j += 1  
            k += 1               
            

        # Absorption:
        i = 32
        j = 201


        while i in range(31, 37) and j in range(200, 206):
            if float(ratiobalance["RatioBalance" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(ratiobalance["RatioBalance" + str(j)]),3)
            i += 1
            j += 1  

        # L'équité de la dette:
        i = 401
        j = 401 #c22
        k = 98 #c56


        while i in range(400, 406) and j in range(399, 406) and k in range(97, 103):
            if float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(balanceliabilities["BalanceLiabilitiesInput" + str(k)]) / float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]),3)
            i += 1
            j += 1 
            k += 1

        # Ratio actuel:
        i = 38
        j = 92 #c53
        k = 104 #c45


        while i in range(37, 43) and j in range(91, 97) and k in range(103, 109):
            if float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(balanceassets["BalanceAssetsInput" + str(k)]) / float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]),3)
            i += 1
            j += 1 
            k += 1  
            
        # rapport rapide:
        i = 44
        j = 91 #c53
        k = 103 #c45
        l = 79 #c36


        while i in range(43, 49) and j in range(90, 97) and k in range(102, 109) and l in range(78, 85):
            if float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(balanceassets["BalanceAssetsInput" + str(k)]) - float(balanceassets["BalanceAssetsInput" + str(l)])) / float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]),3)
            i += 1
            j += 1 
            k += 1
            l += 1    
            
        # solvabilité:
        i = 50
        j = 104 #c61
        k = 401 #c22

        while i in range(49, 55) and j in range(103, 109) and k in range(400, 406):
            if float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(balanceliabilities["BalanceLiabilitiesInput" + str(k)]) / float(balanceliabilities["BalanceLiabilitiesInput" + str(j)]) ,3)
            i += 1
            j += 1 
            k += 1  

        # jours de soldes incroyables:
        i = 56
        j = 1 #c7
        k = 86 #c38

        while i in range(55, 61) and j in range(0, 6) and k in range(85, 91):
            if float(pl["PL_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round(float(balanceassets["BalanceAssetsInput" + str(k)]) / float(pl["PL_Input" + str(j)]) * 365)
            i += 1
            j += 1 
            k += 1


        input = 62
        i = 182
        j = 131
        k = 132
        l = 141
        m = 142
        n = 151
        o = 152
        p = 161
        q = 162

        # jours de dettes impayées:
        #while i in range(181, 191) and j in range(130, 140) and k in range(131, 141) and l in range(140,150) and m in range(141, 151) and n in range(150,160) and o in range(151,161) and p in range(160,170) and q in range(161,171):
            #if float(finreq["FinancialRequirement_Input"]+ str(i)) == 0:
                #x["DealerBenchmarkInput" + str(input)] = 0
            #else:
                #x["DealerBenchmarkInput" + str(input)] = round( ((float(finreq["FinancialRequirement_Input" + str(j)]) *  float(finreq["FinancialRequirement_Input" + str(k)])) + (float(finreq["FinancialRequirement_Input" + str(l)]) *  float(finreq["FinancialRequirement_Input" + str(m)])) + (float(finreq["FinancialRequirement_Input" + str(n)]) *  float(finreq["FinancialRequirement_Input" + str(o)])) + (float(finreq["FinancialRequirement_Input" + str(p)]) *  float(finreq["FinancialRequirement_Input" + str(q)]))) / float(finreq["FinancialRequirement_Input" + str(i)]) )

        input += 1
        i += 2
        j += 2 
        k += 2 
        l += 2 
        m += 2 
        n += 2 
        o += 2 
        p += 2 
        q += 2  


        if float(finreq["FinancialRequirement_Input182"]) == 0:
            x["DealerBenchmarkInput62"] = 0
        else:
            x["DealerBenchmarkInput62"] = round( ((float(finreq["FinancialRequirement_Input131"]) *  float(finreq["FinancialRequirement_Input132"])) + (float(finreq["FinancialRequirement_Input141"]) *  float(finreq["FinancialRequirement_Input142"])) + (float(finreq["FinancialRequirement_Input151"]) *  float(finreq["FinancialRequirement_Input152"])) + (float(finreq["FinancialRequirement_Input161"]) *  float(finreq["FinancialRequirement_Input162"]))) / float(finreq["FinancialRequirement_Input182"]) )

    
        if float(finreq["FinancialRequirement_Input184"]) == 0:
            x["DealerBenchmarkInput63"] = 0
        else:
            x["DealerBenchmarkInput63"] = round( ((float(finreq["FinancialRequirement_Input133"]) *  float(finreq["FinancialRequirement_Input134"])) + (float(finreq["FinancialRequirement_Input143"]) *  float(finreq["FinancialRequirement_Input144"])) + (float(finreq["FinancialRequirement_Input153"]) *  float(finreq["FinancialRequirement_Input154"])) + (float(finreq["FinancialRequirement_Input163"]) *  float(finreq["FinancialRequirement_Input164"]))) / float(finreq["FinancialRequirement_Input184"]) )

        if float(finreq["FinancialRequirement_Input186"]) == 0:
            x["DealerBenchmarkInput64"] = 0
        else:
            x["DealerBenchmarkInput64"] = round( ((float(finreq["FinancialRequirement_Input135"]) *  float(finreq["FinancialRequirement_Input136"])) + (float(finreq["FinancialRequirement_Input145"]) *  float(finreq["FinancialRequirement_Input146"])) + (float(finreq["FinancialRequirement_Input155"]) *  float(finreq["FinancialRequirement_Input156"])) + (float(finreq["FinancialRequirement_Input165"]) *  float(finreq["FinancialRequirement_Input166"]))) / float(finreq["FinancialRequirement_Input186"]) )        

        if float(finreq["FinancialRequirement_Input188"]) == 0:
            x["DealerBenchmarkInput65"] = 0
        else:
            x["DealerBenchmarkInput65"] = round( ((float(finreq["FinancialRequirement_Input137"]) *  float(finreq["FinancialRequirement_Input138"])) + (float(finreq["FinancialRequirement_Input147"]) *  float(finreq["FinancialRequirement_Input148"])) + (float(finreq["FinancialRequirement_Input157"]) *  float(finreq["FinancialRequirement_Input158"])) + (float(finreq["FinancialRequirement_Input167"]) *  float(finreq["FinancialRequirement_Input168"]))) / float(finreq["FinancialRequirement_Input188"]) )        

        if float(finreq["FinancialRequirement_Input190"]) == 0:
            x["DealerBenchmarkInput66"] = 0
        else:
            x["DealerBenchmarkInput66"] = round( ((float(finreq["FinancialRequirement_Input139"]) *  float(finreq["FinancialRequirement_Input140"])) + (float(finreq["FinancialRequirement_Input149"]) *  float(finreq["FinancialRequirement_Input150"])) + (float(finreq["FinancialRequirement_Input159"]) *  float(finreq["FinancialRequirement_Input160"])) + (float(finreq["FinancialRequirement_Input169"]) *  float(finreq["FinancialRequirement_Input170"]))) / float(finreq["FinancialRequirement_Input190"]) )        

        
                                                        
        # nouveaux camions:

        if float(activitycontribution["ActivityContribution_Input41"]) == 0:
            x["DealerBenchmarkInput74"] = 0
        else:
            x["DealerBenchmarkInput74"] = round(float(activitycontribution["ActivityContribution_Input37"]) / (float(activitycontribution["ActivityContribution_Input41"])),3)

        if float(activitycontribution["ActivityContribution_Input329"]) == 0:
            x["DealerBenchmarkInput75"] = 0
        else:
            x["DealerBenchmarkInput75"] = round(float(activitycontribution["ActivityContribution_Input325"]) / (float(activitycontribution["ActivityContribution_Input329"])),3)
    
        if float(activitycontribution["ActivityContribution_Input710"]) == 0:
            x["DealerBenchmarkInput76"] = 0
        else:
            x["DealerBenchmarkInput76"] = round(float(activitycontribution["ActivityContribution_Input706"]) / (float(activitycontribution["ActivityContribution_Input710"])),3)

        if float(activitycontribution["ActivityContribution_Input1001"]) == 0:
            x["DealerBenchmarkInput77"] = 0
        else:
            x["DealerBenchmarkInput77"] = round(float(activitycontribution["ActivityContribution_Input997"]) / (float(activitycontribution["ActivityContribution_Input1001"])),3)

        if float(activitycontribution["ActivityContribution_Input1279"]) == 0:
            x["DealerBenchmarkInput78"] = 0
        else:
            x["DealerBenchmarkInput78"] = round(float(activitycontribution["ActivityContribution_Input1275"]) / (float(activitycontribution["ActivityContribution_Input1279"])),3)  

        # pièces:

        if float(activitycontribution["ActivityContribution_Input41"]) == 0:
            x["DealerBenchmarkInput80"] = 0
        else:
            x["DealerBenchmarkInput80"] = round(float(activitycontribution["ActivityContribution_Input38"]) / (float(activitycontribution["ActivityContribution_Input41"])),3)

        if float(activitycontribution["ActivityContribution_Input329"]) == 0:
            x["DealerBenchmarkInput81"] = 0
        else:
            x["DealerBenchmarkInput81"] = round(float(activitycontribution["ActivityContribution_Input326"]) / (float(activitycontribution["ActivityContribution_Input329"])),3)
    
        if float(activitycontribution["ActivityContribution_Input710"]) == 0:
            x["DealerBenchmarkInput82"] = 0
        else:
            x["DealerBenchmarkInput82"] = round(float(activitycontribution["ActivityContribution_Input707"]) / (float(activitycontribution["ActivityContribution_Input710"])),3)

        if float(activitycontribution["ActivityContribution_Input1001"]) == 0:
            x["DealerBenchmarkInput83"] = 0
        else:
            x["DealerBenchmarkInput83"] = round(float(activitycontribution["ActivityContribution_Input998"]) / (float(activitycontribution["ActivityContribution_Input1001"])),3)

        if float(activitycontribution["ActivityContribution_Input1279"]) == 0:
            x["DealerBenchmarkInput84"] = 0
        else:
            x["DealerBenchmarkInput84"] = round(float(activitycontribution["ActivityContribution_Input1276"]) / (float(activitycontribution["ActivityContribution_Input1279"])),3)  

        # service & carrosserie:

        if float(activitycontribution["ActivityContribution_Input41"]) == 0:
            x["DealerBenchmarkInput86"] = 0
        else:
            x["DealerBenchmarkInput86"] = round(float(activitycontribution["ActivityContribution_Input39"]) / (float(activitycontribution["ActivityContribution_Input41"])),3)

        if float(activitycontribution["ActivityContribution_Input329"]) == 0:
            x["DealerBenchmarkInput87"] = 0
        else:
            x["DealerBenchmarkInput87"] = round(float(activitycontribution["ActivityContribution_Input327"]) / (float(activitycontribution["ActivityContribution_Input329"])),3)
    
        if float(activitycontribution["ActivityContribution_Input710"]) == 0:
            x["DealerBenchmarkInput88"] = 0
        else:
            x["DealerBenchmarkInput88"] = round(float(activitycontribution["ActivityContribution_Input708"]) / (float(activitycontribution["ActivityContribution_Input710"])),3)

        if float(activitycontribution["ActivityContribution_Input1001"]) == 0:
            x["DealerBenchmarkInput89"] = 0
        else:
            x["DealerBenchmarkInput89"] = round(float(activitycontribution["ActivityContribution_Input999"]) / (float(activitycontribution["ActivityContribution_Input1001"])),3)

        if float(activitycontribution["ActivityContribution_Input1279"]) == 0:
            x["DealerBenchmarkInput90"] = 0
        else:
            x["DealerBenchmarkInput90"] = round(float(activitycontribution["ActivityContribution_Input1277"]) / (float(activitycontribution["ActivityContribution_Input1279"])),3)              

        # Livraison: #Dealer area c35

        x["DealerBenchmarkInput92"] = round(float(dealerarea["DealeArea_Input42"]),3)
        x["DealerBenchmarkInput93"] = round(float(dealerarea["DealeArea_Input43"]),3)
        x["DealerBenchmarkInput94"] = round(float(dealerarea["DealeArea_Input44"]),3)
        x["DealerBenchmarkInput95"] = round(float(dealerarea["DealeArea_Input45"]),3)
        x["DealerBenchmarkInput96"] = round(float(dealerarea["DealeArea_Input46"]),3)                                

        # Ventes:
        i = 98
        j = 31

        while i in range(97, 103) and j in range(30, 36):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1

        #chiffre d'affaires moyen #camions: #Dealer area c35
        if float(x["DealerBenchmarkInput92"]) == 0:
            x["DealerBenchmarkInput104"] = 0
        else: 
            x["DealerBenchmarkInput104"] = round(float(turnovervehicle["TurnoverVehicle_Input_A"]) / float(x["DealerBenchmarkInput92"]),3)

        if float(x["DealerBenchmarkInput93"]) == 0:
            x["DealerBenchmarkInput105"] = 0
        else: 
            x["DealerBenchmarkInput105"] = round(float(turnovervehicle["TurnoverVehicle_Input_B"]) / float(x["DealerBenchmarkInput93"]),3)     

        if float(x["DealerBenchmarkInput94"]) == 0:
            x["DealerBenchmarkInput106"] = 0
        else: 
            x["DealerBenchmarkInput106"] = round(float(turnovervehicle["TurnoverVehicle_Input_C"]) / float(x["DealerBenchmarkInput94"]),3)   

        if float(x["DealerBenchmarkInput95"]) == 0:
            x["DealerBenchmarkInput107"] = 0
        else: 
            x["DealerBenchmarkInput107"] = round(float(turnovervehicle["TurnoverVehicle_Input_E"]) / float(x["DealerBenchmarkInput95"]),3)      

        if float(x["DealerBenchmarkInput96"]) == 0:
            x["DealerBenchmarkInput108"] = 0
        else: 
            x["DealerBenchmarkInput108"] = round(float(turnovervehicle["TurnoverVehicle_Input_F"]) / float(x["DealerBenchmarkInput96"]),3)                                     


        #Marge Brute:
        i = 110
        j = 86

        while i in range(109, 115) and j in range(85, 93):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]) * 100,3)
            i += 1
            j += 1

        #Bénéfice brut moyen #camions: #Dealer area c35
        #2. Département camions neufs
        '''i = 115
        j = 92
        k = 81

        while i in range(114, 120) and j in range(91, 97) and k in range(80, 86):
            if float(x["DealerBenchmarkInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else: 
                x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(k)]) / float(x["DealerBenchmarkInput" + str(j)]),3)                                     
        i += 1
        j += 1
        k += 1'''

        if float(x["DealerBenchmarkInput92"]) == 0:
            x["DealerBenchmarkInput115"] = 0
        else: 
            x["DealerBenchmarkInput115"] = round(float(activityanalysis["ActivityAnalysis_Input81"]) / float(x["DealerBenchmarkInput92"]),3)

        if float(x["DealerBenchmarkInput93"]) == 0:
            x["DealerBenchmarkInput116"] = 0
        else: 
            x["DealerBenchmarkInput116"] = round(float(activityanalysis["ActivityAnalysis_Input82"]) / float(x["DealerBenchmarkInput93"]),3)     

        if float(x["DealerBenchmarkInput94"]) == 0:
            x["DealerBenchmarkInput117"] = 0
        else: 
            x["DealerBenchmarkInput117"] = round(float(activityanalysis["ActivityAnalysis_Input83"]) / float(x["DealerBenchmarkInput94"]),3)   

        if float(x["DealerBenchmarkInput95"]) == 0:
            x["DealerBenchmarkInput118"] = 0
        else: 
            x["DealerBenchmarkInput118"] = round(float(activityanalysis["ActivityAnalysis_Input84"]) / float(x["DealerBenchmarkInput95"]),3)      

        if float(x["DealerBenchmarkInput96"]) == 0:
            x["DealerBenchmarkInput119"] = 0
        else: 
            x["DealerBenchmarkInput119"] = round(float(activityanalysis["ActivityAnalysis_Input85"]) / float(x["DealerBenchmarkInput96"]),3) 



        #Marge Brute:
        i = 120
        j = 105

        while i in range(119, 125) and j in range(104, 110):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1  

        # charges d'exploitation %:
        i = 120
        j = 31
        k = 100
        l = 105
        m = 205
        n = 210

        while i in range(119, 125) and j in range(30, 36) and k in range(99, 105) and l in range(104, 110) and m in range(204, 210) and n in range(209, 215):
            if float(activityanalysis["ActivityAnalysis_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(activityanalysis["ActivityAnalysis_Input" + str(k)])+float(activityanalysis["ActivityAnalysis_Input" + str(l)])+float(activityanalysis["ActivityAnalysis_Input" + str(m)])+float(activityanalysis["ActivityAnalysis_Input" + str(n)]))/float(activityanalysis["ActivityAnalysis_Input" + str(j)]) ,3)
                            
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1

        #marge d'exploitation:
        i = 125
        j = 220

        while i in range(124, 130) and j in range(119, 225):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1      

        #rotation des stocks:

        if float(balanceassets["BalanceAssetsInput68"]) == 0:
            x["DealerBenchmarkInput130"] = 0
        else:
            x["DealerBenchmarkInput130"] = round((float(activitycontribution["ActivityContribution_Input37"]) - float(activitycontribution["ActivityContribution_Input97"])) / (float(balanceassets["BalanceAssetsInput68"])),3) 

        if float(balanceassets["BalanceAssetsInput69"]) == 0:
            x["DealerBenchmarkInput131"] = 0
        else:
            x["DealerBenchmarkInput131"] = round((float(activitycontribution["ActivityContribution_Input325"]) - float(activitycontribution["ActivityContribution_Input385"])) / (float(balanceassets["BalanceAssetsInput69"])),3) 

        if float(balanceassets["BalanceAssetsInput70"]) == 0:
            x["DealerBenchmarkInput132"] = 0
        else:
            x["DealerBenchmarkInput132"] = round((float(activitycontribution["ActivityContribution_Input706"]) - float(activitycontribution["ActivityContribution_Input766"])) / (float(balanceassets["BalanceAssetsInput70"])),3) 

        if float(balanceassets["BalanceAssetsInput71"]) == 0:
            x["DealerBenchmarkInput133"] = 0
        else:
            x["DealerBenchmarkInput133"] = round((float(activitycontribution["ActivityContribution_Input997"]) - float(activitycontribution["ActivityContribution_Input1057"])) / (float(balanceassets["BalanceAssetsInput71"])),3)    
            
        if float(balanceassets["BalanceAssetsInput72"]) == 0:
            x["DealerBenchmarkInput134"] = 0
        else:
            x["DealerBenchmarkInput134"] = round((float(activitycontribution["ActivityContribution_Input1275"]) - float(activitycontribution["ActivityContribution_Input1335"])) / (float(balanceassets["BalanceAssetsInput72"])),3)   

        #inventaire DOH:
        i = 135
        j = 130
        k = 365

        while i in range(134, 140) and j in range(129, 135):
            if float(x["DealerBenchmarkInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0 
            else:
                x["DealerBenchmarkInput" + str(i)] = round( k / float(x["DealerBenchmarkInput" + str(j)]),3)  
            i += 1
            j += 1    

        #3. Département des pièces
        #ventes des pièces:
        i = 140
        j = 352

        while i in range(139, 145) and j in range(351, 357):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1

        #Marge Brute:
        '''i = 145
        j = 517

        while i in range(144, 150) and j in range(516, 522):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
        i += 1
        j += 1'''

        x["DealerBenchmarkInput145"] = round(float(activityanalysis["ActivityAnalysis_Input517"]),3)
        x["DealerBenchmarkInput146"] = round(float(activityanalysis["ActivityAnalysis_Input518"]),3)
        x["DealerBenchmarkInput147"] = round(float(activityanalysis["ActivityAnalysis_Input519"]),3) 
        x["DealerBenchmarkInput148"] = round(float(activityanalysis["ActivityAnalysis_Input520"]),3)
        x["DealerBenchmarkInput149"] = round(float(activityanalysis["ActivityAnalysis_Input521"]),3)      

        # charges d'exploitation %:
        '''i = 150
        j = 352
        k = 532
        l = 547
        m = 848
        n = 863

        while i in range(149, 155) and j in range(351, 357) and k in range(531, 537) and l in range(546, 552) and m in range(847, 853) and n in range(862, 868):
            if float(activityanalysis["ActivityAnalysis_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(activityanalysis["ActivityAnalysis_Input" + str(k)])+float(activityanalysis["ActivityAnalysis_Input" + str(l)])+float(activityanalysis["ActivityAnalysis_Input" + str(m)])+float(activityanalysis["ActivityAnalysis_Input" + str(n)]))/float(activityanalysis["ActivityAnalysis_Input" + str(j)]) ,3)
                            
        i += 1
        j += 1
        k += 1
        l += 1
        m += 1
        n += 1'''

        if float(activityanalysis["ActivityAnalysis_Input352"]) == 0:
            x["DealerBenchmarkInput150"] = 0
        else:
            x["DealerBenchmarkInput150"] = round((float(activityanalysis["ActivityAnalysis_Input532"])+float(activityanalysis["ActivityAnalysis_Input547"])+float(activityanalysis["ActivityAnalysis_Input848"])+float(activityanalysis["ActivityAnalysis_Input863"]))/float(activityanalysis["ActivityAnalysis_Input352"]) ,3)

        if float(activityanalysis["ActivityAnalysis_Input353"]) == 0:
            x["DealerBenchmarkInput151"] = 0
        else:
            x["DealerBenchmarkInput151"] = round((float(activityanalysis["ActivityAnalysis_Input533"])+float(activityanalysis["ActivityAnalysis_Input548"])+float(activityanalysis["ActivityAnalysis_Input849"])+float(activityanalysis["ActivityAnalysis_Input864"]))/float(activityanalysis["ActivityAnalysis_Input353"]) ,3)

        if float(activityanalysis["ActivityAnalysis_Input354"]) == 0:
            x["DealerBenchmarkInput152"] = 0
        else:
            x["DealerBenchmarkInput152"] = round((float(activityanalysis["ActivityAnalysis_Input534"])+float(activityanalysis["ActivityAnalysis_Input549"])+float(activityanalysis["ActivityAnalysis_Input850"])+float(activityanalysis["ActivityAnalysis_Input865"]))/float(activityanalysis["ActivityAnalysis_Input354"]) ,3)

        if float(activityanalysis["ActivityAnalysis_Input355"]) == 0:
            x["DealerBenchmarkInput153"] = 0
        else:
            x["DealerBenchmarkInput153"] = round((float(activityanalysis["ActivityAnalysis_Input535"])+float(activityanalysis["ActivityAnalysis_Input550"])+float(activityanalysis["ActivityAnalysis_Input851"])+float(activityanalysis["ActivityAnalysis_Input866"]))/float(activityanalysis["ActivityAnalysis_Input355"]) ,3)     

        if float(activityanalysis["ActivityAnalysis_Input356"]) == 0:
            x["DealerBenchmarkInput154"] = 0
        else:
            x["DealerBenchmarkInput154"] = round((float(activityanalysis["ActivityAnalysis_Input536"])+float(activityanalysis["ActivityAnalysis_Input551"])+float(activityanalysis["ActivityAnalysis_Input852"])+float(activityanalysis["ActivityAnalysis_Input867"]))/float(activityanalysis["ActivityAnalysis_Input356"]) ,3)                   

        #marge d'exploitation:
        ''' i = 155
        j = 1013

        while i in range(154, 160) and j in range(1012, 1018):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
        i += 1
        j += 1  '''

        x["DealerBenchmarkInput155"] = round(float(activityanalysis["ActivityAnalysis_Input1013"]),3)
        x["DealerBenchmarkInput156"] = round(float(activityanalysis["ActivityAnalysis_Input1014"]),3)
        x["DealerBenchmarkInput157"] = round(float(activityanalysis["ActivityAnalysis_Input1015"]),3)
        x["DealerBenchmarkInput158"] = round(float(activityanalysis["ActivityAnalysis_Input1016"]),3)
        x["DealerBenchmarkInput159"] = round(float(activityanalysis["ActivityAnalysis_Input1017"]),3)                        


        #rotation des stocks:

        '''i = 160
        j = 352
        k = 502
        l = 74

        while i in range(159, 165) and j in range(351, 357) and k in range(501, 507) and l in range(73, 79):
            if float(balanceassets["BalanceAssetsInput" + str(l)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(activityanalysis["ActivityAnalysis_Input" + str(j)]) - float(activityanalysis["ActivityAnalysis_Input" + str(k)])) / (float(balanceassets["BalanceAssetsInput" + str(l)])),3)
                            
        i += 1
        j += 1
        k += 1
        l += 1'''

        if float(balanceassets["BalanceAssetsInput75"]) == 0:
            x["DealerBenchmarkInput160"] = 0
        else:
            x["DealerBenchmarkInput160"] = round((float(activityanalysis["ActivityAnalysis_Input352"]) - float(activityanalysis["ActivityAnalysis_Input502"])) / (float(balanceassets["BalanceAssetsInput74"])),3)

        if float(balanceassets["BalanceAssetsInput75"]) == 0:
            x["DealerBenchmarkInput161"] = 0
        else:
            x["DealerBenchmarkInput161"] = round((float(activityanalysis["ActivityAnalysis_Input353"]) - float(activityanalysis["ActivityAnalysis_Input503"])) / (float(balanceassets["BalanceAssetsInput75"])),3)

        if float(balanceassets["BalanceAssetsInput76"]) == 0:
            x["DealerBenchmarkInput162"] = 0
        else:
            x["DealerBenchmarkInput162"] = round((float(activityanalysis["ActivityAnalysis_Input354"]) - float(activityanalysis["ActivityAnalysis_Input504"])) / (float(balanceassets["BalanceAssetsInput76"])),3) 

        if float(balanceassets["BalanceAssetsInput77"]) == 0:
            x["DealerBenchmarkInput163"] = 0
        else:
            x["DealerBenchmarkInput163"] = round((float(activityanalysis["ActivityAnalysis_Input355"]) - float(activityanalysis["ActivityAnalysis_Input520"])) / (float(balanceassets["BalanceAssetsInput77"])),3) 

        if float(balanceassets["BalanceAssetsInput78"]) == 0:
            x["DealerBenchmarkInput164"] = 0
        else:
            x["DealerBenchmarkInput164"] = round((float(activityanalysis["ActivityAnalysis_Input356"]) - float(activityanalysis["ActivityAnalysis_Input506"])) / (float(balanceassets["BalanceAssetsInput78"])),3)                                

        #inventaire DOH:
            #i = 165
            #j = 160
            #k = 365

            #while i in range(164, 170) and j in range(159, 165):
                #if float(x["DealerBenchmarkInput" + str(j)]) == 0:
                    #x["DealerBenchmarkInput" + str(i)] = 0 
                #else:
                    #x["DealerBenchmarkInput" + str(i)] = round( k / float(x["DealerBenchmarkInput" + str(j)]),3)  
            #i += 1
            #j += 1 

            if float(x["DealerBenchmarkInput160"]) == 0:
                x["DealerBenchmarkInput165"] = 0 
            else:
                x["DealerBenchmarkInput165"] = round( 365 / float(x["DealerBenchmarkInput160"]))  

            if float(x["DealerBenchmarkInput161"]) == 0:
                x["DealerBenchmarkInput166"] = 0 
            else:
                x["DealerBenchmarkInput166"] = round( 365 / float(x["DealerBenchmarkInput161"])) 

            if float(x["DealerBenchmarkInput162"]) == 0:
                x["DealerBenchmarkInput167"] = 0 
            else:
                x["DealerBenchmarkInput167"] = round( 365 / float(x["DealerBenchmarkInput162"]))   

            if float(x["DealerBenchmarkInput163"]) == 0:
                x["DealerBenchmarkInput168"] = 0 
            else:
                x["DealerBenchmarkInput168"] = round( 365 / float(x["DealerBenchmarkInput163"])) 

            if float(x["DealerBenchmarkInput164"]) == 0:
                x["DealerBenchmarkInput169"] = 0 
            else:
                x["DealerBenchmarkInput169"] = round( 365 / float(x["DealerBenchmarkInput164"]))   

        # commercial/employé :
        '''i = 170
        j = 129
        k = 140

        while i in range(169, 175) and j in range(128, 134) and k in range(139, 145):
            if float(activityanalysis["ActivityAnalysis_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(x["DealerBenchmarkInput" + str(k)])/float(turnoverpart["TurnoverParts_Input" + str(j)])) ,3)
                            
        i += 1
        j += 1
        k += 1 '''

        if float(activityanalysis["ActivityAnalysis_Input129"]) == 0:
            x["DealerBenchmarkInput170"] = 0
        else:
            x["DealerBenchmarkInput170"] = round((float(x["DealerBenchmarkInput140"])/float(turnoverpart["TurnoverParts_Input129"])) ,3)

        if float(activityanalysis["ActivityAnalysis_Input130"]) == 0:
            x["DealerBenchmarkInput171"] = 0
        else:
            x["DealerBenchmarkInput171"] = round((float(x["DealerBenchmarkInput141"])/float(turnoverpart["TurnoverParts_Input130"])) ,3)

        if float(activityanalysis["ActivityAnalysis_Input131"]) == 0:
            x["DealerBenchmarkInput172"] = 0
        else:
            x["DealerBenchmarkInput172"] = round((float(x["DealerBenchmarkInput142"])/float(turnoverpart["TurnoverParts_Input131"])) ,3)

        if float(activityanalysis["ActivityAnalysis_Input132"]) == 0:
            x["DealerBenchmarkInput173"] = 0
        else:
            x["DealerBenchmarkInput173"] = round((float(x["DealerBenchmarkInput143"])/float(turnoverpart["TurnoverParts_Input132"])) ,3)

        if float(activityanalysis["ActivityAnalysis_Input133"]) == 0:
            x["DealerBenchmarkInput174"] = 0
        else:
            x["DealerBenchmarkInput174"] = round((float(x["DealerBenchmarkInput144"])/float(turnoverpart["TurnoverParts_Input133"])) ,3)                                                


        #ventes des pièces:
        '''i = 175
        j = 357

        while i in range(174, 180) and j in range(356, 362):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1'''

        x["DealerBenchmarkInput175"] = round(float(activityanalysis["ActivityAnalysis_Input357"]),3)
        x["DealerBenchmarkInput176"] = round(float(activityanalysis["ActivityAnalysis_Input358"]),3)
        x["DealerBenchmarkInput177"] = round(float(activityanalysis["ActivityAnalysis_Input359"]),3)
        x["DealerBenchmarkInput178"] = round(float(activityanalysis["ActivityAnalysis_Input360"]),3)
        x["DealerBenchmarkInput179"] = round(float(activityanalysis["ActivityAnalysis_Input361"]),3)                                                    

        #Marge Brute:
        '''i = 180
        j = 522

        while i in range(179, 185) and j in range(521, 527):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
            i += 1
            j += 1'''

        x["DealerBenchmarkInput180"] = round(float(activityanalysis["ActivityAnalysis_Input522"]),3)
        x["DealerBenchmarkInput181"] = round(float(activityanalysis["ActivityAnalysis_Input523"]),3)
        x["DealerBenchmarkInput182"] = round(float(activityanalysis["ActivityAnalysis_Input524"]),3)
        x["DealerBenchmarkInput183"] = round(float(activityanalysis["ActivityAnalysis_Input525"]),3)
        x["DealerBenchmarkInput184"] = round(float(activityanalysis["ActivityAnalysis_Input526"]),3)

        # charges d'exploitation %:
        '''i = 185
        j = 357
        k = 541
        l = 552
        m = 853
        n = 868

        while i in range(184, 190) and j in range(356, 362) and k in range(540, 546) and l in range(551, 557) and m in range(852, 858) and n in range(867, 873):
            if float(activityanalysis["ActivityAnalysis_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(activityanalysis["ActivityAnalysis_Input" + str(k)])+float(activityanalysis["ActivityAnalysis_Input" + str(l)])+float(activityanalysis["ActivityAnalysis_Input" + str(m)])+float(activityanalysis["ActivityAnalysis_Input" + str(n)]))/float(activityanalysis["ActivityAnalysis_Input" + str(j)]) ,3)
                            
        i += 1
        j += 1
        k += 1
        l += 1
        m += 1
        n += 1'''


        if float(activityanalysis["ActivityAnalysis_Input357"]) == 0:
            x["DealerBenchmarkInput185"] = 0
        else:
            x["DealerBenchmarkInput185"] = round((float(activityanalysis["ActivityAnalysis_Input537"])+float(activityanalysis["ActivityAnalysis_Input552"])+float(activityanalysis["ActivityAnalysis_Input853"])+float(activityanalysis["ActivityAnalysis_Input868"]))/float(activityanalysis["ActivityAnalysis_Input357"])*100,3)

        if float(activityanalysis["ActivityAnalysis_Input358"]) == 0:
            x["DealerBenchmarkInput186"] = 0
        else:
            x["DealerBenchmarkInput186"] = round((float(activityanalysis["ActivityAnalysis_Input538"])+float(activityanalysis["ActivityAnalysis_Input553"])+float(activityanalysis["ActivityAnalysis_Input854"])+float(activityanalysis["ActivityAnalysis_Input869"]))/float(activityanalysis["ActivityAnalysis_Input358"])*100,3)

        if float(activityanalysis["ActivityAnalysis_Input359"]) == 0:
            x["DealerBenchmarkInput187"] = 0
        else:
            x["DealerBenchmarkInput187"] = round((float(activityanalysis["ActivityAnalysis_Input539"])+float(activityanalysis["ActivityAnalysis_Input554"])+float(activityanalysis["ActivityAnalysis_Input855"])+float(activityanalysis["ActivityAnalysis_Input870"]))/float(activityanalysis["ActivityAnalysis_Input359"])*100,3)

        if float(activityanalysis["ActivityAnalysis_Input360"]) == 0:
            x["DealerBenchmarkInput188"] = 0
        else:
            x["DealerBenchmarkInput188"] = round((float(activityanalysis["ActivityAnalysis_Input540"])+float(activityanalysis["ActivityAnalysis_Input555"])+float(activityanalysis["ActivityAnalysis_Input856"])+float(activityanalysis["ActivityAnalysis_Input871"]))/float(activityanalysis["ActivityAnalysis_Input360"])*100,3)

        if float(activityanalysis["ActivityAnalysis_Input361"]) == 0:
            x["DealerBenchmarkInput189"] = 0
        else:
            x["DealerBenchmarkInput189"] = round((float(activityanalysis["ActivityAnalysis_Input541"])+float(activityanalysis["ActivityAnalysis_Input556"])+float(activityanalysis["ActivityAnalysis_Input857"])+float(activityanalysis["ActivityAnalysis_Input872"]))/float(activityanalysis["ActivityAnalysis_Input361"])*100,3)



        #marge d'exploitation:
        '''i = 190
        j = 1017

        while i in range(189, 195) and j in range(1016, 1023):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
        i += 1
        j += 1  '''

        x["DealerBenchmarkInput190"] = round(float(activityanalysis["ActivityAnalysis_Input1018"]),3)
        x["DealerBenchmarkInput191"] = round(float(activityanalysis["ActivityAnalysis_Input1019"]),3)
        x["DealerBenchmarkInput192"] = round(float(activityanalysis["ActivityAnalysis_Input1020"]),3)
        x["DealerBenchmarkInput193"] = round(float(activityanalysis["ActivityAnalysis_Input1021"]),3)
        x["DealerBenchmarkInput194"] = round(float(activityanalysis["ActivityAnalysis_Input1022"]),3)
                
        # commercial/employé :
        '''i = 195
        j = 145
        k = 175

        while i in range(194, 200) and j in range(144, 150) and k in range(174, 180):
            if float(activityanalysis["ActivityAnalysis_Input" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(x["DealerBenchmarkInput" + str(k)])/float(turnoverservices["TurnoverServices_Input" + str(j)])) ,3)
                            
        i += 1
        j += 1
        k += 1 '''

        if float(activityanalysis["ActivityAnalysis_Input145"]) == 0:
            x["DealerBenchmarkInput195"] = 0
        else:
            x["DealerBenchmarkInput195"] = round((float(x["DealerBenchmarkInput175"])/float(turnoverservices["TurnoverServices_Input145"])) ,3)        

        if float(activityanalysis["ActivityAnalysis_Input146"]) == 0:
            x["DealerBenchmarkInput196"] = 0
        else:
            x["DealerBenchmarkInput196"] = round((float(x["DealerBenchmarkInput176"])/float(turnoverservices["TurnoverServices_Input146"])) ,3)    

        if float(activityanalysis["ActivityAnalysis_Input147"]) == 0:
            x["DealerBenchmarkInput197"] = 0
        else:
            x["DealerBenchmarkInput197"] = round((float(x["DealerBenchmarkInput177"])/float(turnoverservices["TurnoverServices_Input147"])) ,3)    

        if float(activityanalysis["ActivityAnalysis_Input148"]) == 0:
            x["DealerBenchmarkInput198"] = 0
        else:
            x["DealerBenchmarkInput198"] = round((float(x["DealerBenchmarkInput178"])/float(turnoverservices["TurnoverServices_Input148"])) ,3)    

        if float(activityanalysis["ActivityAnalysis_Input149"]) == 0:
            x["DealerBenchmarkInput199"] = 0
        else:
            x["DealerBenchmarkInput199"] = round((float(x["DealerBenchmarkInput179"])/float(turnoverservices["TurnoverServices_Input149"])) ,3)    

        # 4. Administration générale:
        # dépenses non affectées:
        '''i = 200
        j = 557

        while i in range(199, 205) and j in range(556, 562):
            x["DealerBenchmarkInput" + str(i)] = round(float(activityanalysis["ActivityAnalysis_Input" + str(j)]),3)
        i += 1
        j += 1'''

        x["DealerBenchmarkInput200"] = round(float(activityanalysis["ActivityAnalysis_Input557"]) + float(activityanalysis["ActivityAnalysis_Input858"]) + float(activityanalysis["ActivityAnalysis_Input873"]),3)
        x["DealerBenchmarkInput201"] = round(float(activityanalysis["ActivityAnalysis_Input558"]) + float(activityanalysis["ActivityAnalysis_Input859"]) + float(activityanalysis["ActivityAnalysis_Input874"]),3)
        x["DealerBenchmarkInput202"] = round(float(activityanalysis["ActivityAnalysis_Input559"]) + float(activityanalysis["ActivityAnalysis_Input860"]) + float(activityanalysis["ActivityAnalysis_Input875"]),3)
        x["DealerBenchmarkInput203"] = round(float(activityanalysis["ActivityAnalysis_Input560"]) + float(activityanalysis["ActivityAnalysis_Input861"]) + float(activityanalysis["ActivityAnalysis_Input876"]),3)
        x["DealerBenchmarkInput204"] = round(float(activityanalysis["ActivityAnalysis_Input561"]) + float(activityanalysis["ActivityAnalysis_Input862"]) + float(activityanalysis["ActivityAnalysis_Input877"]),3)

        # % Ventes:
        '''i = 205
        j = 2
        k = 200 

        while i in range(204, 210) and j in range(1, 7) and k in range(199, 205):
            if float(x["DealerBenchmarkInput" + str(j)]) == 0:
                x["DealerBenchmarkInput" + str(i)] = 0
            else:
                x["DealerBenchmarkInput" + str(i)] = round((float(x["DealerBenchmarkInput" + str(k)])/float(x["DealerBenchmarkInput" + str(j)])) ,3)  
        i += 1
        j += 1
        k += 1  '''    
        

        if float(x["DealerBenchmarkInput2"]) == 0:
            x["DealerBenchmarkInput205"] = 0
        else:
            x["DealerBenchmarkInput205"] = round((float(x["DealerBenchmarkInput200"])/float(x["DealerBenchmarkInput2"])) ,3) 

        if float(x["DealerBenchmarkInput3"]) == 0:
            x["DealerBenchmarkInput206"] = 0
        else:
            x["DealerBenchmarkInput206"] = round((float(x["DealerBenchmarkInput201"])/float(x["DealerBenchmarkInput3"])) ,3)   

        if float(x["DealerBenchmarkInput3"]) == 0:
            x["DealerBenchmarkInput207"] = 0
        else:
            x["DealerBenchmarkInput207"] = round((float(x["DealerBenchmarkInput202"])/float(x["DealerBenchmarkInput4"])) ,3)  

        if float(x["DealerBenchmarkInput3"]) == 0:
            x["DealerBenchmarkInput208"] = 0
        else:
            x["DealerBenchmarkInput208"] = round((float(x["DealerBenchmarkInput203"])/float(x["DealerBenchmarkInput5"])) ,3)  

        if float(x["DealerBenchmarkInput3"]) == 0:
            x["DealerBenchmarkInput209"] = 0
        else:
            x["DealerBenchmarkInput209"] = round((float(x["DealerBenchmarkInput204"])/float(x["DealerBenchmarkInput6"])) ,3)                                                                                                                                  
        


    current_db.dealerbenchmark.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.dealerbenchmark.find_one({"GlobalId": "global"})
    print(x)
    return redirect(url_for('dealerbenchmark.dealerbenchmark'))     
    return render_template("dealer-benchmark.html", data=x)


####################################################################################

@dealerbenchmark_bp.route('/dealerbenchmark/delete',  methods=['POST'])
@login_required
def dealerbenchmark_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db() 
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.dealerbenchmark.delete_many({})
    return redirect(url_for('dealerbenchmark.dealerbenchmark'))        
    return render_template("dealer-benchmark.html", data=x)