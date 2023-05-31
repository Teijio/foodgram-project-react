# Generated by Django 4.2.1 on 2023-05-31 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="shoppinglist",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shop_list",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.ingredient",
                verbose_name="Ингредиент",
            ),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="Название рецепта",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор рецепта",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="recipes",
                through="recipes.RecipeIngredient",
                to="recipes.ingredient",
                verbose_name="Ингридиенты",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                related_name="recipes", to="recipes.tag", verbose_name="Теги"
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_by",
                to="recipes.recipe",
                verbose_name="Избранный рецепт",
            ),
        ),
        migrations.AddField(
            model_name="favoriterecipe",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_recipes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="favoriterecipe",
            unique_together={("user", "recipe")},
        ),
    ]
