
TERMINOLOGY 

A class "member" refers to anything defined on a class

An "object" refers to an instance of a class.
Not to be confused with object type!



* Fields: A variable of any type that is declared directly in a class

eg:
class Person
{
	static int IDEAL_FRIEND_AWESOMENESS = 75;

	public string Name;
	public int Age;
	private int Awesomeness;
	private Person BestFriend;
}



* Methods: A function that is declared directly in a class, 
	used to define actions that the class can perform.

class Person
{
	private void SayName()
	{
		Console.WriteLine(Name);
	}

	private void NewBestFriend(Person newFriend)
       	{
		// CHECK FOR NULL !!!!
		if(BestFriend != null && BestFriend.Awesomeness < IDEAL_FRIEND_AWESOMENESS)
		{
			BestFriend = newFriend;	
		}

	}
}

static class Program
{
	public static void Main(string[] args)
	{
		
		Person me = new Person()
		{
			Name = "Devon",
			Age = 34,
			Awesomeness = 60
		};
		
		
		Person you = new Person()
		{
			Name = "Josiah",
			Age = 25,
			Awesomeness = 100
			BestFriend = me
		};

		// => void
		me.SayName();
		// > Devon
		
		me.NewBestFriend(you);
		
		Console.WriteLine(me.DoubleAge);
		
		me.Age = 1000;
		me.Name = "Goofer";


		Console.WriteLine(me.Awesome);
		// > 60
	}
}

* Properties: A special type of method that provides a flexible way to read/write/compute 
*             the value of a field.


	get/set keywords are used to return/assign values to a field
(known as Getters/Setters)


	auto-implemented properties are commonly used to create fields

class Person
{
	public int Awesome
	{
		get { return Awesomness; }
	}

	public int DoubleAge	
	{
		get { return 2 * Age; }
	}
}




* Access modifiers
public, private, protected, internal

public: accessable to any class in your codebase
private: accessable only within THIS class
	 protected: accessable only within THIS class, and all of its children
internal: accessable anywhere within assembely (.dll file)



	     Let's re-define our Person class 


	     public class Person
{
	private string _firstName;
	private string _lastName;

	public string FullName
	{
		get { return $"{_firstName} {_lastName}"; }
	}

	protected string NewFirstName
	{
		set { _firstName = value; }
	}

	public void SayName()
	{
		Console.WriteLine(FullName);
	} 

	// auto-implemented property
	public int Age {get; set;}

}


