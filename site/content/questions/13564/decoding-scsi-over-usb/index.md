+++
type = "question"
title = "decoding scsi over usb"
description = '''I am trying to analyse a conventional SCSI over USB stream (from a USB DVD drive, using Ubuntu 12.04). I have captured the trace using tcpdump, and Wireshark correctly displays the traffic at the USB command level, however in every case the SCSI payload is shown simply as &#x27;leftover capture data&#x27;. On...'''
date = "2012-08-12T03:46:00Z"
lastmod = "2013-07-31T09:55:00Z"
weight = 13564
keywords = [ "scsi", "usb" ]
aliases = [ "/questions/13564" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [decoding scsi over usb](/questions/13564/decoding-scsi-over-usb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13564-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyse a conventional SCSI over USB stream (from a USB DVD drive, using Ubuntu 12.04). I have captured the trace using tcpdump, and Wireshark correctly displays the traffic at the USB command level, however in every case the SCSI payload is shown simply as 'leftover capture data'. On inspection this data is clearly the wanted SCSI payload.</p><p>I have tried both the latest 1.8 and also 1.9 code (wireshark-1.8.0rc2, wireshark-1.9.0-SVN-44445) with identical outcome.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">scsi usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '12, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/23519174af58a085c31174f4deb75077?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hdb3&#39;s gravatar image" /><p>hdb3<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hdb3 has no accepted answers">0%</span></p></div></div><div id="comments-container-13564" class="comments-container"></div><div id="comment-tools-13564" class="comment-tools"></div><div class="clear"></div><div id="comment-13564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13569"></span>

<div id="answer-container-13569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13569-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, without seeing the capture, we can't really tell what the underlying problem is. The USB dissector will report stuff as "Leftover Capture Data" if:</p><ol><li>the URB says it's a "bulk transfer", "interrupt", or "control" packet, and it doesn't find an appropriate dissector for it;</li><li>the URB says it's an "isochronous" packet;</li><li>the URB doesn't say it's any of those.</li></ol><p>It might be failing to find an appropriate dissector due to a dissector bug.</p><p>Please file a bug at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and, if you can, attach a capture that shows the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '12, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13569" class="comments-container"></div><div id="comment-tools-13569" class="comment-tools"></div><div class="clear"></div><div id="comment-13569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23484"></span>

<div id="answer-container-23484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23484-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you start the capture <em>before</em> connecting device to your computer? One reason for leftover capture data would be lack of USB descriptors in capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/96637248dab9a269e98fbf0344e26a93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desowin&#39;s gravatar image" /><p>desowin<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desowin has no accepted answers">0%</span></p></div></div><div id="comments-container-23484" class="comments-container"></div><div id="comment-tools-23484" class="comment-tools"></div><div class="clear"></div><div id="comment-23484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

