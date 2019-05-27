package com.maq.xprize.onecourse.controls;

/**
 * Created by alan on 16/03/2017.
 */

import android.graphics.Canvas;
import android.opengl.GLES20;
import android.os.Handler;
import android.os.SystemClock;

import com.maq.xprize.onecourse.glstuff.ColorShaderProgram;
import com.maq.xprize.onecourse.glstuff.GradientRect;
import com.maq.xprize.onecourse.glstuff.MaskShaderProgram;
import com.maq.xprize.onecourse.glstuff.OBRenderer;
import com.maq.xprize.onecourse.glstuff.PixelRect;
import com.maq.xprize.onecourse.glstuff.PixelShaderProgram;
import com.maq.xprize.onecourse.glstuff.ShadowShaderProgram;
import com.maq.xprize.onecourse.glstuff.TextureShaderProgram;
import com.maq.xprize.onecourse.mainui.OBSectionController;
import com.maq.xprize.onecourse.mainui.OBViewController;
import com.maq.xprize.onecourse.utils.OBUtils;

public class OBShaderControl extends OBControl
{
    public PixelShaderProgram shaderProgram;
    public PixelRect pixelRect;
    long starttm = SystemClock.uptimeMillis();

    private boolean animate = false;
    private Runnable animationRunnable;
    private Handler animationHandler;

    public void render (OBRenderer renderer, OBViewController vc, float[] modelViewMatrix)
    {
        if (!hidden && bounds().width() > 0 && bounds().height() > 0 && shaderProgram != null)
        {
            matrix3dForDraw();
            if (doubleSided)
            {
                GLES20.glDisable(GLES20.GL_CULL_FACE);
            }
            else
            {
                GLES20.glEnable(GLES20.GL_CULL_FACE);
            }
            //
            android.opengl.Matrix.multiplyMM(tempMatrix, 0, modelViewMatrix, 0, modelMatrix, 0);
            //
            shaderProgram.useProgram();
            long tm = SystemClock.uptimeMillis();
            float secs = ((tm - starttm) / 1000f);
            if (dynamicMask && maskControl != null)
            {
                float[] maskFrame = new float[4];
                maskFrame[0] = maskControl.getWorldFrame().left+vc.viewPortLeft;
                maskFrame[1] = maskControl.getWorldFrame().top+vc.viewPortTop;
                maskFrame[2] = maskControl.getWorldFrame().right+vc.viewPortLeft;
                maskFrame[3] = maskControl.getWorldFrame().bottom+vc.viewPortTop;
                shaderProgram.setUniforms(tempMatrix,secs,renderer.textureObjectId(1),maskControlReversed ? 1.0f : 0.0f,renderer.h, maskFrame);
            }
            else
                shaderProgram.setUniforms(tempMatrix,secs);
            if (pixelRect == null)
                pixelRect = new PixelRect(shaderProgram);
            pixelRect.draw(renderer, 0, 0, bounds.right - bounds.left, bounds.bottom - bounds.top, maskControl.texture.bitmap());

        }
    }

    private boolean shouldAnimate(OBSectionController cont)
    {
        return animate && (cont != null && !cont._aborting && cont.status() != OBSectionController.STATUS_EXITING);
    }

    public void startAnimation(final OBSectionController cont)
    {
        OBUtils.runOnMainThread(new OBUtils.RunLambda()
        {
            @Override
            public void run() throws Exception
            {
                if(animationHandler == null)
                    animationHandler = new Handler();
                animate = true;
                scheduleTimerEvent(cont);
            }
        });

    }

    public void stopAnimation()
    {
        animate = false;
        animationHandler.removeCallbacks(animationRunnable);
    }

    private void timerEvent(OBSectionController cont)
    {
        if (shouldAnimate(cont))
        {
            this.invalidate();
            scheduleTimerEvent(cont);
        }
    }


    private void scheduleTimerEvent(final OBSectionController cont)
    {
        if (!shouldAnimate(cont))
            return;
        if (animationRunnable == null)
        {
            animationRunnable = new Runnable()
            {
                @Override
                public void run()
                {
                    timerEvent(cont);
                }
            };
        }
        animationHandler.removeCallbacks(animationRunnable);
        animationHandler.postDelayed(animationRunnable,100);
    }

    public void draw (Canvas canvas, int flags)
    {

    }
}