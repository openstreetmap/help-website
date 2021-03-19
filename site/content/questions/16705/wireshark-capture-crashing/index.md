+++
type = "question"
title = "Wireshark Capture Crashing"
description = '''I&#x27;m trying to setup wireshark on a server in our environment. I have downloaded the most current version at this time 1.8.4 and installed the WinPcap that comes with it. I have tried a few different settings to see if i can get different behavior, i have been unsuccessful. I have set the following p...'''
date = "2012-12-07T12:25:00Z"
lastmod = "2012-12-07T12:37:00Z"
weight = 16705
keywords = [ "1.8.4", "capture", "capture-options", "wireshark" ]
aliases = [ "/questions/16705" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Capture Crashing](/questions/16705/wireshark-capture-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to setup wireshark on a server in our environment. I have downloaded the most current version at this time 1.8.4 and installed the WinPcap that comes with it.</p><p>I have tried a few different settings to see if i can get different behavior, i have been unsuccessful.</p><p>I have set the following parameters and it will work for about 20 minutes and then wireshark crashes with C++ runtime issues.</p><p>Next File Every 15 minutes Ring buffer with 2 files</p><p>I have tried varying these values to see if any difference no luck. Wireshark seems to always crash after about 20 minutes. I'm looking to get this working for debugging we need on a server.</p><p>Thanks, Greg</p></div><div id="question-tags" class="tags-container tags">1.8.4 capture capture-options wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/3712cc52c77ca6755e1412a865dcdca8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="absoluteg449&#39;s gravatar image" /><p>absoluteg449<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="absoluteg449 has no accepted answers">0%</span></p></div></div><div id="comments-container-16705" class="comments-container"><span id="16706"></span><div id="comment-16706" class="comment"><div id="post-16706-score" class="comment-score"></div><div class="comment-text"><p>This is what i see when it breaks: Problem signature: Problem Event Name: APPCRASH Application Name: wireshark.exe Application Version: 1.8.4.46250 Application Timestamp: 50b66046 Fault Module Name: libglib-2.0-0.dll Fault Module Version: 2.32.2.0 Fault Module Timestamp: 4faa7bfc Exception Code: 40000015 Exception Offset: 000000000004fd12 OS Version: 6.1.7600.2.0.0.272.7 Locale ID: 1033 Additional Information 1: 26cb Additional Information 2: 26cb520882fc9cea3b5c8c04fa568662 Additional Information 3: 2ad2 Additional Information 4: 2ad2e6f5b836401c72b8f768cc4a55f1</p></div><div id="comment-16706-info" class="comment-info"><span class="comment-age">(07 Dec '12, 12:26)</span> absoluteg449</div></div></div><div id="comment-tools-16705" class="comment-tools"></div><div class="clear"></div><div id="comment-16705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16707"></span>

<div id="answer-container-16707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16707-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several of these report here and it's most certainly a problem with memory usage.</p><blockquote><p><code>http://wiki.wireshark.org/KnownBugs/OutOfMemory</code><br />
</p></blockquote><p>One user reported to have fixed the problem, by re-installing Wireshark.</p><blockquote><p><code>http://ask.wireshark.org/questions/6031/wireshark-is-faulting-on-windows-7</code><br />
</p></blockquote><p>Solution: Don't capture with Wireshark, use dumpcap instead.</p><blockquote><p><code>http://www.wireshark.org/docs/man-pages/dumpcap.html</code><br />
</p></blockquote><p>After you have captured the data with dumpcap, you can analyze the files with Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16707" class="comments-container"></div><div id="comment-tools-16707" class="comment-tools"></div><div class="clear"></div><div id="comment-16707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

