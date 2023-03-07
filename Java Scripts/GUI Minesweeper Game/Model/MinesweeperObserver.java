package Model;

public interface MinesweeperObserver {
    void cellUpdated(Location loacation, boolean isHint);
    
}
