using System;

public class desafioIfs {

    public static void Main() {
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBenefico = float.Parse(Console.ReadLine());

        float valorImposto = 0;
        
        if(valorSalario >= 0 && valorSalario <= 1100) {
            valorImposto = 0.05F * valorSalario;
        }
        else if(valorSalario >= 1101 && valorSalario <= 2500) {
            valorImposto = 0.10F * valorSalario;
        }
        else {
            valorImposto = 0.15F * valorSalario;
        }

        float saida = valorSalario - valorImposto + valorBenefico;
        Console.WhiteLine(saida.ToString("0.00"));

    }
    
}