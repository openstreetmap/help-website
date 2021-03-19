+++
type = "question"
title = "Preamble frame capture"
description = '''Is it possible to configure wireshark to capture also the preamble and the SFD bytes of a ethernet frame? If affirmative, how to do this capture? Best regards '''
date = "2010-10-25T07:04:00Z"
lastmod = "2010-10-25T19:12:00Z"
weight = 620
keywords = [ "sfd", "preamble" ]
aliases = [ "/questions/620" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Preamble frame capture](/questions/620/preamble-frame-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-620-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to configure wireshark to capture also the preamble and the SFD bytes of a ethernet frame? If affirmative, how to do this capture?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">sfd preamble</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/1689386727cf8cabe8bbc1db88b9a8ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kzxc&#39;s gravatar image" /><p>kzxc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kzxc has no accepted answers">0%</span></p></div></div><div id="comments-container-620" class="comments-container"><span id="621"></span><div id="comment-621" class="comment"><div id="post-621-score" class="comment-score"></div><div class="comment-text"><p>Apparantly not.<br />
See the <a href="http://wiki.wireshark.org">Wireshark Wiki</a>: <a href="http://wiki.wireshark.org/Ethernet#Packet_format">Ethernet</a> -&gt; Packet format.</p></div><div id="comment-621-info" class="comment-info"><span class="comment-age">(25 Oct '10, 07:54)</span> joke</div></div><span id="624"></span><div id="comment-624" class="comment"><div id="post-624-score" class="comment-score"></div><div class="comment-text"><p>Nope - but I wonder... why do you need to capture the preamble/SFD? Interesting question.</p></div><div id="comment-624-info" class="comment-info"><span class="comment-age">(25 Oct '10, 09:03)</span> lchappell ♦</div></div><span id="647"></span><div id="comment-647" class="comment"><div id="post-647-score" class="comment-score"></div><div class="comment-text"><p>I have some old Sniffer boards around here somewhere... clearing off cobwebs in a rarely-visited corner of the office...</p></div><div id="comment-647-info" class="comment-info"><span class="comment-age">(25 Oct '10, 20:38)</span> lchappell ♦</div></div></div><div id="comment-tools-620" class="comment-tools"></div><div class="clear"></div><div id="comment-620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="645"></span>

<div id="answer-container-645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-645-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'd probably need specialized hardware to capture the preamble and SFD; I think most Ethernet adapters will not provide that to the host, no matter how politely the adapter's driver would like to ask it. :-) I don't know what hardware is available to capture that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-645" class="comments-container"></div><div id="comment-tools-645" class="comment-tools"></div><div class="clear"></div><div id="comment-645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

