import java.util.Arrays;

public class Kata {
    public static String createPhoneNumber(int[] numbers) {
      // Your code here!
      String str = "";
      for (int i : numbers) {
        str += i;
      }
      return String.format("(%s) %s-%s", str.substring(1, 3),str.substring(3, 6),str.substring(6, 10))
    }
  }
