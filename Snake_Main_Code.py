import Library_Snake as snake_objs
import time

delay=0.1
color_wnd='light green'
color_head='blue'
color_snake='brown'
color_food='red'

screen=snake_objs.Screen(600,600,color_wnd)
food=snake_objs.Food(color_food,'turtle')
snakes=[snake_objs.Snake(i*30,i*50,'turtle',color_snake,color_head)for i in range(1)]

screen.proc_event(snakes)

while True:
    screen.update()

    for snake in snakes:
        for i in snakes:
            if i.check_error():
                i.step()
            else:
                screen.end_game()
        if snake.check_food(food):
            snake.grow()
            screen.plot_score()
            food.move()

    time.sleep(delay)