package View;

import java.util.Scanner;

import Model.GameState;
import Model.Location;
import Model.Minesweeper;
import Model.MinesweeperException;
import Model.MinesweeperSolver;
import backtracker.Backtracker;

public class MineSweeperCLI {

    private static void help(){
        System.out.println("Commands: \n help - this help message \n pick <row> <col> - uncovers cell a <row> <col> \n hint - displays a safe selection \n reset - resets to a new game \n solve - display the solution to the game \n quit - quits the game");
    }

    private static void solve(int row, int col, int mineCount){
        Backtracker backTracker = new Backtracker(false);

        MinesweeperSolver testMinesweeper = new MinesweeperSolver(row, col, mineCount);

        backtracker.Configuration solution = backTracker.solve(testMinesweeper);

        System.out.println(solution);
    }

    public static void main(String[] args){
        Minesweeper game;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your game as so: row col mineCount: ");
        String input = scanner.nextLine();
        String[] tokens = input.split(" ");
        game = new Minesweeper(Integer.parseInt(tokens[0]), Integer.parseInt(tokens[1]), Integer.parseInt(tokens[2]));
        System.out.println(game);

        while(true){
            input = scanner.nextLine();
            tokens = input.split(" ");
            
            if(tokens[0].equals("help")){
                help();
            }
            else if(tokens[0].equals("solve")){
                solve(game.getRows(), game.getCols(), game.getMineCount());;
            }
            else if(tokens[0].equals("quit")){
                break;
            }
            else if(tokens[0].equals("hint")){
                Object[] possibleList = game.getPossibleSelections().toArray();
                System.out.println(possibleList[0]);
            }
            else if(tokens[0].equals("reset")){
                System.out.println("Enter your game as so: row col mineCount: ");
                input = scanner.nextLine();
                tokens = input.split(" ");
                game = new Minesweeper(Integer.parseInt(tokens[0]), Integer.parseInt(tokens[1]), Integer.parseInt(tokens[2]));
                System.out.println(game);
            }
            else if(tokens[0].equals("pick") && !(game.getGameState() == GameState.LOSS)){
                try{
                    game.makeFirstSelection(new Location(Integer.parseInt(tokens[1]), Integer.parseInt(tokens[2])));
                    System.out.println("Move: " + game.getMoveCount());
                    System.out.println(game);
                }
                catch(MinesweeperException e){
                    System.out.println("Hey you dummy pick in bounds ( Love you :) )");
                    continue;
                }
            }
            else{
                help();
                continue;
            }
            

            //checking win or loss
            if(game.getGameState() == GameState.LOSS){
                System.out.println("You loss Sucker L + ratio (reset to play agian or quit to quit");
                
            }
            else if(game.getGameState() == GameState.WIN){
                System.out.println("Hey, you actually won something in your life!( But hey you won :) ) -Nathan Skomo");

            }


    
        }

        scanner.close();
    }
}
