+++
type = "question"
title = "PSH ACK After ACK Acknowledging same frame but time delta is huge"
description = '''hi all, I am debugging intermittent issues between a client and server application (this application is using IE to load images it used to be on windows XP after PC is upgraded to windows 7 IE 8 users complain complans that intermittently image loads slowly. i can only observe that in the pcap file ...'''
date = "2015-08-17T05:50:00Z"
lastmod = "2015-08-18T02:59:00Z"
weight = 45156
keywords = [ "ack", "psh", "after", "packet-capture" ]
aliases = [ "/questions/45156" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PSH ACK After ACK Acknowledging same frame but time delta is huge](/questions/45156/psh-ack-after-ack-acknowledging-same-frame-but-time-delta-is-huge)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45156-score" class="post-score" title="current number of votes">0</div><span id="post-45156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hi all, I am debugging intermittent issues between a client and server application (this application is using IE to load images it used to be on windows XP after PC is upgraded to windows 7 IE 8 users complain complans that intermittently image loads slowly.</p><p>i can only observe that in the pcap file of the client PC during the issue PSH ACK after ACK with same ACK number.</p><p><code>Client -&gt; Server [SYN] Server-&gt; Client [SYN, ACK] Client -&gt; Server [ACK]  Client -&gt; Server [PSH,ACK]  Server -&gt; Client [ACK]  Server-&gt; Client [PSH, ACK] Client -&gt; Server [ACK]  //ack 1233 Client -&gt; Server [PSH,ACK]  //this push ack is acknowledging the same number as previous frame ack 1233 but there is a delay of 19 sec of delay from previous frame which is the cause of the delay.</code></p><p>i am thinking the delay is the client is sending the request slowly. like to check if anyone has seen this issue before and possible causes. thanks in advance</p><p>Client: 10.205.10.58 Server: 10.203.12.144 <img src="https://osqa-ask.wireshark.org/upfiles/P_20150817_202749_F97oZ8I.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-after" rel="tag" title="see questions tagged &#39;after&#39;">after</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '15, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/9953270910610f76ef959de74c5e3977?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pavil1985&#39;s gravatar image" /><p><span>pavil1985</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pavil1985 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Aug '15, 08:15</strong> </span></p></div></div><div id="comments-container-45156" class="comments-container"></div><div id="comment-tools-45156" class="comment-tools"></div><div class="clear"></div><div id="comment-45156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45164"></span>

<div id="answer-container-45164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45164-score" class="post-score" title="current number of votes">0</div><span id="post-45164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first Frame is an normal ACK. And the second marked frame contains new data. The GAP is application related. But I can´t read the times clearly out of the screenshots. It would be better if you could provide a trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '15, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Aug '15, 12:03</strong> </span></p></div></div><div id="comments-container-45164" class="comments-container"><span id="45180"></span><div id="comment-45180" class="comment"><div id="post-45180-score" class="comment-score"></div><div class="comment-text"><p>hi Christian_R,</p><p>Hope this is a better view, apologies for the bad screenshot.</p><p><code> Time    Source          Destination Info</code></p><p><code></code></p><p><code>15:33.3 10.205.10.58    10.203.12.144   58221 &gt; irdmi [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1 15:33.4 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [SYN, ACK] Seq=0 Ack=1 Win=1460 Len=0 MSS=1400 SACK_PERM=1 15:33.4 10.205.10.58    10.203.12.144   58221 &gt; irdmi [ACK] Seq=1 Ack=1 Win=64400 Len=0 15:33.4 10.205.10.58    10.203.12.144   58221 &gt; irdmi [PSH, ACK] Seq=1 Ack=1 Win=64400 Len=1046 15:33.5 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [ACK] Seq=1 Ack=1047 Win=5246 Len=0 15:33.7 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [PSH, ACK] Seq=1 Ack=1047 Win=5246 Len=1232 15:33.9 10.205.10.58    10.203.12.144   58221 &gt; irdmi [ACK] Seq=1047 Ack=1233 Win=63168 Len=0 15:53.1 10.205.10.58    10.203.12.144   58221 &gt; irdmi [PSH, ACK] Seq=1047 Ack=1233 Win=63168 Len=1046 15:53.2 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [ACK] Seq=1233 Ack=2093 Win=6292 Len=0 15:59.6 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [PSH, ACK] Seq=1233 Ack=2093 Win=6292 Len=1232 //delay from previous frame is 19 Sec 15:59.8 10.205.10.58    10.203.12.144   58221 &gt; irdmi [ACK] Seq=2093 Ack=2465 Win=64400 Len=0 16:03.4 10.205.10.58    10.203.12.144   58221 &gt; irdmi [PSH, ACK] Seq=2093 Ack=2465 Win=64400 Len=1046 16:03.5 10.203.12.144   10.205.10.58    irdmi &gt; 58221 [ACK] Seq=2465 Ack=3139 Win=7338 Len=0 16:07.7 10.205.10.58    10.203.12.144   58221 &gt; irdmi [RST, ACK] Seq=3139 Ack=2465 Win=0 Len=0</code></p></div><div id="comment-45180-info" class="comment-info"><span class="comment-age">(17 Aug '15, 18:34)</span> <span class="comment-user userinfo">pavil1985</span></div></div><span id="45189"></span><div id="comment-45189" class="comment"><div id="post-45189-score" class="comment-score"></div><div class="comment-text"><p>Yes there is a huge gap. But the reason can't be seen in this screenshots. Have you checked the logfiles?</p></div><div id="comment-45189-info" class="comment-info"><span class="comment-age">(18 Aug '15, 02:59)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45164" class="comment-tools"></div><div class="clear"></div><div id="comment-45164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

