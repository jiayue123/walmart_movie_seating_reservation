# Movie-Theater-Seating-Challenge---2020

## Assumptions:

  1. First Come first Serve
  2. Checked avaliable seats alphabetically starts from row "A".
  3. Checked every reservation should buffer at least one row or three positions.
  4. If no reservation option, print "Cannot reserve since we don't have valid positions."
  5. Can Reserved 20 seats once. 

## instructions for building the solution

  1. Using a 2D-grids represents the theatre contains 200 seats (10 X 20).
  2. Read input file into a list of reservation identifier and # of needed seats(pair).
  3. Declare a Depth First Search Function to Find avaliable reservation.
  4. In 2D-Grids, 0 represents vacent, 1 represents occupied, 2 represents unavaliable since buffer of 3 seats or 1 row.
  5. Searching start from each grid, here are some case that fail search, and need to start from other grids.
     * Demand seats more than avaliable seats in the row
     * No buffer of 3 seats or 1 row (Mark it as unavaliable)
     * This seat is already occupied or invalid. 
  6. Using dfs function in every reservation information.
  7. Write the result into output file.

## Test
  1. Using command python theatre.py input.txt outout.txt
 
  
