class Logro(models.Model):
    CATEGORIAS = [
        ('AVENTURA', 'Aventura'),
        ('ORTOGRAFIA', 'Ortografía'),
        ('SOCIAL', 'Social'),
        ('ESPECIAL', 'Especial'),
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    puntos = models.IntegerField(default=10)
    
    def __str__(self):
        return self.nombre

class LogroDesbloqueado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    logro = models.ForeignKey(Logro, on_delete=models.CASCADE)
    fecha_desbloqueo = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['usuario', 'logro']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.logro.nombre}"
