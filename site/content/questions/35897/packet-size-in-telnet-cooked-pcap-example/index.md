+++
type = "question"
title = "Packet size in telnet-cooked .pcap example"
description = '''Hi Experts,  I see in your example cap (telnet-cooked.pcap), in packet number 18 the packet size in IP header is 137 Bytes, but real length of the packet is 66 Bytes. Is it O.K. or this is a mistake? Thanks'''
date = "2014-08-31T07:09:00Z"
lastmod = "2014-08-31T13:13:00Z"
weight = 35897
keywords = [ "cooked", "telnet" ]
aliases = [ "/questions/35897" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet size in telnet-cooked .pcap example](/questions/35897/packet-size-in-telnet-cooked-pcap-example)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35897-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts, I see in your example cap (telnet-cooked.pcap), in packet number 18 the packet size in IP header is 137 Bytes, but real length of the packet is 66 Bytes. Is it O.K. or this is a mistake?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">cooked telnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/8b8fda32ce3802bbb0e84d9b81bf02e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cskovec&#39;s gravatar image" /><p>cskovec<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cskovec has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 31 Aug '14, 07:51</p></div></div><div id="comments-container-35897" class="comments-container"></div><div id="comment-tools-35897" class="comment-tools"></div><div class="clear"></div><div id="comment-35897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35898"></span>

<div id="answer-container-35898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35898-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's apparently a failure, as the IP frame can't be larger than the whole frame itself (see Frame layer). If you look at frame #17, you'll notice that it's the same frame as #18 (same IP ID, all the rest identical), but this time <strong>with the correct size</strong> in the IP header.</p><p>This happens twice in the capture file (filter: ip.len &gt; frame.cap_len), so it looks like a problem on the system where the capture file was taken.</p><p>Good spot!!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '14, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '14, 13:14</p></div></div><div id="comments-container-35898" class="comments-container"></div><div id="comment-tools-35898" class="comment-tools"></div><div class="clear"></div><div id="comment-35898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

