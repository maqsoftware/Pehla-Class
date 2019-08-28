package com.maq.pehlaclass.service;

/*
 * Copyright (C) 2012 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import com.google.android.vending.expansion.downloader.impl.DownloaderService;

/**
 * This class demonstrates the minimal client implementation of the
 * DownloaderService from the Downloader library.
 */
public class ExpansionDownloaderService extends DownloaderService {
    // stuff for LVL -- MODIFY FOR YOUR APPLICATION!
    private static final String BASE64_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5E1t1FQhxSpsPWwpZAb0QVg2CQumGcJYYXvFG8wrm117T+X3X1nQeGMOT4JTZwX5ADGBsJGKviFKZYE5YP+vg8aREXDN1upP3k2L1Ssqg5+tAwPDaV0mNCyn+tPJZPzU8jVAorhjurjWdEJuFnheeTham6tSVkzQyPI6HvPyCB/sR0NYSHiXqb+72YEdoOZivBqQJYo5ThXxEOExHP2SwQlmZsnVnzjOt+7CmLPKWIMIhskQMCDC0+pkkhoqcBZUk45088hxdd7NXM4fkNJNnTeDHcCxWJZ8WUGq+fvTu0XJqD61vzzUOYUCgOBtUdBnrxOcNuZf3TymSwH/2U3u6wIDAQAB";
    // used by the preference obfuscater
    private static final byte[] SALT = new byte[]{
            76, -119, -11, -102, 17, -81,
            -124, 28, -82, 13, -52, -19, 15, -112, -107, 43, 54, -33, -108, 70
    };

    /**
     * This public key comes from your Android Market publisher account, and it
     * used by the LVL to validate responses from Market on your behalf.
     */
    @Override
    public String getPublicKey() {
        return BASE64_PUBLIC_KEY;
    }

    /**
     * This is used by the preference obfuscater to make sure that your
     * obfuscated preferences are different than the ones used by other
     * applications.
     */
    @Override
    public byte[] getSALT() {
        return SALT;
    }

    /**
     * Fill this in with the class name for your alarm receiver. We do this
     * because receivers must be unique across all of Android (it's a good idea
     * to make sure that your receiver is in your unique package)
     */
    @Override
    public String getAlarmReceiverClassName() {
        return ExpansionAlarmReceiver.class.getName();
    }

}