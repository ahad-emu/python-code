class Age:
    def __init__(self, n):
        self.n = n
        if self.n <= 0:
            print("invalids")
        elif self.n < 13 :
            print("you are young")
        elif self.n >= 13 and self.n < 18 :
            print("You are a teenager")
        else:
            print("You are old")

number = int(input())
while number > 0 :
    age = int(input())
    user = Age(age)
    number = number - 1
class Person{
    public:
        int age;
        Person(int initialAge);
        void amIOld();
        void yearPasses();
    };


    Person::Person(int initialAge){
        // Add some more code to run some checks on initialAge

        if(initialAge <= 0)
            {
            age = 0;
            cout<<"Age is not valid, setting age to 0."<<endl;
        }
        else
            age = initialAge;

    }
    void Person::amIOld(){
        // Do some computations in here and print out the correct statement to the console
        if(age<13)
            {
            cout<<"You are young."<<endl;
        }
        else if(age>=13 && age<18)
            {
            cout<<"You are a teenager."<<endl;
        }
        else if(age>=18)
            cout<<"You are old."<<endl;
    }
    void Person::yearPasses(){
        // Increment the age of the person in here
        age++;
    }
