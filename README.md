# Pencil Durability Kata

### Requirements
- Python>=3.6

### Build And Test
To run the tests, navigate to the root directory and run:

    python3 -m unittest discover tests/

### Improvements For Future Versions
A future version of this code could be improved by creating a WritingUtensil parent class. This class could be used to subclass other utensils, for example:
- disposable pens (do not require sharpening but ultimately wear out, non-erasable)
- mechanical pencils (infinitely replacable lead and eraser, fragile lead breaks at random)
- fountain pens (can be refilled, non-erasable)
- erasable pens (leave a terrible mess when erased)

### A Note On 2HB Durability

A quick search turned up [this voluenteer effort](http://towriteamockingbird.blogspot.com). A combination of [this post,](http://towriteamockingbird.blogspot.com/2007/05/report-after-32-hours-into-effort.html) [this post,](http://towriteamockingbird.blogspot.com/2007/06/our-final-word-count-is.html) and some analysis of the first chapter of the text selected by the linked project yield the following information:

- The 6.65" pencil was reduced to 3.2" after 32 sharpenings, thus the pencil degrades approximately .011" per sharpening.
- The pencil had written 32,000 words after 32 sharpenings, thus the pencil writes approximately 1,000 words per sharpening.
- The average word length of the first chapter of the text is 4.7 characters and 3.4% of those characters are capital letters or digits, thus the pencil writes approximately 160 capital and 4540 lowercase letters per sharpening. That equates to 4860 units of durability by the degradation rules in the kata.

A length value of 44 was chosen - this brings a real life pencil to a barely usable 2". The chosen point durability reflects the results of the voluenteer project. The eraser durability is based on the idealistic assumption that a pencil's eraser is durable enough to erase every character written by the pencil.

**I had a blast working on this and I'm really looking forward to your feedback! Thanks!**