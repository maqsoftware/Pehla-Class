# Localization of onecourse


## Process
There are 8 key steps to localize onecourse. We work with local linguistic experts at each stage:

1. **Analyse target language and culture**. Examine the target language, and build a clear description of it, including: linguistic structure, alphabet, phonetic structure, order and frequency of grapheme, list of high frequency words, set of common first and last names.  Carry out a comprehensive analysis to understand the target area, in order to culturally adapt the course to that specific geographical area.
2. **Cross check target language**. Check the description of the new language against our existing learning activities. Develop new components or modes, if beneficial to the child.
3. **Story selection**. Select appropriate stories from our extensive book library, and write or curate further stories as required.
4. **Translation**. Translate the full database of words, instruction scripts for each activity, chosen stories, and numeracy learning units.
5. **Writing**. If there is any additional material required for the target language, such as simple phrases and sentences, it will be written at this stage.
6. **Images**. Creation of any new images required for learning units and stories.
7. **Recording**. Recording of all audio material required, using several voice artists.
8. **Final build**. With all assets prepared, build onecourse in the new target language.


## Overview
Each localized version of onecourse requires a language pack for a _locale_. A locale is a pairing of a language and an optional region (e.g. Tanzanian Swahili, British English). A locale is represented using abbreviated codes, so Swahili would be `sw` and British English `en_GB`. A language pack consists of eight elements:

1. The alphabet
2. Phonemes, syllables and words
3. Audio and images
4. Stories
5. Component audio
6. Learning journey
7. Fonts
8. Video subtitles


## Language Pack

### 1. Alphabet
The file `assets/oc-literacy-gen/local/LOCALE/letters.xml` defines the individual letters that constitute the language’s alphabet.
Each `letter` has a unique id and an optional set of `tags`. Possible values for the tag attribute vary across language families, with `vowel` being used in both English and Swahili. The letters _a_, _b_ and _d_ are represented like this:

```xml	
<letters>
	<letter id="a" tags="vowel"></letter>
	<letter id="b"></letter>
	<letter id="d"></letter>
</letters>
```

### 2. Phonemes, syllables and words
The file `assets/oc-literacy-gen/local/LOCALE/wordcomponents.xml` defines the key phonemes, consonant clusters and syllables present in the language. It also contains a curated set of high-frequency and culturally specific words for learning the language.

Each `phoneme` has a unique `id` with the prefix `is`. In English, the phonemes _a, th_ and _ng'_ are represented like this:

```xml		
<phonemes>
	<phoneme id="is_a">a</phoneme>
	<phoneme id="is_th">th</phoneme>
	<phoneme id="is_ng_apost_">ng'</phoneme>
</phonemes>
```

Next come syllables. Each `syllable` is made from one or more `phoneme` and has a unique `id` with the prefix `isyl`. The individual phonemes in each syllable are delimited by `/`. In English, the syllables _axe_ and _bird_ are represented like this:
	
```xml
<syllables>
	<syllable id="isyl_axe">a/x/e</syllable>
	<syllable id="isyl_zwe">b/ir/d</syllable>
</syllables>
```
	
Finally, the set of words. Each `word` is made from one or more `phonemes` or `syllables` and has a unique `id` with the prefix `fc`. The phonemes or syllables in each word are delimited by `/`. In English, the words _cat_ and _flower_ are represented like this:

```xml
<words>
	<word id="fc_cat">cat</word>
	<word id="fc_flower">flow/er</word>
</words>
```    


### 3. Audio and images

Each `letter`, `phoneme`, `syllable` and `word` is recorded by a native speaker and an _aac_ compressed version is stored in an _.m4a_ file, named by it's English `id`. For example, in English, the words _hair, leaf_ and _monkey_ exist as recorded audio files: `fc_hair.m4a`, `fc_leaf.m4a` and `fc_monkey.m4a`. These reside in the `assets/oc-literacy-gen/local/LOCALE/` directory.

Where a word is broken down into `syllables` or `phonemes`, the recording has an accompanying _.epta_ file which specifies the start time of each phoneme or syllable in the audio file. For example, the English word _kick_, recorded in the file `fc_let_kick.m4a` has the following phoneme breakdowns in `fc_let_kick.etpa`:

```xml
	<timings text="k - i - ck">
		<timing id="0" start="0.000" end="0.207" startframe="0" framelength="9108" text="k"/>
		<timing id="1" start="0.609" end="0.924" startframe="26844" framelength="13915" text="i"/>
		<timing id="2" start="1.324" end="1.486" startframe="58401" framelength="7121" text="ck"/>
	</timings>
```


For each `word`, an optional _.png_ image exists. In English, the words _play, lunch_ and _school_ have image files: `fc_children.png`, `fc_lunchbox.png` and `fc_school.png`.


### 4. Stories
Localised stories each have an `id` and reside in `assets/oc-reading/books/xr-[id]/`. Each story has configuration file `book.xml`.
Presentational aspects of the story are defined on the `book` element. Each `page` contains one or more localised `para`. A `page` can have an optional `picjustify` attribute to specify the page layout.

In lower level stories, there is a syllable breakdown for each word, delimited by `/`. The title and first page of the _A very tall man_ story in English are represented like this:

```xml	
<book id="xr-averytallmanEN" indent="N" lineheight="1.5" paraheight="1.33" letterspacing="1" fontsize="50" noparas="true">
	<page pageno="0">
		<para>A ver/y tall man</para>
	</page>
	<page pageno="1">
		<para>Look at this man. His hoe is too short.</para>
	</page>
…
```


Every `para` has a corresponding _.m4a_ recorded audio file and an accompanying _.etpa_ file which specifies the start time of each word in the audio file. For example, the breakdown of the first page of the story above can be seen in `p1_1.etpa`:


```xml
<xml>
	<timings text="Look at this man. His hoe is too short.">
		<timing id="0" start="0.000" end="0.274" startframe="0" framelength="12103" text="Look"/>
		<timing id="1" start="0.274" end="0.465" startframe="12103" framelength="8413" text="at"/>
		<timing id="2" start="0.465" end="0.669" startframe="20516" framelength="8972" text="this"/>
…
```

Each word within a `para` is also individually recorded, along with a version split into syllables for lower-level stories.  

The English transcripts for stories are stored in `assets/transcripts/oc-reading/xr-[id]/english`. Create transcripts for local language and store them in `assets/transcripts/oc-reading/xr-[id]/LOCALE`. Generate audio files in local language and accent from these locale-specific transcripts by using [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html).  
**Note:** Check for the languages supported by Amazon Polly [here](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html).

After the audio files have been generated, use [Amazon Polly's Speech Marks](https://docs.aws.amazon.com/polly/latest/dg/speechmarkexamples.html), to assist with generating _.txt_ files from transcripts. Create a custom script to generate _.etpa_ files from the text files generated by Amazon Polly.


### 5. Component audio
Component localizations consist of a set of _.m4a_ recorded audio files. The file names tend to correspond to the english localization.
For example in the numeracy component _Add and subtract_, `assets/oc-addsubtract/local/en_GB/q_sevenbees.m4a` is the English recording of the phrase _"Seven bees"_. In the reading component _Making plurals_, `assets/oc-makingplurals/local/en_GB/mp2_goodtheyreinorder.m4a` is the english recording of _"Good, they are in order"_.
We have provided mappings of all English audio to _.m4a_ filenames. These are xml files inside the `assets/localization` directory.  

The English transcripts for all the audio files of a specific module are stored in `assets/transcripts/MODULE/english`. Create transcripts for local language and store them in `assets/transcripts/MODULE/LOCALE`. Generate audio files in local language and accent from these locale-specific transcripts by using [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html).


### 6. Learning journey

The child's _learning journey_ is an ordered set of `learning units` to be worked through. A `learning unit` is a `component` with parameters assigned from the underlying language pack as well as any required visual, audio or configuration assets.  It is specific to a particular localization. There are three variants, all residing in the `assets/masterlists/[community|playzone|library]` directory:

#### Community

This is defined in the file `community_LOCALE/units.xml`. An example of the first part of the onecourse English _learning journey_ from `community_enGB/units.xml`is shown below. The First unit is an introduction to using the tablet, the second a _flashcard_ reading activity:

```xml
<level id="1">
	<unit id="1.OC_VideoPlaybackStudy"
	      		target="OC_VideoPlaybackStudy"
	      		config="oc-video,oc-videos-gen"
	      		params="vps/(null)/video=tablet_care_enGB"
	      		targetDuration="900"
	      		passThreshold="0.5"
	      		catAudio=""
	      		lang="en_GB"
	      		icon="icon_0001"
	      		ub_index="3"
	      		awardStar="-1"/>
	<unit id="2.OC_SectionIT"
			target="OC_SectionIT"
	      		config="oc-introduction"
	      		params="eventit"
	      		targetDuration="900"
	      		passThreshold="0.5"
	      		catAudio=""
	      		lang="en_GB"
	      		icon="icon_0002"
	      		ub_index="4"
	      		awardStar="-1"/>
	<unit id="3.OC_Puzzle"
	      		target="OC_Puzzle"
	      		config="oc-lettersandsounds,oc-literacy-gen" 
			params="puzzle;js/format=puzzle4/showtext=none/demo=true/preassembled=true/words=fc_duck,fc_hippopotamus,fc_giraffe,fc_elephant,fc_snake,fc_parrot,fc_crocodile"
	      		targetDuration="900"
	      		passThreshold="0.5"
	      		catAudio=""
	      		lang="en_GB"
	      		icon="icon_0003"
	      		ub_index="5"
	      		awardStar="-1"/>
…
```


##### Levels
A _learning journey_ consists of a number of `levels`. These are ordered groups of 105 `learning units`. They represent _weeks_ in the course, with 15 units per day.

##### Learning units
A `learning unit` has the following parameters:

- `id` unique identifier.
- `target` component the unit is using.
- `param` list of component-specific parameters in `key=value` form, each delimited by `/`.
- `config` configuration directory for audio and video assets used by the component.
- `lang` language pack to be used.
- `targetDuration` upper bound on the time to should take an average child to complete the unit.
- `passThreshold` the ratio of correct:incorrect answers which constitute the child _passing_ the unit successfully.
- `icon` the image shown to the child before beginning the unit. These are `png` files stored in `assets/masterlists/[community|library|playzone]_LOCALE/icons/`

In the following example, the _letter tracing_ component `OC_LetterTrace` is being used. The `params` indicate:

- `lt` single letter mode.
- `intro=false` no introductory audio.
- `letter=i` use the letter `i` from the Swahili `language pack`
- `notraces=4` the letter is to be traced 4 times.

```xml

<unit	id="0052.OC_LetterTrace"
		target="OC_LetterTrace"
		params="lt/intro=false/letter=i/notraces=4"
		config="oc-lettersandsounds"
		lang="en_GB"
		targetDuration="120"
		passThreshold="0.5"
		icon="icon_0052"
/>
```

#### Play Zone
This is defined in the file `playzone_LOCALE/units.xml`. It specifies which units appear in the _play zone_ for each level (week).

#### Library
This is defined in the file `library_LOCALE/units.xml`. It specifies all of the stories in the story library for the locale. Here, _level_ represents the relative complexity of a set of stories.

### 7. Fonts
onecourse by default uses two fonts, `onebillionreader-Regular.otf` and `onebillionwriter-Regular.otf`. These can be replaced by identically named alternative fonts in `app/src/main/fonts/`. Please note onecourse does not currently support right-to-left scripts.

### 8. Video Subtitles
For video clips in the onecourse _play zone_, optional subtitles can be added. These are standard `.srt` text files placed in the `assets/oc-video/local/LOCALE/` directory. Each subtitle entry within a file consists of four parts:

1. A numeric counter identifying each sequential subtitle.
2. The time that the subtitle should appear on the screen, followed by `-->` and the time it should disappear.
3. The subtitle itself on one or more lines.
4. A blank line indicating the end of this subtitle.

For example, the English subtitle for the video _Origami Elephant_ in `assets/oc-video/local/en_GB/origami_elephant.srt`:

```
1
00:00:00,000 --> 00:09:08,990
Make a paper elephant!

```





## Build

Apply the following configurations to files in the onecourse source code directory

###  Settings

Create a settings `.plist` file for the new locale by copying the English:

`cp app/src/main/config/settings_community_enGB.plist app/src/main/config/settings_community_LOCALE.plist`

Edit the new settings file, replacing the value of the following keys:

```
<key>app_masterlist</key>
<string>community_LOCALE</string>

<key>app_masterlist_playzone</key>
<string>playzone_LOCALE</string>

<key>app_masterlist_library</key>
<string>library_LOCALE</string>

```

### Build target

Append the following configuration to `build.gradle`:

```gradle
LOCALE_community_ {
    applicationId ‘org.onebillion.onecourse.child.LOCALE'
    versionCode 1
    versionName '1.0'
    resValue "string", "app_name", "onecourse - Child"
    resValue "string", "test_only", "false"
    buildConfigField 'String', 'SETTINGS_FILE', '"settings_community_LOCALE.plist"'
    manifestPlaceholders = [
            appIcon: "@mipmap/icon_child"
    ]
}
```

Follow the [build instructions](BUILD.md) to compile onecourse.
