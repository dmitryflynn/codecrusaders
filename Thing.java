import java.awt.event.ActionListener;
import javax.swing.JButton;
import java.awt.event.*;

public class Thing extends JButton implements ActionListener{

    public String typeOfButton;
    public int x;
    public int y;


    public Thing(String typeOfButton, int x, int y){

        this.typeOfButton = typeOfButton;
        this.x = x;
        this.y = y;



        setText(typeOfButton);
        addActionListener( this ); 
        setBounds(x,y, 50,50);
    }




    @Override
    public void actionPerformed(ActionEvent e) {

    System.out.println("Hi!!!!");
    }


}