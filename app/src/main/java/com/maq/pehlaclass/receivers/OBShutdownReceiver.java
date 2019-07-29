package com.maq.pehlaclass.receivers;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

import com.maq.pehlaclass.utils.OBAnalytics;
import com.maq.pehlaclass.utils.OBAnalyticsManager;

/**
 * Created by pedroloureiro on 07/12/2017.
 */

public class OBShutdownReceiver extends BroadcastReceiver
{
    @Override
    public void onReceive (Context context, Intent intent)
    {
        OBAnalyticsManager.sharedManager.deviceTurnedOff();
    }
}
