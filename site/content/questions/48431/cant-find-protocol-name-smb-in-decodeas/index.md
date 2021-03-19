+++
type = "question"
title = "Can&#x27;t find protocol name SMB in DecodeAs"
description = '''I have a pcap with SMB traffic on port 80. Tried to decode it for SMB but can&#x27;t find the protocol name &quot;SMB&quot; by using &quot;DecodeAs&quot;. See the attached snapshot.  My Wireshark has Version 1.10.6. '''
date = "2015-12-10T12:50:00Z"
lastmod = "2015-12-10T13:24:00Z"
weight = 48431
keywords = [ "wireshark" ]
aliases = [ "/questions/48431" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't find protocol name SMB in DecodeAs](/questions/48431/cant-find-protocol-name-smb-in-decodeas)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48431-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a <a href="https://github.com/aol/moloch/blob/master/tests/pcap/smb-port80.pcap?raw=true">pcap</a> with SMB traffic on port 80. Tried to decode it for SMB but can't find the protocol name "SMB" by using "DecodeAs". See the attached snapshot. <img src="https://osqa-ask.wireshark.org/upfiles/3.png" alt="SMB" /></p><p>My Wireshark has Version 1.10.6.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '15, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></img></div></div><div id="comments-container-48431" class="comments-container"></div><div id="comment-tools-48431" class="comment-tools"></div><div class="clear"></div><div id="comment-48431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48432"></span>

<div id="answer-container-48432" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48432-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The reason is that SMB (and SMB2) are client protocols of NBSS, not directly of TCP. If you know that your packet is a SMB packet using non-standard TCP ports, set "Decode as" protocol to NBSS, and Wireshark will find SMB inside it automatically.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '15, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48432" class="comments-container"><span id="48433"></span><div id="comment-48433" class="comment"><div id="post-48433-score" class="comment-score"></div><div class="comment-text"><p>Thanks @sindy. It works great!</p></div><div id="comment-48433-info" class="comment-info"><span class="comment-age">(10 Dec '15, 13:26)</span> pktUser1001</div></div></div><div id="comment-tools-48432" class="comment-tools"></div><div class="clear"></div><div id="comment-48432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

