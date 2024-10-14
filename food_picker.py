import random
def food_selection(weight_category):
    normal_weight_breakfast = [
    "Oats with fruits",
    "Poha with vegetables",
    "Idli with sambar",
    "Dosa with chutney",
    "Upma",
    "Sprout salad",
    "Fruit smoothie",
    "Multigrain toast with avocado",
    "Masala omelette"
]
    normal_weight_lunch = [
    "Grilled chicken salad",
    "Vegetable pulao",
    "Dal and roti",
    "Mixed vegetable curry",
    "Quinoa salad",
    "Paneer tikka",
    "Chickpea curry with rice",
    "Fish curry with brown rice",
    "Vegetable biryani"
]
    normal_weight_dinner = [
    "Grilled fish with vegetables",
    "Vegetable soup",
    "Stir-fried tofu with veggies",
    "Lentil soup with whole grain bread",
    "Vegetable khichdi",
    "Palak paneer with roti",
    "Grilled chicken with quinoa",
    "Stuffed bell peppers",
    "Rajma with brown rice"
]
    obesity_level1_breakfast = [
    "Oats with berries",
    "Vegetable smoothie",
    "Ragi porridge",
    "Fruit salad",
    "Sprouts with lemon",
    "Vegetable sandwich",
    "Moong dal chilla",
    "Greek yogurt with fruits",
    "Scrambled eggs with vegetables"
]
    obesity_level1_lunch = [
    "Vegetable salad with grilled chicken",
    "Lentil soup",
    "Quinoa salad",
    "Mixed vegetable curry with brown rice",
    "Paneer tikka with salad",
    "Chickpea curry with quinoa",
    "Fish curry with steamed rice",
    "Vegetable stir-fry",
    "Dal with roti"
]
    obesity_level1_dinner = [
    "Vegetable soup",
    "Grilled fish with vegetables",
    "Stir-fried tofu with veggies",
    "Lentil soup with whole grain bread",
    "Vegetable khichdi",
    "Palak paneer with roti",
    "Grilled chicken with quinoa",
    "Stuffed bell peppers",
    "Rajma with brown rice"
]
    obesity_level2_breakfast = [
    "Vegetable upma",
    "Fruit smoothie",
    "Multigrain porridge",
    "Sprout salad",
    "Idli with sambar",
    "Oatmeal with fruits",
    "Scrambled eggs with spinach",
    "Moong dal chilla",
    "Greek yogurt with berries"
]
    obesity_level2_lunch = [
    "Vegetable salad with grilled chicken",
    "Mixed vegetable curry with brown rice",
    "Dal with quinoa",
    "Vegetable stir-fry",
    "Rajma with roti",
    "Grilled chicken wrap",
    "Fish curry with steamed rice",
    "Vegetable lentil soup",
    "Methi paratha with yogurt"
]
    obesity_level2_dinner = [
    "Vegetable soup",
    "Grilled tofu with veggies",
    "Dal tadka with brown rice",
    "Stir-fried chicken with vegetables",
    "Spinach and chickpea curry",
    "Vegetable khichdi",
    "Paneer bhurji with roti",
    "Baked fish with vegetables",
    "Lentil stew"
]
    obesity_level3_breakfast = [
    "Oats with berries",
    "Vegetable smoothie",
    "Ragi porridge",
    "Fruit salad",
    "Sprouts with lemon",
    "Vegetable sandwich",
    "Moong dal chilla",
    "Greek yogurt with fruits",
    "Scrambled eggs with vegetables"
]
    obesity_level3_lunch = [
    "Vegetable salad with grilled chicken",
    "Lentil soup",
    "Quinoa salad",
    "Mixed vegetable curry with brown rice",
    "Paneer tikka with salad",
    "Chickpea curry with quinoa",
    "Fish curry with steamed rice",
    "Vegetable stir-fry",
    "Dal with roti"
]
    obesity_level3_dinner = [
    "Vegetable soup",
    "Grilled fish with vegetables",
    "Stir-fried tofu with veggies",
    "Lentil soup with whole grain bread",
    "Vegetable khichdi",
    "Palak paneer with roti",
    "Grilled chicken with quinoa",
    "Stuffed bell peppers",
    "Rajma with brown rice"
]
    overweight_level1_breakfast = [
    "Moong dal chilla",
    "Vegetable upma",
    "Fruit salad with yogurt",
    "Multigrain porridge",
    "Besan cheela",
    "Smoothie bowl",
    "Boiled eggs with spinach",
    "Masala oats",
    "Whole wheat toast with peanut butter"
]
    overweight_level1_lunch = [
    "Mixed vegetable curry with brown rice",
    "Grilled paneer salad",
    "Dal with quinoa",
    "Vegetable stir-fry",
    "Rajma with roti",
    "Grilled chicken wrap",
    "Fish curry with steamed rice",
    "Vegetable lentil soup",
    "Methi paratha with yogurt"
]
    overweight_level1_dinner = [
    "Vegetable soup with whole grain bread",
    "Grilled tofu with veggies",
    "Dal tadka with brown rice",
    "Stir-fried chicken with vegetables",
    "Spinach and chickpea curry",
    "Vegetable khichdi",
    "Paneer bhurji with roti",
    "Baked fish with vegetables",
    "Lentil stew"
]
    overweight_level2_breakfast = [
    "Vegetable smoothie",
    "Quinoa porridge",
    "Idli with coconut chutney",
    "Oatmeal with nuts and fruits",
    "Ragi dosa",
    "Greek yogurt with berries",
    "Avocado toast",
    "Vegetable poha",
    "Scrambled eggs with spinach"
]
    overweight_level2_lunch = [
    "Grilled chicken salad",
    "Vegetable soup",
    "Chickpea salad",
    "Paneer tikka with salad",
    "Vegetable biryani with raita",
    "Dal with brown rice",
    "Stir-fried vegetables with tofu",
    "Quinoa salad",
    "Vegetable curry with roti"
]
    overweight_level2_dinner = [
    "Lentil soup",
    "Vegetable stir-fry with quinoa",
    "Grilled fish with vegetables",
    "Stuffed bell peppers",
    "Vegetable khichdi",
    "Methi thepla with yogurt",
    "Grilled chicken with vegetables",
    "Paneer bhurji with roti",
    "Mixed vegetable curry with brown rice"
]
    insufficient_weight_breakfast = [
    "Peanut butter and banana sandwich",
    "Oats with whole milk and nuts",
    "Fruit smoothie with protein powder",
    "Paneer paratha",
    "Eggs and avocado toast",
    "Greek yogurt with honey and granola",
    "Mango milkshake",
    "Vegetable omelette with cheese",
    "Idli with coconut chutney"
]
    insufficient_weight_lunch = [
    "Chicken biryani",
    "Paneer butter masala with naan",
    "Vegetable pulao with raita",
    "Dal makhani with jeera rice",
    "Chole bhature",
    "Grilled cheese sandwich with tomato soup",
    "Fish curry with steamed rice",
    "Mixed vegetable curry with paratha",
    "Rajma with rice and ghee"
]
    insufficient_weight_dinner = [
    "Butter chicken with naan",
    "Paneer tikka masala with roti",
    "Vegetable pasta with cheese",
    "Chicken stew with bread",
    "Palak paneer with rice",
    "Stuffed paratha with yogurt",
    "Mutton curry with rice",
    "Vegetable biryani with boondi raita",
    "Egg curry with paratha"
]
    selected_breakfast = random.choice(normal_weight_breakfast)
    selected_lunch = random.choice(normal_weight_lunch)
    selected_dinner = random.choice(normal_weight_dinner)
    normal_weight_foods = [selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(overweight_level1_breakfast)
    selected_lunch = random.choice(overweight_level1_lunch)
    selected_dinner = random.choice(overweight_level1_dinner)
    overweight_level_i_foods = [selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(overweight_level2_breakfast)
    selected_lunch = random.choice(overweight_level2_lunch)
    selected_dinner = random.choice(overweight_level2_dinner)
    overweight_level_ii_foods = [selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(obesity_level1_breakfast)
    selected_lunch = random.choice(obesity_level1_lunch)
    selected_dinner = random.choice(obesity_level1_dinner)
    obesity_type_i_foods=[selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(obesity_level2_breakfast)
    selected_lunch = random.choice(obesity_level2_lunch)
    selected_dinner = random.choice(obesity_level2_dinner)
    obesity_type_ii_foods=[selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(obesity_level3_breakfast)
    selected_lunch = random.choice(obesity_level3_lunch)
    selected_dinner = random.choice(obesity_level3_dinner)
    obesity_type_iii_foods = [selected_breakfast, selected_lunch, selected_dinner]
    selected_breakfast = random.choice(insufficient_weight_breakfast)
    selected_lunch = random.choice(insufficient_weight_lunch)
    selected_dinner = random.choice(insufficient_weight_dinner)
    insufficient_weight_foods = [selected_breakfast, selected_lunch, selected_dinner]
    if weight_category == "Normal_Weight":
        selected_array = normal_weight_foods
    elif weight_category == "Overweight_Level_I":
        selected_array = overweight_level_i_foods
    elif weight_category == "Overweight_Level_II":
        selected_array = overweight_level_ii_foods
    elif weight_category == "Obesity_Type_I":
        selected_array = obesity_type_i_foods
    elif weight_category == "Obesity_Type_II":
        selected_array = obesity_type_ii_foods
    elif weight_category == "Obesity_Type_III":
        selected_array = obesity_type_iii_foods
    else:
        selected_array=insufficient_weight_foods
    selected_food = selected_array
    return selected_food