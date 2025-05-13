from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.urls import reverse

class Cat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Description of the cat")
    rarity = models.CharField(
        max_length=50,
        choices=[
            ('NORMAL', 'Normal'),
            ('SPECIAL', 'Special'),
            ('RARE', 'Rare'),
            ('SUPER_RARE', 'Super Rare'),
            ('UBER_RARE', 'Uber Rare'),
            ('LEGEND_RARE', 'Legend Rare')
        ],
        default='NORMAL'
    )
    image = models.ImageField(upload_to='cats/', blank=True, null=True)
    base_health = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Base health points"
    )
    base_attack = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Base attack power"
    )
    abilities = models.ManyToManyField(
        'Ability',
        related_name='cats',
        blank=True,
        help_text="Abilities this cat has"
    )
    attack_range = models.IntegerField(
        default=140,
        validators=[MinValueValidator(1)],
        help_text="Attack range in pixels"
    )
    attack_speed = models.FloatField(
        default=1.0,
        validators=[MinValueValidator(0.1)],
        help_text="Attack speed (attacks per second)"
    )
    movement_speed = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1)],
        help_text="Movement speed"
    )
    cost = models.IntegerField(
        default=75,
        validators=[MinValueValidator(0)],
        help_text="Cost to deploy"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['rarity', 'name']
        verbose_name = "Cat"
        verbose_name_plural = "Cats"

    def __str__(self):
        return f"{self.name} ({self.get_rarity_display()})"

    def get_absolute_url(self):
        return reverse('catspedia:cat-detail', kwargs={'pk': self.pk})

class Objective(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Describe the objective")
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ('EASY', 'Easy'),
            ('MEDIUM', 'Medium'),
            ('HARD', 'Hard'),
            ('EXPERT', 'Expert')
        ],
        default='MEDIUM'
    )
    energy_cost = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0)]
    )
    rewards = models.JSONField(
        default=dict,
        help_text='Rewards for completing the objective'
    )
    required_level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text='Required player level to attempt this objective'
    )
    enemy_types = models.JSONField(
        default=list,
        help_text='Types of enemies that appear in this objective'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['difficulty', 'required_level', 'name']
        verbose_name = "Objective"
        verbose_name_plural = "Objectives"

    def __str__(self):
        return f"{self.name} ({self.get_difficulty_display()})"

    def get_absolute_url(self):
        return reverse('catspedia:objective-detail', kwargs={'pk': self.pk})

class Effect(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Description of what the effect does")
    effect_type = models.CharField(
        max_length=50,
        choices=[
            ('DAMAGE', 'Damage'),
            ('DEFENSE', 'Defense'),
            ('UTILITY', 'Utility'),
            ('CONTROL', 'Control'),
            ('SUPPORT', 'Support')
        ],
        default='DAMAGE'
    )
    base_power = models.FloatField(
        default=1.0,
        validators=[MinValueValidator(0.1)],
        help_text="Base power of the effect"
    )
    duration = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text='Duration in frames (1 frame = 1/30 second)'
    )
    cooldown = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text='Cooldown before the effect can be used again (in frames)'
    )
    area_of_effect = models.BooleanField(
        default=False,
        help_text="Whether the effect hits multiple targets"
    )
    proc_chance = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Probability of the effect activating (0-100%)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['effect_type', 'name']
        verbose_name = "Effect"
        verbose_name_plural = "Effects"

    def __str__(self):
        return f"{self.name} ({self.get_effect_type_display()})"

    def get_absolute_url(self):
        return reverse('catspedia:effect-detail', kwargs={'pk': self.pk})

class Ability(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(help_text="Description of the ability")
    effects = models.ManyToManyField(
        Effect,
        related_name='abilities',
        blank=True,
        help_text="Effects this ability can produce (optional)"
    )
    ability_type = models.CharField(
        max_length=50,
        choices=[
            ('PASSIVE', 'Passive'),
            ('ACTIVE', 'Active'),
            ('CONDITIONAL', 'Conditional'),
            ('TRIGGERED', 'Triggered')
        ],
        default='PASSIVE'
    )
    target_traits = models.JSONField(
        default=list,
        help_text="List of enemy traits this ability affects"
    )
    requirements = models.JSONField(
        default=dict,
        help_text="Requirements to unlock/use this ability"
    )
    energy_cost = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Energy cost to use the ability (if active)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ability_type', 'name']
        verbose_name = "Ability"
        verbose_name_plural = "Abilities"

    def __str__(self):
        return f"{self.name} ({self.get_ability_type_display()})"

    def get_absolute_url(self):
        return reverse('catspedia:ability-detail', kwargs={'pk': self.pk})