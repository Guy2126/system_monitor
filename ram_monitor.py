import psutil 

def minitor_ram():
    memory = psutil.virtual_memory()
    print(f"RAM totale : {memory.total/ (1024**3):.2f} GB")
    print(f"RAM utilisee : {memory.used / (1024**3):.2f} GB")
    print(f"RAM disponible : {memory.available / (1024**3):.2f} GB")
    print(f"Utilisateur : {memory.percent}%")

if __name__=="__main__":
    minitor_ram()