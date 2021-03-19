+++
type = "question"
title = "Too many retransmission packets defect - ok or bad?"
description = '''Hello,  We got pcaps from our customer in between their application server and Database server. It was noticed that there were too many retransmission packets sent in between them. Is this something to be bothered about or is this normal tcp.analysis.lost_segment filter too showed lots of segment lo...'''
date = "2016-08-18T11:03:00Z"
lastmod = "2016-08-18T11:44:00Z"
weight = 54959
keywords = [ "unseen_segment", "retransmission" ]
aliases = [ "/questions/54959" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Too many retransmission packets defect - ok or bad?](/questions/54959/too-many-retransmission-packets-defect-ok-or-bad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54959-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We got pcaps from our customer in between their application server and Database server. It was noticed that there were too many retransmission packets sent in between them. Is this something to be bothered about or is this normal</p><p>tcp.analysis.lost_segment filter too showed lots of segment loss, sent by APP to DB . What does this mean, app is slower or DB is slower.</p><p>Since it is customer's pcaps I am not uploading the file but attaching few screenshots without the IPs, the port 50002 belongs to Database and other ports seen in the screenshot belongs to the application.</p><p>This is seen almost throughout the trace, and re-transmissions almost every packet <img src="https://osqa-ask.wireshark.org/upfiles/One-1_65nioLX.jpg" alt="alt text" /></p><p>Lost segments - packets sent from App to DB (with tcp.analysis.lost_segment filter) <img src="https://osqa-ask.wireshark.org/upfiles/lostSegment_1_h5qMWHi.jpg" alt="alt text" /></p><p>Lost segments - packets sent from App to DB (with tcp.analysis.lost_segment filter) <img src="https://osqa-ask.wireshark.org/upfiles/lostSegment_2_Pzlh8FO.jpg" alt="alt text" /></p><p>Lost segments - packets sent DB to App this time (with tcp.analysis.lost_segment filter) <img src="https://osqa-ask.wireshark.org/upfiles/lostSegment_3_DataBaseTOApplication_aSMmWKR.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">unseen_segment retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/ab3cec7a65e9f6482c02f8efe91a0b95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnishFromBangalore&#39;s gravatar image" /><p>AnishFromBan...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnishFromBangalore has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '16, 02:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-54959" class="comments-container"></div><div id="comment-tools-54959" class="comment-tools"></div><div class="clear"></div><div id="comment-54959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54960"></span>

<div id="answer-container-54960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54960-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seems, that you have captured all packets twice. Please use:</p><pre><code>editcap -d</code></pre><p>to remove the double captured packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-54960" class="comments-container"></div><div id="comment-tools-54960" class="comment-tools"></div><div class="clear"></div><div id="comment-54960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

