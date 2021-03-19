+++
type = "question"
title = "Network keeps losing connection to internet."
description = '''Hello,  I&#x27;m new to using Wireshark. My issue is that the connection to the internet continues to drop. I have called Comcast and they tell me that all is good on there end. I have begun to capture packets from behind my Comcast modem using a Dualcom port mirroring switch and I&#x27;m able to capture that...'''
date = "2014-01-27T09:22:00Z"
lastmod = "2014-01-30T12:33:00Z"
weight = 29200
keywords = [ "capture" ]
aliases = [ "/questions/29200" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network keeps losing connection to internet.](/questions/29200/network-keeps-losing-connection-to-internet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29200-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm new to using Wireshark. My issue is that the connection to the internet continues to drop. I have called Comcast and they tell me that all is good on there end. I have begun to capture packets from behind my Comcast modem using a Dualcom port mirroring switch and I'm able to capture that packets. Can someone please offer any advice or suggestions on how to filter my capture to troubleshoot/find the issue?<br />
</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/679521f410a7bd2d90e57ad95cbb63b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wiich0&#39;s gravatar image" /><p>Wiich0<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wiich0 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29200" class="comments-container"><span id="29202"></span><div id="comment-29202" class="comment"><div id="post-29202-score" class="comment-score"></div><div class="comment-text"><p>Are you establishing a PPPoE session?</p></div><div id="comment-29202-info" class="comment-info"><span class="comment-age">(27 Jan '14, 11:38)</span> randyp</div></div><span id="29204"></span><div id="comment-29204" class="comment"><div id="post-29204-score" class="comment-score"></div><div class="comment-text"><blockquote><p>behind my Comcast modem</p></blockquote><p>'behind' the modem means towards the ISP or towards the LAN?</p></div><div id="comment-29204-info" class="comment-info"><span class="comment-age">(27 Jan '14, 12:04)</span> Kurt Knochner ♦</div></div><span id="29329"></span><div id="comment-29329" class="comment"><div id="post-29329-score" class="comment-score"></div><div class="comment-text"><p>By behind the modem I mean from the Comcast modem towards the LAN.<br />
</p></div><div id="comment-29329-info" class="comment-info"><span class="comment-age">(30 Jan '14, 12:11)</span> Wiich0</div></div><span id="29330"></span><div id="comment-29330" class="comment"><div id="post-29330-score" class="comment-score"></div><div class="comment-text"><p>By behind the modem I mean from the Comcast modem towards the LAN.</p></div><div id="comment-29330-info" class="comment-info"><span class="comment-age">(30 Jan '14, 12:12)</span> Wiich0</div></div></div><div id="comment-tools-29200" class="comment-tools"></div><div class="clear"></div><div id="comment-29200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29331"></span>

<div id="answer-container-29331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, then you won't see any 'connection drops' at the ISP side. You will only be able to watch the effects caused by a connection drop, but you will never know if it was the ISP link, the router or even the server on the Internet.</p><p>A better approach would to run Smokeping (Google that) and let it monitor several hosts on the Internet and some systems of the ISP. With the monitoring results you should be able to figure out if the link to the ISP is the problem or if the ISPs link to the Internet is part of the problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '14, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-29331" class="comments-container"></div><div id="comment-tools-29331" class="comment-tools"></div><div class="clear"></div><div id="comment-29331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

