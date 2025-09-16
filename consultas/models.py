from django.db import models

class UsuarioMedico(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True)
    id_medico = models.IntegerField(unique=True)  # Mejor usar IntegerField si es un ID
    alcance = models.IntegerField(default=0)
    n_matricula = models.IntegerField(default=0)
    pregunta = models.CharField(max_length=50, null=True, blank=True)
    respuesta = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    stamp = models.DateTimeField(null=True)
    datos_medico = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        db_table = 'UsuariosMedicos'
        indexes = [
            models.Index(fields=['id_medico']),
        ]

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_medico})"


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Pacientes'

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni})"


class Episodio(models.Model):
    id_episodio = models.AutoField(primary_key=True)
    id_ingreso = models.IntegerField(default=0)
    id_hcl = models.IntegerField(default=0)
    id_tipo_episodio = models.IntegerField(default=0)
    id_capitulo = models.IntegerField(default=0)
    
    medico = models.ForeignKey(
        UsuarioMedico,
        to_field='usuario',
        on_delete=models.SET_NULL,
        null=True,
        db_column='Usuario'
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.SET_NULL,
        null=True,
        db_column='IdPaciente'
    )

    fecha_atencion = models.DateTimeField(null=True, blank=True)
    hora_atencion = models.DateTimeField(null=True, blank=True)
    txt_fecha_hora_atencion = models.CharField(max_length=50, null=True, blank=True)

    motivo_de_consulta = models.CharField(max_length=50, default='', blank=True)
    sintomas_breve = models.TextField(null=True, blank=True)
    tratamiento_previo = models.TextField(default='', blank=True)
    diagnostico_presuntivo = models.CharField(max_length=255, default='', blank=True)
    cie10_diagnostico_presuntivo = models.CharField(max_length=10, default='', blank=True)
    tratamiento = models.TextField(default='', blank=True)
    stamp = models.CharField(max_length=255, default='current_timestamp()', blank=True)

    class Meta:
        db_table = 'TblEpisodios'
        indexes = [
            models.Index(fields=['id_capitulo']),
            models.Index(fields=['id_ingreso']),
            models.Index(fields=['medico']),
            models.Index(fields=['paciente']),
        ]

    def __str__(self):
        return f"Episodio {self.id_episodio} - {self.medico} - {self.paciente}"