+++
type = "question"
title = "missing SMTP traffic"
description = '''I&#x27;m trying to debug a connection issue with network printer that is refusing to connect to a specific smtp server. While capturing from the same switch that the printer is connected to I can see packets coming up and down but, even smtp communication with &quot;other smtp servers&quot; but NOT to this particu...'''
date = "2012-01-31T06:37:00Z"
lastmod = "2012-02-01T07:03:00Z"
weight = 8729
keywords = [ "smtp", "missing" ]
aliases = [ "/questions/8729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [missing SMTP traffic](/questions/8729/missing-smtp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to debug a connection issue with network printer that is refusing to connect to a specific smtp server. While capturing from the same switch that the printer is connected to I can see packets coming up and down but, even smtp communication with "other smtp servers" but NOT to this particular one. the smtp server is alive as I can ping it and telnet it to port 25, and I can even send mails from email clients and all this will be visible with wireshark, not the failed connection to the problematic smtp.server4 I found that when the printer connect to the other smtp servers the packet length is 1514 so I suspected an mtu issue, but shouldn't I be able to see the the requests from mac source at least?</p></div><div id="question-tags" class="tags-container tags">smtp missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '12, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/cd1cbda04ce8b94557cce44c96a39338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="D10221&#39;s gravatar image" /><p>D10221<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="D10221 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jan '12, 09:20</p></div></div><div id="comments-container-8729" class="comments-container"><span id="8736"></span><div id="comment-8736" class="comment"><div id="post-8736-score" class="comment-score"></div><div class="comment-text"><p>Is the printer configured with the SMTP server's name, or its IP address? If name, do you see a DNS query from the printer? If so, does it get a successful response?</p><p>Do you see an ARP request from the printer for the SMTP server's IP address? (You might need to power-cycle the printer in order to clear its ARP cache.)</p><p>1,514 bytes is a common frame size on networks that do not have jumbo frames enabled, so it's probably not an MTU issue.</p></div><div id="comment-8736-info" class="comment-info"><span class="comment-age">(31 Jan '12, 13:11)</span> Jim Aragon</div></div><span id="8737"></span><div id="comment-8737" class="comment"><div id="post-8737-score" class="comment-score"></div><div class="comment-text"><p>Thanks jim, ip or host name made no difference, I can see http,icmp,and the printer services,even ipx traffic and arp traffic just before the smtp functions, and i can confirm from my laptop the smtp server won't answer pings with packets larger than 1464 bytes. no arp request seen from the moment I try smtp application until I use other services (http,ping,etc)</p></div><div id="comment-8737-info" class="comment-info"><span class="comment-age">(31 Jan '12, 19:25)</span> D10221</div></div></div><div id="comment-tools-8729" class="comment-tools"></div><div class="clear"></div><div id="comment-8729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8745"></span>

<div id="answer-container-8745" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8745-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The real and deep reason why I couldn't see the specific smtp packets is still escaping to me, but it was solved hooking up an old hub instead of a switch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '12, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/cd1cbda04ce8b94557cce44c96a39338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="D10221&#39;s gravatar image" /><p>D10221<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="D10221 has no accepted answers">0%</span></p></div></div><div id="comments-container-8745" class="comments-container"></div><div id="comment-tools-8745" class="comment-tools"></div><div class="clear"></div><div id="comment-8745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

