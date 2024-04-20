import javax.swing.JFrame;
import java.awt.FlowLayout;


public class Screen extends JFrame{

    public Screen(){
        setTitle("TheGame");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setSize(400, 425);
        setResizable(true);
        setLocationRelativeTo(null);
        setVisible(true);
    }



    public void addButton(String nameOfThing, String typeOfButton, int x, int y){

        Thing a = new Thing(typeOfButton, x, y);
        add(a);

    }


    public void SetButton(Thing nameOfThing, int x, int y){

        //a.setLocation(x, y);

    }




}






