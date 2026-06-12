
```python
import streamlit as st
import re

# =========================================================================
# 1. COMPREHENSIVE BASELINE HEALTH MATRIX (VEGETARIAN & NON-VEGETARIAN)
# =========================================================================
WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Base menus optimized per Age Cohort & Diet Preference
BASE_NUTRITION = {
    "Youth (1-18)": {
        "Vegetarian": {
            "sleep_ideal": "9 to 11 hours",
            "exercise": "60 minutes of active play daily (running, cycling, outdoor games).",
            "avoid": "Packed artificially flavored juices, highly processed maida biscuits, and spicy roadside mixtures.",
            "days": {
                "Monday": {"Breakfast": "Ragi porridge with whole milk & soft idli.", "Lunch": "Soft dal khichdi with ghee and carrots.", "Snack": "Apple slices with a tiny bit of honey.", "Dinner": "Wheat upma with grated carrots."},
                "Tuesday": {"Breakfast": "Millet porridge with organic jaggery.", "Lunch": "Curd rice with mashed carrots.", "Snack": "Homemade soft ragi biscuits.", "Dinner": "Soft paneer bhurji with a mini chapati."},
                "Wednesday": {"Breakfast": "Warm oats porridge with milk and sliced bananas.", "Lunch": "Soft-cooked rice, tomato rasam, and soft potato cubes.", "Snack": "Stewed apple.", "Dinner": "Moong dal soup with broken wheat khichdi."},
                "Thursday": {"Breakfast": "Ragi Java with a little milk and nuts.", "Lunch": "Vegetable khichdi with fresh curd.", "Snack": "Roasted makhana.", "Dinner": "Soft vermicelli upma with peas."},
                "Friday": {"Breakfast": "Oats porridge with mashed banana.", "Lunch": "Mashed rice, leafy green dal, and ghee.", "Snack": "Fresh curd with honey.", "Dinner": "Paneer cubes with soft wheat dahlia upma."},
                "Saturday": {"Breakfast": "Wheat pancake (Dosa style) with milk.", "Lunch": "Sambar rice with soft-cooked pumpkin.", "Snack": "A handful of boiled sweet corn.", "Dinner": "Light vegetable clear soup and idli."},
                "Sunday": {"Breakfast": "Ragi vermicelli sweet semiya.", "Lunch": "Soft rice, thick paneer dal.", "Snack": "Fresh fruit smoothie.", "Dinner": "Soft-cooked broken rice khichdi with ghee."}
            }
        },
        "Non-Vegetarian": {
            "sleep_ideal": "9 to 11 hours",
            "exercise": "60 minutes of active play daily (running, cycling, outdoor games).",
            "avoid": "Packed artificially flavored juices, deep-fried chicken nuggets, and heavy processed meats.",
            "days": {
                "Monday": {"Breakfast": "Scrambled eggs (2 eggs) with soft toast.", "Lunch": "Soft dal khichdi with shredded chicken breast.", "Snack": "Apple slices with a tiny bit of honey.", "Dinner": "Wheat upma with soft chicken strips."},
                "Tuesday": {"Breakfast": "Millet porridge with organic jaggery & one boiled egg.", "Lunch": "Curd rice with steamed mashed fish.", "Snack": "Homemade soft ragi biscuits.", "Dinner": "Soft chicken bhurji with a mini chapati."},
                "Wednesday": {"Breakfast": "Boiled eggs with sliced bananas.", "Lunch": "Soft-cooked rice, chicken clear soup, and soft potato cubes.", "Snack": "Stewed apple.", "Dinner": "Moong dal soup with boiled egg whites."},
                "Thursday": {"Breakfast": "Ragi Java with a little milk & scrambled eggs.", "Lunch": "Chicken khichdi with fresh curd.", "Snack": "Roasted makhana.", "Dinner": "Soft vermicelli upma with egg drop."},
                "Friday": {"Breakfast": "Oats porridge with mashed banana & boiled egg.", "Lunch": "Mashed rice, chicken dal soup, and ghee.", "Snack": "Fresh curd with honey.", "Dinner": "Shredded chicken with soft wheat dahlia upma."},
                "Saturday": {"Breakfast": "Wheat pancake (Dosa style) with milk and egg white.", "Lunch": "Sambar rice with soft boiled fish.", "Snack": "A handful of boiled sweet corn.", "Dinner": "Light chicken clear soup and idli."},
                "Sunday": {"Breakfast": "Ragi vermicelli sweet semiya with a boiled egg.", "Lunch": "Soft rice, chicken clear soup.", "Snack": "Fresh fruit smoothie.", "Dinner": "Soft-cooked chicken khichdi."}
            }
        }
    },
    "Adult (19-59)": {
        "Vegetarian": {
            "sleep_ideal": "7 to 9 hours",
            "exercise": "30-45 minutes of moderate exercise 5 days a week (brisk walking, gym, yoga).",
            "avoid": "Excessive white sugar, refined flour (maida), highly processed packaged snacks, and late-night heavy meals.",
            "days": {
                "Monday": {"Breakfast": "Unsweetened Ragi Java with buttermilk & sprouts.", "Lunch": "Jowar Roti, a bowl of Toor Dal, and ladyfinger (bhindi) sabzi.", "Snack": "A handful of roasted chana.", "Dinner": "Light Foxtail Millet Khichdi with curd."},
                "Tuesday": {"Breakfast": "Millet Poha with roasted peanuts and lemon juice.", "Lunch": "Brown rice, mixed vegetable sambar, and palak stir-fry.", "Snack": "One seasonal fruit (Guava or Apple).", "Dinner": "Two whole wheat chapatis with paneer bhurji."},
                "Wednesday": {"Breakfast": "Oats Idli with mint and coriander chutney.", "Lunch": "Bajra Roti, green moong dal, and ivy gourd sabzi.", "Snack": "Plain buttermilk with roasted cumin powder.", "Dinner": "Broken wheat (dalia) upma with carrots and peas."},
                "Thursday": {"Breakfast": "Moong Dal Chilla (savory pancake) with curd.", "Lunch": "Jowar Roti, chana masala, and cucumber salad.", "Snack": "Soaked almonds and walnuts.", "Dinner": "Little Millet curd rice with stir-fried veggies."},
                "Friday": {"Breakfast": "Ragi porridge with a dash of jaggery and almonds.", "Lunch": "Brown rice, tomato rasam, and paneer curry.", "Snack": "Roasted makhana.", "Dinner": "Mixed vegetable clear soup with grilled tofu/paneer."},
                "Saturday": {"Breakfast": "Vegetable Upma made from multi-millet semolina.", "Lunch": "Whole wheat chapatis, ridge gourd curry, and dal.", "Snack": "Coconut water.", "Dinner": "Foxtail Millet pulao with raita."},
                "Sunday": {"Breakfast": "Healthy Multi-grain Dosa with ginger chutney.", "Lunch": "Brown rice or Jowar Roti, sprouted methi dal.", "Snack": "A cup of green tea or spiced buttermilk.", "Dinner": "Light oats porridge or vegetable khichdi."}
            }
        },
        "Non-Vegetarian": {
            "sleep_ideal": "7 to 9 hours",
            "exercise": "30-45 minutes of moderate exercise 5 days a week (brisk walking, gym, strength training).",
            "avoid": "Excessive white sugar, deep-fried chicken, highly processed meats, and trans-fats.",
            "days": {
                "Monday": {"Breakfast": "Two scrambled eggs with spinach and whole wheat toast.", "Lunch": "Jowar Roti, yellow dal, and chicken breast curry.", "Snack": "A handful of roasted chana.", "Dinner": "Light Foxtail Millet chicken khichdi with curd."},
                "Tuesday": {"Breakfast": "Millet Poha with boiled egg whites.", "Lunch": "Brown rice, mixed vegetable sambar, and grilled fish.", "Snack": "One seasonal fruit (Guava or Apple).", "Dinner": "Two whole wheat chapatis with chicken minced kheema."},
                "Wednesday": {"Breakfast": "Oats omelette with chopped tomatoes and coriander.", "Lunch": "Bajra Roti, green moong dal, and chicken cubes.", "Snack": "Plain buttermilk with cumin powder.", "Dinner": "Broken wheat (dalia) upma with soft chicken strips."},
                "Thursday": {"Breakfast": "Moong Dal Chilla with egg drop and curd.", "Lunch": "Jowar Roti, chicken masala, and cucumber salad.", "Snack": "Soaked almonds and walnuts.", "Dinner": "Little Millet egg curd rice."},
                "Friday": {"Breakfast": "Ragi porridge with boiled eggs.", "Lunch": "Brown rice, tomato rasam, and steamed fish.", "Snack": "Roasted makhana.", "Dinner": "Mixed vegetable clear soup with shredded chicken breast."},
                "Saturday": {"Breakfast": "Egg bhurji (2 eggs) with single chapati.", "Lunch": "Whole wheat chapatis, chicken curry, and dal.", "Snack": "Coconut water.", "Dinner": "Foxtail Millet chicken pulao with raita."},
                "Sunday": {"Breakfast": "Healthy Multi-grain Dosa with chicken mince stuffing.", "Lunch": "Brown rice, simple fish curry, and curd.", "Snack": "A cup of green tea or spiced buttermilk.", "Dinner": "Light oats porridge with egg white drop."}
            }
        }
    },
    "Senior (60-80+)": {
        "Vegetarian": {
            "sleep_ideal": "7 to 8 hours",
            "exercise": "20-30 minutes of low-impact movement (gentle walking, joint mobility stretches, light pranayama).",
            "avoid": "Hard-to-chew vegetables, heavily oiled pickles, high-sodium papads, and gas-forming heavy lentils.",
            "days": {
                "Monday": {"Breakfast": "Warm Ragi Ambali (porridge) with thin buttermilk.", "Lunch": "Soft-cooked rice, ridge gourd dal, and curd.", "Snack": "Stewed apple (soft).", "Dinner": "Thin vegetable khichdi (easy to digest)."},
                "Tuesday": {"Breakfast": "Soft oats porridge with milk.", "Lunch": "Mashed brown rice with bottle gourd (lauki) curry and moong dal.", "Snack": "Warm papaya pieces.", "Dinner": "Soft broken wheat dahlia upma."},
                "Wednesday": {"Breakfast": "Well-cooked idli with light tomato chutney.", "Lunch": "Soft jowar roti soaked in dal, with mashed ash gourd sabzi.", "Snack": "A cup of warm milk with turmeric.", "Dinner": "Clear vegetable broth with soft boiled paneer."},
                "Thursday": {"Breakfast": "Finger millet flour rava upma (very soft).", "Lunch": "Mashed rice, curd, and a side of soft boiled ivy gourd.", "Snack": "One ripe banana.", "Dinner": "Moong dal soup with an idli."},
                "Friday": {"Breakfast": "Warm ragi malt (sweet version with little jaggery).", "Lunch": "Soft rice, drumstick sambar, and mashed carrot subzi.", "Snack": "Thin curd water.", "Dinner": "Oats porridge with no sugar, spices or oil."},
                "Saturday": {"Breakfast": "Soft-cooked vermicelli with carrots.", "Lunch": "Soft whole wheat chapati mashed inside yellow dal.", "Snack": "Stewed pear or warm papaya.", "Dinner": "Little millet khichdi cooked with extra water."},
                "Sunday": {"Breakfast": "Moong dal green chilla (soft texturized).", "Lunch": "Mashed rice, light cumin flavored rasam and curd.", "Snack": "Coconut water.", "Dinner": "Warm vegetable stock soup with soft idli."}
            }
        },
        "Non-Vegetarian": {
            "sleep_ideal": "7 to 8 hours",
            "exercise": "20-30 minutes of low-impact movement (gentle walking, joint mobility stretches, breathing exercises).",
            "avoid": "Hard-to-chew meats, highly spiced non-veg curries, heavily oiled pickles, and processed cold cuts.",
            "days": {
                "Monday": {"Breakfast": "Scrambled egg whites with soft warm milk.", "Lunch": "Soft-cooked rice with fish bone broth and curd.", "Snack": "Stewed apple (soft).", "Dinner": "Thin chicken khichdi (easy to digest)."},
                "Tuesday": {"Breakfast": "Soft oats porridge with milk and egg drop.", "Lunch": "Mashed brown rice with chicken dal broth.", "Snack": "Warm papaya pieces.", "Dinner": "Soft dahlia with shredded chicken."},
                "Wednesday": {"Breakfast": "Well-cooked idli with soft egg bhurji.", "Lunch": "Soft jowar roti soaked in chicken soup.", "Snack": "A cup of warm milk with turmeric.", "Dinner": "Clear chicken broth with boiled egg whites."},
                "Thursday": {"Breakfast": "Finger millet flour soft upma with egg white crumbs.", "Lunch": "Mashed rice, curd, and boiled soft fish.", "Snack": "One ripe banana.", "Dinner": "Moong dal soup with a soft chicken idli."},
                "Friday": {"Breakfast": "Warm ragi malt with egg whites.", "Lunch": "Soft rice, simple fish broth, and mashed carrot subzi.", "Snack": "Thin curd water.", "Dinner": "Oats porridge cooked in water with egg drop."},
                "Saturday": {"Breakfast": "Soft-cooked vermicelli with egg white drop.", "Lunch": "Soft chapati mashed inside chicken stew.", "Snack": "Stewed pear.", "Dinner": "Little millet chicken khichdi cooked with extra water."},
                "Sunday": {"Breakfast": "Moong dal chilla with soft chicken mince.", "Lunch": "Mashed rice, light chicken clear soup and curd.", "Snack": "Coconut water.", "Dinner": "Warm chicken stock soup with soft idli."}
            }
        }
    }
}

# =========================================================================
# 2. HEALTH CONDITIONS DATABASE (FROM HANDWRITTEN SHEET b34f0876-1131-45ff-8e3b-36f642de263b)
# =========================================================================
CLINICAL_RULES = {
    "Normal / Baseline": {
        "advice": "Keep maintaining a great, balanced, age-appropriate health routine!",
        "avoid_add": [],
        "swap_rules": {}
    },
    "Diabetes (Sugar)": {
        "advice": "⚠️ **Diabetes Protocol:** Avoid white sugar, maida, and refined white rice entirely. Prioritize complex carbs like Foxtail Millet or Jowar. Restrict heavy starches and high-sugar fruits.",
        "avoid_add": ["White sugar", "White rice", "Maida", "Potato", "Fizzy fruit juices", "Ice cream"],
        "swap_rules": {
            "rice": "brown rice / foxtail millet (sugar control)",
            "rice gruel": "barley water (sugar control)",
            "Roti": "Jowar Roti (low GI)",
            "chapati": "Jowar/Bajra Roti (low GI)",
            "chapatis": "Jowar Rotis",
            "jaggery": "unsweetened organic stevia / raw nuts",
            "sweet": "unsweetened / low-sugar option",
            "semiya": "foxtail millet vermicelli (unsweetened)"
        }
    },
    "Hypertension (BP)": {
        "advice": "⚠️ **Hypertension Protocol:** Restrict dietary sodium strictly. Remove all packaging-heavy foods, pickles, papads, and namkeens. Focus on high-potassium foods (potassium stabilizes blood vessel pressure).",
        "avoid_add": ["Table salt", "Commercial pickles", "Salted papads", "Processed cheese", "Salted snacks"],
        "swap_rules": {
            "salt": "zero-sodium herb substitute",
            "chana": "unsalted roasted chana",
            "nuts": "unsalted raw almonds",
            "curd": "unsalted thin curd",
            "sambar": "low-sodium unsalted sambar",
            "dal": "low-sodium unsalted dal"
        }
    },
    "Tuberculosis (TB)": {
        "advice": "⚠️ **Tuberculosis Protocol:** High-protein, nutrient-dense diet is mandatory to offset muscle wasting. Increase consumption of healthy fats (ghee, seeds) and easily absorbable minerals.",
        "avoid_add": ["Refined oil", "Alcohol", "Raw unpasteurized milk", "Fasting", "Carbonated drinks"],
        "swap_rules": {
            "rice": "protein-enriched brown rice (with dal mix)",
            "Snack": "High-protein seed mix & double eggs (if non-veg) or paneer",
            "water": "warm turmeric water",
            "fruit": "nutrient-dense banana with dry fruits"
        }
    },
    "Thyroid": {
        "advice": "⚠️ **Thyroid Protocol:** Regulate your metabolism. Strictly restrict raw goitrogenic vegetables (like raw cabbage, raw cauliflower, raw kale). Fully cooking, baking, or steaming these elements destroys goitrogenic enzymes.",
        "avoid_add": ["Raw cabbage", "Raw broccoli", "Raw cauliflower", "Raw kale", "Unfermented soy"],
        "swap_rules": {
            "salad": "cooked carrot beetroot stir-fry",
            "veggies": "thoroughly steamed/cooked vegetables",
            "vegetable": "fully cooked gourd vegetable",
            "peanuts": "selenium-rich walnuts"
        }
    },
    "Chickenpox": {
        "advice": "⚠️ **Chickenpox Protocol:** Emphasize soft, cool, easily chewable, and non-acidic foods to soothe potential oral lesions and lesions in the GI tract. Maximize lysine-rich foods.",
        "avoid_add": ["Chili powder", "Raw citrus fruits", "Salty chips", "Hot spicy curries", "Tough fibrous meat"],
        "swap_rules": {
            "Breakfast": "Cool ragi malt or oats porridge with milk",
            "Snack": "Cool mashed banana or sweet coconut water",
            "Lunch": "Soft curd rice (cool, not hot)",
            "Dinner": "Mashed soft dal with soft-cooked rice"
        }
    },
    "Headache / Migraine": {
        "advice": "⚠️ **Headache/Migraine Protocol:** Remove vascular triggers. Avoid all amine-rich foods (aged cheeses), cured meats, MSG, and aspartame. Focus on high-magnesium items to stabilize intracranial blood vessels.",
        "avoid_add": ["Aged cheese", "Nitrite-cured meats", "MSG / Chinese sauces", "Artificial sweeteners", "Excess cocoa"],
        "swap_rules": {
            "cheese": "fresh homemade paneer",
            "peanuts": "magnesium-rich pumpkin seeds",
            "Snack": "Magnesium-dense pumpkin seeds",
            "chapatis": "magnesium-dense whole wheat chapatis"
        }
    },
    "PCOD": {
        "advice": "⚠️ **PCOD Protocol:** Focus heavily on clearing androgens and normalizing insulin-like growth factors (IGF-1). Eliminate commercial dairy products. Focus on raw flaxseeds and pumpkin seeds.",
        "avoid_add": ["Commercial milk", "Full-fat commercial dairy", "Processed white flour", "Soy isolates"],
        "swap_rules": {
            "milk": "almond/coconut milk",
            "curd": "dairy-free almond curd",
            "dairy": "vegan plant-based alternatives",
            "butter": "cold-pressed olive oil",
            "ghee": "flaxseed oil",
            "cheese": "grilled firm tofu"
        }
    },
    "Malaria": {
        "advice": "⚠️ **Malaria Protocol:** High-carbohydrate, high-protein, easily digestible foods are required to assist the liver and fight heavy infection. Ensure rigorous hydration with electrolytes.",
        "avoid_add": ["Heavy red meat", "Deep fried foods", "High-fiber raw salad", "Spicy masalas"],
        "swap_rules": {
            "Lunch": "Soft-cooked white rice with simple yellow dal soup (easy digesting)",
            "Snack": "Fresh tender coconut water or sweet apple puree",
            "Dinner": "Rice gruel with a touch of ghee and soft carrots"
        }
    },
    "Stomach Pain / Motions / Vomiting / Nausea": {
        "advice": "⚠️ **Gastrointestinal Distress Protocol (Acute GI Rest):** Adopt a highly restricted Bland/BRAT regimen (Bananas, soft Rice, Applesauce, Toast). Eliminate raw items, heavy fats, dairy, and strong spices to minimize gastric peristalsis.",
        "avoid_add": ["Raw salads", "Chili powder", "Commercial milk", "Heavy oils", "Ghee", "Fibrous lentils"],
        "swap_rules": {
            "Breakfast": "Diluted thin warm ragi water or single dry toast",
            "Lunch": "Double-cooked soft white rice with diluted thin curd or rasam water",
            "Dinner": "Light watery rice gruel with a tiny pinch of salt",
            "Snack": "Soft ripe banana or stewed peeled applesauce",
            "curd": "highly diluted curd whey water",
            "veggies": "soft carrots (peeled, boiled & mashed)",
            "paneer": "soft steamed tofu cubes (very light)"
        }
    },
    "Uterine Fibroids (Ribroids)": {
        "advice": "⚠️ **Uterine Fibroids Protocol:** Estrogen dominance fuels fibroid tissues. Eliminate saturated animal fats and red meats. Increase cruciferous options (must be fully cooked/steamed) containing indole-3-carbinol to bind toxic estrogens.",
        "avoid_add": ["Red meat", "Full-fat dairy", "Alcohol", "Processed refined sugars"],
        "swap_rules": {
            "vegetable": "steamed/cooked cruciferous vegetable (broccoli/cabbage)",
            "veggies": "steamed broccoli and cauliflower",
            "chicken": "steamed skinless fish",
            "paneer": "steamed organic tofu"
        }
    },
    "Ovarian Cyst": {
        "advice": "⚠️ **Ovarian Cyst Protocol:** Maintain strict hormonal balance. Lower estrogen burden while boosting cellular insulin receptors. Integrate anti-inflammatory fats (omega-3 from seeds).",
        "avoid_add": ["Refined carbohydrates", "Saturated animal fats", "Unfermented soy", "Sugar syrups"],
        "swap_rules": {
            "milk": "chia seed coconut infusion",
            "ghee": "cold-pressed avocado oil",
            "sweet": "steamed apple slices with cinnamon"
        }
    },
    "Seizures / Fits (Sizer/Fids)": {
        "advice": "⚠️ **Seizures / Fits Protocol:** Support neurotransmitter stability. Restrict high-GI glucose spikes that cause erratic neuronal activity. Focus on clean fats and proteins.",
        "avoid_add": ["High-fructose corn syrup", "Refined sugar desserts", "MSG", "Caffeine-heavy energy drinks"],
        "swap_rules": {
            "rice": "high-protein cooked quinoa / scrambled egg whites",
            "bread": "almond flour keto-bread substitute",
            "Roti": "almond-flaxseed low-carb flatbread",
            "Snack": "Handful of healthy raw walnuts and pumpkin seeds"
        }
    },
    "Weight Loss": {
        "advice": "⚠️ **Weight Loss Protocol:** Enhance satiety and regulate metabolic speed. Drink 1 glass of unsweetened ragi ambali mixed with buttermilk 20 minutes before core meals to block mechanical overeating.",
        "avoid_add": ["Deep-fried items", "Bakery sweets", "Late night calorie dense meals", "Sugary tea/coffee"],
        "swap_rules": {
            "sweet": "roasted unsalted makhana",
            "banana": "fiber-dense green apples",
            "rice": "high-protein quinoa or foxtail millet",
            "upma": "multi-vegetable oats upma"
        }
    },
    "Weight Gain / Malnutrition": {
        "advice": "⚠️ **Weight Gain / Malnutrition Protocol:** Ensure nutrient density and a healthy caloric surplus. Integrate healthy lipids (ghee, nuts, seeds, full-fat dairy) and structured high-quality protein matrices.",
        "avoid_add": ["Junk trans-fats", "Carbonated diet sodas", "Empty sugar calories", "Oiled roadside fried items"],
        "swap_rules": {
            "buttermilk": "creamy whole milk",
            "thin": "thick and nutrient-dense",
            "Snack": "Ragi porridge prepared with whole milk, honey, and nuts",
            "Lunch": "Ghee-roasted grains served with dense dal/paneer and cream"
        }
    },
    "Cold / Cough": {
        "advice": "⚠️ **Cold / Cough Protocol:** Soothe inflamed bronchial tracts. Eliminate all chilled beverages, ice creams, and excessive mucus-producing dairy. Emphasize warming bioactives (gingerols, curcumin, piperine).",
        "avoid_add": ["Chilled drinks", "Ice creams", "Yogurt / Curd from fridge", "Cold raw salads"],
        "swap_rules": {
            "curd": "warm peppercorn clear rasam",
            "buttermilk": "warm ginger herbal infusion",
            "Snack": "Roasted makhana with organic turmeric and black pepper",
            "Dinner": "Steaming hot vegetable soup with ginger and garlic"
        }
    }
}

# Priority mapping to resolve conflicting rules (e.g. GI distress overrides high-fiber Diabetes rules)
CLINICAL_PRIORITY = {
    "Normal / Baseline": 0,
    "Diabetes (Sugar)": 1,
    "Hypertension (BP)": 1,
    "Thyroid": 1,
    "PCOD": 1,
    "Uterine Fibroids (Ribroids)": 1,
    "Ovarian Cyst": 1,
    "Seizures / Fits (Sizer/Fids)": 1,
    "Weight Loss": 1,
    "Tuberculosis (TB)": 2,
    "Malaria": 2,
    "Chickenpox": 2,
    "Cold / Cough": 2,
    "Weight Gain / Malnutrition": 2,
    "Stomach Pain / Motions / Vomiting / Nausea": 3 # Acute GI has the highest override priority
}

# =========================================================================
# 3. CLINICAL DIET GENERATOR (MULTIPLE-SELECT CONFLICT RESOLUTION)
# =========================================================================
def compile_clinical_diet_plan(age, diet_pref, selected_issues):
    # Fetch base demographic menu directly by age and diet preference (fixes previous loop error)
    base = BASE_NUTRITION[age][diet_pref]
    
    # Clone to prevent modifying static dictionary reference
    compiled_days = {}
    for day, meals in base["days"].items():
        compiled_days[day] = meals.copy()

    # Resolve pathologies in priority order so highest overrides (e.g. Gastro BRAT) win at the end
    active_issues = [issue for issue in selected_issues if issue != "Normal / Baseline"]
    if not active_issues:
        active_issues = ["Normal / Baseline"]
    else:
        # Sort based on the clinical priority values
        active_issues.sort(key=lambda x: CLINICAL_PRIORITY.get(x, 1))

    combined_advice = []
    combined_avoid = set()

    for issue in active_issues:
        rule_data = CLINICAL_RULES[issue]
        if issue != "Normal / Baseline":
            combined_advice.append(rule_data["advice"])
            # Merge avoid rules
            for item in rule_data.get("avoid_add", []):
                combined_avoid.add(item)
            
            # Apply dynamic regex meal adjustments
            swap_rules = rule_data.get("swap_rules", {})
            for day, meals in compiled_days.items():
                for meal_type, meal_desc in meals.items():
                    # If the entire meal category is overridden (e.g. BRAT diet complete swaps)
                    if meal_type in swap_rules:
                        compiled_days[day][meal_type] = swap_rules[meal_type]
                    else:
                        temp_desc = meal_desc
                        for old_word, new_word in swap_rules.items():
                            pattern = re.compile(re.escape(old_word), re.IGNORECASE)
                            temp_desc = pattern.sub(new_word, temp_desc)
                        compiled_days[day][meal_type] = temp_desc

    # Clean compile string advice
    if not combined_advice:
        final_advice = CLINICAL_RULES["Normal / Baseline"]["advice"]
    else:
        final_advice = "\n\n".join(combined_advice)

    # Clean compile avoid list
    base_avoid = base["avoid"]
    if combined_avoid:
        final_avoid = f"{base_avoid} AND strictly avoid: {', '.join(sorted(list(combined_avoid)))}."
    else:
        final_avoid = base_avoid

    return {
        "sleep": base["sleep_ideal"],
        "exercise": base["exercise"],
        "avoid": final_avoid,
        "days": compiled_days,
        "advice": final_advice
    }

# =========================================================================
# 4. CHATBOT MULTI-KEYWORD MAPPER
# =========================================================================
EXTENDED_CHAT_RULES = {
    ("gastric", "acidity", "reflux", "gas", "bloating", "stomach pain", "motions", "vomiting", "nausea"): (
        "### 🤢 Gastric, Reflux & Stomach Pain Relief\n"
        "**🍛 Food Core:** Drink cold unsalted buttermilk with roasted cumin powder. Include alkaline ash gourd juice. Avoid raw red chili, citrus, and unsoaked heavy lentils.\n"
        "**🏃‍♂️ Movement:** Practice *Vajrasana* for 5-10 minutes post-meal to support digestion.\n"
        "**⏰ Rest:** Elevate head by 4 inches during sleep. Do not lie down within 2 hours of a meal."
    ),
    ("heart", "bp", "hypertension", "cardiovascular", "cholesterol", "heart attack"): (
        "### 🫀 Hypertension & Cardiac Rehab\n"
        "**🍛 Food Core:** Strictly restrict table salt. Avoid processed pickles, papads, and re-heated vegetable oils. Focus on potassium (coconut water, banana) and soluble beta-glucan fibers (oats).\n"
        "**🏃‍♂️ Movement:** 30 minutes of low-impact walking. Strictly avoid sudden heavy strain.\n"
        "**⏰ Rest:** Ensure 7-8 hours. Sleep deprivation spikes vascular cortisol levels."
    ),
    ("diabetes", "sugar", "glucose", "insulin"): (
        "### 🩸 Diabetes & Insulin Regulation\n"
        "**🍛 Food Core:** Replace refined white rice and maida with Jowar rotis or Foxtail Millet. Focus on high-fiber bitter vegetables (bitter gourd, okra, ivy gourd).\n"
        "**🏃‍♂️ Movement:** Walk for 15 minutes immediately after main meals to sweep glucose out of the blood stream."
    ),
    ("pcod", "pcos", "ovarian", "cyst", "irregular periods"): (
        "### 🦋 PCOD & Ovarian Cyst Hormonal Recovery\n"
        "**🍛 Food Core:** Adopt low-GI ancient grains. Strictly eliminate commercial dairy (IGF-1 triggers). Consume pumpkin and flaxseeds to clear systemic androgens.\n"
        "**🏃‍♂️ Movement:** Moderate strength/resistance workouts 3 times a week to improve cellular insulin sensitivity."
    ),
    ("fibroids", "uterine fibroids", "uterus", "heavy bleeding", "ribroids"): (
        "### 🩸 Estrogen Detox & Fibroid Shrinkage\n"
        "**🍛 Food Core:** Heavily consume cooked cruciferous greens (broccoli, cabbage, kale) to leverage Indole-3-Carbinol for liver estrogen binding. Strictly avoid red meat and full-fat dairy."
    ),
    ("headache", "migraine", "throbbing", "migraines"): (
        "### 🧠 Headache & Migraine Trigger Elimination\n"
        "**🍛 Food Core:** Purge vasoactive compounds (aged cheese, nitrites in processed meats, MSG, aspartame). Eat magnesium-heavy pumpkin and pumpkin seeds."
    ),
    ("thyroid", "hypothyroid", "tsh", "thyriod", "thypoid"): (
        "### 🦋 Thyroid Metabolic Restoration\n"
        "**🍛 Food Core:** Eat selenium-dense brazil nuts or walnuts. Avoid raw uncooked crucifers (cabbage, kale) to safeguard TPO enzymes. Eat cooked grains."
    ),
    ("weight loss", "lose weight", "dieting", "fat loss"): (
        "### 📉 Sustainable Caloric Deficit\n"
        "**🍛 Food Core:** Consume unsweetened Ragi Java with buttermilk before meals to block mechanical overeating. Avoid evening refined snacks."
    ),
    ("seizures", "fits", "sizer", "fids"): (
        "### 🧠 Neurotransmitter Stabilization (Seizures Protocol)\n"
        "**🍛 Food Core:** Lower high-GI glucose spikes. Emphasize low-carb keto-friendly nutrition: high healthy fats (nuts, seeds) and balanced clean proteins. Avoid refined sugar and MSG."
    ),
    ("tb", "tuberculosis", "chickenpox", "malaria"): (
        "### 🦠 Acute Infectious Pathology Recovery (TB, Malaria, Chickenpox)\n"
        "**🍛 Food Core:** Prioritize high-protein absorption and cellular repair. Drink cool, soft fluids for Chickenpox, and high-energy broths for TB and Malaria. Avoid raw heavy fiber."
    ),
    ("malnutrition", "weight gain", "cold", "cough"): (
        "### 🌡️ Cold, Cough & Malnutrition Interventions\n"
        "**🍛 Food Core:** Incorporate warm bone broths or spiced rasam infusions for respiratory issues. For malnutrition, provide ghee, honey, whole milk, and seed powders."
    )
}

# =========================================================================
# 5. STREAMLIT FRAMEWORK SETUP
# =========================================================================
st.set_page_config(page_title="Demographic Clinical Diet Engine", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Select Multi-Generation Clinical Diet Engine")
st.write("An advanced multi-select rules processor synthesizing overlapping pathologies derived from clinical reference b34f0876-1131-45ff-8e3b-36f642de263b.")

# Interface Tabs
tab1, tab2 = st.tabs(["📋 Clinical Lifestyle Assessment", "💬 Knowledge Chat Interrogator"])

# =========================================================================
# TAB 1: PERSISTENT ASSESSMENT FORM
# =========================================================================
with tab1:
    st.write("### 📝 Patient Parameters Intake")
    
    with st.form("health_assessment_form"):
        col1, col2 = st.columns(2)
        with col1:
            age_group = st.selectbox("👉 Select Age Group Bracket:", list(BASE_NUTRITION.keys()))
            diet_pref = st.selectbox("👉 Select Dietary Preference Segment:", ["Vegetarian", "Non-Vegetarian"])
            sleep_hours = st.number_input("👉 Enter Patient Sleep Hours (Daily):", min_value=1, max_value=24, value=7, step=1)
        with col2:
            # Multi-select input for choosing multiple pathologies simultaneously
            health_issues = st.multiselect(
                "👉 Select All Applicable Health Concerns (b34f0876-1131-45ff-8e3b-36f642de263b):",
                options=list(CLINICAL_RULES.keys()),
                default=["Normal / Baseline"]
            )
            routine = st.selectbox("👉 Select Activity Profile Classification:", ["Sedentary", "Moderate Active", "Heavy Active"])
            
        submit_button = st.form_submit_button(label="⚡ Compile Demographically Modified Diet Plan")

    if submit_button:
        # Standardize empty selection to normal baseline
        if not health_issues:
            health_issues = ["Normal / Baseline"]
            
        # Generate personalized, multi-condition modified diet plan
        result_plan = compile_clinical_diet_plan(age_group, diet_pref, health_issues)
        
        st.markdown("---")
        st.markdown(f"## 📋 Rule-Driven Health & Lifestyle Blueprint ({diet_pref})")
        st.write(f"**Synthesized Pathologies:** {', '.join(health_issues)}")
        
        # Validate sleep ranges
        sleep_comment = "✅ Current sleep duration satisfies demographic standards."
        ideal_str = result_plan["sleep"]
        if "to" in ideal_str:
            ideal_min = int(ideal_str.split()[0])
            if sleep_hours < ideal_min:
                sleep_comment = f"⚠️ Sleep Deficit Detected. Your group profile demands {ideal_str}. Increase duration."
                
        # Display Metrics Blocks
        st.info(f"**⏰ Sleep Evaluation Status:** {sleep_comment}")
        st.success(f"**🏃‍♂️ Prescribed Activity Protocol:** {result_plan['exercise']}")
        
        # Display merged advice blocks sequentially
        st.warning(result_plan["advice"])
        
        st.markdown("### 🍛 Combined & Modified 7-Day Clinical Diet Schedule")
        st.write(f"The structural menus have been dynamically synthesized and recursively adjusted for **{age_group}** requirements:")
        
        # Build layout grid
        table_data = []
        for day in WEEK_DAYS:
            meals = result_plan["days"][day]
            table_data.append({
                "Day Order": day,
                "Breakfast Combo": meals["Breakfast"],
                "Lunch Core": meals["Lunch"],
                "Evening Snack Choice": meals["Snack"],
                "Dinner Option": meals["Dinner"]
            })
            
        st.table(table_data)
        st.error(f"🚫 **Strict Avoid List (Amended):** {result_plan['avoid']}")

# =========================================================================
# TAB 2: LIVE KNOWLEDGE CHAT
# =========================================================================
with tab2:
    st.write("### 💬 Clinical Knowledge Bot")
    st.caption("Ask specific metabolic, infection, or general health questions (e.g., 'Diabetes rules', 'fits advice', 'malaria food guidelines').")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Ask a clinical query..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        bot_response = "🤖 I am a clinical rule assistant. Try asking about 'Diabetes', 'PCOD', 'Fibroids', 'Seizures', 'Malaria', or 'TB' to trigger guidelines."
        
        normalized_query = prompt.lower()
        for key_tuple, descriptive_advice in EXTENDED_CHAT_RULES.items():
            if any(re.search(rf"\b{word}\b", normalized_query) for word in key_tuple):
                bot_response = descriptive_advice
                break
                
        with st.chat_message("assistant"):
            st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

```
