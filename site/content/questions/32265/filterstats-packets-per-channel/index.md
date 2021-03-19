+++
type = "question"
title = "Filter/Stats; # Packets per Channel?"
description = '''I&#x27;m trying to find a way utilizing wireshark/tshark to provide me with the number of packets per channel seen in a given pcap file. I already know the long way (doing individual filters by channel), but I&#x27;m trying to find a faster process. I&#x27;ve looked through a lot of questions but I can&#x27;t seem to f...'''
date = "2014-04-28T10:08:00Z"
lastmod = "2014-05-01T16:44:00Z"
weight = 32265
keywords = [ "filter", "statistics", "channel" ]
aliases = [ "/questions/32265" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter/Stats; \# Packets per Channel?](/questions/32265/filterstats-packets-per-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32265-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to find a way utilizing wireshark/tshark to provide me with the number of packets per channel seen in a given pcap file. I already know the long way (doing individual filters by channel), but I'm trying to find a faster process. I've looked through a lot of questions but I can't seem to find anyway to do this. I would be happy with just the raw numbers (I don't need no fancy graphs).</p><p>Simply put; Given a .pcap file, how can I determine the number of packets seen per channel (1-14), in a single filter / more automated fashion?</p></div><div id="question-tags" class="tags-container tags">filter statistics channel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/0ccf92e667f3b910d97d1526ff9dbc20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kinmuan&#39;s gravatar image" /><p>Kinmuan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kinmuan has no accepted answers">0%</span></p></div></div><div id="comments-container-32265" class="comments-container"><span id="32266"></span><div id="comment-32266" class="comment"><div id="post-32266-score" class="comment-score"></div><div class="comment-text"><p>Whats your definition of a "Channel"?</p></div><div id="comment-32266-info" class="comment-info"><span class="comment-age">(28 Apr '14, 10:13)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32265" class="comment-tools"></div><div class="clear"></div><div id="comment-32265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32369"></span>

<div id="answer-container-32369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you are talking about TCP conversations while you say: 'Channel'. If that is the case, you can see the frames per TCP connection by using the statistics functions.</p><blockquote><p>Statistics -&gt; Conversations -&gt; TCP [tab]</p></blockquote><p>and then check the columns <strong>Packets</strong> and/or <strong>Bytes</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32369" class="comments-container"></div><div id="comment-tools-32369" class="comment-tools"></div><div class="clear"></div><div id="comment-32369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

