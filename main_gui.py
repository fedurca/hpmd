from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

# Create the App class 
class TutorialApp(App): 
      
    def build(self): 
  
        b = BoxLayout(orientation ='vertical') 
  
        # Adding the text input 
        t = TextInput(font_size = 50, 
                      size_hint_y = None, 
                      height = 100) 
          
        f = FloatLayout() 
  
        # By this you are able to move the 
        # Text on the screen to anywhere you want 
        s = Scatter() 
  
        l = Label(text ="Hello !", 
                  font_size = 50) 
  
        f.add_widget(s) 
        s.add_widget(l) 
  
        b.add_widget(t) 
        b.add_widget(f) 
  
        # Binding it with the label 
        t.bind(text = l.setter('text')) 
  
          
        return b 
  
# Run the App 
if __name__ == "__main__": 
    TutorialApp().run() 