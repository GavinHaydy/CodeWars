public class TotalPoints {
  
    public static int points(String[] games) {
        Integer result = 0;
      for (String str : games) {
        String arr = str.split(":")[0];
        if (Integer.parseInt(str.split(":")[0]) > Integer.parseInt(str.split(":")[1])) {
            result += 3;
        }else if (Integer.parseInt(str.split(":")[0]) == Integer.parseInt(str.split(":")[1])) {
            result += 1;
        }
      }
      return result;
    }
}