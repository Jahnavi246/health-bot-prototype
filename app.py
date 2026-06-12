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

# Specific rules for health concerns
CLINICAL_RULES = {
    "Normal": {
        "advice": "Keep maintaining a great, balanced, age-appropriate health routine!",
        "modifiers": {}
    },
    "Diabetes (Sugar)": {
        "advice": "⚠️ **Diabetes Protocol:** Strictly avoid all white sugar, maida, and refined white rice. Replace white rice with Foxtail Millet or Brown Rice, and chapatis with Jowar or Bajra rotis. Prioritize high-fiber non-starchy vegetables (okra, bitter gourd, ivy gourd) and ensure a 15-minute post-meal walk.",
        "avoid_add": ["White sugar", "White rice", "Maida", "Potato", "Ice cream", "Fruit juices"],
        "swap_rules": {
            "rice": "brown rice / foxtail millet (sugar control)",
            "rice gruel": "barley water (sugar control)",
            "Roti": "Jowar Roti (low GI)",
            "chapati": "Jowar/Bajra Roti (low GI)",
            "chapatis": "Jowar Rotis",
            "jaggery": "unsweetened stevia / raw nuts",
            "sweet": "unsweetened / low-sugar",
            "semiya": "foxtail millet vermicelli (unsweetened)"
        }
    },
    "PCOD": {
        "advice": "⚠️ **PCOD Protocol (Decoupled from Diabetes):** Focus on restoring ovarian insulin sensitivity. Eliminate all commercial dairy products and high-IGF elements. Incorporate healthy fats like raw flaxseeds, chia seeds, and pumpkin seeds. Ensure regular resistance training to build muscle mass.",
        "avoid_add": ["Commercial milk", "Full-fat dairy", "Bakery items", "Soy products", "High-fat red meat"],
        "swap_rules": {
            "milk": "almond/coconut milk",
            "curd": "dairy-free almond curd",
            "dairy": "vegan alternatives",
            "butter": "cold-pressed olive oil",
            "ghee": "flaxseed oil",
            "cheese": "grilled tofu"
        }
    },
    "Hypertension (BP)": {
        "advice": "⚠️ **Hypertension Protocol:** Strictly restrict sodium intake to under 1500mg daily. Completely avoid commercial pickles, salted papads, packaged snacks, and canned soups. Focus on potassium-rich foods (coconut water, ash gourd, banana) to lower blood pressure.",
        "avoid_add": ["Pickles", "Papads", "Canned soups", "Baking soda", "Table salt", "Processed cheese"],
        "swap_rules": {
            "salt": "zero-sodium potassium salt substitute",
            "chana": "unsalted roasted chana",
            "nuts": "unsalted raw almonds",
            "curd": "unsalted thin curd",
            "sambar": "low-sodium unsalted sambar",
            "dal": "low-sodium unsalted dal"
        }
    },
    "Uterine Fibroids": {
        "advice": "⚠️ **Uterine Fibroids Protocol:** Estrogen dominance accelerates fibroid tissue progression. Strictly eliminate red meat, full-fat dairy, and alcohol. Optimize liver detoxification by adding heavy cruciferous vegetables (cooked broccoli, cabbage, brussels sprouts) which contain Indole-3-Carbinol to bind and excrete excess estrogen.",
        "avoid_add": ["Red meat", "Pork", "Lamb", "Full-fat dairy", "Unfermented soy", "Excessive caffeine"],
        "swap_rules": {
            "vegetable": "cruciferous vegetable (broccoli/cabbage)",
            "veggies": "cruciferous greens (kale/broccoli)",
            "chicken": "steamed white fish (estrogen friendly)",
            "paneer": "steamed organic tofu (low estrogen)"
        }
    },
    "Post-Heart Attack": {
        "advice": "⚠️ **Cardiac Rehab Protocol:** Enforce clinical-grade cardiovascular protection. Strictly eliminate all saturated fats, trans-fats, re-heated oils, and saturated dairy. Restrict sodium strictly. Ensure heavy intake of soluble beta-glucan fibers (Oats) and anti-inflammatory Omega-3 fatty acids (soaked walnuts, flaxseeds). Workouts must be low impact.",
        "avoid_add": ["Re-heated oil", "Vanaspati ghee", "Butter", "Red meat", "Processed meats", "High-salt items"],
        "swap_rules": {
            "rice": "soluble oats fiber (cardiac support)",
            "Roti": "oats-wheat chapati (Omega-3 rich)",
            "ghee": "cold-pressed flaxseed oil",
            "butter": "avocado mash",
            "chicken": "Omega-3 rich boiled fish"
        }
    },
    "Nausea / Vomiting / Stomach Pain": {
        "advice": "⚠️ **Gastrointestinal Distress Protocol:** Allow maximum mechanical rest to the gastric lining. Follow a strict, easy-to-digest Bland/BRAT diet (Bananas, soft white Rice, Applesauce, Toast). Absolutely eliminate all raw vegetables, fats, spices, and dairy. Sip warm ginger water to naturally block gastric emetic receptors.",
        "avoid_add": ["Spices", "Chili powder", "Butter", "Ghee", "Milk", "Cheese", "Fats", "Raw vegetables"],
        "swap_rules": {
            "Breakfast": "Soft cooked white rice with diluted thin curd (or warm ginger water)",
            "Lunch": "Mashed soft yellow moong dal khichdi (no ghee, no spices, no oil)",
            "Dinner": "Double-boiled thin rice gruel with a tiny pinch of salt",
            "Snack": "Soft ripe banana or stewed peeled applesauce",
            "curd": "water-diluted thin curd",
            "veggies": "soft carrots (boiled & mashed)",
            "paneer": "boiled soft tofu cubes"
        }
    },
    "Headache / Migraine": {
        "advice": "⚠️ **Migraine/Headache Protocol:** Prevent neurogenic vascular triggers. Strictly purge all vasoactive amines: aged cheeses (high in tyramine), cured meats (nitrites), MSG-heavy processed foods, and artificial sweeteners (aspartame). Prioritize heavy magnesium sources (pumpkin seeds, flaxseeds, leafy greens) to stabilize cranial blood vessels.",
        "avoid_add": ["Aged cheese", "Cured meats", "MSG", "Chinese sauces", "Artificial sweeteners", "Vinegar", "Chocolate"],
        "swap_rules": {
            "cheese": "freshly made paneer",
            "peanuts": "magnesium-rich pumpkin seeds",
            "Snack": "A handful of raw pumpkin seeds",
            "chapatis": "magnesium-dense whole wheat chapatis"
        }
    },
    "Thyroid": {
        "advice": "⚠️ **Thyroid Protocol:** Regulate core metabolic pathways. Strictly avoid raw goitrogenic vegetables (uncooked cabbage, raw kale, uncooked cauliflower, raw broccoli) which inhibit thyroid peroxidase. Bake or steam these foods entirely to neutralize goitrogens. Prioritize selenium and iodine sources.",
        "avoid_add": ["Raw cabbage", "Raw broccoli", "Raw cauliflower", "Raw kale", "Excess soy protein"],
        "swap_rules": {
            "salad": "cooked carrot beetroot stir-fry",
            "veggies": "thoroughly steamed/cooked vegetables",
            "vegetable": "fully cooked gourd vegetable",
            "peanuts": "selenium-rich brazil nuts or walnuts"
        }
    },
    "Weight Loss": {
        "advice": "⚠️ **Weight Loss Protocol:** Optimize basal satiety limits. Drink 1 glass of unsweetened Ragi Java prepared with diluted buttermilk 20 minutes before lunch and dinner. Replace high-GI evening carbs with light cucumber sticks or raw roasted makhana.",
        "avoid_add": ["Sugary sweets", "Midnight heavy snacks", "Refined deep-fried pakodas", "Fizzy sodas"],
        "swap_rules": {
            "sweet": "roasted unsalted makhana",
            "banana": "fiber-dense green apples",
            "rice": "high-protein quinoa or foxtail millet",
            "upma": "multi-vegetable oats upma"
        }
    }
}

# =========================================================================
# 2. CLINICAL DIET GENERATOR (DYNAMIC COMPILER & MODIFIER ENGINE)
# =========================================================================
def compile_clinical_diet_plan(age, diet_pref, health_issue):
    # Fetch base demographic menu
    base = BASE_NUTRITION[age][diet_pref]
    
    # Clone to prevent modifying static dictionary reference
    compiled_days = {}
    for day, meals in base["days"].items():
        compiled_days[day] = meals.copy()
        
    rule_data = CLINICAL_RULES[health_issue]
    
    # Apply pathological replacements if condition is not "Normal"
    if health_issue != "Normal":
        swap_rules = rule_data["swap_rules"]
        
        for day, meals in compiled_days.items():
            for meal_type, meal_desc in meals.items():
                
                # Check for absolute layout replacement overrides (e.g., BRAT overrides for Nausea)
                if meal_type in swap_rules:
                    compiled_days[day][meal_type] = swap_rules[meal_type]
                else:
                    # Apply keyword regex text replacements
                    temp_desc = meal_desc
                    for old_word, new_word in swap_rules.items():
                        # Case-insensitive replacement
                        pattern = re.compile(re.escape(old_word), re.IGNORECASE)
                        temp_desc = pattern.sub(new_word, temp_desc)
                    compiled_days[day][meal_type] = temp_desc
                    
    # Generate avoid list
    base_avoid = base["avoid"]
    additional_avoid = rule_data.get("avoid_add", [])
    if additional_avoid:
        final_avoid = f"{base_avoid} AND strictly avoid: {', '.join(additional_avoid)}."
    else:
        final_avoid = base_avoid
        
    return {
        "sleep": base["sleep_ideal"],
        "exercise": base["exercise"],
        "avoid": final_avoid,
        "days": compiled_days,
        "advice": rule_data["advice"]
    }

# =========================================================================
# 3. CHATBOT MULTI-KEYWORD REGEX MAPPER
# =========================================================================
EXTENDED_CHAT_RULES = {
    ("gastric", "acidity", "reflux", "gas", "bloating", "stomach pain"): (
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
        "### 🦋 PCOD Hormonal Recovery\n"
        "**🍛 Food Core:** Adopt low-GI ancient grains. Strictly eliminate commercial dairy (IGF-1 triggers). Consume pumpkin and flaxseeds to clear systemic androgens.\n"
        "**🏃‍♂️ Movement:** Moderate strength/resistance workouts 3 times a week to improve cellular insulin sensitivity."
    ),
    ("fibroids", "uterine fibroids", "uterus", "heavy bleeding"): (
        "### 🩸 Estrogen Detox & Fibroid Shrinkage\n"
        "**🍛 Food Core:** Heavily consume cooked cruciferous greens (broccoli, cabbage, kale) to leverage Indole-3-Carbinol for liver estrogen binding. Strictly avoid red meat and full-fat dairy."
    ),
    ("nausea", "vomiting", "sick", "throw up", "upset stomach"): (
        "### 🤢 Nausea & Stomach Irritation Rescue\n"
        "**🍛 Food Core:** Strictly follow the Bland BRAT regimen (Banana, Rice, Applesauce, Toast). Avoid all dairy, butter, oils, and hot chilies. Sip fresh warm ginger tea slowly."
    ),
    ("headache", "migraine", "throbbing", "migraines"): (
        "### 🧠 Headache & Migraine Trigger Elimination\n"
        "**🍛 Food Core:** Purge vasoactive compounds (aged cheese, nitrites in processed meats, MSG, aspartame). Eat magnesium-heavy pumpkin and pumpkin seeds."
    ),
    ("thyroid", "hypothyroid", "tsh"): (
        "### 🦋 Thyroid Metabolic Restoration\n"
        "**🍛 Food Core:** Eat selenium-dense brazil nuts or walnuts. Avoid raw uncooked crucifers (cabbage, kale) to safeguard TPO enzymes. Eat cooked grains."
    ),
    ("weight loss", "lose weight", "dieting", "fat loss"): (
        "### 📉 Sustainable Caloric Deficit\n"
        "**🍛 Food Core:** Consume unsweetened Ragi Java with buttermilk before meals to block mechanical overeating. Avoid evening refined snacks."
    )
}

# =========================================================================
# 4. STREAMLIT FRAMEWORK SETUP
# =========================================================================
st.set_page_config(page_title="Demographic Clinical Diet Engine", page_icon="🤖", layout="wide")

st.title("🤖 Rule-Based Multi-Generation Clinical Diet Engine")
st.write("An advanced pathophysiological rules processor automating age-cohort dynamics, dietary restrictions, and split clinical menu swapping.")

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
            health_issue = st.selectbox("👉 Select Primary Medical Concern:", list(CLINICAL_RULES.keys()))
            routine = st.selectbox("👉 Select Activity Profile Classification:", ["Sedentary", "Moderate Active", "Heavy Active"])
            
        submit_button = st.form_submit_button(label="⚡ Compile Demographically Modified Diet Plan")

    if submit_button:
        # Generate personalized modified diet plan
        result_plan = compile_clinical_diet_plan(age_group, diet_pref, health_issue)
        
        st.markdown("---")
        st.markdown(f"## 📋 Rule-Driven Health & Lifestyle Blueprint ({diet_pref} - {health_issue})")
        
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
        st.warning(result_plan["advice"])
        
        st.markdown("### 🍛 Modified 7-Day Clinical Diet Schedule")
        st.write(f"The structural menus have been dynamically updated with specific clinical substitutions for **{age_group}** demands:")
        
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
    st.caption("Ask specific metabolic or dietary questions (e.g., 'Diabetes guidelines', 'PCOD flaxseed benefits', 'BP rules').")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("Ask a clinical query..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        bot_response = "🤖 I am a clinical rule assistant. Try asking about 'Diabetes', 'PCOD', 'Fibroids', 'Migraine', or 'Stomach Pain' to trigger target guidelines."
        
        normalized_query = prompt.lower()
        for key_tuple, descriptive_advice in EXTENDED_CHAT_RULES.items():
            if any(re.search(rf"\b{word}\b", normalized_query) for word in key_tuple):
                bot_response = descriptive_advice
                break
                
        with st.chat_message("assistant"):
            st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
