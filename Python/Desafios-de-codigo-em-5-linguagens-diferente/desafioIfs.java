import java.util.Scanner;

public class desafioIfs {

    public static void main(String[] args) {
        //Ler valores de entrada
        Scanner leitorDeEntrada =  new Scanner(System.in);
        float valorSalario = leitorDeEntrada.nextFloat();
        float valorBenefico = leitorDeEntrada.nextFloat();

        float valorImposto = 0;
        
        if(valorSalario >= 0 && valorSalario <= 1100) {
            //atribui a aliquota de 5%
            valorImposto = 0.05F * valorSalario;
        }
        else if(valorSalario >= 110.01 && valorSalario <= 2500) {
            valorImposto = 0.10F * valorSalario;
        }
        else {
            valorImposto = 0.15F * valorSalario;
        }

        float saida = valorSalario - valorImposto + valorBenefico;
        System.out.println(String.format("%.2f", saida));

    }
    
}