package com.maq.xprize.onecourse.hindi.utils;

import android.support.v7.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

// testing date for which testing scripts are made is "2019/04/12 16:00:45" set it using constructor
public class TestingMode extends AppCompatActivity {
    public static boolean testingActive = false; // enable testing mode and stop bubble's motion in playground
    public static boolean studySection = false;   //shows all modules in study section even if testing mode is disabled
    public static boolean nightMode = false;      // In testing mode, this helps you to activate and deactivate night mode permanently else as per the implementation
    public static boolean playZone = false;  // In testing mode, this helps you to activate and deactivate play ground permanently else as per the implementation
    public static long timeSec = 0;        // testing date can set using file assets/testing/testing.txt in application's data directory.

    public TestingMode() { //public constructor
        String filePath = OBConfigManager.sharedManager.getAssetsExternalPath() + File.separator + "testing" + File.separator + "testing.txt";
        String line = null;
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = null;
        String dateStr = "2019/04/12 16:00:45";
        int count = 0;
        try {

            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader =
                    new BufferedReader(fileReader);

            while ((line = bufferedReader.readLine()) != null) {
                switch (count) {
                    case 1:
                        dateStr = line;
                        break;
                    case 2:
                        if (line.equals("1")) {
                            testingActive = true;
                        }
                        break;
                    case 3:
                        if (line.equals("1")) {
                            studySection = true;
                        }
                        break;
                    case 4:
                        if (line.equals("1")) {
                            nightMode = true;
                        }
                        break;
                    case 5:
                        if (line.equals("1")) {
                            playZone = true;
                        }
                        break;
                    default:
                        break;
                }
                count++;
            }

            bufferedReader.close();
        } catch (FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" +
                            filePath + "'");
        } catch (IOException ex) {
            System.out.println(
                    "Error reading file '"
                            + filePath + "'");
        }

        try {
            date = dateFormat.parse(dateStr);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        timeSec = date.getTime() / 1000;
    }
}




