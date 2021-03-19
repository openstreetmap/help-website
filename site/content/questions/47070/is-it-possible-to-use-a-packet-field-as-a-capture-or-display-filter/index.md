+++
type = "question"
title = "Is it possible to use a packet field as a capture or display filter??"
description = '''I want to use the Bridge Priority field in a BPDU packet as a capture or display filter, is it possible?? How can I do it?? '''
date = "2015-10-29T08:39:00Z"
lastmod = "2015-10-29T08:55:00Z"
weight = 47070
keywords = [ "filter", "field", "bpdu" ]
aliases = [ "/questions/47070" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to use a packet field as a capture or display filter??](/questions/47070/is-it-possible-to-use-a-packet-field-as-a-capture-or-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47070-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use the <strong>Bridge Priority</strong> field in a <strong>BPDU</strong> packet as a capture or display filter, is it possible?? How can I do it??</p><p><img src="https://osqa-ask.wireshark.org/upfiles/q1.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">filter field bpdu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/8752544ec453a6d8e08fdde4d465eca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MehranBazgir&#39;s gravatar image" /><p>MehranBazgir<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MehranBazgir has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47070" class="comments-container"></div><div id="comment-tools-47070" class="comment-tools"></div><div class="clear"></div><div id="comment-47070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47071"></span>

<div id="answer-container-47071" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47071-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Highlight the Bridge Priority field in Wireshark's Packet Details pane, and then look down to the status bar to see the field name, which for regular STP will be "stp.bridge.prio". You can use that in a display filter. Or, to find the field name even if you can't find a field in a packet, click on the "Expressions" button on the display filter toolbar, scroll down to the protocol, STP in this case, and you will see all the fields/expressions you can use in display filters listed there.</p><p>There is no capture filter keyword for the Bridge Priority field, however, if the bridge priority field is always found at a fixed offset from the start of the frame, you could build a capture filter using byte-offset notation. See the <a href="http://www.tcpdump.org/tcpdump_man.html">tcpdump man page</a> for complete capture filter syntax.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-47071" class="comments-container"></div><div id="comment-tools-47071" class="comment-tools"></div><div class="clear"></div><div id="comment-47071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

