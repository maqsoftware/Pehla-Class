package com.maq.pehlaclass.glstuff;

import android.content.Context;
import android.opengl.GLSurfaceView;
import android.view.View;

import com.maq.pehlaclass.mainui.MainActivity;
import com.maq.pehlaclass.mainui.OBViewController;
import com.maq.pehlaclass.utils.OBConfigManager;

/**
 * Created by alan on 02/05/16.
 */
public class OBGLView extends GLSurfaceView
{
    public OBViewController controller;

    public OBGLView(Context context)
    {
        super(context);
        this.addOnLayoutChangeListener(new OnLayoutChangeListener()
        {
            @Override
            public void onLayoutChange(View v, int left, int top, int right, int bottom, int
                    oldLeft, int oldTop, int oldRight, int oldBottom)
            {
                OBConfigManager.sharedManager.updateGraphicScale(right-left,bottom-top);
            }
        });
    }

    @Override
    protected void onLayout(boolean changed, int l, int t, int r, int b)
    {
        if (controller != null)
            controller.viewWasLaidOut(changed, l, t, r, b);
    }



}
