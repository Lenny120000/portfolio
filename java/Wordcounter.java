import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Wordcounter {
    int wordCount;
    Scanner myScan = new Scanner(System.in);
    String answer;

    public static void main(String[] args) {
        Wordcounter myWord = new Wordcounter();

        try {
            System.out.println("Give Filename:");
            myWord.answer = myWord.myScan.nextLine();

            File myFile = new File(myWord.answer);
            
            try (Scanner myReader = new Scanner(myFile)) {
                while (myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    String[] wordArray = data.trim().split("\\w+");
                    myWord.wordCount += wordArray.length;

                    System.out.println();
                    System.out.println(data);
                }

            System.out.println();
            System.out.println("Word count is = " + myWord.wordCount);
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}