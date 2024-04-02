import java.util.Scanner;

public class SecureTester {
  
    public static boolean alphanumeric(String s){
        String pat = "^[a-zA-Z0-9]+$";
        if (!s.matches(pat)) {            
            return false;
        }
        return true;
    }
}
  
/*
 * public class SecureTester {
  public static boolean alphanumeric(String s) {
    return s.matches("[A-Za-z0-9]+");
  }
}
 */