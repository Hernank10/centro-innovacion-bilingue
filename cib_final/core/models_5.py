class Notificacion(models.Model):
    TIPOS = [
        ('BIENVENIDA', 'Bienvenida'),
        ('LOGRO', 'Logro'),
        ('AMISTAD', 'Amistad'),
        ('SISTEMA', 'Sistema'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS, default='SISTEMA')
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
