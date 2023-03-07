package Model;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;




public class Minesweeper{
    //Constatns
    static final char MINE = 'M';
    static final char COVERED = '-';

    //Variables
    private int rows;
    private int cols;
    private int mineCount;
    private GameState gameState;
    private int moveCount;
    private char[][] board;
    private boolean[][] booleanBoard;
    private MinesweeperObserver observer;

    //Constructor
    public Minesweeper(int rows, int cols, int mineCount){
        this.rows = rows;
        this.cols = cols;
        this.mineCount = mineCount;
        gameState = GameState.NOT_STARTED;

        makeBoards(mineCount);
    }

    //Copy Constructor
    public Minesweeper(Minesweeper template){

        this.rows = template.rows;
        this.cols = template.cols;
        this.board = new char[rows][cols];
        this.booleanBoard = new boolean[rows][cols];

        for(int i = 0; i < rows; i++){
            for(int i2 = 0; i2 < cols; i2++){
                this.board[i][i2] = template.board[i][i2];
                this.booleanBoard[i][i2] = template.booleanBoard[i][i2];
            }
        }
        
        this.gameState = template.gameState;
        this.mineCount = template.mineCount;
        this.moveCount = template.moveCount;
        
    }

    //Getters
    public int getMoveCount() {
        return moveCount;
    }

    public GameState getGameState() {
        return gameState;
    }

    public char getSymbol(Location location) throws MinesweeperException{
        if (location.getRow() < 0 || location.getRow() > rows || location.getCol() < 0 || location.getCol() > cols){
            throw new MinesweeperException("Out of bounds");
        }
        return board[location.getRow()][location.getCol()];
    }

    public int getMineCount(){
        return mineCount;
    }

    public int getRows(){
        return rows;
    }

    public int getCols(){
        return cols;
    }

    //Helpers
    //make board helper function
    private void makeBoards(int minecount){
        board = new char[rows][cols];
        booleanBoard = new boolean[rows][cols];

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                board[i][j] = '0';
                booleanBoard[i][j] = false;
            }
        }

        Random RNG = new Random();

        for(int i = 0; i < mineCount; i++){
            int randRow = RNG.nextInt(rows);
            int randCol = RNG.nextInt(cols);

            if(board[randRow][randCol] == MINE){
                i--;
                continue;
            }
            else{
                board[randRow][randCol] = MINE;
                setMines(getNeighbors(new Location(randRow, randCol)));
            }
        }
    }

    private List<Location> getNeighbors(Location location){
        Set<Location> pSelect = getPossibleSelections();
        List<Location> neighborList = new ArrayList<>();

        //Upper Diag Right
        if(pSelect.contains(new Location(location.getRow() + 1, location.getCol() + 1))){
            neighborList.add(new Location(location.getRow() + 1, location.getCol() + 1));
        }
        //Right
        if(pSelect.contains(new Location(location.getRow(), location.getCol() + 1))){
            neighborList.add(new Location(location.getRow(), location.getCol() + 1));
        }
        //Lower Diag Right
        if(pSelect.contains(new Location(location.getRow() - 1, location.getCol() + 1))){
            neighborList.add(new Location(location.getRow() - 1, location.getCol() + 1));
        }
        //Down
        if(pSelect.contains(new Location(location.getRow() - 1, location.getCol()))){
            neighborList.add(new Location(location.getRow() - 1, location.getCol()));
        }
        //Bottom Diag Left
        if(pSelect.contains(new Location(location.getRow() - 1, location.getCol() - 1))){
            neighborList.add(new Location(location.getRow() - 1, location.getCol() - 1));
        }
        //Left
        if(pSelect.contains(new Location(location.getRow(), location.getCol() - 1))){
            neighborList.add(new Location(location.getRow(), location.getCol() - 1));
        }
        //Upper Diag Left
        if(pSelect.contains(new Location(location.getRow() + 1, location.getCol() - 1))){
            neighborList.add(new Location(location.getRow() + 1, location.getCol() - 1));
        }
        //Up
        if(pSelect.contains(new Location(location.getRow() + 1, location.getCol()))){
            neighborList.add(new Location(location.getRow() + 1, location.getCol()));
        }

        return neighborList;
    }

    private void setMines(List<Location> neighborList){
        for(Location neighbor : neighborList){
            if(board[neighbor.getRow()][neighbor.getCol()] != MINE) board[neighbor.getRow()][neighbor.getCol()] ++;
        }
    }

    private void checkWin(){
        if(getPossibleSelections().size() <= mineCount){
            gameState = GameState.WIN;
            Set<Location> pSelections =  getPossibleSelections();
            for(Location location2 : pSelections){
                booleanBoard[location2.getRow()][location2.getCol()] = true;
                notifyObserver(location2, false);
            }
        }

    }

    //Behaviors
    public void makeFirstSelection(Location location)throws MinesweeperException{
        if(!booleanBoard[location.getRow()][location.getCol()]) moveCount++;
        makeSelection(location);
    }

    public void makeSelection(Location location)throws MinesweeperException{
        gameState = GameState.IN_PROGRESS;
        int r = location.getRow();
        int c = location.getCol();
        if (r >= rows || c >= cols){
            throw new MinesweeperException("Out of Bounds");
        }

        if(board[r][c] == '0'){
            List<Location> neighbors = getNeighbors(new Location(r, c));
            for(Location location2: neighbors){
                booleanBoard[location2.getRow()][location2.getCol()] = true;
            }
            for(Location location2: neighbors){
               makeSelection(location2);
            }
        }else if(board[r][c] == MINE){
            gameState = GameState.LOSS;
            Set<Location> pSelections =  getPossibleSelections();
            for(Location location2 : pSelections){
                booleanBoard[location2.getRow()][location2.getCol()] = true;
                notifyObserver(location2, false);
            }

        }else{
            booleanBoard[r][c] = true;
        }

        if(gameState != GameState.LOSS){
            checkWin();
        }

        notifyObserver(location, false);
        
    }

    public Set<Location> getPossibleSelections(){
        
        Set<Location> pSelect = new HashSet<>();
        
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if(!booleanBoard[i][j]){
                    Location location = new Location(i, j);
                    pSelect.add(location);
                }
            }
        }

        return pSelect;
    }

    public void getHint(Set<Location> possibleHints){

        for(Location hint : possibleHints){

            if(board[hint.getRow()][hint.getCol()] != MINE){
                notifyObserver(hint, true);
                break;
            }

        }
    }

    public boolean isCovered(Location location)throws MinesweeperException{
        if (location.getRow() < 0 || location.getRow() > rows || location.getCol() < 0 || location.getCol() > cols){
            throw new MinesweeperException("Out of bounds");
        }
        return !booleanBoard[location.getRow()][location.getCol()];
    }

    public void register(MinesweeperObserver observer){
        this.observer = observer;
    }

    private void notifyObserver(Location location, boolean isHint){
        if(observer != null){
            observer.cellUpdated(location, isHint);
        }
    }

    @Override
    public String toString() {
        String string = "";
        for (int i = 0; i < rows; i++){
            string += "\n";
            for (int j = 0; j < cols; j++){
                if(booleanBoard[i][j]){
                    string += "[" + board[i][j] + "] ";
                }else{
                    string += "[" + COVERED + "] ";
                }
            }
        }

        return string;
    }

}
