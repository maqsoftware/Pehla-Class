package com.maq.xprize.onecourse.hindi.receivers;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.support.v4.app.NotificationCompat;

import com.maq.xprize.onecourse.hindi.R;
import com.maq.xprize.onecourse.hindi.mainui.MainActivity;

public class NotificationReminderReceiver extends BroadcastReceiver {
    private static final String CHANNEL_ID = "studyReminderChannel";
    private static final String LOGTAG = "ReminderNotification";
    private static final int NOTIFICATION_ID = LOGTAG.hashCode();
    private static final CharSequence notificationContentText = "It's time to study today's content. Let's start...";
    private NotificationManager notificationManager;

    @Override
    public void onReceive(Context context, Intent intent) {
        // Intent to start main activity when notification is tapped
        Intent notifyIntent = new Intent(context, MainActivity.class);
        // Set the Activity to start in a new, empty task
        notifyIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK
                | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        // Create the PendingIntent
        PendingIntent notifyPendingIntent = PendingIntent.getActivity(
                context, 0, notifyIntent, PendingIntent.FLAG_UPDATE_CURRENT
        );

        // Create notification channel to display notifications
        createNotificationChannel(context);

        // Get application label
        CharSequence applicationLabel = context.getPackageManager().getApplicationLabel(context.getApplicationInfo());

        // Notification manager for Android 7 and below
        NotificationManager mNotificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);

        // Notification builder object to set notification properties
        NotificationCompat.Builder mBuilder = new NotificationCompat.Builder(context, CHANNEL_ID);

        // Set notification properties
        mBuilder.setPriority(Notification.PRIORITY_DEFAULT);
        mBuilder.setCategory(Notification.CATEGORY_REMINDER);
        mBuilder.setContentText(notificationContentText);
        mBuilder.setSmallIcon(R.mipmap.icon_child);
        mBuilder.setContentTitle(applicationLabel);
        mBuilder.setDefaults(Notification.DEFAULT_SOUND);
        mBuilder.setContentIntent(notifyPendingIntent);
        mBuilder.setAutoCancel(true);

        // Issue notification based on Device's Android version
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            notificationManager.notify(NOTIFICATION_ID, mBuilder.build());
        } else {
            mNotificationManager.notify(NOTIFICATION_ID, mBuilder.build());
        }
//        }
    }

    private void createNotificationChannel(Context context) {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is new and not in the support library
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            CharSequence name = context.getResources().getString(R.string.reminders_channel_name);
            String description = context.getResources().getString(R.string.reminders_channel_description);
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, name, importance);
            channel.setDescription(description);
            // Register the channel with the system; you can't change the importance
            // or other notification behaviors after this
            notificationManager = context.getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }
}
