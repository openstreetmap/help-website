+++
type = "question"
title = "Scan certain network or IP"
description = '''I was wondering is there a way to monitor a certain ip address or address range? thank you'''
date = "2010-12-01T11:27:00Z"
lastmod = "2010-12-01T20:30:00Z"
weight = 1194
keywords = [ "ip", "certain", "networks", "scan" ]
aliases = [ "/questions/1194" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Scan certain network or IP](/questions/1194/scan-certain-network-or-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering is there a way to monitor a certain ip address or address range? thank you</p></div><div id="question-tags" class="tags-container tags">ip certain networks scan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '10, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/7af69ca2debd99163d9c2112f10e60ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keyboard&#39;s gravatar image" /><p>keyboard<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keyboard has no accepted answers">0%</span></p></div></div><div id="comments-container-1194" class="comments-container"></div><div id="comment-tools-1194" class="comment-tools"></div><div class="clear"></div><div id="comment-1194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1198"></span>

<div id="answer-container-1198" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1198-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can only monitor traffic seen on the interface you have Wireshark to capture on. You need to arrange for that traffic to be presented on that interface by whatever means. Usually this will mean port-mirroring on a switch that is carrying the traffic you are interested in.</p><p>You can then use capture filters in wireshark to narrow the capture like "host 10.1.2.3" or "net 10.1.2.0/24"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '10, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1198" class="comments-container"><span id="1326"></span><div id="comment-1326" class="comment"><div id="post-1326-score" class="comment-score"></div><div class="comment-text"><p>ok thank you. I was particularly wanting to watch certain machines but if I watch a network then I should still see everything on that network correct. Including the machine I am wanting to watch?</p></div><div id="comment-1326-info" class="comment-info"><span class="comment-age">(13 Dec '10, 06:45)</span> keyboard</div></div></div><div id="comment-tools-1198" class="comment-tools"></div><div class="clear"></div><div id="comment-1198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

