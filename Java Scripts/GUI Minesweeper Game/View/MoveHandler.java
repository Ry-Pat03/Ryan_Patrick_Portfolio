
package View;

import Model.GameState;
import Model.Location;
import Model.Minesweeper;
import Model.MinesweeperException;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Label;


public class MoveHandler implements EventHandler<ActionEvent>{

    private Minesweeper board;
    private int row, col;
    private Label gameSatus;

    public MoveHandler(Minesweeper board, int row, int col, Label gameSatus){
        this.board = board;
        this.row = row;
        this.col = col;
        this.gameSatus = gameSatus;
    }

    @Override
    public void handle(ActionEvent arg0) {
        //Update Backend
        if(board.getGameState() != GameState.WIN && board.getGameState() != GameState.LOSS){
          try{
            board.makeFirstSelection(new Location(row, col));
            gameSatus.setText(board.getGameState().toString());
        }
        catch(MinesweeperException e){
            System.out.println(e);
        }  
        }
        
       
    }

}
