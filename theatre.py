import sys

def solution():
    #  seat matrix  with 0 represent vacant, 1 represents occupied
    #  initializing all seats vacant with 0
    seats = [[0] * 20 for _ in range(10)] 

    # we have a dictionary to record whether a row is full (no avalible seats).
    #isfull = {row : False for row in range(10)}
    
    # Read input file into a list
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    f = open(inFile, "r").readlines()
    input = [s.split(" ") for s in f]

    
    
    # List that store each reservation
    res = []

    # DFS that find avalible seats. 
    def dfs(r, c, remain, positions, resIndex):
        """ Base case that we found a valid reservation of seats
             we set these seat occupied in the matrix. """
        if remain == 0:
            #set these seat occupied in the matrix
            for row, col in positions:
                seats[row][col] = 1
            #put positions into result
            res.append([resIndex,positions])
            #check whether this row have no avalible seats
            #if all(seats[r]): isfull[r] = True
            return True

        """ Check whether a row is full. """
        #if isfull[r]:
            #return False


        """ Case that the seat is already occupied or invalid. """
        if seats[r][c] != 0:
            return False

        """ Case that the row is not enough for reservation"""
        if c + remain > 20:
            return False

        """ Case that the seat is not buffer by 3 positions. """
        # we set (r, c) in seats 2 if (r, c) cannot be used anyway, so we do not need to check next time
        for i in range(1, 4):
            # whether either left 3 is occupied
            if c - i >= 0 and seats[r][c - i] == 1:
                seats[r][c] = 2
                return False
            # whether either right 3 is occupied
            if c + i <= 19 and seats[r][c + i] == 1:
                seats[r][c] = 2
                return False


        """ Case that the seat is not buffer by 1 row. """
        # whether up 1 is occupied
        if r - 1 > -1 and seats[r - 1][c] == 1:
            seats[r][c] = 2
            return False
        # whether down 1 is occupied
        if r + 1 < 9 and seats[r + 1][c] == 1:
            seats[r][c] = 2
            return False

        return dfs(r, c + 1, remain - 1, positions + [(r, c)], resIndex)
        
    print(input)
    # Start DFS, append reservation index and (seat positions or an explaination)
    for resIndex, num in input:
        if num[:-1].isalpha() or int(num[:-1]) < 1 or int(num[:-1]) > 20:
            res.append([resIndex, "Invalid Reservation"])
            continue
        for r in range(10):
            #if isfull[r]:
                #continue
            for c in range(20):
                found = dfs(r, c, int(num[:-1]), [], resIndex)
                if found:break
            if found: break
        if not found: res.append([resIndex, "Cannot reserve since we don't have enough positions"])

    # Write output file.
    f = open(outFile, "w")
    for resIndex, positions in res:
        f.write(resIndex + " ")
        if isinstance(positions, list):
            for row, col in positions[:-1]:
                f.write(chr(65 + row) + str(col) + ", ")
            f.write(chr(65 + positions[-1][0]) + str(positions[-1][1]) + "\n")
        else:
            f.write(positions + "\n")
    f.close()
    return f

solution()



    
       

        
        
