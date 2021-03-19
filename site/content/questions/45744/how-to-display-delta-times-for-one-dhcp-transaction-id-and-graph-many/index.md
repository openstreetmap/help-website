+++
type = "question"
title = "How to display delta times for one DHCP transaction ID and graph many?"
description = '''or how to sort DHCP transaction ID&#x27;s in a manner that you can see the delta between first &#x27;discover&#x27; and the last &#x27;ack&#x27;?  So far I&#x27;ve tried to make an extra column for bootp.id and sort | filter out transaction ID&#x27;s that match. Now as much as this is possible for a few packets as seen in the example...'''
date = "2015-09-10T01:22:00Z"
lastmod = "2015-09-10T07:25:00Z"
weight = 45744
keywords = [ "dhcp", "bootp", "graph" ]
aliases = [ "/questions/45744" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to display delta times for one DHCP transaction ID and graph many?](/questions/45744/how-to-display-delta-times-for-one-dhcp-transaction-id-and-graph-many)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45744-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>or how to sort DHCP transaction ID's in a manner that you can see the delta between first 'discover' and the last 'ack'? <img src="https://osqa-ask.wireshark.org/upfiles/DHCP02.jpg" alt="alt text" /></p><p>So far I've tried to make an extra column for <code>bootp.id</code> and sort | filter out transaction ID's that match. Now as much as this is possible for a few packets as seen in the example above, i'd like to be able to graph all valid question | response pairs so i can see some DHCP server response time trends? I'd appreciate any idea's! Thanks!</p></div><div id="question-tags" class="tags-container tags">dhcp bootp graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '15, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></img></div></div><div id="comments-container-45744" class="comments-container"><span id="45758"></span><div id="comment-45758" class="comment"><div id="post-45758-score" class="comment-score"></div><div class="comment-text"><p>Don't tell me it's too difficult to be done ;-)</p></div><div id="comment-45758-info" class="comment-info"><span class="comment-age">(10 Sep '15, 06:41)</span> Marc</div></div></div><div id="comment-tools-45744" class="comment-tools"></div><div class="clear"></div><div id="comment-45744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45761"></span>

<div id="answer-container-45761" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try the following:</p><p><code>View &gt; Time Display Format &gt; Time since previously displayed packet</code></code></p><code></code><p>and as a display filter</p><p><code>(bootp.id == 0x55d87b83) &amp;&amp; ((bootp.option.dhcp == 1) || (bootp.option.dhcp == 5))</code></code></p><code></code><p>In regards to your second question, I don't have a packet capture to test it, but I would export the relevant columns as csv and use Excel to graph the trend.</p></code></code></code></code></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-45761" class="comments-container"><span id="45776"></span><div id="comment-45776" class="comment"><div id="post-45776-score" class="comment-score"></div><div class="comment-text"><p>Cheers Roland, but that does the trick for only one DHCP Discover| ACK pair, if instead i would filter the trace for just <code>((bootp.option.dhcp == 1) || (bootp.option.dhcp == 5))</code> i would get all DHCP discovers and DHCP ACKS and with it i have created a column "Transaction ID" ... Now consider the following, 'when is my cycle complete if i get ACKS from more then one server, i.e. more answers on the same transaction ID?' This happens when tracing packets on the exit of an DHCP relay switch, we see more than 1 outgoing request and more than 1 answer: <img src="https://osqa-ask.wireshark.org/upfiles/2015-09-11_085841.jpg" alt="alt text" /></p></div><div id="comment-45776-info" class="comment-info"><span class="comment-age">(10 Sep '15, 23:48)</span> Marc</div></div><span id="45777"></span><div id="comment-45777" class="comment"><div id="post-45777-score" class="comment-score"></div><div class="comment-text"><p>So basically i have two things to solve: one being time measurement, when is that DHCP cycle finished? and two how to match up the first packet and the last from oe transaction iD , without me (without a human looking at the data)?</p></div><div id="comment-45777-info" class="comment-info"><span class="comment-age">(10 Sep '15, 23:51)</span> Marc</div></div><span id="45778"></span><div id="comment-45778" class="comment"><div id="post-45778-score" class="comment-score"></div><div class="comment-text"><p>Maybe you could provide us a trace in a public accessible place.</p></div><div id="comment-45778-info" class="comment-info"><span class="comment-age">(11 Sep '15, 00:04)</span> Christian_R</div></div><span id="45782"></span><div id="comment-45782" class="comment"><div id="post-45782-score" class="comment-score">1</div><div class="comment-text"><p>I tailored the answer to your screenshot, but the main point was, if you only filter for discover and ack you will reduce the amount of displayed packets. With DHCP relay everything changes. We have to look for another identifier, since the transaction id is the same. To match the packets without human interaction you will have to write a script.</p></div><div id="comment-45782-info" class="comment-info"><span class="comment-age">(11 Sep '15, 02:37)</span> Roland</div></div><span id="45784"></span><div id="comment-45784" class="comment"><div id="post-45784-score" class="comment-score"></div><div class="comment-text"><p>Basically saying that the 'unique identifier' is a set of values combined, like (client MAC adres + Transaction ID + Discover + Offer + etc) to get answer response pairs to match ..</p></div><div id="comment-45784-info" class="comment-info"><span class="comment-age">(11 Sep '15, 05:09)</span> Marc</div></div></div><div id="comment-tools-45761" class="comment-tools"></div><div class="clear"></div><div id="comment-45761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

