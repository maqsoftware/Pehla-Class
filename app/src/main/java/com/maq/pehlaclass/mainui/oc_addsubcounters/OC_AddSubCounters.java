package com.maq.pehlaclass.mainui.oc_addsubcounters;

import android.graphics.Color;
import android.graphics.PointF;

import com.maq.pehlaclass.controls.OBLabel;
import com.maq.pehlaclass.mainui.OC_SectionController;
import com.maq.pehlaclass.utils.OBUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class OC_AddSubCounters extends OC_SectionController
{
    boolean equAudio;
    public class ocasc_equation
    {
        boolean isPlus;
        int lh, rh;
    }
    static boolean isovernum(ocasc_equation eq,int num)
    {
        if(eq.lh > num || eq.rh > num)
            return true;
        if(eq.isPlus)
            return eq.lh + eq.rh > num;
        else
            return eq.lh - eq.rh > num;
    }

    public void miscSetUp()
    {
        equAudio = OBUtils.coalesce(parameters.get("equaudio") , "true").equals("true");
    }
    public void prepare()
    {
        super.prepare();
        loadFingers();
        miscSetUp();
        doVisual(currentEvent());
    }

    public void start()
    {
        setStatus(0);
        OBUtils.runOnOtherThread(new OBUtils.RunLambda()
        {
            public void run() throws Exception
            {
                try
                {
                    if(!performSel("demo",currentEvent()))
                    {
                        doBody(currentEvent());
                    }
                }
                catch(Exception exception)
                {
                }
            }
        });
    }

    public void readEquation(OBLabel equLabel, ocasc_equation eq, int col) throws Exception
    {
        equLabel.setColour(col);
        waitForSecs(0.2f);
        if(equAudio)
        {
            List audarray = new ArrayList<>();
            String op = eq.isPlus?"add":"sub";
            audarray.add(String.format(Locale.US,"addsub_st%d",eq.lh));
            audarray.add(String.format(Locale.US,"addsub_%s%d",op,eq.rh));
            audarray.add(String.format(Locale.US,"addsub_ans%d",eq.lh +(eq.isPlus?1:-1) * eq.rh));
            playAudioQueued(audarray,true);
        }
        waitForSecs(0.2f);
        equLabel.setColour(Color.BLACK);
    }


    public Object findTarget(PointF pt)
    {
        return(finger(-1,3,targets,pt));
    }


}
