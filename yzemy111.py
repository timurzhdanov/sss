import json

basa_met = {
    "station_name": "severnay kakashka",
    "address": "forgot street, 69",
    "workers": [
        {
            "id": 1,
            "name": "Armen Vasko",
            "age": 25,
            "email": "armen@example.com",
            "class_id": 1
        },
        {
            "id": 2,
            "name": "Oleg Mongol",
            "age": 99,
            "email": "ystal@garaz.com",
            "class_id": 2
        },
        {
            "id": 3,
            "name": "Ivan Pytin",
            "age": 7,
            "email": "besit@json.com",
            "class_id": 1
        },
        {
            "id": 4,
            "name": "Marina Guapovna",
            "age": 43,
            "email": "letitop@example.com",
            "class_id": 2
        }
    ],   
    "classes": [
        {
            "id": 1,
            "name": "scientists",
            "class_nachalnik_id": 1,
            "workers_id": [
                1,
                3
            ],
        },
        {
            "id": 2,        
            "name": "cleaners",
            "class_nachalnik_id": 2,
            "workers_id": [
                2,
                4
            ],            
        }
    ],    
    "nachalniks": [
    {
        "id": 1,
        "name": "Zloi Kavkazech",
        "email": "opasniy@example.com",            
    },
    {
        "id": 2,
        "name": "Prigozin Evgesha",
        "email": "vagner@example.com",
    }
    ]
}
        

def wr(basa_met,file_name):
    basa_met = json.dumps(basa_met)
    basa_met = json.loads(str(basa_met))
    

    with open(file_name,'w',encoding="utf-8") as file:
        json.dump(basa_met,file,indent=4)
        

wr(basa_met,"basa.json")

      
def read_inf(file_name):
    with open(file_name,'r',encoding="utf-8") as file:
        return json.load(file)
    
def gtoid(id,elem):
    basa = read_inf("basa.json")

    for e in basa[elem]:
        if e["id"] == id:
            return e

    return {"message": f"Element with {id} not found"}

def upoid(id,pers,name):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[name]):
        if e["id"] == id:
            e["name"] = pers["name"]
            e["age"] = pers["age"]
            e["email"] = pers["email"]
            wr(basa,"basa.json")
            return e

    return {"message": f"Element with {id} not found"}

def cro(pers,kto):
    basa = read_inf("basa.json")

    last_id = len(basa[kto])
    basa[kto].append({"id": last_id + 1, **pers})
    wr(basa,"basa.json")
    
def deloid(id,pers):
    basa = read_inf("basa.json")
    for i, e in enumerate(basa[pers]):
        if e["id"] == id:
            dele = basa[pers].pop(i)
            wr(basa,"basa.json")
            return dele

    return {"message": f"Element with {id} not found"}

beck = 10
while beck > 0:
    while True:
        sp = 1,2,3,4
        try:
            print("what do you want to do with the data? create (1), read (2), update (3), delete (4)")
            zap = int(input())
            if zap in sp:
                break
            else: print("Try again:")
        except ValueError:
            print("Try again:")
            
    if zap == 2:
        basa = read_inf("basa.json")
        print("display the readings of one element(1) or all(2)")
        zap1 = int(input()) 
        if zap1 == 2:
            print(read_inf("basa.json"))
        if zap1 == 1:
            print("display what element readings station name(1), address(2), workers(3),classes(4),nachalniks(5)")
            zap2 = int(input())
            if zap2 == 1: print(basa["station_name"])
            if zap2 == 2: print(basa["address"])
            if zap2 == 3: 
                print("all workers(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["workers"])
                if zap3 == 2:
                    print("wich worker")
                    zap4 = int(input())
                    print(gtoid(zap4,"workers"))
            if zap2 == 4: 
                print("all classes(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["classes"])
                if zap3 == 2:
                    print("wich class")
                    zap4 = int(input())
                    print(gtoid(zap4,"classes"))
            if zap2 == 5: 
                print("all nachalniks(1) or one(2)")
                zap3 = int(input())
                if zap3 == 1: print(basa["nachalniks"])
                if zap3 == 2:
                    print("wich nachalnik")
                    zap4 = int(input())
                    print(gtoid(zap4,"nachalniks"))
                    
    if zap == 3:
        basa = read_inf("basa.json")
        print("display update workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            print("wich worker")
            zap2 = int(input())
            new_n = input("new name ")
            new_a = input("new age ")
            new_e = input("new email ")
            print(upoid(zap2,{"name": new_n,"age": new_a,"email": new_e},"workers"))
        if zap1 == 2:
            print("wich nachalnik")
            zap2 = int(input())
            new_n = input("new name ")
            new_a = input("new age ")
            new_e = input("new email ")
            print(upoid(zap2,{"name": new_n,"age": new_a,"email": new_e},"nachalniks"))
            
    if zap == 1:
        print("display create workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            new_n = input("name ")
            new_a = input("age ")
            new_e = input("email ")
            cro({"name": new_n,"age": new_a,"email": new_e},"workers"),"basa.json"
            print(read_inf("basa.json")["workers"])
        if zap1 == 2:
            new_n = input("name ")
            new_a = input("age ")
            new_e = input("email ")
            cro({"name": new_n,"age": new_a,"email": new_e},"nachalniks"),"basa.json"
            print(read_inf("basa.json")["nachalniks"])
    
            
    if zap == 4:
        print("display delete workers(1) or nachalniks(2)")
        zap1 = int(input()) 
        if zap1 == 1:
            print("wich worker")
            zap2 = int(input())
            deloid(zap2,"workers")
            print(read_inf("basa.json")["workers"])
        if zap1 == 2:
            print("wich nachalnik")
            zap2 = int(input())
            deloid(zap2,"nachalniks")
            print(read_inf("basa.json")["nachalniks"])
            
            

            
                    

                    

                    
                
            
                
        
