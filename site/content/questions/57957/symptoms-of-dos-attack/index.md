+++
type = "question"
title = "Symptoms of DOS attack"
description = '''Hi i have a packet capture of a attack on our network. It was reported that users felt the network was slow for many applications and the internet. Upon starting the capture we notice the network was back to normal. I notice many ACK packet which might be normal attack but I read somewhere many ACK ...'''
date = "2016-12-08T04:09:00Z"
lastmod = "2016-12-08T04:53:00Z"
weight = 57957
keywords = [ "dos" ]
aliases = [ "/questions/57957" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Symptoms of DOS attack](/questions/57957/symptoms-of-dos-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57957-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have a packet capture of a attack on our network. It was reported that users felt the network was slow for many applications and the internet. Upon starting the capture we notice the network was back to normal. I notice many ACK packet which might be normal attack but I read somewhere many ACK packet can also be DOS attack. Without the packet capture from earlier, how do i tell the difference between a normal traffic data flow and after attack from DOS ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/DOS_attack.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '16, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p>doran_lum<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57957" class="comments-container"></div><div id="comment-tools-57957" class="comment-tools"></div><div class="clear"></div><div id="comment-57957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57959"></span>

<div id="answer-container-57959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57959-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wouldn't call it as an attack. But of course you can. What you see is bandwidth consuming traffic to the internet on port 9001 (TOR). The difference of normal and not normal traffic can be only find by baseline and then defining rules out of that. And in the end you can close a lot of ports which you don't need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '16, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '16, 23:21</p></div></div><div id="comments-container-57959" class="comments-container"></div><div id="comment-tools-57959" class="comment-tools"></div><div class="clear"></div><div id="comment-57959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

