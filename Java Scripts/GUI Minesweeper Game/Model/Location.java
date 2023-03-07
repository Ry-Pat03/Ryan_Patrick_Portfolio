package Model;

public class Location{
    //Variables
    private int row;
    private int col;

    //Constructor
    public Location(int row, int col){
        this.row = row;
        this.col = col;
    }

    //Getters
    public int getRow(){
        return row;
    }

    public int getCol(){
        return col;
    }

    @Override
    public int hashCode() {
        return (int)(Math.pow(27, row) + Math.pow(31, col));
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof Location)){
            return false;
        }
        else{
            Location newLocal = (Location)obj;
            return this.getCol() == newLocal.getCol() && this.getRow() == newLocal.getRow();
        }
    }

    @Override
    public String toString() {
        return "[" + row + ", " + col + "]";
    }
    
}