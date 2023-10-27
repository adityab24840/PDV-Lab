public class LargeIntegerMultiplication {
    public static void main(String[] args) {
        int n = 10; // You can change this value to generate numbers of different sizes
        String num1 = generateRandomNumber(n);
        String num2 = generateRandomNumber(n);
        System.out.println("A = " + num1);
        System.out.println("B = " + num2);
        String result = largeIntegerMultiplicationDiv3(num1, num2);
        System.out.println("The large integer multiplication from the division of three smaller integers is A*B = " + result);
    }

    public static String largeIntegerMultiplicationDiv3(String num1, String num2) {
        int n = Math.max(num1.length(), num2.length());

        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        } else if (n <= 3) {
            return String.valueOf(Long.parseLong(num1) * Long.parseLong(num2));
        } else {
            int m = n / 2;
            String x = num1.substring(0, n - m);
            String y = num1.substring(n - m);
            String w = num2.substring(0, n - m);
            String z = num2.substring(n - m);

            String prodXW = largeIntegerMultiplicationDiv3(x, w);
            String prodYZ = largeIntegerMultiplicationDiv3(y, z);
            String prodXZ_WY = add(largeIntegerMultiplicationDiv3(x, z), largeIntegerMultiplicationDiv3(w, y));

            String ans1 = prodXW + repeatZeros(2 * m);
            String ans2 = prodXZ_WY + repeatZeros(m);

            return add(add(ans1, ans2), prodYZ);
        }
    }

    public static String add(String num1, String num2) {
        int n1 = num1.length();
        int n2 = num2.length();
        int carry = 0;
        StringBuilder result = new StringBuilder();
        for (int i = n1 - 1, j = n2 - 1; i >= 0 || j >= 0 || carry != 0; i--, j--) {
            int digit1 = i < 0 ? 0 : num1.charAt(i) - '0';
            int digit2 = j < 0 ? 0 : num2.charAt(j) - '0';
            int sum = digit1 + digit2 + carry;
            result.insert(0, sum % 10);
            carry = sum / 10;
        }
        return result.toString();
    }

    public static String repeatZeros(int n) {
        return new String(new char[n]).replace("\0", "0");
    }
    
    public static String generateRandomNumber(int n) {
        Random random = new Random();
        StringBuilder sb = new StringBuilder();
        sb.append(random.nextInt(9) + 1); // Ensures the most significant digit is between 1 and 9
        for (int i = 1; i < n; i++) {
            sb.append(random.nextInt(10));
        }
        return sb.toString();
    }
}
