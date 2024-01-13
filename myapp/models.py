from django.db import models


class Svcs(models.Model):
    ARMY = 'Army'
    NAVY = 'Navy'
    AIR_FORCE = 'Air Force'
    AFD = 'AFD'

    SERVICE_CHOICES = [
        (ARMY, 'Army'),
        (NAVY, 'Navy'),
        (AIR_FORCE, 'Air Force'),
        (AFD, 'AFD'),
    ]

    name = models.CharField(max_length=20, choices=SERVICE_CHOICES)

    def __str__(self):
        return self.name


class Sections(models.Model):
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)

    def __str__(self):
        return self.name





class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country_class = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])

    def __str__(self):
        return self.name


class Evcats(models.Model):
    name = models.CharField(max_length=100, choices=[("Course", "Course"), ("SMEE", "SMEE"), ("Visit", "Visit"), ("Exercise", "Exercise"), ("Seminar", "Seminar"), ("Symposium", "Symposium"), ("Misc", "Misc")])

    def __str__(self):
        return self.name


class GovtOrder(models.Model):
    event_name = models.CharField(max_length=100)
    go_number = models.CharField(max_length=100, unique=True)
    go_pub_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    days_involved = models.IntegerField(blank=True, null=True)
    govt_order_document = models.FileField(upload_to='govt_order_documents/', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    svc = models.ForeignKey(Svcs, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        self.days_involved = (self.end_date - self.start_date).days
        super(GovtOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.event_name}-{self.go_number}-{self.go_pub_date}"

    class Meta:
        ordering = ['-go_pub_date']


class Participants(models.Model):
    Service_Number = models.CharField(max_length=200)
    Rank = models.CharField(max_length=40)
    name = models.CharField(max_length=100, unique=True)
    svc = models.ForeignKey(Svcs, on_delete=models.CASCADE)
    govt_order = models.ForeignKey(GovtOrder, on_delete=models.CASCADE, related_name='participants', default=1)

    def __str__(self):
        return self.name
class Events(models.Model):
    name = models.CharField(max_length=100, unique=False)
    event_category = models.ForeignKey(Evcats, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants, related_name='courses')
    duration = models.IntegerField(blank=True, null=True)  # Add this line

    def save(self, *args, **kwargs):
        self.duration = (self.end_date - self.start_date).days
        super(Events, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class VacancyDistribution(models.Model):
    course_offer = models.ForeignKey('CourseOffer', on_delete=models.CASCADE)
    svc = models.ForeignKey('Svcs', on_delete=models.CASCADE)
    vacancies_allocated = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.course_offer.event_name} - {self.svc.name} ({self.vacancies_allocated} allocated)"


class CourseOffer(models.Model):
    ff_country = models.ForeignKey('Country', on_delete=models.CASCADE)
    event_name = models.ForeignKey('Events', on_delete=models.CASCADE)
    vac_offered = models.PositiveIntegerField(default=1)
    vac_accepted = models.PositiveIntegerField(default=1)
    vac_regretted = models.PositiveIntegerField(default=0)
    financial = models.CharField(
        max_length=20,
        choices=[
            ("gratis", "Gratis"),
            ("non-gratis", "Non-Gratis"),
            ("partial-gratis", "Partial-Gratis")
        ],
        default='Gratis'
    )

    def save(self, *args, **kwargs):
        # Calculate vac_regretted dynamically based on vac_offered and vac_accepted
        self.vac_regretted = max(0, self.vac_offered - self.vac_accepted)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Offered: {self.event_name} from {self.ff_country}"




