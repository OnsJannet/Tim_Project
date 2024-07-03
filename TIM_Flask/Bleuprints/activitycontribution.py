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

activitycontribution_bp = Blueprint('activitycontribution', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["activitycontribution"]

@activitycontribution_bp.route('/activitycontribution', methods=['GET', 'POST'])
@login_required
def activitycontribution():
    """
    Create new collection in the database
    """    
    current_db = get_current_db()    
    x = {}
    x['GlobalId'] = 'global'
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["ActivityContribution_Header1"] = (int(ref["basic_year"])) 
    x["ActivityContribution_Header2"] = (int(ref["basic_year"]) + 1 )
    x["ActivityContribution_Header3"] = (int(ref["basic_year"]) + 2 )
    x["ActivityContribution_Header4"] = (int(ref["basic_year"]) + 3 )
    x["ActivityContribution_Header5"] = (int(ref["basic_year"]) + 4 ) 
    i = 1
    lst = []
    while(i <1527):
        lst.append(("ActivityContribution_Input" + str(i)))
        i += 1
    
    for entry in lst:
        x[entry] = 0                  
                                    

    current_db.activitycontribution.insert_one(x)
    x = current_db.activitycontribution.find_one({"GlobalId": "global"})
    return render_template("activity-contribution.html", data=x)   

####################################################################################

@activitycontribution_bp.route('/activitycontribution/update', methods=['POST'])
@login_required
def activitycontribution_update():
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
        fin = current_db.financialincome.find_one({"GlobalId": "global"})
        finreq = current_db.financialrequirements.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["ActivityContribution_Header1"] = (int(ref["basic_year"])) 
        x["ActivityContribution_Header2"] = (int(ref["basic_year"]) + 1 )
        x["ActivityContribution_Header3"] = (int(ref["basic_year"]) + 2 )
        x["ActivityContribution_Header4"] = (int(ref["basic_year"]) + 3 )
        x["ActivityContribution_Header5"] = (int(ref["basic_year"]) + 4 )   

        #DAF:
        x["ActivityContribution_Input13"] = round(float(vehicle["TurnoverVehicle_Input_A"]))
        x["ActivityContribution_Input301"] = round(float(vehicle["TurnoverVehicle_Input_B"])) 
        x["ActivityContribution_Input681"] = round(float(vehicle["TurnoverVehicle_Input_C"]))
        x["ActivityContribution_Input973"] = round(float(vehicle["TurnoverVehicle_Input_E"]),3)
        x["ActivityContribution_Input1251"] = round(float(vehicle["TurnoverVehicle_Input_F"]),3)


        x["ActivityContribution_Input14"] = round(float(parts["TurnoverParts_Input20"]) - float(parts["TurnoverParts_Input36"]))
        x["ActivityContribution_Input302"] = round(float(parts["TurnoverParts_Input21"]) - float(parts["TurnoverParts_Input37"]))
        x["ActivityContribution_Input682"] = round(float(parts["TurnoverParts_Input22"]) - float(parts["TurnoverParts_Input38"]))
        x["ActivityContribution_Input974"] = round(float(parts["TurnoverParts_Input23"]) - float(parts["TurnoverParts_Input39"]),3)
        x["ActivityContribution_Input1252"] = round(float(parts["TurnoverParts_Input24"]) - float(parts["TurnoverParts_Input40"]),3)


        x["ActivityContribution_Input15"] = round(float(services["TurnoverServices_Input73"]))
        x["ActivityContribution_Input303"] = round(float(services["TurnoverServices_Input74"]))
        x["ActivityContribution_Input683"] = round(float(services["TurnoverServices_Input75"]))
        x["ActivityContribution_Input975"] = round(float(services["TurnoverServices_Input76"]),3)
        x["ActivityContribution_Input1253"] = round(float(services["TurnoverServices_Input77"]),3)

        x["ActivityContribution_Input17"] = round(float(x["ActivityContribution_Input13"]) + float(x["ActivityContribution_Input14"]) + float(x["ActivityContribution_Input15"]) + float(x["ActivityContribution_Input16"]))
        x["ActivityContribution_Input18"] = round(float(x["ActivityContribution_Input13"]) + float(x["ActivityContribution_Input14"]) + float(x["ActivityContribution_Input15"]) + float(x["ActivityContribution_Input16"]))

          

        #Oil & Lubricants:
        x["ActivityContribution_Input20"] = round(float(parts["TurnoverParts_Input25"]))
        x["ActivityContribution_Input308"] = round(float(parts["TurnoverParts_Input26"]))
        x["ActivityContribution_Input688"] = round(float(parts["TurnoverParts_Input27"]))
        x["ActivityContribution_Input980"] = round(float(parts["TurnoverParts_Input28"]))
        x["ActivityContribution_Input1258"] = round(float(parts["TurnoverParts_Input29"]))       

        x["ActivityContribution_Input23"] = round(float(x["ActivityContribution_Input19"]) + float(x["ActivityContribution_Input20"]) + float(x["ActivityContribution_Input21"]) + float(x["ActivityContribution_Input22"]))
        x["ActivityContribution_Input24"] = round(float(x["ActivityContribution_Input19"]) + float(x["ActivityContribution_Input20"]) + float(x["ActivityContribution_Input21"]) + float(x["ActivityContribution_Input22"])) 

        #Outsourced workshop activities:
        x["ActivityContribution_Input27"] = round(float(services["TurnoverServices_Input88"]))
        x["ActivityContribution_Input315"] = round(float(services["TurnoverServices_Input89"]))
        x["ActivityContribution_Input695"] = round(float(services["TurnoverServices_Input90"]))
        x["ActivityContribution_Input987"] = round(float(services["TurnoverServices_Input91"]))
        x["ActivityContribution_Input1265"] = round(float(services["TurnoverServices_Input92"]))

        x["ActivityContribution_Input29"] = round(float(x["ActivityContribution_Input25"]) + float(x["ActivityContribution_Input26"]) + float(x["ActivityContribution_Input27"]) + float(x["ActivityContribution_Input28"]))
        x["ActivityContribution_Input30"] = round(float(x["ActivityContribution_Input25"]) + float(x["ActivityContribution_Input26"]) + float(x["ActivityContribution_Input27"]) + float(x["ActivityContribution_Input28"]))  

        #Internal:
        x["ActivityContribution_Input32"] = round(float(parts["TurnoverParts_Input41"]))
        x["ActivityContribution_Input320"] = round(float(parts["TurnoverParts_Input42"]))
        x["ActivityContribution_Input701"] = round(float(parts["TurnoverParts_Input43"]))
        x["ActivityContribution_Input992"] = round(float(parts["TurnoverParts_Input44"]))
        x["ActivityContribution_Input1270"] = round(float(parts["TurnoverParts_Input45"]))


        x["ActivityContribution_Input33"] = float(services["TurnoverServices_Input78"])
        x["ActivityContribution_Input321"] = float(services["TurnoverServices_Input79"])
        x["ActivityContribution_Input702"] = float(services["TurnoverServices_Input80"])
        x["ActivityContribution_Input993"] = float(services["TurnoverServices_Input81"])
        x["ActivityContribution_Input1271"] = float(services["TurnoverServices_Input82"])

        x["ActivityContribution_Input35"] = float(x["ActivityContribution_Input31"]) + float(x["ActivityContribution_Input32"]) + float(x["ActivityContribution_Input33"]) + float(x["ActivityContribution_Input34"])
        #x["ActivityContribution_Input36"] = float(x["ActivityContribution_Input31"]) + float(x["ActivityContribution_Input32"]) + float(x["ActivityContribution_Input33"]) + float(x["ActivityContribution_Input34"])                           

        #Total:
        x["ActivityContribution_Input37"] = float(x["ActivityContribution_Input13"]) + float(x["ActivityContribution_Input19"]) + float(x["ActivityContribution_Input25"]) + float(x["ActivityContribution_Input31"])        
        x["ActivityContribution_Input38"] = float(x["ActivityContribution_Input14"]) + float(x["ActivityContribution_Input20"]) + float(x["ActivityContribution_Input26"]) + float(x["ActivityContribution_Input32"])
        x["ActivityContribution_Input39"] = float(x["ActivityContribution_Input15"]) + float(x["ActivityContribution_Input21"]) + float(x["ActivityContribution_Input27"]) + float(x["ActivityContribution_Input33"])
        x["ActivityContribution_Input40"] = float(x["ActivityContribution_Input16"]) + float(x["ActivityContribution_Input22"]) + float(x["ActivityContribution_Input28"]) + float(x["ActivityContribution_Input34"])
        x["ActivityContribution_Input41"] = float(x["ActivityContribution_Input17"]) + float(x["ActivityContribution_Input23"]) + float(x["ActivityContribution_Input29"]) + float(x["ActivityContribution_Input35"])
        x["ActivityContribution_Input42"] = float(x["ActivityContribution_Input18"]) + float(x["ActivityContribution_Input24"]) + float(x["ActivityContribution_Input30"]) + float(x["ActivityContribution_Input36"])

        x["ActivityContribution_Input706"] = float(x["ActivityContribution_Input681"]) + float(x["ActivityContribution_Input687"]) + float(x["ActivityContribution_Input693"]) + float(x["ActivityContribution_Input700"])        
        x["ActivityContribution_Input707"] = float(x["ActivityContribution_Input682"]) + float(x["ActivityContribution_Input688"]) + float(x["ActivityContribution_Input694"]) + float(x["ActivityContribution_Input701"])
        x["ActivityContribution_Input708"] = float(x["ActivityContribution_Input683"]) + float(x["ActivityContribution_Input689"]) + float(x["ActivityContribution_Input695"]) + float(x["ActivityContribution_Input702"])
        x["ActivityContribution_Input709"] = float(x["ActivityContribution_Input684"]) + float(x["ActivityContribution_Input690"]) + float(x["ActivityContribution_Input696"]) + float(x["ActivityContribution_Input703"])
       

        # Cost DAF
        x["ActivityContribution_Input55"] = float(costs["CostOFSales_Input131"])
        x["ActivityContribution_Input337"] = float(costs["CostOFSales_Input132"])
        x["ActivityContribution_Input724"] = float(costs["CostOFSales_Input133"]) 
        x["ActivityContribution_Input1015"] = float(costs["CostOFSales_Input134"]) 
        x["ActivityContribution_Input1293"] = float(costs["CostOFSales_Input135"])                      

        x["ActivityContribution_Input56"] = float(costs["CostOFSales_Input157"]) +  float(costs["CostOFSales_Input177"]) + float(costs["CostOFSales_Input187"])
        x["ActivityContribution_Input338"] = float(costs["CostOFSales_Input159"]) +  float(costs["CostOFSales_Input179"]) + float(costs["CostOFSales_Input189"]) 
        x["ActivityContribution_Input725"] = float(costs["CostOFSales_Input161"]) +  float(costs["CostOFSales_Input181"]) + float(costs["CostOFSales_Input191"]) 
        x["ActivityContribution_Input1016"] = float(costs["CostOFSales_Input163"]) +  float(costs["CostOFSales_Input183"]) + float(costs["CostOFSales_Input193"]) 
        x["ActivityContribution_Input1294"] = float(costs["CostOFSales_Input165"]) +  float(costs["CostOFSales_Input185"]) + float(costs["CostOFSales_Input195"])        


        # Cost Internal:
        x["ActivityContribution_Input59"] = float(x["ActivityContribution_Input55"]) +  float(x["ActivityContribution_Input56"]) + float(x["ActivityContribution_Input57"]) + float(x["ActivityContribution_Input58"])
        x["ActivityContribution_Input60"] = float(x["ActivityContribution_Input55"]) +  float(x["ActivityContribution_Input56"]) + float(x["ActivityContribution_Input57"]) + float(x["ActivityContribution_Input58"])

        # Cost Oil & Lubricants:
        x["ActivityContribution_Input62"] = float(costs["CostOFSales_Input197"])
        x["ActivityContribution_Input344"] = float(costs["CostOFSales_Input199"]) 
        x["ActivityContribution_Input731"] = float(costs["CostOFSales_Input201"]) 
        x["ActivityContribution_Input1022"] = float(costs["CostOFSales_Input203"]) 
        x["ActivityContribution_Input1300"] = float(costs["CostOFSales_Input205"])                                  

        x["ActivityContribution_Input65"] = float(x["ActivityContribution_Input61"]) +  float(x["ActivityContribution_Input62"]) + float(x["ActivityContribution_Input63"]) + float(x["ActivityContribution_Input64"])
        x["ActivityContribution_Input66"] = float(x["ActivityContribution_Input61"]) +  float(x["ActivityContribution_Input62"]) + float(x["ActivityContribution_Input63"]) + float(x["ActivityContribution_Input64"])    

        #Salaries & Wages 
        x["ActivityContribution_Input69"] = float(salaries["Salaries_Input299"])
        x["ActivityContribution_Input351"] = float(salaries["Salaries_Input300"])
        x["ActivityContribution_Input738"] = float(salaries["Salaries_Input301"])
        x["ActivityContribution_Input1029"] = float(salaries["Salaries_Input302"])
        x["ActivityContribution_Input1307"] = float(salaries["Salaries_Input303"])                                

        x["ActivityContribution_Input71"] = float(x["ActivityContribution_Input67"]) +  float(x["ActivityContribution_Input68"]) + float(x["ActivityContribution_Input69"]) + float(x["ActivityContribution_Input70"])
        x["ActivityContribution_Input72"] = float(x["ActivityContribution_Input67"]) +  float(x["ActivityContribution_Input68"]) + float(x["ActivityContribution_Input69"]) + float(x["ActivityContribution_Input70"])

        #Bonus supplier on sales
        x["ActivityContribution_Input73"] = float(costs["CostOFSales_Input137"])
        x["ActivityContribution_Input355"] = float(costs["CostOFSales_Input138"])
        x["ActivityContribution_Input742"] = float(costs["CostOFSales_Input139"])
        x["ActivityContribution_Input1033"] = float(costs["CostOFSales_Input140"])
        x["ActivityContribution_Input1311"] = float(costs["CostOFSales_Input141"])                


        #x["ActivityContribution_Input74"] = float(costs["CostOFSales_Input237"]) + float(costs["CostOFSales_Input247"])
        #x["ActivityContribution_Input356"] = float(costs["CostOFSales_Input238"]) + float(costs["CostOFSales_Input248"])
        #x["ActivityContribution_Input743"] = float(costs["CostOFSales_Input239"]) + float(costs["CostOFSales_Input249"])
        #x["ActivityContribution_Input1034"] = float(costs["CostOFSales_Input240"]) + float(costs["CostOFSales_Input250"])
        #x["ActivityContribution_Input1312"] = float(costs["CostOFSales_Input241"]) + float(costs["CostOFSales_Input251"]) 

        x["ActivityContribution_Input74"] = -float(costs["CostOFSales_Input237"])
        x["ActivityContribution_Input356"] = -float(costs["CostOFSales_Input239"])
        x["ActivityContribution_Input743"] = -float(costs["CostOFSales_Input241"])
        x["ActivityContribution_Input1034"] = -float(costs["CostOFSales_Input243"])
        x["ActivityContribution_Input1312"] = -float(costs["CostOFSales_Input245"])                             

        x["ActivityContribution_Input77"] = float(x["ActivityContribution_Input73"]) +  float(x["ActivityContribution_Input74"]) + float(x["ActivityContribution_Input75"]) + float(x["ActivityContribution_Input76"])
        x["ActivityContribution_Input78"] = float(x["ActivityContribution_Input73"]) +  float(x["ActivityContribution_Input74"]) + float(x["ActivityContribution_Input75"]) + float(x["ActivityContribution_Input76"])

        #Outsourced workshop activities:
        x["ActivityContribution_Input81"] = float(costs["CostOFSales_Input267"])
        x["ActivityContribution_Input363"] = float(costs["CostOFSales_Input269"])
        x["ActivityContribution_Input750"] = float(costs["CostOFSales_Input271"])
        x["ActivityContribution_Input1041"] = float(costs["CostOFSales_Input273"])
        x["ActivityContribution_Input1319"] = float(costs["CostOFSales_Input275"])                                

        x["ActivityContribution_Input83"] = float(x["ActivityContribution_Input79"]) +  float(x["ActivityContribution_Input80"]) + float(x["ActivityContribution_Input81"]) + float(x["ActivityContribution_Input82"])
        x["ActivityContribution_Input84"] = float(x["ActivityContribution_Input79"]) +  float(x["ActivityContribution_Input80"]) + float(x["ActivityContribution_Input81"]) + float(x["ActivityContribution_Input82"])

        #Internal:
        x["ActivityContribution_Input85"] = float(services["TurnoverServices_Input78"]) + float(parts["TurnoverParts_Input36"])
        x["ActivityContribution_Input367"] = float(services["TurnoverServices_Input79"]) + float(parts["TurnoverParts_Input37"])
        x["ActivityContribution_Input754"] = float(services["TurnoverServices_Input80"]) + float(parts["TurnoverParts_Input38"])
        x["ActivityContribution_Input1045"] = float(services["TurnoverServices_Input81"]) + float(parts["TurnoverParts_Input39"])
        x["ActivityContribution_Input1323"] = float(services["TurnoverServices_Input82"]) + float(parts["TurnoverParts_Input40"])                        

        x["ActivityContribution_Input89"] = float(x["ActivityContribution_Input85"]) +  float(x["ActivityContribution_Input86"]) + float(x["ActivityContribution_Input87"]) + float(x["ActivityContribution_Input88"])
        #x["ActivityContribution_Input90"] = float(x["ActivityContribution_Input85"]) +  float(x["ActivityContribution_Input86"]) + float(x["ActivityContribution_Input87"]) + float(x["ActivityContribution_Input88"]) 



        
        #Total Turnover
        # Year2:

        i = 301
        j = 302
        k = 303
        l = 304

        m = 325
        n = 326
        o = 327
        p = 328

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(300, 320) and j in range(301, 321) and k in range(302, 322) and l in range(303, 323):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6    


        # Year3:

        #i = 681
        #j = 682
        #k = 683
        #l = 684

        #m = 704
        #n = 705
        #o = 706
        #p = 707

        #total_i = []
        #total_j = []
        #total_k = []
        #total_l = []


        #while i in range(680, 701) and j in range(681, 702) and k in range(682, 703) and l in range(683, 704):

            #total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            #total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            #total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            #total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            #x['ActivityContribution_Input' + str(m)] = sum(total_i)
            #x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            #x['ActivityContribution_Input' + str(o)] = sum(total_k)
            #x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            #i += 6
            #j += 6
            #k += 6
            #l += 6    

        # Year4:

        i = 973
        j = 974
        k = 975
        l = 976

        m = 997
        n = 998
        o = 999
        p = 1000

        total_i = []
        total_j = []
        total_k = []
        total_l = []

        while i in range(972, 992) and j in range(973, 993) and k in range(974, 994) and l in range(975, 993):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6 

        # fix the range for variable j
        total_j.append(float(x['ActivityContribution_Input' + str(j)]))
        j += 1

        x['ActivityContribution_Input' + str(m)] = sum(total_i)
        x['ActivityContribution_Input' + str(n)] = sum(total_j)           
        x['ActivityContribution_Input' + str(o)] = sum(total_k)
        x['ActivityContribution_Input' + str(p)] = sum(total_l)


        # Year5:

        i = 1251
        j = 1252
        k = 1253
        l = 1254

        m = 1275
        n = 1276
        o = 1277
        p = 1278

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(1250, 1270) and j in range(1251, 1271) and k in range(1252, 1272) and l in range(1253, 1273):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6               


        #Total:
        x["ActivityContribution_Input91"] = round(float(x["ActivityContribution_Input55"]) +  float(x["ActivityContribution_Input61"]) + float(x["ActivityContribution_Input67"]) + float(x["ActivityContribution_Input73"])\
            + float(x["ActivityContribution_Input79"]) + float(x["ActivityContribution_Input85"]))

        x["ActivityContribution_Input92"] = round(float(x["ActivityContribution_Input56"]) +  float(x["ActivityContribution_Input62"]) + float(x["ActivityContribution_Input68"]) + float(x["ActivityContribution_Input74"])\
            + float(x["ActivityContribution_Input80"]) + float(x["ActivityContribution_Input86"]))

        x["ActivityContribution_Input93"] = round(float(x["ActivityContribution_Input57"]) +  float(x["ActivityContribution_Input63"]) + float(x["ActivityContribution_Input69"]) + float(x["ActivityContribution_Input75"])\
            + float(x["ActivityContribution_Input81"]) + float(x["ActivityContribution_Input87"]))

        x["ActivityContribution_Input94"] = round(float(x["ActivityContribution_Input58"]) +  float(x["ActivityContribution_Input64"]) + float(x["ActivityContribution_Input70"]) + float(x["ActivityContribution_Input76"])\
            + float(x["ActivityContribution_Input82"]) + float(x["ActivityContribution_Input88"]))

        x["ActivityContribution_Input95"] = round(float(x["ActivityContribution_Input59"]) +  float(x["ActivityContribution_Input65"]) + float(x["ActivityContribution_Input71"]) + float(x["ActivityContribution_Input77"])\
            + float(x["ActivityContribution_Input83"]) + float(x["ActivityContribution_Input89"]))

        x["ActivityContribution_Input96"] = round(float(x["ActivityContribution_Input60"]) +  float(x["ActivityContribution_Input66"]) + float(x["ActivityContribution_Input72"]) + float(x["ActivityContribution_Input78"])\
            + float(x["ActivityContribution_Input84"]) + float(x["ActivityContribution_Input90"]))


        x["ActivityContribution_Input379"] = float(x["ActivityContribution_Input337"]) + float(x["ActivityContribution_Input343"]) + float(x["ActivityContribution_Input349"]) + float(x["ActivityContribution_Input355"]) + float(x["ActivityContribution_Input361"]) + float(x["ActivityContribution_Input367"])
        x["ActivityContribution_Input380"] = float(x["ActivityContribution_Input338"]) + float(x["ActivityContribution_Input344"]) + float(x["ActivityContribution_Input350"]) + float(x["ActivityContribution_Input356"]) + float(x["ActivityContribution_Input362"]) + float(x["ActivityContribution_Input368"])
        x["ActivityContribution_Input381"] = float(x["ActivityContribution_Input339"]) + float(x["ActivityContribution_Input345"]) + float(x["ActivityContribution_Input351"]) + float(x["ActivityContribution_Input357"]) + float(x["ActivityContribution_Input363"]) + float(x["ActivityContribution_Input369"])
        x["ActivityContribution_Input382"] = float(x["ActivityContribution_Input340"]) + float(x["ActivityContribution_Input346"]) + float(x["ActivityContribution_Input352"]) + float(x["ActivityContribution_Input358"]) + float(x["ActivityContribution_Input364"]) + float(x["ActivityContribution_Input370"])


        #Total Cost of Sales: Year3:
        input = 760
        i = 724
        j = 730
        k = 736
        l = 742
        m = 748
        n = 754

        while input in range(759, 764) and i in range(723, 728) and j in range(729, 734) and k in range(735, 740) and l in range(741, 746) \
            and m in range(747, 752) and n in range(753, 758):

            x["ActivityContribution_Input" + str(input)] =  float(x["ActivityContribution_Input" + str(i)]) + float(x["ActivityContribution_Input" + str(j)]) \
                + float(x["ActivityContribution_Input" + str(k)]) + float(x["ActivityContribution_Input" + str(l)]) + float(x["ActivityContribution_Input" + str(m)]) \
                    + float(x["ActivityContribution_Input" + str(n)])

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1

            


        #Total Cost of Sales: Year4:
        input = 1051
        i = 1015
        j = 1021
        k = 1027
        l = 1033
        m = 1039
        n = 1045

        while input in range(1050, 1055) and i in range(1014, 1019) and j in range(1020, 1025) and k in range(1026, 1031) and l in range(1032, 1037) \
            and m in range(1038, 1043) and n in range(1044, 1049):

            x["ActivityContribution_Input" + str(input)] =  float(x["ActivityContribution_Input" + str(i)]) + float(x["ActivityContribution_Input" + str(j)]) \
                + float(x["ActivityContribution_Input" + str(k)]) + float(x["ActivityContribution_Input" + str(l)]) + float(x["ActivityContribution_Input" + str(m)]) \
                    + float(x["ActivityContribution_Input" + str(n)])

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1  


        #Total Cost of Sales: Year5:
        input = 1329
        i = 1293
        j = 1299
        k = 1305
        l = 1311
        m = 1317
        n = 1323

        while input in range(1328, 1333) and i in range(1292, 1297) and j in range(1298, 1303) and k in range(1304, 1309) and l in range(1310, 1315) \
            and m in range(1316, 1321) and n in range(1322, 1327):

            x["ActivityContribution_Input" + str(input)] =  float(x["ActivityContribution_Input" + str(i)]) + float(x["ActivityContribution_Input" + str(j)]) \
                + float(x["ActivityContribution_Input" + str(k)]) + float(x["ActivityContribution_Input" + str(l)]) + float(x["ActivityContribution_Input" + str(m)]) \
                    + float(x["ActivityContribution_Input" + str(n)])

            input += 1
            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1                       
            

        #Total Cost of Sales:
        #i = 55
        #j = 61
        #k = 67
        #l = 73
        #m = 79
        #n = 85
        #o = 91

        #while i in range(54, 61) and j in range(60, 67) and k in range(66, 73) and l in range(72, 79) and m in range(80, 85) and n in range(86, 91) and o in range(90, 97):
            #x["ActivityContribution_Input" + str(o)] = float(x["ActivityContribution_Input" + str(i)]) + float(x["ActivityContribution_Input" + str(j)]) + x["ActivityContribution_Input" + str(k)]\
                #+ x["ActivityContribution_Input" + str(l)] + x["ActivityContribution_Input" + str(m)] + x["ActivityContribution_Input" + str(n)]
        
            #i += 6
            #j += 6
            #k += 6
            #l += 6
            #m += 6
            #n += 6
            #o += 6         

        #Gross Profit/Loss:
        #Total_turnover = 37
        #Total_Cost_of_Sales = 91
        #Groos_Profit_Loss = 97

        #while Total_turnover in range(36, 43) and Total_Cost_of_Sales in range(90, 97) and Groos_Profit_Loss(96, 103):
           #x["ActivityContribution_Input" + str(Groos_Profit_Loss)] = float(x["ActivityContribution_Input" + str(Total_turnover)]) - float(x["ActivityContribution_Input" + str(Total_Cost_of_Sales)])
        #Total_turnover += 1
        #Total_Cost_of_Sales += 1
        #Groos_Profit_Loss += 1

        x["ActivityContribution_Input97"] = float(x["ActivityContribution_Input37"]) - x["ActivityContribution_Input91"]
        x["ActivityContribution_Input98"] = float(x["ActivityContribution_Input38"]) - x["ActivityContribution_Input92"]
        x["ActivityContribution_Input99"] = float(x["ActivityContribution_Input39"]) - x["ActivityContribution_Input93"]    
        x["ActivityContribution_Input100"] = float(x["ActivityContribution_Input40"]) - x["ActivityContribution_Input94"]
        x["ActivityContribution_Input101"] = float(x["ActivityContribution_Input41"]) - x["ActivityContribution_Input95"]
        x["ActivityContribution_Input102"] = float(x["ActivityContribution_Input42"]) - x["ActivityContribution_Input96"] 

        x["ActivityContribution_Input385"] = float(x["ActivityContribution_Input325"]) - x["ActivityContribution_Input379"]
        x["ActivityContribution_Input386"] = float(x["ActivityContribution_Input326"]) - x["ActivityContribution_Input380"]
        x["ActivityContribution_Input387"] = float(x["ActivityContribution_Input327"]) - x["ActivityContribution_Input381"]    
        x["ActivityContribution_Input388"] = float(x["ActivityContribution_Input328"]) - x["ActivityContribution_Input382"]

        x["ActivityContribution_Input766"] = float(x["ActivityContribution_Input706"]) - x["ActivityContribution_Input760"]
        x["ActivityContribution_Input767"] = float(x["ActivityContribution_Input707"]) - x["ActivityContribution_Input761"]
        x["ActivityContribution_Input768"] = float(x["ActivityContribution_Input708"]) - x["ActivityContribution_Input762"]    
        x["ActivityContribution_Input769"] = float(x["ActivityContribution_Input709"]) - x["ActivityContribution_Input763"]

        x["ActivityContribution_Input1057"] = float(x["ActivityContribution_Input997"]) - x["ActivityContribution_Input1051"]
        x["ActivityContribution_Input1058"] = float(x["ActivityContribution_Input998"]) - x["ActivityContribution_Input1052"]
        x["ActivityContribution_Input1059"] = float(x["ActivityContribution_Input999"]) - x["ActivityContribution_Input1053"]    
        x["ActivityContribution_Input1060"] = float(x["ActivityContribution_Input1000"]) - x["ActivityContribution_Input1054"]

        x["ActivityContribution_Input1335"] = float(x["ActivityContribution_Input1275"]) - x["ActivityContribution_Input1329"]
        x["ActivityContribution_Input1336"] = float(x["ActivityContribution_Input1276"]) - x["ActivityContribution_Input1330"]
        x["ActivityContribution_Input1337"] = float(x["ActivityContribution_Input1277"]) - x["ActivityContribution_Input1331"]    
        x["ActivityContribution_Input1338"] = float(x["ActivityContribution_Input1278"]) - x["ActivityContribution_Input1332"]                 


 

        
        #x["ActivityContribution_Input241"] = x["ActivityContribution_Input97"] - x["ActivityContribution_Input103"] - x["ActivityContribution_Input109"] - x["ActivityContribution_Input229"]\
            #- x["ActivityContribution_Input235"]

        #x["ActivityContribution_Input242"] = x["ActivityContribution_Input98"] - x["ActivityContribution_Input104"] - x["ActivityContribution_Input110"] - x["ActivityContribution_Input230"]\
           # - x["ActivityContribution_Input236"]
        
        #x["ActivityContribution_Input243"] = x["ActivityContribution_Input99"] - x["ActivityContribution_Input105"] - x["ActivityContribution_Input111"] - x["ActivityContribution_Input231"]\
           # - x["ActivityContribution_Input237"]

        #x["ActivityContribution_Input244"] = x["ActivityContribution_Input100"] - x["ActivityContribution_Input106"] - x["ActivityContribution_Input112"] - x["ActivityContribution_Input232"]\
            #- x["ActivityContribution_Input238"]





        # Gross Profit/Loss: Year 2:

        #input = 385
        #i = 325
        #j = 379

        #while input in range(384, 389) and i in range(324, 329) and j in range(378, 383):

            #x["ActivityContribution_Input" + str(input)] = float(x["ActivityContribution_Input" + str(i)]) - float(x["ActivityContribution_Input" + str(j)])
        
        #input += 1
        #i += 1
        #j += 1   

        #Gross Profit/Loss: Year 3:

        #i = 766
        #j = 706
        #k = 760

        #while i in range(765, 770) and j in range(705, 710) and k in range(759, 764):

            #x["ActivityContribution_Input" + str(i)] = float(x["ActivityContribution_Input" + str(j)]) - float(x["ActivityContribution_Input" + str(k)])
        
        #i += 1
        #j += 1
        #k += 1

        #Gross Profit/Loss: Year 4:

        #i = 1057
        #j = 997
        #k = 1051

        #while i in range(1056, 1061) and j in range(996, 1001) and k in range(1050, 1055):

            #x["ActivityContribution_Input" + str(i)] = float(x["ActivityContribution_Input" + str(j)]) - float(x["ActivityContribution_Input" + str(k)])
        
        #i += 1
        #j += 1
        #k += 1 

        #Gross Profit/Loss: Year 5:

        #i = 1335
        #j = 1275
        #k = 1329

        #while i in range(1334, 1339) and j in range(1274, 1279) and k in range(1328, 1333):

            #x["ActivityContribution_Input" + str(i)] = float(x["ActivityContribution_Input" + str(j)]) - float(x["ActivityContribution_Input" + str(k)])
        
        #i += 1
        #j += 1
        #k += 1                        


        #Selling expenses:
        x["ActivityContribution_Input103"] = round(float(vehicle["TurnoverVehicle_Input126"]) * float(salaries["Salaries_Input13136"]) * (1 + (float(salaries["Salaries_Input231"])/100)) + float(selling["SellingOperation_Input5"]) * (float(selling["SellingOperation_Input159"])/100),0)
        x["ActivityContribution_Input391"] = float(vehicle["TurnoverVehicle_Input127"]) * float(salaries["Salaries_Input13137"]) * (1 + (float(salaries["Salaries_Input231"])/100)) + float(selling["SellingOperation_Input6"]) * (float(selling["SellingOperation_Input159"])/100)
        x["ActivityContribution_Input772"] = float(vehicle["TurnoverVehicle_Input128"]) * float(salaries["Salaries_Input13138"]) * (1 + (float(salaries["Salaries_Input231"])/100)) + float(selling["SellingOperation_Input7"]) * (float(selling["SellingOperation_Input159"])/100)
        x["ActivityContribution_Input1063"] = float(vehicle["TurnoverVehicle_Input129"]) * float(salaries["Salaries_Input13139"]) * (1 + (float(salaries["Salaries_Input231"])/100)) + float(selling["SellingOperation_Input8"]) * (float(selling["SellingOperation_Input159"])/100)
        x["ActivityContribution_Input1341"] = float(vehicle["TurnoverVehicle_Input130"]) * float(salaries["Salaries_Input13140"]) * (1 + (float(salaries["Salaries_Input231"])/100)) + float(selling["SellingOperation_Input9"]) * (float(selling["SellingOperation_Input159"])/100)



        x["ActivityContribution_Input104"] = float(selling["SellingOperation_Input5"]) * float(selling["SellingOperation_Input160"])
        x["ActivityContribution_Input392"] = float(selling["SellingOperation_Input6"]) * float(selling["SellingOperation_Input160"]) 
        x["ActivityContribution_Input773"] = float(selling["SellingOperation_Input7"]) * float(selling["SellingOperation_Input160"])
        x["ActivityContribution_Input1064"] = float(selling["SellingOperation_Input8"]) * float(selling["SellingOperation_Input160"])
        x["ActivityContribution_Input1342"] = float(selling["SellingOperation_Input9"]) * float(selling["SellingOperation_Input160"])                               

        x["ActivityContribution_Input105"] = float(selling["SellingOperation_Input5"]) * float(selling["SellingOperation_Input161"])
        x["ActivityContribution_Input393"] = float(selling["SellingOperation_Input6"]) * float(selling["SellingOperation_Input161"]) 
        x["ActivityContribution_Input774"] = float(selling["SellingOperation_Input7"]) * float(selling["SellingOperation_Input161"])
        x["ActivityContribution_Input1065"] = float(selling["SellingOperation_Input8"]) * float(selling["SellingOperation_Input161"])
        x["ActivityContribution_Input1343"] = float(selling["SellingOperation_Input9"]) * float(selling["SellingOperation_Input161"])                       

        x["ActivityContribution_Input106"] = float(selling["SellingOperation_Input5"]) * float(selling["SellingOperation_Input162"])
        x["ActivityContribution_Input394"] = float(selling["SellingOperation_Input6"]) * float(selling["SellingOperation_Input162"]) 
        x["ActivityContribution_Input775"] = float(selling["SellingOperation_Input7"]) * float(selling["SellingOperation_Input162"])
        x["ActivityContribution_Input1066"] = float(selling["SellingOperation_Input8"]) * float(selling["SellingOperation_Input162"]) 
        x["ActivityContribution_Input1344"] = float(selling["SellingOperation_Input9"]) * float(selling["SellingOperation_Input162"])                              

        x["ActivityContribution_Input107"] = float(x["ActivityContribution_Input103"]) + float(x["ActivityContribution_Input104"]) + float(x["ActivityContribution_Input105"]) + float(x["ActivityContribution_Input106"])
        x["ActivityContribution_Input108"] = float(x["ActivityContribution_Input103"]) + float(x["ActivityContribution_Input104"]) + float(x["ActivityContribution_Input105"]) + float(x["ActivityContribution_Input106"])            


        #Other Operating:

            # Year1 

        i = 121
        j = 122
        k = 123
        l = 124

        m = 164
        n = 165
        o = 166
        p = 167

        q = 10

 
        while i in range(120, 158) and m in range(163, 195) and q in range(9, 41) \
            and j in range(121, 159) and n in range(164, 196)and \
                k in range(122, 160) and o in range(165, 197)\
                    and l in range(123, 161) and p in range(166, 198):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)                                    

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5       


        i = 163
        j = 164
        k = 165
        l = 166

        m = 204
        n = 205
        o = 206
        p = 207


        q = 45

        while i in range(162, 176) and m in range(203, 215) and q in range(44, 56) \
            and j in range(163, 177) and n in range(204, 216) and \
                k in range(164, 178) and o in range(205, 217) and \
                    l in range(165, 179) and p in range(206, 218):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5  



        i = 181
        j = 182
        k = 183
        l = 184

        m = 224
        n = 225
        o = 226
        p = 227

        q = 60


        x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)



        i = 187
        j = 188
        k = 189
        l = 190

        m = 234
        n = 235
        o = 236
        p = 237

        q = 65

        while i in range(186, 224) and m in range(233, 265) and q in range(64, 96) \
            and j in range(187, 225) and n in range(234, 266) and \
                k in range(188, 226) and o in range(235, 267) and \
                    l in range(189, 227) and p in range(236, 268):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5   

           # Year2 

        i = 499
        j = 500
        k = 501
        l = 502

        m = 164
        n = 165
        o = 166
        p = 167

        q = 11

 
        while i in range(498, 536) and m in range(163, 195) and q in range(10, 42) \
            and j in range(499, 537) and n in range(164, 196)and \
                k in range(500, 538) and o in range(165, 197)\
                    and l in range(501, 539) and p in range(166, 198):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)                                  

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5       


        i = 541
        j = 542
        k = 543
        l = 544

        m = 204
        n = 205
        o = 206
        p = 207


        q = 46

        while i in range(540, 554) and m in range(203, 215) and q in range(45, 57) \
            and j in range(541,555) and n in range(204, 216) and \
                k in range(542, 556) and o in range(205, 217) and \
                    l in range(543, 557) and p in range(206, 218):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5   


        i = 559
        j = 560
        k = 561
        l = 562

        m = 224
        n = 225
        o = 226
        p = 227

        q = 61




        x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)




        i = 565
        j = 566
        k = 567
        l = 568

        m = 234
        n = 235
        o = 236
        p = 237

        q = 66

        while i in range(564, 604) and m in range(233, 265) and q in range(65, 97) \
            and j in range(565, 605) and n in range (234, 266) \
                and k in range(566, 606) and o in range(235, 267) \
                    and l in range (567, 607) and p in range(236, 268):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)


            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5  

           # Year3

        i = 790
        j = 791
        k = 792
        l = 793

        m = 164
        n = 165
        o = 166
        p = 167

        q = 12

 
        while i in range(789, 827) and m in range(163, 195) and q in range(11, 43) \
            and j in range(790, 828) and n in range(164, 196)and \
                k in range(791, 829) and o in range(165, 197)\
                    and l in range(792, 830) and p in range(166, 198):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)                                   

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5       




        i = 832
        j = 833
        k = 834
        l = 835

        m = 204
        n = 205
        o = 206
        p = 207


        q = 47

        while i in range(831, 845) and m in range(203, 215) and q in range(46, 58) \
            and j in range(832,846) and n in range(204, 216) and \
                k in range(833, 847) and o in range(205, 217) and \
                    l in range(834, 848) and p in range(206, 218):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5   


        i = 850
        j = 851
        k = 852
        l = 853

        m = 224
        n = 225
        o = 226
        p = 227

        q = 62




        x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)




        i = 856
        j = 857
        k = 858
        l = 859

        m = 234
        n = 235
        o = 236
        p = 237

        q = 67

        while i in range(855, 893) and m in range(233, 265) and q in range(66, 98) \
            and j in range(856, 894) and n in range (234, 266) \
                and k in range(857, 895) and o in range(235, 267) \
                    and l in range (858, 896) and p in range(236, 268):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)


            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5  

           # Year4

        i = 1081
        j = 1082
        k = 1083
        l = 1084

        m = 164
        n = 165
        o = 166
        p = 167

        q = 13

 
        while i in range(1080, 1118) and m in range(163, 195) and q in range(12, 44) \
            and j in range(1081, 1119) and n in range(164, 196)and \
                k in range(1082, 1120) and o in range(165, 197)\
                    and l in range(1083, 1121) and p in range(166, 198):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100) 
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100) 
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100) 
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)                                   

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5       


        i = 1123
        j = 1124
        k = 1125
        l = 1126

        m = 204
        n = 205
        o = 206
        p = 207


        q = 48

        while i in range(1122, 1136) and m in range(203, 215) and q in range(47, 59) \
            and j in range(1123,1137) and n in range(204, 216) and \
                k in range(1124, 1138) and o in range(205, 217) and \
                    l in range(1125, 1139) and p in range(206, 218):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5   


        i = 1141
        j = 1142
        k = 1143
        l = 1144

        m = 224
        n = 225
        o = 226
        p = 227

        q = 63




        x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)




        i = 1147
        j = 1148
        k = 1149
        l = 1150

        m = 234
        n = 235
        o = 236
        p = 237

        q = 68

        while i in range(1146, 1185) and m in range(233, 265) and q in range(67, 99) \
            and j in range(1147, 1186) and n in range (234, 266) \
                and k in range(1148, 1187) and o in range(235, 267) \
                    and l in range (1149, 1188) and p in range(236, 268):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)


            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5                        

            
           # Year5

        i = 1359
        j = 1360
        k = 1361
        l = 1362

        m = 164
        n = 165
        o = 166
        p = 167

        q = 14

 
        while i in range(1358, 1396) and m in range(163, 195) and q in range(13, 45) \
            and j in range(1359, 1397) and n in range(164, 196)and \
                k in range(1360, 1398) and o in range(165, 197)\
                    and l in range(1361, 1399) and p in range(166, 198):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)                                   

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5       


        i = 1401
        j = 1402
        k = 1403
        l = 1404

        m = 204
        n = 205
        o = 206
        p = 207


        q = 49

        while i in range(1400, 1414) and m in range(203, 215) and q in range(48, 60) \
            and j in range(1401,1415) and n in range(204, 216) and \
                k in range(1402, 1416) and o in range(205, 217) and \
                    l in range(1403, 1417) and p in range(206, 218):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)

            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5   


        i = 1419
        j = 1420
        k = 1421
        l = 1422

        m = 224
        n = 225
        o = 226
        p = 227

        q = 63




        x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
        x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)




        i = 1425
        j = 1426
        k = 1427
        l = 1428

        m = 234
        n = 235
        o = 236
        p = 237

        q = 69

        while i in range(1424, 1462) and m in range(233, 265) and q in range(68, 100) \
            and j in range(1425, 1463) and n in range (234, 266) \
                and k in range(1426, 1464) and o in range(235, 267) \
                    and l in range (1427, 1465) and p in range(236, 268):

            x['ActivityContribution_Input' + str(i)] =  float(selling['SellingOperation_Input' + str(m)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(j)] =  float(selling['SellingOperation_Input' + str(n)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(k)] =  float(selling['SellingOperation_Input' + str(o)]) * (float(selling['SellingOperation_Input' + str(q)])/100)
            x['ActivityContribution_Input' + str(l)] =  float(selling['SellingOperation_Input' + str(p)]) * (float(selling['SellingOperation_Input' + str(q)])/100)


            i += 6
            j += 6
            k += 6
            l += 6

            m += 5
            n += 5
            o += 5
            p += 5 

            q += 5


        #x['ActivityContribution_Input856'] =  float(selling['SellingOperation_Input67']) * (float(selling['SellingOperation_Input234'])/100)
        #x['ActivityContribution_Input857'] =  float(selling['SellingOperation_Input68']) * (float(selling['SellingOperation_Input235'])/100)
        #x['ActivityContribution_Input858'] =  float(selling['SellingOperation_Input69']) * (float(selling['SellingOperation_Input236'])/100)

        #Total other operating expenses :
        #Year1:

        i = 121
        j = 122
        k = 123
        l = 124

        m = 229
        n = 230
        o = 231
        p = 232

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(120, 224) and j in range(121, 225) and k in range(122, 226) and l in range(123, 227):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6


        # Year 2:

        i = 499
        j = 500
        k = 501
        l = 502

        m = 607
        n = 608
        o = 609
        p = 610

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(498, 602) and j in range(499, 603) and k in range(500, 604) and l in range(501, 605):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6   

        # Year 3:

        i = 790
        j = 791
        k = 792
        l = 793

        m = 898
        n = 899
        o = 900
        p = 901

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(789, 893) and j in range(790, 894) and k in range(791, 895) and l in range(792, 896):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6  

        # Year 4:

        i = 1081
        j = 1082
        k = 1083
        l = 1084

        m = 1190
        n = 1191
        o = 1192
        p = 1193

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(1080, 1184) and j in range(1081, 1185) and k in range(1082, 1186) and l in range(1083, 1187):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6   

        # Year 5:

        i = 1359
        j = 1360
        k = 1361
        l = 1362

        m = 1467
        n = 1468
        o = 1469
        p = 1470

        total_i = []
        total_j = []
        total_k = []
        total_l = []


        while i in range(1358, 1462) and j in range(1359, 1463) and k in range(1360, 1464) and l in range(1361, 1465):

            total_i.append(float(x['ActivityContribution_Input' + str(i)]))
            total_j.append(float(x['ActivityContribution_Input' + str(j)]))
            total_k.append(float(x['ActivityContribution_Input' + str(k)]))
            total_l.append(float(x['ActivityContribution_Input' + str(l)]))

            x['ActivityContribution_Input' + str(m)] = sum(total_i)
            x['ActivityContribution_Input' + str(n)] = sum(total_j)           
            x['ActivityContribution_Input' + str(o)] = sum(total_k)
            x['ActivityContribution_Input' + str(p)] = sum(total_l) 

            i += 6
            j += 6
            k += 6
            l += 6     




        #Salaries & Wages

        #Depreciations & Amortization
        x['ActivityContribution_Input235'] = float(inv['InvDep_Input296'])
        x['ActivityContribution_Input615'] = float(inv['InvDep_Input297'])        
        x['ActivityContribution_Input904'] = float(inv['InvDep_Input298'])
        x['ActivityContribution_Input1196'] = float(inv['InvDep_Input299'])
        x['ActivityContribution_Input1473'] = float(inv['InvDep_Input300'])
        
        x['ActivityContribution_Input236'] = float(inv['InvDep_Input302'])
        x['ActivityContribution_Input616'] = float(inv['InvDep_Input303'])        
        x['ActivityContribution_Input905'] = float(inv['InvDep_Input304'])
        x['ActivityContribution_Input1197'] = float(inv['InvDep_Input305'])
        x['ActivityContribution_Input1474'] = float(inv['InvDep_Input306'])

        x['ActivityContribution_Input238'] = float(inv['InvDep_Input230']) + float(inv['InvDep_Input278']) + float(inv['InvDep_Input308'])
        x['ActivityContribution_Input618'] = float(inv['InvDep_Input231']) + float(inv['InvDep_Input279'])  + float(inv['InvDep_Input309'])      
        x['ActivityContribution_Input907'] = float(inv['InvDep_Input232']) + float(inv['InvDep_Input280']) + float(inv['InvDep_Input310'])
        x['ActivityContribution_Input1199'] = float(inv['InvDep_Input233']) + float(inv['InvDep_Input281']) + float(inv['InvDep_Input311'])
        x['ActivityContribution_Input1476'] = float(inv['InvDep_Input234'])   + float(inv['InvDep_Input282']) + float(inv['InvDep_Input312'])                            


        #Salaries & Wages:

        #='7.2.1 Turnover Vehicles'!C84*'7.4.1 Salaries & Wages'!C80+(B16/(B16+C16+D16+0.00001)*('7.4.1 Salaries & Wages'!C71+'7.4.1 Salaries & Wages'!C91))-('7.2.1 Turnover Vehicles'!$C$84*(1+'7.4.1 Salaries & Wages'!$B$78))
        formula = round(float(vehicle['TurnoverVehicle_Input126'])) * float(salaries['Salaries_Input237'])+((float(x['ActivityContribution_Input37']))/((float(x['ActivityContribution_Input37']))+0.00001)*(float(salaries['Salaries_Input221'])+float(salaries['Salaries_Input273'])))-(float(vehicle['TurnoverVehicle_Input126']))*(1+(float(salaries['Salaries_Input231'])/100)) 
        x['ActivityContribution_Input109'] = round(formula) 
        

        x['ActivityContribution_Input397'] =  float(vehicle['TurnoverVehicle_Input127']) * float(salaries['Salaries_Input238']) + (float(x['ActivityContribution_Input38']) / (float(x['ActivityContribution_Input38'])+0.00001) * (float(salaries['Salaries_Input222']) + float(salaries['Salaries_Input274']))) - (float(vehicle['TurnoverVehicle_Input127']) * float(salaries['Salaries_Input13137']) * (1+(float(salaries['Salaries_Input231'])/100)))
        x['ActivityContribution_Input778'] =  float(vehicle['TurnoverVehicle_Input128']) * float(salaries['Salaries_Input239']) + (float(x['ActivityContribution_Input379']) / (float(x['ActivityContribution_Input379'])+0.00001) * (float(salaries['Salaries_Input223']) + float(salaries['Salaries_Input275']))) - (float(vehicle['TurnoverVehicle_Input128']) * float(salaries['Salaries_Input13138']) * (1+(float(salaries['Salaries_Input231'])/100)))
        x['ActivityContribution_Input1069'] = float(vehicle['TurnoverVehicle_Input129']) * float(salaries['Salaries_Input240']) + (float(x['ActivityContribution_Input706']) / (float(x['ActivityContribution_Input706'])+0.00001) * (float(salaries['Salaries_Input224']) + float(salaries['Salaries_Input276']))) - (float(vehicle['TurnoverVehicle_Input129']) * float(salaries['Salaries_Input13139']) * (1+(float(salaries['Salaries_Input231'])/100)))
        x['ActivityContribution_Input1347'] = float(vehicle['TurnoverVehicle_Input130']) * float(salaries['Salaries_Input241']) + (float(x['ActivityContribution_Input997']) / (float(x['ActivityContribution_Input997'])+0.00001) * (float(salaries['Salaries_Input225']) + float(salaries['Salaries_Input277']))) - (float(vehicle['TurnoverVehicle_Input130']) * float(salaries['Salaries_Input13140']) * (1+(float(salaries['Salaries_Input231'])/100)))
        
              

        #x['ActivityContribution_Input397'] = round(float(vehicle['TurnoverVehicle_Input127']) * float(salaries['Salaries_Input238']) + (float(x['ActivityContribution_Input38'])/(float(x['ActivityContribution_Input38'])+0.00001)*(float(salaries['Salaries_Input222'])+float(salaries['Salaries_Input274'])))-(float(vehicle['TurnoverVehicle_Input127'])*(1+float(salaries['Salaries_Input232']))),0) 
        #x['ActivityContribution_Input778'] = round(float(vehicle['TurnoverVehicle_Input128']) * float(salaries['Salaries_Input239']) + ((float(x['ActivityContribution_Input39']) / (float(x['ActivityContribution_Input39'])) + 0.00001)) * float(salaries['Salaries_Input223']) + float(salaries['Salaries_Input275']) - (float(vehicle['TurnoverVehicle_Input128']) * float(salaries['Salaries_Input13138'])) * (1 + float(salaries['Salaries_Input231'])),0) 
        #x['ActivityContribution_Input1069'] = round(float(vehicle['TurnoverVehicle_Input129']) * float(salaries['Salaries_Input240']) + ((float(x['ActivityContribution_Input40']) / (float(x['ActivityContribution_Input40'])) + 0.00001)) * float(salaries['Salaries_Input224']) + float(salaries['Salaries_Input276']) - (float(vehicle['TurnoverVehicle_Input129']) * float(salaries['Salaries_Input13139'])) * (1 + float(salaries['Salaries_Input231'])),0) 
        #x['ActivityContribution_Input1347'] = round(float(vehicle['TurnoverVehicle_Input130']) * float(salaries['Salaries_Input241']) + ((float(x['ActivityContribution_Input41']) / (float(x['ActivityContribution_Input41'])) + 0.00001)) * float(salaries['Salaries_Input225']) + float(salaries['Salaries_Input277']) - (float(vehicle['TurnoverVehicle_Input130']) * float(salaries['Salaries_Input13140'])) * (1 + float(salaries['Salaries_Input231'])),0) 

        x['ActivityContribution_Input110']= round(float(salaries['Salaries_Input403']) + float(salaries['Salaries_Input429']) + float(salaries['Salaries_Input455']) + float(salaries['Salaries_Input481']),0) 
        x['ActivityContribution_Input398']= round(float(salaries['Salaries_Input404']) + float(salaries['Salaries_Input430']) + float(salaries['Salaries_Input456']) + float(salaries['Salaries_Input482']),3) 
        x['ActivityContribution_Input779']= round(float(salaries['Salaries_Input405']) + float(salaries['Salaries_Input431']) + float(salaries['Salaries_Input457']) + float(salaries['Salaries_Input483']),3) 
        x['ActivityContribution_Input1070']= round(float(salaries['Salaries_Input406']) + float(salaries['Salaries_Input432']) + float(salaries['Salaries_Input458']) + float(salaries['Salaries_Input484']),3)       
        x['ActivityContribution_Input1348']= round(float(salaries['Salaries_Input407']) + float(salaries['Salaries_Input433']) + float(salaries['Salaries_Input459']) + float(salaries['Salaries_Input485']),3) 


        x['ActivityContribution_Input111']= round(float(salaries['Salaries_Input351']) + float(salaries['Salaries_Input377'])) 
        x['ActivityContribution_Input399']= round(float(salaries['Salaries_Input352']) + float(salaries['Salaries_Input378'])) 
        x['ActivityContribution_Input780']= round(float(salaries['Salaries_Input353']) + float(salaries['Salaries_Input379'])) 
        x['ActivityContribution_Input1071']= round(float(salaries['Salaries_Input354']) + float(salaries['Salaries_Input380']))         
        x['ActivityContribution_Input1349']= round(float(salaries['Salaries_Input355']) + float(salaries['Salaries_Input381'])) 


        x['ActivityContribution_Input112']= round(float(salaries['Salaries_Input114']) +float(salaries['Salaries_Input140'])+ float(salaries['Salaries_Input168']) + float(salaries['Salaries_Input194']) ,0) 
        x['ActivityContribution_Input400']= round(float(salaries['Salaries_Input115']) +float(salaries['Salaries_Input141'])+ float(salaries['Salaries_Input169']) + float(salaries['Salaries_Input195']) ,3) 
        x['ActivityContribution_Input781']= round(float(salaries['Salaries_Input116']) +float(salaries['Salaries_Input142'])+ float(salaries['Salaries_Input170']) + float(salaries['Salaries_Input196'])  ,3) 
        x['ActivityContribution_Input1072']= round(float(salaries['Salaries_Input117']) +float(salaries['Salaries_Input143'])+ float(salaries['Salaries_Input171']) + float(salaries['Salaries_Input197'])  ,3)     
        x['ActivityContribution_Input1350']= round(float(salaries['Salaries_Input118']) +float(salaries['Salaries_Input144'])+ float(salaries['Salaries_Input172']) + float(salaries['Salaries_Input198'])  ,3)       

       #Operating profit/loss per activity:
        # Year1:
            
        i = 241
        j = 97
        k = 103
        l = 109
        m = 229
        n = 235
                                                                                
        while i in range(240, 245) and j in range(96, 101) and k in range(102, 107) and l in range(108, 113) and m in range(228, 233) and n in range(234, 239):
            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(j)]) - float(x['ActivityContribution_Input' + str(k)]) \
                - float(x['ActivityContribution_Input' + str(l)]) - float(x['ActivityContribution_Input' + str(m)]) - float(x['ActivityContribution_Input' + str(n)]),3)

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1

        # Year2:
            
        i = 621
        j = 385
        k = 391
        l = 397
        m = 607
        n = 615
                                                                                
        while i in range(620, 625) and j in range(384, 389) and k in range(390, 395) and l in range(396, 401) and m in range(606, 611) and n in range(614, 619):
            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(j)]) - float(x['ActivityContribution_Input' + str(k)]) \
                - float(x['ActivityContribution_Input' + str(l)]) - float(x['ActivityContribution_Input' + str(m)]) - float(x['ActivityContribution_Input' + str(n)]),3)

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1

        # Year3:
            
        i = 910
        j = 766
        k = 772
        l = 778
        m = 898
        n = 904
                                                                                
        while i in range(909, 914) and j in range(765, 770) and k in range(771, 776) and l in range(777, 782) and m in range(897, 902) and n in range(903, 908):
            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(j)]) - float(x['ActivityContribution_Input' + str(k)]) \
                - float(x['ActivityContribution_Input' + str(l)]) - float(x['ActivityContribution_Input' + str(m)]) - float(x['ActivityContribution_Input' + str(n)]),3)

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1  

        # Year4:
            
        i = 1203
        j = 1057
        k = 1063
        l = 1069
        m = 1190
        n = 1196
                                                                                
        while i in range(1202, 1207) and j in range(1056, 1061) and k in range(1062, 1067) and l in range(1068, 1073) and m in range(1189, 1194) and n in range(1195, 1200):
            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(j)]) - float(x['ActivityContribution_Input' + str(k)]) \
                - float(x['ActivityContribution_Input' + str(l)]) - float(x['ActivityContribution_Input' + str(m)]) - float(x['ActivityContribution_Input' + str(n)]),3)

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1   

        # Year5:
            
        i = 1479
        j = 1335
        k = 1341
        l = 1347
        m = 1467
        n = 1473
                                                                                
        while i in range(1478, 1483) and j in range(1334, 1339) and k in range(1340, 1345) and l in range(1346, 1351) and m in range(1466, 1471) and n in range(1472, 1477):
            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(j)]) - float(x['ActivityContribution_Input' + str(k)]) \
                - float(x['ActivityContribution_Input' + str(l)]) - float(x['ActivityContribution_Input' + str(m)]) - float(x['ActivityContribution_Input' + str(n)]),3)

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1                                 
                    #####################################################################

            x['ActivityContribution_Input250'] = -float(fin['FinancialExp_Input152']) 
            x['ActivityContribution_Input256'] = -float(fin['FinancialExp_Input162']) 
            x['ActivityContribution_Input262'] = -float(fin['FinancialExp_Input173'])
            x['ActivityContribution_Input630'] = -float(fin['FinancialExp_Input154'])
            x['ActivityContribution_Input636'] = - float(fin['FinancialExp_Input164'])
            x['ActivityContribution_Input642'] = -float(fin['FinancialExp_Input175'])
            x['ActivityContribution_Input919'] = -float(fin['FinancialExp_Input156'])
            x['ActivityContribution_Input925'] = -float(fin['FinancialExp_Input166'])
            x['ActivityContribution_Input931'] = -float(fin['FinancialExp_Input177'])
            x['ActivityContribution_Input1212'] = -float(fin['FinancialExp_Input158'])
            x['ActivityContribution_Input1218'] = -float(fin['FinancialExp_Input168'])
            x['ActivityContribution_Input1224'] = -float(fin['FinancialExp_Input179'])
            x['ActivityContribution_Input1488'] = -float(fin['FinancialExp_Input160'])
            x['ActivityContribution_Input1494'] = -float(fin['FinancialExp_Input170'])
            x['ActivityContribution_Input1500'] = -float(fin['FinancialExp_Input181']) 


            #####################################################################
            x['ActivityContribution_Input265'] = float(finreq['FinancialRequirement_Input92']) * (float(fin['FinancialExp_Input116'])/100) * (float(fin['FinancialExp_Input182'])/100)
            x['ActivityContribution_Input645'] = float(finreq['FinancialRequirement_Input94']) * (float(fin['FinancialExp_Input117'])/100) * (float(fin['FinancialExp_Input182'])/100)
            x['ActivityContribution_Input934'] = float(finreq['FinancialRequirement_Input96']) * (float(fin['FinancialExp_Input118'])/100) * (float(fin['FinancialExp_Input182'])/100)
            x['ActivityContribution_Input1227'] = float(finreq['FinancialRequirement_Input98']) * (float(fin['FinancialExp_Input119'])/100) * (float(fin['FinancialExp_Input182'])/100)
            x['ActivityContribution_Input1503'] = float(finreq['FinancialRequirement_Input100']) * (float(fin['FinancialExp_Input120'])/100) * (float(fin['FinancialExp_Input182'])/100)                                    


        #Financial Expenses Y1:
        #input = 271
        #i = 247
        #j = 253
        #k = 249
        #l = 265

        #while input in range(270, 275) and i in range(246, 251) and j in range(252, 257) and k in range(258, 263) \
            #and l in range(264, 269):

            #x['ActivityContribution_Input' + str(input)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) \
                #+ float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])

        #input += 1
        #i += 1
        #j += 1
        #k += 1
        #l += 1

        x['ActivityContribution_Input271'] = float(x['ActivityContribution_Input247']) + float(x['ActivityContribution_Input253']) + float(x['ActivityContribution_Input247']) + float(x['ActivityContribution_Input265'])
        x['ActivityContribution_Input272'] = float(x['ActivityContribution_Input248']) + float(x['ActivityContribution_Input254']) + float(x['ActivityContribution_Input248']) + float(x['ActivityContribution_Input266'])
        x['ActivityContribution_Input273'] = float(x['ActivityContribution_Input249']) + float(x['ActivityContribution_Input255']) + float(x['ActivityContribution_Input249']) + float(x['ActivityContribution_Input267'])
        x['ActivityContribution_Input274'] = float(x['ActivityContribution_Input250']) + float(x['ActivityContribution_Input256']) + float(x['ActivityContribution_Input262']) + float(x['ActivityContribution_Input268'])

        #Financial Expenses Y2:
        #input = 651
        #i = 627
        #j = 633
        #k = 639
        #l = 645

        #while input in range(650, 655) and i in range(626, 631) and j in range(632, 637) and k in range(638, 643) \
            #and l in range(694, 649):

            #x['ActivityContribution_Input' + str(input)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) \
                #+ float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])

        #input += 1
        #i += 1
        #j += 1
        #k += 1
        #l += 1

        x['ActivityContribution_Input651'] = float(x['ActivityContribution_Input627']) + float(x['ActivityContribution_Input633']) + float(x['ActivityContribution_Input639']) + float(x['ActivityContribution_Input645'])
        x['ActivityContribution_Input652'] = float(x['ActivityContribution_Input628']) + float(x['ActivityContribution_Input634']) + float(x['ActivityContribution_Input640']) + float(x['ActivityContribution_Input646'])
        x['ActivityContribution_Input653'] = float(x['ActivityContribution_Input629']) + float(x['ActivityContribution_Input635']) + float(x['ActivityContribution_Input641']) + float(x['ActivityContribution_Input647'])
        x['ActivityContribution_Input654'] = float(x['ActivityContribution_Input630']) + float(x['ActivityContribution_Input636']) + float(x['ActivityContribution_Input642']) + float(x['ActivityContribution_Input648'])

        #Financial Expenses Y3:
        #input = 940
        #i = 916
        #j = 922
        #k = 928
        #l = 934

        #while input in range(939, 942) and i in range(915, 920) and j in range(921, 926) and k in range(927, 932) \
            #and l in range(933, 938):

            #x['ActivityContribution_Input' + str(input)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) \
                #+ float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])

        #input += 1
        #i += 1
        #j += 1
        #k += 1
        #l += 1  

        x['ActivityContribution_Input940'] = float(x['ActivityContribution_Input916']) + float(x['ActivityContribution_Input922']) + float(x['ActivityContribution_Input928']) + float(x['ActivityContribution_Input934'])
        x['ActivityContribution_Input941'] = float(x['ActivityContribution_Input917']) + float(x['ActivityContribution_Input923']) + float(x['ActivityContribution_Input929']) + float(x['ActivityContribution_Input935'])
        x['ActivityContribution_Input942'] = float(x['ActivityContribution_Input918']) + float(x['ActivityContribution_Input924']) + float(x['ActivityContribution_Input930']) + float(x['ActivityContribution_Input936'])
        x['ActivityContribution_Input943'] = float(x['ActivityContribution_Input919']) + float(x['ActivityContribution_Input925']) + float(x['ActivityContribution_Input931']) + float(x['ActivityContribution_Input937'])        

        #Financial Expenses Y4:
        #input = 1233
        #i = 1209
        #j = 1215
        #k = 1221
        #l = 1227

        #while input in range(1232, 1237) and i in range(1208, 1211) and j in range(1214, 1219) and k in range(1220, 1225) \
            #and l in range(1226, 1231):

            #x['ActivityContribution_Input' + str(input)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) \
                #+ float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])

        #input += 1
        #i += 1
        #j += 1
        #k += 1
        #l += 1 

        x['ActivityContribution_Input1233'] = float(x['ActivityContribution_Input1209']) + float(x['ActivityContribution_Input1215']) + float(x['ActivityContribution_Input1221']) + float(x['ActivityContribution_Input1227'])
        x['ActivityContribution_Input1234'] = float(x['ActivityContribution_Input1210']) + float(x['ActivityContribution_Input1216']) + float(x['ActivityContribution_Input1222']) + float(x['ActivityContribution_Input1228'])
        x['ActivityContribution_Input1235'] = float(x['ActivityContribution_Input1211']) + float(x['ActivityContribution_Input1217']) + float(x['ActivityContribution_Input1223']) + float(x['ActivityContribution_Input1229'])
        x['ActivityContribution_Input1236'] = float(x['ActivityContribution_Input1212']) + float(x['ActivityContribution_Input1218']) + float(x['ActivityContribution_Input1224']) + float(x['ActivityContribution_Input1230'])          

        #Financial Expenses Y5:
        #input = 1509
        #i = 1485
        #j = 1491
        #k = 1497
        #l = 1503

        #while input in range(1508, 1513) and i in range(1484, 1489) and j in range(1490, 1495) and k in range(1496, 1501) \
            #and l in range(1502, 1507):

            #x['ActivityContribution_Input' + str(input)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) \
                #+ float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])

        #input += 1
        #i += 1
        #j += 1
        #k += 1
        #l += 1 

        x['ActivityContribution_Input1509'] = float(x['ActivityContribution_Input1485']) + float(x['ActivityContribution_Input1491']) + float(x['ActivityContribution_Input1497']) + float(x['ActivityContribution_Input1503'])
        x['ActivityContribution_Input1510'] = float(x['ActivityContribution_Input1486']) + float(x['ActivityContribution_Input1492']) + float(x['ActivityContribution_Input1498']) + float(x['ActivityContribution_Input1504'])
        x['ActivityContribution_Input1511'] = float(x['ActivityContribution_Input1487']) + float(x['ActivityContribution_Input1493']) + float(x['ActivityContribution_Input1499']) + float(x['ActivityContribution_Input1505'])
        x['ActivityContribution_Input1512'] = float(x['ActivityContribution_Input1488']) + float(x['ActivityContribution_Input1494']) + float(x['ActivityContribution_Input1500']) + float(x['ActivityContribution_Input1506'])                       

        # Financial Income
        x['ActivityContribution_Input280'] = float(fin['FinancialExp_Input213'])
        x['ActivityContribution_Input660'] = float(fin['FinancialExp_Input215']) 

        x['ActivityContribution_Input952'] = float(fin['FinancialExp_Input217']) 
        x['ActivityContribution_Input1242'] = float(fin['FinancialExp_Input219'])
        x['ActivityContribution_Input1518'] = float(fin['FinancialExp_Input221'])

        # Profit before tax & ex-ord income/loss:
        x['ActivityContribution_Input283'] = round(float(x['ActivityContribution_Input241']) + float(x['ActivityContribution_Input271']) + float(x['ActivityContribution_Input277']) ,3)
        x['ActivityContribution_Input284'] = round(float(x['ActivityContribution_Input242']) + float(x['ActivityContribution_Input272']) + float(x['ActivityContribution_Input278']) ,3)
        x['ActivityContribution_Input285'] = round(float(x['ActivityContribution_Input243']) + float(x['ActivityContribution_Input273']) + float(x['ActivityContribution_Input279']) ,3)
        x['ActivityContribution_Input286'] = round(float(x['ActivityContribution_Input244']) + float(x['ActivityContribution_Input274']) + float(x['ActivityContribution_Input280']) ,3)

        x['ActivityContribution_Input663'] = round(float(x['ActivityContribution_Input621']) + float(x['ActivityContribution_Input651']) + float(x['ActivityContribution_Input657']) ,3)
        x['ActivityContribution_Input664'] = round(float(x['ActivityContribution_Input622']) + float(x['ActivityContribution_Input652']) + float(x['ActivityContribution_Input658']) ,3)
        x['ActivityContribution_Input665'] = round(float(x['ActivityContribution_Input623']) + float(x['ActivityContribution_Input653']) + float(x['ActivityContribution_Input659']) ,3)
        x['ActivityContribution_Input666'] = round(float(x['ActivityContribution_Input624']) + float(x['ActivityContribution_Input654']) + float(x['ActivityContribution_Input660']) ,3)

        x['ActivityContribution_Input955'] = round(float(x['ActivityContribution_Input910']) + float(x['ActivityContribution_Input940']) + float(x['ActivityContribution_Input949']) ,3)
        x['ActivityContribution_Input956'] = round(float(x['ActivityContribution_Input911']) + float(x['ActivityContribution_Input941']) + float(x['ActivityContribution_Input950']) ,3)
        x['ActivityContribution_Input957'] = round(float(x['ActivityContribution_Input912']) + float(x['ActivityContribution_Input942']) + float(x['ActivityContribution_Input951']) ,3)
        x['ActivityContribution_Input958'] = round(float(x['ActivityContribution_Input913']) + float(x['ActivityContribution_Input943']) + float(x['ActivityContribution_Input952']) ,3)

        x['ActivityContribution_Input1245'] = round(float(x['ActivityContribution_Input1203']) + float(x['ActivityContribution_Input1233']) + float(x['ActivityContribution_Input1239']) ,3)
        x['ActivityContribution_Input1246'] = round(float(x['ActivityContribution_Input1204']) + float(x['ActivityContribution_Input1234']) + float(x['ActivityContribution_Input1240']) ,3)
        x['ActivityContribution_Input1247'] = round(float(x['ActivityContribution_Input1205']) + float(x['ActivityContribution_Input1235']) + float(x['ActivityContribution_Input1241']) ,3)
        x['ActivityContribution_Input1248'] = round(float(x['ActivityContribution_Input1206']) + float(x['ActivityContribution_Input1236']) + float(x['ActivityContribution_Input1242']) ,3)

        x['ActivityContribution_Input1521'] = round(float(x['ActivityContribution_Input1479']) + float(x['ActivityContribution_Input1509']) + float(x['ActivityContribution_Input1515']) ,3)
        x['ActivityContribution_Input1522'] = round(float(x['ActivityContribution_Input1480']) + float(x['ActivityContribution_Input1510']) + float(x['ActivityContribution_Input1516']) ,3)
        x['ActivityContribution_Input1523'] = round(float(x['ActivityContribution_Input1481']) + float(x['ActivityContribution_Input1511']) + float(x['ActivityContribution_Input1517']) ,3)
        x['ActivityContribution_Input1524'] = round(float(x['ActivityContribution_Input1482']) + float(x['ActivityContribution_Input1512']) + float(x['ActivityContribution_Input1518']) ,3)

        x['ActivityContribution_Input113'] = round(float(x['ActivityContribution_Input109']) + float(x['ActivityContribution_Input110']) + float(x['ActivityContribution_Input111'])  + float(x['ActivityContribution_Input112']),3) + 1              
        x['ActivityContribution_Input114'] = round(float(x['ActivityContribution_Input113']),3)

        #All total:
        #i = 109
        #j = 110
        #k = 111
        #l = 112
        #m = 113
        #n = 114

        #while i in range(108, 284) and j in range(109, 285) and k in range(110, 286) and l in range(111, 287) and m in range(112, 288) and n in range(113, 289):
            #x['ActivityContribution_Input' + str(m)] = float(x['ActivityContribution_Input' + str(i)]) + float(x['ActivityContribution_Input' + str(j)]) + float(x['ActivityContribution_Input' + str(k)]) + float(x['ActivityContribution_Input' + str(l)])
            #x['ActivityContribution_Input' + str(n)] = float(x['ActivityContribution_Input' + str(m)])
            #i += 6
            #j += 6
            #k += 6
            #l += 6
            #m += 6
            #n += 6 
            

        i = 125
        j = 126

        k = 121
        l = 122
        m = 123
        n = 124

        while i in range(124, 288) and j in range(125, 289) and k in range(120, 284) \
            and l in range(121, 285) and m in range(122, 286) and n in range(123, 287):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6 

        i = 305
        j = 306

        k = 301
        l = 302
        m = 303
        n = 304

        while i in range(304, 330) and j in range(305, 331) and k in range(300, 326) \
            and l in range(301, 327) and m in range(302, 328) and n in range(303, 329):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6  


        i = 341
        j = 342

        k = 337
        l = 338
        m = 339
        n = 340


        while i in range(340, 372) and j in range(341, 373) and k in range(336, 368) \
            and l in range(337, 369) and m in range(338, 370) and n in range(339, 371):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6  

        i = 383
        j = 384

        k = 379
        l = 380
        m = 381
        n = 382


        while i in range(382, 402) and j in range(383, 403) and k in range(378, 398) \
            and l in range(379, 399) and m in range(380, 400) and n in range(381, 401):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6  



        i = 503
        j = 504

        k = 499
        l = 500
        m = 501
        n = 502


        while i in range(502, 612) and j in range(503, 613) and k in range(498, 608) \
            and l in range(499, 609) and m in range(500, 610) and n in range(501, 611):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6  



        i = 619
        j = 620

        k = 615
        l = 616
        m = 617
        n = 618


        while i in range(618, 668) and j in range(619, 669) and k in range(614, 664) \
            and l in range(615, 665) and m in range(616, 666) and n in range(617, 667):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6 


        i = 685
        j = 686

        k = 681
        l = 682
        m = 683
        n = 684


        while i in range(684, 698) and j in range(685, 699) and k in range(680, 694) \
            and l in range(681, 695) and m in range(682, 696) and n in range(683, 697):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6

        i = 1194
        j = 1195

        k = 1190
        l = 1191
        m = 1192
        n = 1193


        while i in range(1193, 1201) and j in range(1194, 1202) and k in range(1189, 1197) \
            and l in range(1190, 1198) and m in range(1191, 1199) and n in range(1192, 1200):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6 

        i = 1213
        j = 1214


        x['ActivityContribution_Input1207'] = float(x['ActivityContribution_Input1203']) \
            + float(x['ActivityContribution_Input1204']) + float(x['ActivityContribution_Input1205']) \
                 + float(x['ActivityContribution_Input1206'])       

        x['ActivityContribution_Input1208'] = float(x['ActivityContribution_Input1207'])

        k = 1209
        l = 1210
        m = 1211
        n = 1212


        while i in range(1212, 1250) and j in range(1213, 1251) and k in range(1208, 1246) \
            and l in range(1209, 1247) and m in range(1210, 1248) and n in range(1211, 1249):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6                         


        i = 704
        j = 705

        k = 700
        l = 701
        m = 702
        n = 703


        while i in range(703, 711) and j in range(704, 712) and k in range(669, 707) \
            and l in range(700, 708) and m in range(701, 709) and n in range(702, 710):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6   


        i = 728
        j = 729

        k = 724
        l = 725
        m = 726
        n = 727


        while i in range(727, 783) and j in range(728, 784) and k in range(723, 779) \
            and l in range(724, 780) and m in range(725, 781) and n in range(726, 782):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6   


        i = 794
        j = 795

        k = 790
        l = 791
        m = 792
        n = 793


        while i in range(793, 945) and j in range(794, 946) and k in range(789, 941) \
            and l in range(790, 942) and m in range(791, 943) and n in range(792, 944):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6 


        i = 953
        j = 954

        k = 949
        l = 950
        m = 951
        n = 952


        while i in range(952, 960) and j in range(954, 961) and k in range(948, 956) \
            and l in range(949, 957) and m in range(950, 958) and n in range(951, 959):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6  

        i = 977
        j = 978

        k = 973
        l = 974
        m = 975
        n = 976


        while i in range(976, 1002) and j in range(977, 1003) and k in range(972, 998) \
            and l in range(973, 999) and m in range(974, 1000) and n in range(975, 1001):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6                                                           


        i = 1019
        j = 1020

        k = 1015
        l = 1016
        m = 1017
        n = 1018


        while i in range(1018, 1074) and j in range(1019, 1075) and k in range(1014, 1070) \
            and l in range(1015, 1071) and m in range(1016, 1072) and n in range(1017, 1073):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6

        i = 1085
        j = 1086

        k = 1081
        l = 1082
        m = 1083
        n = 1084


        while i in range(1084, 1188) and j in range(1085, 1189) and k in range(1080, 1184) \
            and l in range(1081, 1185) and m in range(1082, 1186) and n in range(1083, 1187):

            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)]),3)
                  
            x['ActivityContribution_Input' + str(j)] = round(float(x['ActivityContribution_Input' + str(i)]),3)

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6            


        # Y5:

        i = 1255
        j = 1256

        k = 1251
        l = 1252
        m = 1253
        n = 1254


        while i in range(1254, 1280) and j in range(1255, 1281) and k in range(1250, 1276) \
            and l in range(1251, 1277) and m in range(1252, 1278) and n in range(1253, 1279):

            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)]),3)
                  
            x['ActivityContribution_Input' + str(j)] = round(float(x['ActivityContribution_Input' + str(i)]),3)

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6   


        i = 1297
        j = 1298

        k = 1293
        l = 1294
        m = 1295
        n = 1296


        while i in range(1296, 1352) and j in range(1297, 1353) and k in range(1292, 1348) \
            and l in range(1293, 1349) and m in range(1294, 1350) and n in range(1295, 1351):

            x['ActivityContribution_Input' + str(i)] = round(float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)]),3)
                  
            x['ActivityContribution_Input' + str(j)] = round(float(x['ActivityContribution_Input' + str(i)]),3)

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6                                                                      

        i = 1363
        j = 1364

        k = 1359
        l = 1360
        m = 1361
        n = 1362


        while i in range(1362, 1526) and j in range(1363, 1527) and k in range(1292, 1522) \
            and l in range(1293, 1523) and m in range(1294, 1524) and n in range(1295, 1525):

            x['ActivityContribution_Input' + str(i)] = float(x['ActivityContribution_Input' + str(k)]) \
                + float(x['ActivityContribution_Input' + str(l)]) + float(x['ActivityContribution_Input' + str(m)]) \
                    + float(x['ActivityContribution_Input' + str(n)])
                  
            x['ActivityContribution_Input' + str(j)] = float(x['ActivityContribution_Input' + str(i)])

            i += 6
            j += 6
            k += 6
            l += 6
            m += 6
            n += 6   


        x['ActivityContribution_Input661'] = 0
        x['ActivityContribution_Input661'] = 0


        current_db.activitycontribution.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.activitycontribution.find_one({"GlobalId": "global"})

    
    return redirect(url_for('activitycontribution.activitycontribution')) 
    return render_template("activity-contribution.html", data=x)



####################################################################################

@activitycontribution_bp.route('/activitycontribution/delet', methods=['GET', 'POST'])
@login_required
def activitycontribution_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()    
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'   
        x= current_db.activitycontribution.delete_many({})
    return redirect(url_for('activitycontribution.activitycontribution')) 
    return render_template("activity-contribution.html", data=x)