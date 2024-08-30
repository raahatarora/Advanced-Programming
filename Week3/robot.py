movement_distances = {
    
    'UP' : 5,
    'DOWN' : 3,
    'LEFT' : 3,
    'RIGHT' : 2
}

x,y = 0,0

movements = [
    
    ('UP',2),
    ('RIGHT',3),
    ('DOWN',1),
    ('LEFT',1) 
]

for direction , steps in  movements:
    if direction == 'UP':
        y+= movement_distances['UP']*steps
    elif direction == 'DOWN' :
        y-=movement_distances['DOWN']*steps
    elif direction == 'LEFT' :
        x-=movement_distances['LEFT']*steps
    elif direction == 'RIGHT':
        x += movement_distances["RIGHT"]*steps
        
        
distance = (x**2 + y**2) ** 0.5

distance_rounded = round(distance)

print(f"Final Position: ({x},{y}")
print(f"Distance from origin (rounded): {distance_rounded}")