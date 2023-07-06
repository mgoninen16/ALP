import play

'''
def smiley():
  face = play.new_circle(
          color='yellow', 
          x=0, 
          y=25, 
          radius=250, 
          border_color="black", 
          border_width=10, 
          transparency=100
      )
  
  leye = play.new_circle(
          color='black', 
          x=-105, 
          y=100, 
          radius=50, 
          border_color="black", 
          border_width=0, 
          transparency=100
      )
  
  reye = play.new_circle(
          color='black', 
          x=105, 
          y=100, 
          radius=50, 
          border_color="black", 
          border_width=0, 
          transparency=100
      )

  mouth = play.new_text(
          words='\/', 
          x=0, 
          y=-100, 
          angle=0, 
          font="arial", 
          font_size=200, 
          color='black', 
          transparency=100
      )
  
  play.set_backdrop('light yellow')
  
  greeting = play.new_text(
          words='\"smiley face.\"', 
          x=0, 
          y=-260, 
          angle=0, 
          font="arial", 
          font_size=50, 
          color='black', 
          transparency=100
      )

smiley()
'''

play.set_backdrop('light yellow')

sprite = play.new_box(
        color='black',
        x=0,
        y=0,
        width=100,
        height=200,
        border_color="light blue",
        border_width=10
    )

greeting = play.new_text(
        words='bouncing box', 
        x=0, 
        y=0, 
        angle=0, 
        font=None, 
        font_size=50, 
        color='black', 
        transparency=100
    )

sprite.start_physics(can_move=True, stable=False, x_speed=0, y_speed=200, obeys_gravity=True, bounciness=3, mass=1, friction=0.1)
greeting.start_physics(can_move=True, stable=False, x_speed=0, y_speed=200, obeys_gravity=True, bounciness=3, mass=1, friction=0.1)

play.start_program()