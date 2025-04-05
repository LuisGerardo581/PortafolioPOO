class Pokemon:
    def __init__(self, nombre, defensa, ataque, tipo = "N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.tipo = tipo
    
    def __str__(self):
        tipo.emojis = {
            "Fuego": "🔥",
            "Elenctrico": "⚡",
            "Agua": "🌊"
        }
        
        emoji = tipo.emojis.get(self.tipo, "❓")
        
        return f"{self.nombre} ({self.tipo})"