public class aprendendojava{
    public static void main(String[] args) {

        try{

        System.out.println("E nossa primeira pergunta é!");
        Thread.sleep(1000);
            System.out.println("2+2!");
                Thread.sleep(3000);
                    System.out.println("E o resultado é!");
                    Thread.sleep(500);
                        System.out.println(2+2);

                   } catch (InterruptedException e) {
            e.printStackTrace();

        }
    }
    
}