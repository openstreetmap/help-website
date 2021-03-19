+++
type = "question"
title = "MSSQL Connection String"
description = '''Hi, I am migrating one of our db server to new hardware. Our application is legacy and not all developer exist who developed this app. We want to see what servers are connecting to database, we had done this with dmvs. But the next challenge is to capture connection string. In code usually qualified...'''
date = "2015-06-05T05:28:00Z"
lastmod = "2015-06-05T05:47:00Z"
weight = 42923
keywords = [ "connection", "mssql" ]
aliases = [ "/questions/42923" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MSSQL Connection String](/questions/42923/mssql-connection-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am migrating one of our db server to new hardware. Our application is legacy and not all developer exist who developed this app.</p><p>We want to see what servers are connecting to database, we had done this with dmvs. But the next challenge is to capture connection string. In code usually qualified domain exist for connection but on some places one had bind the IPAddress. So this is risky to move without know these details. We want to extract that information, so that dev can fix code on required server</p><p>I want to capture connection string information e.g. &lt;connectionstring&gt;Server = ServerName , Catalog=MyDb ........ &lt;connectionstring&gt;Server = ServerIP , Catalog=MyDb ..............</p><p>How can I capture such information ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">connection mssql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '15, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/f926d086643b1aa8b7ed648e282518fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thbaig1&#39;s gravatar image" /><p>thbaig1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thbaig1 has no accepted answers">0%</span></p></div></div><div id="comments-container-42923" class="comments-container"></div><div id="comment-tools-42923" class="comment-tools"></div><div class="clear"></div><div id="comment-42923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42925"></span>

<div id="answer-container-42925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42925-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Basically, the best way is to use a SPAN port or TAP to record what the server is doing. Take a look at the Wiki page for some setup options: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>Then, you have to hope that the communication isn't encrypted or you won't see any connection strings. Use the conversation statistics to see what conversations your server is using, and then use "Follow TCP Stream" to see ASCII extracts of the communication details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '15, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42925" class="comments-container"></div><div id="comment-tools-42925" class="comment-tools"></div><div class="clear"></div><div id="comment-42925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

