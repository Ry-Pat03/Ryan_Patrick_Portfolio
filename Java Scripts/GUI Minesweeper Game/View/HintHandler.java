package View;


import Model.Minesweeper;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class HintHandler implements EventHandler<ActionEvent>{
    private Minesweeper board;
    public HintHandler(Minesweeper board){
        this.board = board;
    }
    @Override
    public void handle(ActionEvent event) {
        board.getHint(board.getPossibleSelections());
    }
    
}
