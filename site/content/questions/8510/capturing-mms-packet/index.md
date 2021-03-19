+++
type = "question"
title = "capturing mms packet"
description = '''What setting we have to do to capture mms(manufacturing message specification) on wire shark?'''
date = "2012-01-20T05:04:00Z"
lastmod = "2012-01-20T17:02:00Z"
weight = 8510
keywords = [ "mms" ]
aliases = [ "/questions/8510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing mms packet](/questions/8510/capturing-mms-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What setting we have to do to capture mms(manufacturing message specification) on wire shark?</p></div><div id="question-tags" class="tags-container tags">mms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '12, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/b8b70dd240bd3fbc80f3d3cf1c4fb225?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tod&#39;s gravatar image" /><p>tod<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tod has no accepted answers">0%</span></p></div></div><div id="comments-container-8510" class="comments-container"></div><div id="comment-tools-8510" class="comment-tools"></div><div class="clear"></div><div id="comment-8510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8525"></span>

<div id="answer-container-8525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The same settings you need to capture any other type of traffic; the only way the protocol would matter when <em>capturing</em> traffic would be if you were using a capture filter. The Wireshark dissector for MMS expects it to run atop the OSI Connection-Oriented Transport Protocol (COTP), and that's expected to run atop the OSI Connectionless Network Protocol, the TPKT protocol atop TCP, X.25, or IPv4/IPv6. If you're using a capture filter, it would have to be one that would see the traffic with whatever encapsulation is being used.</p><p>Note, however, that just because Wireshark <em>captures</em> a particular protocol, that doesn't mean it'll <em>recognize</em> the traffic as being that protocol. If you're not seeing that traffic in Wireshark, it might be because it's not recognizing the MMS traffic; see, for example, <a href="http://ask.wireshark.org/questions/6298/wireshark-cannot-dissect-mms-packets-that-dont-begin-with-initiate">this other question wherein somebody wasn't seeing MMS traffic when they should have been</a> - the problem was that Wireshark didn't see the initiate-request and initiate-response packets so it didn't have enough context information to realize that the protocol running atop the OSI Presentation Protocol was MMS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8525" class="comments-container"></div><div id="comment-tools-8525" class="comment-tools"></div><div class="clear"></div><div id="comment-8525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

