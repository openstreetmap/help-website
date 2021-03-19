+++
type = "question"
title = "using wireshark to debug http traffic on a non standard port"
description = '''I am debugging a web application that runs on a non standard http port, and because of this I do not get any HTTP packets in wireshark. Is there some way to have WS decode these packets as HTTP?'''
date = "2011-09-12T13:37:00Z"
lastmod = "2011-09-12T13:51:00Z"
weight = 6294
keywords = [ "http" ]
aliases = [ "/questions/6294" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [using wireshark to debug http traffic on a non standard port](/questions/6294/using-wireshark-to-debug-http-traffic-on-a-non-standard-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6294-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am debugging a web application that runs on a non standard http port, and because of this I do not get any HTTP packets in wireshark. Is there some way to have WS decode these packets as HTTP?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/e7c938d8e53e63895278d9f5aa65027a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaylill&#39;s gravatar image" /><p>jaylill<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaylill has no accepted answers">0%</span></p></div></div><div id="comments-container-6294" class="comments-container"></div><div id="comment-tools-6294" class="comment-tools"></div><div class="clear"></div><div id="comment-6294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6295"></span>

<div id="answer-container-6295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6295-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right click on of the packets in the capture, select "Decode As ...", on the transport tab choose the appropriate port that the server is sitting on and then select HTTP in the protocol list, then click OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6295" class="comments-container"></div><div id="comment-tools-6295" class="comment-tools"></div><div class="clear"></div><div id="comment-6295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

