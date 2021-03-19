+++
type = "question"
title = "tcp error control problem"
description = '''in this capture file there is strange problem  http://www.mediafire.com/download/ouaxioxglpogd0z/FDR_7_9613.pcap i have two devices one called FDR with ip 105.181.145.115 only sends data to the server with ip 41.32.98.66 in case of packet drop FDR sends retransmission packet why ??? '''
date = "2015-06-05T16:05:00Z"
lastmod = "2015-06-08T23:14:00Z"
weight = 42934
keywords = [ "tcp" ]
aliases = [ "/questions/42934" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcp error control problem](/questions/42934/tcp-error-control-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42934-score" class="post-score" title="current number of votes">0</div><span id="post-42934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in this capture file there is strange problem <a href="http://www.mediafire.com/download/ouaxioxglpogd0z/FDR_7_9613.pcap">http://www.mediafire.com/download/ouaxioxglpogd0z/FDR_7_9613.pcap</a></p><p>i have two devices one called FDR with ip 105.181.145.115 only sends data to the server with ip 41.32.98.66</p><p>in case of packet drop FDR sends retransmission packet why ???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '15, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p><span>shady</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div></div><div id="comments-container-42934" class="comments-container"><span id="42935"></span><div id="comment-42935" class="comment"><div id="post-42935-score" class="comment-score"></div><div class="comment-text"><p>it think something wrong with RTO of FDR</p></div><div id="comment-42935-info" class="comment-info"><span class="comment-age">(05 Jun '15, 17:16)</span> <span class="comment-user userinfo">shady</span></div></div><span id="42936"></span><div id="comment-42936" class="comment"><div id="post-42936-score" class="comment-score">1</div><div class="comment-text"><p>At the first view I would say, common packet loss behaviour. FDR knows what he needs to send because of the ACK of the server. Which packet exactly is suspicious to you?</p></div><div id="comment-42936-info" class="comment-info"><span class="comment-age">(05 Jun '15, 17:46)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="42948"></span><div id="comment-42948" class="comment"><div id="post-42948-score" class="comment-score"></div><div class="comment-text"><p>i agree with you its common packet loss</p><p>when i studied the file i found that in retransmission events ACK packet from server didnt reach FDR so FDR sends retransmission packet to server asking for ACK packet</p><p>is this right ?? Christian_R</p></div><div id="comment-42948-info" class="comment-info"><span class="comment-age">(07 Jun '15, 11:16)</span> <span class="comment-user userinfo">shady</span></div></div></div><div id="comment-tools-42934" class="comment-tools"></div><div class="clear"></div><div id="comment-42934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42951"></span>

<div id="answer-container-42951" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42951-score" class="post-score" title="current number of votes">1</div><span id="post-42951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What I know out of the trace is that the trace is taken on the server.<br />
So from that point I only can talk clear about the server. And I can only asume what the client sees. Because I see only the client packets that reach the server. I asume that the client is a few hops (router) away from the server, because the TTL is at 45 in the client packets.</p><p>It is clear that there are some errors between the server and the client. Packet Loss, Out of Order,... -&gt; Maybe this is due to an instable network, bottlenecks, or ...</p><p>But if I understand your question right than this all is not your question. Right? You want to know why there is the "DUP ACK" in FRAME 17, for example. For the answer I must start in FRAME 7: There is a PACKET with SEQ=111 and LEN=55 wich arrives the server. Afer that the server receives more segments in correct order until FRAME 16. In FRAME 16 he receives the same SEGMENT as he has seen in FRAME 7, but he has received so far Segements till 275. And he is expecting 276. So as an respond to FRAME 16 the server sends in FRAME 17 the ACK with the next expected SEQ number 276. Later in the trace behaviour is still there, but with a few more events around. <img src="https://osqa-ask.wireshark.org/upfiles/Error_KFTSWG9.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '15, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></img></div></div><div id="comments-container-42951" class="comments-container"><span id="42979"></span><div id="comment-42979" class="comment"><div id="post-42979-score" class="comment-score"></div><div class="comment-text"><p>you are great all information you said is exactly right</p><p>check out this report i made <a href="http://www.mediafire.com/view/gdef2p03legeebb/FDR.docx">http://www.mediafire.com/view/gdef2p03legeebb/FDR.docx</a></p><p>i want to be sure that my analysis is right ?</p><p>thank you</p></div><div id="comment-42979-info" class="comment-info"><span class="comment-age">(08 Jun '15, 09:50)</span> <span class="comment-user userinfo">shady</span></div></div></div><div id="comment-tools-42951" class="comment-tools"></div><div class="clear"></div><div id="comment-42951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42994"></span>

<div id="answer-container-42994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42994-score" class="post-score" title="current number of votes">1</div><span id="post-42994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that we face a real packet loss problem here.<br />
The problem is more a combination of the 200ms delayACK timer of the windows server, the nature of the traffic sending 55 bytes every 100ms and the FDR dropping its RTO below 200 ms.<br />
</p><p>Traffic Pattern indicating that the FDR tries to send 10 55-bytes records within 1 second:</p><pre><code>       MMDDYY hhmmss no 
..1113 032914 122001  1 49.4100 49.4087 054.5200 2.9043
..1113 032914 122001  2 49.4111 49.4093 054.5200 2.5333
..1113 032914 122001  3 49.4108 49.4094 054.5090 2.1621
..1113 032914 122001  4 49.4089 49.4086 054.5200 1.7907
..1113 032914 122001  5 49.4087 49.4095 054.5200 1.4194
..1113 032914 122001  6 49.4063 49.4080 054.5090 1.0479
..1113 032914 122001  7 49.4073 49.4090 054.5090 0.6764
..1113 032914 122001  8 49.4073 49.4082 054.5090 0.3046
..1113 032914 122001  9 49.4090 49.4083 054.5200 6.2159
..1113 032914 122001 10 49.4110 49.4092 054.5090 5.8447</code></pre><p>So if everything runs smoothly, we should see a 55 byte (single) segment arriving at 10 0ms intervals.<br />
A single segment is not enough for the windows TCP stack to send an ACK right away so we wait for the next segment to arrive or for the 200 ms delayAck timer to expire, whatever occurs first.<br />
The trace shows that the retransmission timeout in FDR drops below 200 ms which will cause the spurious retransmissions that you see.<br />
So in order to fix this problem (if it still needs fixing after more than a year...) would be to turn off delayed acknowledgements in windows TCP. <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-241.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '15, 22:50</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '15, 22:52</strong> </span></p></div></div><div id="comments-container-42994" class="comments-container"><span id="42995"></span><div id="comment-42995" class="comment"><div id="post-42995-score" class="comment-score"></div><div class="comment-text"><p>(voted up) I was just trying to explaiin the dup ack and not the rest.</p></div><div id="comment-42995-info" class="comment-info"><span class="comment-age">(08 Jun '15, 23:14)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-42994" class="comment-tools"></div><div class="clear"></div><div id="comment-42994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

