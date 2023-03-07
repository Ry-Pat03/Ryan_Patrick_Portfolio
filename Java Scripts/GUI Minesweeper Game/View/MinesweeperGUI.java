package View;


import Model.Minesweeper;
import Model.MinesweeperException;
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderStroke;
import javafx.scene.layout.BorderStrokeStyle;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class MinesweeperGUI extends Application {
    //Set up images
    public static final Image MINE = new Image("file:media/images/mine24.png");
    public static final Image FLAG = new Image("file:media/images/flag24.png");

    private static final int ROWS = 10;
    private static final int COLS = 10;
    private static final int MINES = 10;
    private Button[][] buttons = new Button[ROWS][COLS];


    private Minesweeper board;

    @Override
    public void start(Stage stage) throws Exception {

        this.board = new Minesweeper(ROWS, COLS, MINES);
        

        VBox vbox = new VBox();

        Button makeHB = makeHintButton();
        Button makeReset = makeResetButton(stage);
        Button solve = makeSolveButton(stage);

        Label mineCount = new Label("Mines: " + board.getMineCount());
        Label moveCount = new Label("Moves: " + board.getMoveCount());
        Label gameSatus = new Label(board.getGameState().toString());

        GridPane gridPane = makeGridPane(gameSatus);
        mineCount.setBackground((new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY))));
        mineCount.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        mineCount.setPrefSize(158, 72);
        moveCount.setBackground((new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY))));
        moveCount.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        moveCount.setPrefSize(158, 72);
        gameSatus.setBackground((new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY))));
        gameSatus.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        gameSatus.setPrefSize(158, 72);

        vbox.getChildren().addAll(makeHB, makeReset, solve, mineCount, moveCount, gameSatus);      

        HBox box = new HBox();

        box.getChildren().addAll(vbox, gridPane);
        board.register((location, isHint) -> {
            Button button = buttons[location.getRow()][location.getCol()];
            try{
                if(isHint){
                    button.setBackground((new Background(new BackgroundFill(Color.GREEN, CornerRadii.EMPTY, Insets.EMPTY))));
                }
                else{
                    moveCount.setText("Moves: " + board.getMoveCount());
                    gameSatus.setText(board.getGameState().toString());
                    char sym = board.getSymbol(location);
                    button.setBackground(new Background(new BackgroundFill(Color.BLUE, CornerRadii.EMPTY, Insets.EMPTY)));
                    if( sym == 'M'){
                        ImageView imageView = new ImageView(MINE);
                        button.setGraphic(imageView);
                    }
                    else if(sym != '0'){
                        button.setText(Character.toString(sym));
                        button.setFont(new Font("Comic Sans", 24));
                    }
                }
                
            }catch (MinesweeperException e){
                System.out.println(e);
            }

        });
        stage.setScene(new Scene(box));
        stage.setTitle("Minesweeper");
        stage.show();
        
    }



    private GridPane makeGridPane(Label gameStatus){
        GridPane gridpane = new GridPane();
        for(int col = 0; col< COLS; col++){
            for(int row = 0; row < ROWS; row++){
                Button button = makeButton(row, col, gameStatus);
                gridpane.add(button, col, row);
            }
        }

        return gridpane;
    }

    private Button makeButton(int row, int col, Label gameStatus){

        Button button = new Button("");
        button.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY)));
        button.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        button.setPrefSize(72, 72);
        button.setPadding(Insets.EMPTY);
        buttons[row][col] = button;

        button.setOnAction(new MoveHandler(board, row, col, gameStatus));
        

        return button;
    }

    private Button makeHintButton(){
        Button button = new Button("HINT");
        
        button.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY)));
        button.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        button.setPrefSize(158, 72);
        button.setPadding(Insets.EMPTY);

        button.setOnAction(new HintHandler(board));

        return button;
    }

    private Button makeResetButton(Stage stage){
        Button button = new Button("RESET");
        button.setOnAction(new ResetHandler(stage));
        button.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY)));
        button.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        button.setPrefSize(158, 72);
        button.setPadding(Insets.EMPTY);

        return button;
    }

    private Button makeSolveButton(Stage stage){
        Button button = new Button("SOLVE");
        button.setOnAction(new SolveHandler(board, stage));
        button.setBackground(new Background(new BackgroundFill(Color.GREY, CornerRadii.EMPTY, Insets.EMPTY)));
        button.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY, BorderStroke.THICK, Insets.EMPTY)));
        button.setPrefSize(158, 72);
        button.setPadding(Insets.EMPTY);

        return button;
    }

    public static void main(String[] args) {
        launch(args);
    }
    
}
