package com.maq.xprize.onecourse.hindi.utils;

import android.app.Application;

import com.google.firebase.database.FirebaseDatabase;

public class Firebase_offline_capability extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        FirebaseDatabase.getInstance().setPersistenceEnabled(true);
    }
}
