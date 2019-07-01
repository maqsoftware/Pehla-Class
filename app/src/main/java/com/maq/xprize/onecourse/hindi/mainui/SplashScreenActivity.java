package com.maq.xprize.onecourse.hindi.mainui;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.Dialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Toast;

import com.google.android.vending.expansion.downloader.Helpers;
import com.maq.xprize.onecourse.hindi.R;
import com.maq.xprize.onecourse.hindi.utils.Zip;

import java.io.File;
import java.io.IOException;
import java.util.zip.ZipFile;

import static com.maq.xprize.onecourse.hindi.R.layout.activity_splash_screen;
import static com.maq.xprize.onecourse.hindi.mainui.DownloadExpansionFile.xAPKS;
import static com.maq.xprize.onecourse.hindi.mainui.MainActivity.sharedPref;

public class SplashScreenActivity extends Activity {

    public static String assetsPath;
    Intent mainActivityIntent = null;
    String unzipDataFilePath;
    File expansionFile;
    ZipFile expansionZipFile;
    Zip zipHandler;
    File packageNameDir;
    int defaultFileVersion = 0;
    int storedMainFileVersion;
    int storedPatchFileVersion;
    boolean flagSwitchToInternal = false;
    boolean isExtractionRequired = false;

    public Dialog sdCardPreferenceDialog() {
        final SharedPreferences.Editor editor = sharedPref.edit();
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(false);
        builder.setMessage(R.string.dialogInfo)
                .setPositiveButton(R.string.dialogYes, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int id) {
                        editor.putInt(getString(R.string.dataPath), 2);
                        editor.apply();
                        startExtraction();
                    }
                })
                .setNegativeButton(R.string.dialogNo, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int id) {
                        editor.putInt(getString(R.string.dataPath), 1);
                        editor.apply();
                        startExtraction();
                    }
                });
        return builder.create();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        View decorView = this.getWindow().getDecorView();
        int uiOptions = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY;
        decorView.setSystemUiVisibility(uiOptions);
        setContentView(activity_splash_screen);
        if (isSDcard() && sharedPref.getInt("dataPath", 0) == 0) {
            flagSwitchToInternal = true;
            Dialog builder = sdCardPreferenceDialog();
            builder.show();
        } else {
            final SharedPreferences.Editor editor = sharedPref.edit();
            editor.putInt("dataPath", 1);
            editor.apply();
            startExtraction();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           @NonNull String[] permissions, @NonNull int[] grantResults) {
        // If request is cancelled, the result arrays are empty.
        if (requestCode == 1) {
            if (grantResults.length > 0
                    && grantResults[0] == PackageManager.PERMISSION_GRANTED
                    && grantResults[1] == PackageManager.PERMISSION_GRANTED) {
                sharedPref = getSharedPreferences("ExpansionFile", MODE_PRIVATE);
                // Retrieve the stored values of main and patch file version
                storedMainFileVersion = sharedPref.getInt(getString(R.string.mainFileVersion), defaultFileVersion);
                storedPatchFileVersion = sharedPref.getInt(getString(R.string.patchFileVersion), defaultFileVersion);
                isExtractionRequired = isExpansionExtractionRequired(storedMainFileVersion, storedPatchFileVersion);
                // If main or patch file is updated, the extraction process needs to be performed again
                if (isExtractionRequired) {
                    new DownloadFile().execute(null, null, null);
                }
            } else {
                Toast.makeText(this, "Permission required!", Toast.LENGTH_LONG).show();
                finish();
            }
        }
    }

    private boolean isExpansionExtractionRequired(int storedMainFileVersion, int storedPatchFileVersion) {
        for (DownloadExpansionFile.XAPKFile xf : xAPKS) {
            // If main or patch file is updated set isExtractionRequired to true
            if (xf.mIsMain && xf.mFileVersion != storedMainFileVersion || !xf.mIsMain && xf.mFileVersion != storedPatchFileVersion) {
                return true;
            }
        }
        return false;
    }

    public boolean isSDcard() {
        File[] fileList = getObbDirs();
        return fileList.length >= 2;
    }

    private void startExtraction() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED ||
                ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED ||
                ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED) {
            // Permission is not granted
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.RECORD_AUDIO, Manifest.permission.CAMERA}, 1);
        } else {
            new DownloadFile().execute(null, null, null);
        }
    }

    public String getDataFilePath(Context activityContext) {
        String internalDataFilePath = null;
        String externalDataFilePath = null;
        String dataFilePath = null;
        File[] fileList = activityContext.getExternalFilesDirs(null);
        for (File file : fileList) {
            if (!file.getAbsolutePath().equalsIgnoreCase(Environment.getExternalStorageDirectory().getAbsolutePath() + "/Android/data/" + activityContext.getPackageName() + "/files") &&
                    file.isDirectory() &&
                    file.canRead() &&
                    isSDcard() &&
                    sharedPref.getInt(getString(R.string.dataPath), 0) == 2) {
//              For external storage path
                externalDataFilePath = file.getAbsolutePath() + File.separator;
            } else if ((sharedPref.getInt(activityContext.getString(R.string.dataPath), 0) == 1 || !flagSwitchToInternal) && internalDataFilePath == null) {
//              For internal storage path
                internalDataFilePath = file.getAbsolutePath() + File.separator;
            }
        }
        if (externalDataFilePath == null) {
            dataFilePath = internalDataFilePath;
        } else if (sharedPref.getInt(activityContext.getString(R.string.dataPath), 0) == 2) {
            dataFilePath = externalDataFilePath;
        }
        assetsPath = dataFilePath;
        return dataFilePath;
    }

    public File getOBBFilePath(DownloadExpansionFile.XAPKFile xf) {
        sharedPref = getSharedPreferences("ExpansionFile", MODE_PRIVATE);
        storedMainFileVersion = sharedPref.getInt(getString(R.string.mainFileVersion), 0);
        storedPatchFileVersion = sharedPref.getInt(getString(R.string.patchFileVersion), 0);
        String internalOBBFilePath = null;
        String externalOBBFilePath = null;
        File externalOBBFile = null;
        File internalOBBFile = null;
        File[] fileList = getObbDirs();
        for (File file : fileList) {
            if (!file.getAbsolutePath().equalsIgnoreCase(Environment.getExternalStorageDirectory().getAbsolutePath() + "/Android/obb/" + getPackageName()) &&
                    file.isDirectory() &&
                    file.canRead() &&
                    isSDcard()) {
//              For external storage path
                externalOBBFilePath = file.getAbsolutePath() + File.separator +
                        Helpers.getExpansionAPKFileName(this, xf.mIsMain, xf.mFileVersion);
                externalOBBFile = new File(externalOBBFilePath);
            } else {
//              For internal storage path
                internalOBBFilePath = file.getAbsolutePath() + File.separator +
                        Helpers.getExpansionAPKFileName(this, xf.mIsMain, xf.mFileVersion);
                internalOBBFile = new File(internalOBBFilePath);
            }
        }
        /*
         * Check for OBB file in both internal and external storage and choose internal storage path if file is not available in external storage.
         * externalOBBFile is null only when internal storage is available
         */
        if (externalOBBFile != null && externalOBBFile.exists()) {
            return externalOBBFile;
        }
        return internalOBBFile;
    }

    /* function to call the main application after extraction */
    public void toCallApplication() {
        mainActivityIntent = new Intent(this, MainActivity.class);
        startActivity(mainActivityIntent);
        finish();
    }

    public void unzipFile() {
        int totalZipSize = getTotalExpansionFileSize();
        try {
            for (DownloadExpansionFile.XAPKFile xf : xAPKS) {
                if (xf.mIsMain && xf.mFileVersion != storedMainFileVersion || !xf.mIsMain && xf.mFileVersion != storedPatchFileVersion) {
                    expansionFile = getOBBFilePath(xf);
                    expansionZipFile = new ZipFile(expansionFile);
                    zipHandler = new Zip(expansionZipFile, this);
                    unzipDataFilePath = getDataFilePath(this);
                    packageNameDir = new File(unzipDataFilePath);
                    if (xf.mIsMain && !packageNameDir.exists()) {
                        packageNameDir.mkdir();
                    }
                    zipHandler.unzip(packageNameDir, totalZipSize, xf.mIsMain, xf.mFileVersion, sharedPref);
                    zipHandler.close();
                }
            }
            toCallApplication();
        } catch (IOException e) {
            System.out.println("Could not extract assets");
            System.out.println("Stack trace:" + e);
        }
    }

    public boolean isStorageSpaceAvailable() {
        long totalExpansionFileSize = 0;
        File internalStorageDir = Environment.getDataDirectory();
        for (DownloadExpansionFile.XAPKFile xf : xAPKS) {
            if (xf.mIsMain && xf.mFileVersion != storedMainFileVersion || !xf.mIsMain && xf.mFileVersion != storedPatchFileVersion) {
                totalExpansionFileSize = xf.mFileSize;
            }
        }
        return totalExpansionFileSize < internalStorageDir.getFreeSpace();
    }

    public int getTotalExpansionFileSize() {
        int totalExpansionFileSize = 0;
        ZipFile zipFile;
        try {
            for (DownloadExpansionFile.XAPKFile xf : xAPKS) {
                if (xf.mIsMain && xf.mFileVersion != storedMainFileVersion || !xf.mIsMain && xf.mFileVersion != storedPatchFileVersion) {
                    ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 99);
                    expansionFile = getOBBFilePath(xf);
                    zipFile = new ZipFile(expansionFile);
                    totalExpansionFileSize += zipFile.size();
                }
            }
        } catch (IOException ie) {
            System.out.println("Couldn't get total expansion file size");
            System.out.println("Stacktrace: " + ie);
        }
        return totalExpansionFileSize;
    }


    private class DownloadFile extends AsyncTask<String, Integer, String> {
        @Override
        protected String doInBackground(String... sUrl) {
            if (isStorageSpaceAvailable()) {
                unzipFile();
            } else {
                SplashScreenActivity.this.runOnUiThread(new Runnable() {
                    public void run() {
                        Toast.makeText(SplashScreenActivity.this, "Insufficient storage space! Please free up your storage to use this application.", Toast.LENGTH_LONG).show();
                        // Call finish after the toast message disappears
                        new Handler().postDelayed(new Runnable() {
                            @Override
                            public void run() {
                                SplashScreenActivity.this.finish();
                            }
                        }, Toast.LENGTH_LONG);
                    }
                });
            }
            return null;
        }
    }
}