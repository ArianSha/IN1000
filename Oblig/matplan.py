def få_matplan():
    matplan={"karin":{"egg","suppe","pasta"}, 
    "daniel":{"brød","havregryn","kyllingvinger"}}
    navn = input("hvem sin matplan leter du etter? ").lower()
    if navn in matplan:
        print("beboeren sin matplan er følgenede:" , matplan[navn])
    else:
        print("beboeren er ikke i vårt register")

få_matplan()