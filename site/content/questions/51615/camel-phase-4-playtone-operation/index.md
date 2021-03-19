+++
type = "question"
title = "CAMEL Phase 4 PlayTone Operation"
description = '''Hi Does anyone have a Wireshark compatible trace of a CAMEL Phase 4 voice call containing the PlayTone CAMEL operation (operation code 97). I am analysing a trace which contains the PlayTone operation but Wireshark is showing a &quot;Malformed PAcket&quot; error where the &quot;Burst&quot; parameter appears to be locat...'''
date = "2016-04-12T17:40:00Z"
lastmod = "2016-04-13T01:37:00Z"
weight = 51615
keywords = [ "packet-camel", "camel" ]
aliases = [ "/questions/51615" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CAMEL Phase 4 PlayTone Operation](/questions/51615/camel-phase-4-playtone-operation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51615-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Does anyone have a Wireshark compatible trace of a CAMEL Phase 4 voice call containing the PlayTone CAMEL operation (operation code 97). I am analysing a trace which contains the PlayTone operation but Wireshark is showing a "Malformed PAcket" error where the "Burst" parameter appears to be located.</p><p>Not sure if the operation is actually incorrectly encoded or if this is a Wireshark bug. I have completed a manual ASN.1 decode and I believe the encoding is correct. Access to another trace would be very helpful in confirming.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">packet-camel camel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/9950b586de4a4eddba13f29fa07f80d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiamRed&#39;s gravatar image" /><p>LiamRed<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiamRed has no accepted answers">0%</span></p></div></div><div id="comments-container-51615" class="comments-container"></div><div id="comment-tools-51615" class="comment-tools"></div><div class="clear"></div><div id="comment-51615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51623"></span>

<div id="answer-container-51623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51623-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check <a href="https://ask.wireshark.org/questions/50998/issue-decoding-inap-systemfailure-parameter">this older question</a> which deals with a similar topic, and try to open your capture using the <a href="https://wireshark.org/download/automated/">current automated build</a>.</p><p>If that helps, it is enough to wait until the existing fix bubbles through to the next stable version (and use the automated build until then).</p><p>If it doesn't help, please publish the capture (it is enough if it contains the single packet of interest, use <code>File -&gt; Export Specified Packets</code> if you have some privacy concerns) somewhere (cloudshark, google drive, MS one drive, whatever) login-free and edit your Question with a link to it. It may turn out to be a bug which needs to be <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">filed</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51623" class="comments-container"></div><div id="comment-tools-51623" class="comment-tools"></div><div class="clear"></div><div id="comment-51623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

