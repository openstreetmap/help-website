+++
type = "question"
title = "Differences Between I/O Graph and TCPStream Throughput Graph"
description = '''The I/O graph appears to let you visually graph throughput, yet there&#x27;s the TCPStream Throughput graph. The throughput measured between the two graphs seem to be way off just comparing Bytes/sec. I&#x27;m not sure how either is derived, so I need some input on this. Which is the more accurate representat...'''
date = "2012-09-28T09:51:00Z"
lastmod = "2012-09-29T22:43:00Z"
weight = 14605
keywords = [ "graph", "throughput" ]
aliases = [ "/questions/14605" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Differences Between I/O Graph and TCPStream Throughput Graph](/questions/14605/differences-between-io-graph-and-tcpstream-throughput-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14605-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The I/O graph appears to let you visually graph throughput, yet there's the TCPStream Throughput graph. The throughput measured between the two graphs seem to be way off just comparing Bytes/sec. I'm not sure how either is derived, so I need some input on this.</p><p>Which is the more accurate representation of actual data throughput?<br />
</p></div><div id="question-tags" class="tags-container tags">graph throughput</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/9b63b6c21518055db59ce7f1f839985a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarlT&#39;s gravatar image" /><p>CarlT<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarlT has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-14605" class="comments-container"></div><div id="comment-tools-14605" class="comment-tools"></div><div class="clear"></div><div id="comment-14605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14612"></span>

<div id="answer-container-14612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14612-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>They are both accurate, but they're displaying different things by default.</p><p>Unless you apply a display filter, the I/O graph will show you the throughput of all traffic in the trace file, in both directions. The TCP Stream Throughput graph will show only the throughput from one TCP stream, in one direction, based on the selected packet. If you filter the I/O graph so that it is looking at the same traffic as the Throughput graph, you'll see the same values for Bytes/sec.</p><p>To verify:</p><p>Select a TCP packet traveling in the direction of data flow. Note the source IP address, then expand the TCP portion of the packet and note the stream index number. With this packet still selected, view the TCP Stream Throughput graph.</p><p>Now open the I/O graph (leave the Throughput graph open for comparison). Under 'X-axis' leave the 'Tick interval' at 1 second. Under 'Y-axis' change 'Units' to 'Bytes/Tick' and then apply the following filter to the Graph 1 field:</p><p>tcp.stream==<em>n</em> &amp;&amp; ip.src==<em>a.b.c.d</em></p><p>For 'n' substitute the TCP stream index number and for a.b.c.d substitute the source IP address. Click the Graph 1 button once to turn it off, then click it again to turn it back on, which will activate the filter that you entered.</p><p>Now arrange the I/O graph and the Throughput graph side-by-side on your screen. The two graphs are now looking at the same data and you should see that the values in the two graphs correspond very closely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '12, 22:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Sep '12, 23:56</p></div></div><div id="comments-container-14612" class="comments-container"></div><div id="comment-tools-14612" class="comment-tools"></div><div class="clear"></div><div id="comment-14612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

