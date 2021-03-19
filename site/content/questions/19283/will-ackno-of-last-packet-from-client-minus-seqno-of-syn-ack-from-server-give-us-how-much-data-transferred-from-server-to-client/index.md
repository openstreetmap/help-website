+++
type = "question"
title = "Will ack.no of last packet from client (minus) seq.no of syn-ack from server give us how much data transferred from server to client?"
description = '''I am looking a way to compute the data transfer from server to client. Seq.no of syn-ack from server is 0(relative seq enabled) Ack.no of last packet from client is 158068267 By subtracting 158068267 from 0 we will get total number of bytes transferred from server to client. However,the approach sta...'''
date = "2013-03-07T12:30:00Z"
lastmod = "2013-03-12T12:08:00Z"
weight = 19283
keywords = [ "bytes", "computation" ]
aliases = [ "/questions/19283" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Will ack.no of last packet from client (minus) seq.no of syn-ack from server give us how much data transferred from server to client?](/questions/19283/will-ackno-of-last-packet-from-client-minus-seqno-of-syn-ack-from-server-give-us-how-much-data-transferred-from-server-to-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19283-score" class="post-score" title="current number of votes">0</div><span id="post-19283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking a way to compute the data transfer from server to client.</p><p>Seq.no of syn-ack from server is 0(relative seq enabled) Ack.no of last packet from client is 158068267</p><p>By subtracting 158068267 from 0 we will get total number of bytes transferred from server to client.</p><p>However,the approach statistics&gt;Conversations&gt;TCP is showing 163837601 bytes transferred from B---&gt;A</p><p>Any reason behind this difference?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-computation" rel="tag" title="see questions tagged &#39;computation&#39;">computation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '13, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-19283" class="comments-container"></div><div id="comment-tools-19283" class="comment-tools"></div><div class="clear"></div><div id="comment-19283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19285"></span>

<div id="answer-container-19285" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19285-score" class="post-score" title="current number of votes">1</div><span id="post-19285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Statistics &gt; Conversations &gt; TCP shows the total number of bytes transferred including overhead, such as the TCP header, the IP header, the Ethernet header, any Ethernet padding on undersized frames, etc.</p><p>Subtracting the initial sequence number from the final sequence number will give you the total number of bytes of TCP data transferred (assuming the sequence number has not wrapped). This is payload only and does not include overhead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '13, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19285" class="comments-container"><span id="19286"></span><div id="comment-19286" class="comment"><div id="post-19286-score" class="comment-score"></div><div class="comment-text"><p>That helps.Thanks!</p></div><div id="comment-19286-info" class="comment-info"><span class="comment-age">(07 Mar '13, 12:52)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="19394"></span><div id="comment-19394" class="comment"><div id="post-19394-score" class="comment-score"></div><div class="comment-text"><p>What if i get, Less acknowledgement number and high sequence number.</p><p>What will be my transfer data session ?</p><p>Will this still valid - Subtracting the initial sequence number from the final sequence number will give you the total number of bytes of TCP data transferred ??</p><p>Please help.</p><p><img src="http://s9.postimage.org/wvq8epab3/1111.jpg" alt="alt text" /></p></div><div id="comment-19394-info" class="comment-info"><span class="comment-age">(12 Mar '13, 09:48)</span> <span class="comment-user userinfo">adtmv7</span></div></div><span id="19401"></span><div id="comment-19401" class="comment"><div id="post-19401-score" class="comment-score">1</div><div class="comment-text"><p>AFAIK,Less acknowledgement and high sequence number will never happen. In your screen shot you are comparing sequence and acknowledgement from single host perspective that is why you are seeing high sequence number and low acknowledgement number but if you compare the sequence number of other end(which will be in syn-ack if it is server or in syn if it is client) with the acknowledgement of the one you are showing,ack number will outweigh(data transfer is incremental starting from 1 byte and goes on) the sequence number. Hope this clears...</p></div><div id="comment-19401-info" class="comment-info"><span class="comment-age">(12 Mar '13, 11:50)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="19402"></span><div id="comment-19402" class="comment"><div id="post-19402-score" class="comment-score">1</div><div class="comment-text"><p>IF you're using relative sequence numbers, and IF the sequence numbers haven't wrapped, and IF you captured the SYN and SYN/ACK, THEN the SEQ number is the number of bytes of TCP data transmitted by this host in this one TCP conversation up to this point, and the ACK number is the number of bytes transmitted by the other host. If you want to be really accurate, subtract one byte in each direction for the phantom byte during connection establishment, and if this is the last packet and the connection has been closed, subtract another byte in each direction for the phantom byte during teardown.</p></div><div id="comment-19402-info" class="comment-info"><span class="comment-age">(12 Mar '13, 12:08)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-19285" class="comment-tools"></div><div class="clear"></div><div id="comment-19285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

