package Model;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;
import org.junit.platform.commons.annotation.Testable;

@Testable  
public class TestLocation {
    @Test
    public void testGetRow(){
        
        Location location = new Location(2, 2);

        assertEquals(2, location.getRow());

    }

    @Test
    public void testGetCol(){
        
        Location location = new Location(2, 2);

        assertEquals(2, location.getCol());

    }

    @Test
    public void testHash(){
        Location location = new Location(1, 1);

        Location location2 = new Location(1, 1);

        assertEquals(location, location2);
    }

    @Test
    public void testEquals(){

        Location location = new Location(1, 1);

        Location location2 = new Location(1, 1);

        assertEquals(location.hashCode(), location2.hashCode());

    }

}
