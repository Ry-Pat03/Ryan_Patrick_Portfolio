package Model;

import backtracker.Backtracker;
import backtracker.Configuration;

public class MineSweeperBacktrackerTest {
   
    public static void main(String[] args) {
      Backtracker backTracker = new Backtracker(false);

        MinesweeperSolver testMinesweeper = new MinesweeperSolver(9, 9, 10);

        Configuration Solution = backTracker.solve(testMinesweeper);

        System.out.println(Solution);
   
    }
}
