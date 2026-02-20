class PuntuacionDiaria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    tipo_juego = models.CharField(max_length=20)
    fecha = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.fecha} - {self.puntos}pts"
