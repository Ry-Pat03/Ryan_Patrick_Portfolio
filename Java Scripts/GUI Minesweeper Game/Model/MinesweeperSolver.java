package Model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;


import backtracker.Configuration;

public class MinesweeperSolver implements Configuration{

    private Minesweeper mineBoard;
    private Location[] moves;
    private int rows, cols, mineCount;

    //intial config
    public MinesweeperSolver(int rows, int cols, int mineCount){
        this.rows = rows;
        this.cols = cols;
        this.mineCount = mineCount;
        moves = new Location[1];
        this.mineBoard = new Minesweeper(rows, cols, mineCount);
    }

    //deep copy configuration
    public MinesweeperSolver(int rows, int cols, int mineCount,  Location[] moves, Minesweeper mineBoard){
        this.rows = rows;
        this.cols = cols;
        this.mineCount = mineCount;
        this.mineBoard = mineBoard;
        this.moves = moves;
    }

    @Override
    public Collection<Configuration> getSuccessors() {
        Collection<Configuration> successors = new ArrayList<>();
        for(Location location: mineBoard.getPossibleSelections()){

            Minesweeper deepCopy = new Minesweeper(mineBoard);
            moves[moves.length - 1] = location;
            MinesweeperSolver succesor = new MinesweeperSolver(rows, cols, mineCount, Arrays.copyOf(moves, moves.length + 1), deepCopy);

            try {
                deepCopy.makeFirstSelection(location);
            } catch (MinesweeperException e) {
                e.printStackTrace();
            }
            successors.add(succesor);
        
        }
        return successors;
    }

    @Override
    public boolean isValid() {
        return mineBoard.getGameState() != GameState.LOSS;
    }

    @Override
    public boolean isGoal() {
        return mineBoard.getGameState() == GameState.WIN;
    }

    @Override
    public String toString() {
        return mineBoard.toString() + " " + mineBoard.getGameState();
    }

    public Location[] getMoves() {
        return moves;
    }
    
}
