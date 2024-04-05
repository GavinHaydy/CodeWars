import java.util.HashMap;
import java.util.Map;

public class Kata {
    public static String firstNonRepeatingLetter(String s){
      // Add your code here
      String res = s.toLowerCase();
        Map<String,Integer> m = new HashMap<>();
        for (int i = 0; i < res.length(); i++) {
            if (m.get(String.valueOf(res.charAt(i))) == null) {
                m.put(String.valueOf(res.charAt(i)), 1);
            }else{
                m.put(String.valueOf(res.charAt(i)), m.get(String.valueOf(res.charAt(i))) + 1);
            }
        }
        for (char c : s.toCharArray()) {
          if (m.get(String.valueOf(c).toLowerCase()) != null && m.get(String.valueOf(c).toLowerCase()) == 1) {
            return String.valueOf(c);
          }
        }
        return "";
    }
  }


/*	best
public class Kata {
  public static String firstNonRepeatingLetter(String s){
    for (String str : s.split("")) {
      if (s.toUpperCase().indexOf(str.toUpperCase()) == s.toUpperCase().lastIndexOf(str.toUpperCase())) return str;
     }
    return "";
  }
}
*/
