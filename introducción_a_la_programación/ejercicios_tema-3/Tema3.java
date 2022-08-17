public class Tema3{    
    public static void main(String[] args) {
        // Primera parate - 1st section
        sum(7, 14, 21);
        // Segunda parte - Second section
        Car myCar = new Car();
        myCar.incrementDoors();
        System.out.println(myCar.doors);
    
    }
    
    public static int sum(int a, int b, int c) {
        return a + b + c;
    }
    
}
    class Car {
        public int doors = 0;
    
        public void incrementDoors() {
            this.doors++;
        }
    }

    // By Favio Varela