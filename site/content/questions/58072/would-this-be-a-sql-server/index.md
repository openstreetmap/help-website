+++
type = "question"
title = "Would this be a SQL server ?"
description = '''Hi, I was wondering usually SQL communication should be on port 14333. by filter using &quot;browser&quot;, there&#x27;s some indication of SQL services. Is 192.168.255.255 a SQL server ?  Are the clients broadcasting to look for SQL services ? '''
date = "2016-12-14T03:51:00Z"
lastmod = "2016-12-14T05:36:00Z"
weight = 58072
keywords = [ "sql" ]
aliases = [ "/questions/58072" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Would this be a SQL server ?](/questions/58072/would-this-be-a-sql-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was wondering usually SQL communication should be on port 14333. by filter using "browser", there's some indication of SQL services. Is 192.168.255.255 a SQL server ?</p><p>Are the clients broadcasting to look for SQL services ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/sql.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p>doran_lum<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58072" class="comments-container"></div><div id="comment-tools-58072" class="comment-tools"></div><div class="clear"></div><div id="comment-58072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58075"></span>

<div id="answer-container-58075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58075-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol is the <a href="https://technet.microsoft.com/en-us/library/cc737661%28v=ws.10%29.aspx?f=255&amp;MSPPError=-2147217396">Microsoft Computer Browser service</a>, and that specific message is a master browser annonuncement sent by the elected local master browser, which is usually done by a server if there's one in the workgroup\domain. Such announcements carry a set of bit flags indicating the server type, one of which is SQL server.</p><p>Clients receive the broadcasts and <em>could</em> use it to determine SQL server capability\availability.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58075" class="comments-container"></div><div id="comment-tools-58075" class="comment-tools"></div><div class="clear"></div><div id="comment-58075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

