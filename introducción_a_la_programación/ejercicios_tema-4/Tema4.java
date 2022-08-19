public class Tema4{
    public static void main(String[] args){
            // conditional if
            System.out.println("If block");
            int numeroIf = 5;
            if(numeroIf > 0){
                System.out.println("Your variable is a positive number");
            } else if(numeroIf < 0){
                System.out.println("Your variable is a negative number");
            } else{
                System.out.println("Your variable is zero");
            }
            
            //while and do-while loops
            System.out.println("While and do-while block");
            int numeroWhile = 0;
            while(numeroWhile < 3){
                numeroWhile++;
                System.out.println(numeroWhile);
            }
            
            do{
                numeroWhile++;
                System.out.println(numeroWhile);
            }while(numeroWhile < 3);
            
            //for loop
            System.out.println("For block");
            for(int numeroFor = 0; numeroFor <= 3; numeroFor++){
                System.out.println(numeroFor);
                
            }
            
            //switch statement
            System.out.println("Switch block");
            String estacion = "SUMMER";
            switch(estacion){
                case "SPRING":
                    System.out.println("It's spring season");
                    break;
                case "SUMMER":
                    System.out.println("It's summer season");
                    break;
                case "AUTUMN":
                    System.out.println("It's autumn season");
                    break;
                case "WINTER":
                    System.out.println("It's winter season");
                    break;
            }
    }
}

//By Favio Varela