class Item(models.Model):
    TIPOS = [
        ('ESPECIAL', 'Especial'),
        ('CONSUMIBLE', 'Consumible'),
        ('COLECCIONABLE', 'Coleccionable'),
        ('MEDALLA', 'Medalla'),
    ]
    
    RAREZAS = [
        ('COMUN', 'Común'),
        ('RARO', 'Raro'),
        ('EPICO', 'Épico'),
        ('LEGENDARIO', 'Legendario'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    rareza = models.CharField(max_length=20, choices=RAREZAS, default='COMUN')
    descripcion = models.TextField()
    valor = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
