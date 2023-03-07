package View;

import Model.Location;
import Model.Minesweeper;
import Model.MinesweeperException;
import Model.MinesweeperSolver;
import backtracker.Backtracker;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.stage.Stage;

public class SolveHandler implements EventHandler<ActionEvent>{

    private int row, col, minecount;
    private Minesweeper board;
    

    public SolveHandler(Minesweeper board, Stage stage){
        this.board = board;
        this.row = board.getRows();
        this.col = board.getCols();
        this.minecount = board.getMineCount();
    }

    @Override
    public void handle(ActionEvent arg0) {
        Backtracker backTracker = new Backtracker(false);
        MinesweeperSolver testMinesweeper = new MinesweeperSolver(row, col, minecount);
        MinesweeperSolver solution = (MinesweeperSolver) backTracker.solve(testMinesweeper);
        Location[] moves = solution.getMoves();
        for (int i = 0; i < moves.length - 1; i++){
            try {
                board.makeFirstSelection(moves[i]);
            } catch (MinesweeperException e) {
                System.out.print(moves[i].getRow() + ", " + moves[i].getCol());
                e.printStackTrace();
            }
        }
        
    }
    
}
