package com.maq.pehlaclass.mainui.oc_typing;

import com.maq.pehlaclass.controls.OBGroup;

/**
 * Created by michal on 12/06/2018.
 */

public interface OC_TypewriterReceiver
{
    void touchDownKey(OBGroup key, boolean sound);
    void touchUpKey(OBGroup key);
}
