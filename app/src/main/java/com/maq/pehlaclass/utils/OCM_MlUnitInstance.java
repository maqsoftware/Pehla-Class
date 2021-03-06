package com.maq.pehlaclass.utils;

import android.content.ContentValues;
import android.database.Cursor;
import android.util.ArrayMap;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.json.JSONObject;
import com.maq.pehlaclass.mainui.MainActivity;
import com.maq.pehlaclass.mainui.OBSectionController;

import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

/**
 * Created by michal on 02/08/2017.
 * MlUnitInstance - Masterlist Unit Instance
 * This is individual instance of MlUnit. Every time a Unit is opened, an instance is created and
 * saved in the database. It contains all the progress details, such as score, start/end time,
 * reason of completion (STATUS). Some units contain extra data saved as json in DB. This is used
 * so analysis like wrong answers chosen, timings between actions
 *
 */

public class OCM_MlUnitInstance extends DBObject
{
    public final static int INSTANCE_TYPE_STUDY = 1,
            INSTANCE_TYPE_COMMUNITY = 2,
            INSTANCE_TYPE_PLAYZONE=3,
            INSTANCE_TYPE_PZ_LOCKED=4,
            INSTANCE_TYPE_LIBRARY=5,
            INSTANCE_TYPE_EXTRA=6;
    public final static int STATUS_STARTED = 1,
            STATUS_COMPLETED = 2,
            STATUS_USER_CLOSED =3,
            STATUS_UNIT_TIMEOUT = 10,
            STATUS_SESSION_LOCKED = 11,
            STATUS_BATTERY_LOW = 12,
            STATUS_FAILURE = 20;

    public long assetid;
    public int userid, sessionid, seqNo, elapsedTime, typeid, starColour, statusid;
    public int scoreCorrect, scoreWrong;
    public long startTime, endTime;
    private Map<String,Object> extraData;

    public OBSectionController sectionController;
    public OCM_MlUnit mlUnit;

    private static final String[] intFields = {"userid","sessionid","seqNo","elapsedTime","statusid","typeid","starColour","scoreCorrect", "scoreWrong"};
    private static final String[] longFields = {"startTime","endTime","assetid"};

    public OCM_MlUnitInstance()
    {
        scoreCorrect = 0;
        scoreWrong = 0;
        elapsedTime = 0;
        startTime = 0;
        endTime = 0;
        starColour = -1;
        statusid = STATUS_STARTED;
        assetid = -1;
        extraData = new ArrayMap<>();
    }


    public static OCM_MlUnitInstance initWithMlUnit(OCM_MlUnit unit, int userid, int sessionid, long starttime, int level, int typeid)
    {
        return initInDBWithMlUnit(unit,userid,sessionid,starttime,level,typeid);
    }

    private static OCM_MlUnitInstance initInDBWithMlUnit(OCM_MlUnit unit, int userid, int sessionid, long starttime, int week, int typeid)
    {
        OCM_MlUnitInstance mlui = new OCM_MlUnitInstance();
        mlui.userid = userid;
        mlui.sessionid = sessionid;
        mlui.mlUnit = unit;
        mlui.typeid = typeid;

        DBSQL db = null;
        try
        {
            db = new DBSQL(true);
            Cursor cursor = db.prepareRawQuery(String.format("SELECT MAX(seqNo) as seqNo FROM %s AS UI " +
                    "JOIN %s AS S ON S.userid = UI.userid AND S.sessionid = UI.sessionid " +
                            "WHERE UI.userid = ? AND UI.unitid = ? AND UI.extraunitid = ? AND UI.typeid = ? AND S.day > ? AND S.day <= ?",
                    DBSQL.TABLE_UNIT_INSTANCES, DBSQL.TABLE_SESSIONS),
                    Arrays.asList(String.valueOf(userid), String.valueOf(unit.unitid),String.valueOf(unit.extraunitid),String.valueOf(typeid)
                            ,String.valueOf((week-1)*7),String.valueOf(week*7)));

            int columnIndex = cursor.getColumnIndex("seqNo");
            if(cursor.moveToFirst() && !cursor.isNull(columnIndex))
            {
                mlui.seqNo = cursor.getInt(columnIndex) + 1;
            }
            else
            {
                mlui.seqNo = 0;
            }
            mlui.startTime = starttime;
            if(!mlui.saveToDB(db))
                mlui = null;
            cursor.close();
        }
        catch(Exception e)
        {
            MainActivity.log("OCM_MlUnitInstance: database access error: " + e.getMessage());
        }
        finally
        {
            if(db != null)
                db.close();
        }
        return mlui;
    }


    public boolean updateDataInDB(DBSQL db)
    {
        Map<String,String> whereMap = new ArrayMap<>();
        whereMap.put("userid",String.valueOf(userid));
        whereMap.put("unitid",String.valueOf(mlUnit.unitid));
        whereMap.put("seqNo",String.valueOf(seqNo));
        whereMap.put("sessionid",String.valueOf(sessionid));
        whereMap.put("typeid",String.valueOf(typeid));
        whereMap.put("extraunitid",String.valueOf(mlUnit.extraunitid));

        ContentValues contentValues = new ContentValues();
        contentValues.put("endTime",endTime);
        contentValues.put("scoreCorrect",scoreCorrect);
        contentValues.put("scoreWrong",scoreWrong);
        contentValues.put("elapsedTime",elapsedTime);
        contentValues.put("starColour",starColour);
        contentValues.put("statusid",statusid);
        contentValues.put("assetid",assetid);
        if(extraData.size() > 0)
        {
            try
            {
                Gson gson = new GsonBuilder().disableHtmlEscaping().create();
                contentValues.put("extra", gson.toJson(extraData));
            }
            catch (Exception e)
            {
                MainActivity.log("OCM_MlUnitInstance: error converting data to json: " + e.getMessage());
            }
        }
        boolean result = db.doUpdateOnTable(DBSQL.TABLE_UNIT_INSTANCES,whereMap,contentValues) > 0;
        return result;
    }

    public Boolean saveToDB(DBSQL db)
    {
        ContentValues contentValues = getContentValues(null,intFields,longFields,null);
        contentValues.put("unitid", mlUnit.unitid);
        contentValues.put("extraunitid", mlUnit.extraunitid);
        boolean result = db.doInsertOnTable(DBSQL.TABLE_UNIT_INSTANCES,contentValues) > 0;
        return result;
    }


    public void addExtraData(String tag, Object data)
    {
        extraData.put(tag, data);
    }
}
