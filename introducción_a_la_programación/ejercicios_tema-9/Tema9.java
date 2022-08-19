public class Tema9{
    public static void main(String[] args) {
        Cliente client = new Cliente();
        Trabajador employee = new Trabajador();

        client.setAge(30);
        client.setName("Celeste");;
        client.setTelephone(5529876543L);

        System.out.println(client.getAge());
        System.out.println(client.getName());
        System.out.println(client.getTelephone());
        
        employee.setAge(28);
        employee.setName("Favio");;
        employee.setTelephone(5521234567L);


        System.out.println(employee.getAge());
        System.out.println(employee.getName());
        System.out.println(employee.getTelephone());
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
    private int credito;

    public int getCredito() {
        return credito;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    private int salario;

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

}