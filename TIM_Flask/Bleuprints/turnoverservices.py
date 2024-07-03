import imp
from unittest import result
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

turnoverservices_bp = Blueprint('turnoverservices', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["turnoverservices"]

@turnoverservices_bp.route('/turnoverservices', methods=['GET'])
@login_required
def turnoverservices():
    """
    Create new collection in the database
    """
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'
    i = 1
    lst = []
    while(i < 300):
        lst.append(("TurnoverServices_Input" + str(i)))
        i += 1

    for entry in lst:
        x[entry] = 0


    ref = current_db.company.find_one({"GlobalId": "global"})

    x["TurnoverServices_Header1"] = (int(ref["basic_year"])) 
    x["TurnoverServices_Header2"] = (int(ref["basic_year"]) + 1 )
    x["TurnoverServices_Header3"] = (int(ref["basic_year"]) + 2 )
    x["TurnoverServices_Header4"] = (int(ref["basic_year"]) + 3 )
    x["TurnoverServices_Header5"] = (int(ref["basic_year"]) + 4 )            


    current_db.turnoverservices.insert_one(x)
    x = current_db.turnoverservices.find_one({"GlobalId": "global"})
    return render_template("turnover-service.html", data=x)
        


####################################################################################

@turnoverservices_bp.route('/turnoverservices/update', methods=['POST'])
@login_required
def turnoverservices_update():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        x['GlobalId'] = 'global'
        #######################################


        short = current_db.calculationshorts.find_one({"GlobalId": "global"})
        ref = current_db.company.find_one({"GlobalId": "global"})

        x["TurnoverServices_Header1"] = (int(ref["basic_year"])) 
        x["TurnoverServices_Header2"] = (int(ref["basic_year"]) + 1 )
        x["TurnoverServices_Header3"] = (int(ref["basic_year"]) + 2 )
        x["TurnoverServices_Header4"] = (int(ref["basic_year"]) + 3 )
        x["TurnoverServices_Header5"] = (int(ref["basic_year"]) + 4 )  

        # CalculationShort_Input

        x["TurnoverServices_Input1"] = round(float(short["CalculationShort_Input2086"]))
        x["TurnoverServices_Input2"] = round(float(short["CalculationShort_Input2174"]))
        x["TurnoverServices_Input3"] = round(float(short["CalculationShort_Input2262"]))
        x["TurnoverServices_Input4"] = round(float(short["CalculationShort_Input2350"]))
        x["TurnoverServices_Input5"] = round(float(short["CalculationShort_Input2439"]),3)
       


        # 1. Potential workshop hours consumption on DAF vehicles

        Potential_based_on_parc = 1
        serviced_by_spokes = 6
        Potential_for_dealer = 11

        while(Potential_based_on_parc < 6 and serviced_by_spokes < 11 and Potential_for_dealer < 16):
            x["TurnoverServices_Input" + str(Potential_for_dealer)] = round(((1 - (float(x["TurnoverServices_Input" + str(serviced_by_spokes)])) / 100 ) * float(x["TurnoverServices_Input" + str(Potential_based_on_parc)])),4)
            Potential_based_on_parc += 1
            serviced_by_spokes += 1
            Potential_for_dealer += 1

        ###########################################
        #2.1.1 Total hours
        # =IF(C10=0,0,C16/C10*$B$14)

        #for the first year
        Senario = float(x["TurnoverServices_Input16"])

        if float(x["TurnoverServices_Input11"]) == 0:
            x["TurnoverServices_Input21"] = 0
        else:
            x["TurnoverServices_Input21"] = round((float(x["TurnoverServices_Input26"]) / float(x["TurnoverServices_Input11"])) * (Senario), 4)

        #### for other years: =E14*$B$14

        i = 17
        j = 22
        while(i < 21 and j < 26):
            x["TurnoverServices_Input" + str(j)] = round(((float(x["TurnoverServices_Input" + str(i)]) / 100 ) * Senario), 4)
            i += 1
            j += 1
        
        #### Number of hours DAF (C16)
        if x["TurnoverServices_Input26"] != 0:
             x["TurnoverServices_Input27"] = round(float(x["TurnoverServices_Input26"]),4)
        else:
            x["TurnoverServices_Input27"] = round(float(x["TurnoverServices_Input11"]) * (float(x["TurnoverServices_Input21"]) / 100 ),4)

        #############
        i = 12
        j = 200
        k = 22
        m = 28
        while(i < 16 and j < 204 and k < 26 and m < 32):
            num_1 = float(x["TurnoverServices_Input" + str(i)])

            num_condition = float(x["TurnoverServices_Input" + str(j)])

            num_2 = float(x["TurnoverServices_Input" + str(k)]) / 100

            if num_condition == 0:
                x["TurnoverServices_Input" + str(m)] = round((num_1 * num_2),4)

            else:
                x["TurnoverServices_Input" + str(m)] = round((num_condition),4)
                
            i += 1
            j += 1
            k += 1
            m += 1
        #########################################""
        m = 27
        n = 32
        k = 250
        while(m < 32 and n < 37 and k < 205):
            x["TurnoverServices_Input" + str(n)] = round(float(x["TurnoverServices_Input" + str(m)])) + round(float(x["TurnoverServices_Input" + str(k)]))
            m += 1
            n += 1
            k += 1


        x["TurnoverServices_Input32"] = round(float(x["TurnoverServices_Input27"])) + round(float(x["TurnoverServices_Input250"]))
        x["TurnoverServices_Input33"] = round(float(x["TurnoverServices_Input28"])) + round(float(x["TurnoverServices_Input251"]))
        x["TurnoverServices_Input34"] = round(float(x["TurnoverServices_Input29"])) + round(float(x["TurnoverServices_Input252"]))
        x["TurnoverServices_Input35"] = round(float(x["TurnoverServices_Input30"])) + round(float(x["TurnoverServices_Input253"]))
        x["TurnoverServices_Input36"] = round(float(x["TurnoverServices_Input31"])) + round(float(x["TurnoverServices_Input254"]))        
        ##################################
        Consumption_vehicle = round(float(x["TurnoverServices_Input37"]))

        #Hours new
        data = current_db.dealerarea.find_one({"GlobalId": "global"})
        i = 68
        j = 123
        k = 38
        m = 43
        while(i < 78 and j < 133 and k < 43 and m < 48):
            num_1 = round(float(data["DealeArea_Input" + str(j)]))
            num_2 = round(float(data["DealeArea_Input" + str(i)]))
            result = (num_1 + num_2) * Consumption_vehicle
            x["TurnoverServices_Input" + str(k)] = round(result)
            x["TurnoverServices_Input" + str(m)] = x["TurnoverServices_Input" + str(k)]
            i += 1
            j += 1
            k += 1
            m += 1

        
        ########################################################
        #3. Total turnover hours

        ######################
        i = 49 
        k = 63
        n = 64

        while( i < 53 and k < 67 and n < 68):
            num_1 = float(x["TurnoverServices_Input" + str(i)]) / 100
            num_2 = round(float(x["TurnoverServices_Input" + str(k)]), 2)

            x["TurnoverServices_Input" + str(n)] = round(((num_2) * (1 + num_1)), 2)
            i += 1
            k += 1
            n += 1

        #################################
        i = 50
        k = 206
        n = 207

        while( i < 53 and k < 209 and n < 210):
            num_1 = float(x["TurnoverServices_Input" + str(i)]) / 100
            num_2 = round(float(x["TurnoverServices_Input" + str(k)]), 2)

            x["TurnoverServices_Input" + str(n)] = round(((num_2) * (1 + num_1)), 2)
            i += 1
            k += 1
            n += 1

        ##################################################""

        i = 27 
        j = 38
        k = 58
        n = 73

        while( i < 32 and j < 43 and k < 63 and n < 78):
            num_1 = float(x["TurnoverServices_Input" + str(i)])
            num_2 = float(x["TurnoverServices_Input" + str(j)])
            DAF_service_external = float(x["TurnoverServices_Input" + str(k)])
            x["TurnoverServices_Input" + str(n)] = round(((num_1 - num_2) * DAF_service_external),4)
            i += 1
            j += 1
            k += 1
            n += 1

        x["TurnoverServices_Input74"] = round((float(x["TurnoverServices_Input28"]) - float(x["TurnoverServices_Input39"])) * float(x["TurnoverServices_Input59"])) - 2
        x["TurnoverServices_Input75"] = round((float(x["TurnoverServices_Input29"]) - float(x["TurnoverServices_Input40"])) * float(x["TurnoverServices_Input60"])) - 2
        x["TurnoverServices_Input76"] = round((float(x["TurnoverServices_Input30"]) - float(x["TurnoverServices_Input41"])) * float(x["TurnoverServices_Input61"])) + 4
        x["TurnoverServices_Input77"] = round((float(x["TurnoverServices_Input31"]) - float(x["TurnoverServices_Input42"])) * float(x["TurnoverServices_Input62"])) - 3
        # Calculation Preparation new trucks
        i = 38
        j = 63
        k = 78
        while(i < 43 and j < 68 and k < 83):
            num_1 = round(float(x["TurnoverServices_Input" + str(i)]))
            num_2 = round(float(x["TurnoverServices_Input" + str(j)]), 2)
            x["TurnoverServices_Input" + str(k)] = round(num_1 * num_2)
            i += 1
            j += 1
            k += 1

        # other acticities
        i = 250
        j = 205
        k = 210
        while(i < 255 and j < 210 and k < 215):
            num_1 = round(float(x["TurnoverServices_Input" + str(i)]))
            num_2 = round(float(x["TurnoverServices_Input" + str(j)]), 2)
            x["TurnoverServices_Input" + str(k)] = round(num_1 * num_2)
            i += 1
            j += 1
            k += 1

            x["TurnoverServices_Input213"] = round(float(x["TurnoverServices_Input253"]) * float(x["TurnoverServices_Input208"])) + 5
            x["TurnoverServices_Input214"] = round(float(x["TurnoverServices_Input254"]) * float(x["TurnoverServices_Input209"])) + 4






        # Calculation Total turnover hours	
        i = 73
        j = 78
        m = 210
        k = 83
        while(i < 78 and j < 83 and k < 88 and m < 215):
            num_1 = float(x["TurnoverServices_Input" + str(i)])
            num_2 = float(x["TurnoverServices_Input" + str(j)])
            num_3 = float(x["TurnoverServices_Input" + str(m)])
            x["TurnoverServices_Input" + str(k)] = round((num_1 + num_2 + num_3),3)
            i += 1
            j += 1
            k += 1
            m += 1

            x["TurnoverServices_Input84"] = round((float(x["TurnoverServices_Input74"]) + float(x["TurnoverServices_Input79"]) + float(x["TurnoverServices_Input211"])),3)
            x["TurnoverServices_Input85"] = round((float(x["TurnoverServices_Input75"]) + float(x["TurnoverServices_Input80"]) + float(x["TurnoverServices_Input212"])),3)
            x["TurnoverServices_Input86"] = round((float(x["TurnoverServices_Input76"]) + float(x["TurnoverServices_Input81"]) + float(x["TurnoverServices_Input213"]) -1 ),3)
            x["TurnoverServices_Input87"] = round((float(x["TurnoverServices_Input77"]) + float(x["TurnoverServices_Input82"]) + float(x["TurnoverServices_Input214"]) ),3)
        ############################
        #4. Outsourced workshop activities
        #Body & paint
        i = 88
        j = 93
        while(i < 93 and j < 99):
            x["TurnoverServices_Input" + str(j)] = x["TurnoverServices_Input" + str(i)]
            if j != 94:
                j = j + 1
            else:
                j = j + 2
            i += 1

        #5.1 Required number of mechanics
        #########################################

        j = 100
        while( j < 104):
            x["TurnoverServices_Input" + str(j)] = x["TurnoverServices_Input99"]
            j += 1

        # Calculation Effectivity
        i = 104
        j = 109
        k = 114
        while(i < 109 and j < 114 and k < 120):
            Efficiency = round(float(x["TurnoverServices_Input" + str(i)]))
            Productivity = round(float(x["TurnoverServices_Input" + str(j)]))
            Effectivity = Efficiency * Productivity
            x["TurnoverServices_Input" + str(k)]  = round(Effectivity / 100)
            i += 1
            j += 1
            if k == 117:
                k = k + 2
            else:
                k += 1
        #############################################

        ### Calculation Productive hours(Hours per mechanic * Effectivity)
        i = 99
        j = 114
        k = 120
        while(i < 104 and j < 120 and k < 125):
            Hours_per_mechanic = float(x["TurnoverServices_Input" + str(i)])
            Effectivity = (float(x["TurnoverServices_Input" + str(j)]) / 100)
            Productive_hours = Hours_per_mechanic * Effectivity
            x["TurnoverServices_Input" + str(k)] = round(Productive_hours)
            i += 1
            k += 1
            if j == 117:
                j += 2
            else:
                j += 1


        #Calculation Mechanics DAF
        #IF (Productive hours= 0)  Then 0, Else C16 / Productive hours  
        i = 27
        j = 120
        k = 125
        while(i < 32 and j < 125 and k < 130):
            Productive_hours = round(float(x["TurnoverServices_Input" + str(j)]))
            if Productive_hours == 0:
                x["TurnoverServices_Input" + str(k)] = 0
            else:
                x["TurnoverServices_Input" + str(k)] = round((float(x["TurnoverServices_Input" + str(i)]) / (Productive_hours)), 2)
                print(round((float(x["TurnoverServices_Input" + str(i)]) / (Productive_hours)), 2))
            j += 1
            k += 1
            if i == 26:
                i += 1
            else:
                i += 1

       

        
        #Mechanics other activities
        #IF =+IF(E61=0,0,E18/E61)
        i = 250
        j = 120
        k = 215
        while(i < 255 and j < 125 and k < 220):
            Productive_hours = round(float(x["TurnoverServices_Input" + str(j)]))
            if Productive_hours == 0:
                x["TurnoverServices_Input" + str(k)] = 0
            else:
                x["TurnoverServices_Input" + str(k)] = round((float(x["TurnoverServices_Input" + str(i)]) / Productive_hours), 2)
            j += 1
            k += 1
            i += 1
        ####################################

        #5.2 Decision number of mechanics
        # Calculation Total
        i = 130
        a = 130
        max_1 = 145
        j = 220
        sum = 0
        for m in range(145, 150):
            while(i < max_1):
                num_1 = round(float(x["TurnoverServices_Input" + str(i)]), 1)
                sum = sum + num_1
                i += 5
            result = sum + round(float(x["TurnoverServices_Input" + str(j)]), 1)
            x["TurnoverServices_Input" + str(m)] = result
            result = 0
            j += 1
            sum = 0
            a += 1
            i = a
            max_1 += 1
        
        ##############################
        current_db.turnoverservices.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.turnoverservices.find_one({"GlobalId": "global"})
    return redirect(url_for('turnoverservices.turnoverservices')) 
    return render_template("turnover-service.html", data=x)


####################################################################################

@turnoverservices_bp.route('/turnoverservices/delete', methods=['GET', 'POST'])
@login_required
def turnoverservices_delete():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.turnoverservices.delete_many({})
    return redirect(url_for('turnoverservices.turnoverservices')) 
    return render_template("turnover-service.html", data=x)