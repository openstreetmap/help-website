+++
type = "question"
title = "audio mapping - error playing audio in JOSM"
description = '''I just tried my luck at doing some audio mapping. Audio recorder in one pocket, GPS in the other. I got an mp3 file (a little over 14min long) and a GPX track, which I tried to sync in JOSM. I used Audacity to convert the mp3 file to WAV, as it&#x27;s the only format JOSM knows. Importing audio works ok,...'''
date = "2013-08-01T12:36:00Z"
lastmod = "2013-08-13T03:49:00Z"
weight = 24786
keywords = [ "josm", "audio" ]
aliases = [ "/questions/24786" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [audio mapping - error playing audio in JOSM](/questions/24786/audio-mapping-error-playing-audio-in-josm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24786-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just tried my luck at doing some audio mapping. Audio recorder in one pocket, GPS in the other. I got an mp3 file (a little over 14min long) and a GPX track, which I tried to sync in JOSM. I used Audacity to convert the mp3 file to WAV, as it's the only format JOSM knows. Importing audio works ok, but then I'm unable to play the file. I get an error message saying: "Error plyaing sound / unspecified reason", which is pretty criptic.</p>
<p>Is there a specific format for wav that josm requires? or some other trick I should be aware of? I think I followed the help pages, but still...</p>
<p>I'm using JOSM 6060 (openJDK 7) on ubuntu 12.04.</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '13, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/86699511eef78befb285a9c1d64677bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LaurentS&#39;s gravatar image" />
<p><span>LaurentS</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LaurentS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24786" class="comments-container">
<span id="25290"></span>
<div id="comment-25290" class="comment">
<div id="post-25290-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could upload the wav (or a part of it) to somewhere. Then others here could try if it plays on their systems/JOSMs.</p>
</div>
<div id="comment-25290-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 01:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25291"></span>
<div id="comment-25291" class="comment">
<div id="post-25291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I made 2 Wav files (using different codecs) from the recorded. None played under linux, but I tried on OSX, where 1 worked, the other not (but gave a proper message hinting at a wrong encoding). So I'm guessing there might be some issue with audio+linux, but I haven't found any java demo to test audio in some other app. Any hints?</p>
</div>
<div id="comment-25291-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 02:03)</span> <span class="comment-user userinfo">LaurentS</span>
</div>
</div>
<span id="25294"></span>
<div id="comment-25294" class="comment">
<div id="post-25294-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean by "2 wav files using different codecs"? I suspect JOSM is expecting 16-bit PCM, are you using something else?</p>
<p>(You might also try using mpg123 to dump your source mp3 to .wav ["mpg123 -w (filename).wav (filename).mp3"] if the ones you're getting from Audacity are giving you trouble, since I think mpg123 dumps standard 16-bit PCM wav files.</p>
</div>
<div id="comment-25294-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 03:23)</span> <span class="comment-user userinfo">Epicanis</span>
</div>
</div>
<span id="25295"></span>
<div id="comment-25295" class="comment">
<div id="post-25295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried it (never used before and had to find out how to open - not via "open"(!) but via gpx, import audio - an audio file. However, I (JOSM v6115, sun java 1.7.0) got this error message box, no error in the terminal and no sound: "No line matching interface SourceDataLine supporting format PCM_SIGNED 44100.0 Hz, 16 bit, stereo, 4 bytes/frame, little-endian is supported." By searching the web a bit I found out that sound with java under linux is known to be problematic. I am stopping here - someone with JOSM audio mapping experience will likely know...</p>
</div>
<div id="comment-25295-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 03:49)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24786-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25288"></span>

<div id="answer-container-25288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25288-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm afraid I can't be of much help, but wanted to comment because I didn't even know this (geosynchronised audio) was possible. I'll have to play with it - I've thought about trying to do similar things (perhaps a script that generates video frames from map imagery at the appropriate intervals, then transcodes the audio and images into webm or similar video format).</p>
<p>As far as the unhelpful "like, dude, something went wrong" error from JOSM, the only thing I can think of as something to check is that perhaps pulseaudio is causing a problem. You might try killing pulseaudio before launching JOSM and see if that works any better.</p>
<p>(Additionally, it might be worth trying to run JOSM from a terminal window, just in case there are any potentially-useful "raw" error messages coming out on stderr that might give a hint on where to look).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '13, 01:06</strong></p>
<img src="https://secure.gravatar.com/avatar/57654c826776bb5110ac59503f83b3b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Epicanis&#39;s gravatar image" />
<p><span>Epicanis</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Epicanis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25288" class="comments-container">
<span id="25292"></span>
<div id="comment-25292" class="comment">
<div id="post-25292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't mention it, but I did run in terminal, but it gave no further info, sadly :( As for pulseaudio, I don't use it, alsa instead, maybe that could be it?</p>
</div>
<div id="comment-25292-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 02:29)</span> <span class="comment-user userinfo">LaurentS</span>
</div>
</div>
<span id="25293"></span>
<div id="comment-25293" class="comment">
<div id="post-25293-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you're running just ALSA without pulseaudio but DON'T have DMIX configured, you might be running into a problem where some other program is monopolizing the audio device - that could also be an issue, though your other comment may suggest something else is happening with the wav files instead.</p>
</div>
<div id="comment-25293-info" class="comment-info">
<span class="comment-age">(13 Aug '13, 03:20)</span> <span class="comment-user userinfo">Epicanis</span>
</div>
</div>
</div>
<div id="comment-tools-25288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25288-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

