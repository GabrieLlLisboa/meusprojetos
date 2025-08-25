public class aprendendojava{
    public static void main(String[] args) {

        try {

        int idade = 30;
        String nome = "Samuel";

        System.out.println("Mostrando suas informações...");
        Thread.sleep(500);
        System.out.println("Seu nome é: " + nome);
        System.out.println("Sua idade é: " + idade);
        Thread.sleep(1000);
        System.out.println("Fim");


        } catch (InterruptedException e) {

            e.printStackTrace();
        }

     }

 }


