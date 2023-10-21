print()
#Blank line

print("Good morning! After a nice 8 hours of sleep you have woken up at 9am on Saturday")
#You wake up at 9am Saturday
print("You get dressed and go downstairs for some breakfast")
#Get dressed and go downstairs
print("You decide that you could eat breakfast at HOME or eat OUT")
place = input("Where will you eat? ").lower()
#Ask will you eat at home or out

print()
#Blank line

if place == 'home':
    print("You decide to have breafast at home")
    #You decide to make breakfast at home
    print("You search the kitchen and find you could make CEREAL, EGGS, or PANCAKES")
    #List what you could make for breakfast
    make = input("What will you make for breakfast? ").lower()

    print()
    #Blank line

    if make == 'cereal':
        print("You decide to make cereal for breakfast")
        print("You grab milk from the fridge, a bowl from the cupboard, and a spoon from a drawer")
        print("Finally, you open the pantry and look at all of the cereal options")
        #You start to make cereal
        print("In the pantry you find LIFE, CAPTAIN CRUNCH, and CHEERIOS")
        #List cereal options

        print()
        #Blank line

        cereal = input("Which cereal do you choose to eat? ").lower()
        if cereal == 'life':
            print("You decide to eat Life cereal")
            #You decide to eat Life cereal
            print("You grab the Life cereal from the pantry and place it on the counter")
            print("You then go to the fridge to grab some milk")
            print("In the fridge you find SKIM MILK and WHOLE MILK, or you could have NO MILK")
            milk = input("What milk do you grab? ").lower()
            #Do you take skim, whole, or no milk

            print()
            #Blank line

            if milk == 'skim milk':
                print("You decide to use skim milk")
                #You take skim milk
                print("You pour the Life cereal into the bowl")
                print("Next goes the skim milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            elif milk == 'whole milk':
                print("You decide to use whole milk")
                #You take whole milk
                print("You pour the Life cereal into the bowl")
                print("Next goes the whole milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            else:
                print("You decide not to use milk")
                #You don't take any milk
                print("You pour the Life cereal into the bowl")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
        elif cereal == 'captian crunch':
            print("You decide to eat Captain Crunch cereal")
            #You decide to eat Captain crunch cereal
            print("You grab the Captain Crunch cereal from the pantry and place it on the counter")
            print("You then go to the fridge to grab some milk")
            print("In the fridge you find SKIM MILK and WHOLE MILK, or you could have NO MILK")
            milk = input("What milk do you grab? ").lower()

            print()
            #Blank line

            #Do you take skim, whole, or no milk
            if milk == 'skim milk':
                print("You decide to use skim milk")
                #You take skim milk
                print("You pour the Captain Crunch cereal into the bowl")
                print("Next goes the skim milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            elif milk == 'whole milk':
                print("You decide to use whole milk")
                #You take whole milk
                print("You pour the Captain Crunch cereal into the bowl")
                print("Next goes the whole milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            else:
                print("You decide not to use milk")
                #You don't take any milk
                print("You pour the Captain Crunch cereal into the bowl")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
        elif cereal == 'cheerios':
            print("You decide to eat Cheerios cereal")
            #You decide to eat Cheerios cereal
            print("You grab the Cheerios cereal from the pantry and place it on the counter")
            print("You then go to the fridge to grab some milk")
            print("In the fridge you find SKIM MILK and WHOLE MILK, or you could have NO MILK")
            milk = input("What milk do you grab? ").lower()
            #Do you take skim, whole, or no milk

            print()
            #Blank line

            if milk == 'skim milk':
                print("You decide to use skim milk")
                #You take skim milk
                print("You pour the Cheerios cereal into the bowl")
                print("Next goes the skim milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            elif milk == 'whole milk':
                print("You decide to use whole milk")
                #You take whole milk
                print("You pour the Cheerios cereal into the bowl")
                print("Next goes the whole milk")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
            else:
                print("You decide not to use milk")
                #You don't take any milk
                print("You pour the Cheerios cereal into the bowl")
                print("You chow down on your wonderful bowl of cereal")
                print("Now with a full stomach you are ready to start the day")
        else:
            print("You can't decide which cereal to eat so you decide to just have a glass of milk")
            print("You grab a glass from the cupboard and place it on the counter")
            print("Then you go to the fridge to grab some milk")
            print("In the fridge you find SKIM MILK and WHOLE MILK")
            milk = input("What milk do you grab? ").lower()
            #Do you take skim or whole milk

            print()
            #Blank line

            if milk == 'skim milk':
                print("You decide to use skim milk")
                #You take skim milk
                print("You pour the skim milk into your glass")
                print("Then you down your refreshing glass of milk")
                print("Now with a full stomach you are ready to start the day")
            elif milk == 'whole milk':
                print("You decide to use whole milk")
                #You take whole milk
                print("You pour the whole milk into your glass")
                print("Then you down your refreshing glass of milk")
                print("Now with a full stomach you are ready to start the day")
            else:
                print("You decide not to have a glass of milk")
                #You don't take any milk
                print("You close the fridge and put your glass away")
                print("Now with a empty stomach you are ready to start the day")
    elif make == 'eggs':
        print("You decide to make eggs for breakfast")
        #You decide to make eggs
        print("You go to the fridge and grab the carton")
        print("You could eat ONE, TWO or THREE eggs")
        eggs_num = input("How many eggs do you grab? ").lower()

        print()
        #Blank line

        if eggs_num == 'one':
            print("You decide to eat one egg")
            #You take one egg
            print("You take your egg out of the fridge and think of how to prepare it")
            print("You could eat it SCRAMBLED, HARD BOILED, or RAW")
            egg_prep = input("How will you prepare your egg? ").lower()

            print()
            #Blank line

            if egg_prep == 'scrambled':
                print("You decide to eat your egg scrambled")
                #You choose to eat your egg scrambled
                print("You start the stove and begin the scrambling process")
                print("When the egg is done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'hard boiled':
                print("You decide to eat your egg hard boiled")
                #You choose to eat your egg hard boiled
                print("You start the stove and begin the boiling process")
                print("When the egg is done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'raw':
                print("You decide to eat your egg raw")
                #You choose to eat your egg raw
                print("You crunch down on your delicous egg and enjoy")
                print("You are now ready to start the day with a full stomach")
            else:
                print("You just wanted an egg, unrelated to eating it")
                print("You throw the egg on the ground and start your day without breakfast")
        elif eggs_num == 'two':
            print("You decide to eat two eggs")
            #You take two eggs
            print("You take the eggs out of the fridge and think of how to prepare them")
            print("You could eat them SCRAMBLED, HARD BOILED, or RAW")
            egg_prep = input("How will you prepare the eggs? ").lower()

            print()
            #Blank line

            if egg_prep == 'scrambled':
                print("You decide to eat your eggs scrambled")
                #You choose to eat your eggs scrambled
                print("You start the stove and begin the scrambling process")
                print("When the eggs are done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'hard boiled':
                print("You decide to eat your eggs hard boiled")
                #You choose to eat your eggs hard boiled
                print("You start the stove and begin the boiling process")
                print("When the eggs are done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'raw':
                print("You decide to eat your eggs raw")
                #You choose to eat your eggs raw
                print("You crunch down on your delicous eggs and enjoy")
                print("You are now ready to start the day with a full stomach")
            else:
                print("You just wanted some eggs, unrelated to eating them")
                print("You throw the eggs on the ground and start your day without breakfast")
        elif eggs_num == 'three':
            print("You decide to eat three eggs")
            #You take three eggs
            print("You take the eggs out of the fridge and think of how to prepare them")
            print("You could eat them SCRAMBLED, HARD BOILED, or RAW")
            egg_prep = input("How will you prepare the eggs? ").lower()

            print()
            #Blank line

            if egg_prep == 'scrambled':
                print("You decide to eat your eggs scrambled")
                #You choose to eat your eggs scrambled
                print("You start the stove and begin the scrambling process")
                print("When the eggs are done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'hard boiled':
                print("You decide to eat your eggs hard boiled")
                #You choose to eat your eggs hard boiled
                print("You start the stove and begin the boiling process")
                print("When the eggs are done you chow down on your delicous breakfast")
                print("You are now ready to start the day with a full stomach")
            elif egg_prep == 'raw':
                print("You decide to eat your eggs raw")
                #You choose to eat your eggs raw
                print("You crunch down on your delicous eggs and enjoy")
                print("You are now ready to start the day with a full stomach")
            else:
                print("You just wanted some eggs, unrelated to eating them")
                print("You throw the eggs on the ground and start your day without breakfast")
        else:
            print("Nevermind, you don't actually want eggs")
            print("You close the fridge and decide to start the day without breakfast")
    elif make == 'pancakes':
        print("You decide to make pancakes for breakfast")
        print("You could make CHOCOLATE CHIP, BLUEBERRY, or PLAIN pancakes")
        pancake = input("What kind of pancakes will you make? ").lower()

        print()
        #Blank line

        if pancake == 'chocolate chip':
            print("You decide to make chocolate chip pancakes")
            #You decide to make chocolate chip pancakes
            print("You make the batter and pour in some chocolate chips")
            print("When the pancakes are done you chow down")
            print("You are now ready to start the day on a full stomcach")
        elif pancake == 'blueberry':
            print("You decide to make blueberry pancakes")
            #You decide to make blueberry pancakes
            print("You make the batter and pour in some blueberries")
            print("When the pancakes are done you chow down")
            print("You are now ready to start the day on a full stomcach")
        elif pancake == 'plain':
            print("You decide to make plain pancakes")
            #You decide to make plain pancakes
            print("You make the batter with nothing extra added")
            print("When the pancakes are done you chow down")
            print("You are now ready to start the day on a full stomcach")
        else:
            print("You decide making pancakes is to hard for this early in the morning")
            print("With that you start your day with an empty stomach")
    else:
        print("you decide to be lazy and don't make any breakfast at all")
        print("You are ready to start the day on an empty stomach")
elif place == 'out':
    print("You decide to eat out for breakfast")
    print("The best breakfast places nearby are MCDONALDS, ARBYS, and BURGER KING")
    restaurant = input("Where will you go for breakfast? ").lower()

    print()
    #Blank line

    if restaurant == 'mcdonalds':
        print("You decide to eat at McDonalds")
        #You decide to go to McDonalds
        print("You get in your car and drive to McDonalds")
        print("You head inside and start looking at the menu")
        print("You could buy a BISCUIT, some PANCAKES, or a breakfast BURRITO")
        order = input("What will you order? ").lower()

        print()
        #Blank line

        if order == 'biscuit':
            print("You decide to order a biscuit")
            #You order a biscuit
            print("You wait your turn then order a biscuit")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a goo view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order =='pancakes':
            print("You decide to order pancakes")
            #You order pancakes
            print("You wait your turn then order some pancakes")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order =='burrito':
            print("You decide to order a breakfast burrito")
            #You order a breakfast burrito
            print("You wait your turn then order a breakfast burrito")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        else:
            print("The menu looks a little too pricy for your taste")
            print("You head back to your car and start your day without breakfast")

    elif restaurant == 'arbys':
        print("You decide to eat at Arbys")
        #You decide to go to Arbys
        print("You get in your car and drive to Arbys")
        print("You head inside and start looking at the menu")
        print("You could buy a BISCUIT, SANDWHICH, or WRAP")
        order = input("What will you order? ").lower()

        print()
        #Blank line

        if order == 'biscuit':
            print("You decide to order a biscuit")
            #You order a biscuit
            print("You wait your turn then order a biscuit")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order == 'sandwhich':
            print("You decide to order a croissant sandwhich")
            #You order a biscuit
            print("You wait your turn then order a croissant sandwhich")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order == 'wrap':
            print("You decide to order a breakfast wrap")
            #You order a biscuit
            print("You wait your turn then order a breakfast wrap")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        else:
            print("The menu looks a little too pricy for your taste")
            print("You head back to your car and start your day without breakfast")

    elif restaurant == 'burger king':
        print("You decide to eat at Burger King")
        #You decide to go to Burger King
        print("You get in your car and drive to Burger King")
        print("You head inside and start looking at the menu")
        print("You could buy a OMLET, SANDWICH, or FRENCH TOAST")
        order = input("What will you order? ").lower()

        print()
        #Blank line

        if order == 'omlet':
            print("You decide to order a omlet")
            #You order a biscuit
            print("You wait your turn then order a omlet")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order == 'sandwhich':
            print("You decide to order a sandwhich")
            #You order a biscuit
            print("You wait your turn then order a sandwhich")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        elif order == 'french toast':
            print("You decide to order some french toast ")
            #You order a biscuit
            print("You wait your turn then order some french toast")
            print("You pay for your meal and go to take a seat")
            print("You could sit at a TABLE, BOOTH, or COUNTER")
            sit = input("Where will you sit? ").lower()

            print()
            #Blank line

            if sit =='table':
                print("You decide to sit at a table")
                print("You find a nice clean one in the middle of the floor and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='booth':
                print("You decide to sit at a booth")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            elif sit =='counter':
                print("You decide to sit at a counter")
                print("You find a nice clean one with a good view and sit down")
                print("When your order finally arrives you eagerly dig in")
                print("When you finish you walk back to your car and start your day")
            else:
                print("You decide you'd rather stand")
                print("When you get your order you take it with you to your car")
                print("You eagerly eat your breakfast and then get started on your day")

        else:
            print("The menu looks a little too pricy for your taste")
            print("You head back to your car and start your day without breakfast")

    else:
        print("You change your mind, going out is to much work")
        print("You start your day without any breakfast")
else:
    print("You decide to save time and skip breakfast")
    #You don't have breakfast
    print("You weren't that hungry anyway")

print()
#Blank line