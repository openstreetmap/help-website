+++
type = "question"
title = "Detect all conversation with a FIN packet"
description = '''How can I detect/print all conversation that (will) have a FIN packet within an existing capture file.  I&#x27;m aiming at tshark usage.'''
date = "2011-12-06T07:18:00Z"
lastmod = "2011-12-06T07:33:00Z"
weight = 7802
keywords = [ "fin" ]
aliases = [ "/questions/7802" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Detect all conversation with a FIN packet](/questions/7802/detect-all-conversation-with-a-fin-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I detect/print all conversation that (will) have a FIN packet within an existing capture file.<br />
I'm aiming at tshark usage.</p></div><div id="question-tags" class="tags-container tags">fin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '11, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/920a90d8a3dca941060cc1e39cc76346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trevor&#39;s gravatar image" /><p>Trevor<br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trevor has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7802" class="comments-container"></div><div id="comment-tools-7802" class="comment-tools"></div><div class="clear"></div><div id="comment-7802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7803"></span>

<div id="answer-container-7803" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7803-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One way would be to actually filter for tcp.flags.fin==1 and then look for unique identifiers for that particular session. This could be tcp.port (if unique), tcp.stream (which I think is the easiest) or maybe even initial sequence number...</p><p>You'll need a proper identifier to later filter those sessions if you want to see them complete and not only the FIN-packets.</p><p>tshark -r testtrace.pcap -R "tcp.flags.fin==1" -n -Tfields -e tcp.stream</p><p>can give you a list of those tcp.stream numbers. You can append | sort -u or whatever to go ahead with script building e.g.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7803" class="comments-container"><span id="7844"></span><div id="comment-7844" class="comment"><div id="post-7844-score" class="comment-score"></div><div class="comment-text"><p>10x. That seems like a good way to start</p></div><div id="comment-7844-info" class="comment-info"><span class="comment-age">(08 Dec '11, 03:03)</span> Trevor</div></div></div><div id="comment-tools-7803" class="comment-tools"></div><div class="clear"></div><div id="comment-7803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

