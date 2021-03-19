+++
type = "question"
title = "SIP CID tracking"
description = '''I would like to sniff the WAN for a SIP trunk that is sending CID information to my customer. I have downloaded the Sniffer and have a HUB that I can capture the packets. What should I look for and how can I read the information that I receive? Is there a program routine that would help me?'''
date = "2014-01-06T12:00:00Z"
lastmod = "2014-01-06T14:52:00Z"
weight = 28606
keywords = [ "sipcid" ]
aliases = [ "/questions/28606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP CID tracking](/questions/28606/sip-cid-tracking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to sniff the WAN for a SIP trunk that is sending CID information to my customer. I have downloaded the Sniffer and have a HUB that I can capture the packets. What should I look for and how can I read the information that I receive? Is there a program routine that would help me?</p></div><div id="question-tags" class="tags-container tags">sipcid</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '14, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/db3b83af165cff64ec41b4f3dbe6472a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fonedoc&#39;s gravatar image" /><p>Fonedoc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fonedoc has no accepted answers">0%</span></p></div></div><div id="comments-container-28606" class="comments-container"></div><div id="comment-tools-28606" class="comment-tools"></div><div class="clear"></div><div id="comment-28606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28608"></span>

<div id="answer-container-28608" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28608-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once you connect a computer to the hub to receive the traffic, you'll need to capture it and read it. Your question is a little bit open-ended, so I'll recommend looking over the Wireshark user manual as a base: <a href="http://www.wireshark.org/download/docs/user-guide-us.pdf">http://www.wireshark.org/download/docs/user-guide-us.pdf</a></p><p>Section 4 of the manual goes over how to capture the traffic, and section 6.3 goes over packet filtering. For filtering, just use the filter "sip" in the filter box to see only the SIP packets. From there, you can click on a packet to see all the fields and values, including SIP fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '14, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-28608" class="comments-container"></div><div id="comment-tools-28608" class="comment-tools"></div><div class="clear"></div><div id="comment-28608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

