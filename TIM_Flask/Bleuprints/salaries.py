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


salaries_bp = Blueprint('salaries', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["salaries"]

@salaries_bp.route('/salaries', methods=['GET', 'POST'])
@login_required
def salaries():
    """
    Create new collection in the database
    """   
    current_db = get_current_db() 
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i <495):
        lst.append(("Salaries_Input" + str(i)))
        i += 1


    ref = current_db.company.find_one({"GlobalId": "global"})

    x["Salaries_Header1"] = (int(ref["basic_year"])) 
    x["Salaries_Header2"] = (int(ref["basic_year"]) + 1 )
    x["Salaries_Header3"] = (int(ref["basic_year"]) + 2 )
    x["Salaries_Header4"] = (int(ref["basic_year"]) + 3 )
    x["Salaries_Header5"] = (int(ref["basic_year"]) + 4 ) 

    for entry in lst:
        x[entry] = 0 
    x["Salaries_Input495"] = 0
    x["Salaries_Input496"] = 0
    x["Salaries_Input497"] = 0
    x["Salaries_Input498"] = 0
    x["Salaries_Input499"] = 0  

    x["Salaries_Input13130"] = 0
    x["Salaries_Input13131"] = 0
    x["Salaries_Input13132"] = 0
    x["Salaries_Input13133"] = 0
    x["Salaries_Input13134"] = 0   

    x["Salaries_Input13135"] = 0
    x["Salaries_Input13136"] = 0
    x["Salaries_Input13137"] = 0
    x["Salaries_Input13138"] = 0
    x["Salaries_Input13139"] = 0
    x["Salaries_Input13140"] = 0                        
                                  

    current_db.salaries.insert_one(x)
    x = current_db.salaries.find_one({"GlobalId": "global"})
    return render_template("salaries-wages.html", data=x)                           


####################################################################################

@salaries_bp.route('/salaries/update', methods=['POST'])
@login_required
def salaries_update():
    """
    Update a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":

        ref = current_db.company.find_one({"GlobalId": "global"})

        x["Salaries_Header1"] = (int(ref["basic_year"])) 
        x["Salaries_Header2"] = (int(ref["basic_year"]) + 1 )
        x["Salaries_Header3"] = (int(ref["basic_year"]) + 2 )
        x["Salaries_Header4"] = (int(ref["basic_year"]) + 3 )
        x["Salaries_Header5"] = (int(ref["basic_year"]) + 4 ) 

        x = get_form_to_dict(request.form)

        # 1.1 Dealer principal
        x ['Salaries_Input3'] = x ['Salaries_Input4'] = x ['Salaries_Input5'] = x ['Salaries_Input6'] = round(float(x["Salaries_Input2"])) 

        # 1.2 Controller
        x ['Salaries_Input8'] = x ['Salaries_Input9'] = x ['Salaries_Input10'] = x ['Salaries_Input11'] = round(float(x["Salaries_Input7"]))   

        # 1.3 General & administration
        x ['Salaries_Input13'] = x ['Salaries_Input14'] = x ['Salaries_Input15'] = x ['Salaries_Input16'] = round(float(x["Salaries_Input12"]))  

        # 1.4 After sales manager
        x ['Salaries_Input18'] = x ['Salaries_Input19'] = x ['Salaries_Input20'] = x ['Salaries_Input21'] = round(float(x["Salaries_Input17"]))  
        
        # Calculation 1.7 Sales administration & other
        data = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        x ['Salaries_Input32'] =  float(data["TurnoverVehicle_Input131"])  
        x ['Salaries_Input33'] =  float(data["TurnoverVehicle_Input132"]) 
        x ['Salaries_Input34'] =  float(data["TurnoverVehicle_Input133"])       
        x ['Salaries_Input35'] =  float(data["TurnoverVehicle_Input134"]) 
        x ['Salaries_Input36'] =  float(data["TurnoverVehicle_Input135"])              
        #x ['Salaries_Input33'] = x ['Salaries_Input34'] = x ['Salaries_Input35'] = x ['Salaries_Input36'] = round(float(x["Salaries_Input32"]),3)  


       # Calculation 1.5 Sales Manager 
        data = current_db.turnovervehicle.find_one({"GlobalId": "global"})

        Sales_Manager = 22
        Vehicles = 136

        while Sales_Manager in range (21, 27) and Vehicles in range (135, 141):         
            x["Salaries_Input" + str(Sales_Manager)] = round(float(data["TurnoverVehicle_Input" + str(Vehicles)]))
            Sales_Manager +=  1
            Vehicles +=  1                                                  
        
        # Calculation 1.6 Salesmen Manager  ('Re calculate')
        data = current_db.turnovervehicle.find_one({"GlobalId": "global"})

        Salesmen_manager = 27
        Total_Number_Vehicle = 141
        Sales_Manager = 22
        Sales_Administration = 32

        while Salesmen_manager in range (26, 32) and Total_Number_Vehicle in range (140, 146) and Sales_Manager in range (21, 27) and Sales_Administration in range (31, 37):
            x["Salaries_Input" + str(Salesmen_manager)] = round(float(data["TurnoverVehicle_Input" + str(Total_Number_Vehicle)]) - float(x["Salaries_Input" + str(Sales_Manager)]) - float(x["Salaries_Input" + str(Sales_Administration)]))
            Salesmen_manager +=  1
            Total_Number_Vehicle +=  1
            Sales_Manager +=  1
            Sales_Administration +=  1

        # Calculation 1.8 Mechanics DAF      
        data = current_db.turnoverservices.find_one({"GlobalId": "global"})
        Mechanics_DAF_Salaries = 37
        Mechanics_DAF_Services = 130

        while Mechanics_DAF_Salaries in range(36, 42) and Mechanics_DAF_Services in range(129, 136):
            x["Salaries_Input" + str(Mechanics_DAF_Salaries)] = round(float(data["TurnoverServices_Input" + str(Mechanics_DAF_Services)]))
            Mechanics_DAF_Salaries +=  1
            Mechanics_DAF_Services +=  1   


        # Calculation 1.10 Workshop administration & other      
        data = current_db.turnoverservices.find_one({"GlobalId": "global"})
        Workshop_Administration_Salaries = 52
        Workshop_Administration_Services = 140

        while Workshop_Administration_Salaries in range(51, 57) and Workshop_Administration_Services in range(139, 145):
            x["Salaries_Input" + str(Workshop_Administration_Salaries)] = round(float(data["TurnoverServices_Input" + str(Workshop_Administration_Services)]))
            Workshop_Administration_Salaries +=  1
            Workshop_Administration_Services +=  1    

        # Calculation 1.11 Workshop managers      
        data = current_db.turnoverservices.find_one({"GlobalId": "global"})
        Workshop_Managers_Salaries = 57
        Workshop_Managers_Services = 135

        while Workshop_Managers_Salaries in range(56, 62) and Workshop_Managers_Services in range(134, 140):
            x["Salaries_Input" + str(Workshop_Managers_Salaries)] = round(float(data["TurnoverServices_Input" + str(Workshop_Managers_Services)]))
            Workshop_Managers_Salaries +=  1
            Workshop_Managers_Services +=  1  


        # Calculation 1.12 Warehouse clerks      
        data = current_db.turnoverpart.find_one({"GlobalId": "global"})
        Warehouse_Clerks_Salaries = 62
        Warehouse_Clerks_Parts = 109

        while Warehouse_Clerks_Salaries in range(61, 67) and Warehouse_Clerks_Parts in range(108, 114):
            x["Salaries_Input" + str(Warehouse_Clerks_Salaries)] = round(float(data["TurnoverParts_Input" + str(Warehouse_Clerks_Parts)]))
            Warehouse_Clerks_Salaries +=  1
            Warehouse_Clerks_Parts +=  1   


        # Calculation 1.13 Warehouse administration & other     
        data = current_db.turnoverpart.find_one({"GlobalId": "global"})
        Warehouse_Administration_Salaries = 67
        Warehouse_Administration_Parts = 114

        while Warehouse_Administration_Salaries in range(66, 72) and Warehouse_Administration_Parts in range(113, 119):
            x["Salaries_Input" + str(Warehouse_Administration_Salaries)] = round(float(data["TurnoverParts_Input" + str(Warehouse_Administration_Parts)]))
            Warehouse_Administration_Salaries+=  1
            Warehouse_Administration_Parts +=  1    

        # Calculation 1.14 Parts sales manager     
        data = current_db.turnoverpart.find_one({"GlobalId": "global"})
        Parts_sales_manager_Salaries = 72
        Parts_sales_manager_Parts = 119

        while Parts_sales_manager_Salaries in range(71, 77) and Parts_sales_manager_Parts in range(118, 124):
            x["Salaries_Input" + str(Parts_sales_manager_Salaries)] = round(float(data["TurnoverParts_Input" + str(Parts_sales_manager_Parts)]))
            Parts_sales_manager_Salaries +=  1
            Parts_sales_manager_Parts +=  1                                     


        # Calculation 1.15 Parts manager   
        data = current_db.turnoverpart.find_one({"GlobalId": "global"})
        Parts_manager_Salaries = 77
        Parts_managers_Parts = 124

        while Parts_manager_Salaries in range(76, 82) and Parts_managers_Parts in range(123, 139):
            x["Salaries_Input" + str(Parts_manager_Salaries)] = round(float(data["TurnoverParts_Input" + str(Parts_managers_Parts)]))
            Parts_manager_Salaries +=  1
            Parts_managers_Parts +=  1  



        #Total 1:
        x ['Salaries_Input82'] =  round(float(x['Salaries_Input2'])+ float(x['Salaries_Input7']) + float(x['Salaries_Input12']) + float(x['Salaries_Input17']) + float(x['Salaries_Input22']) + float(x['Salaries_Input32'])+ float(x['Salaries_Input27']) + float(x['Salaries_Input37'])+ float(x['Salaries_Input52'])+ float(x['Salaries_Input57'])+ float(x['Salaries_Input62'])+ float(x['Salaries_Input67'])+ float(x['Salaries_Input72']) + float(x['Salaries_Input77']))
        x ['Salaries_Input83'] =  round(float(x['Salaries_Input3'])+ float(x['Salaries_Input8']) + float(x['Salaries_Input13']) + float(x['Salaries_Input18']) + float(x['Salaries_Input23']) + float(x['Salaries_Input33'])+ float(x['Salaries_Input28']) + float(x['Salaries_Input38'])+ float(x['Salaries_Input53'])+ float(x['Salaries_Input58'])+ float(x['Salaries_Input63'])+ float(x['Salaries_Input68'])+ float(x['Salaries_Input73']) + float(x['Salaries_Input78']))
        x ['Salaries_Input84'] =  round(float(x['Salaries_Input4'])+ float(x['Salaries_Input9']) + float(x['Salaries_Input14']) + float(x['Salaries_Input19']) + float(x['Salaries_Input24']) + float(x['Salaries_Input34'])+ float(x['Salaries_Input29']) + float(x['Salaries_Input39'])+ float(x['Salaries_Input54'])+ float(x['Salaries_Input59'])+ float(x['Salaries_Input64'])+ float(x['Salaries_Input69'])+ float(x['Salaries_Input74']) + float(x['Salaries_Input79']))
        x ['Salaries_Input85'] =  round(float(x['Salaries_Input5'])+ float(x['Salaries_Input10']) + float(x['Salaries_Input15']) + float(x['Salaries_Input20']) + float(x['Salaries_Input25']) + float(x['Salaries_Input35'])+ float(x['Salaries_Input30']) + float(x['Salaries_Input40'])+ float(x['Salaries_Input55'])+ float(x['Salaries_Input60'])+ float(x['Salaries_Input65'])+ float(x['Salaries_Input70'])+ float(x['Salaries_Input75']) + float(x['Salaries_Input80']))
        x ['Salaries_Input86'] =  round(float(x['Salaries_Input6'])+ float(x['Salaries_Input11']) + float(x['Salaries_Input16']) + float(x['Salaries_Input21']) + float(x['Salaries_Input26']) + float(x['Salaries_Input36'])+ float(x['Salaries_Input31']) + float(x['Salaries_Input41'])+ float(x['Salaries_Input56'])+ float(x['Salaries_Input61'])+ float(x['Salaries_Input66'])+ float(x['Salaries_Input71'])+ float(x['Salaries_Input76']) + float(x['Salaries_Input81']))







 
        #####################    1. Average gross salary     #####################        

       #  2.1. Dealer principal

        Average_Gross_Year = 93
        Average_Gross_Previous = 92
        Yearly_Indexation = 87


        while Average_Gross_Year in range (92, 97) and Average_Gross_Previous in range (91, 96) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous +=  1
            Yearly_Indexation +=  1


       #  2.2. Controller

        Average_Gross_Year = 120
        Average_Gross_Previous = 119
        Yearly_Indexation = 87


        while Average_Gross_Year in range (119, 124) and Average_Gross_Previous in range (118, 123) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ))
            Average_Gross_Year +=  1
            Average_Gross_Previous +=  1
            Yearly_Indexation +=  1


       #  2.3. General & administration
      
        Average_Gross_Year = 148
        Average_Gross_Previous = 147
        Yearly_Indexation = 87


        while Average_Gross_Year in range (147, 152) and Average_Gross_Previous in range (146, 151) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1


       #  2.4. After sales managern

        Average_Gross_Year = 174
        Average_Gross_Previous = 173
        Yearly_Indexation = 87


        while Average_Gross_Year in range (173, 178) and Average_Gross_Previous in range (172, 177) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ))
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1


       #  2.5. Sales manager

        Average_Gross_Year = 200
        Average_Gross_Previous = 199
        Yearly_Indexation = 87


        while Average_Gross_Year in range (199, 204) and Average_Gross_Previous in range (198, 203) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1  






       #  2.6. Salesmen_fixed

        Average_Gross_Year = 13131
        Average_Gross_Previous = 13130
        Yearly_Indexation = 87


        while Average_Gross_Year in range (13130, 13135) and Average_Gross_Previous in range (13129, 13134) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1 

       #  2.6. Salesmen_variable
        data = current_db.turnovervehicle.find_one({"GlobalId": "global"})
        dealer = current_db.dealerarea.find_one({"GlobalId": "global"})       

        #Decision_of_num = 126
        #Dealer_area_1 = 68
        #Dealer_area_2 = 123
        #input = 13136

        #while input in range(13135, 13142) and Decision_of_num in range (125, 130) and Dealer_area_1 in range (67, 77) and Dealer_area_2 in range (122, 132):
            #if float(data["TurnoverVehicle_Input" + str(Decision_of_num)]) == 0:
                #x["Salaries_Input" + str(input)] = 0
            #else:
                #x["Salaries_Input" + str(input)] = (float(dealer["DealeArea_Input" + str(Dealer_area_1)]) + float(dealer["DealeArea_Input" + str(Dealer_area_2)])) / (float(data["TurnoverVehicle_Input" + str(Decision_of_num)])) * float(x["Salaries_Input257"])

        #Decision_of_num += 1
        #Dealer_area_1 += 2
        #Dealer_area_2 += 2
        #input += 1

        if float(data["TurnoverVehicle_Input126"]) == 0:
            x["Salaries_Input13136"] = 0
        else:
            x["Salaries_Input13136"] = round((float(dealer["DealeArea_Input68"]) + float(dealer["DealeArea_Input123"])) / (float(data["TurnoverVehicle_Input126"])) * float(x["Salaries_Input13135"]),3)


        if float(data["TurnoverVehicle_Input127"]) == 0:
            x["Salaries_Input13137"] = 0
        else:
            x["Salaries_Input13137"] = round((float(dealer["DealeArea_Input70"]) + float(dealer["DealeArea_Input125"])) / (float(data["TurnoverVehicle_Input127"])) * float(x["Salaries_Input13135"]),3)


        if float(data["TurnoverVehicle_Input128"]) == 0:
            x["Salaries_Input13138"] = 0
        else:
            x["Salaries_Input13138"] = round((float(dealer["DealeArea_Input72"]) + float(dealer["DealeArea_Input127"])) / (float(data["TurnoverVehicle_Input128"])) * float(x["Salaries_Input13135"]),3)


        if float(data["TurnoverVehicle_Input129"]) == 0:
            x["Salaries_Input13139"] = 0
        else:
            x["Salaries_Input13139"] = round((float(dealer["DealeArea_Input74"]) + float(dealer["DealeArea_Input129"])) / (float(data["TurnoverVehicle_Input129"])) * float(x["Salaries_Input13135"]),3)


        if float(data["TurnoverVehicle_Input130"]) == 0:
            x["Salaries_Input13140"] = 0
        else:
            x["Salaries_Input13140"] = round((float(dealer["DealeArea_Input76"]) + float(dealer["DealeArea_Input131"])) / (float(data["TurnoverVehicle_Input129"])) * float(x["Salaries_Input13135"]))                                                                                               

       # 2.6 Salesmen_all:
        #fixed = 13130
        #variable = 13136
        #input_all = 226

        #while fixed in range(13129, 13135) and variable in range (13135, 131342) and input_all in range (225, 231):
            #x["Salaries_Input" + str(input_all)] = float(x["Salaries_Input" + str(fixed)]) + float(x["Salaries_Input" + str(variable)])

        #fixed += 1
        #variable += 1
        #input_all += 1 

        x["Salaries_Input226"] = round(float(x["Salaries_Input13130"]) + float(x["Salaries_Input13136"]),3)
        x["Salaries_Input227"] = round(float(x["Salaries_Input13131"]) + float(x["Salaries_Input13137"]),3)
        x["Salaries_Input228"] = round(float(x["Salaries_Input13132"]) + float(x["Salaries_Input13138"]),3)               
        x["Salaries_Input229"] = round(float(x["Salaries_Input13133"]) + float(x["Salaries_Input13139"]),3)
        x["Salaries_Input230"] = round(float(x["Salaries_Input13134"]) + float(x["Salaries_Input13140"]),3)         

       
       #  2.7. Sales administration & other

        Average_Gross_Year = 253
        Average_Gross_Previous = 252
        Yearly_Indexation = 87


        while Average_Gross_Year in range (252, 257) and Average_Gross_Previous in range (251, 256) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1                                            


       #  2.8. Mechanics DAF

        Average_Gross_Year = 279
        Average_Gross_Previous = 278
        Yearly_Indexation = 87


        while Average_Gross_Year in range (278, 465) and Average_Gross_Previous in range (277, 464) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1 

       #  2.10. Workshop administration & other

        Average_Gross_Year = 331
        Average_Gross_Previous = 330
        Yearly_Indexation = 87


        while Average_Gross_Year in range (330, 335) and Average_Gross_Previous in range (329, 334) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1 


       #  2.11. Workshop managers

        Average_Gross_Year = 357
        Average_Gross_Previous = 356
        Yearly_Indexation = 87


        while Average_Gross_Year in range (356, 361) and Average_Gross_Previous in range (355, 360) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1 

       #  2.12. Warehouse clerks

        Average_Gross_Year = 383
        Average_Gross_Previous = 382
        Yearly_Indexation = 87


        while Average_Gross_Year in range (382, 387) and Average_Gross_Previous in range (381, 386) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1  


       #  2.13. Warehouse administration & other

        Average_Gross_Year = 409
        Average_Gross_Previous = 408
        Yearly_Indexation = 87


        while Average_Gross_Year in range (408, 413) and Average_Gross_Previous in range (407, 412) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1  


       #  2.14. Parts sales manager

        Average_Gross_Year = 435
        Average_Gross_Previous = 434
        Yearly_Indexation = 87


        while Average_Gross_Year in range (434, 439) and Average_Gross_Previous in range (433, 438) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1      


       #  2.15. Parts manager

        Average_Gross_Year = 461
        Average_Gross_Previous = 460
        Yearly_Indexation = 87


        while Average_Gross_Year in range (460, 465) and Average_Gross_Previous in range (459, 464) and Yearly_Indexation in range (86, 91):
            x["Salaries_Input" + str(Average_Gross_Year)] = round(float(x["Salaries_Input" + str(Average_Gross_Previous)]) * ( 1 + float(x["Salaries_Input" + str(Yearly_Indexation)]) / 100 ),3)
            Average_Gross_Year +=  1
            Average_Gross_Previous += 1
            Yearly_Indexation +=  1                                             



        #####################    2. Social security and taxes employer     #####################  
    
       #  2.1. Dealer principal

        Social_Security = 99
        Average_Gross_Year = 92

        while Social_Security in range (98, 104) and Average_Gross_Year in range (91, 97):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100, 3)
            Social_Security +=  1
            Average_Gross_Year += 1


        #input = 99
        #i = 98
        #j = 92

        #while input in range(98, 104) and j in range(91, 97):
            #x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            #input += 1
            #j += 1 

       #  2.2. Controller

        Social_Security = 125
        Average_Gross_Year = 119

        while Social_Security in range (124, 130) and Average_Gross_Year in range (118, 124):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 125
        i = 124
        j = 119

        while input in range(124, 130) and j in range(118, 124):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)))
            input += 1
            j += 1  


       #  2.3. General & administration 
             
        Social_Security = 154
        Average_Gross_Year = 147

        while Social_Security in range (153, 159) and Average_Gross_Year in range (146, 152):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100,3)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 154
        i = 153
        j = 147

        while input in range(153, 159) and j in range(146, 152):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1              


       #  2.4. After sales manager 
             
        Social_Security = 179
        Average_Gross_Year = 173

        while Social_Security in range (178, 184) and Average_Gross_Year in range (172, 178):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 179
        i = 178
        j = 173

        while input in range(178, 184) and j in range(172, 178):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)))
            input += 1
            j += 1              


       #  2.5. Sales manager
        Social_Security = 205
        Average_Gross_Year = 199

        while Social_Security in range (204, 211) and Average_Gross_Year in range (198, 204):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 205
        i = 204
        j = 199

        while input in range(204, 211) and j in range(198, 204):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1              

       #  2.6. Salesmen
        Social_Security = 232
        Average_Gross_Year = 226 

        while Social_Security in range (231, 237) and Average_Gross_Year in range (225, 231):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 232
        i = 231
        j = 226

        while input in range(231, 237) and j in range(225, 231):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1              

       #  2.7. Sales administration & other              
        Social_Security = 258
        Average_Gross_Year = 252

        while Social_Security in range (257, 263) and Average_Gross_Year in range (251, 257):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100, 3)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 258
        i = 257
        j = 252

        while input in range(257, 263) and j in range(251, 257):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1  


       #  2.8. Mechanics DAF              
        Social_Security = 284
        Average_Gross_Year = 278

        while Social_Security in range (283, 289) and Average_Gross_Year in range (277, 283):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1   


        input = 284
        i = 283
        j = 278

        while input in range(283, 289) and j in range(277, 283):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1              


       #  2.10. Workshop administration & other            
        Social_Security = 336
        Average_Gross_Year = 330

        while Social_Security in range (335, 341) and Average_Gross_Year in range (329, 335):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 

        input = 336
        i = 335
        j = 330

        while input in range(335, 341) and j in range(329, 335):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1

       #  2.11. Workshop managers             
        Social_Security = 362
        Average_Gross_Year = 356

        while Social_Security in range (361, 367) and Average_Gross_Year in range (354, 361):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100,3)
            Social_Security +=  1
            Average_Gross_Year += 1 


        input = 362
        i = 361
        j = 356

        while input in range(361, 367) and j in range(354, 361):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1          


       #  2.12. Warehouse clerks             
        Social_Security = 388
        Average_Gross_Year = 382

        while Social_Security in range (387, 393) and Average_Gross_Year in range (381, 387):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 

        input = 388
        i = 387
        j = 382

        while input in range(387, 393) and j in range(381, 387):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1            


       #  2.13. Warehouse administration & other           
        Social_Security = 414
        Average_Gross_Year = 408

        while Social_Security in range (413, 419) and Average_Gross_Year in range (407, 413):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 

        input = 414
        i = 413
        j = 408

        while input in range(413, 419) and j in range(407, 413):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1                


        #  2.14. Parts sales manager            
        Social_Security = 440
        Average_Gross_Year = 434

        while Social_Security in range (439, 445) and Average_Gross_Year in range (433, 439):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 

        input = 440
        i = 439
        j = 434

        while input in range(439, 445) and j in range(433, 439):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1             
            

       #  2.15. Parts manager             
        Social_Security = 466
        Average_Gross_Year = 460

        while Social_Security in range (465, 471) and Average_Gross_Year in range (459, 465):
            x["Salaries_Input" + str(Social_Security)] = round((float(x["Salaries_Input" + str(Average_Gross_Year)]) * float(x["Salaries_Input97"])) / 100)
            Social_Security +=  1
            Average_Gross_Year += 1 

                                                                                             
        input = 466
        i = 465
        j = 460

        while input in range(465, 471) and j in range(459, 465):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(j)]) * (float(x["Salaries_Input" + str(i)])/100)),3)
            input += 1
            j += 1  

        #####################    Total cost1     #####################  

       #  2.1. Dealer principal

        total = 104
        Average_Gross_Salary = 92
        Social_Security = 99

        while total in range (103, 109) and Average_Gross_Salary in range (91, 97) and Social_Security in range (98, 104):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1   


       #  2.2. Controller

        total = 130
        Average_Gross_Salary = 119
        Social_Security = 125

        while total in range (129, 135) and Average_Gross_Salary in range (118, 124) and Social_Security in range (124, 130):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1 


       #  2.3. General & administration

        total = 495
        Average_Gross_Salary = 147
        Social_Security = 154

        while total in range (494, 500) and Average_Gross_Salary in range (146, 152) and Social_Security in range (153, 159):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1 



       #  2.4. After sales manager 

        total = 184
        Average_Gross_Salary = 173
        Social_Security = 179

        while total in range (183, 189) and Average_Gross_Salary in range (172, 178) and Social_Security in range (178, 184):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]))
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1           

       #  2.5. Sales manager

        total = 211
        Average_Gross_Salary = 199
        Social_Security = 205

        while total in range (210, 216) and Average_Gross_Salary in range (198, 204) and Social_Security in range (204, 210):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1    



       #  2.6. Salesmen

        total = 237
        Average_Gross_Salary = 226
        Social_Security = 232

        while total in range (236, 243) and Average_Gross_Salary in range (225, 231) and Social_Security in range (231, 237):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1      


       #  2.7. Sales administration & other

        total = 263
        Average_Gross_Salary = 252
        Social_Security = 258

        while total in range (262, 268) and Average_Gross_Salary in range (251, 257) and Social_Security in range (257, 263):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1   


       #  2.8. Mechanics DAF

        total = 289
        Average_Gross_Salary = 278
        Social_Security = 284

        while total in range (288, 294) and Average_Gross_Salary in range (277, 283) and Social_Security in range (283, 289):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1 

       #  2.10. Workshop administration & other

        total = 341
        Average_Gross_Salary = 330
        Social_Security = 336

        while total in range (340, 346) and Average_Gross_Salary in range (329, 335) and Social_Security in range (335, 341):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1 

       #  2.11. Workshop managers

        total = 367
        Average_Gross_Salary = 356
        Social_Security = 362

        while total in range (366, 372) and Average_Gross_Salary in range (355, 361) and Social_Security in range (361, 367):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1             

       #  2.12. Warehouse clerks

        total = 393
        Average_Gross_Salary = 382
        Social_Security = 388

        while total in range (392, 398) and Average_Gross_Salary in range (381, 387) and Social_Security in range (387, 393):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1   

       #  2.13. Warehouse administration & other

        total = 419
        Average_Gross_Salary = 408
        Social_Security = 414

        while total in range (418, 424) and Average_Gross_Salary in range (407, 413) and Social_Security in range (413, 419):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1      

       #  2.14. Parts sales manager

        total = 445
        Average_Gross_Salary = 434
        Social_Security = 440

        while total in range (444, 450) and Average_Gross_Salary in range (433, 439) and Social_Security in range (439, 445):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1   

        #  2.15. Parts managerParts manager

        total = 471
        Average_Gross_Salary = 460
        Social_Security = 466

        while total in range (470, 476) and Average_Gross_Salary in range (459, 465) and Social_Security in range (465, 471):
            x["Salaries_Input" + str(total)] = round(float(x["Salaries_Input" + str(Average_Gross_Salary)]) + float(x["Salaries_Input" + str(Social_Security)]),3)
            Social_Security +=  1
            Average_Gross_Salary += 1 
            total +=  1               



        #####################    Number    #####################  


       #  2.1. Dealer principal        
        Dealer_Principal_1 = 109
        Dealer_Principal_2 = 2

        while Dealer_Principal_1 in range (108, 114) and Dealer_Principal_2 in range (1, 7):
            x["Salaries_Input" + str(Dealer_Principal_1)] = round(float(x["Salaries_Input" + str(Dealer_Principal_2)]))
            Dealer_Principal_1 += 1              
            Dealer_Principal_2 += 1 



       #  2.2. Controller
        Controller_1 = 135
        controller_2 = 7


        while Controller_1 in range (134, 140) and controller_2 in range (6, 12):
            x["Salaries_Input" + str(Controller_1)] = round(float(x["Salaries_Input" + str(controller_2)]))
            Controller_1 +=  1              
            controller_2 += 1



       #  2.3. General & administration 
        General_Administration_1 = 163
        General_Administration_2 = 12


        while General_Administration_1 in range (162, 168) and General_Administration_2 in range (11, 17):
            x["Salaries_Input" + str(General_Administration_1)] = round(float(x["Salaries_Input" + str(General_Administration_2)]))
            General_Administration_1 +=  1              
            General_Administration_2 += 1 



       #  2.4. After sales manager 
        After_Sales_Manager_1 = 189
        After_Sales_Manager_2 = 17

        while After_Sales_Manager_1 in range (188, 194) and After_Sales_Manager_2 in range (16, 22):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1 


       #  2.5. Sales manager 
        After_Sales_Manager_1 = 216
        After_Sales_Manager_2 = 22

        while After_Sales_Manager_1 in range (215, 221) and After_Sales_Manager_2 in range (21, 27):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1   

        input = 221
        i = 211
        j = 216
        k = 489

        while input in range (220, 226) and i in range (210, 216) and j in range(215, 221):
            x["Salaries_Input" + str(input)] = round((float(x["Salaries_Input" + str(i)]) * float(x["Salaries_Input" + str(j)])) * (float(x["Salaries_Input" + str(k)]) / 100 ))
            input +=  1
            i += 1
            j +=  1              


       #  2.6. Salesmen
        After_Sales_Manager_1 = 242
        After_Sales_Manager_2 = 27

        while After_Sales_Manager_1 in range (241, 247) and After_Sales_Manager_2 in range (26, 32):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1  


       #  2.7. Sales administration & other
        After_Sales_Manager_1 = 268
        After_Sales_Manager_2 = 32

        while After_Sales_Manager_1 in range (267, 273) and After_Sales_Manager_2 in range (31, 37):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1   

       #  2.8. Mechanics DAF
        After_Sales_Manager_1 = 294
        After_Sales_Manager_2 = 37

        while After_Sales_Manager_1 in range (293, 299) and After_Sales_Manager_2 in range (36, 42):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1 

       #  2.10. Workshop administration & other
        After_Sales_Manager_1 = 346
        After_Sales_Manager_2 = 52

        while After_Sales_Manager_1 in range (345, 351) and After_Sales_Manager_2 in range (51, 57):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1    

       #  2.11. 
        After_Sales_Manager_1 = 372
        After_Sales_Manager_2 = 57

        while After_Sales_Manager_1 in range (371, 377) and After_Sales_Manager_2 in range (56, 62):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1  

       #  2.12. Warehouse clerks
        After_Sales_Manager_1 = 398
        After_Sales_Manager_2 = 62

        while After_Sales_Manager_1 in range (397, 403) and After_Sales_Manager_2 in range (61, 67):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1  

       #  2.13. Warehouse administration & other
        After_Sales_Manager_1 = 424
        After_Sales_Manager_2 = 67

        while After_Sales_Manager_1 in range (423, 429) and After_Sales_Manager_2 in range (66, 82):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1  


       #  2.14. Parts sales manager
        After_Sales_Manager_1 = 450
        After_Sales_Manager_2 = 72

        while After_Sales_Manager_1 in range (449, 455) and After_Sales_Manager_2 in range (71, 77):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1  


        #  2.15. Parts managerParts manager
        After_Sales_Manager_1 = 476
        After_Sales_Manager_2 = 77

        while After_Sales_Manager_1 in range (475, 481) and After_Sales_Manager_2 in range (76, 82):
            x["Salaries_Input" + str(After_Sales_Manager_1)] = round(float(x["Salaries_Input" + str(After_Sales_Manager_2)]))
            After_Sales_Manager_1 +=  1              
            After_Sales_Manager_2 += 1                          






        #####################    Total cost2    #####################  

       #  2.1. Dealer principal

        Result_Dealer_Principal = 114
        Total_Cost_Dealer_Principal = 109        
        Number_Dealer_Principal = 104


        while Result_Dealer_Principal in range (113, 119) and Total_Cost_Dealer_Principal in range (108, 114) and Number_Dealer_Principal in range (103, 109):
            x['Salaries_Input' + str(Result_Dealer_Principal)] = round(float(x['Salaries_Input' + str(Total_Cost_Dealer_Principal)]) * float(x['Salaries_Input' + str(Number_Dealer_Principal)]) * (float(x["Salaries_Input489"])/100),3)
            Result_Dealer_Principal += 1
            Total_Cost_Dealer_Principal += 1       
            Number_Dealer_Principal += 1



       #  2.2. Controller

        Result_Controller = 140
        Total_Cost_Controller = 135       
        Number_Controller = 130


        while Result_Controller in range (139, 145) and Total_Cost_Controller in range (134, 140) and Number_Controller in range (129, 135):
            x['Salaries_Input' + str(Result_Controller)] = round(float(x['Salaries_Input' + str(Total_Cost_Controller)]) * float(x['Salaries_Input' + str(Number_Controller)]) * (float(x["Salaries_Input489"])/100),3)
            Result_Controller += 1
            Total_Cost_Controller += 1       
            Number_Controller += 1


       #  2.3. General & administration

        Result_General_Administration = 168
        Total_General_Administration = 495       
        Number_General_Administration = 163


        while Result_General_Administration in range (167, 173) and Total_General_Administration in range (494, 500) and Number_General_Administration in range (162, 168):
            x['Salaries_Input' + str(Result_General_Administration)] = round(float(x['Salaries_Input' + str(Total_General_Administration)]) * float(x['Salaries_Input' + str(Number_General_Administration)]) * (float(x["Salaries_Input489"])/100),3)
            Result_General_Administration += 1
            Total_General_Administration += 1       
            Number_General_Administration += 1


       #  2.4. After sales manager 

        Result_Sales_Manager = 194
        Total_Sales_Manager = 189       
        Number_Sales_Manager = 184


        while Result_Sales_Manager in range (193, 199) and Total_Sales_Manager in range (188, 194) and Number_Sales_Manager in range (183, 189):
            x['Salaries_Input' + str(Result_Sales_Manager)] = round(float(x['Salaries_Input' + str(Total_Sales_Manager)]) * float(x['Salaries_Input' + str(Number_Sales_Manager)]) * (float(x["Salaries_Input489"])/100),3)
            Result_Sales_Manager += 1
            Total_Sales_Manager += 1       
            Number_Sales_Manager += 1


       #  2.5. Sales manager 
       
        Result = 221
        Total = 211       
        Number = 216


        while Result in range (220, 226) and Total in range (210, 216) and Number in range (215, 221):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1

       #  2.6. Salesmen

        Result = 247
        Total = 237       
        Number = 242


        while Result in range (246, 252) and Total in range (236, 242) and Number in range (241, 247):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1  

       #  2.7. Sales administration & other

        Result = 273
        Total = 263       
        Number = 268


        while Result in range (272, 278) and Total in range (262, 268) and Number in range (267, 273):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1   


       #  2.8. Mechanics DAF

        Result = 299
        Total = 289       
        Number = 294


        while Result in range (298, 304) and Total in range (288, 294) and Number in range (293, 300):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1   



       #  2.10. Workshop administration & other

        Result = 351
        Total = 341       
        Number = 346


        while Result in range (350, 356) and Total in range (340, 346) and Number in range (345, 351):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1    



       #  2.11. Workshop managers

        Result = 377
        Total = 367       
        Number = 372


        while Result in range (376, 382) and Total in range (366, 372) and Number in range (371, 377):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1    



       #  2.12. Warehouse clerks 

        Result = 403
        Total = 393       
        Number = 398


        while Result in range (402, 408) and Total in range (392, 398) and Number in range (397, 403):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1     



       #  2.13. Warehouse administration & other

        Result = 429
        Total = 419       
        Number = 424


        while Result in range (428, 434) and Total in range (418, 424) and Number in range (423, 429):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1 



       #  2.14. Parts sales manager 

        Result = 455
        Total = 445       
        Number = 450


        while Result in range (454, 460) and Total in range (445, 451) and Number in range (449, 455):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1                                                                                       



        #  2.15. Parts managerParts manager

        Result = 481
        Total = 471       
        Number = 476


        while Result in range (480, 486) and Total in range (470, 476) and Number in range (475, 481):
            x['Salaries_Input' + str(Result)] = round(float(x['Salaries_Input' + str(Total)]) * float(x['Salaries_Input' + str(Number)]) * (float(x["Salaries_Input489"])/100),3)
            Result += 1
            Total += 1       
            Number += 1             


        #Total 2:
        x ['Salaries_Input490'] =  round(float(x['Salaries_Input114'])+ float(x['Salaries_Input140']) + float(x['Salaries_Input168']) + float(x['Salaries_Input194']) + float(x['Salaries_Input221']) + float(x['Salaries_Input247'])+ float(x['Salaries_Input273']) + float(x['Salaries_Input299'])+ float(x['Salaries_Input351'])+ float(x['Salaries_Input377'])+ float(x['Salaries_Input403'])+ float(x['Salaries_Input429'])+ float(x['Salaries_Input455']) + float(x['Salaries_Input481'])+1)
        x ['Salaries_Input491'] =  round(float(x['Salaries_Input115'])+ float(x['Salaries_Input141']) + float(x['Salaries_Input169']) + float(x['Salaries_Input195']) + float(x['Salaries_Input222']) + float(x['Salaries_Input248'])+ float(x['Salaries_Input274']) + float(x['Salaries_Input300'])+ float(x['Salaries_Input352'])+ float(x['Salaries_Input378'])+ float(x['Salaries_Input404'])+ float(x['Salaries_Input430'])+ float(x['Salaries_Input456']) + float(x['Salaries_Input482']))
        # Assuming x is a dictionary containing the keys 'Salaries_Input115', 'Salaries_Input141', and so on...

        salaries = [
            float(x['Salaries_Input115']), float(x['Salaries_Input141']), float(x['Salaries_Input169']),
            float(x['Salaries_Input195']), float(x['Salaries_Input222']), float(x['Salaries_Input248']),
            float(x['Salaries_Input274']), float(x['Salaries_Input300']), float(x['Salaries_Input352']),
            float(x['Salaries_Input378']), float(x['Salaries_Input404']), float(x['Salaries_Input430']),
            float(x['Salaries_Input456']), float(x['Salaries_Input482'])
        ]

        result = round(sum(salaries))

        # Print individual numbers and the result
        for salary in salaries:
            print(f"Number: {salary}")

        print(f"Result: {result}")

        x ['Salaries_Input490'] =  round(float(x['Salaries_Input114'])+ float(x['Salaries_Input140']) + float(x['Salaries_Input168']) + float(x['Salaries_Input194']) + float(x['Salaries_Input221']) + float(x['Salaries_Input247'])+ float(x['Salaries_Input273']) + float(x['Salaries_Input299'])+ float(x['Salaries_Input351'])+ float(x['Salaries_Input377'])+ float(x['Salaries_Input403'])+ float(x['Salaries_Input429'])+ float(x['Salaries_Input455']) + float(x['Salaries_Input481'])+ 1 )
        x ['Salaries_Input492'] =  round(float(x['Salaries_Input116'])+ float(x['Salaries_Input142']) + float(x['Salaries_Input170']) + float(x['Salaries_Input196']) + float(x['Salaries_Input223']) + float(x['Salaries_Input249'])+ float(x['Salaries_Input275']) + float(x['Salaries_Input301'])+ float(x['Salaries_Input353'])+ float(x['Salaries_Input379'])+ float(x['Salaries_Input405'])+ float(x['Salaries_Input431'])+ float(x['Salaries_Input457']) + float(x['Salaries_Input483']))
        x ['Salaries_Input493'] =  round(float(x['Salaries_Input117'])+ float(x['Salaries_Input143']) + float(x['Salaries_Input171']) + float(x['Salaries_Input197']) + float(x['Salaries_Input224']) + float(x['Salaries_Input250'])+ float(x['Salaries_Input276']) + float(x['Salaries_Input302'])+ float(x['Salaries_Input354'])+ float(x['Salaries_Input380'])+ float(x['Salaries_Input406'])+ float(x['Salaries_Input432'])+ float(x['Salaries_Input458']) + float(x['Salaries_Input484']))
        x ['Salaries_Input494'] =  round(float(x['Salaries_Input118'])+ float(x['Salaries_Input144']) + float(x['Salaries_Input172']) + float(x['Salaries_Input198']) + float(x['Salaries_Input225']) + float(x['Salaries_Input251'])+ float(x['Salaries_Input277']) + float(x['Salaries_Input303'])+ float(x['Salaries_Input355'])+ float(x['Salaries_Input381'])+ float(x['Salaries_Input407'])+ float(x['Salaries_Input433'])+ float(x['Salaries_Input459']) + float(x['Salaries_Input485']))


        current_db.salaries.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.salaries.find_one({"GlobalId": "global"})
    return redirect(url_for('salaries.salaries')) 
    return render_template("salaries-wages.html", data=x)



####################################################################################

@salaries_bp.route('/salaries/delete',  methods=['POST'])
@login_required
def salaries_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.salaries.delete_many({})
    return redirect(url_for('salaries.salaries'))    
    return render_template("salaries-wages.html", data=x)