public class Tema8{
    public static void main(String[] args) {
        Persona person = new Persona();

        person.setAge(28);
        person.setName("Favio");;
        person.setTelephone(5521234567L);

        System.out.println(person.getAge());
        System.out.println(person.getName());
        System.out.println(person.getTelephone());
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

//By Favio Varela