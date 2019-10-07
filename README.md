# Pencil Durability Kata
#### Requirements
- Python>=3.6
#### Build And Test
To run the tests, navigate to the root directory and run:

    python3 -m unittest discover tests/

#### Improvements For Future Versions
If the simulation required multiple types of writing instruments, it would be a farily obvious improvement to create a writing utensil class that each instrument would derive from. From this class you could subclass to define things like:
- disposable pens (does not require sharpening but ultimately wears out, non-erasable)
- mechanical pencils (replacable lead and eraser, perhaps fragile lead breaks at random)
- fountain pens (can be refilled when out of ink, non-erasable)
- erasable pens (leaves a terrible mess when erased)

I contemplated creating a factory for erasers but decided it was outside the scope of the kata. This factory would allow for things like erasers meant to slip over the top of a worn out eraser.
#### Note On 2HB Durability
[This voluenteer effort](http://towriteamockingbird.blogspot.com) was my favorite discovery when researching pencil point durability. A combination of [this post](http://towriteamockingbird.blogspot.com/2007/05/report-after-32-hours-into-effort.html) and [this post](http://towriteamockingbird.blogspot.com/2007/06/our-final-word-count-is.html) provide the following information
- The pencil was reduced to 3.2 inches after 32 sharpenings. I decided on a length of 35 (which would reduce the pencil to a reasonably unusable 3 inches).
- After 32 sharpenings, the pencil had written 32,000 words. The first chapter of their selected text has an average word length of 4.7, thus 32 sharpenings provided about 150,000 characters 
#### Some Thoughts
The spec says in various places:
- When a pencil is created, it **can** be provided with a value for point durability
- A pencil **should** also be created with an initial length value
- When a pencil is created, it **can** be provided with a value for eraser durability.

I was unsure how much importance to place on the bolded words. I originally took them to mean the pencil should instantiate with reasonable constants. I was unsatisfied with that solution because it left my test class messy, so my final version removes constants from the constructor and opts to use a simple factory to create pencils for the tests.

**I'm really looking forward to feedback!**