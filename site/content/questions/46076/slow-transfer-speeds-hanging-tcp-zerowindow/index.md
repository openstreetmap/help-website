+++
type = "question"
title = "Slow Transfer Speeds / Hanging - TCP ZeroWindow"
description = '''Hi All, Looking at the attached diagram - My server is IP 10.x.x.x and the client is on 172.x.x.x. 10.x.x.x Server sits in Our DataCentre. The PC on 172.x.x.x is a DMVPN Site I have complaints from users at this site when using a system to upload/download files. I have about 20 other sites who use t...'''
date = "2015-09-23T06:32:00Z"
lastmod = "2015-09-23T09:51:00Z"
weight = 46076
keywords = [ "slow", "zero-window", "tcp" ]
aliases = [ "/questions/46076" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Transfer Speeds / Hanging - TCP ZeroWindow](/questions/46076/slow-transfer-speeds-hanging-tcp-zerowindow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46076-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Looking at the attached diagram - My server is IP 10.x.x.x and the client is on 172.x.x.x.</p><p>10.x.x.x Server sits in Our DataCentre. The PC on 172.x.x.x is a DMVPN Site</p><p>I have complaints from users at this site when using a system to upload/download files. I have about 20 other sites who use the system also with no complaints. Bandwidth Utilization at the sites is not saturated.</p><p>Looking at the screenshot - does this suggest that it is my server having buffer issues? (10.44.145.196)? Trying to decipher what the actual messages are telling me.</p><p>Thanks<img src="https://osqa-ask.wireshark.org/upfiles/tcpzero.JPG" alt="alt text" /></p><p>![alt text][2]</p></div><div id="question-tags" class="tags-container tags">slow zero-window tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/a28bceae0effe0ec1130bab7cb87a4e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exit12&#39;s gravatar image" /><p>exit12<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exit12 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '15, 06:33</p></div></div><div id="comments-container-46076" class="comments-container"></div><div id="comment-tools-46076" class="comment-tools"></div><div class="clear"></div><div id="comment-46076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46079"></span>

<div id="answer-container-46079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46079-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes your Server has a full receive window and the client tests if the window is still at the zero size. What is the OS at the server?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '15, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-46079" class="comments-container"><span id="46099"></span><div id="comment-46099" class="comment"><div id="post-46099-score" class="comment-score"></div><div class="comment-text"><p>Hi Christian,</p><p>The server side is actually a Linux machine I believe. I've attached another screenshot from the conversation as I just want to understand what each part means.</p><p>Looking at packet 4248 - it looks like the server reports a TCP Zero window. What does the 8010 - 63607 numbers represent/mean? Also seen in packet 4305, 4509, 4788.</p><p>Thanks<img src="https://osqa-ask.wireshark.org/upfiles/zeronew.JPG" alt="alt text" /></p></div><div id="comment-46099-info" class="comment-info"><span class="comment-age">(24 Sep '15, 02:27)</span> exit12</div></div><span id="46120"></span><div id="comment-46120" class="comment"><div id="post-46120-score" class="comment-score"></div><div class="comment-text"><p>8010 is the Source Port and 63607 is the Destination Port of that packet.</p></div><div id="comment-46120-info" class="comment-info"><span class="comment-age">(24 Sep '15, 11:38)</span> Christian_R</div></div></div><div id="comment-tools-46079" class="comment-tools"></div><div class="clear"></div><div id="comment-46079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

