package com.example.testing;


import android.support.v7.app.AppCompatActivity;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

// testing date for which testing scripts are made is "2019/04/12 16:00:45" set it using constructor
public class testingMode extends AppCompatActivity {
    public static final boolean testingActive = true; // enable testing mode and stops bubble in playground
    public static final boolean studySection = false;   //shows all modules in study section even if test mode is disabled
    public static final boolean nightMode = false;      // if in test mode, this helps you to activate and deactivate night mode permanently else as per the implementation
    public static final boolean playZone = true;  // if in test mode this helps you to activate and deactivate play ground permanently else as per the implementation
    public static long timeSec = 0;        // testing date can set using the constructor below

    public testingMode() { //public constructor
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = null;
        String dateStr = "2019/04/12 16:00:45";

//        File file = new File("D:\\kitkit\\GLEXP-Team-onebillion-Hindi\\testing\\src\\main\\assets\\data.txt");
//        if (file != null) {
//            BufferedReader br = null;
//            try {
//                br = new BufferedReader(new FileReader(file));
//            } catch (FileNotFoundException e1) {
//                dateStr = "2019/04/12 16:00:45";
//            }
//
//
//            try {
//                assert br != null;
//                dateStr = br.readLine();
//            } catch (IOException e) {
//                dateStr = "2019/04/12 16:00:45";
//            }
//            System.out.println(dateStr);
//        }
        try {
            date = dateFormat.parse(dateStr);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        timeSec = date.getTime() / 1000;


    }
}




