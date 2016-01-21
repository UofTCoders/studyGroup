---
layout: page
title: 'Intro to Ruby'
visible: true
---

# Introduction to Ruby (for beginners)

- **Authors**: Jenna Blumenthal
- **Research field**: Mechanical & Industrial Engineering
- **Lesson topic**: Introduction to Ruby
- **Lesson content URL**: <https://github.com/jennaleeb/ruby_workshop>

This is a very basic introduction to Ruby directed for those without much programming experience. It will cover using the terminal and interative ruby shell (IRB), data types, objects/classes, methods, conditional logic, and running a program from a file in the terminal.

Content source:
---------------
Based on the [**workshop**](https://github.com/ladieslearningcode/Ruby) developed by [Dessy Deskalov](https://twitter.com/dess_e) for [Ladies Learning Code](http://ladieslearningcode.com/)

Agenda
------

-   What is Ruby?
-   Working in the Terminal
-   Data Types
-   Methods
-   Objects and Classes
-   Writing/running a program
-   Control Flow

What is Ruby?
=============

Ruby is a programming language
------------------------------

Why do people love Ruby?

-   Easy to learn (compared to C, C++, Java)
-   Forgiving syntax
-   Large and supportive online community

Created in 1993 by Yukihiro Matsumoto, from Japan.

> "I hope to see Ruby help every programmer in the world to be productive, and to enjoy programming, and to be happy. That is the primary purpose of the Ruby language."

Ruby in the Command Line
------------------------

The IRB ("Interactive Ruby Shell") is an interactive command-line interpreter that can be used to test code quickly.

### OS X

    Applications -> Utilities -> Terminal

### Windows

(C:\\windows\\system32\\cmd.exe)
    
    Start -> All Programs -> Accessories -> Command Prompt

Using IRB (Interactive Ruby)
----------------------------

Type IRB into the console

    irb

Then you'll see somthing like this:

    ruby-1.9.2-p290 :001 >

What can Ruby do?
-----------------

Try typing:

    irb(main):001:0>puts "Hello World"
        Hello World
        => nil

`puts` is the basic command to print something out in Ruby.
`=> nill` is the result of the expression.

Math:

    > 1 + 1
    => 2

    > 462 * 86
    => 39732

Data Types
==========

Data Types
----------

Numbers without decimals are called `INTEGERS`. We just did some math with some integers.

Letters, words, and sentences are called `STRINGS`. We tell Ruby that we are intending to use a string by wrapping it in quotes.

Some other data types in Ruby:

-   `binary`
-   `boolean`
-   `float`
-   `decimal`
-   ...

Variables
=========

How do Variables Work?
----------------------

What if we want to remember the result of some of this math? Assign the result to a variable.

    irb(main):007:0> a = 3 ** 2 
    => 9 
    irb(main):007:0> b = 4 ** 2
    => 16
    irb(main):007:0> Math.sqrt(a+b)
    => 5.0
        
      

We can also assign a String to a variable

    irb(main):007:0> my_name = "John Doe" 
     => "John Doe" 
      

Telling Ruby the `variable` **my\_name** points to the `string` "**John Doe**".

Objects
=======

Objects, Objects, Everywhere!
-----------------------------

Everything in Ruby is an `Object`.

Great, but what is an object?

An `OBJECT` is an `INSTANCE` of a `CLASS`.

### A what is a what of a what?

<img src="http://i.imgur.com/U1PHT7H.gif" class="delayed" />

Classes
-------

Before she can do something with an object, Ruby needs to know what kind of `object` she's dealing with.

    irb(main):007:0> 1+1 
    => 2 
    irb(main):007:0> "1" + "1" 
    => "11"

### So how do classes help?

`Classes` define `objects` and what can be done with them.

The **Integer** `class` will have different instructions for "+" than the **String** `class`.

`Objects` have an **IS A** relationship with their `classes`.

Methods
-------

The **actions** you can perform on an `object` are called `methods`.

Every `object` that IS A `class` can perform the methods defined by that class.

    irb(main):010:0> def hi 
    irb(main):011:1>   puts "Hello World!" 
    irb(main):012:1> end 
    => :hi

Integer Methods
---------------

The `Integer class` has instructions for the methods **next**, **odd?**, and **even?**.

You can call **next**, **odd?**, and **even?** on ALL Objects that are `Integers`

String Methods
--------------

The `String class` has instructions for the methods **capitalize**, **upcase**, and **reverse**.

You can call **capitalize**, **upcase**, and **reverse** on ALL `Objects` that are `Strings`.

Playing with Integers
---------------------

    > 99.zero?
    => false

    > 99.odd?
    => true

    > 99.even?
    => false

Another example
---------------

    > title = "Peter Rabbit"
    > title.reverse

 | 
 --- | ---
What am I supposed to do with this object? | `reverse`
Do I know how to do that action on this object? | Yes! The `String` class defines a method **reverse** and returns the string in reverse order.

    =>"tibbaR reteP"

Fun with strings
----------------

    > "universityoftoronto".capitalize
    => "Universityoftoronto"

    > "universityoftoronto".upcase
    => "UNIVERSITYOFTORONTO"

    > "UNIVERSITYOFTORONTO".downcase
    => "universityoftoronto"

    > "universityoftoronto".reverse
    => "otnorotfoytisrevinu"

Method Errors
-------------

    > myNumber = 123
    > myNumber.reverse

 | 
--- | ---
What am I supposed to do with this object? | `reverse`
Do I know how to do that action on this object? | No. The **Integer** class does not define a method **reverse**.

    => NoMethodError: undefined method `reverse' for 123:Fixnum
        from (irb):1
        from :0
      

Methods and Objects and Classes, Oh My!
---------------------------------------

How can I find the class of my object?

    > mysteryObject = "What am I?"
    > mysteryObject.class
    => String

How do I know what methods I can call on my object?

    > mysteryObject.methods
    => ["upcase!", "zip", "pretty_print_cycle"....]

How do I know what those methods do?

Look them up [**here**](http://ruby-doc.org/)

Built-in Classes
----------------

Ruby comes with many built-in classes that we can use.

`String`, `Integer`, `File`, `Hash`, `Array`...

You can read about all the built-in objects [**here**](http://www.ruby-doc.org/core-2.0/)

Custom Classes
--------------

What if we want to define our own class?

Let's return to the `method` **hi** we wrote (and improve it)

    irb(main):010:0> def hi(name) 
    irb(main):011:1>   puts "Hello #{name}!" 
    irb(main):012:1> end 
    => :hi

The `method` **hi** takes the **name** as a `parameter`.

`#{name}` is Ruby's way of inserting something into a string

    irb(main):024:0> class Greeter
    irb(main):025:1>   def initialize(name)
    irb(main):026:2>     @name = name
    irb(main):027:2>   end
    
    irb(main):028:1>   def say_hi
    irb(main):029:2>     puts "Hi #{@name}!"
    irb(main):030:2>   end
    irb(main):034:1> end
    => nil
      

The new keyword here is `class`. This defines a new class called Greeter and a bunch of methods for that class. Also notice `@name`. This is an instance variable, and is available to all the methods of the class. As you can see it’s used by `say_hi`.

Custom Classes
--------------

Lets create a **Greeter** object and use it:

    irb(main):035:0> greeter = Greeter.new("Pat")
    => #
    irb(main):036:0> greeter.say_hi
    Hi Pat!
    => nil

The method `new` is a unique type of method, which is predefined in the Ruby library. The new method belongs to the class methods. The `initialize` method is a special type of method, which will be executed when the `new` method of the class is called with parameters.

Custom Classes: Exercise
------------------------

Let's make a class `Calculator` that has the methods `add` and `subtract`

    irb(main):035:0> my_calculator = Calculator.new
    => # 
    irb(main):036:0> my_calculator.add(5,2)
    7
    => nil
    irb(main):036:0> my_calculator.subtract(5,2)
    3
    => nil

Custom Classes: Solution
------------------------

    irb(main):024:0> class Calculator
    
    irb(main):025:1>   def add(x,y)
    irb(main):026:2>     puts x + y
    irb(main):027:2>   end
    
    irb(main):028:1>   def subtract(x,y)
    irb(main):029:2>     puts x - y
    irb(main):030:2>   end
    irb(main):034:1> end
    => nil

Writing a Program
-----------------

Open any text editor, add the same code, and save it as twitter.rb.
Remember the directory you have saved it in.

    tweet = "I'm writing my first program and it's pretty rad."
    puts tweet.length

To run your program, type **quit** to exit from IRB, and then type:

    ruby twitter.rb

Getting Input From the User
---------------------------

### The real Twitter...

Asks you to type something.

Tells you how many characters you're working with.

So far, we've just been putting our tweet directly into the program.

Asking for Input
----------------

The **puts** `method` is used for output, and the **gets** `method` is used for input. Try this:

The gets `method` warns Ruby that you're about to speak.

    > tweet = gets
     all-string
    I'm learning Ruby with #ladieslearningcode
    
    => "I'm learning Ruby with #ladieslearningcode\n"

Wait, we didn't type \\n in our tweet. What is that?

Asking for Input
----------------

The \\n is there because you hit the enter button after you typed your tweet. It represents a new line, and counts as exactly one character. To get rid of it, do this:

    > tweet = gets.chomp
     all-string
    I'm learning Ruby with #ladieslearningcode
    
    => "I'm learning Ruby with #ladieslearningcode"

Asking for Input
----------------

Now try this:

    > tweet = gets.chomp
     all-string
    I'm a lady learning code with @learningcode #ladieslearningcode

    => "I'm a lady learning code with @learningcode #ladieslearningcode"

    > puts tweet
     all-string
    I'm a lady learning code with @learningcode #ladieslearningcode
    => nil

Back to your Twitter Program
----------------------------

Working with your group, modify your Twitter program to do the following:

1. Ask (politely!) for a tweet from the user.

2. Store the tweet in a variable, without \\n

3. Output the tweet the user gave.

4. Output the number of characters in the tweet.

5. Output how many **more** characters the user can add until they hit 140 characters.

(answers in assignments/twitter\_3.rb)

Giving Output Based on Input
----------------------------

Twitter...

Lets you send your tweet if it is 140 characters or less

Tells you that your tweet is too long to send otherwise.

Giving Output Based on Input
----------------------------

So far we know how to determine the length of the user's tweet.

We don't know how to tell them whether they can or cannot send their tweet, depending on it's length.

Conditional Logic
-----------------

Programming is writing out sets of simple instructions for the computer to follow.

Let's break down out tweet logic into simple instructions.

Conditional Logic
-----------------

We want our program to ...

if the tweet is greater than 140 characters, tell the user that they cannot send their tweet

if the tweet is less than or equal to 140 characters, tell the user that they can send their tweet

Conditional Logic
-----------------

Logical operators

-   &gt;
-   &lt;
-   &gt;=
-   &lt;=
-   ==

<!-- -->

    > 200 > 140

    => true
    
    > 200 < 140
    
    => false

Conditional Logic: IF Statements
--------------------------------

Try the code below in IRB:

    >if 200 > 140 
    >  puts true
    >end

    => true

Conditional Logic: IF/ELSE Statements
-------------------------------------

Try the code below in IRB:

    >if 200 > 140 
    > puts true
    >else
      puts false
    >end

    => true

Conditional Logic in Our Simple Twitter
---------------------------------------

    tweet = gets.chomp

    if tweet.length <= 140
      puts "Tweet your heart out!"
    end

Conditional Logic in Our Simple Twitter
---------------------------------------

    tweet = gets.chomp

    if tweet.length <= 140
      puts "Tweet your heart out!"
    else
      puts "Your tweet is too long!"
    end

While Loops
-----------

What if you want to be able to tell your program when to stop running? Create a new program with the following code.

    puts "Hi!"
    greeting = gets.chomp

    while greeting != "bye!"
      puts greeting
      greeting = gets.chomp
    end

This is called a while loop. The program will run while the user inputs anything other than "bye!"

Arrays
------

    [1, 2, 3, 4, 5]

    [7, 13, 14, 16, 14, 48]

    ["ladies", "learning", "code"]

Iterating through an Array
--------------------------

     > my_numbers = [1, 2, 3, 4, 5]
     > my_numbers.each do |i| 
     >  puts i**2 
     > end 

Final Task
----------

-   Make an array of 5 tweets.
-   For every tweet, check the number of characters.
-   If the tweet is too long, give the user an error message.
-   If the tweet is &lt; 140 characters, print the tweet.

Credits
-------

Inspired by Chris Pine's **Learn to Program**

![](framework/img/workshop/learn-to-program.jpg)

Resources
---------

[Learn Ruby in 20 Minutes](http://www.ruby-lang.org/en/documentation/quickstart/)

[why's poignent guide to Ruby](http://mislav.uniqpath.com/poignant-guide/)

[Ruby Koans](http://rubykoans.com/)

[Rails](http://rubyonrails.org/screencasts)

[Lots more!](http://www.ruby-lang.org/en/documentation/)

And finally...

Thank you!
==========

[![Creative Commons License](framework/img/cc-by-nc.svg)](http://creativecommons.org/licenses/by-nc/4.0/) by [Ladies Learning Code](http://ladieslearningcode.com)
