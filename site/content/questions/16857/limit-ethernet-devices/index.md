+++
type = "question"
title = "Limit ethernet devices"
description = '''Hi there, Is possible to limit capture devices only to group members? like wireshark group can capture only on ethernet device eth0 where another group can capture only on eth1 ? (i&#x27;ve already done the http://wiki.wireshark.org/CaptureSetup/CapturePrivileges) br. Pidgreen'''
date = "2012-12-13T17:25:00Z"
lastmod = "2012-12-14T08:00:00Z"
weight = 16857
keywords = [ "ethernet", "security", "linux", "dumpcap", "limiting" ]
aliases = [ "/questions/16857" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Limit ethernet devices](/questions/16857/limit-ethernet-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Is possible to limit capture devices only to group members? like wireshark group can capture only on ethernet device eth0 where another group can capture only on eth1 ?</p><p>(i've already done the <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges)">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges)</a></p><p>br.</p><p>Pidgreen</p></div><div id="question-tags" class="tags-container tags">ethernet security linux dumpcap limiting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 17:25</strong></p><img src="https://secure.gravatar.com/avatar/4f6c4029e6fe95a7bbff22ee63becabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pidgreen&#39;s gravatar image" /><p>pidgreen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pidgreen has no accepted answers">0%</span></p></div></div><div id="comments-container-16857" class="comments-container"><span id="16867"></span><div id="comment-16867" class="comment"><div id="post-16867-score" class="comment-score"></div><div class="comment-text"><p>You'll have to specify the platform. On Linux I'm not sure, since it's capability based, on MAC OSX it may be possible through bpf permissions.</p></div><div id="comment-16867-info" class="comment-info"><span class="comment-age">(14 Dec '12, 04:22)</span> Jaap ♦</div></div></div><div id="comment-tools-16857" class="comment-tools"></div><div class="clear"></div><div id="comment-16857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16893"></span>

<div id="answer-container-16893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16893-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Linux and Windows that's not possible without a code change. Regarding Mac OSX, I don't know.</p><blockquote><p><code>http://ask.wireshark.org/questions/15577/how-to-limit-access-of-wireshark-to-1-of-several-nics</code><br />
<code>http://ask.wireshark.org/questions/14067/limit-interface</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '12, 08:05</p></div></div><div id="comments-container-16893" class="comments-container"></div><div id="comment-tools-16893" class="comment-tools"></div><div class="clear"></div><div id="comment-16893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

