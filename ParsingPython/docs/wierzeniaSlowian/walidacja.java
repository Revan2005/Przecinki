import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class walidacja{

  public static void main(String[] args) throws FileNotFoundException {
    Scanner odczyt = new Scanner(new File("outputMIRA.txt"));
    String line;
    String[] cols;
    int dobrze = 0, zle = 0;
    while(odczyt.hasNext()){
      line = odczyt.nextLine();
      //System.out.println(line);
      cols = line.split("\t");
      for(int i=0; i<cols.length; i++){
        cols[i] = cols[i].trim();
      }
      //System.out.println(cols.length);
      if(cols.length == 4){
        //System.out.println(cols[2]+"  "+cols[3]);
        if( (cols[2].equals("comma_after")) || (cols[3].equals("comma_after")) ){
          //System.out.println("weszlo");
          if(cols[2].equals(cols[3]))
            dobrze++;
          else
            zle++;
        }
      }
    }
    System.out.println("\n\nDobrze/(dobrze+zle) = " + (double)100*dobrze/(dobrze+zle) + "%\n\n");
  }

}
