def TowerOfHanoi(n , rod1, rod2, aux_rod):
    if n == 1:
        print ("Move disk 1 from rod",rod1,"to rod",rod2)
        return
    TowerOfHanoi(n-1, rod1, aux_rod, rod2)
    print ("Move disk",n,"from rod",rod1,"to rod",rod2)
    TowerOfHanoi(n-1, aux_rod, rod2, rod1)

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, B, C are the rod
