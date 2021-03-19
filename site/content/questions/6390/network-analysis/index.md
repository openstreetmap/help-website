+++
type = "question"
title = "Network Analysis"
description = '''I am trying to do some network analysis to find out why one of my switches is so slow. As a test, I created a capture during which I copied a file from the host system to another system on the network. In the capture, I could see at least 20 other systems that were communicating with my host. I trie...'''
date = "2011-09-15T07:40:00Z"
lastmod = "2011-09-15T19:33:00Z"
weight = 6390
keywords = [ "coloring", "troubleshooting", "analysis", "network" ]
aliases = [ "/questions/6390" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Network Analysis](/questions/6390/network-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6390-score" class="post-score" title="current number of votes">0</div><span id="post-6390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to do some network analysis to find out why one of my switches is so slow. As a test, I created a capture during which I copied a file from the host system to another system on the network. In the capture, I could see at least 20 other systems that were communicating with my host. I tried to determine what some of them were, and I could see that several were related to Windows Media Player and <code>schemas.xmlsoap.org</code>. Many of these packets are highlighted in black with red text, which I believe means they were dropped.</p><p>Any suggestions on weather or not this is normal? What other steps could I take to further analyze what's going on. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-coloring" rel="tag" title="see questions tagged &#39;coloring&#39;">coloring</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '11, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/10623986f2faf0fe6960fec9af8c4b2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IsPurchase&#39;s gravatar image" /><p><span>IsPurchase</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IsPurchase has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '11, 19:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6390" class="comments-container"></div><div id="comment-tools-6390" class="comment-tools"></div><div class="clear"></div><div id="comment-6390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6398"></span>

<div id="answer-container-6398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6398-score" class="post-score" title="current number of votes">2</div><span id="post-6398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first step is to determine why the packet is colored the way it is. In the Packet Details pane, expand the frame section. If the packet matches a coloring rule, you will see an entry for Coloring Rule Name, and Coloring Rule String. The Coloring Rule String will show what display filter condition the packet matched.</p><p>The default Wireshark installation has a coloring rule named "Bad TCP" which uses red text on a black background. This coloring rule matches the condition "tcp.analysis.flags". This is probably what you're seeing. By itself, this information isn't tremendously helpful, because tcp.analysis.flags matches several different TCP conditions.</p><p>To see exactly what triggered the tcp.analysis.flags, expand the Transmission Control Protocol section of the Packet Details pane. Under that, expand "SEQ/ACK analysis" then expand "TCP Analysis Flags." This will list exactly what caused the packet to match the tcp.analysis.flags filter. After you've examined a few of these packets, you'll notice that an abbreviated version of this information is shown in brackets in the Info column of the Packet List pane, so you don't really have to expand anything in the Packet Details pane. For example, "[TCP Window Update]".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '11, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-6398" class="comments-container"><span id="6400"></span><div id="comment-6400" class="comment"><div id="post-6400-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. Here is what I found. The 'Coloring Rule Name' is 'Checksum Error.' Under the 'SEQ/ACK' header I don't see any information. Under the Internet Protocol Version 4 head there is one line that is highlighted in red that reads. "Header checksum: 0x0000 {incorrect, should be 0x08fe (maybe caused by "IP Checksum offload"?)]"</p></div><div id="comment-6400-info" class="comment-info"><span class="comment-age">(15 Sep '11, 10:51)</span> <span class="comment-user userinfo">IsPurchase</span></div></div><span id="6405"></span><div id="comment-6405" class="comment"><div id="post-6405-score" class="comment-score">1</div><div class="comment-text"><p>Checksum Offload means the checksum is calculated by the NIC driver instead of the OS. Therefore, an outgoing packet doesn't have the correct checksum when Wireshark sees it, but does have the correct checksum when the packet is transmitted on the wire. In this case, the checksum error will be seen only on outgoing packets and the error is cosmetic.</p><p>One way to make the error go away is to turn off checksum offload in the NIC properties. Remember that you can have IP checksum offload, TCP checksum offload, or UDP checksum offload.</p><p>Another way is to disable the Checksum Errors coloring rule.</p></div><div id="comment-6405-info" class="comment-info"><span class="comment-age">(15 Sep '11, 12:39)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="6408"></span><div id="comment-6408" class="comment"><div id="post-6408-score" class="comment-score">1</div><div class="comment-text"><p>...and yet another way is to disable IP checksum validation. Menu: <strong>Edit &gt; Preferences &gt; Protocols &gt; IPv4 &gt; Validate the IPv4 checksum if possible</strong> (uncheck this box)</p></div><div id="comment-6408-info" class="comment-info"><span class="comment-age">(15 Sep '11, 19:33)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-6398" class="comment-tools"></div><div class="clear"></div><div id="comment-6398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

