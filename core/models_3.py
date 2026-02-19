class Inventario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inventario_core')
    items = models.ManyToManyField(Item, through='ItemUsuario', related_name='inventarios')
    
    def __str__(self):
        return f"Inventario de {self.usuario.username}"

class ItemUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_usuario')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='usuarios_item')
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, null=True, blank=True, related_name='items_inventario')
    cantidad = models.IntegerField(default=1)
    equipado = models.BooleanField(default=False)
    fecha_obtencion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['usuario', 'item']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.item.nombre} x{self.cantidad}"
