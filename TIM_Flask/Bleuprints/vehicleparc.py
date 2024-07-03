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

vehicleparc_bp = Blueprint('vehicleparc', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["TIM_Demo"]
collection = db["vehicle"]

@vehicleparc_bp.route('/vehicleparc', methods=['GET'])
@login_required
def vehicle():
    """
    Create a company in the database
    """
    current_db = get_current_db()
    x = {}
    x['GlobalId'] = 'global'

    #needed collections
    ref = current_db.company.find_one({"GlobalId": "global"})
    i = 1
    lst = []
    while(i < 208):
        lst.append(("VehicleParc_Input" + str(i)))
        i += 1

        ref = current_db.company.find_one({"GlobalId": "global"})
        x["VehicleParc_Header1"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header2"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header3"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header4"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header5"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header6"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header7"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header8"] = (int(ref["basic_year"]) + 4 ) 

        x["VehicleParc_Header9"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header10"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header11"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header12"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header13"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header14"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header15"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header16"] = (int(ref["basic_year"]) + 4 ) 


        x["VehicleParc_Header17"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header18"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header19"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header20"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header21"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header22"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header23"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header24"] = (int(ref["basic_year"]) + 4 ) 
        x["VehicleParc_Header25"] = (int(ref["basic_year"]) + 5 ) 
        x["VehicleParc_Header26"] = (int(ref["basic_year"]) + 6 ) 
        x["VehicleParc_Header27"] = (int(ref["basic_year"]) + 7 ) 
        x["VehicleParc_Header28"] = (int(ref["basic_year"]) + 8 )   
        x["VehicleParc_Header29"] = (int(ref["basic_year"]) + 9 ) 
        x["VehicleParc_Header30"] = (int(ref["basic_year"]) + 10 ) 
        x["VehicleParc_Header31"] = (int(ref["basic_year"]) + 11 ) 
        x["VehicleParc_Header32"] = (int(ref["basic_year"]) + 12 )                
        x["VehicleParc_Header33"] = (int(ref["basic_year"]) + 13 ) 
        x["VehicleParc_Header34"] = (int(ref["basic_year"]) + 14 )    

        x["VehicleParc_Header100"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header101"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header102"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header103"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header104"] = (int(ref["basic_year"]) + 4 ) 
        x["VehicleParc_Header105"] = (int(ref["basic_year"]) + 5 ) 
        x["VehicleParc_Header106"] = (int(ref["basic_year"]) + 6 ) 
        x["VehicleParc_Header107"] = (int(ref["basic_year"]) + 7 ) 
        x["VehicleParc_Header108"] = (int(ref["basic_year"]) + 8 )   
        x["VehicleParc_Header109"] = (int(ref["basic_year"]) + 9 ) 
        x["VehicleParc_Header110"] = (int(ref["basic_year"]) + 10 ) 
        x["VehicleParc_Header111"] = (int(ref["basic_year"]) + 11 ) 
        x["VehicleParc_Header112"] = (int(ref["basic_year"]) + 12 )                
        x["VehicleParc_Header113"] = (int(ref["basic_year"]) + 13 ) 
        x["VehicleParc_Header114"] = (int(ref["basic_year"]) + 14 )        

        
        x["VehicleParc_Header200"] = (int(ref["basic_year"]) - 3 )  
        x["VehicleParc_Header201"] = (int(ref["basic_year"]) - 2 ) 
        x["VehicleParc_Header202"] = (int(ref["basic_year"]) - 1 )  
        x["VehicleParc_Header203"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header204"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header205"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header206"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header207"] = (int(ref["basic_year"]) + 4 )               

    print(lst)
    for entry in lst:
        x[entry] = 0
    x["VehicleParc_Input205"] = 0
    x["VehicleParc_Input208"] = 0
    x["VehicleParc_Input209"] = 0
    x["VehicleParc_Input210"] = 0
    x["VehicleParc_Input211"] = 0
    x["VehicleParc_Input212"] = 0
    x["VehicleParc_Input213"] = 0
    x["VehicleParc_Input214"] = 0
    x["VehicleParc_Input215"] = 0
    x["VehicleParc_Input216"] = 0
    x["VehicleParc_Input217"] = 0
    x["VehicleParc_Input218"] = 0  
    x["VehicleParc_Input219"] = 0     
    x["VehicleParc_Input220"] = 0
    x["VehicleParc_Input221"] = 0
    x["VehicleParc_Input222"] = 0    
    x["VehicleParc_Input223"] = 0    
    x["VehicleParc_Input224"] = 0  
    x["VehicleParc_Input225"] = 0
    x["VehicleParc_Input226"] = 0
    x["VehicleParc_Input227"] = 0   
    x["VehicleParc_Input228"] = 0      
    x["VehicleParc_Input229"] = 0     
    x["VehicleParc_Input230"] = 0  
    x["VehicleParc_Input231"] = 0         
    print(x)
    current_db.vehicle.insert_one(x)
    x = current_db.vehicle.find_one({"GlobalId": "global"})
    return render_template("vehicleparc.html", data=x)
 
####################################################################################


@vehicleparc_bp.route('/vehicleparc/update', methods=['POST'])
@login_required
def update_vehicle():
    """
    Update a company in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)

        #needed collections
        ref = current_db.company.find_one({"GlobalId": "global"})
        x["VehicleParc_Header1"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header2"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header3"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header4"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header5"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header6"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header7"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header8"] = (int(ref["basic_year"]) + 4 ) 

        x["VehicleParc_Header9"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header10"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header11"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header12"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header13"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header14"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header15"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header16"] = (int(ref["basic_year"]) + 4 ) 


        x["VehicleParc_Header17"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header18"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header19"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header20"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header21"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header22"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header23"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header24"] = (int(ref["basic_year"]) + 4 )

        x["VehicleParc_Header100"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header101"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header102"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header103"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header104"] = (int(ref["basic_year"]) + 4 ) 
        x["VehicleParc_Header105"] = (int(ref["basic_year"]) + 5 ) 
        x["VehicleParc_Header106"] = (int(ref["basic_year"]) + 6 ) 
        x["VehicleParc_Header107"] = (int(ref["basic_year"]) + 7 ) 
        x["VehicleParc_Header108"] = (int(ref["basic_year"]) + 8 )   
        x["VehicleParc_Header109"] = (int(ref["basic_year"]) + 9 ) 
        x["VehicleParc_Header110"] = (int(ref["basic_year"]) + 10 ) 
        x["VehicleParc_Header111"] = (int(ref["basic_year"]) + 11 ) 
        x["VehicleParc_Header112"] = (int(ref["basic_year"]) + 12 )                
        x["VehicleParc_Header113"] = (int(ref["basic_year"]) + 13 ) 
        x["VehicleParc_Header114"] = (int(ref["basic_year"]) + 14 )  

        x["VehicleParc_Header200"] = (int(ref["basic_year"]) - 3 )  
        x["VehicleParc_Header201"] = (int(ref["basic_year"]) - 2 ) 
        x["VehicleParc_Header202"] = (int(ref["basic_year"]) - 1 )  
        x["VehicleParc_Header203"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header204"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header205"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header206"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header207"] = (int(ref["basic_year"]) + 4 )       


        i = 1
        j = 9
        k = 17
        while( i != 9 and j != 17 and k != 25):
            a = float(x["VehicleParc_Input" + str(i)]) + float(x["VehicleParc_Input"+ str(j)])
            x["VehicleParc_Input" + str(k)] = a
            i +=1
            j +=1
            k +=1
        i = 25
        j = 33
        k = 41
        while( i != 33 and j != 41 and k != 49):
            a = float(x["VehicleParc_Input" + str(i)]) + float(x["VehicleParc_Input"+ str(j)])
            x["VehicleParc_Input" + str(k)] = a
            i +=1
            j +=1
            k +=1

        #Headers for the vehicle parc

        x["VehicleParc_Header1"] = (int(ref["basic_year"]) - 3 ) 
        x["VehicleParc_Header2"] = (int(ref["basic_year"]) - 2 )
        x["VehicleParc_Header3"] = (int(ref["basic_year"]) - 1 ) 
        x["VehicleParc_Header4"] = (int(ref["basic_year"])) 
        x["VehicleParc_Header5"] = (int(ref["basic_year"]) + 1 ) 
        x["VehicleParc_Header6"] = (int(ref["basic_year"]) + 2 ) 
        x["VehicleParc_Header7"] = (int(ref["basic_year"]) + 3 ) 
        x["VehicleParc_Header8"] = (int(ref["basic_year"]) + 4 ) 


        # Calculation Running parc DAF - dealer area Table
        sum = 0
        m = 49
        n = 64
        for j in range(64, 176, 16):
            for i in range(m, n):
                sum = sum + float(x["VehicleParc_Input" + str(i)])
                x["VehicleParc_Input" + str(j)] = sum
            sum = 0
            m = m + 16
            n = n + 16
        # Calculation Running parc DAF - dealer area Table
        sum = 0
        m = 49
        n = 161
        for j in range(161, 177):
            for i in range(m, n, 16):
                sum = sum + float(x["VehicleParc_Input" + str(i)])
                x["VehicleParc_Input" + str(j)] = sum
            sum = 0
            m = m + 1
            n = n + 1
        #Calculation Trailers sales dealer
        i = 177
        j = 185
        k = 193
        while( i != 185 and j != 194 and k != 201):
            a = float(x["VehicleParc_Input" + str(i)]) + float(x["VehicleParc_Input"+ str(j)])
            x["VehicleParc_Input" + str(k)] = a
            i +=1
            j +=1
            k +=1
    i = 208
    j = 216
    k = 224

    while i in range(207, 216) and j in range(215, 224) and k in range(223, 232):
        x["VehicleParc_Input" + str(k)] = float(x["VehicleParc_Input" + str(i)]) + float(x["VehicleParc_Input"+ str(j)])
        i +=1
        j +=1
        k +=1



        current_db.vehicle.update_one({"GlobalId": "global"}, {"$set": x})
    x = current_db.vehicle.find_one({"GlobalId": "global"})
    return redirect(url_for('vehicleparc.vehicle'))      
    return render_template("vehicleparc.html", data=x)


####################################################################################

@vehicleparc_bp.route('/vehicleparc/delete',  methods=['POST'])
@login_required
def delete_vehicle():
    """
    deletes a collection in the database
    """
    current_db = get_current_db()
    x = {}
    if request.method == "POST":
        x = get_form_to_dict(request.form)
        
        x['GlobalId'] = 'global'   
        x= current_db.vehicle.delete_many({})

    return redirect(url_for('vehicleparc.vehicle'))          
    return render_template("vehicleparc.html", data=x)