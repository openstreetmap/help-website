+++
type = "question"
title = "Filtering pcap file"
description = '''Hello, is it possible to make in wireshark/tshark a filter which display all packet with response? I have a file with DHCPv6 packets, for example in this file is 100 Solicit packets (dhcpv6.msgtype==1) but only 50 packets with Advertise packets (msgtype==2). A common part of these packets is transac...'''
date = "2016-01-02T12:21:00Z"
lastmod = "2016-01-02T14:02:00Z"
weight = 48795
keywords = [ "filter", "wireshark" ]
aliases = [ "/questions/48795" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering pcap file](/questions/48795/filtering-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48795-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, is it possible to make in wireshark/tshark a filter which display all packet with response? I have a file with DHCPv6 packets, for example in this file is 100 Solicit packets (dhcpv6.msgtype==1) but only 50 packets with Advertise packets (msgtype==2). A common part of these packets is transaction id (dhcpv6.xid) and I would like to display this 50 Solicit packets and 50 Advertise packets with this common part (xid). Is it possible?</p></div><div id="question-tags" class="tags-container tags">filter wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '16, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/5a74bb5e2a46cd343fd29fc5fa2b182b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razz9&#39;s gravatar image" /><p>razz9<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razz9 has no accepted answers">0%</span></p></div></div><div id="comments-container-48795" class="comments-container"></div><div id="comment-tools-48795" class="comment-tools"></div><div class="clear"></div><div id="comment-48795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48799"></span>

<div id="answer-container-48799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, not directly with the current dhcpv6 dissector, because unlike some other dissectors, it does not provide the frame cross-reference pseudo-fields.</p><p>The display filters only evaluate fields of a single frame, so they cannot handle inter-packet relationships unless the dissector generates the pseudo-fields representing such relationships.</p><p>You should be able to fulfil your goal using <a href="https://wiki.wireshark.org/Mate">MATE</a>, though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '16, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48799" class="comments-container"></div><div id="comment-tools-48799" class="comment-tools"></div><div class="clear"></div><div id="comment-48799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

