#Madlib Game

name = input("Enter Name: ")
place = input("Enter place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")


print("\n" + "=" * 50)
print("           STORY BEGINS")
print("=" * 50)


print(f"""
One day, {name} went to {place} for a ritual that happens once every 1000 years.
It was a very {adjective} day.

Suddenly, a {noun} appeared and started to {verb}.
The {noun} had power at captain level.
""")

print("-" * 50)


choice = input("What will you do? (fight/run):").lower()


print("-" * 50)


if choice == "fight":
    print(f"""
{name} released his Bankai...

"Ban... Kai... Getsuga Tenshou!!!"

{noun} survived the attack.
{name} was shocked...

"Impossible... it's just a {noun}, how did he survived!?"

Tension rises-

And suddenly all the captians arrived on time and then... 
          
TO BE CONTINUED
""")
    
else:
    print(f"""
{name} felt an overwhelming spiritual pressure.
Without thinking twice, {name} tried to run.

But the {noun} was far too powerful.
It caught {name} before the captains could arrive...

TO BE CONTINUED
""")
    
print("=" * 50)
