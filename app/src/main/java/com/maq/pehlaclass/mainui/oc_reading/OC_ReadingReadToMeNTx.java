package com.maq.pehlaclass.mainui.oc_reading;

import android.graphics.Bitmap;
import android.graphics.Color;
import android.graphics.Path;
import android.graphics.PathMeasure;
import android.graphics.PointF;
import android.graphics.RectF;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;

import com.maq.pehlaclass.controls.OBControl;
import com.maq.pehlaclass.controls.OBEmitter;
import com.maq.pehlaclass.controls.OBEmitterCell;
import com.maq.pehlaclass.controls.OBGroup;
import com.maq.pehlaclass.controls.OBPath;
import com.maq.pehlaclass.controls.OBPresenter;
import com.maq.pehlaclass.mainui.MainActivity;
import com.maq.pehlaclass.utils.OBAnim;
import com.maq.pehlaclass.utils.OBAnimBlock;
import com.maq.pehlaclass.utils.OBAnimationGroup;
import com.maq.pehlaclass.utils.OBReadingPara;
import com.maq.pehlaclass.utils.OBReadingWord;
import com.maq.pehlaclass.utils.OBUtils;
import com.maq.pehlaclass.utils.OB_Maths;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import static com.maq.pehlaclass.utils.OBUtils.coalesce;

/**
 * Created by alan on 07/06/16.
 */
public class OC_ReadingReadToMeNTx extends OC_ReadingReadToMe
{
    OBPresenter presenter;
    int cqType;
    boolean questionsAsked;
    String pageName;
    OBEmitter starEmitter;
    OBPath shape;

    public void start()
    {
        setStatus(0);
        new AsyncTask<Void, Void,Void>()
        {
            protected Void doInBackground(Void... params) {
                try
                {
                    if (pageNo == 0)
                    {
                        setStatus(STATUS_DOING_DEMO);
                        demoa();
                        waitForSecs(0.7);
                        readTitle();
                        waitForSecs(0.5);
                        waitForSecs(0.3f);
                        showNextArrowAndRA(true);
                        if (doArrowDemo)
                            democ();
                        setStatus(STATUS_AWAITING_CLICK);
                    }
                    else
                    {
                        waitForSecs(0.5);
                        currPara = 0;
                        readPage();
                    }
                }
                catch (Exception exception)
                {
                }
                return null;
            }}.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, (Void[]) null);
    }

    public void loadTemplate()
    {
        eventsDict = loadXML(getConfigPath("booktemplate.xml"));
        if (pageNo == 0)
        {
            loadEvent("title");
            String s;
            if ((s = eventAttributes.get("largefontsize"))!=null)
                fontSize = applyGraphicScale(Float.parseFloat(s));
            if ((s = eventAttributes.get("largelineheight"))!=null)
                lineHeightMultiplier = Float.parseFloat(s);
            if ((s = eventAttributes.get("largespacing"))!=null)
                letterSpacing = Float.parseFloat(s);
            textJustification = TEXT_JUSTIFY_CENTRE;
        }
        else
        {
            if (picJustify == PIC_JUSTIFY_RIGHT|| picJustify == PIC_JUSTIFY_LEFT)
                loadEvent("piconlyport");
            else
                loadEvent("piconly");
        }
    }

    public float layOutText()
    {
        if (pageNo == 0)
            return super.layOutText();
        return 0;
    }

    public void readParagraph(int pidx,long token,boolean canInterrupt) throws Exception
    {
        List<Object> l = (List<Object>)(Object)Collections.singletonList(String.format(Locale.US,"p%d_%d",pageNo,pidx+1,true));
        playAudioQueued(l,true);
    }

    public void readTitle() throws Exception
    {
        OBReadingPara para = paragraphs.get(0);
        Exception ex = null;
        long token = -1;
        try
        {
            token = takeSequenceLockInterrupt(true);
            if (token == sequenceToken)
            {
                lockScreen();
                for (OBReadingWord w : para.words)
                {
                    if (w.label != null)
                        highlightWord(w,true,false);
                }
                textBox.setNeedsRetexture();
                unlockScreen();
                readParagraph(0,0,false);
            }

        }
        catch (Exception e)
        {
            ex = e;
        }
        lockScreen();
        for (OBReadingWord w : para.words)
        {
            if (w.label != null)
                highlightWord(w,false,false);
        }
        textBox.setNeedsRetexture();
        unlockScreen();
        sequenceLock.unlock();
        if (ex != null)
            throw ex;
    }

    public boolean showNextButton()
    {
        return false;
    }

    public void replayAudio()
    {
        if (_aborting || MainViewController().navigating || status() == STATUS_FINISHING)
            return;
        if (pageNo == 0)
        {
            setStatus(status());
            new AsyncTask<Void, Void, Void>()
            {
                protected Void doInBackground(Void... params)
                {
                    try
                    {
                        readTitle();
                    }
                    catch(Exception e)
                    {

                    }
                    return null;
                }
            }.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, (Void[]) null);
        }
        else
            super.replayAudio();
    }

    public void demoa() throws Exception
    {
        lockScreen();
        loadEvent("anna");
        presenter = OBPresenter.characterWithGroup((OBGroup)objectDict.get("presenter"));
        presenter.control.setZPosition(200);
        presenter.control.setProperty("restpos",new PointF(presenter.control.position().x,presenter.control.position().y));
        presenter.control.setRight(0);
        presenter.control.show();
        unlockScreen();

        presenter.walk((PointF) presenter.control.propertyValue("restpos"));
        presenter.faceFront();
        waitForSecs(0.2f);
        boolean usecq = OBUtils.coalesce(parameters.get("cq"),"false").equals("true");

        Map<String,List> eventd = (Map<String, List>) audioScenes.get("a");

        List<Object> aud = eventd.get("DEMO");
        int idx = usecq?1:0;
        presenter.speak(Arrays.asList(aud.get(idx)),this);
        waitForSecs(0.4f);
        PointF currPos = presenter.control.position();
        PointF destpos = new PointF(-presenter.control.width()/2, currPos.y);
        presenter.walk(destpos);
    }

    public void democ() throws Exception
    {
        PointF destPoint = OB_Maths.locationForRect(-0.1f, 0.3f, MainActivity.mainViewController.bottomRightButton.frame());
        loadPointerStartPoint(OB_Maths.locationForRect(0.5f, 1.1f,new RectF(bounds())),destPoint);
        movePointerToPoint(destPoint,-1,true);
        playAudioQueuedScene("c","DEMO",true);
        waitForSecs(0.5f);
        thePointer.hide();
    }


    void faceForward()
    {
        lockScreen();
        presenter.control.objectDict.get("faceside").hide();
        presenter.control.objectDict.get("faceforward").show();
        unlockScreen();
    }

    public void showQuestionElements() throws Exception
    {
        if (!objectDict.get("cameo").hidden)
            return;
        playSfxAudio("anna_on",false);
        lockScreen();
        showControls("cameo");
        unlockScreen();
    }

    public void hideQuestionElements() throws Exception
    {
        playSfxAudio("anna_off",false);
        lockScreen();
        hideControls("cameo");
        if (cqType == 2)
        {
            hideControls("answer.*");
        }
        unlockScreen();
    }

    public void workOutQuestionType(Map<String,Object> eventAudio)
    {
        if (eventAudio.get("ANSWER") != null)
            cqType = 2;
        else if (eventAudio.get("CORRECT") != null)
            cqType = 1;
        else
            cqType = 3;
    }

    public boolean correctFirst()
    {
        Map<String,List<String>> asp = (Map<String, List<String>>) audioScenes.get(pageName);
        List<String> keys = asp.get("__keys");
        for (String key : keys)
        {
            if (key.equals("CORRECT"))
                return true;
            else if (key.equals("INCORRECT"))
                return false;
        }
        return true;
    }

    public void loadCQAudioXMLs()
    {
        String path = getConfigPath("cqaudio.xml");
        loadAudioXML(path);
        Map<String,Object> d = audioScenes;
        if (pageNo == maxPageNo)
        {
            if (d.get("final") != null)
                d.put(pageName,d.get("final"));
        }
        path = getConfigPath("cqsfx.xml");
        loadAudioXML(path);
        audioScenes.putAll(d);
    }

    public String pageName()
    {
        return String.format(Locale.US,"p%d",pageNo);
    }

    public boolean considerComprehensionQuestions() throws Exception
    {
        String usecq = parameters.get("cq");
        if (usecq == null || !usecq.equals("true"))
            return false;
        if (questionsAsked)
            return false;
        loadCQAudioXMLs();
        pageName = pageName();
        if (audioScenes.get(pageName) != null)
        {
            workOutQuestionType((Map<String, Object>) audioScenes.get(pageName));
            loadCQPage();
            questionsAsked = true;
            if (cqType == 1)
            {
                targets = Arrays.asList(objectDict.get("shape"));
                demoCqType1a();
            }
            else if (cqType == 2)
            {
                OBControl a1 = objectDict.get("answer1");
                OBControl a2 = objectDict.get("answer2");
                if (correctFirst())
                    targets = Arrays.asList(a1,a2);
                else
                    targets = Arrays.asList(a2,a1);
                a1.setProperty("nm","answer1");
                a2.setProperty("nm","answer2");
                demoCqType2a();
            }
            else if (cqType == 3)
            {
                targets = Collections.emptyList();
                demoCqType3a();
            }
            return true;
        }
        return false;
    }

    public void demoCqType2a() throws Exception
    {
        setStatus(STATUS_DOING_DEMO);
        waitForSecs(0.4f);
        showQuestionElements();
        waitForSecs(0.4f);
        demoCqType2b(true);
    }

    public void demoCqType2b(boolean firstTime)
    {
        long token = -1;
        try
        {
            token = takeSequenceLockInterrupt(true);
            if (token == sequenceToken)
            {
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("PROMPT");
                //audl = OBUtils.insertAudioInterval(audl,300);
                presenter.speakWithToken(audl,token,this);
                waitForSecs(0.4f);
                OBPath answer1 = (OBPath) objectDict.get("answer1");
                answer1.show();
                deployFlashAnim(answer1);
                audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("ANSWER");
                presenter.speakWithToken(audl,token,this);
                checkSequenceToken(token);
                waitForSecs(0.2f);
                killAnimations();
                setStatus(STATUS_WAITING_FOR_ANSWER);
                checkSequenceToken(token);
                waitForSecs(0.4f);
                OBPath answer2 = (OBPath) objectDict.get("answer2");
                answer2.show();
                deployFlashAnim(answer2);
                audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("ANSWER2");
                presenter.speakWithToken(audl,token,this);
                checkSequenceToken(token);
                waitForSecs(0.2f);
                checkSequenceToken(token);
                killAnimations();
                waitForSecs(0.3f);
                checkSequenceToken(token);
                audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("PROMPT2");
                presenter.speakWithToken(audl,token,this);
                checkSequenceToken(token);
                waitForSecs(0.3f);
                checkSequenceToken(token);
                if (firstTime)
                    reprompt(statusTime, null, 5, new OBUtils.RunLambda() {
                        @Override
                        public void run() throws Exception
                        {
                            demoCqType2b(true);
                        }
                    });
            }
        }
        catch (Exception exception)
        {
        }
        killAnimations();
        sequenceLock.unlock();
    }

    public void demoCqType3a() throws Exception {
        setStatus(STATUS_DOING_DEMO);
        waitForSecs(0.4f);
        showQuestionElements();
        waitForSecs(0.4f);
        demoCqType3b(true);
    }

    public void demoCqType3b(boolean firstTime)
    {
        long token = -1;
        try
        {
            token = takeSequenceLockInterrupt(true);
            if (token == sequenceToken)
            {
                checkSequenceToken(token);
                for (int i = 1;i < 10;i++)
                {
                    String nm = StrAndNo("PROMPT", i);
                    List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get(nm);

                    if (audl == null)
                        break;

                    presenter.speakWithToken(audl,token,this);
                    checkSequenceToken(token);
                    waitForSecs(1.2f);
                }
            }
        }
        catch (Exception exception)
        {
        }
        killAnimations();
        sequenceLock.unlock();
        try
        {
            finishQuestion();
        }
        catch (Exception e)
        {

        }
    }

    public void finishQuestion() throws Exception {
        waitForSecs(0.6f);
        if (cqType == 1)
        {
        }
        hideQuestionElements();
        waitForSecs(0.8f);
        setStatus(STATUS_IDLE);
        bringUpNextButton();
    }

    public void readingFinished()
    {
        try
        {
            waitForSecs(0.8f);
            if(status()  != STATUS_FINISHING && !_aborting)
            {
                if (!considerComprehensionQuestions())
                    bringUpNextButton();
            }
        }
        catch(Exception exception)
        {
        }
    }

    public void deployFlashAnim(final OBPath c)
    {
        OBAnim blockAnim = new OBAnimBlock()
        {
            @Override
            public void runAnimBlock(float frac)
            {
                if (frac < 0.5)
                {
                    setAnswerButtonSelected(c);
                }
                else
                {
                    setAnswerButtonInActive(c);
                }
            }
        };
        OBAnimationGroup ag = new OBAnimationGroup();
        registerAnimationGroup(ag,"flash");
        ag.applyAnimations(Collections.singletonList(blockAnim), 0.25f, false, OBAnim.ANIM_LINEAR, -1, new OBUtils.RunLambda() {
            @Override
            public void run() throws Exception {
                setAnswerButtonActive(c);
            }
        }, this);
    }
    void setAnswerButtonActive(OBPath c)
    {
        if ("act".equals(coalesce(c.propertyValue("st"),"--")))
            return;
        lockScreen();
        c.setFillColor((Integer)c.propertyValue("fillcolour"));
        c.setStrokeColor((Integer)c.propertyValue("strokecolour"));
        c.lowlight();
        unlockScreen();
        c.setProperty("st","act");
    }

    void setAnswerButtonInActive(OBPath c)
    {
        if ("inact".equals(coalesce(c.propertyValue("st"),"--")))
            return;
        lockScreen();
        c.lowlight();
        c.setFillColor((Integer)c.propertyValue("desatfillcolour"));
        c.setStrokeColor((Integer)c.propertyValue("desatstrokecolour"));
        unlockScreen();
        c.setProperty("st","inact");
    }

    void setAnswerButtonSelected(OBPath c)
    {
        if ("sel".equals(coalesce(c.propertyValue("st"),"--")))
            return;
        lockScreen();
        c.setFillColor((Integer)c.propertyValue("selcolour"));
        c.setStrokeColor((Integer)c.propertyValue("strokecolour"));
        //c.highlight();
        unlockScreen();
        c.setProperty("st","sel");
    }

    public void loadCQPage()
    {
        Map<String, Object> evd = loadXML(getConfigPath("cq.xml"));
        eventsDict.putAll(evd);
        evd = loadXML(getConfigPath("eventcq.xml"));
        eventsDict.putAll(evd);
        lockScreen();
        doVisual("cqmain");
        presenter = OBPresenter.characterWithGroup((OBGroup)objectDict.get("annahead"));
        OBGroup cameo = (OBGroup) objectDict.get("cameo");
        cameo.setShouldTexturise(false);
        //anna = (OBGroup) objectDict.get("annahead");
        OBPath circleStroke = (OBPath) cameo.objectDict.get("circlestroke");
        circleStroke.sizeToBoundingBoxIncludingStroke();
        faceForward();
        if (cqType == 1 || cqType == 3)
        {
            loadEvent(pageName());
            shape = (OBPath) objectDict.get("shape");
            detachControl(shape);

        }
        else if (cqType == 2)
        {
            for (OBControl p : filterControls("answer.*"))
            {
                OBPath c = (OBPath) p;
                float l = c.lineWidth();
                ((OBPath) p).outdent(l);
                int col = c.fillColor();
                int selcol = Color.argb(255,Color.red(col)/2,Color.green(col)/2,Color.blue(col)/2);
                c.setProperty("fillcolour", col);
                c.setProperty("selcolour", selcol);
                c.setProperty("desatfillcolour", OBUtils.DesaturatedColour(col, 0.2f));
                col = c.strokeColor();
                c.setProperty("strokecolour", col);
                c.setProperty("desatstrokecolour", OBUtils.DesaturatedColour(col, 0.2f));
                setAnswerButtonInActive(c);
            }
        }
        else
        {

        }
        hideControls("answer.*");
        hideControls("cameo");
        unlockScreen();
    }

    public void demoCqType1a() throws Exception
    {
        setStatus(STATUS_DOING_DEMO);
        waitForSecs(0.4f);
        showQuestionElements();
        waitForSecs(0.4f);
        demoCqType1b(true);
    }

    public void demoCqType1b(boolean firstTime)
    {
        long token = -1;
        try
        {
            token = takeSequenceLockInterrupt(true);
            if (token == sequenceToken)
            {
                waitForSecs(0.4f);
                showQuestionElements();
                waitForSecs(0.4f);
                checkSequenceToken(token);
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("PROMPT");
                presenter.speakWithToken(audl,token,this);
                checkSequenceToken(token);
                setStatus(STATUS_WAITING_FOR_ANSWER);
                waitForSecs(0.4f);
                checkSequenceToken(token);
                if (firstTime)
                    reprompt(statusTime, null, 5, new OBUtils.RunLambda() {
                        @Override
                        public void run() throws Exception {
                            demoCqType1b(true);
                        }
                    });
            }
        }
        catch (Exception exception)
        {
        }
        sequenceLock.unlock();
    }

    public OBEmitterCell starEmitterCell(int i, Bitmap im, float rs,float gs,float bs)
    {
        OBEmitterCell ec = new OBEmitterCell();
        ec.birthRate = 10;
        ec.lifeTime = 2;
        ec.lifeTimeRange = 0.5f;
        ec.red = 1.0f;
        ec.green = 216.0f/255.0f;
        ec.blue = 0.0f;
        ec.contents = im;
        ec.name = String.format(Locale.US,"star%d",i);
        ec.velocity = 0;
        ec.velocityRange = 2;
        ec.emissionRange = (float)(Math.PI * 2.0);
        ec.blueSpeed = bs;
        ec.greenSpeed = gs;
        ec.redSpeed = rs;
        ec.alphaSpeed = -0.2f;
        ec.spin = 0.0f;
        ec.spinRange = 3.0f;
        ec.scale = 1.0f ;
        ec.scaleRange = -(ec.scale / 2.0f);
        ec.scaleSpeed = ec.scaleRange / 2.0f;
        return ec;
    }

    public void stopEmissions() throws Exception {
        OBEmitterCell cell = starEmitter.cells.get(0);

        cell.birthRate = 3;
        cell.alphaSpeed = 0;
        cell.spinRange = 0;
        cell.scaleSpeed = 0;
        cell.scaleRange = 0;
        cell.lifeTime = 10;
        waitForSecs(2);
        cell.birthRate = 0;
        waitForSecs(2f);
    }

    public void doEmitter()
    {
        OBPath smallStar = StarWithScale(applyGraphicScale(8), false);
        smallStar.setFillColor(Color.WHITE);
        smallStar.setStrokeColor(Color.argb((int)(0.7*255),(int)(0.3*255),(int)(0.3*255),(int)(0.3*255)));
        smallStar.enCache();
        //OBPath shape = (OBPath) objectDict.get("shape");
        //attachControl(shape);
        //shape.setZPosition(200);
        //shape.show();
        PointF firstpt = shape.sAlongPath(0,null);
        firstpt = convertPointFromControl(firstpt,shape);

        starEmitter = new OBEmitter();
        starEmitter.setBounds(0,0,64,64);
        starEmitter.setPosition(firstpt);
        OBEmitterCell cell = starEmitterCell(0, smallStar.cache, 0, 0, 0);
        cell.position = OB_Maths.locationForRect(0.5f,0.5f,starEmitter.bounds());
        starEmitter.cells.add(cell);

        starEmitter.setZPosition(100);
        objectDict.put("starEmitter", starEmitter);
        attachControl(starEmitter);
        starEmitter.run();
        OBUtils.runOnOtherThreadDelayed(2, new OBUtils.RunLambda() {
            @Override
            public void run() throws Exception {
                stopEmissions();
            }
        });
    }

    List<Path> pathsFromComplexPath(Path p)
    {
        List<Path>pathList = new ArrayList<>();
        PathMeasure pm = new PathMeasure(p,false);
        Boolean fin = false;
        while (!fin)
        {
            float len = pm.getLength();
            if (len > 0)
            {
                Path np = new Path();
                pm.getSegment(0,len,np,true);
                pathList.add(np);
            }
            fin = !pm.nextContour();
        }
        return pathList;
    }
    public void moveEmitter()
    {
        OBControl starEmitter = objectDict.get("starEmitter");
        Path p = convertPathFromControl(shape.path(),shape);
        List<List<OBAnim>>anims = new ArrayList<>();
        for (Path sp : pathsFromComplexPath(p))
        {
            OBAnim anim = OBAnim.pathMoveAnim(starEmitter, sp, false, 0);
            anims.add(Collections.singletonList(anim));
        }
        OBAnimationGroup agp = new OBAnimationGroup();
        //agp.applyAnimations(Collections.singletonList(anim),2,false,OBAnim.ANIM_LINEAR,2,null,this);
        agp.chainAnimations(anims,Collections.singletonList(2f/anims.size()),false,Collections.singletonList(OBAnim.ANIM_LINEAR),2,this);
    }

    public void checkAnswer1(OBControl targ,PointF pt)
    {
        setStatus(STATUS_CHECKING);
        try
        {
            if (targ != null)
            {
                gotItRightBigTick(false);
                waitSFX();
                if (cqType == 1)
                {
                    doEmitter();
                    moveEmitter();
                    playSfxAudio("shimmer",false);
                    waitForSecs(0.5f);
                    waitSFX();
                }
                waitForSecs(0.5f);
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("CORRECT");
                presenter.speak(audl,this);
                finishQuestion();
            }
            else
            {
                gotItWrongWithSfx();
                waitSFX();
                waitForSecs(0.1f);
                setStatus(STATUS_WAITING_FOR_ANSWER);
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("INCORRECT");
                presenter.speak(audl,this);
            }
        }
        catch (Exception exception)
        {
        }

    }

    public void checkAnswer2(OBControl targ,PointF pt)
    {
        setStatus(STATUS_CHECKING);
        long token = -1;
        try
        {
            if (sequenceLock.isLocked())
            {
                token = takeSequenceLockInterrupt(true);
                sequenceLock.unlock();
                waitForSecs(0.02);
            }
            setAnswerButtonSelected((OBPath)targ);
            if (targ == targets.get(0))
            {
                gotItRightBigTick(false);
                waitSFX();
                setAnswerButtonActive((OBPath)targ);
                waitForSecs(0.5f);
                faceForward();
                waitForSecs(0.3f);
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("CORRECT");
                presenter.speak(audl,this);
                finishQuestion();
            }
            else
            {
                gotItWrongWithSfx();
                waitSFX();
                setAnswerButtonActive((OBPath)targ);
                waitForSecs(0.1f);
                faceForward();
                waitForSecs(0.1f);
                List<Object>audl = (List<Object>) ((Map<String,Object>)audioScenes.get(pageName)).get("INCORRECT");
                presenter.speak(audl,this);
                waitAudio();
                waitForSecs(0.1f);
                demoCqType2b(false);
                //setStatus(STATUS_WAITING_FOR_ANSWER);
            }
        }
        catch (Exception exception)
        {
        }

    }
    public Object findTarget(PointF pt)
    {
        OBControl c = finger(-1,2,targets,pt);
        return c;
    }

    public void touchDownAtPoint(final PointF pt,View v)
    {
        if (status() == STATUS_WAITING_FOR_ANSWER)
        {
            final OBControl obj = (OBControl) findTarget(pt);
            if (cqType == 1 || obj != null)
            {
                setStatus(STATUS_CHECKING);
                target = obj;
                OBUtils.runOnOtherThread(new OBUtils.RunLambda() {
                    @Override
                    public void run() throws Exception {
                        if (cqType == 1)
                        {
                            takeSequenceLockInterrupt(true);
                            sequenceLock.unlock();
                            checkAnswer1(target,pt);
                            return;
                        }
                        if (target != null)
                        {
                            takeSequenceLockInterrupt(true);
                            sequenceLock.unlock();
                            checkAnswer2(target,pt);
                        }
                    }
                });
            }
        }
    }

}
