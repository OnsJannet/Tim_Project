#from curses import pair_content
from decimal import Rounded
import imp
from unittest import result
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

calculationshorts_bp = Blueprint('calculationshorts', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["calculationshorts"]

@calculationshorts_bp.route('/calculationshorts', methods=['GET', 'POST'])
@login_required
def calculationshorts():
    """
    Create a company in the database
    """
    current_db = get_current_db()  
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i <3142):
        lst.append(("CalculationShort_Input" + str(i)))
        i += 1

    for entry in lst:
        x[entry] = 0

    x["CalculationShort_Input13130"] = 0
    x["CalculationShort_Input13131"] = 0        
    x["CalculationShort_Input13132"] = 0
    x["CalculationShort_Input13133"] = 0
    x["CalculationShort_Input13134"] = 0
    x["CalculationShort_Input13135"] = 0        
    x["CalculationShort_Input13136"] = 0
    x["CalculationShort_Input13137"] = 0 
    x["CalculationShort_Input13138"] = 0 
    x["CalculationShort_Input13139"] = 0
    x["CalculationShort_Input13140"] = 0 
    
                     
                              

    current_db.calculationshorts.insert_one(x)
    x = current_db.calculationshorts.find_one({"GlobalId": "global"})
    return render_template("calculation-short.html", data=x)  

####################################################################################

@calculationshorts_bp.route('/calculationshorts/update', methods=['POST'])
@login_required
def calculationshorts_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        x['GlobalId'] = 'global'

        # Calculation park basic year: 
        data = current_db.dealerarea.find_one({"GlobalId": "global"})

        Park = 1
        Vehicles = 48
      
        while Park in range (0, 13) and Vehicles in range (47, 59):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10  

        Park = 23
        Vehicles = 83
      
        while Park in range (22, 46) and Vehicles in range (82, 104):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10


        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        x ['CalculationShort_Input67'] = float(data["DealeArea_Input113"])



        data = current_db.vehicle.find_one({"GlobalId": "global"})

        Park = 2
        Vehicles = 49        
                  
        while Park in range (1, 69) and Vehicles in range (48, 146):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16  


        data = current_db.vehicle.find_one({"GlobalId": "global"})

        Park = 3
        Vehicles = 50      
                  
        while Park in range (2, 70) and Vehicles in range (49, 147):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16  


        Park = 4
        Vehicles = 51     
                  
        while Park in range (3, 71) and Vehicles in range (50, 148):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16  


        Park = 5
        Vehicles = 52     
                  
        while Park in range (4, 72) and Vehicles in range (51, 149):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16   


        Park = 6
        Vehicles = 53    
                  
        while Park in range (5, 73) and Vehicles in range (52, 150):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16    


        Park = 7
        Vehicles = 54   
                  
        while Park in range (6, 74) and Vehicles in range (53, 151):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16  

        Park = 8
        Vehicles = 55   
                  
        while Park in range (7, 75) and Vehicles in range (54, 152):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16 

        Park = 9
        Vehicles = 56   
                  
        while Park in range (8, 76) and Vehicles in range (55, 153):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16  

        Park = 10
        Vehicles = 57   
                  
        while Park in range (9, 77) and Vehicles in range (56, 154):         
            x["CalculationShort_Input" + str(Park)] = float(data["VehicleParc_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 16 





                                ################################################

        data = current_db.dealerarea.find_one({"GlobalId": "global"})

        Park = 89
        Vehicles = 50
      
        while Park in range (88, 101) and Vehicles in range (49, 61):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10  

        Park = 111
        Vehicles = 85
      
        while Park in range (110, 134) and Vehicles in range (84, 106):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10


        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        x ['CalculationShort_Input155'] = float(data["DealeArea_Input115"])



        Park = 90
        Vehicles = 1      
                  
        while Park in range (89, 100) and Vehicles in range (0, 10):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 101
        Vehicles = 12      
                  
        while Park in range (100, 110) and Vehicles in range (11, 22):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1 


        Park = 112
        Vehicles = 23      
                  
        while Park in range (111, 121) and Vehicles in range (22, 33):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 123
        Vehicles = 34      
                  
        while Park in range (122, 132) and Vehicles in range (33, 44):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1   

        Park = 134
        Vehicles = 45      
                  
        while Park in range (133, 143) and Vehicles in range (44, 55):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1 


        Park = 145
        Vehicles = 56     
                  
        while Park in range (144, 154) and Vehicles in range (55, 66):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 156
        Vehicles = 67    
                  
        while Park in range (155, 165) and Vehicles in range (66, 77):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1    
            
                                ################################################


        data = current_db.dealerarea.find_one({"GlobalId": "global"})

        Park = 178
        Vehicles = 52
      
        while Park in range (177, 190) and Vehicles in range (51, 63):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10  

        Park = 200
        Vehicles = 87
      
        while Park in range (199, 223) and Vehicles in range (86, 108):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10


        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        x ['CalculationShort_Input244'] = float(data["DealeArea_Input117"])


        Park = 179
        Vehicles = 89      
                  
        while Park in range (178, 188) and Vehicles in range (88, 98):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


            
        Park = 190
        Vehicles = 100      
                  
        while Park in range (189, 199) and Vehicles in range (99, 109):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 201
        Vehicles = 111      
                  
        while Park in range (200, 210) and Vehicles in range (110, 120):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 212
        Vehicles = 122      
                  
        while Park in range (211, 221) and Vehicles in range (121, 131):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 223
        Vehicles = 133      
                  
        while Park in range (222, 232) and Vehicles in range (132, 142):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 234
        Vehicles = 144      
                  
        while Park in range (233, 243) and Vehicles in range (143, 153):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 245
        Vehicles = 155      
                  
        while Park in range (244, 254) and Vehicles in range (154, 164):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  

                                ################################################


        data = current_db.dealerarea.find_one({"GlobalId": "global"})

        Park = 255
        Vehicles = 54
      
        while Park in range (254, 267) and Vehicles in range (53, 65):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10  

        Park = 277
        Vehicles = 89
      
        while Park in range (276, 800) and Vehicles in range (88, 110):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10


        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        x ['CalculationShort_Input321'] = float(data["DealeArea_Input119"])


        Park = 256
        Vehicles = 178     
                  
        while Park in range (255, 265) and Vehicles in range (177, 187):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


            
        Park = 267
        Vehicles = 189      
                  
        while Park in range (266, 276) and Vehicles in range (188, 198):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 278
        Vehicles = 200      
                  
        while Park in range (277, 287) and Vehicles in range (199, 209):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 289
        Vehicles = 211      
                  
        while Park in range (288, 298) and Vehicles in range (210, 220):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 300
        Vehicles = 222      
                  
        while Park in range (299, 309) and Vehicles in range (221, 231):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 311
        Vehicles = 233      
                  
        while Park in range (310, 320) and Vehicles in range (232, 242):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 322
        Vehicles = 244      
                  
        while Park in range (321, 331) and Vehicles in range (243, 253):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1          



                                ################################################


        data = current_db.dealerarea.find_one({"GlobalId": "global"})

        Park = 832
        Vehicles = 56
      
        while Park in range (831, 844) and Vehicles in range (55, 67):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10  

        Park = 854
        Vehicles = 91
      
        while Park in range (853, 877) and Vehicles in range (90, 112):         
            x["CalculationShort_Input" + str(Park)] = float(data["DealeArea_Input" + str(Vehicles)])
            Park +=  11
            Vehicles += 10


        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        x ['CalculationShort_Input898'] = float(data["DealeArea_Input121"])


        Park = 833
        Vehicles = 255     
                  
        while Park in range (832, 842) and Vehicles in range (254, 264):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


            
        Park = 844
        Vehicles = 266      
                  
        while Park in range (843, 853) and Vehicles in range (265, 275):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 855
        Vehicles = 277      
                  
        while Park in range (854, 864) and Vehicles in range (276, 286):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 866
        Vehicles = 288      
                  
        while Park in range (865, 875) and Vehicles in range (287, 297):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 877
        Vehicles = 299      
                  
        while Park in range (876, 886) and Vehicles in range (298, 308):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1  


        Park = 888
        Vehicles = 310      
                  
        while Park in range (887, 897) and Vehicles in range (309, 319):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1


        Park = 899
        Vehicles = 321      
                  
        while Park in range (898, 908) and Vehicles in range (320, 330):         
            x["CalculationShort_Input" + str(Park)] = float(x["CalculationShort_Input" + str(Vehicles)])
            Park +=  1
            Vehicles += 1          


                                ################################################



        # =((Year DAF Parts CPV short) * ((1-Vehicule input stand still / (1-Default stand still))) * (1+Parts pricing factor) * (1+Country factor))
        # =((20*((1-1200/(1-(30/100))))*(1+(40/100))*(1+(50/100))))$'OM Parts CPV'.F7

        data = current_db.shorts.find_one({"GlobalId": "global"})
        data1 = current_db.vehicle.find_one({"GlobalId": "global"})


        DAF_Calculation = 909
        DAF_Shorts = 1

        Parts_Pricing_Factor = float(x["CalculationShort_Input2875"]) / 100
        Country_Factor = float(x["CalculationShort_Input2876"]) / 100
        Default_Standstill_Factor = float(x["CalculationShort_Input2877"]) / 100
        Number_of_years_to_calculate_potential = float(x["CalculationShort_Input2878"])
        Vehicle_Parc_Standstill = float(data1["VehicleParc_Input205"]) / 100
        Standstill = ((1 - Vehicle_Parc_Standstill) / (1 - Default_Standstill_Factor))
        
        

        while DAF_Calculation in range (908, 924) and DAF_Shorts in range (0, 16):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1 
            
        DAF_Calculation = 925
        DAF_Shorts = 17

        while DAF_Calculation in range(924, 940) and DAF_Shorts in range(16, 32):
            unrounded_value = float(data["Short_Input" + str(DAF_Shorts)]) * (
                (1 - Vehicle_Parc_Standstill / (1 - Default_Standstill_Factor))
                * (1 + Parts_Pricing_Factor)
                * (1 + Country_Factor)
            )

            # Keep the unrounded value in the variable
            x["Unrounded_CalculationShort_Input" + str(DAF_Calculation)] = unrounded_value

            # Format the unrounded value to display only three digits after the decimal point without rounding
            formatted_value = "{:.3f}".format(unrounded_value)

            x["CalculationShort_Input" + str(DAF_Calculation)] = formatted_value
            DAF_Calculation += 1
            DAF_Shorts += 1


            

        DAF_Calculation = 941
        DAF_Shorts = 33

        while DAF_Calculation in range (940, 956) and DAF_Shorts in range (32, 48):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1    

        DAF_Calculation = 957
        DAF_Shorts = 49

        while DAF_Calculation in range (956, 972) and DAF_Shorts in range (48, 64):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1   

        DAF_Calculation = 973
        DAF_Shorts = 65

        while DAF_Calculation in range (972, 988) and DAF_Shorts in range (64, 80):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1  

        DAF_Calculation = 989
        DAF_Shorts = 81

        while DAF_Calculation in range (988, 1004) and DAF_Shorts in range (80, 96):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1 

        DAF_Calculation = 1005
        DAF_Shorts = 97

        while DAF_Calculation in range (1004, 1020) and DAF_Shorts in range (96, 112):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)]) *((1-Vehicle_Parc_Standstill/(1-Default_Standstill_Factor)))*(1+Parts_Pricing_Factor)*(1+Country_Factor)),3) 
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round
            DAF_Calculation +=  1
            DAF_Shorts += 1                                                                                                         


                    ######################################################################
                    # 2. DAF Labour Hours:

        DAF_Calculation = 1037
        DAF_Shorts = 129

        while DAF_Calculation in range (1036, 1053) and DAF_Shorts in range (128, 145):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1 


        DAF_Calculation = 1053
        DAF_Shorts = 145
        while DAF_Calculation in range (1052, 1068) and DAF_Shorts in range (144, 161):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1    

            

        DAF_Calculation = 1068
        DAF_Shorts = 161

        while DAF_Calculation in range (1067, 1084) and DAF_Shorts in range (160, 177):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1 

        DAF_Calculation = 1084
        DAF_Shorts = 177

        while DAF_Calculation in range (1083, 1101) and DAF_Shorts in range (176, 193):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1 

        DAF_Calculation = 1101
        DAF_Shorts = 193

        while DAF_Calculation in range (1100, 1117) and DAF_Shorts in range (192, 209):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1 

        DAF_Calculation = 1117
        DAF_Shorts = 209

        while DAF_Calculation in range (1116, 1134) and DAF_Shorts in range (208, 225):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  


        DAF_Calculation = 1134
        DAF_Shorts = 225

        while DAF_Calculation in range (1133, 1149) and DAF_Shorts in range (224, 241):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) * ( ( 1-Vehicle_Parc_Standstill ) / (1-Default_Standstill_Factor )) * (1+ Country_Factor), 3)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1   



                        ##########################################################################################################

        DAF_Calculation = 1166
        DAF_Shorts = 129
        DAF_Running = 49

        while DAF_Calculation in range (1165, 1182) and DAF_Shorts in range (128, 145) and DAF_Running in range (48, 64):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1    


        DAF_Calculation = 1183
        DAF_Shorts = 145
        DAF_Running = 65

        while DAF_Calculation in range (1182, 1201) and DAF_Shorts in range (144, 161) and DAF_Running in range (64, 81):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1 


        DAF_Calculation = 1201
        DAF_Shorts = 161
        DAF_Running = 81

        while DAF_Calculation in range (1200, 1217) and DAF_Shorts in range (160, 175) and DAF_Running in range (80, 95):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1    


        DAF_Calculation = 1217
        DAF_Shorts = 177
        DAF_Running = 97

        while DAF_Calculation in range (1216, 1233) and DAF_Shorts in range (176, 193) and DAF_Running in range (96, 113):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1   


        DAF_Calculation = 1233
        DAF_Shorts = 193
        DAF_Running = 113

        while DAF_Calculation in range (1232, 1249) and DAF_Shorts in range (192, 209) and DAF_Running in range (112, 129):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1   


        DAF_Calculation = 1249
        DAF_Shorts = 209
        DAF_Running = 129

        while DAF_Calculation in range (1248, 1265) and DAF_Shorts in range (208, 225) and DAF_Running in range (128, 145):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1  


        DAF_Calculation = 1265
        DAF_Shorts = 225
        DAF_Running = 145

        while DAF_Calculation in range (1264, 1281) and DAF_Shorts in range (224, 241) and DAF_Running in range (144, 161):
            Round = round(((float(data["Short_Input" + str(DAF_Shorts)]) * float(data1["VehicleParc_Input" + str(DAF_Running)]))* (((1 - Vehicle_Parc_Standstill) / (1-Default_Standstill_Factor)))*(1 + Country_Factor)),2)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  
            DAF_Running += 1                                                                             


                    ###################################################
                    #4. DAF Oil

        DAF_Calculation = 1297
        DAF_Shorts = 1313


        while DAF_Calculation in range (1296, 1313) and DAF_Shorts in range (1312, 1329):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  

         

        DAF_Calculation = 1313
        DAF_Shorts = 257


        while DAF_Calculation in range (1312, 1328) and DAF_Shorts in range (256, 273):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1   


        DAF_Calculation = 1329
        DAF_Shorts = 273


        while DAF_Calculation in range (1328, 1345) and DAF_Shorts in range (272, 289):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  


        DAF_Calculation = 1345
        DAF_Shorts = 289


        while DAF_Calculation in range (1344, 1360) and DAF_Shorts in range (288, 305):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  


        DAF_Calculation = 1361
        DAF_Shorts = 305


        while DAF_Calculation in range (1360, 1377) and DAF_Shorts in range (304, 321):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1   


        DAF_Calculation = 1377
        DAF_Shorts = 321


        while DAF_Calculation in range (1376, 1393) and DAF_Shorts in range (320, 337):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1  


        DAF_Calculation = 1393
        DAF_Shorts = 337


        while DAF_Calculation in range (1392, 1409) and DAF_Shorts in range (336, 352):
            Round = round((float(data["Short_Input" + str(DAF_Shorts)])) / (1) * (( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor )) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1                                                                   


               ###################################################
                #5. OM Parts

        DAF_Calculation = 1425
        DAF_Shorts = 369

        while DAF_Calculation in range (1424, 1441) and DAF_Shorts in range (368, 384):
            Round = round(( 0 * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1    


        DAF_Calculation = 1441
        DAF_Shorts = 384

        while DAF_Calculation in range (1440, 1457) and DAF_Shorts in range (383, 399):
            Round = round(( 0 * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1                             

            

                ###################################################                
                #6. Trailer Parts

        DAF_Calculation = 1457
        DAF_Shorts = 414
        Trailer_Sales_Dealer = 177

        while DAF_Calculation in range (1456, 1464) and DAF_Shorts in range (413, 421) and Trailer_Sales_Dealer in range (176, 185):
            Round = round(( float(data1["VehicleParc_Input" + str(Trailer_Sales_Dealer)]) * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1
            Trailer_Sales_Dealer +=1   


        DAF_Calculation = 1473
        DAF_Shorts = 429
        Trailer_Sales_Dealer = 185

        while DAF_Calculation in range (1472, 1481) and DAF_Shorts in range (428, 436) and Trailer_Sales_Dealer in range (184, 193):
            Round = round(( float(data1["VehicleParc_Input" + str(Trailer_Sales_Dealer)]) * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1
            Trailer_Sales_Dealer +=1     

        DAF_Calculation = 1464
        DAF_Shorts = 421
        Trailer_Sales_Dealer = 177

        while DAF_Calculation in range (1463, 1473) and DAF_Shorts in range (420, 429) and Trailer_Sales_Dealer in range (176, 185):
            Round = round(( float(data1["VehicleParc_Input" + str(Trailer_Sales_Dealer)]) * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1
            Trailer_Sales_Dealer +=1   


        DAF_Calculation = 1481
        DAF_Shorts = 430
        Trailer_Sales_Dealer = 185

        while DAF_Calculation in range (1480, 1489) and DAF_Shorts in range (429, 443) and Trailer_Sales_Dealer in range (184, 193):
            Round = round(( float(data1["VehicleParc_Input" + str(Trailer_Sales_Dealer)]) * float(data["Short_Input" + str(DAF_Shorts)])) * ( 1 - Vehicle_Parc_Standstill ) / ( 1 - Default_Standstill_Factor) * (1 + Parts_Pricing_Factor) * ( 1 + Country_Factor ),0)
            x["CalculationShort_Input" + str(DAF_Calculation)] = Round  
            DAF_Calculation +=  1
            DAF_Shorts += 1
            Trailer_Sales_Dealer +=1              


                ################################################### 

        Year_Short = 2879
        Type_Short = 1489
        
        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1488, 1499):
            
            if  float( x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0



            Year_Short +=  1
            Type_Short += 1   

        Year_Short = 2879
        Type_Short = 1499
        
        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1498, 1509):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

     
            Year_Short +=  1
            Type_Short += 1  

        Year_Short = 2879
        Type_Short = 1509
        
        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1508, 1519):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

     
            Year_Short +=  1
            Type_Short += 1  


        Year_Short = 2879
        Type_Short = 1519
        
        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1518, 1529):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

    
            Year_Short +=  1
            Type_Short += 1                          





        Year_Short = 2879
        Type_Short = 1529
        
        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1528, 1539):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

     
            Year_Short +=  1
            Type_Short += 1   

        Year_Short = 2879
        Type_Short = 1539            

        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1538, 1549):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

      
            Year_Short +=  1
            Type_Short += 1    

        Year_Short = 2879
        Type_Short = 1549            

        Number_Years = float(x["CalculationShort_Input2878"])

        while Year_Short in range (2878, 2889) and Type_Short in range (1548, 1559):
            
            if  float(x["CalculationShort_Input" + str(Year_Short)]) <= Number_Years:
                x["CalculationShort_Input" + str(Type_Short)]  = 1
            else:
                x["CalculationShort_Input" + str(Type_Short)] = 0

   
            Year_Short +=  1
            Type_Short += 1                          


                ###################################################
                # DAF Oil
                #1st. Current YEar

        DAF_Parks = 1 #D48
        DAF_Labour = 909 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 1559

        while DAF_Parks in range (0, 11) and DAF_Labour in range (908, 924) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (1558, 1570):
            
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   


        DAF_Parks = 12 #D48
        DAF_Labour = 925 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 1570

        while DAF_Parks in range (11, 22) and DAF_Labour in range (924, 940) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (1569, 1580):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 23 #D48
        DAF_Labour = 941 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 1581

        while DAF_Parks in range (22, 33) and DAF_Labour in range (940, 956) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (1580, 1591):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 34 #D48
        DAF_Labour = 957 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 1592

        while DAF_Parks in range (33, 44) and DAF_Labour in range (956, 972) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (1591, 1602):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 45 #D48
        DAF_Labour = 973 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 1603

        while DAF_Parks in range (44, 55) and DAF_Labour in range (972, 988) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (1602, 1613):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 56 #D48
        DAF_Labour = 989 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 1614

        while DAF_Parks in range (55, 66) and DAF_Labour in range (988, 1002) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (1613, 1624):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1                                     

        DAF_Parks = 67 #D48
        DAF_Labour = 1005 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 1625

        while DAF_Parks in range (66, 77) and DAF_Labour in range (1004, 1018) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (1624, 1635):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round((float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

            ###############################################################################
                        #2nd year

        DAF_Parks = 89 #D48
        DAF_Labour = 909 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 1647

        while DAF_Parks in range (88, 99) and DAF_Labour in range (908, 924) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (1646, 1657):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 100 #D48
        DAF_Labour = 925 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 1658

        while DAF_Parks in range (99, 110) and DAF_Labour in range (924, 940) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (1657, 1668):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 111 #D48
        DAF_Labour = 941 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 1669

        while DAF_Parks in range (110, 121) and DAF_Labour in range (940, 956) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (1668, 1679):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 122 #D48
        DAF_Labour = 957 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 1680

        while DAF_Parks in range (121, 132) and DAF_Labour in range (956, 972) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (1679, 1691):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 133 #D48
        DAF_Labour = 973 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 1691

        while DAF_Parks in range (132, 143) and DAF_Labour in range (972, 988) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (1690, 1701):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 144 #D48
        DAF_Labour = 989 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 1702

        while DAF_Parks in range (143, 154) and DAF_Labour in range (988, 1004) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (1701, 1712):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] = round( float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 155 #D48
        DAF_Labour = 1005 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 1713

        while DAF_Parks in range (154, 165) and DAF_Labour in range (1004, 1019) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (1712, 1729):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  
            
                                    ###########################################  
                                    # 3rd year DAF Parts 


        DAF_Parks = 178 #D48
        DAF_Labour = 909 #R7 
        DAF_Parts = 1489
        Current_Year_Daf = 1735

        while DAF_Parks in range (177, 188) and DAF_Labour in range (908, 924) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (1734, 1745):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 189 #D48
        DAF_Labour = 925 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 1746

        while DAF_Parks in range (188, 199) and DAF_Labour in range (924, 940) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (1745, 1756):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 200 #D48
        DAF_Labour = 941 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 1757

        while DAF_Parks in range (199, 210) and DAF_Labour in range (940, 956) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (1756, 1767):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 211 #D48
        DAF_Labour = 957 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 1768

        while DAF_Parks in range (210, 221) and DAF_Labour in range (956, 972) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (1767, 1778):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)      

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 222 #D48
        DAF_Labour = 973 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 1779

        while DAF_Parks in range (221, 232) and DAF_Labour in range (972, 988) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (1778, 1789):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 233 #D48
        DAF_Labour = 989 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 1790

        while DAF_Parks in range (232, 243) and DAF_Labour in range (988, 1004) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (1789, 1800):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 244 #D48
        DAF_Labour = 1005 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 1801

        while DAF_Parks in range (243, 254) and DAF_Labour in range (1004, 1020) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (1800, 1811):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

                                    ###########################################  
                                    # 4th year DAF Parts 

        DAF_Parks = 255 #D48
        DAF_Labour = 909 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 1823

        while DAF_Parks in range (254, 265) and DAF_Labour in range (908, 924) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (1822, 1833):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 266 #D48
        DAF_Labour = 925 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 1834

        while DAF_Parks in range (265, 276) and DAF_Labour in range (924, 940) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (1833, 1844):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 277 #D48
        DAF_Labour = 941 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 1845

        while DAF_Parks in range (276, 287) and DAF_Labour in range (940, 956) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (1844, 1855):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 288 #D48
        DAF_Labour = 957 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 1856

        while DAF_Parks in range (287, 298) and DAF_Labour in range (956, 972) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (1855, 1866):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 299 #D48
        DAF_Labour = 973 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 1867

        while DAF_Parks in range (298, 309) and DAF_Labour in range (972, 988) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (1866, 1877):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 310 #D48
        DAF_Labour = 989 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 1878

        while DAF_Parks in range (309, 320) and DAF_Labour in range (988, 1004) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (1877, 1888):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 321 #D48
        DAF_Labour = 1005 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 1889

        while DAF_Parks in range (320, 331) and DAF_Labour in range (1004, 1020) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (1888, 1899):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 



                                    ###########################################  
                                    # 5th year DAF Parts 

        DAF_Parks = 832 #D48
        DAF_Labour = 909 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 1911

        while DAF_Parks in range (831, 842) and DAF_Labour in range (908, 924) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (1910, 1921):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 843 #D48
        DAF_Labour = 925 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 1922

        while DAF_Parks in range (842, 853) and DAF_Labour in range (924, 940) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (1921, 1932):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 854 #D48
        DAF_Labour = 941 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 1933

        while DAF_Parks in range (853, 864) and DAF_Labour in range (940, 956) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (1932, 1943):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 865 #D48
        DAF_Labour = 957 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 1944

        while DAF_Parks in range (864, 875) and DAF_Labour in range (956, 972) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (1943, 1954):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 876 #D48
        DAF_Labour = 973 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 1955

        while DAF_Parks in range (875, 886) and DAF_Labour in range (972, 988) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (1954, 1965):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 887 #D48
        DAF_Labour = 989 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 1966

        while DAF_Parks in range (886, 897) and DAF_Labour in range (988, 1004) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (1965, 1976):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 898 #D48
        DAF_Labour = 1005 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 1977

        while DAF_Parks in range (897, 908) and DAF_Labour in range (1004, 1020) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (1976, 1987):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 




                ###################################################
                # DAF Labour
                #1st. Current YEar

        DAF_Parks = 1 #D48
        DAF_Labour = 1037 #R7
        DAF_Parts = 1484 #AK7
        Current_Year_Daf = 1999

        while DAF_Parks in range (0, 11) and DAF_Labour in range (1036, 1052) and DAF_Parts in range (1483, 1499) and Current_Year_Daf in range (1998, 2009):
            
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   


        DAF_Parks = 12 #D48
        DAF_Labour = 1053 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2010

        while DAF_Parks in range (11, 22) and DAF_Labour in range (1052, 1067) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2009, 2020):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 23 #D48
        DAF_Labour = 1068 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2021

        while DAF_Parks in range (22, 33) and DAF_Labour in range (1067, 1083) and DAF_Parts in range (1508, 1559) and Current_Year_Daf in range (2020, 2031):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 34 #D48
        DAF_Labour = 1084 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2032

        while DAF_Parks in range (33, 44) and DAF_Labour in range (1083, 1100) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2031, 2042):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 45 #D48
        DAF_Labour = 1101 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2043

        while DAF_Parks in range (44, 55) and DAF_Labour in range (1100, 1116) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2042, 2053):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 56 #D48
        DAF_Labour = 1117 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2054

        while DAF_Parks in range (55, 66) and DAF_Labour in range (1116, 1133) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2053, 2064):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1                                     

        DAF_Parks = 67 #D48
        DAF_Labour = 1134 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2065

        while DAF_Parks in range (66, 77) and DAF_Labour in range (1133, 1149) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2064, 2076):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

            ###############################################################################
                        #2nd year

        DAF_Parks = 89 #D48
        DAF_Labour = 1037 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2087

        while DAF_Parks in range (88, 99) and DAF_Labour in range (1036, 1052) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2086, 2097):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 100 #D48
        DAF_Labour = 1053 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2098

        while DAF_Parks in range (99, 110) and DAF_Labour in range (1052, 1067) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2097, 2108):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 111 #D48
        DAF_Labour = 1068 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2109

        while DAF_Parks in range (110, 121) and DAF_Labour in range (1067, 1083) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2108, 2119):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 122 #D48
        DAF_Labour = 1084 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2120

        while DAF_Parks in range (121, 132) and DAF_Labour in range (1083, 1100) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2119, 2130):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 133 #D48
        DAF_Labour = 1101 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2131

        while DAF_Parks in range (132, 143) and DAF_Labour in range (1100, 1116) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2130, 2141):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 144 #D48
        DAF_Labour = 1117 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2142

        while DAF_Parks in range (143, 154) and DAF_Labour in range (1116, 1133) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2141, 2152):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 155 #D48
        DAF_Labour = 1134 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2153

        while DAF_Parks in range (154, 165) and DAF_Labour in range (1133, 1149) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2152, 2163):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  
            
                                    ###########################################  
                                    # 3rd year 


        DAF_Parks = 178 #D48
        DAF_Labour = 1037 #R7 
        DAF_Parts = 1489
        Current_Year_Daf = 2175

        while DAF_Parks in range (177, 188) and DAF_Labour in range (1036, 1052) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2174, 2185):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 189 #D48
        DAF_Labour = 1053 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2186

        while DAF_Parks in range (188, 199) and DAF_Labour in range (1052, 1067) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2185, 2196):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 200 #D48
        DAF_Labour = 1068 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2197

        while DAF_Parks in range (199, 210) and DAF_Labour in range (1067, 1083) and DAF_Parts in range (1508, 1559) and Current_Year_Daf in range (2196, 2207):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 211 #D48
        DAF_Labour = 1084 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2208

        while DAF_Parks in range (210, 221) and DAF_Labour in range (1083, 1100) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2207, 2218):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 222 #D48
        DAF_Labour = 1101 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2219

        while DAF_Parks in range (221, 232) and DAF_Labour in range (1100, 1116) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2218, 2229):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 233 #D48
        DAF_Labour = 1117 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2230

        while DAF_Parks in range (232, 243) and DAF_Labour in range (1116, 1133) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2229, 2240):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 244 #D48
        DAF_Labour = 1134 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2241

        while DAF_Parks in range (243, 254) and DAF_Labour in range (1133, 1149) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2240, 2251):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

                                    ###########################################  
                                    # 4th year DAF Parts 

        DAF_Parks = 255 #D48
        DAF_Labour = 1037 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2263

        while DAF_Parks in range (254, 265) and DAF_Labour in range (1036, 1052) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2262, 2273):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 266 #D48
        DAF_Labour = 1053 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2274

        while DAF_Parks in range (265, 276) and DAF_Labour in range (1052, 1067) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2273, 2284):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 277 #D48
        DAF_Labour = 1068 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2285

        while DAF_Parks in range (276, 287) and DAF_Labour in range (1067, 1083) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2284, 2295):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 288 #D48
        DAF_Labour = 1084 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2296

        while DAF_Parks in range (287, 298) and DAF_Labour in range (1083, 1100) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2295, 2306):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 299 #D48
        DAF_Labour = 1101 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2307

        while DAF_Parks in range (298, 309) and DAF_Labour in range (1100, 1116) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2306, 2317):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 310 #D48
        DAF_Labour = 1117 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2318

        while DAF_Parks in range (309, 320) and DAF_Labour in range (1116, 1133) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2317, 2328):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] = round( float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 321 #D48
        DAF_Labour = 1134 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2329

        while DAF_Parks in range (320, 331) and DAF_Labour in range (1133, 1149) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2328, 2340):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  round(float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]),3)     

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 



                                    ###########################################  
                                    # 5th year DAF Parts 

        DAF_Parks = 832 #D48
        DAF_Labour = 1037 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2351

        while DAF_Parks in range (831, 842) and DAF_Labour in range (1036, 1052) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2350, 2361):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 843 #D48
        DAF_Labour = 1053 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2362

        while DAF_Parks in range (842, 853) and DAF_Labour in range (1052, 1067) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2361, 2372):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 854 #D48
        DAF_Labour = 1068 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2373

        while DAF_Parks in range (853, 864) and DAF_Labour in range (1067, 1083) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2372, 2383):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 865 #D48
        DAF_Labour = 1084 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2384

        while DAF_Parks in range (864, 875) and DAF_Labour in range (1083, 1100) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2383, 2394):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 876 #D48
        DAF_Labour = 1101 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2395

        while DAF_Parks in range (875, 886) and DAF_Labour in range (1100, 1116) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2394, 2406):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 887 #D48
        DAF_Labour = 1117 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2407

        while DAF_Parks in range (886, 897) and DAF_Labour in range (1116, 1133) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2406, 2417):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 898 #D48
        DAF_Labour = 1134 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2418

        while DAF_Parks in range (897, 908) and DAF_Labour in range (1133, 1149) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2417, 2428):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

                ###################################################
                # DAF Oil
                #1st. Current YEar

        DAF_Parks = 1 #D48
        DAF_Labour = 1297 #R7
        DAF_Parts = 1484 #AK7
        Current_Year_Daf = 2440

        while DAF_Parks in range (0, 11) and DAF_Labour in range (1296, 1312) and DAF_Parts in range (1483, 1499) and Current_Year_Daf in range (2439, 2450):
            
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   


        DAF_Parks = 12 #D48
        DAF_Labour = 1313 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2451

        while DAF_Parks in range (11, 22) and DAF_Labour in range (1312, 1328) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2450, 2461):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 23 #D48
        DAF_Labour = 1329 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2462

        while DAF_Parks in range (22, 33) and DAF_Labour in range (1328, 1344) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2461, 2472):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 34 #D48
        DAF_Labour = 1345 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2473

        while DAF_Parks in range (33, 44) and DAF_Labour in range (1344, 1360) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2472, 2483):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 45 #D48
        DAF_Labour = 1361 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2484

        while DAF_Parks in range (44, 55) and DAF_Labour in range (1360, 1376) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2483, 2494):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 

        DAF_Parks = 56 #D48
        DAF_Labour = 1377 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2495

        while DAF_Parks in range (55, 66) and DAF_Labour in range (1376, 1392) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2494, 2505):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1                                     

        DAF_Parks = 67 #D48
        DAF_Labour = 1393 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2506

        while DAF_Parks in range (66, 77) and DAF_Labour in range (1392, 1409) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2505, 2516):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

            ###############################################################################
                        #2nd year

        DAF_Parks = 89 #D48
        DAF_Labour = 1297 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2528

        while DAF_Parks in range (88, 99) and DAF_Labour in range (1296, 1312) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2527, 2538):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 100 #D48
        DAF_Labour = 1313 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2539

        while DAF_Parks in range (99, 110) and DAF_Labour in range (1312, 1328) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2538, 2549):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 111 #D48
        DAF_Labour = 1329 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2550

        while DAF_Parks in range (110, 121) and DAF_Labour in range (1328, 1344) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2549, 2560):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 122 #D48
        DAF_Labour = 1345 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2561

        while DAF_Parks in range (121, 132) and DAF_Labour in range (1344, 1360) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2560, 2571):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 133 #D48
        DAF_Labour = 1361 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2572

        while DAF_Parks in range (132, 143) and DAF_Labour in range (1360, 1376) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2571, 2582):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 144 #D48
        DAF_Labour = 1377 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2583

        while DAF_Parks in range (143, 154) and DAF_Labour in range (1376, 1392) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2582, 2593):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 155 #D48
        DAF_Labour = 1393 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2594

        while DAF_Parks in range (154, 165) and DAF_Labour in range (1392, 1408) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2593, 2604):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  
            
                                    ###########################################  
                                    # 3rd year DAF Parts 


        DAF_Parks = 178 #D48
        DAF_Labour = 1297 #R7 
        DAF_Parts = 1489
        Current_Year_Daf = 2616

        while DAF_Parks in range (177, 188) and DAF_Labour in range (1296, 1312) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2615, 2626):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 189 #D48
        DAF_Labour = 1313 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2627

        while DAF_Parks in range (188, 199) and DAF_Labour in range (1312, 1328) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2626, 2637):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 200 #D48
        DAF_Labour = 1329 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2638

        while DAF_Parks in range (199, 210) and DAF_Labour in range (1328, 1344) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2627, 2648):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 211 #D48
        DAF_Labour = 1345 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2649

        while DAF_Parks in range (210, 221) and DAF_Labour in range (1344, 1360) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2648, 2659):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 222 #D48
        DAF_Labour = 1361 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2660

        while DAF_Parks in range (221, 232) and DAF_Labour in range (1360, 1376) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2659, 2670):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 233 #D48
        DAF_Labour = 1377 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2671

        while DAF_Parks in range (232, 243) and DAF_Labour in range (1376, 1392) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2670, 2682):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 244 #D48
        DAF_Labour = 1393 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2682

        while DAF_Parks in range (243, 254) and DAF_Labour in range (1392, 1408) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2681, 2692):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

                                    ###########################################  
                                    # 4th year DAF Parts 

        DAF_Parks = 255 #D48
        DAF_Labour = 1297 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2704

        while DAF_Parks in range (254, 265) and DAF_Labour in range (1296, 1312) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2703, 2714):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 266 #D48
        DAF_Labour = 1313 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2715

        while DAF_Parks in range (265, 276) and DAF_Labour in range (1312, 1328) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2714, 2725):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 277 #D48
        DAF_Labour = 1329 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2726

        while DAF_Parks in range (276, 287) and DAF_Labour in range (1328, 1344) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2725, 2736):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 288 #D48
        DAF_Labour = 1345 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2737

        while DAF_Parks in range (287, 298) and DAF_Labour in range (1344, 1360) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2736, 2747):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 299 #D48
        DAF_Labour = 1361 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2748

        while DAF_Parks in range (298, 309) and DAF_Labour in range (1360, 1376) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2747, 2758):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 310 #D48
        DAF_Labour = 1377 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2759

        while DAF_Parks in range (309, 320) and DAF_Labour in range (1376, 1392) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2758, 2769):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])    

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 321 #D48
        DAF_Labour = 1393 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2770

        while DAF_Parks in range (320, 331) and DAF_Labour in range (1392, 1408) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2769, 2780):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 



                                    ###########################################  
                                    # 5th year DAF Parts 

        DAF_Parks = 832 #D48
        DAF_Labour = 1297 #R7
        DAF_Parts = 1489 #AK7
        Current_Year_Daf = 2792

        while DAF_Parks in range (831, 842) and DAF_Labour in range (1296, 1312) and DAF_Parts in range (1488, 1499) and Current_Year_Daf in range (2791, 2802):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])   

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1    

        DAF_Parks = 843 #D48
        DAF_Labour = 1313 #R7
        DAF_Parts = 1499 #AK7
        Current_Year_Daf = 2803

        while DAF_Parks in range (842, 853) and DAF_Labour in range (1312, 1328) and DAF_Parts in range (1498, 1509) and Current_Year_Daf in range (2802, 2813):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1   

        DAF_Parks = 854 #D48
        DAF_Labour = 1329 #R7
        DAF_Parts = 1509 #AK7
        Current_Year_Daf = 2815

        while DAF_Parks in range (853, 864) and DAF_Labour in range (1328, 1344) and DAF_Parts in range (1508, 1519) and Current_Year_Daf in range (2814, 2825):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  


        DAF_Parks = 865 #D48
        DAF_Labour = 1345 #R7
        DAF_Parts = 1519 #AK7
        Current_Year_Daf = 2826

        while DAF_Parks in range (864, 875) and DAF_Labour in range (1344, 1360) and DAF_Parts in range (1518, 1529) and Current_Year_Daf in range (2825, 2836):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 876 #D48
        DAF_Labour = 1361 #R7
        DAF_Parts = 1529 #AK7
        Current_Year_Daf = 2837

        while DAF_Parks in range (875, 886) and DAF_Labour in range (1360, 1376) and DAF_Parts in range (1528, 1539) and Current_Year_Daf in range (2836, 2847):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 887 #D48
        DAF_Labour = 1377 #R7
        DAF_Parts = 1539 #AK7
        Current_Year_Daf = 2848

        while DAF_Parks in range (886, 897) and DAF_Labour in range (1376, 1392) and DAF_Parts in range (1538, 1549) and Current_Year_Daf in range (2847, 2858):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)])  

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1  

        DAF_Parks = 898 #D48
        DAF_Labour = 1393 #R7
        DAF_Parts = 1549 #AK7
        Current_Year_Daf = 2911

        while DAF_Parks in range (897, 908) and DAF_Labour in range (1392, 1408) and DAF_Parts in range (1548, 1559) and Current_Year_Daf in range (2910, 2921):
                
            x["CalculationShort_Input" + str(Current_Year_Daf)] =  float(x["CalculationShort_Input" + str(DAF_Parks)]) * float(x["CalculationShort_Input" + str(DAF_Labour)]) * float(x["CalculationShort_Input" + str(DAF_Parts)]) 

            DAF_Labour +=  1                                                                     
            DAF_Parts +=  1
            DAF_Parks +=  1            
            Current_Year_Daf += 1 
                                        ###########################################
                                        #Total
                         
 
            x["CalculationShort_Input78"] = float(x["CalculationShort_Input1"]) + float(x["CalculationShort_Input12"]) \
                                            + float(x["CalculationShort_Input23"]) + float(x["CalculationShort_Input34"]) \
                                                + float(x["CalculationShort_Input45"]) + float(x["CalculationShort_Input56"]) + float(x["CalculationShort_Input67"])

 
            x["CalculationShort_Input79"] = float(x["CalculationShort_Input2"]) + float(x["CalculationShort_Input13"]) \
                                            + float(x["CalculationShort_Input24"]) + float(x["CalculationShort_Input35"]) \
                                                + float(x["CalculationShort_Input46"]) + float(x["CalculationShort_Input57"]) + float(x["CalculationShort_Input68"])  


            x["CalculationShort_Input80"] = float(x["CalculationShort_Input3"]) + float(x["CalculationShort_Input14"]) \
                                            + float(x["CalculationShort_Input25"]) + float(x["CalculationShort_Input36"]) \
                                                + float(x["CalculationShort_Input47"]) + float(x["CalculationShort_Input58"]) + float(x["CalculationShort_Input69"]) 


            x["CalculationShort_Input81"] = float(x["CalculationShort_Input4"]) + float(x["CalculationShort_Input15"]) \
                                            + float(x["CalculationShort_Input26"]) + float(x["CalculationShort_Input37"]) \
                                                + float(x["CalculationShort_Input48"]) + float(x["CalculationShort_Input59"]) + float(x["CalculationShort_Input70"])  

 
            x["CalculationShort_Input82"] = float(x["CalculationShort_Input5"]) + float(x["CalculationShort_Input16"]) \
                                            + float(x["CalculationShort_Input27"]) + float(x["CalculationShort_Input38"]) \
                                                + float(x["CalculationShort_Input49"]) + float(x["CalculationShort_Input60"]) + float(x["CalculationShort_Input71"])

 
            x["CalculationShort_Input83"] = float(x["CalculationShort_Input6"]) + float(x["CalculationShort_Input17"]) \
                                            + float(x["CalculationShort_Input28"]) + float(x["CalculationShort_Input39"]) \
                                                + float(x["CalculationShort_Input50"]) + float(x["CalculationShort_Input61"]) + float(x["CalculationShort_Input72"])  


            x["CalculationShort_Input84"] = float(x["CalculationShort_Input7"]) + float(x["CalculationShort_Input18"]) \
                                            + float(x["CalculationShort_Input29"]) + float(x["CalculationShort_Input40"]) \
                                                + float(x["CalculationShort_Input51"]) + float(x["CalculationShort_Input62"]) + float(x["CalculationShort_Input73"]) 


            x["CalculationShort_Input85"] = float(x["CalculationShort_Input8"]) + float(x["CalculationShort_Input19"]) \
                                            + float(x["CalculationShort_Input30"]) + float(x["CalculationShort_Input41"]) \
                                                + float(x["CalculationShort_Input52"]) + float(x["CalculationShort_Input63"]) + float(x["CalculationShort_Input74"]) 


            x["CalculationShort_Input86"] = float(x["CalculationShort_Input9"]) + float(x["CalculationShort_Input20"]) \
                                            + float(x["CalculationShort_Input31"]) + float(x["CalculationShort_Input42"]) \
                                                + float(x["CalculationShort_Input53"]) + float(x["CalculationShort_Input64"]) + float(x["CalculationShort_Input75"])   


            x["CalculationShort_Input87"] = float(x["CalculationShort_Input10"]) + float(x["CalculationShort_Input21"]) \
                                            + float(x["CalculationShort_Input32"]) + float(x["CalculationShort_Input43"]) \
                                                + float(x["CalculationShort_Input54"]) + float(x["CalculationShort_Input65"]) + float(x["CalculationShort_Input76"])


            x["CalculationShort_Input88"] = float(x["CalculationShort_Input78"]) + float(x["CalculationShort_Input79"]) \
                                            + float(x["CalculationShort_Input80"]) + float(x["CalculationShort_Input81"]) \
                                                + float(x["CalculationShort_Input82"]) + float(x["CalculationShort_Input83"]) + float(x["CalculationShort_Input84"]) \
                                                   + float(x["CalculationShort_Input85"]) +  float(x["CalculationShort_Input86"]) + float(x["CalculationShort_Input87"])    


                                        ###########################################
                                        #Tota2
                         
 
            x["CalculationShort_Input166"] = float(x["CalculationShort_Input89"]) + float(x["CalculationShort_Input122"]) \
                                            + float(x["CalculationShort_Input100"]) + float(x["CalculationShort_Input133"]) \
                                                + float(x["CalculationShort_Input111"]) + float(x["CalculationShort_Input144"]) + float(x["CalculationShort_Input155"])

 
            x["CalculationShort_Input167"] = float(x["CalculationShort_Input90"]) + float(x["CalculationShort_Input123"]) \
                                            + float(x["CalculationShort_Input101"]) + float(x["CalculationShort_Input134"]) \
                                                + float(x["CalculationShort_Input112"]) + float(x["CalculationShort_Input145"]) + float(x["CalculationShort_Input156"])  


            x["CalculationShort_Input169"] = float(x["CalculationShort_Input91"]) + float(x["CalculationShort_Input124"]) \
                                            + float(x["CalculationShort_Input102"]) + float(x["CalculationShort_Input135"]) \
                                                + float(x["CalculationShort_Input113"]) + float(x["CalculationShort_Input146"]) + float(x["CalculationShort_Input157"]) 


            x["CalculationShort_Input170"] = float(x["CalculationShort_Input92"]) + float(x["CalculationShort_Input125"]) \
                                            + float(x["CalculationShort_Input103"]) + float(x["CalculationShort_Input136"]) \
                                                + float(x["CalculationShort_Input114"]) + float(x["CalculationShort_Input147"]) + float(x["CalculationShort_Input158"])  

 
            x["CalculationShort_Input171"] = float(x["CalculationShort_Input93"]) + float(x["CalculationShort_Input126"]) \
                                            + float(x["CalculationShort_Input104"]) + float(x["CalculationShort_Input137"]) \
                                                + float(x["CalculationShort_Input115"]) + float(x["CalculationShort_Input148"]) + float(x["CalculationShort_Input159"])

 
            x["CalculationShort_Input172"] = float(x["CalculationShort_Input94"]) + float(x["CalculationShort_Input127"]) \
                                            + float(x["CalculationShort_Input105"]) + float(x["CalculationShort_Input138"]) \
                                                + float(x["CalculationShort_Input116"]) + float(x["CalculationShort_Input149"]) + float(x["CalculationShort_Input160"])  

            x["CalculationShort_Input173"] = float(x["CalculationShort_Input95"]) + float(x["CalculationShort_Input128"]) \
                                            + float(x["CalculationShort_Input106"]) + float(x["CalculationShort_Input139"]) \
                                                + float(x["CalculationShort_Input117"]) + float(x["CalculationShort_Input150"]) + float(x["CalculationShort_Input161"])  

            x["CalculationShort_Input174"] = float(x["CalculationShort_Input96"]) + float(x["CalculationShort_Input129"]) \
                                            + float(x["CalculationShort_Input107"]) + float(x["CalculationShort_Input140"]) \
                                                + float(x["CalculationShort_Input118"]) + float(x["CalculationShort_Input151"]) + float(x["CalculationShort_Input162"]) 


            x["CalculationShort_Input175"] = float(x["CalculationShort_Input97"]) + float(x["CalculationShort_Input130"]) \
                                            + float(x["CalculationShort_Input108"]) + float(x["CalculationShort_Input141"]) \
                                                + float(x["CalculationShort_Input119"]) + float(x["CalculationShort_Input152"]) + float(x["CalculationShort_Input163"])   


            x["CalculationShort_Input176"] = float(x["CalculationShort_Input98"]) + float(x["CalculationShort_Input131"]) \
                                            + float(x["CalculationShort_Input109"]) + float(x["CalculationShort_Input142"]) \
                                                + float(x["CalculationShort_Input120"]) + float(x["CalculationShort_Input153"]) + float(x["CalculationShort_Input164"])
    


            x["CalculationShort_Input177"] = float(x["CalculationShort_Input166"]) + float(x["CalculationShort_Input167"]) \
                                            + float(x["CalculationShort_Input169"]) + float(x["CalculationShort_Input170"]) \
                                                + float(x["CalculationShort_Input171"]) + float(x["CalculationShort_Input172"]) + float(x["CalculationShort_Input173"]) \
                                                   + float(x["CalculationShort_Input174"]) +  float(x["CalculationShort_Input175"]) + float(x["CalculationShort_Input176"])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                        

                                        ###########################################
                                        #Tota3

            x["CalculationShort_Input13130"] = float(x["CalculationShort_Input178"]) + float(x["CalculationShort_Input189"]) \
                                            + float(x["CalculationShort_Input200"]) + float(x["CalculationShort_Input211"]) \
                                                + float(x["CalculationShort_Input222"]) + float(x["CalculationShort_Input233"]) + float(x["CalculationShort_Input244"])

 
            x["CalculationShort_Input13131"] = float(x["CalculationShort_Input179"]) + float(x["CalculationShort_Input190"]) \
                                            + float(x["CalculationShort_Input201"]) + float(x["CalculationShort_Input212"]) \
                                                + float(x["CalculationShort_Input223"]) + float(x["CalculationShort_Input234"]) + float(x["CalculationShort_Input245"])  


            x["CalculationShort_Input13132"] = float(x["CalculationShort_Input180"]) + float(x["CalculationShort_Input191"]) \
                                            + float(x["CalculationShort_Input202"]) + float(x["CalculationShort_Input213"]) \
                                                + float(x["CalculationShort_Input224"]) + float(x["CalculationShort_Input235"]) + float(x["CalculationShort_Input246"]) 


            x["CalculationShort_Input13133"] = float(x["CalculationShort_Input181"]) + float(x["CalculationShort_Input192"]) \
                                            + float(x["CalculationShort_Input203"]) + float(x["CalculationShort_Input214"]) \
                                                + float(x["CalculationShort_Input225"]) + float(x["CalculationShort_Input236"]) + float(x["CalculationShort_Input247"])  

 
            x["CalculationShort_Input13134"] = float(x["CalculationShort_Input182"]) + float(x["CalculationShort_Input193"]) \
                                            + float(x["CalculationShort_Input204"]) + float(x["CalculationShort_Input215"]) \
                                                + float(x["CalculationShort_Input226"]) + float(x["CalculationShort_Input237"]) + float(x["CalculationShort_Input248"])

 
            x["CalculationShort_Input13135"] = float(x["CalculationShort_Input183"]) + float(x["CalculationShort_Input194"]) \
                                            + float(x["CalculationShort_Input205"]) + float(x["CalculationShort_Input216"]) \
                                                + float(x["CalculationShort_Input227"]) + float(x["CalculationShort_Input238"]) + float(x["CalculationShort_Input249"])  

            x["CalculationShort_Input13136"] = float(x["CalculationShort_Input184"]) + float(x["CalculationShort_Input195"]) \
                                            + float(x["CalculationShort_Input206"]) + float(x["CalculationShort_Input217"]) \
                                                + float(x["CalculationShort_Input228"]) + float(x["CalculationShort_Input239"]) + float(x["CalculationShort_Input250"])  

            x["CalculationShort_Input13137"] = float(x["CalculationShort_Input185"]) + float(x["CalculationShort_Input196"]) \
                                            + float(x["CalculationShort_Input207"]) + float(x["CalculationShort_Input218"]) \
                                                + float(x["CalculationShort_Input229"]) + float(x["CalculationShort_Input240"]) + float(x["CalculationShort_Input251"]) 


            x["CalculationShort_Input13138"] = float(x["CalculationShort_Input186"]) + float(x["CalculationShort_Input197"]) \
                                            + float(x["CalculationShort_Input208"]) + float(x["CalculationShort_Input219"]) \
                                                + float(x["CalculationShort_Input230"]) + float(x["CalculationShort_Input241"]) + float(x["CalculationShort_Input252"])   


            x["CalculationShort_Input13139"] = float(x["CalculationShort_Input187"]) + float(x["CalculationShort_Input198"]) \
                                            + float(x["CalculationShort_Input209"]) + float(x["CalculationShort_Input220"]) \
                                                + float(x["CalculationShort_Input231"]) + float(x["CalculationShort_Input242"]) + float(x["CalculationShort_Input253"])
    


            x["CalculationShort_Input13140"] = float(x["CalculationShort_Input13130"]) + float(x["CalculationShort_Input13131"]) \
                                            + float(x["CalculationShort_Input13132"]) + float(x["CalculationShort_Input13133"]) \
                                                + float(x["CalculationShort_Input13134"]) + float(x["CalculationShort_Input13135"]) + float(x["CalculationShort_Input13136"]) \
                                                   + float(x["CalculationShort_Input13137"]) +  float(x["CalculationShort_Input13138"]) + float(x["CalculationShort_Input13139"])

                                        ###########################################
                                        #Tota4

            x["CalculationShort_Input3131"] = float(x["CalculationShort_Input255"]) + float(x["CalculationShort_Input266"]) \
                                            + float(x["CalculationShort_Input277"]) + float(x["CalculationShort_Input288"]) \
                                                + float(x["CalculationShort_Input299"]) + float(x["CalculationShort_Input310"]) + float(x["CalculationShort_Input321"])

 
            x["CalculationShort_Input3132"] = float(x["CalculationShort_Input256"]) + float(x["CalculationShort_Input267"]) \
                                            + float(x["CalculationShort_Input278"]) + float(x["CalculationShort_Input289"]) \
                                                + float(x["CalculationShort_Input300"]) + float(x["CalculationShort_Input311"]) + float(x["CalculationShort_Input322"])  


            x["CalculationShort_Input3133"] = float(x["CalculationShort_Input257"]) + float(x["CalculationShort_Input268"]) \
                                            + float(x["CalculationShort_Input279"]) + float(x["CalculationShort_Input290"]) \
                                                + float(x["CalculationShort_Input301"]) + float(x["CalculationShort_Input312"]) + float(x["CalculationShort_Input323"]) 


            x["CalculationShort_Input3134"] = float(x["CalculationShort_Input258"]) + float(x["CalculationShort_Input269"]) \
                                            + float(x["CalculationShort_Input280"]) + float(x["CalculationShort_Input291"]) \
                                                + float(x["CalculationShort_Input302"]) + float(x["CalculationShort_Input313"]) + float(x["CalculationShort_Input324"])  

 
            x["CalculationShort_Input3135"] = float(x["CalculationShort_Input259"]) + float(x["CalculationShort_Input270"]) \
                                            + float(x["CalculationShort_Input281"]) + float(x["CalculationShort_Input292"]) \
                                                + float(x["CalculationShort_Input303"]) + float(x["CalculationShort_Input314"]) + float(x["CalculationShort_Input325"])

 
            x["CalculationShort_Input3136"] = float(x["CalculationShort_Input260"]) + float(x["CalculationShort_Input271"]) \
                                            + float(x["CalculationShort_Input282"]) + float(x["CalculationShort_Input293"]) \
                                                + float(x["CalculationShort_Input304"]) + float(x["CalculationShort_Input315"]) + float(x["CalculationShort_Input326"])  

            x["CalculationShort_Input3137"] = float(x["CalculationShort_Input261"]) + float(x["CalculationShort_Input272"]) \
                                            + float(x["CalculationShort_Input283"]) + float(x["CalculationShort_Input294"]) \
                                                + float(x["CalculationShort_Input305"]) + float(x["CalculationShort_Input316"]) + float(x["CalculationShort_Input327"])  

            x["CalculationShort_Input3138"] = float(x["CalculationShort_Input262"]) + float(x["CalculationShort_Input273"]) \
                                            + float(x["CalculationShort_Input284"]) + float(x["CalculationShort_Input295"]) \
                                                + float(x["CalculationShort_Input306"]) + float(x["CalculationShort_Input317"]) + float(x["CalculationShort_Input328"]) 


            x["CalculationShort_Input3139"] = float(x["CalculationShort_Input263"]) + float(x["CalculationShort_Input274"]) \
                                            + float(x["CalculationShort_Input285"]) + float(x["CalculationShort_Input296"]) \
                                                + float(x["CalculationShort_Input307"]) + float(x["CalculationShort_Input318"]) + float(x["CalculationShort_Input329"])   


            x["CalculationShort_Input3140"] = float(x["CalculationShort_Input264"]) + float(x["CalculationShort_Input275"]) \
                                            + float(x["CalculationShort_Input286"]) + float(x["CalculationShort_Input297"]) \
                                                + float(x["CalculationShort_Input308"]) + float(x["CalculationShort_Input319"]) + float(x["CalculationShort_Input330"])
    


            x["CalculationShort_Input3141"] = float(x["CalculationShort_Input3131"]) + float(x["CalculationShort_Input3132"]) \
                                            + float(x["CalculationShort_Input3133"]) + float(x["CalculationShort_Input3134"]) \
                                                + float(x["CalculationShort_Input3135"]) + float(x["CalculationShort_Input3136"]) + float(x["CalculationShort_Input3137"]) \
                                                   + float(x["CalculationShort_Input3138"]) +  float(x["CalculationShort_Input3139"]) + float(x["CalculationShort_Input3140"])

                                        ###########################################
                                        #Tota5

            x["CalculationShort_Input2864"] = float(x["CalculationShort_Input832"]) + float(x["CalculationShort_Input843"]) \
                                            + float(x["CalculationShort_Input854"]) + float(x["CalculationShort_Input865"]) \
                                                + float(x["CalculationShort_Input876"]) + float(x["CalculationShort_Input887"]) + float(x["CalculationShort_Input898"])

 
            x["CalculationShort_Input2865"] = float(x["CalculationShort_Input833"]) + float(x["CalculationShort_Input844"]) \
                                            + float(x["CalculationShort_Input855"]) + float(x["CalculationShort_Input866"]) \
                                                + float(x["CalculationShort_Input877"]) + float(x["CalculationShort_Input888"]) + float(x["CalculationShort_Input899"])  


            x["CalculationShort_Input2866"] = float(x["CalculationShort_Input834"]) + float(x["CalculationShort_Input845"]) \
                                            + float(x["CalculationShort_Input856"]) + float(x["CalculationShort_Input867"]) \
                                                + float(x["CalculationShort_Input878"]) + float(x["CalculationShort_Input889"]) + float(x["CalculationShort_Input900"]) 


            x["CalculationShort_Input2867"] = float(x["CalculationShort_Input835"]) + float(x["CalculationShort_Input846"]) \
                                            + float(x["CalculationShort_Input857"]) + float(x["CalculationShort_Input868"]) \
                                                + float(x["CalculationShort_Input879"]) + float(x["CalculationShort_Input890"]) + float(x["CalculationShort_Input901"])  

 
            x["CalculationShort_Input2868"] = float(x["CalculationShort_Input836"]) + float(x["CalculationShort_Input847"]) \
                                            + float(x["CalculationShort_Input858"]) + float(x["CalculationShort_Input869"]) \
                                                + float(x["CalculationShort_Input880"]) + float(x["CalculationShort_Input891"]) + float(x["CalculationShort_Input902"])

 
            x["CalculationShort_Input2869"] = float(x["CalculationShort_Input837"]) + float(x["CalculationShort_Input848"]) \
                                            + float(x["CalculationShort_Input859"]) + float(x["CalculationShort_Input870"]) \
                                                + float(x["CalculationShort_Input881"]) + float(x["CalculationShort_Input892"]) + float(x["CalculationShort_Input903"])  

            x["CalculationShort_Input2870"] = float(x["CalculationShort_Input838"]) + float(x["CalculationShort_Input849"]) \
                                            + float(x["CalculationShort_Input860"]) + float(x["CalculationShort_Input871"]) \
                                                + float(x["CalculationShort_Input882"]) + float(x["CalculationShort_Input893"]) + float(x["CalculationShort_Input904"])  

            x["CalculationShort_Input2871"] = float(x["CalculationShort_Input839"]) + float(x["CalculationShort_Input850"]) \
                                            + float(x["CalculationShort_Input861"]) + float(x["CalculationShort_Input872"]) \
                                                + float(x["CalculationShort_Input883"]) + float(x["CalculationShort_Input894"]) + float(x["CalculationShort_Input905"]) 


            x["CalculationShort_Input2872"] = float(x["CalculationShort_Input840"]) + float(x["CalculationShort_Input851"]) \
                                            + float(x["CalculationShort_Input862"]) + float(x["CalculationShort_Input873"]) \
                                                + float(x["CalculationShort_Input884"]) + float(x["CalculationShort_Input895"]) + float(x["CalculationShort_Input906"])   


            x["CalculationShort_Input2873"] = float(x["CalculationShort_Input841"]) + float(x["CalculationShort_Input852"]) \
                                            + float(x["CalculationShort_Input863"]) + float(x["CalculationShort_Input874"]) \
                                                + float(x["CalculationShort_Input885"]) + float(x["CalculationShort_Input896"]) + float(x["CalculationShort_Input907"])
    


            x["CalculationShort_Input2874"] = float(x["CalculationShort_Input2864"]) + float(x["CalculationShort_Input2865"]) \
                                            + float(x["CalculationShort_Input2866"]) + float(x["CalculationShort_Input2867"]) \
                                                + float(x["CalculationShort_Input2868"]) + float(x["CalculationShort_Input2869"]) + float(x["CalculationShort_Input2870"]) \
                                                   + float(x["CalculationShort_Input2871"]) +  float(x["CalculationShort_Input2872"]) + float(x["CalculationShort_Input2873"]) 

                                        ###########################################
                                        #Tota DAF_Parts 1:

        i = 1559
        j = 1570
        k = 1581
        l = 1592
        m = 1603
        n = 1614
        o = 1625
        p = 1636

        while i in range(1558, 1569) and j in range(1569, 1580) and k in range(1580, 1591) and l in range(1591, 1602) and m in range (1602, 1613) and n in range(1613, 1624) and o in range(1624, 1635) and p in range(1635, 1646):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        #Tota DAF_Parts 2:

        i = 1647
        j = 1658
        k = 1669
        l = 1680
        m = 1691
        n = 1702
        o = 1713
        p = 1724

        while i in range(1646, 1657) and j in range(1657, 1668) and k in range(1668, 1679) and l in range(1679, 1690) and m in range (1690, 1701) and n in range(1701, 1712) and o in range(1712, 1723) and p in range(1723, 1734):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  


                                        ###########################################
                                        #Tota DAF_Parts 3:

        i = 1735
        j = 1746
        k = 1757
        l = 1768
        m = 1779
        n = 1790
        o = 1801
        p = 1812

        while i in range(1734, 1745) and j in range(1745, 1756) and k in range(1756, 1767) and l in range(1767, 1778) and m in range (1778, 1789) and n in range(1789, 1800) and o in range(1800, 1811) and p in range(1811, 1822):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        #Tota DAF_Parts 4:

        i = 1823
        j = 1834
        k = 1845
        l = 1856
        m = 1867
        n = 1878
        o = 1889
        p = 1900

        while i in range(1822, 1833) and j in range(1833, 1844) and k in range(1844, 1855) and l in range(1855, 1866) and m in range (1866, 1877) and n in range(1877, 1888) and o in range(1888, 1899) and p in range(1899, 1910):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        #Tota DAF_Parts 5:

        i = 1911
        j = 1922
        k = 1933
        l = 1944
        m = 1955
        n = 1966
        o = 1977
        p = 1988

        while i in range(1910, 1921) and j in range(1921, 1932) and k in range(1932, 1943) and l in range(1943, 1954) and m in range (1954, 1965) and n in range(1965, 1976) and o in range(1976, 1987) and p in range(1987, 1998):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        #Tota DAF_Parts 6:

        i = 1999
        j = 2010
        k = 2021
        l = 2032
        m = 2043
        n = 2054
        o = 2065
        p = 2076

        while i in range(1998, 2009) and j in range(2009, 2020) and k in range(2020, 2031) and l in range(2031, 2042) and m in range (2042, 2053) and n in range(2053, 5064) and o in range(2064, 2075) and p in range(2075, 2089):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1   

                                        ###########################################
                                        #Tota DAF_Parts 6:

        i = 2087
        j = 2098
        k = 2109
        l = 2120
        m = 2131
        n = 2142
        o = 2153
        p = 2164

        while i in range(2086, 2097) and j in range(2097, 2108) and k in range(2108, 2119) and l in range(2119, 2130) and m in range (2130, 2141) and n in range(2141, 2152) and o in range(2152, 2163) and p in range(2163, 2174):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1                 

                                        ###########################################
                                        #Tota DAF_Labour 1:

        i = 2175
        j = 2186
        k = 2197
        l = 2208
        m = 2219
        n = 2230
        o = 2241
        p = 2252

        while i in range(2174, 2185) and j in range(2185, 2196) and k in range(2196, 2207) and l in range(2207, 2218) and m in range (2218, 2229) and n in range(2229, 2240) and o in range(2240, 2251) and p in range(2251, 2262):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1 

                                        ###########################################
                                        #Tota DAF_Labour 2:

        i = 2351
        j = 2362
        k = 2373
        l = 2384
        m = 2395
        n = 2407
        o = 2418
        p = 2429

        while i in range(2350, 2361) and j in range(2361, 2372) and k in range(2372, 2383) and l in range(2383, 2394) and m in range (2394, 2406) and n in range(2406, 2417) and o in range(2417, 2428) and p in range(2428, 2439):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        #Tota DAF_Labour 3:

        i = 2175
        j = 2186
        k = 2197
        l = 2208
        m = 2219
        n = 2230
        o = 2241
        p = 2252

        while i in range(2174, 2185) and j in range(2185, 2196) and k in range(2196, 2207) and l in range(2207, 2218) and m in range (2218, 2229) and n in range(2229, 2240) and o in range(2240, 2251) and p in range(2251, 2262):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1 

                                        ###########################################
                                        

        i = 2263
        j = 2274
        k = 2285
        l = 2296
        m = 2307
        n = 2318
        o = 2329
        p = 2340

        while i in range(2262, 2273) and j in range(2273, 2284) and k in range(2284, 2295) and l in range(2295, 2306) and m in range (2306, 2317) and n in range(2317, 2328) and o in range(2328, 2339) and p in range(2339, 2350):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        

        i = 2440
        j = 2451
        k = 2462
        l = 2473
        m = 2484
        n = 2495
        o = 2506
        p = 2517

        while i in range(2439, 2450) and j in range(2450, 2461) and k in range(2461, 2472) and l in range(2472, 2483) and m in range (2483, 2494) and n in range(2494, 2505) and o in range(2505, 2516) and p in range(2516, 2528):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        

        i = 2528
        j = 2539
        k = 2550
        l = 2561
        m = 2572
        n = 2583
        o = 2594
        p = 2605

        while i in range(2527, 2538) and j in range(2538, 2549) and k in range(2549, 2560) and l in range(2560, 2571) and m in range (2571, 2582) and n in range(2582, 2593) and o in range(2593, 2604) and p in range(2604, 2616):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  

                                        ###########################################
                                        

        i = 2616
        j = 2627
        k = 2638
        l = 2649
        m = 2660
        n = 2671
        o = 2682
        p = 2693

        while i in range(2615, 2626) and j in range(2626, 2637) and k in range(2637, 2648) and l in range(2648, 2659) and m in range (2659, 2670) and n in range(2670, 2681) and o in range(2681, 2692) and p in range(2692, 2703):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1 

                                        ###########################################
                                        

        i = 2704
        j = 2715
        k = 2726
        l = 2737
        m = 2748
        n = 2759
        o = 2770
        p = 2781

        while i in range(2703, 2714) and j in range(2714, 2725) and k in range(2725, 2736) and l in range(2736, 2747) and m in range (2747, 2758) and n in range(2758, 2769) and o in range(2769, 2781) and p in range(2781, 2791):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1 


                                        ###########################################
                                        

        i = 2792
        j = 2803
        k = 2815
        l = 2826
        m = 2837
        n = 2848
        o = 2911
        p = 2900

        while i in range(2791, 2802) and j in range(2802, 2813) and k in range(2814, 2825) and l in range(2825, 2836) and m in range (2836, 2847) and n in range(2847, 2858) and o in range(2910, 2921) and p in range(2899, 2910):
                
            x["CalculationShort_Input" + str(p)] =  float(x["CalculationShort_Input" + str(i)]) + float(x["CalculationShort_Input" + str(j)]) + float(x["CalculationShort_Input" + str(k)]) + float(x["CalculationShort_Input" + str(l)]) + float(x["CalculationShort_Input" + str(m)]) + float(x["CalculationShort_Input" + str(n)]) + float(x["CalculationShort_Input" + str(o)])   

            i +=  1                                                                     
            j +=  1
            k +=  1            
            l +=  1
            m +=  1
            n +=  1
            o +=  1
            p +=  1  


                                ###########################################
        #Total Parts Y1:

        i = 1559
        j = 1570
        k = 1581
        l = 1592
        m = 1603
        n = 1614
        o = 1625
        p = 1636

        input_1 = 1569
        input_2 = 1580
        input_3 = 1591
        input_4 = 1602
        input_5 = 1613
        input_6 = 1624
        input_7 = 1635
        input_8 = 1646

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1558, 1569) and j in range(1569, 1580) and k in range(1580, 1591) \
            and l in range(1591, 1602) and m in range(1602, 1613) and n in range(1613, 1624) and o\
                in range(1624, 1635) and p in range(1635, 1646):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)  
            print(round(sum(total_p),3))          

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1    

                                ###########################################
        #Total parts Y2
        i = 1647
        j = 1658
        k = 1669
        l = 1680
        m = 1691
        n = 1702
        o = 1713
        p = 1724

        input_1 = 1657
        input_2 = 1668
        input_3 = 1679
        input_4 = 1690
        input_5 = 1701
        input_6 = 1712
        input_7 = 1723
        input_8 = 1734

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1646, 1657) and j in range(1657, 1668) and k in range(1668, 1679) \
            and l in range(1679, 1690) and m in range(1690, 1701) and n in range(1701, 1712) and o\
                in range(1712, 1723) and p in range(1723, 1734):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1                                    

                                ###########################################
        #Total parts Y3  
        i = 1735
        j = 1746
        k = 1757
        l = 1769
        m = 1779
        n = 1790
        o = 1801
        p = 1812

        input_1 = 1745
        input_2 = 1756
        input_3 = 1767
        input_4 = 1778
        input_5 = 1789
        input_6 = 1800
        input_7 = 1811
        input_8 = 1822

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1734, 1745) and j in range(1745, 1756) and k in range(1756, 1767) \
            and l in range(1768, 1778) and m in range(1778, 1789) and n in range(1789, 1800) and o\
                in range(1800, 1811) and p in range(1811, 1822):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1                               

                                ###########################################
        #Total parts Y4  
        i = 1823
        j = 1834
        k = 1845
        l = 1856
        m = 1867
        n = 1878
        o = 1889
        p = 1900

        input_1 = 1833
        input_2 = 1844
        input_3 = 1855
        input_4 = 1866
        input_5 = 1877
        input_6 = 1888
        input_7 = 1899
        input_8 = 1910

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1822, 1833) and j in range(1833, 1844) and k in range(1844, 1855) \
            and l in range(1855, 1866) and m in range(1866, 1877) and n in range(1877, 1888) and o\
                in range(1888, 1899) and p in range(1899, 1910):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1  

                                ###########################################
        #Total parts Y5  
        i = 1911
        j = 1922
        k = 1933
        l = 1944
        m = 1955
        n = 1966
        o = 1977
        p = 1988

        input_1 = 1921
        input_2 = 1932
        input_3 = 1943
        input_4 = 1954
        input_5 = 1965
        input_6 = 1976
        input_7 = 1987
        input_8 = 1998

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1910, 1921) and j in range(1921, 1930) and k in range(1932, 1943) \
            and l in range(1943, 1954) and m in range(1954, 1965) and n in range(1965, 1976) and o\
                in range(1976, 1987) and p in range(1987, 1998):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1  

                                ###########################################
        #Total labour hours Y1 
        i = 1999
        j = 2010
        k = 2021
        l = 2032
        m = 2043
        n = 2054
        o = 2065
        p = 2076

        input_1 = 2009
        input_2 = 2020
        input_3 = 2031
        input_4 = 2042
        input_5 = 2053
        input_6 = 2064
        input_7 = 2075
        input_8 = 2086

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(1998, 2009) and j in range(2009, 2020) and k in range(2020, 2031) \
            and l in range(2031, 2042) and m in range(2042, 2053) and n in range(2053, 2064) and o\
                in range(2064, 2075) and p in range(2075, 2086):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1   

                                ###########################################
        #Total labour hours Y2 
        i = 2087
        j = 2098
        k = 2109
        l = 2120
        m = 2131
        n = 2142
        o = 2153
        p = 2164

        input_1 = 2097
        input_2 = 2108
        input_3 = 2119
        input_4 = 2130
        input_5 = 2141
        input_6 = 2152
        input_7 = 2163
        input_8 = 2174

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2086, 2097) and j in range(2097, 2108) and k in range(2108, 2119) \
            and l in range(2119, 2130) and m in range(2130, 2141) and n in range(2141, 2152) and o\
                in range(2152, 2163) and p in range(2163, 2174):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1  

                                ###########################################
        #Total labour hours Y3 
        i = 2175
        j = 2186
        k = 2197
        l = 2208
        m = 2219
        n = 2230
        o = 2241
        p = 2252

        input_1 = 2185
        input_2 = 2196
        input_3 = 2207
        input_4 = 2218
        input_5 = 2229
        input_6 = 2240
        input_7 = 2251
        input_8 = 2262

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2174, 2185) and j in range(2185, 2196) and k in range(2196, 2207) \
            and l in range(2207, 2216) and m in range(2218, 2229) and n in range(2229, 2240) and o\
                in range(2240, 2251) and p in range(2251, 2262):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3) 

            x["CalculationShort_Input2262"] =  float(x["CalculationShort_Input2252"]) + float(x["CalculationShort_Input2253"]) + float(x["CalculationShort_Input2254"]) + float(x["CalculationShort_Input2255"]) + float(x["CalculationShort_Input2256"]) + float(x["CalculationShort_Input2257"]) + float(x["CalculationShort_Input2258"])  + float(x["CalculationShort_Input2259"])+ float(x["CalculationShort_Input2260"])+ float(x["CalculationShort_Input2261"])
            x["CalculationShort_Input2229"] =  float(x["CalculationShort_Input2219"]) + float(x["CalculationShort_Input2220"]) + float(x["CalculationShort_Input2221"]) + float(x["CalculationShort_Input2222"]) + float(x["CalculationShort_Input2223"]) + float(x["CalculationShort_Input2224"]) + float(x["CalculationShort_Input2225"])  + float(x["CalculationShort_Input2226"])+ float(x["CalculationShort_Input2227"])+ float(x["CalculationShort_Input2228"])         

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1   

                                ###########################################
        #Total labour hours Y4
        i = 2263
        j = 2274
        k = 2285
        l = 2296
        m = 2307
        n = 2318
        o = 2329
        p = 2340

        input_1 = 2273
        input_2 = 2284
        input_3 = 2295
        input_4 = 2306
        input_5 = 2317
        input_6 = 2328
        input_7 = 2339
        input_8 = 2350

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2262, 2273) and j in range(2273, 2284) and k in range(2284, 2295) \
            and l in range(2295, 2306) and m in range(2306, 2317) and n in range(2317, 2328) and o\
                in range(2328, 2339) and p in range(2339, 2350):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)           
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1 

                                ###########################################
        #Total labour hours Y5
        i = 2351
        j = 2362
        k = 2373
        l = 2384
        m = 2395
        n = 2407
        o = 2418
        p = 2429

        input_1 = 2361
        input_2 = 2372
        input_3 = 2383
        input_4 = 2394
        input_5 = 2406
        input_6 = 2417
        input_7 = 2428
        input_8 = 2439

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2350, 2361) and j in range(2361, 2372) and k in range(2372, 2383) \
            and l in range(2383, 2394) and m in range(2394, 2406) and n in range(2406, 2417) and o\
                in range(2417, 2428) and p in range(2428, 2439):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)           
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) ,3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1 

                                ###########################################
        #Total Oil Y1
        i = 2440
        j = 2451
        k = 2462
        l = 2473
        m = 2484
        n = 2495
        o = 2506
        p = 2517

        input_1 = 2450
        input_2 = 2461
        input_3 = 2472
        input_4 = 2483
        input_5 = 2494
        input_6 = 2505
        input_7 = 2516
        input_8 = 2527

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2439, 2450) and j in range(2450, 2461) and k in range(2461, 2472) \
            and l in range(2472, 2483) and m in range(2483, 2494) and n in range(2494, 2505) and o\
                in range(2505, 2516) and p in range(2516, 2527):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j) ,3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) ,3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p) ,3)           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1

        #Total Oil Y2
        i = 2528
        j = 2539
        k = 2550
        l = 2561
        m = 2572
        n = 2583
        o = 2594
        p = 2605

        input_1 = 2538
        input_2 = 2549
        input_3 = 2560
        input_4 = 2571
        input_5 = 2582
        input_6 = 2593
        input_7 = 2604
        input_8 = 2615

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2527, 2538) and j in range(2538, 2549) and k in range(2549, 2560) \
            and l in range(2560, 2571) and m in range(2571, 2582) and n in range(2582, 2593) and o\
                in range(2593, 2604) and p in range(2604, 2615):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1 

        #Total Oil Y3
        i = 2616
        j = 2627
        k = 2638
        l = 2649
        m = 2660
        n = 2671
        o = 2682
        p = 2693

        input_1 = 2626
        input_2 = 2637
        input_3 = 2648
        input_4 = 2659
        input_5 = 2670
        input_6 = 2681
        input_7 = 2692
        input_8 = 2703

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2615, 2626) and j in range(2626, 2637) and k in range(2637, 2648) \
            and l in range(2648, 2659) and m in range(2659, 2670) and n in range(2670, 2681) and o\
                in range(2681, 2692) and p in range(2692, 2703):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)          

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1   

        #Total Oil Y4
        i = 2704
        j = 2715
        k = 2726
        l = 2737
        m = 2748
        n = 2759
        o = 2770
        p = 2781

        input_1 = 2714
        input_2 = 2725
        input_3 = 2736
        input_4 = 2747
        input_5 = 2758
        input_6 = 2769
        input_7 = 2780
        input_8 = 2791

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2703, 2714) and j in range(2714, 2725) and k in range(2725, 2736) \
            and l in range(2736, 2747) and m in range(2747, 2758) and n in range(2758, 2769) and o\
                in range(2769, 2780) and p in range(2780, 2791):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1    

        #Total Oil Y5
        i = 2792
        j = 2803
        k = 2815
        l = 2826
        m = 2837
        n = 2848
        o = 2911
        p = 2900

        input_1 = 2802
        input_2 = 2813
        input_3 = 2825
        input_4 = 2836
        input_5 = 2847
        input_6 = 2858
        input_7 = 2921
        input_8 = 2910

        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        total_p = []        

        while i in range(2791, 2802) and j in range(2802, 2813) and k in range(2814, 2825) \
            and l in range(2825, 2836) and m in range(2836, 2847) and n in range(2847, 2858) and o\
                in range(2910, 2921) and p in range(2889, 2910):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))
            total_p.append(float(x['CalculationShort_Input' + str(p)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
            x['CalculationShort_Input' + str(input_8)] = round(sum(total_p),3)            

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1
            p += 1    


        #1. Basic year park
        i = 1
        j = 12
        k = 23
        l = 34
        m = 45
        n = 56
        o = 67


        input_1 = 11
        input_2 = 22
        input_3 = 33
        input_4 = 44
        input_5 = 55
        input_6 = 66
        input_7 = 77


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(0, 11) and j in range(11, 22) and k in range(22, 33) \
            and l in range(33, 44) and m in range(44, 55) and n in range(55, 66) and o\
                in range(66, 77):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))



            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1


        # Second Year park
        i = 89
        j = 100
        k = 111
        l = 122
        m = 133
        n = 144
        o = 155


        input_1 = 99
        input_2 = 110
        input_3 = 121
        input_4 = 132
        input_5 = 143
        input_6 = 154
        input_7 = 165


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(88, 99) and j in range(99, 110) and k in range(110, 121) \
            and l in range(121, 132) and m in range(132, 143) and n in range(143, 154) and o\
                in range(154, 165):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1 

         # Third Year park
        i = 89
        j = 100
        k = 111
        l = 122
        m = 133
        n = 144
        o = 155


        input_1 = 99
        input_2 = 110
        input_3 = 121
        input_4 = 132
        input_5 = 143
        input_6 = 154
        input_7 = 165


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(88, 99) and j in range(99, 110) and k in range(110, 121) \
            and l in range(121, 132) and m in range(132, 143) and n in range(143, 154) and o\
                in range(154, 165):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1  


         # Fourth Year park
        i = 255
        j = 266
        k = 277
        l = 288
        m = 299
        n = 310
        o = 321


        input_1 = 265
        input_2 = 276
        input_3 = 287
        input_4 = 298
        input_5 = 309
        input_6 = 320
        input_7 = 331


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(254, 265) and j in range(265, 276) and k in range(276, 287) \
            and l in range(287, 298) and m in range(298, 309) and n in range(309, 320) and o\
                in range(320, 331):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))

            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1   

         # Fifth Year park
        i = 832
        j = 843
        k = 854
        l = 865
        m = 876
        n = 887
        o = 898


        input_1 = 842
        input_2 = 853
        input_3 = 864
        input_4 = 875
        input_5 = 886
        input_6 = 897
        input_7 = 908


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(831, 842) and j in range(842, 853) and k in range(853, 864) \
            and l in range(864, 875) and m in range(875, 886) and n in range(886, 897) and o\
                in range(897, 906):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))



            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round((sum(total_m) + x['CalculationShort_Input884'] + x['CalculationShort_Input885']  ),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1    

        i = 178
        j = 189
        k = 200
        l = 211
        m = 222
        n = 233
        o = 244


        input_1 = 188
        input_2 = 199
        input_3 = 210
        input_4 = 221
        input_5 = 232
        input_6 = 243
        input_7 = 254


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(177, 188) and j in range(188, 199) and k in range(199, 210) \
            and l in range(210, 221) and m in range(221, 232) and n in range(232, 243) and o\
                in range(243, 254):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n),3)          
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1                                                                                                                                                                        

                           ######################################################

        # 1
        i = 909
        j = 925
        k = 941
        l = 957
        m = 973
        n = 989
        o = 1005


        input_1 = 924
        input_2 = 940
        input_3 = 956
        input_4 = 972
        input_5 = 988
        input_6 = 1004
        input_7 = 1020


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(908, 924) and j in range(924, 940) and k in range(940, 956) \
            and l in range(956, 972) and m in range(972, 988) and n in range(987, 1004) and o\
                in range(1004, 1020):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round((sum(total_i) / len(total_i)),2)
            x['CalculationShort_Input' + str(input_2)] = round((sum(total_j) / len(total_j)),2)          
            x['CalculationShort_Input' + str(input_3)] = round((sum(total_k) / len(total_k)),2)
            x['CalculationShort_Input' + str(input_4)] = round((sum(total_l) / len(total_l)),2)
            x['CalculationShort_Input' + str(input_5)] = round((sum(total_m) / len(total_m)),2)
            x['CalculationShort_Input' + str(input_6)] = round((sum(total_n) / len(total_n)),2)          
            x['CalculationShort_Input' + str(input_7)] = round((sum(total_o) / len(total_o)),2)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1  

        # 2
        i = 1037
        j = 1053
        k = 1068
        l = 1084
        m = 1101
        n = 1117
        o = 1134


        input_1 = 1052
        input_2 = 1067
        input_3 = 1083
        input_4 = 1100
        input_5 = 1116
        input_6 = 1133
        input_7 = 1149


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(1036, 1052) and j in range(1052, 1067) and k in range(1067, 1083) \
            and l in range(1083, 1095) and m in range(1100, 1116) and n in range(1116, 1133) and o\
                in range(1133, 1149):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i) / len(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j) / len(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k) / len(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l) / len(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m) / len(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) / len(total_n),3)         
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o) / len(total_o),3)
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1 

        # 3
        #i = 1166
        #j = 1183
        #k = 1201
        #l = 1217
        #m = 1233
        #n = 1249
        #o = 1265


        #input_1 = 1181
        #input_2 = 1198
        #input_3 = 1216
        #input_4 = 1232
        #input_5 = 1248
        #input_6 = 1264
        #input_7 = 1280


        #total_i = []
        #total_j = []
        #total_k = []
        #total_l = []
        #total_m = []
        #total_n = []
        #total_o = []
        

        #while i in range(1165, 1181) and j in range(1182, 1198) and k in range(1200, 1216) \
            #and l in range(1216, 1232) and m in range(1232, 1248) and n in range(1248, 1264) and o\
               # in range(1264, 1280):
            
            #total_i.append(float(x['CalculationShort_Input' + str(i)]))
            #total_j.append(float(x['CalculationShort_Input' + str(j)]))
            #total_k.append(float(x['CalculationShort_Input' + str(k)]))
            #total_l.append(float(x['CalculationShort_Input' + str(l)]))
            #total_m.append(float(x['CalculationShort_Input' + str(m)]))
            #total_n.append(float(x['CalculationShort_Input' + str(n)]))
            #total_o.append(float(x['CalculationShort_Input' + str(o)]))


            #x['CalculationShort_Input' + str(input_1)] = round(sum(total_i) / len(total_i),3)
            #x['CalculationShort_Input' + str(input_2)] = round(sum(total_j) / len(total_j),3)          
            #x['CalculationShort_Input' + str(input_3)] = round(sum(total_k) / len(total_k),3)
            #x['CalculationShort_Input' + str(input_4)] = round(sum(total_l) / len(total_l),3)
            #x['CalculationShort_Input' + str(input_5)] = round(sum(total_m) / len(total_m),3)
            #x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) / len(total_n),3)         
            #x['CalculationShort_Input' + str(input_7)] = round(sum(total_o) / len(total_o),3)
           

           # i += 1
            #j += 1
            #k += 1
            #l += 1
            #m += 1
            #n += 1
            #o += 1    

        # 4
        i = 1297
        j = 1313
        k = 1329
        l = 1345
        m = 1361
        n = 1377
        o = 1393


        input_1 = 1312
        input_2 = 1328
        input_3 = 1344
        input_4 = 1360
        input_5 = 1376
        input_6 = 1392
        input_7 = 1408


        total_i = []
        total_j = []
        total_k = []
        total_l = []
        total_m = []
        total_n = []
        total_o = []
        

        while i in range(1296, 1312) and j in range(1312, 1328) and k in range(1328, 1344) \
            and l in range(1344, 1360) and m in range(1360, 1374) and n in range(1376, 1392) and o\
                in range(1392, 1408):
            
            total_i.append(float(x['CalculationShort_Input' + str(i)]))
            total_j.append(float(x['CalculationShort_Input' + str(j)]))
            total_k.append(float(x['CalculationShort_Input' + str(k)]))
            total_l.append(float(x['CalculationShort_Input' + str(l)]))
            total_m.append(float(x['CalculationShort_Input' + str(m)]))
            total_n.append(float(x['CalculationShort_Input' + str(n)]))
            total_o.append(float(x['CalculationShort_Input' + str(o)]))


            x['CalculationShort_Input' + str(input_1)] = round(sum(total_i) +  x['CalculationShort_Input1310'] +  x['CalculationShort_Input1311'] - 1 ,3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j) +  x['CalculationShort_Input1326'] +  x['CalculationShort_Input1327'] + 1 ,3)        
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k) +  x['CalculationShort_Input1342'] +  x['CalculationShort_Input1343'] + 1 ,3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l) +  x['CalculationShort_Input1358'] +  x['CalculationShort_Input1359'] - 3 ,3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m) +  x['CalculationShort_Input1374'] +  x['CalculationShort_Input1375'] ,3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) +  x['CalculationShort_Input1390'] +  x['CalculationShort_Input1391'] ,3)      
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o) +  x['CalculationShort_Input1406'] +  x['CalculationShort_Input1407'] - 1 ,3)

            

            '''x['CalculationShort_Input' + str(input_1)] = round(sum(total_i) / len(total_i),3)
            x['CalculationShort_Input' + str(input_2)] = round(sum(total_j) / len(total_j),3)          
            x['CalculationShort_Input' + str(input_3)] = round(sum(total_k) / len(total_k),3)
            x['CalculationShort_Input' + str(input_4)] = round(sum(total_l) / len(total_l),3)
            x['CalculationShort_Input' + str(input_5)] = round(sum(total_m) / len(total_m),3)
            x['CalculationShort_Input' + str(input_6)] = round(sum(total_n) / len(total_n),3)         
            x['CalculationShort_Input' + str(input_7)] = round(sum(total_o) / len(total_o),3)'''
           

            i += 1
            j += 1
            k += 1
            l += 1
            m += 1
            n += 1
            o += 1       

                                                                    


        current_db.calculationshorts.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.calculationshorts.find_one({"GlobalId": "global"})
    return redirect(url_for('calculationshorts.calculationshorts')) 
    return render_template("calculation-short.html", data=x)  




####################################################################################

@calculationshorts_bp.route('/calculationshorts/delete',  methods=['POST'])
@login_required
def calculationshorts_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()  
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.calculationshorts.delete_many({})
    return redirect(url_for('calculationshorts.calculationshorts'))    
    return render_template("calculation-short.html", data=x)  