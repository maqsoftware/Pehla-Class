# Building Pehla Class

Last updated: August 26, 2019

## Requirements
1. Ensure you have _adb_ installed on your computer. To do this, you can [follow the steps in this helpful guide](https://www.androidpit.com/how-to-install-adb-and-fastboot).
2. Connect your device to the computer via USB.

## 1. Device preparation

##### Enable developer mode on your device
1. Go to **Settings --> About Phone/tablet**.
2. Tap **Build Number** 7 times until it displays _"You are now a developer"_.

##### Enable USB Debugging on your device
1. Go to **Settings --> Developer** options.
2. Tap **Enable USB debugging**.
3. Tap **OK** when prompted by the disclaimer.
4. You should see a dialog box with your computer's _"RSA key fingerprint"_.
5. Tap _"Always allow from this computer"_.
6. Tap **OK**.

## 2. Building the Pehla Class app

1. Ensure you have **Android Studio** installed. To do this, you can [follow the steps in this helpful guide](https://developer.android.com/studio/install.html).
     
2. Start Android Studio and import the project into it.

3. In order to build the app for a specific language, select the desired language from the build variant.

4. Add `google-services.json` file in language specific [app](https://github.com/maqsoftware/Pehla-Class/tree/master/app/src) folder. The `google-services.json` file is available after registering a new app in the Firebase console.

5. Build the project.
		
## 3. Installing Pehla Class

1. Install the application via adb:

	Pehla Class English:

		adb install app/english/debug/app-english-release.apk
		
	Pehla Class Hindi:
	
		adb install app/hindi/debug/app-hindi-release.apk
		
2. Download the OBB file from the latest GitHub [release](https://github.com/maqsoftware/Pehla-Class/releases) and follow the instructions provided there.


## FAQs
1. The application throws _keystore_ file not found error. How do I fix this?
	> _keystore_ file is used to digitally sign an Android application and hence, it is not provided with the project. One must create their own _keystore_ file using the [Android KeyTool](https://developer.android.com/studio/publish/app-signing) which comes with the Android Studio in order to sign the APK.

2. How to enable the _Build variant_ option in the _Build_ menu?
	> The _Build variant_ option is enabled only when the module's gradle file is opened.
