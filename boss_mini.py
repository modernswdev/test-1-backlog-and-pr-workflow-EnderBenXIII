# boss_mini.py

# A tiny combat script for the GitHub Workflow Exam.


# Security Risk: Hardcoded access is a huge security risk
SECRET_CODE = "ADMIN_ACCESS_2025"



p_hp = 50

b_hp = 50


# Attack Function: The function to subtract 10 health from the Boss is missing.
def attack():

  global b_hp

    print("You deal 10 damage!")


# Heal Function: Missing boundary checks allows for the player to heal past 50 HP or when dead.
def heal():

  global p_hp

  p_hp += 20

  print(f"Healed! HP is now {p_hp}")



# --- Simple Game Loop ---
# Add a Win Condition: The game loop does not trigger a win state when the boss dies, it should also print "Victory!"
while p_hp > 0 and b_hp > 0:

  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")

  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()



  if choice == 'a':

    attack()

  elif choice == 'h':

    heal()

  elif choice == 'c':
# Security Risk, Remove cheat function.
    if input("Code: ") == SECRET_CODE:

      b_hp = 0

  

  if b_hp > 0:

    p_hp -= 10



print("Game Over!")