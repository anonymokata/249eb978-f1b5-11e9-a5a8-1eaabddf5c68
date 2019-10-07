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

I contemplated also creating a factory for erasers but decided it was outside the scope of the kata. This factory would allow for things like erasers meant to slip over the top of a worn out eraser.
#### Note On 2HB Durability
[This voluenteer effort](http://towriteamockingbird.blogspot.com) was my favorite discovery when researching pencil point durability. A combination of [this post,](http://towriteamockingbird.blogspot.com/2007/05/report-after-32-hours-into-effort.html) [this post,](http://towriteamockingbird.blogspot.com/2007/06/our-final-word-count-is.html) and some analysis of the first chapter of the text selected by the linked project provide the following information:
- The 6.65" pencil was reduced to 3.2" after 32 sharpenings, thus the pencil degrades approximately .011" per sharpening.
- The pencil had written 32,000 words after 32 sharpenings, thus the pencil writes approximately 1,000 words per sharpening.
- The average word length of the first chapter of the text is 4.7 characters and 3.4% of those characters are capital letters or digits, thus the pencil writes approximately 160 capital and 4540 lowercase letters per sharpening - or 4860 units of durability by the degradation rules in the kata.

I chose a value of 44 for the pencil length - this brings a real life pencil to a barely usable 2". I'm using the point durability achieved by the voluenteers (4860). In determining a value for eraser durability, I made the idealistic assumption that a pencil would be able to erase every character it has written.

#### Some Thoughts
The spec says in various places:
- When a pencil is created, it **can** be provided with a value for point durability
- A pencil **should** also be created with an initial length value
- When a pencil is created, it **can** be provided with a value for eraser durability.

I was unsure how much importance to place on the bolded words. I originally took them to mean the pencil should instantiate with reasonable constants. I was unsatisfied with that solution because it left my test class messy, so my final version removes constants from the constructor and opts to use a simple factory to create pencils for the tests.


**I had a blast working on this and I'm really looking forward to your feedback! Thanks!**