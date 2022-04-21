from fitness.models import Exercise
from nutrition.models import Meal
from django.contrib.auth import get_user_model

userModel = get_user_model()

list_of_users = [
            ("Sam", "admin1@admin", "Sam"),
            ("Xin", "admin2@admin", "Xin"),
            ("Thomas", "admin3@admin", "Thomas"),
            ("Syeda", "admin4@admin", "Syeda"),
            ("Mohammed", "admin5@admin", "Mohammed")
            ]
for arg in list_of_users:
    newUser = userModel.objects.create_user(name=arg[0], email=arg[1], password=arg[2])
    newUser.is_superuser = True
    newUser.is_staff = True
    newUser.save()


Exercise.create_ex("Barbell Squat", 0, "Squat Rack", "None", "Quadriceps", "The squat is a fundamental weight training "
                                                                           "exercise for building strength, mass "
                                                                           "sports performance and long-term health.")
Exercise.create_ex("Bench Press", 0, "Bench", "None", "Chest", "The bench press is a fundamental barbell exercise, "
                                                               "notoriously used for bragging rights and as a bench "
                                                               "mark of strength. It is an excellent upper-body "
                                                               "exercise primarily targeting the chest and shoulders "
                                                               "and is one of the great Olympic strength lifts for "
                                                               "developing upper body mass, strength and power.")
Exercise.create_ex("Bent Over Row", 0, "Barbell", "None", "Back", "The barbell bent over row is a fundamental exerise "
                                                                  "that develops strong back muscles.")
Exercise.create_ex("Clean and Jerk", 0, "Barbell", "None", "Quadriceps", "The clean and jerk is an advanced Olympic "
                                                                         "lift and one of the most effective and all "
                                                                         "encompassing strength and performance "
                                                                         "exercises available.")
Exercise.create_ex("Deadlift", 0, "Barbell", "None", "Back", "The barbell deadlift exercise is a highly recommend "
                                                             "weight training exercise for those wanting to build "
                                                             "muscle mass, strength and power. The deadliest movement "
                                                             "gives great bang for the buck and works the body from "
                                                             "head to toe.")
Exercise.create_ex("Biceps Curl", 0, "Dumbell", "None", "Biceps", "Develop biceps size and strength with this basic "
                                                                  "isolation exercise.")
Exercise.create_ex("Farmers Walk", 0, "Dumbell", "None", "Forearms", "The Farmer's Walk is an old school exercise that "
                                                                     "builds grip strength and endurance.")
Exercise.create_ex("Dumbell Pullover", 0, "Dumbell", "None", "Chest", "The dumbbell pullover is a classic bodybuilding "
                                                                      "exercise that targets the upper body with "
                                                                      "particular focus on the chest muscles.")
Exercise.create_ex("Dumbell Shoulder Press", 0, "Dumbell", "None", "Shoulders", "An essential isolation exercise for "
                                                                                "building shoulder size and strength "
                                                                                "in bodybuilding and weight training.")
Exercise.create_ex("Overhead Squat", 0, "Barbell", "None", "Quadriceps", "The overhead squat is an advanced weight "
                                                                         "training movement that is a true test of "
                                                                         "midline control and develops impressive "
                                                                         "athleticism, power and speed skills.")
Exercise.create_ex("Hammer Curl", 0, "Dumbell", "None", "Biceps", "The dumbbell hammer curl is a basic weight training "
                                                                  "exercise for the biceps muscle.")
Exercise.create_ex("Overhead Lunge", 0, "Weighted Plate", "None", "Quadriceps", "The overhead lunge is an advanced "
                                                                                "weighted lunge movement for excellent "
                                                                                "lower body development and shoulder "
                                                                                "strength.")
Exercise.create_ex("Renegade Row", 0, "Dumbell", "None", "Abdominals", "The renegade row builds serious abdominal and "
                                                                       "upper-body strength that will particularly "
                                                                       "develop the core.")
Exercise.create_ex("Sled Pulls", 0, "Rope and Sled", "None", "Back", "Sled pulls are a brutal functional exercise that "
                                                                     "hits the upper body, developing both aerobic and "
                                                                     "anaerobic capacity and targeting the back, "
                                                                     "shoulders, biceps and grip muscles.")
Exercise.create_ex("Tire Flip", 0, "Tire", "None", "Quardiceps", "A classic strongman exercise and all round "
                                                                 "functional strength builder - the tire flip is a "
                                                                 "great addition to your strength and conditioning "
                                                                 "training routine.")
Exercise.create_ex("Triceps Extension", 0, "Curl Bar", "None", "Triceps", "A weight training exercise to target the "
                                                                          "triceps muscle.")
Exercise.create_ex("Weighted Step-Up", 0, "Barbell", "None", "Quadriceps", "The Weighted Step-up is a useful "
                                                                           "alternative exercise to the squat and is "
                                                                           "effective in building leg strength, power "
                                                                           "and cardiovascular abilities.")
Exercise.create_ex("Ab Wheel Rollout", 0, "Ab Wheel", "None", "Abdominals", "Classic abdominal exercise to build "
                                                                            "strength and muscular density in the "
                                                                            "abs using an ab wheel.")
Exercise.create_ex("Body Row", 0, "Squat Rack", "None", "Biceps", "The body row is an excellent upper body exercise "
                                                                  "and useful for those wanting to progress to full "
                                                                  "bodyweight pull-ups as it uses the same muscle "
                                                                  "groups.")
Exercise.create_ex("Burpees", 0, "None", "None", "Quadriceps", "Burpees are a popular and highly effective full-body "
                                                               "conditioning exercise that requires no equipment to "
                                                               "perform.")
Exercise.create_ex("Bridge", 0, "None", "None", "Back", "The bridge is a highly underrated bodyweight exercise that "
                                                        "builds high levels of strength and flexibility throughout the "
                                                        "body but particularly in the back and spine.")
Exercise.create_ex("Dead Hang", 0, "Pull-Up Bar", "None", "Forearms", "The dead hang is used as a good introduction to "
                                                                      "calisthenics / bar training and for developing "
                                                                      "foundation body strength. It's also recommended "
                                                                      "as part of the progression exercises for "
                                                                      "pull-ups.")
Exercise.create_ex("Dips", 0, "Parallel Bars", "None", "Triceps", "Dips are a fundamental calisthenics exercise that "
                                                                  "builds serious upper body strength across the "
                                                                  "chest, shoulders and triceps, whilst engaging the "
                                                                  "core.")
Exercise.create_ex("Flexed Arm Hang", 0, "Pull-Up Bar", "None", "Biceps", "The flexed arm hang is a pull-up "
                                                                          "progression exercise and a common military "
                                                                          "test of upper body strength.")
Exercise.create_ex("Frog Stand", 0, "None", "None", "Shoulders", "The frog stand is a classic beginners gymnastics "
                                                                 "position to build strength and balance skills.")
Exercise.create_ex("Handstand", 0, "None", "None", "Shoulders", "A fundamental upper-body exercise that builds "
                                                                "strength and balance, the freestanding handstand is "
                                                                "an essential bodyweight exercise worth mastering.")
Exercise.create_ex("Front Lever", 0, "Pull-Up Bar", "None", "Abdominals", "The front lever is an fundamental "
                                                                          "gymnastics strength hold that develops the "
                                                                          "core and upper-body muscles. Learn how to "
                                                                          "do the front lever and of the progression "
                                                                          "exercises path to build up to the full "
                                                                          "lever hold.")
Exercise.create_ex("Hanging Knee Raise", 0, "Pull-Up Bar", "None", "Abdominals", "Isolate the abs and build strength "
                                                                                 "in the hip flexors using hanging "
                                                                                 "knee raises.")
Exercise.create_ex("Hollow Body Hold", 0, "None", "None", "Abdominals", "The fundamental core gymnastics exercise for "
                                                                        "developing mid-line stabilisation.")
Exercise.create_ex("Lunge", 0, "None", "None", "Quadriceps", "A foundation bodyweight strength exercise for developing "
                                                             "the leg muscles. The lunge is suitable for beginners and "
                                                             "can be used with additional weight to increase "
                                                             "intensity.")
Exercise.create_ex("Negative Pull-Up", 0, "Pull-Up Bar", "None", "Back", "The negative pull-up involves performing "
                                                                         "only the lowering phase of the exercise, and "
                                                                         "is a popular technique when building "
                                                                         "strength for full pull-ups.")
Exercise.create_ex("One-Leg Deadlift", 0, "None", "None", "Hamstrings", "The One-Legged Deadlift is a more advanced "
                                                                        "version of the regular deadlift increasing "
                                                                        "intensity on the legs and challenging your "
                                                                        "balance and coordination. It's an excellent "
                                                                        "bodyweight exercise that can be performed "
                                                                        "anywhere, with no equipment.")
Exercise.create_ex("Plank", 0, "None", "None", "Abdominals", "A fundamental core conditioning exercise - the plank "
                                                             "develops the abs without a crunch in sight.")
Exercise.create_ex("Push-Up", 0, "None", "None", "Chest", "The push-up is a fundamental upper-body strength exercise "
                                                          "that is incredibly versatile and has many variations for "
                                                          "developing strength and definition in the chest, shoulders "
                                                          "and arms.")
Exercise.create_ex("Pull-Up", 0, "Pull-Up Bar", "None", "Back", "The pull-up exercise is a hugely popular exercise "
                                                                "that develops a strong and defined upper body. This "
                                                                "is a staple movement that everyone should strive to "
                                                                "achieve.")
Exercise.create_ex("Sit-Up", 0, "None", "None", "Abdominals", "The classic abdominal strength training exercise guide.")
Exercise.create_ex("Bodyweight Squat", 0, "None", "None", "Quadriceps", "The bodyweight squat is a lower body "
                                                                        "strengthening exercise that can be performed "
                                                                        "virtually anywhere with no equipment and "
                                                                        "limited space. It's a highly functional "
                                                                        "movement working all the major muscles of the "
                                                                        "legs.")
Meal.create_meal("Lean Beef", 188, 33, 6, 0, 150, "Grams")
Meal.create_meal("Beef", 337, 30, 24, 0, 150, "Grams")
Meal.create_meal("Rump Steak", 187, 33, 6, 0, 150, "Grams")
Meal.create_meal("Sirloin Steak", 202, 35, 7, 0, 150, "Grams")
Meal.create_meal("White Meat Chicken", 159, 35, 2, 0, 150, "Grams")
Meal.create_meal("Dark Meat Chicken", 163, 31, 4, 0, 150, "Grams")
Meal.create_meal("Lean Lamb", 234, 29, 13, 0, 150, "Grams")
Meal.create_meal("Lamb", 294, 29, 20, 0, 150, "Grams")
Meal.create_meal("White Meat Turkey", 157, 37, 1, 0, 150, "Grams")
Meal.create_meal("Dark Meat Turkey", 156, 31, 4, 0, 150, "Grams")
Meal.create_meal("Pork Loin", 337, 30, 24, 0, 150, "Grams")
Meal.create_meal("Pork Ribs", 293, 28, 20, 0, 150, "Grams")
Meal.create_meal("Bacon", 225, 17, 17, 0, 105, "Grams")
Meal.create_meal("Duck Breast (No Skin)", 206, 30, 10, 0, 150, "Grams")
Meal.create_meal("Duck Breast (With Skin)", 582, 20, 56, 0, 140, "Grams")
Meal.create_meal("Venison", 155, 33, 2, 0, 150, "Grams")
Meal.create_meal("Pheasant", 200, 37, 5, 0, 150, "Grams")
Meal.create_meal("Boar", 174, 32, 5, 0, 150, "Grams")
Meal.create_meal("Cod", 113, 26, 1, 0, 150, "Grams")
Meal.create_meal("Cod (Smoked)", 118, 27, 1, 0, 150, "Grams")
Meal.create_meal("Haddock", 112, 27, 1, 0, 150, "Grams")
Meal.create_meal("Hake", 138, 27, 3, 0, 150, "Grams")
Meal.create_meal("Halibut", 155, 32, 3, 0, 150, "Grams")
Meal.create_meal("Monkfish", 100, 24, 1, 0, 150, "Grams")
Meal.create_meal("Plaice", 114, 25, 2, 0, 150, "Grams")
Meal.create_meal("Sole (Lemon)", 110, 25, 1, 0, 150, "Grams")
Meal.create_meal("Sole (Dover)", 133, 27, 3, 0, 150, "Grams")
Meal.create_meal("Wild Trout", 173, 31, 5, 0, 150, "Grams")
Meal.create_meal("Wild Salmon", 269, 33, 15, 0, 150, "Grams")
Meal.create_meal("Lobster", 115, 25.5, 2, 0, 150, "Grams")
Meal.create_meal("Mussels", 11, 18, 3, 0, 150, "Grams")
Meal.create_meal("Oysters", 99, 16, 2, 0, 150, "Grams")
Meal.create_meal("Prawns", 115, 26, 1, 0, 150, "Grams")
Meal.create_meal("Scallops", 132, 43, 3, 0, 150, "Grams")
Meal.create_meal("Squid", 115, 23, 3, 0, 150, "Grams")
Meal.create_meal("Eggs", 150, 14, 10, 0, 2, "Eggs")
Meal.create_meal("Duck Eggs", 245, 21, 18, 0, 2, "Eggs")
Meal.create_meal("Collagen Powder", 107, 27, 0, 0, 30, "Grams")
Meal.create_meal("Pea Protein", 109, 20, 2, 3, 30, "Grams")
Meal.create_meal("Rice Protein", 106, 23, 0, 3, 30, "Grams")
Meal.create_meal("Whey Protein Isolate", 114, 27, 0, 0, 30, "Grams")
Meal.create_meal("Whey Protein Concentrate", 121, 24, 2, 2, 30, "Grams")
Meal.create_meal("Chicken Broth", 158, 6, 4, 0, 250, "mL")
Meal.create_meal("Beef Broth", 278, 20, 9, 0, 250, "mL")
Meal.create_meal("Amaranth", 72, 10, 5, 41, 70, "Grams")
Meal.create_meal("Beans (Taken from Red Kidney)", 206, 15, 1, 28, 70, "Grams")
Meal.create_meal("Buckwheat", 217, 5, 1, 46, 60, "Grams")
Meal.create_meal("chickpeas", 236, 15, 4, 32, 70, "Grams")
Meal.create_meal("Lentils", 226, 17, 1, 36, 70, "Grams")
Meal.create_meal("Millet", 242, 8, 3, 45, 70, "Grams")
Meal.create_meal("Quinoa", 191, 8, 3, 31, 60, "Grams")
Meal.create_meal("Brown Rice", 266, 7, 2, 53, 75, "Grams")
Meal.create_meal("White Rice", 259, 6, 0, 57, 75, "Grams")
Meal.create_meal("Rye", 254, 7, 1, 48, 70, "Grams")
Meal.create_meal("Beetroot", 36, 1, 0, 6, 80, "Grams")
Meal.create_meal("Carrots", 30, 0, 0, 5, 70, "Grams")
Meal.create_meal("Parsnips", 88, 2, 1, 14, 120, "Grams")
Meal.create_meal("Potatoes", 114, 3, 0, 24, 135, "Grams")
Meal.create_meal("Sweet Potatoes", 74, 1, 0, 16, 82, "Grams")
Meal.create_meal("Butternut Squash", 33, 1, 0, 6, 80, "Grams")
Meal.create_meal("Turnips", 24, 1, 0, 4, 80, "Grams")
Meal.create_meal("Yams", 94, 1, 0, 21, 80, "Grams")
Meal.create_meal("Apple", 99, 1, 1, 20, 1, "Apple")
Meal.create_meal("Apricot", 13, 0, 0, 3, 1, "Apricot")
Meal.create_meal("Banana", 108, 1, 0, 24, 1, "Banana")
Meal.create_meal("Blackberry", 7, 0, 0, 1, 16, "Grams")
Meal.create_meal("Blueberry", 11, 0, 0, 2, 24, "Grams")
Meal.create_meal("Cherry", 30, 0, 0, 6, 54, "Grams")
Meal.create_meal("Coconut", 170, 2, 16, 2, 45, "Grams")
Meal.create_meal("Date (Dried)", 100, 1, 0, 23, 34, "Grams")
Meal.create_meal("Grape", 40, 0, 0, 9, 54, "Grams")
Meal.create_meal("Grapefruit", 95, 2, 0, 17, 1, "Grapefruit")
Meal.create_meal("Kiwi", 36, 1, 0, 6, 60, "Grams")
Meal.create_meal("Lemon", 35, 1, 0, 3, 1, "Lemon")
Meal.create_meal("Lime", 13, 0, 0, 0, 1, "Lime")
Meal.create_meal("Lychee", 31, 0, 0, 7, 6, "Lychee")
Meal.create_meal("Mango", 35, 0, 0, 7, 52, "Grams")
Meal.create_meal("Watermelon", 84, 1, 1, 17, 250, "Grams")
Meal.create_meal("Nectarine", 53, 2, 0, 10, 110, "Grams")
Meal.create_meal("Orange", 55, 1, 0, 10, 128, "Grams")
Meal.create_meal("Passionfruit", 17, 1, 0, 2, 1, "Passionfruit")
Meal.create_meal("Peach", 45, 1, 0, 8, 1, "Peach")
Meal.create_meal("Pear", 83, 1, 0, 17, 160, "Grams")
Meal.create_meal("Persimmon", 24, 0, 0, 5, 1, "Persimmon")
Meal.create_meal("Plum", 39, 0, 0, 7, 85, "Grams")
Meal.create_meal("Pineapple", 40, 0, 0, 8, 80, "Grams")
Meal.create_meal("Raspberry", 24, 1, 0, 2, 53, "Grams")
Meal.create_meal("Satsuma", 29, 0, 0, 6, 1, "Satsuma")
Meal.create_meal("Strawberry", 33, 0, 0, 5, 78, "Grams")
Meal.create_meal("Sultana", 53, 0, 0, 12, 18, "Grams")
Meal.create_meal("Artichokes", 24, 2, 0, 2, 80, "Grams")
Meal.create_meal("Asparagus", 24, 2, 0, 2, 75, "Grams")
Meal.create_meal("Aubergine", 19, 1, 0, 2, 80, "Grams")
Meal.create_meal("Bamboo Shoots", 22, 1, 0, 1, 80, "Grams")
Meal.create_meal("Bean Sprouts", 29, 2, 0, 3, 75, "Grams")
Meal.create_meal("Bok Choy", 14, 1, 0, 1, 80, "Grams")
Meal.create_meal("Broccoli", 40, 4, 1, 3, 85, "Grams")
Meal.create_meal("Cabbage", 15, 1, 0, 2, 40, "Grams")
Meal.create_meal("Cauliflower", 15, 1, 0, 2, 40, "Grams")
Meal.create_meal("Celery", 11, 0, 0, 1, 80, "Grams")
Meal.create_meal("Courgette", 21, 1, 0, 1, 80, "Grams")
Meal.create_meal("Cucumber", 8, 0, 0, 0, 40, "Grams")
Meal.create_meal("Fennel", 19, 1, 0, 1, 80, "Grams")
Meal.create_meal("Garlic", 3, 0, 0, 0, 3, "Grams")
Meal.create_meal("Green Bean", 26, 1, 0, 2, 75, "Grams")
Meal.create_meal("Kale", 27, 2, 1, 1, 60, "Grams")
Meal.create_meal("Leek", 24, 1, 0, 2, 80, "Grams")
Meal.create_meal("Mangetout", 33, 3, 0, 3, 80, "Grams")
Meal.create_meal("Mushroom", 5, 1, 0, 0, 30, "Grams")
Meal.create_meal("Okra", 37, 2, 1, 3, 85, "Grams")
Meal.create_meal("Onion", 9, 0, 0, 2, 20, "Grams")
Meal.create_meal("Pea", 49, 3, 0, 6, 60, "Grams")
Meal.create_meal("Bell Pepper", 27, 1, 0, 4, 80, "Grams")
Meal.create_meal("Radicchio", 14, 1, 0, 2, 50, "Grams")
Meal.create_meal("Radish", 6, 0, 0, 1, 40, "Grams")
Meal.create_meal("Runner Bean", 19, 1, 0, 2, 70, "Grams")
Meal.create_meal("Spinach", 15, 2, 0, 0, 80, "Grams")
Meal.create_meal("Tomato", 75, 0, 0, 3, 85, "Grams")
Meal.create_meal("Avocado", 141, 1, 14, 1, 70, "Grams")
Meal.create_meal("Butter", 67, 0, 7, 0, 1, "tsp")
Meal.create_meal("Chia Seed", 94, 4, 6, 2, 20, "Grams")
Meal.create_meal("Coconut Oil", 81, 0, 9, 0, 1, "tsp")
Meal.create_meal("Coconut Milk", 79, 1, 5, 5, 250, "mL")
Meal.create_meal("Coconut Yoghurt", 219, 3, 21, 4, 100, "Grams")
Meal.create_meal("Feta Cheese", 76, 5, 6, 0, 30, "Grams")
Meal.create_meal("Ghee", 44, 0, 5, 0, 5, "Grams")
Meal.create_meal("Almond", 62, 2, 5, 1, 10, "Grams")
Meal.create_meal("Brazil Nuts", 178, 4, 17, 1, 25, "Grams")
Meal.create_meal("Cashew Nuts", 131, 5, 11, 4, 22, "Grams")
Meal.create_meal("Macadamia Nuts", 191, 2, 19, 1, 25, "Grams")
Meal.create_meal("Walnuts", 107, 3, 10, 0, 15, "Grams")
Meal.create_meal("Peanut Butter", 128, 6, 11, 1, 1, "tbsp")
Meal.create_meal("Green Olives", 17, 0, 2, 0, 15, "Grams")
Meal.create_meal("Olive Oil", 108, 0, 12, 0, 1, "tbsp")
Meal.create_meal("Plain Yoghurt", 104, 7, 4, 10, 125, "Grams")
Meal.create_meal("Basil", 5, 0, 0, 1, 2, "Grams")
Meal.create_meal("Caraway", 9, 0, 0, 1, 2, "Grams")
Meal.create_meal("Dill", 6, 0, 0, 1, 2, "Grams")
Meal.create_meal("Fennel", 6, 0, 0, 0, 2, "Grams")
Meal.create_meal("Garlic", 3, 0, 0, 0, 3, "Grams")
Meal.create_meal("Marjoram", 6, 0, 0, 1, 2, "Grams")
Meal.create_meal("Mint", 6, 0, 0, 1, 2, "Grams")
Meal.create_meal("Mustard Seed", 8, 1, 1, 0, 2, "Grams")
Meal.create_meal("Oregano", 5, 0, 0, 0, 2, "Grams")
Meal.create_meal("Parsley", 5, 0, 0, 0, 2, "Grams")
Meal.create_meal("Rosemary", 15, 0, 2, 0, 2, "Grams")
Meal.create_meal("Sage", 6, 0, 0, 1, 2, "Grams")
Meal.create_meal("Thyme", 7, 0, 0, 1, 2, "Grams")
Meal.create_meal("Cayenne Pepper", 7, 0, 0, 1, 2, "Grams")
Meal.create_meal("Chilli Powder", 6, 0, 0, 0, 2, "Grams")
Meal.create_meal("Cinnamon", 5, 0, 0, 1, 2, "Grams")
Meal.create_meal("Coriander", 7, 0, 0, 0, 2, "Grams")
Meal.create_meal("Cumin", 8, 0, 0, 1, 2, "Grams")
Meal.create_meal("Ginger", 6, 0, 0, 1, 2, "Grams")
Meal.create_meal("Paprika", 6, 0, 0, 0, 2, "Grams")
Meal.create_meal("Turmeric", 8, 0, 0, 1, 2, "Grams")
Meal.create_meal("Kefir", 17, 2, 1, 1, 30, "Grams")
Meal.create_meal("Kimchee", 9, 0, 0, 1, 40, "Grams")
Meal.create_meal("Kombucha", 33, 0, 0, 8, 250, "mL")
Meal.create_meal("Probiotic Yoghurt", 52, 1, 1, 10, 65, "Grams")
Meal.create_meal("Sauerkraut", 4, 0, 0, 0, 30, "Grams")
