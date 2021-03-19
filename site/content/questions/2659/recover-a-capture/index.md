+++
type = "question"
title = "Recover a capture"
description = '''Hello, Yesterday I started a capture at 8:42 am. This morning at 9am I wanted to watch the capture but everything has been cleared and the capture has begun at 8:42 this morning. How to retrieve the capture yesterday? Sorry for my bad english ;) Thanks'''
date = "2011-03-04T00:57:00Z"
lastmod = "2011-03-04T09:19:00Z"
weight = 2659
keywords = [ "capture", "history" ]
aliases = [ "/questions/2659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Recover a capture](/questions/2659/recover-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Yesterday I started a capture at 8:42 am. This morning at 9am I wanted to watch the capture but everything has been cleared and the capture has begun at 8:42 this morning. How to retrieve the capture yesterday?</p><p>Sorry for my bad english ;)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture history</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '11, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/116c7ecceb1d27d4e9d21c0ed7ae2008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chandler124&#39;s gravatar image" /><p>chandler124<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chandler124 has no accepted answers">0%</span></p></div></div><div id="comments-container-2659" class="comments-container"></div><div id="comment-tools-2659" class="comment-tools"></div><div class="clear"></div><div id="comment-2659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2664"></span>

<div id="answer-container-2664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2664-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark starts the command line tool <strong>dumpcap</strong> to record traffic in the background. dumpcap writes the recorded traffic into your temp directory. The exact location depends on your operating system:</p><ul><li>For Windows Vista / Win 7: <strong>C:\Users\username\AppData\Local\Temp</strong></li><li>For Windows XP and earlier: <strong>C:\Documents and Settings\username\Application DataWireshark</strong></li><li>For Linux / Unix: <strong>/home/username/.wireshark</strong></li></ul><p>If Wireshark crashed - probably because 24 hours of traffic don't fit into memory - you have a good chance to find the file written by dumpcap file in the temp directory. Look for files like etherXXXX1234</p><p>Despite a missing file extension this is your capture file. If it is too big to load in Wireshark try chopping it up with editcap.</p><p>If no etherXXXX file is present it got deleted for whatever reason. Try to run an undelete tool to get it back from the grave yard. This is an art in itself and probably beyond the scope of this forum.</p><p>For a long term capture operation try this:</p><ul><li>Capture -&gt; Options</li><li>Specify a file name</li><li>check "use multiple files"</li><li>Get a new trace file every 64 or 128 MB</li><li>Uncheck the "Ring buffer" option</li><li>In the section "Stop capture" check "... after" and select 24 hours</li></ul><p>Don't forget to deactivate all power saving options that might put your PC to sleep mode.</p><p>Good hunting - Use multiple files</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '11, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '11, 09:34</p></div></div><div id="comments-container-2664" class="comments-container"><span id="2665"></span><div id="comment-2665" class="comment"><div id="post-2665-score" class="comment-score"></div><div class="comment-text"><p>your backslashes got removed from the paths because they're used to "escape" other things. I think you need to do double backslashes instead, not sure.</p></div><div id="comment-2665-info" class="comment-info"><span class="comment-age">(04 Mar '11, 09:25)</span> Jasper ♦♦</div></div><span id="2666"></span><div id="comment-2666" class="comment"><div id="post-2666-score" class="comment-score"></div><div class="comment-text"><p>And it looked so nice in the preview. Double backslash did the job. Thx for the hint.</p></div><div id="comment-2666-info" class="comment-info"><span class="comment-age">(04 Mar '11, 09:35)</span> packethunter</div></div></div><div id="comment-tools-2664" class="comment-tools"></div><div class="clear"></div><div id="comment-2664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

