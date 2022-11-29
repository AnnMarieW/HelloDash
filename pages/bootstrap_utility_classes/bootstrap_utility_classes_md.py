

intro = """
## Bootstrap utility classes
Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content. See all the Bootstrap classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/).

Bootstrap utility classes can be applied to any Dash component to quickly style them without the need to write custom CSS rules. Just add them to the Dash component’s `className` prop.

For example, instead of using CSS in the `style` prop:
```
style={
    "backgroundColor": "blue",
    "padding": 16,
    "marginTop": 32,
    "textAlign": "center",
    "fontSize": 32,
}
```
You can use  Bootstrap utilities in the `className` prop:
```
className="bg-primary p-1 mt-2 text-center h2",
```
"""









arrange_elements_intro = """
### Position  
------------

Use these shorthand utilities for quickly configuring the position of an element.
Arrange elements easily with the edge positioning utilities. The format is {property}-{position}.

Where property is one of:
- `top` - for the vertical top position
- `start` - for the horizontal left position (in LTR)
- `bottom` - for the vertical bottom position
- `end` - for the horizontal right position (in LTR)  

Where position is one of:

- `0` - for 0 edge position
- `50` - for 50% edge position
- `100` - for 100% edge position
"""






translate_middle_intro = """
### Position - translate-middle 
------------

This class applies the transformations translateX(-50%) and translateY(-50%) to the element which, in combination
 with the edge positioning utilities, allows you to absolute center an element.

This is often used to create components with indicators.  See examples below.

"""





translate_middle_xy_intro = """
### Position - translate-middle 
------------

By adding `translate-middle-x` or `translate-middle-y` classes, elements can be positioned only in horizontal or vertical direction.
"""



next = """
-----------------  

### Next:  
Back to <dccLink href="/" children="Theme Explorer Home Page" />
"""