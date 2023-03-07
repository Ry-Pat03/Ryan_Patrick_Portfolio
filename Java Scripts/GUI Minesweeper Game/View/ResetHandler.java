package View;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.stage.Stage;

public class ResetHandler implements EventHandler<ActionEvent>{

    private Stage stage;

    //Constructor
    public ResetHandler(Stage stage){
        this.stage = stage;
    }

    //Behaviors
    @Override
    public void handle(ActionEvent arg0) {
        MinesweeperGUI game = new MinesweeperGUI();
        try {
            game.start(stage);
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
    }
    
}
