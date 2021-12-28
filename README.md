# 🍽️ Recipager

## About

Small Recipe Manager application in Django that allows the creation of ingredients and recipes and calculates the costs for the recipes.
> This was an assignment to a Full Stack Python Developer position

## 📑 Requirements

### Ingredients
- [x] An ingredient minimally has:
   - name
   - article number
   - cost for a certain amount
- [x] You need to minimally support the following units: 
  - grams
  - kilograms
  - centiliter
  - liter
- [x] There should be a page to add a new ingredient
- [x] There should be a page to edit an existing ingredient
- [x] There should be a page to view all ingredients
- [x] A user should be able to search his ingredients based on name or article number

### Recipes
- [x] A recipe minimally has:
   - name
   - list of ingredients with the amounts needed
- [ ] There should be a page to create new recipes
- [ ] There should be a page to edit existing recipes
- [x] There should be a page to view all recipes
- [x] There should be a page to see the details of a recipe. This page should show the name but also the cost for each ingredient used in the recipe 

## 🧬 Technologies
- Python
- Django
- Materialize CSS
- Javascript

## ⚙️ Setup
To run this project, be sure to have installed:
- [Python 3.9.7](https://nodejs.dev/download/)
- [A code editor](https://code.visualstudio.com)

After that, you need to clone this repo:
```bash
git clone https://github.com/LBeghini/Recipager.git
```
Before running the code, you need to install the dependencies. From a terminal at the root directory of the project, run:
```bash
pip install -r requirements.txt
```

## ▶️ Running
To run the code, from a terminal, on the project's root directory, run:
```bash
python manage.py runserver
```
## 🧭 Usage
From a browser, go to url [localhost:8000/recipager/](http://localhost:8000/recipager/).
If everything is working fine, you should be able to see the main page of the application.

## ⚖️ [License](https://github.com/LBeghini/Recipager/blob/main/LICENSE)
Feel free to modify as you wish!

