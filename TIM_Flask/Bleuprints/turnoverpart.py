import imp
from flask import Blueprint, flash, g, redirect,\
                    render_template, request, session, url_for, jsonify
from pymongo import MongoClient
from services.mongodb_interactions import get_form_to_dict
from models.user import User
from Bleuprints.auth import login_required
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from Bleuprints.db_routes import db, client, get_current_db
load_dotenv()

turnoverpart_bp = Blueprint('turnover', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["turnoverpart"]

@turnoverpart_bp.route('/turnoverpart', methods=['GET', 'POST'])
@login_required
def turnoverpart():
    """
    Create a company in the database
    """
    current_db = get_current_db()
    print('turnoverpart current_db soumettre:', current_db)
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i <1000):
        lst.append(("TurnoverParts_Input" + str(i)))
        i += 1
    for entry in lst:
        x[entry] = 0
    x["TurnoverParts_Header250"] = 0
    ref = current_db.company.find_one({"GlobalId": "global"})

    x["TurnoverParts_Header1"] = (int(ref["basic_year"])) 
    x["TurnoverParts_Header2"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverParts_Header3"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverParts_Header4"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverParts_Header5"] = (int(ref["basic_year"]) + 4 ) 


    current_db.turnoverpart.insert_one(x)
    x = current_db.turnoverpart.find_one({"GlobalId": "global"})
    return render_template("turnover-parts.html", data=x)


####################################################################################



@turnoverpart_bp.route('/turnoverpart/update', methods=['POST'])
@login_required
def turnoverpart_update():
    """
    Update a company in the database
    """
    print("toggeled update")
    current_db = get_current_db()  



    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'

        
        vehicle_parc = current_db.vehicle.find_one({"GlobalId": "global"})
        calculation_short = current_db.calculationshorts.find_one({"GlobalId": "global"})
        cost_of_sales = current_db.costofsale.find_one({"GlobalId": "global"})
        Dealer_area = current_db.dealerarea.find_one({"GlobalId": "global"})
        Inv = current_db.invdepr.find_one({"GlobalId": "global"})  
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["TurnoverParts_Header1"] = (int(ref["basic_year"])) 
        x["TurnoverParts_Header2"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverParts_Header3"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverParts_Header4"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverParts_Header5"] = (int(ref["basic_year"]) + 4 )            

        # Vehicle Parc Standstill % (input in 5.1):
        x["TurnoverParts_Input2"] = float(vehicle_parc["VehicleParc_Input205"])


        #Potential based on parc Y1
        x["TurnoverParts_Input4"] =  round(float(calculation_short["CalculationShort_Input1646"]) / (1 -(float(cost_of_sales["CostOFSales_Input217"])/100)))
        print(calculation_short["CalculationShort_Input1646"])
        print((float(cost_of_sales["CostOFSales_Input217"])/100))
        #Potential based on parc Y1
        #x["TurnoverParts_Input5"] =  round(float(calculation_short["CalculationShort_Input1734"]) / (1 -(float(cost_of_sales["CostOFSales_Input218"])/100)) * (1+ (float(x["TurnoverParts_Input1"])/100)),3)
        #Potential based on parc Y2
        #x["TurnoverParts_Input6"] =  round(float(calculation_short["CalculationShort_Input1822"]) / (1 -(float(cost_of_sales["CostOFSales_Input220"])/100)) * pow((1+ (float(x["TurnoverParts_Input1"])/100)),2),3)
        #Potential based on parc Y3
        #x["TurnoverParts_Input7"] =  round(float(calculation_short["CalculationShort_Input1910"]) / (1 -(float(cost_of_sales["CostOFSales_Input222"])/100)) * pow((1+ (float(x["TurnoverParts_Input1"])/100)),3),3)
        #Potential based on parc Y4 
        #x["TurnoverParts_Input8"] =  round(float(calculation_short["CalculationShort_Input1998"]) / (1 -(float(cost_of_sales["CostOFSales_Input224"])/100)) * pow((1+ (float(x["TurnoverParts_Input1"])/100)),4),3)    

        #Parts retention DAF vehicles: =IF(C11=0,0,C16/C11)
        '''Potential_based_on_parc_1 = float(x["TurnoverParts_Input4"])           
        if (Potential_based_on_parc_1 != 0):
            x['TurnoverParts_Input15'] = round(((float(x['TurnoverParts_Input10'])) / Potential_based_on_parc_1),2)
        else:
            x['TurnoverParts_Input15'] = 0 '''

        #Parts turnover DAF: =IF(C16<>0,C16,C15*C11*$B$14)
        Parts_turnover_DAF = 20
        c_16 = 10
        Parts_retention_DAF_vehicles = 15
        Potential_based_on_parc = 4
        Scenario = x ["TurnoverParts_Input9"]

        while Parts_turnover_DAF in range(20, 25) and c_16 in range(9, 15) and Parts_retention_DAF_vehicles in range(14, 20) and Potential_based_on_parc in range(3,9):
            if (float(x["TurnoverParts_Input" + str(c_16)]) != 0):
                x ["TurnoverParts_Input" + str(Parts_turnover_DAF)] = round(float(x["TurnoverParts_Input" + str(c_16)]),3)
            else:
                x ["TurnoverParts_Input" + str(Parts_turnover_DAF)] =  round((float(x["TurnoverParts_Input" + str(Parts_retention_DAF_vehicles)]) /100 ) * float(x["TurnoverParts_Input" + str(Potential_based_on_parc)]) * (float(x ["TurnoverParts_Input9"])/100),3)

            Parts_turnover_DAF += 1
            c_16 += 1
            Parts_retention_DAF_vehicles += 1
            Potential_based_on_parc += 1

        #Oil_and_lubricants
        #x ["TurnoverParts_Input25"] = round(float(calculation_short["CalculationShort_Input2527"]) * (float(x["TurnoverParts_Input15"])/100) ,3)
        #x ["TurnoverParts_Input26"] = round(float(calculation_short["CalculationShort_Input2615"]) * (float(x["TurnoverParts_Input16"])/100) ,3)
        #x ["TurnoverParts_Input27"] = round(float(calculation_short["CalculationShort_Input2703"]) * (float(x["TurnoverParts_Input17"]/100) ,3)
        #x ["TurnoverParts_Input28"] = round(float(calculation_short["CalculationShort_Input2791"]) * (float(x["TurnoverParts_Input18"]/100) ,3)
        #x ["TurnoverParts_Input29"] = round(float(calculation_short["CalculationShort_Input2910"]) * (float(x["TurnoverParts_Input19"]/100) ,3)

        


        #Oil_and_lubricants ='Calculation (short)'!CJ14*C15
        #DAF_Oil_Total = 2527
        #Parts_retention_DAF_vehicles = 15
        #Oil_and_lubricants = 25

        #while DAF_Oil_Total in range (2526, 2792) and Parts_retention_DAF_vehicles in range(14, 19) and Oil_and_lubricants in range(24, 28):            
            #x ["TurnoverParts_Input" + str(Oil_and_lubricants)] = float(calculation_short["CalculationShort_Input" + str(DAF_Oil_Total)]) * float(x ["TurnoverParts_Input" + str(Parts_retention_DAF_vehicles)])

            #DAF_Oil_Total += 88
            #Parts_retention_DAF_vehicles += 1
            #Oil_and_lubricants += 1

        #x ["TurnoverParts_Input29"] = float(calculation_short["CalculationShort_Input2910"]) * float(x ["TurnoverParts_Input19"])

        #total =SUM(C17:C20)

        #i = 20
        #j = 25
        #k = 30
        
        #while i in range(19, 25) and j in range(24, 30) and k in range(29, 35):
            #x ["TurnoverParts_Input" + str(k)] = float(x["TurnoverParts_Input" + str(i)]) + float(x["TurnoverParts_Input" + str(j)])

        #i += 1
        #j += 1
        #k += 1  

        x ["TurnoverParts_Input30"] = round(float(x["TurnoverParts_Input25"]) + float(x["TurnoverParts_Input20"]) + float(x["TurnoverParts_Input400"]) + float(x["TurnoverParts_Input405"]))
        x ["TurnoverParts_Input31"] = round(float(x["TurnoverParts_Input26"]) + float(x["TurnoverParts_Input21"]) + float(x["TurnoverParts_Input401"]) + float(x["TurnoverParts_Input406"]))
        x ["TurnoverParts_Input32"] = round(float(x["TurnoverParts_Input27"]) + float(x["TurnoverParts_Input22"]) + float(x["TurnoverParts_Input402"]) + float(x["TurnoverParts_Input407"]))
        x ["TurnoverParts_Input33"] = round(float(x["TurnoverParts_Input28"]) + float(x["TurnoverParts_Input23"]) + float(x["TurnoverParts_Input403"]) + float(x["TurnoverParts_Input408"]))
        x ["TurnoverParts_Input34"] = round(float(x["TurnoverParts_Input29"]) + float(x["TurnoverParts_Input24"]) + float(x["TurnoverParts_Input404"]) + float(x["TurnoverParts_Input409"]) + 1)
    
     

    #Parts new trucks =$B26*('7.1 Dealer area'!C47+'7.1 Dealer area'!C41)

        Parts_new_trucks_3 = 36
        Dealer_Are_1 = 123
        Dealer_Are_2 = 68

        while Parts_new_trucks_3 in range(35, 41) and Dealer_Are_1 in range(122, 132) and Dealer_Are_2 in range(67, 77):
            x["TurnoverParts_Input" + str(Parts_new_trucks_3)] = round(float(x["TurnoverParts_Input35"]) * (float(Dealer_area["DealeArea_Input" + str(Dealer_Are_1)]) + float(Dealer_area["DealeArea_Input" + str(Dealer_Are_2)])))

            Parts_new_trucks_3 += 1
            Dealer_Are_1 += 2
            Dealer_Are_2 += 2


    # 2.2 Preparation new and used trucks (internal invoiced parts as part of the total invoiced parts) (Used)

        x["TurnoverParts_Input410"] = round(float(x["TurnoverParts_Input520"]) * float(vehicle_parc["VehicleParc_Input224"])) 
        x["TurnoverParts_Input411"] = round(float(x["TurnoverParts_Input520"]) * float(vehicle_parc["VehicleParc_Input225"])) 
        x["TurnoverParts_Input412"] = round(float(x["TurnoverParts_Input520"]) * float(vehicle_parc["VehicleParc_Input226"]) )                              
        x["TurnoverParts_Input413"] = round(float(x["TurnoverParts_Input520"]) * float(vehicle_parc["VehicleParc_Input227"]) ) 
        x["TurnoverParts_Input414"] = round(float(x["TurnoverParts_Input520"]) * float(vehicle_parc["VehicleParc_Input228"]) )  

    #Error: =IF(C26>C16,"ERROR"," ")
        if float(x["TurnoverParts_Input36"]) > float(x["TurnoverParts_Input10"]):
            x["TurnoverParts_Input_error_1"] = 'Error'
        else: 
            x["TurnoverParts_Input_error_1"] = ' '


        x["TurnoverParts_Input41"] = round(float(x["TurnoverParts_Input36"]) + float(x["TurnoverParts_Input410"]))
        x["TurnoverParts_Input42"] = round(float(x["TurnoverParts_Input37"]) + float(x["TurnoverParts_Input411"]))
        x["TurnoverParts_Input43"] = round(float(x["TurnoverParts_Input38"]) + float(x["TurnoverParts_Input412"]))
        x["TurnoverParts_Input44"] = round(float(x["TurnoverParts_Input39"]) + float(x["TurnoverParts_Input413"]) )         
        x["TurnoverParts_Input45"] = round(float(x["TurnoverParts_Input40"]) + float(x["TurnoverParts_Input414"]) )

    #Workshop DAF vehicles: =C33*C17

        x["TurnoverParts_Input56"] = round((float(x["TurnoverParts_Input46"])/100) * float(x["TurnoverParts_Input20"])) 
        x["TurnoverParts_Input57"] = round((float(x["TurnoverParts_Input47"])/100) * float(x["TurnoverParts_Input21"]))
        x["TurnoverParts_Input58"] = round((float(x["TurnoverParts_Input48"])/100) * float(x["TurnoverParts_Input22"]))                                     
        x["TurnoverParts_Input59"] = round((float(x["TurnoverParts_Input49"])/100) * float(x["TurnoverParts_Input23"]))
        x["TurnoverParts_Input60"] = round((float(x["TurnoverParts_Input50"])/100) * float(x["TurnoverParts_Input24"]))

    #Workshop DAF others:

        x["TurnoverParts_Input420"] = round((float(x["TurnoverParts_Input415"])/100) * float(x["TurnoverParts_Input400"])) 
        x["TurnoverParts_Input421"] = round((float(x["TurnoverParts_Input416"])/100) * float(x["TurnoverParts_Input401"])) 
        x["TurnoverParts_Input422"] = round((float(x["TurnoverParts_Input417"])/100) * float(x["TurnoverParts_Input402"]))                                 
        x["TurnoverParts_Input423"] = round((float(x["TurnoverParts_Input418"])/100) * float(x["TurnoverParts_Input403"]))
        x["TurnoverParts_Input424"] = round((float(x["TurnoverParts_Input419"])/100) * float(x["TurnoverParts_Input404"]))

    
    
    

    #total

        #x["TurnoverParts_Input66"] = float(x["TurnoverParts_Input56"]) 
        #x["TurnoverParts_Input67"] = float(x["TurnoverParts_Input57"]) 
        #x["TurnoverParts_Input68"] = float(x["TurnoverParts_Input58"])                                        
        #x["TurnoverParts_Input69"] = float(x["TurnoverParts_Input59"])  
        #x["TurnoverParts_Input70"] = float(x["TurnoverParts_Input60"])

        i = 66
        j = 56
        k = 420

        while i in range( 65, 71) and j in range(55, 61) and k in range(419, 425):
            x["TurnoverParts_Input" + str(i)] = round(float(x["TurnoverParts_Input" + str(j)]))  +    round(float(x["TurnoverParts_Input" + str(k)]))            
            i += 1
            j += 1
            k += 1
  
    # Counter DAF vehicles to spokes =(1-C33)*C40*C16*$B$14
        i = 46
        j = 71
        k = 10
        l = 76

        while i in range(45, 51) and j in range(70, 76) and k in range(9, 15) and l in range(75, 81):
            Round = round((1 - (float(x["TurnoverParts_Input" + str(i)])/100)) * (float(x["TurnoverParts_Input" + str(j)])/100) * float(x["TurnoverParts_Input" + str(k)]) *  (float(x["TurnoverParts_Input9"])/100))
            x["TurnoverParts_Input" + str(l)] = Round             
            i += 1
            j += 1
            k += 1
            l += 1   

    # Counter DAF vehicles to others =(1-C33)*(1-C40)*C17
        i = 46
        j = 71
        k = 20
        l = 81

        while i in range(45, 51) and j in range(70, 76) and k in range(19, 25) and l in range(80, 86):
            Round = round((1 - (float(x["TurnoverParts_Input" + str(i)])/100)) * (1 - (float(x["TurnoverParts_Input" + str(j)])/100)) * float(x["TurnoverParts_Input" + str(k)]))
            x["TurnoverParts_Input" + str(l)] = Round            
            i += 1
            j += 1
            k += 1
            l += 1 


    # 
        i = 415
        j = 400

        l = 425

        while i in range(414, 420) and j in range(399, 405) and l in range(424, 430):
            Round = round((1 - (float(x["TurnoverParts_Input" + str(i)])/100)) * (float(x["TurnoverParts_Input" + str(j)])))
            x["TurnoverParts_Input" + str(l)] = Round            
            i += 1
            j += 1
            l += 1 


    # Total counter =SUM(C41:C43) 
        i = 76
        j = 81
        k = 91
        l = 425


        while i in range(75, 81) and j in range(80, 86) and k in range(90, 96) and l in range(424, 430):
            x["TurnoverParts_Input" + str(k)] = round(float(x["TurnoverParts_Input" + str(i)]) + float(x["TurnoverParts_Input" + str(j)])  + float(x["TurnoverParts_Input" + str(l)]))         
            i += 1
            j += 1
            k += 1
            l += 1

    #Required number of parts personnel =IF(C49=0,0,C21/C49)
        #i = 96
        #j = 30
        #k = 101                                
        #while i in range(95, 101) and j in range(29, 36) and k in range(100, 107):
            #if  float(x["TurnoverParts_Input" + str(i)]) is 0:                
                #x["TurnoverParts_Input" + str(k)] = 0
            #else:
                #x["TurnoverParts_Input" + str(k)] = float(x["TurnoverParts_Input" + str(j)]) / float(x["TurnoverParts_Input" + str(k)])
            #i += 1
            #j += 1
            #k += 1
            
        if float(x["TurnoverParts_Input96"]) == 0:
            x["TurnoverParts_Input101"] = 0
        else:
            x["TurnoverParts_Input101"] = round(float(x["TurnoverParts_Input30"]) / float(x["TurnoverParts_Input96"]),2)


        if float(x["TurnoverParts_Input97"]) == 0:
            x["TurnoverParts_Input102"] = 0
        else:
            x["TurnoverParts_Input102"] = round(float(x["TurnoverParts_Input31"]) / float(x["TurnoverParts_Input97"]),2) 


        if float(x["TurnoverParts_Input98"]) == 0:
            x["TurnoverParts_Input103"] = 0
        else:
            x["TurnoverParts_Input103"] = round(float(x["TurnoverParts_Input32"]) / float(x["TurnoverParts_Input98"]),2)


        if float(x["TurnoverParts_Input99"]) == 0:
            x["TurnoverParts_Input105"] = 0
        else:
            x["TurnoverParts_Input105"] = round(float(x["TurnoverParts_Input33"]) / float(x["TurnoverParts_Input99"]),2)


        if float(x["TurnoverParts_Input100"]) == 0:
            x["TurnoverParts_Input106"] = 0
        else:
            x["TurnoverParts_Input106"] = round(float(x["TurnoverParts_Input34"]) / float(x["TurnoverParts_Input100"]),2)
           
    #Stock rotation months =IF(C63=0,0,12/C63)
        #i = 134 #C63
        #j = 139 #input                                
        #while i in range(133, 139) and j in range(138, 144):
            #if float(x["TurnoverParts_Input" + str(i)]) == 0:                
                #x["TurnoverParts_Input" + str(j)] = 0
            #else:
                #x["TurnoverParts_Input" + str(j)] = 12 / float(x["TurnoverParts_Input" + str(i)])
            #i += 1
            #j += 1

            if float(x["TurnoverParts_Input134"]) == 0:
                x["TurnoverParts_Input139"] = 0
            else:
                x["TurnoverParts_Input139"] = round(12 / float(x["TurnoverParts_Input134"]))


            if float(x["TurnoverParts_Input135"]) == 0:
                x["TurnoverParts_Input140"] = 0
            else:
                x["TurnoverParts_Input140"] = round(12 / float(x["TurnoverParts_Input135"])) 


            if float(x["TurnoverParts_Input136"]) == 0:
                x["TurnoverParts_Input141"] = 0
            else:
                x["TurnoverParts_Input141"] = round(12 / float(x["TurnoverParts_Input136"])) 

            if float(x["TurnoverParts_Input137"]) == 0:
                x["TurnoverParts_Input142"] = 0
            else:
                x["TurnoverParts_Input142"] = round(12 / float(x["TurnoverParts_Input137"])) 

            if float(x["TurnoverParts_Input138"]) == 0:
                x["TurnoverParts_Input143"] = 0
            else:
                x["TurnoverParts_Input143"] = round(12 / float(x["TurnoverParts_Input138"]))                                                                



    #Parts stock at sales price =IF(C63=0,0,C21/C63)
        i = 134 #C63
        k = 30
        j = 144 #input                                
        while i in range(133, 139) and j in range(144, 149) and k in range(23, 35):
            if float(x["TurnoverParts_Input" + str(i)]) == 0:                
                x["TurnoverParts_Input" + str(j)] = 0
            else:
                x["TurnoverParts_Input" + str(j)] = round(float(x["TurnoverParts_Input" + str(k)]) / float(x["TurnoverParts_Input" + str(i)]))
            i += 1
            k += 1
            j += 1


    #(+) Closing stock =IF('7.3 Cost of sales'!C85=0,0,
    # ('7.3 Cost of sales'!B76*'7.3 Cost of sales'!C76+
    # '7.3 Cost of sales'!B77*'7.3 Cost of sales'!C77+
    # '7.3 Cost of sales'!B78*'7.3 Cost of sales'!C78+
    # '7.3 Cost of sales'!B79*'7.3 Cost of sales'!C79+
    # '7.3 Cost of sales'!B80*'7.3 Cost of sales'!C80+
    # '7.3 Cost of sales'!B81*'7.3 Cost of sales'!C81+'
    # 7.3 Cost of sales'!B82*'7.3 Cost of sales'!C82+
    # '7.3 Cost of sales'!B83*'7.3 Cost of sales'!C83+
    # '7.3 Cost of sales'!B84*'7.3 Cost of sales'!C84)
    # /'7.3 Cost of sales'!C85+IF('7.3 Cost of sales'!C85=0,0))


    if float(cost_of_sales["CostOFSales_Input207"]) == 0:
        x["TurnoverParts_Input152"] = 0
    else:
        x["TurnoverParts_Input152"] = (
            (float(cost_of_sales["CostOFSales_Input156"]) * float(cost_of_sales["CostOFSales_Input157"])) +
            (float(cost_of_sales["CostOFSales_Input166"]) * float(cost_of_sales["CostOFSales_Input167"])) +
            (float(cost_of_sales["CostOFSales_Input176"]) * float(cost_of_sales["CostOFSales_Input177"])) +
            (float(cost_of_sales["CostOFSales_Input186"]) * float(cost_of_sales["CostOFSales_Input187"])) +
            (float(cost_of_sales["CostOFSales_Input196"]) * float(cost_of_sales["CostOFSales_Input197"]))
        ) / float(cost_of_sales["CostOFSales_Input207"])

        
        #(-) Initial stock =IF(B72=0,0,B72)
        if float(x['TurnoverParts_Input152']) is 0 :
            x['TurnoverParts_Input150'] = 0
        else:
            x['TurnoverParts_Input150'] = float(x['TurnoverParts_Input152'])



        # (+) =('7.2.2 Turnover Parts'!C65-'7.4.3 Inv. & Depr.'!D129)/(1+B72)
        #In_Depr = current_db.invdepr.find_one({"GlobalId": "global"})
        #x['TurnoverParts_Input158'] =  float(x['TurnoverParts_Input158']) -  float(In_Depr['InvDep_Input'])   

        #Total_parts_personnel = 129
        #Warehouse_clerks = 109
        #Administration = 114
        #parts_sales = 119
        #parts_manager = 124

        #while Total_parts_personnel in range(128, 134) and Warehouse_clerks in range(108, 114) and Administration in range(113, 119)\
            #and  parts_sales in range(118, 124) and parts_manager in range(123, 129):

            #x["TurnoverParts_Input" + str(Total_parts_personnel)] =  float(x["TurnoverParts_Input" + str(Warehouse_clerks)]) + float(x["TurnoverParts_Input" + str(Administration)])\
                #+ float(x["TurnoverParts_Input" + str(parts_sales)]) + float(x["TurnoverParts_Input" + str(parts_manager)])

        #Total_parts_personnel += 1
        #Warehouse_clerks += 1
        #Administration += 1
        #parts_sales += 1
        #parts_manager += 1 
        
        x['TurnoverParts_Input129'] = round(float(x['TurnoverParts_Input109']) + float(x['TurnoverParts_Input114']) + float(x['TurnoverParts_Input119']) + float(x['TurnoverParts_Input124']))
        x['TurnoverParts_Input130'] = round(float(x['TurnoverParts_Input110']) + float(x['TurnoverParts_Input115']) + float(x['TurnoverParts_Input120']) + float(x['TurnoverParts_Input125']))
        x['TurnoverParts_Input131'] = round(float(x['TurnoverParts_Input111']) + float(x['TurnoverParts_Input116']) + float(x['TurnoverParts_Input121']) + float(x['TurnoverParts_Input126']))
        x['TurnoverParts_Input132'] = round(float(x['TurnoverParts_Input112']) + float(x['TurnoverParts_Input117']) + float(x['TurnoverParts_Input122']) + float(x['TurnoverParts_Input127']))   
        x['TurnoverParts_Input133'] = round(float(x['TurnoverParts_Input113']) + float(x['TurnoverParts_Input118']) + float(x['TurnoverParts_Input123']) + float(x['TurnoverParts_Input128']))

            #(-) Initial stock:
        part_1 = (float(x['TurnoverParts_Input144']) - float(Inv['InvDep_Input302']))
        part_2 = (1 + (float(x['TurnoverParts_Input150']) / 100))
        x['TurnoverParts_Input154'] = round(((float(x['TurnoverParts_Input144']) - float(Inv['InvDep_Input302']))) / ((1 + (float(x['TurnoverParts_Input150']) / 100))),3)


        percentage = 27
        result = 1 + (percentage / 100)



        x['TurnoverParts_Input155'] = round((float(x['TurnoverParts_Input145']) - float(Inv['InvDep_Input303'])) / (1 + (float(x['TurnoverParts_Input150']) / 100)),3)
        x['TurnoverParts_Input156'] = round((float(x['TurnoverParts_Input146']) - float(Inv['InvDep_Input304'])) / (1 + (float(x['TurnoverParts_Input150']) / 100)),3)
        x['TurnoverParts_Input157'] = round((float(x['TurnoverParts_Input147']) - float(Inv['InvDep_Input305'])) / (1 + (float(x['TurnoverParts_Input150']) / 100)),3)


        #(+) Closing stock: 
        x['TurnoverParts_Input158'] = round((float(x['TurnoverParts_Input154'])))
        x['TurnoverParts_Input159'] = round((float(x['TurnoverParts_Input155'])))
        x['TurnoverParts_Input160'] = round((float(x['TurnoverParts_Input156'])))
        x['TurnoverParts_Input161'] = round((float(x['TurnoverParts_Input157'])))
        x['TurnoverParts_Input162'] = round(((float(x['TurnoverParts_Input148'])) - float(Inv['InvDep_Input306'])) / (1 + (float(x['TurnoverParts_Input150']) / 100)))

        #Change in stock
        i = 153
        j = 158
        k = 163

        while i in range(152, 158) and j in range(157, 163) and k in range(162, 168):

            x["TurnoverParts_Input" + str(k)] = round(float(x["TurnoverParts_Input" + str(j)]) - float(x["TurnoverParts_Input" + str(i)]))

            i += 1
            k += 1
            j += 1  


        x["TurnoverParts_Input167"] = round(float(x["TurnoverParts_Input162"]) - float(x["TurnoverParts_Input157"]) -1 )
        

        #Purchases
        #i = 153
        #j = 158
        #k = 257
        #l = 168

        #while i in range(152, 158) and j in range(157, 163) and k in range(256, 226) and l in range(167, 173):

            #x["TurnoverParts_Input" + str(l)] = float(x["TurnoverParts_Input" + str(i)]) + float(x["TurnoverParts_Input" + str(j)]) + float(cost_of_sales["CostOFSales_Input" + str(k)])

            #i += 1
            #j += 1
            #k += 2
            #l += 1

        x["TurnoverParts_Input168"] = round(float(x["TurnoverParts_Input158"]) - float(x["TurnoverParts_Input153"]) + float(cost_of_sales["CostOFSales_Input207"]))
        x["TurnoverParts_Input169"] = round(float(x["TurnoverParts_Input159"]) - float(x["TurnoverParts_Input154"]) + float(cost_of_sales["CostOFSales_Input209"]))
        x["TurnoverParts_Input170"] = round(float(x["TurnoverParts_Input160"]) - float(x["TurnoverParts_Input155"]) + float(cost_of_sales["CostOFSales_Input211"]))
        x["TurnoverParts_Input171"] = round(float(x["TurnoverParts_Input161"]) - float(x["TurnoverParts_Input156"]) + float(cost_of_sales["CostOFSales_Input213"]))                                      
        x["TurnoverParts_Input172"] = round(float(x["TurnoverParts_Input162"]) - float(x["TurnoverParts_Input157"]) + float(cost_of_sales["CostOFSales_Input215"]))        
     


    current_db.turnoverpart.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.turnoverpart.find_one({"GlobalId": "global"})
    return redirect(url_for('turnover.turnoverpart')) 





####################################################################################

@turnoverpart_bp.route('/turnoverpart/delete',  methods=['POST'])
@login_required
def turnoverpart_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()     
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.turnoverpart.delete_many({})
        return redirect(url_for('turnover.turnoverpart'))    
    return render_template("turnover-parts.html", data=x)