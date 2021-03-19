+++
type = "question"
title = "Prevent capture of file contents"
description = '''I&#x27;m running a test that transfers large files on/off the test machine (which is running Wireshark). Need to run overnight (cycles files every 30 minutes) and the logging in Wireshark fills the machine too quickly and makes Wireshark unusable. I&#x27;d like to filter all file contents (but maintain the tr...'''
date = "2016-10-17T13:16:00Z"
lastmod = "2016-10-17T22:19:00Z"
weight = 56477
keywords = [ "large", "transfer", "filter", "file" ]
aliases = [ "/questions/56477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Prevent capture of file contents](/questions/56477/prevent-capture-of-file-contents)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56477-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running a test that transfers large files on/off the test machine (which is running Wireshark). Need to run overnight (cycles files every 30 minutes) and the logging in Wireshark fills the machine too quickly and makes Wireshark unusable.</p><p>I'd like to filter all file contents (but maintain the transfer time for the file copy), before it gets captured. I'm trying to isolate the network traffic when the file transfers intermittently take much longer than expected.</p><p>Any suggestions or pointers to filter file contents on the way into the log are appreciated.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">large transfer filter file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/6892e0984829a3e6a084191da7f659e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WayneConnection&#39;s gravatar image" /><p>WayneConnection<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WayneConnection has no accepted answers">0%</span></p></div></div><div id="comments-container-56477" class="comments-container"><span id="56479"></span><div id="comment-56479" class="comment"><div id="post-56479-score" class="comment-score"></div><div class="comment-text"><p>Can you please clarify your question?</p><p>Are you asking for how to isolate only the packets of interest in order to limit the amount of data captured, or are you trying to run Wireshark for only as long as it takes for the file transfer to occur and then stop capturing and only retain the file if the time exceeded some threshold for data transfer? Or are you looking to do something else?</p></div><div id="comment-56479-info" class="comment-info"><span class="comment-age">(17 Oct '16, 16:45)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-56477" class="comment-tools"></div><div class="clear"></div><div id="comment-56477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56482"></span>

<div id="answer-container-56482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56482-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is the option to set the snap length on the interface you capture on to less than the default value of 65535. This allows you to keep the start of all packets (retaining timing and header info) while leaving (most of the) payload (file data) for what it is. This limits the capture file size. You'll have to tune this parameter to your particular needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56482" class="comments-container"><span id="56494"></span><div id="comment-56494" class="comment"><div id="post-56494-score" class="comment-score"></div><div class="comment-text"><p>Cmaynard: I was looking "how to isolate only the packets of interest in order to limit the amount of data captured" - thanks for the follow-up</p><p>Jaap: This did the trick. Thanks for both your quick responses, I'm new to wireshark and this saved lots of time.</p></div><div id="comment-56494-info" class="comment-info"><span class="comment-age">(18 Oct '16, 05:55)</span> WayneConnection</div></div></div><div id="comment-tools-56482" class="comment-tools"></div><div class="clear"></div><div id="comment-56482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

