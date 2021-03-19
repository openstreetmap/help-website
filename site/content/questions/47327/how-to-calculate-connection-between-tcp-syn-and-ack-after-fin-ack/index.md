+++
type = "question"
title = "How to calculate connection between tcp syn and ack after fin-ack?"
description = '''Hi all I have a pcap file that contains many tcp connections, i would like to calculate duration time between tcp syn and ack after Fin-ack for every connection ? thank you for helping us '''
date = "2015-11-06T03:33:00Z"
lastmod = "2015-11-06T03:48:00Z"
weight = 47327
keywords = [ "tcp" ]
aliases = [ "/questions/47327" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate connection between tcp syn and ack after fin-ack?](/questions/47327/how-to-calculate-connection-between-tcp-syn-and-ack-after-fin-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47327-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all I have a pcap file that contains many tcp connections, i would like to calculate duration time between <strong>tcp syn</strong> and <strong>ack after Fin-ack</strong> for every connection ? thank you for helping us</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '15, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/6a816926666b06f5160340dd59f59042?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abo3abbas&#39;s gravatar image" /><p>Abo3abbas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abo3abbas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>wikified 06 Nov '15, 05:43</p></div></div><div id="comments-container-47327" class="comments-container"></div><div id="comment-tools-47327" class="comment-tools"></div><div class="clear"></div><div id="comment-47327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47329"></span>

<div id="answer-container-47329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47329-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried Statistics -&gt; Conversations -&gt; TCP, looking at the "Duration" column?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '15, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47329" class="comments-container"><span id="47331"></span><div id="comment-47331" class="comment"><div id="post-47331-score" class="comment-score"></div><div class="comment-text"><p>So which duration are you looking for?</p><ul><li>SYN - SYN/ACK - ACK</li><li>SYN-SYN/ACK - ACK ... FIN - ACK - FIN - ACK?</li></ul><p>First one is iRTT, which you can see in the TCP decode in the SEQ/ACK Analysis, the second one is duration usually.</p></div><div id="comment-47331-info" class="comment-info"><span class="comment-age">(06 Nov '15, 03:55)</span> Jasper ♦♦</div></div><span id="47334"></span><div id="comment-47334" class="comment"><div id="post-47334-score" class="comment-score"></div><div class="comment-text"><p>Well, Wireshark separates conversations from SYN to FIN or Reset, so even if you have port reuse, you'll see two conversations then, with a duration each. That should be good enough for most cases.</p><p>When you have to deal with missing FIN packets (incomplete conversations) the duration will be wrong, but the only way to verify those is to do it manually.</p></div><div id="comment-47334-info" class="comment-info"><span class="comment-age">(06 Nov '15, 04:06)</span> Jasper ♦♦</div></div></div><div id="comment-tools-47329" class="comment-tools"></div><div class="clear"></div><div id="comment-47329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

