import random
from django.shortcuts import render


def FortuneData():
        fortunes = [
           "A beautiful, smart, and loving person will be coming into your life.",
            "A faithful friend is a strong defense.",
            "A fresh start will put you on your way.",
            "A friend asks only for your time, not your money.",
            "A friend is a present you give yourself.",
            "A gambler not only will lose what he has, but also will lose what he doesn’t have.",
            "A golden egg of opportunity falls into your lap this month.",
            "A good time to finish up old tasks.",
            "A hunch is creativity trying to tell you something.",
            "A lifetime friend shall soon be made.",
            "A lifetime of happiness lies ahead of you.",
            "A light heart carries you through all the hard times.",
            "A new perspective will come with the new year.",
            "A person is never too old to learn.",
            "A person of words and not deeds is like a garden full of weeds.",
            "A pleasant surprise is waiting for you.",
            "A short pencil is usually better than a long memory any day.",
            "A small donation is call for. It’s the right thing to do.",
            "A smile is your personal welcome mat.",
            "A smooth long journey! Great expectations.",
            "A soft voice may be awfully persuasive.",
            "A truly rich life contains love and art in abundance.",
            "Accept something that you cannot change, and you will feel better.",
            "Adventure can be real happiness.",
            "Advice is like kissing. It costs nothing and is a pleasant thing to do.",
            "Advice, when most needed, is least heeded.",
            "All the effort you are making will ultimately pay off.",
            "All the troubles you have will pass away very quickly.",
            "All will go well with your new project.",
            "All your hard work will soon pay off.",
            "Allow compassion to guide your decisions.",
            "An agreeable romance might begin to take on the appearance.",
            "An important person will offer you support.",
            "An inch of time is an inch of gold.",
            "Any decision you have to make tomorrow is a good decision.",
            "At the touch of love, everyone becomes a poet.",
            "Be careful or you could fall for some tricks today.",
            "Beauty in its various forms appeals to you.",
            "Because you demand more from yourself, others respect you deeply.",
            "Believe in yourself and others will too.",
            "Believe it can be done.",
            "Better ask twice than lose yourself once.",
            "Bide your time, for success is near.",
            "Carve your name on your heart and not on marble.",
            "Change is happening in your life, so go with the flow!",
            "Competence like yours is underrated.",
            "Congratulations! You are on your way.",
            "Could I get some directions to your heart?",
            "Courtesy begins in the home.",
            "Courtesy is contagious.",
            "Dedicate yourself with a calm mind to the task at hand.",
            "Depart not from the path which fate has you assigned.",
            "Determination is what you need now.",
            "Disbelief destroys the magic.",
            "Distance yourself from the vain.",
            "Do not be intimidated by the eloquence of others.",
            "Do not demand for someone’s soul if you already got his heart.",
            "Do not let ambitions overshadow small success.",
            "Do not make extra work for yourself.",
            "Do not underestimate yourself. Human beings have unlimited potentials.",
            "Do you know that the busiest person has the largest amount of time?",
            "Don’t be discouraged, because every wrong attempt discarded is another step forward.",
            "Don’t confuse recklessness with confidence.",
            "Don’t just spend time. Invest it.",
            "Don’t just think, act!",
            "Don’t let friends impose on you, work calmly and silently.",
            "Don’t let the past and useless detail choke your existence.",
            "Don’t let your limitations overshadow your talents.",
            "Don’t worry; prosperity will knock on your door soon.",
            "Each day, compel yourself to do something you would rather not do.",
            "Education is the ability to meet life’s situations.",
            "Embrace this love relationship you have!",
            "Every flower blooms in its own sweet time.",
            "Every wise man started out by asking many questions.",
            "Everyday in your life is a special occasion.",
            "Everywhere you choose to go, friendly faces will greet you.",
            "Expect much of yourself and little of others.",
            "Failure is the chance to do better next time.",
            "Failure is the path of least persistence.",
            "Fear and desire – two sides of the same coin.",
            "Feeding a cow with roses does not get extra appreciation.",
            "Fame, riches and romance are yours for the asking.",
            "Fearless courage is the foundation of victory.",
            "Feeding a cow with roses does not get extra appreciation.",
            "For hate is never conquered by hate. Hate is conquered by love.",
            "For the things we have to learn before we can do them, we learn by doing them.",
            "Fortune Not Found: Abort, Retry, Ignore?",
            "From now on your kindness will lead you to success.",
            "Get your mind set – confidence will lead you on.",
            "Get your mind set…confidence will lead you on.",
            "Go take a rest; you deserve it.",
            "Good news will be brought to you by mail.",
            "Good news will come to you by mail.",
            "Good to begin well, better to end well.",
            "Happiness begins with facing life with a smile and a wink.",
            "Happiness will bring you good luck.",
            "Happy life is just in front of you." 
        ]

        return random.choice(fortunes)


def RiddleData():
        riddles = [
            "Q: Why haven't you graduated yet?\nA: Well, Dad, I could have finished years ago, but I wanted my dissertation to rhyme.",
            "Q: Why did the cow cross the road?\nA: To get to the other side.",
            "Q: What has keys but can't open locks?\nA: A piano.",
            "Q: What has a heart that doesn't beat?\nA: An artichoke.",
            "Q: What can travel around the world while staying in a corner?\nA: A stamp.",
            "Q: What comes once in a minute, twice in a moment, but never in a thousand years?\nA: The letter 'M'.",
            "Q: I am not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?\nA: Fire.",
            "Q: I have branches, but no fruit, trunk, or leaves. What am I?\nA: A bank.",
            "Q: What has to be broken before you can use it?\nA: An egg.",
            "Q: I'm tall when I'm young, and I'm short when I'm old. What am I?\nA: A candle.",
            "Q: What month of the year has 28 days?\nA: All of them.",
            "Q: What is full of holes but still holds water?\nA: A sponge.",
            "Q: What question can you never answer yes to?\nA: Are you asleep yet?",
            "Q: What is always in front of you but can’t be seen?\nA: The future.",
            "Q: There's a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?\nA: There aren't any—it's a one-story house.",
            "Q: What can you break, even if you never pick it up or touch it?\nA: A promise.",
            "Q: What goes up but never comes down?\nA: Your age.",
            "Q: A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?\nA: He was bald.",
            "Q: What gets wet while drying?\nA: A towel.",
            "Q: What can you keep after giving to someone?\nA: Your word.",
            "Q: I shave every day, but my beard stays the same. What am I?\nA: A barber.",
            "Q: You see me once in June, twice in November, and not at all in May. What am I?\nA: The letter 'E'.",
            "Q: I have lakes with no water, mountains with no stone, and cities with no buildings. What am I?\nA: A map.",
            "Q: What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?\nA: The letter 'R'.",
            "Q: You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?\nA: All the people were married.",
            "Q: What runs all around a backyard, yet never moves?\nA: A fence.",
            "Q: What can fill a room but takes up no space?\nA: Light.",
            "Q: If you drop me, I'm sure to crack, but give me a smile and I'll always smile back. What am I?\nA: A mirror.",
            "Q: I have keys but no locks. I have a space but no room. You can enter, but you can’t go outside. What am I?\nA: A keyboard.",
            "Q: What has many teeth but can’t bite?\nA: A comb.",
            "Q: Where does today come before yesterday?\nA: In a dictionary.",
            "Q: What kind of band never plays music?\nA: A rubber band.",
            "Q: What has lots of eyes, but can’t see?\nA: A potato.",
            "Q: What has one eye, but can’t see?\nA: A needle.",
            "Q: What has many needles, but doesn’t sew?\nA: A Christmas tree.",
            "Q: What is cut on a table, but is never eaten?\nA: A deck of cards.",
            "Q: What has a head, a tail, is brown, and has no legs?\nA: A penny.",
            "Q: What is black when it’s clean and white when it’s dirty?\nA: A chalkboard.",
            "Q: What gets bigger the more you take away?\nA: A hole.",
            "Q: I’m light as a feather, yet the strongest man can’t hold me for much longer. What am I?\nA: Breath.",
            "Q: I’m found in socks, scarves and mittens; and often in the paws of playful kittens. What am I?\nA: Yarn.",
            "Q: Where does one wall meet the other wall?\nA: On the corner.",
            "Q: What building has the most stories?\nA: The library.",
            "Q: What tastes better than it smells?\nA: Your tongue.",
            "Q: What has one head, one foot, and four legs?\nA: A bed.",
            "Q: What has many keys but can't open a single lock?\nA: A piano.",
            "Q: What begins with T, ends with T, and has T in it?\nA: A teapot.",
            "Q: What has words, but never speaks?\nA: A book.",
            "Q: What has four wheels and flies?\nA: A garbage truck."
        ]
        return random.choice(riddles)