+++
type = "question"
title = "how can I filter activity that is just between a PC and server, or between two servers?"
description = '''I&#x27;m brand new to WireShark. I simply want to evaluate the network activity between one user&#x27;s PC, and the application and data servers their session is communicating with. I have, or can get, the IP addresses for all.'''
date = "2013-10-30T13:14:00Z"
lastmod = "2013-10-30T13:26:00Z"
weight = 26550
keywords = [ "capture-filter-wlan" ]
aliases = [ "/questions/26550" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can I filter activity that is just between a PC and server, or between two servers?](/questions/26550/how-can-i-filter-activity-that-is-just-between-a-pc-and-server-or-between-two-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26550-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm brand new to WireShark. I simply want to evaluate the network activity between one user's PC, and the application and data servers their session is communicating with. I have, or can get, the IP addresses for all.</p></div><div id="question-tags" class="tags-container tags">capture-filter-wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/29319afe0978d94ea82d4a2829498366?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zorro&#39;s gravatar image" /><p>Zorro<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zorro has no accepted answers">0%</span></p></div></div><div id="comments-container-26550" class="comments-container"></div><div id="comment-tools-26550" class="comment-tools"></div><div class="clear"></div><div id="comment-26550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26551"></span>

<div id="answer-container-26551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26551-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display filter: ip.addr==192.168.1.1 &amp;&amp; ip.addr==192.168.1.10</p><p>Capture filter: host 192.168.1.1 and host 192.168.1.10</p><p>...substituting the correct IP addresses, of course.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-26551" class="comments-container"><span id="26552"></span><div id="comment-26552" class="comment"><div id="post-26552-score" class="comment-score"></div><div class="comment-text"><p>Just in case this is not clear: note that Wireshark will normally need to be run on one of the endpoints, (e.g., the user PC) to be able to capture traffic between that endpoint and other nodes.</p><p>There certainly are ways to capture traffic between various nodes on a network from a 3rd node, but they are more complicated.</p><p>See:</p><p><a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a></p></div><div id="comment-26552-info" class="comment-info"><span class="comment-age">(30 Oct '13, 13:55)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-26551" class="comment-tools"></div><div class="clear"></div><div id="comment-26551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

