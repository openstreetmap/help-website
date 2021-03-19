+++
type = "question"
title = "how to get a Number of frames in a saved pcap file ?"
description = '''Hi, I have a simple doubt in Wireshark, in opening a saved capture file. here what I observed is, when we open the capture file (file-&amp;gt;open), it will open the selected file. if the file is large then it will show a window to show some statistical information as the image shows, here my doubt is 1...'''
date = "2015-04-07T05:59:00Z"
lastmod = "2015-04-07T06:15:00Z"
weight = 41247
keywords = [ "pcap", "wireshark" ]
aliases = [ "/questions/41247" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get a Number of frames in a saved pcap file ?](/questions/41247/how-to-get-a-number-of-frames-in-a-saved-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a simple doubt in Wireshark, in opening a saved capture file. here what I observed is, when we open the capture file (file-&gt;open), it will open the selected file. if the file is large then it will show a window to show some statistical information<img src="https://osqa-ask.wireshark.org/upfiles/process.JPG" alt="alt text" /></p><p>as the image shows, here my doubt is 1) How do we know the number of frames in the saved capture file?</p><p>2) It is showing Elapsed time and Time Left, how it is achieving?</p></div><div id="question-tags" class="tags-container tags">pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '15, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/74ab8994ff0e776c06c6b4f14f4dfca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sathish308&#39;s gravatar image" /><p>sathish308<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sathish308 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-41247" class="comments-container"></div><div id="comment-tools-41247" class="comment-tools"></div><div class="clear"></div><div id="comment-41247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41248"></span>

<div id="answer-container-41248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41248-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your screenshot is not a loading dialog, it's a frame processing dialog (e.g. when you apply a filter). After loading a capture file Wireshark knows how many packets are in the file, so that's easy. If you're loading a file Wireshark usually scans the file when you click on it in the file dialog and tries to determine some file details. If the file is too big it will abort that scan at some point.</p><p>Elapsed time and time left are most likely calculated based on the current read speed and the amount of remaining bytes Wireshark has to load.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41248" class="comments-container"><span id="41269"></span><div id="comment-41269" class="comment"><div id="post-41269-score" class="comment-score"></div><div class="comment-text"><p>Yes - "elapsed time" is just derived from the date-and-time-of-day clock values provided by the operating system, and "time left" is derived based on an assumption that the rate at which frames have been and will be read is constant, so if you've read 50 out of 100 frames, and it took 10 seconds, the remaining 50 frames should take another 10 seconds. The "time left" is recalculated as the process continues, so it gets adjusted as the rate of reading increases or decreases.</p><p>(When reading the file for the first time, Wireshark doesn't know how many frames there are, so it gives no estimate. It counts the frames as it reads the file for the first time, so it knows it after that.)</p></div><div id="comment-41269-info" class="comment-info"><span class="comment-age">(07 Apr '15, 20:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-41248" class="comment-tools"></div><div class="clear"></div><div id="comment-41248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

