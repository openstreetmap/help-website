+++
type = "question"
title = "Need advice with trace file"
description = '''This issue is with the client timing out when accessing a particular web site going through a proxy appliance. The client can access all other Internet web sites with no issue with exception of this url that had previously worked fine. A capture was done on the bluecoat proxy and it shows the http 2...'''
date = "2012-09-26T15:19:00Z"
lastmod = "2012-09-26T16:06:00Z"
weight = 14561
keywords = [ "http-ok_non-response" ]
aliases = [ "/questions/14561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need advice with trace file](/questions/14561/need-advice-with-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14561-score" class="post-score" title="current number of votes">0</div><span id="post-14561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This issue is with the client timing out when accessing a particular web site going through a proxy appliance. The client can access all other Internet web sites with no issue with exception of this url that had previously worked fine. A capture was done on the bluecoat proxy and it shows the http 200 ok response being sent to the client. For the client side, the firewall capture does not show the reply reaching the firewall. No visibility along the paths after the bluecoat so don’t know where it could have been loss. It is odd that only this web site is affected and all other web sites are working. At this time, all firewall, bluecoat and routing issues have been ruled out and root cause is unknown at this time.</p><p>The trace file is can be found at <a href="http://cloudshark.org/captures/4a3b7c2a3230">http://cloudshark.org/captures/4a3b7c2a3230</a></p><pre><code>Request: Client-?Client site FW&lt;---?FW1----?ISP--?Data Center Core/Proxy--?Internet

Reply: Internet-?Data Center Core/Proxy--?ISP-?FW1--?Client site FW--?Client
client FW NAT IP: 192.168.1.1 Proxy:192.168.1.2</code></pre><p>FW1 capture is shown below.</p><pre><code>13:22:17.   0x0800 62: 192.168.1.1.50863 &gt; 192.168.1.2.80: S [tcp sum ok] 2755830644:2755830644(0) win 8192 &lt;mss 1260,nop,nop,sackOK&gt; (DF) (ttl 126, id 6888) : SYN

13:22:17.   0x0800 62: 192.168.1.2.80 &gt; 192.168.1.1.50863: S [tcp sum ok] 2416274753:2416274753(0) ack 2755830645 win 65535 &lt;mss 1350,sackOK,eol&gt; (ttl 60, id 37726) : SYN, ACK

13:22:17.   0x0800 60: 192.168.1.1.50863 &gt; 192.168.1.2.80: . [tcp sum ok] 2755830645:2755830645(0) ack 2416274754 win 65520 (DF) (ttl 126, id 6889) : ACK

13:22:17.   0x0800 365: 192.168.1.1.50863 &gt; 192.168.1.2.80: P 2755830645:2755830956(311) ack 2416274754 win 65520 (DF) (ttl 126, id 6890) : GET HTTP

13:22:18.   ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? id 38997 is missing (id 38997 is in the trace packet capture from the bluecoat).

13:22:18   0x0800 392: 192.168.1.2.80 &gt; 192.168.1.1.50863: P 2416276014:2416276352(338) ack 2755830956 win 65535 [tos 0x60]  (ttl 60, id 38998) : TCP segment of a reassembled PDU

13:22:18   0x0800 66: 192.168.1.1.50863 &gt; 192.168.1.2.80: P [tcp sum ok] 2755830956:2755830956(0) ack 2416274754 win 65520 &lt;nop,nop,sack sack 1 {2416276014:2416276352} &gt; (ttl 255, id 46285) : TCP Dup ACK4#1

13:22:18.   0x0800 365: 192.168.1.1.50863 &gt; 192.168.1.2.80: P 2755830645:2755830956(311) ack 2416274754 win 65520 (DF) (ttl 126, id 6897) : TCP Retransmission</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http-ok_non-response" rel="tag" title="see questions tagged &#39;http-ok_non-response&#39;">http-ok_non-response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '12, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '12, 15:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-14561" class="comments-container"></div><div id="comment-tools-14561" class="comment-tools"></div><div class="clear"></div><div id="comment-14561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14562"></span>

<div id="answer-container-14562" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14562-score" class="post-score" title="current number of votes">0</div><span id="post-14562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The client sends an MSS of 1260 to the bluecoat and the bluecoat does indeed follow up with sending packets with 1260-byte segments. But from your tracefile on Cloudshark one can see that all frames of length 1314 (1260 bytes payload) don't get to the client. This can be seen by looking at frame 9 in which the client acknowledges receiving frame 6 but not frame 5 (look at the SACK edges).</p><p>To me this looks like an MTU issue. There might be a link in the network between the bluecoat and the client that is not capable of transporting 1314 byte frames. Normally the frames would be fragmented, but either fragmenting is disabled or a fw drops the frames which are fragmented.</p><p>You might want to use ping with different packet sizes and the DF bit set to determine the actual smallest MTU of all the links between the client and the bluecoat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '12, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14562" class="comments-container"><span id="14565"></span><div id="comment-14565" class="comment"><div id="post-14565-score" class="comment-score"></div><div class="comment-text"><p>I believe mtu was changed but did not resolve the timed out and i can verify again. It is odd since the client can access all other web sites on the same connection without any issue. Thanks.</p></div><div id="comment-14565-info" class="comment-info"><span class="comment-age">(26 Sep '12, 16:06)</span> <span class="comment-user userinfo">ws2006</span></div></div></div><div id="comment-tools-14562" class="comment-tools"></div><div class="clear"></div><div id="comment-14562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

