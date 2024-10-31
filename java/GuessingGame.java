import java.util.*;

/* Arvaus peli */
public class GuessingGame {
  Random random = new Random();
  int numMax;
  int numMin;
  int livesLeft;
  int answer;
  Scanner myScan = new Scanner(System.in);

    public GuessingGame(int max, int min, int lives) {
      numMax = max;
      numMin = min;
      livesLeft = lives;
    }

    public static void main(String[] args) {
      GuessingGame myGuess = new GuessingGame(10, 1, 3);
      int correctNumber = myGuess.random.nextInt((myGuess.numMax - myGuess.numMin) + 1) + myGuess.numMin;
      
      System.out.println();
      System.out.println("Guess between " + myGuess.numMin + " - " + myGuess.numMax);

      while (myGuess.livesLeft > 0) {
        System.out.println();
        System.out.println("You have " + myGuess.livesLeft + " lives left.");

        try {

          System.out.print("Guess a number: ");
          myGuess.answer = myGuess.myScan.nextInt();
          System.out.println();

          if (correctNumber == myGuess.answer) {
            System.out.println("Correct, you won!");
            break;
          } else if (correctNumber < myGuess.answer) {
            System.out.println("Too high.");
            --myGuess.livesLeft;
          } else if (correctNumber > myGuess.answer) {
            System.out.println("Too low.");
            --myGuess.livesLeft;
          }

        } catch (InputMismatchException  e) {
          System.out.println();
          System.out.println("That's not a number...");
          myGuess.myScan.nextLine();
        }
      }

      if (myGuess.livesLeft == 0) {
        System.out.println();
        System.out.println("Out of lives, you lose!");
        System.out.println("Correct number was: " + correctNumber);
      }

    }

  }
  