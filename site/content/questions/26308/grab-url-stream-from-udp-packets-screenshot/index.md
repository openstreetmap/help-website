+++
type = "question"
title = "Grab URL stream from UDP packets [+screenshot]"
description = '''I&#x27;m trying to grab the stream url from a Mixlr.com channel using Wireshark. It seems to send UDP packets, but I don&#x27;t know how to proceed. Here&#x27;s a screenshot. http://prntscr.com/1z4gx5/direct My aim is to play the audio stream within foobar2000 or winamp.'''
date = "2013-10-22T20:31:00Z"
lastmod = "2013-10-23T00:30:00Z"
weight = 26308
keywords = [ "udp", "audio", "packets", "stream" ]
aliases = [ "/questions/26308" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Grab URL stream from UDP packets \[+screenshot\]](/questions/26308/grab-url-stream-from-udp-packets-screenshot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26308-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to grab the stream url from a Mixlr.com channel using Wireshark. It seems to send UDP packets, but I don't know how to proceed. Here's a screenshot.</p><p><a href="http://prntscr.com/1z4gx5/direct">http://prntscr.com/1z4gx5/direct</a></p><p>My aim is to play the audio stream within foobar2000 or winamp.</p></div><div id="question-tags" class="tags-container tags">udp audio packets stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/5f6001f7b74af5228928f35770f0d79e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redraw&#39;s gravatar image" /><p>redraw<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redraw has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '13, 20:32</p></div></div><div id="comments-container-26308" class="comments-container"></div><div id="comment-tools-26308" class="comment-tools"></div><div class="clear"></div><div id="comment-26308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26311"></span>

<div id="answer-container-26311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26311-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can not see the screenshot (campany's web proxy), but this is the workflow I follow...</p><ol><li>Capture the udp stream.</li><li>With wireshark, right mouse, and Follow UDP Stream.</li><li>Under the window "Follow UDP Stream", there is a combo: Select the direction of the stream you want to hear.</li><li>Leave "RAW" an press Save As, and put the file in your hard disk, for example c:\tmp\listen.raw</li></ol><p>Now, you need an audio program, I use Adobe Audition (COOLEDIT before)</p><ol><li>File-&gt;Open As, select your file c:\tmp\listen.raw, and a new window appears.</li><li>Select sample rate, Mono/Stereo and bits per sample. You must try different parameters until you find the correct values or know exactly them from another source.</li><li>In the second window (I don't know the title in English, but must be something like "Interprete sample format as") I usually put the same values as the second's.</li><li>A third window called "PCM Raw Data (no header)" is presented. Play a little with the options. In telephony, A-Law or Mu-Law encoding is used, but I suppose is not your scenario. Click OK.</li><li>The decoded audio is presented and you can play, pause, etc with the "Transport" window under the waveform.</li></ol><p>I hope this solves your doubt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/e0ca40365e0601cbfef67d5c9b7d27f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chirrin%20Dul%20Ari&#39;s gravatar image" /><p>Chirrin Dul Ari<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chirrin Dul Ari has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '13, 00:34</p></div></div><div id="comments-container-26311" class="comments-container"><span id="26327"></span><div id="comment-26327" class="comment"><div id="post-26327-score" class="comment-score"></div><div class="comment-text"><p>Hey that's interesting! I'll try that for saving audio. However it's not what I needed. What I wanted is to grab the Stream URL. For example, <a href="http://live.radio.com:8080/play.m3u">http://live.radio.com:8080/play.m3u</a></p><p>I tried searching on the HTML code of some Mixlr channel but couldn't find any clue.</p></div><div id="comment-26327-info" class="comment-info"><span class="comment-age">(23 Oct '13, 09:21)</span> redraw</div></div></div><div id="comment-tools-26311" class="comment-tools"></div><div class="clear"></div><div id="comment-26311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

