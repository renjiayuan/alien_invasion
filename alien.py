alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
point_value=alien_0.get('point','No point value assigned')
print(point_value)
for k,v in alien_0.items():#注意冒号
    print(f"\nKey:{k}")
    print(f"Value:{v}")