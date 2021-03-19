+++
type = "question"
title = "How can I export data from TCPstream Graph and calculate the Throughput"
description = '''Dear All I need to create a file that allows me to calculate the throughput of the network and check with the values ​​of the graph TCPStream. How can I export the graph data TCPStream. I have calculated the throughput considering the following formula: throughput = packet length / (time of arrival ...'''
date = "2012-12-23T05:38:00Z"
lastmod = "2012-12-23T05:38:00Z"
weight = 17192
keywords = [ "throughput" ]
aliases = [ "/questions/17192" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I export data from TCPstream Graph and calculate the Throughput](/questions/17192/how-can-i-export-data-from-tcpstream-graph-and-calculate-the-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17192-score" class="post-score" title="current number of votes">0</div><span id="post-17192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All</p><p>I need to create a file that allows me to calculate the throughput of the network and check with the values ​​of the graph TCPStream. How can I export the graph data TCPStream.</p><p>I have calculated the throughput considering the following formula:</p><p>throughput = packet length / (time of arrival of the packet - time of arrival of the previous packet). Using this formula I have found differents values from the graph of TCPStream</p><p>Example: Considering the values below: Observe that the packets are filtered by: ip.addr == 10.136.1.12 and ip.addr == 10.250.40.10 and tcp.port == 102</p><pre><code>No        time             source       destination     protocol   length  info

8       0.012479        10.136.1.12.    10.250.40.10    PRES        205     Data Transfer (DT)...

21      0.030623        10.250.40.10    10.136.1.12     TCP          66     iso-tsap &gt; 60049.....

305     0.031452        10.250.40.10    10.136.1.12     PRES         95     Data Transfer (DT)...</code></pre><p>throughput = 66 * 8 / ( 0.030623 - 0.012479) = 29100.5291 bits/sec</p><p>Please, what is wrong with this way to calculate the throughput<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '12, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/7f7ebc2aa14d7797dd8431f7c74dd9fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ubiratan%20Carmo&#39;s gravatar image" /><p><span>Ubiratan Carmo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ubiratan Carmo has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '14, 18:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-17192" class="comments-container"></div><div id="comment-tools-17192" class="comment-tools"></div><div class="clear"></div><div id="comment-17192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

