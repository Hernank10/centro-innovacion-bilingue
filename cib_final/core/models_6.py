class Amistad(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ACEPTADA', 'Aceptada'),
        ('RECHAZADA', 'Rechazada'),
    ]
    
    usuario1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amistades1')
    usuario2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amistades2')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['usuario1', 'usuario2']
    
    def __str__(self):
        return f"{self.usuario1.username} - {self.usuario2.username} ({self.estado})"

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    leido = models.BooleanField(default=False)
    fecha_envio = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"De: {self.remitente.username} Para: {self.destinatario.username}"
