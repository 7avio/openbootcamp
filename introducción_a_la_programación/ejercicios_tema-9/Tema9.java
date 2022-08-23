public class Tema9{
    public static void main(String[] args) {
        Cliente client = new Cliente();
        Trabajador employee = new Trabajador();

        client.setName("Celeste");
        client.setAge(30);
        client.setTelephone(5529876543L);
        client.setCredit(50000);
        System.out.println( client.getName() + " (" + client.getAge() + ") " + " with contact number: " + client.getTelephone() + ". Has $" + client.getCredit() + " of credit in their account."  );
        
        
        employee.setName("Favio");;
        employee.setAge(28);
        employee.setTelephone(5521234567L);
        employee.setSalary(50000);
        
        System.out.println( employee.getName() + " (" + employee.getAge() + ") " + " with contact number: " + employee.getTelephone() + ". Reach $" + employee.getSalary() + " per year."  );
        
    }
}

class Persona {
    private int age;
    private String name;
    private long telephone;

    
    public void setAge(int age) {
        this.age = age;
    }
    public int getAge() {
        return age;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public long getTelephone() {
        return telephone;
    }
    public void setTelephone(long telephone) {
        this.telephone = telephone;
    }
}


class Cliente extends Persona{
    private double credito;

    public double getCredit() {
        return credito;
    }

    public void setCredit(double credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    private double salario;

    public double getSalary() {
        return salario;
    }

    public void setSalary(double salario) {
        this.salario = salario;
    }

}