package com.example.testing;


import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;


public class Testing_Mode {
        public static final boolean testing = true; // enable testing mode
        public static final boolean study_section = false;   //shows all modules in study section
        public static final boolean night_mode = true;      // if in test mode this helps you to activate and deactivate night mode else as per the implementation
        public static final boolean play_ground = false;  // if in test mode this helps you to activate and deactivate play ground else as per the implementation
    public static long timemillis = 0;
    public static void main(String args[]){
        String myDate = "2019/04/12 16:00:45";
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = null;
        try {
            date = sdf.parse(myDate);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        timemillis = date.getTime();
        System.out.println(timemillis);

    }
    }



