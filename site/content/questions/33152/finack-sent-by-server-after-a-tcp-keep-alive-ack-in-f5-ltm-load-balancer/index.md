+++
type = "question"
title = "FIN/ACK sent by server, after a TCP KEEP alive ACK in F5 LTM load balancer"
description = '''FIN/ACK sent by server, after a TCP KEEP alive ACK in F5 LTM load balancer No. Time Source Destination Protocol Info  280 2014-05-27 15:37:20 6.6.6.6 1.1.1.1 TCP [TCP Keep-Alive] 9041 &amp;gt; 57703 [ACK] Seq=2629992488 Ack=144158763 Win=65535 Len=0 No. Time Source Destination Protocol Info  281 2014-05...'''
date = "2014-05-29T01:17:00Z"
lastmod = "2014-05-30T05:38:00Z"
weight = 33152
keywords = [ "traffic" ]
aliases = [ "/questions/33152" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FIN/ACK sent by server, after a TCP KEEP alive ACK in F5 LTM load balancer](/questions/33152/finack-sent-by-server-after-a-tcp-keep-alive-ack-in-f5-ltm-load-balancer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33152-score" class="post-score" title="current number of votes">0</div><span id="post-33152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>FIN/ACK sent by server, after a TCP KEEP alive ACK in F5 LTM load balancer</p><pre><code>No.     Time                Source                Destination           Protocol Info
    280 2014-05-27 15:37:20 6.6.6.6         1.1.1.1         TCP      [TCP Keep-Alive] 9041 &gt; 57703 [ACK] Seq=2629992488 Ack=144158763 Win=65535 Len=0
No.     Time                Source                Destination           Protocol Info
    281 2014-05-27 15:37:20 3.3.3.3         2.2.2.2          TCP      [TCP Keep-Alive] 57703 &gt; 9041 [ACK] Seq=380327577 Ack=1111550497 Win=65535 Len=0
No.     Time                Source                Destination           Protocol Info
    282 2014-05-27 15:37:20 2.2.2.2          3.3.3.3         TCP      [TCP Window Update] 9041 &gt; 57703 [ACK] Seq=1111550497 Ack=380327578 Win=46 Len=0
No.     Time                Source                Destination           Protocol Info
    283 2014-05-27 15:37:20 1.1.1.1         6.6.6.6         TCP      [TCP Keep-Alive ACK] 57703 &gt; 9041 [ACK] Seq=144158763 Ack=2629992489 Win=68 Len=0
No.     Time                Source                Destination           Protocol Info
    284 2014-05-27 15:37:22 2.2.2.2          3.3.3.3         TCP      9041 &gt; 57703 [FIN, ACK] Seq=1111550497 Ack=380327578 Win=46 Len=0
No.     Time                Source                Destination           Protocol Info
    285 2014-05-27 15:37:22 3.3.3.3         2.2.2.2          TCP      57703 &gt; 9041 [ACK] Seq=380327578 Ack=1111550498 Win=4380 Len=0
No.     Time                Source                Destination           Protocol Info
    286 2014-05-27 15:37:22 6.6.6.6         1.1.1.1         TCP      9041 &gt; 57703 [FIN, ACK] Seq=2629992489 Ack=144158763 Win=3780 Len=0
No.     Time                Source                Destination           Protocol Info
    287 2014-05-27 15:37:22 1.1.1.1         6.6.6.6         TCP      57703 &gt; 9041 [ACK] Seq=144158763 Ack=2629992490 Win=68 Len=0
No.     Time                Source                Destination           Protocol Info
    288 2014-05-27 15:37:22 1.1.1.1         6.6.6.6         TCP      57703 &gt; 9041 [FIN, ACK] Seq=144158763 Ack=2629992490 Win=68 Len=0
No.     Time                Source                Destination           Protocol Info
    289 2014-05-27 15:37:22 6.6.6.6         1.1.1.1         TCP      9041 &gt; 57703 [ACK] Seq=2629992490 Ack=144158764 Win=3780 Len=0
6.6.6.6---VIP   
2.2.2.2---Pool member   
3.3.3.3---snat   
1.1.1.1---client</code></pre></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '14, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/a11f0b7df5037a9a069c37d4e897871e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aneshk&#39;s gravatar image" /><p><span>Aneshk</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aneshk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 May '14, 02:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-33152" class="comments-container"><span id="33153"></span><div id="comment-33153" class="comment"><div id="post-33153-score" class="comment-score"></div><div class="comment-text"><p>The Server that sends the FIN/ACK in response to the ACK is listening on a HTTPS port</p></div><div id="comment-33153-info" class="comment-info"><span class="comment-age">(29 May '14, 01:23)</span> <span class="comment-user userinfo">Aneshk</span></div></div><span id="33158"></span><div id="comment-33158" class="comment"><div id="post-33158-score" class="comment-score"></div><div class="comment-text"><p>what is your question?</p></div><div id="comment-33158-info" class="comment-info"><span class="comment-age">(29 May '14, 02:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33168"></span><div id="comment-33168" class="comment"><div id="post-33168-score" class="comment-score"></div><div class="comment-text"><p>I also manage F5 load-balancers, so I look at traces like this quite often. I don't see much of interest in the data you have chosen to include. There's no TCP data transmitted - basically the connection is idle. The Server sends an ACK with a larger window in #282 in response to a keepalive packet sent by the LTM in #281. Then both clientside and serverside connection sits idle for two seconds, until the Server begins closing the connection by sending a FIN packet to the LTM in #284. The rest of the packets are just artifacts of the connection being gracefully closed on both sides of the LTM.</p><p>So I'd agree with Kurt here - what exactly is your question?</p><p>If the question is why does the Server begin closing the connection in #284, my guess is that either the TCP stack is configured to close connections after two seconds of idle time, or that the application layer has finished processing all the TCP data and has triggered the TCP stack to close the connection.</p></div><div id="comment-33168-info" class="comment-info"><span class="comment-age">(29 May '14, 06:51)</span> <span class="comment-user userinfo">smp</span></div></div><span id="33186"></span><div id="comment-33186" class="comment"><div id="post-33186-score" class="comment-score"></div><div class="comment-text"><p>i started seeing this behavior of the server closing the connection, right after i set the keep alive interval for 60 seonds, that is the connection is removed from the connection table after 60 seconds, My question is whether the server closing the connection in response to the keep-alive sent by the load balancer</p></div><div id="comment-33186-info" class="comment-info"><span class="comment-age">(29 May '14, 21:20)</span> <span class="comment-user userinfo">Aneshk</span></div></div><span id="33198"></span><div id="comment-33198" class="comment"><div id="post-33198-score" class="comment-score"></div><div class="comment-text"><blockquote><p>My question is whether the server closing the connection in response to the keep-alive sent by the load balancer</p></blockquote><p>No, I don't think so - at least not directly. It's difficult to tell what is happening since you've only included the final few segments of the TCP stream. And you didn't state what the original keepalive interval was (was it larger or smaller?). But my initial thought is that by adjusting the down, you are forcing the Server to process more or less keepalive packets. Perhaps you have caused the the Server to reach a limit imposed on its TCP stack to process a certain number of these packets.</p><p>If Keepalives are really at the heart of this issue, then I think we'd need to see all of the keepalive packets which means you'd need to provide the entire trace. You can upload one to cloudshark.org and provide a link if you want some additional insight from me.</p></div><div id="comment-33198-info" class="comment-info"><span class="comment-age">(30 May '14, 05:38)</span> <span class="comment-user userinfo">smp</span></div></div></div><div id="comment-tools-33152" class="comment-tools"></div><div class="clear"></div><div id="comment-33152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

