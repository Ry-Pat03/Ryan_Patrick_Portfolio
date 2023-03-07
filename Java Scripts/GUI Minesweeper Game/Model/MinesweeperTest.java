package Model;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.Test;
import org.junit.platform.commons.annotation.Testable;

@Testable
public class MinesweeperTest {
    @Test
    public void testDeepCopy(){
        Minesweeper minesweeper = new Minesweeper(4, 4, 2);
        Minesweeper deepCopy = new Minesweeper(minesweeper);

        assertTrue(minesweeper != deepCopy);
        for(int i = 0; i < 4; i++){
            for(int i2 = 0; i2 < 4; i2++){
               try {
                assertTrue(minesweeper.getSymbol(new Location(i, i2)) == deepCopy.getSymbol(new Location(i, i2)));
            } catch (MinesweeperException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            } 
            }
        }
    }
}
