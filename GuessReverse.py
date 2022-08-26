
print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")

def guess_reverse(max, min, chance):
    while chance != 0:
        guess = int((max - min) / 2) + min
        print(f"Zgaduję:{guess} ")
        answer = input("Czy zgadłem? ")
        chance -= 1
        if answer == 'yes':
            print("You win!")
            break
        elif answer == 'no':
            ask_again = input("To big?")
            if ask_again == 'yes':
                max = guess
                continue
            elif ask_again == 'no':
                ask_again_2 = input("To small?")
                if ask_again_2 == 'yes':
                    min = guess
                    continue
                else:
                    print("Stop cheating!")
                    continue

guess_reverse(1000, 0, 10)