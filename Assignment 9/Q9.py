def employee(**deatiles):
    for k,v in deatiles.items():
        print(f"{k} : {v}")
employee(name="Kiran",id=101,dept="IT")