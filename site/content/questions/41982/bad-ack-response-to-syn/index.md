+++
type = "question"
title = "bad ACK response to SYN"
description = '''I&#x27;m having a problem with a web server, which causes the web client to occasionally throw a Connection refused exception despite the server being up and listening. This seems to happen when the rate of socket establishment from the client is high enough that the client is reusing ephemeral ports rou...'''
date = "2015-04-30T09:37:00Z"
lastmod = "2015-05-04T09:29:00Z"
weight = 41982
keywords = [ "ack", "reused", "syn", "sequencenumber" ]
aliases = [ "/questions/41982" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [bad ACK response to SYN](/questions/41982/bad-ack-response-to-syn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41982-score" class="post-score" title="current number of votes">0</div><span id="post-41982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having a problem with a web server, which causes the web client to occasionally throw a Connection refused exception despite the server being up and listening. This seems to happen when the rate of socket establishment from the client is high enough that the client is reusing ephemeral ports roughly every couple minutes.</p><p>In packet captures, I note the following unusual sequence around the time of the Connection refused exception:</p><p>Client -- SYN -&gt; Server</p><p>Client &lt;- ACK -- Server</p><p>Client -- RST -&gt; Server</p><p>The server replies to SYN with ACK, rather than SYN,ACK. Furthermore, in this ACK, the acknowledgement number is not the SYN sequence number plus one. Rather, it is the same acknowledgement number last sent by the server in the previous socket that used the same client port. This acknowledgement number falls outside the window, thus eliciting a RST response from the client.</p><p>Wireshark seq/ack analysis marks the erroneous ACK with [TCP ACKed unseen segment] and shows the RST cause as TCPS_SYN_SENT-Bad_seq</p><p>For this service, the server initiates socket close, so all the sockets have the following closing packet sequence:</p><p>1) Server -- FIN,ACK -&gt; Client</p><p>2) Server &lt;--- ACK ---- Client</p><p>3) Server &lt;- FIN,ACK -- Client</p><p>4) Server ---- ACK ---&gt; Client</p><p>and in the problem cases, the acknowledgement number from (4) above is repeated much later in the server's ACK response to the client's SYN request for a new socket.</p><p>The server is running RHEL, and the TIME_WAIT interval is 60 seconds. When I see the problem behavior, the client SYN is sent more than 100 seconds after the closing sequence from the previous time the ephemeral port in the SYN was used, so from the server's point of view the previous connection should be fully closed.</p><p>It looks as if the server sometimes loses track that a connection is closed. Any ideas on what might be wrong?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-reused" rel="tag" title="see questions tagged &#39;reused&#39;">reused</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-sequencenumber" rel="tag" title="see questions tagged &#39;sequencenumber&#39;">sequencenumber</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '15, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/fd1625af7dfcfbc58117af8826427254?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peconnol&#39;s gravatar image" /><p><span>peconnol</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peconnol has no accepted answers">0%</span></p></div></div><div id="comments-container-41982" class="comments-container"></div><div id="comment-tools-41982" class="comment-tools"></div><div class="clear"></div><div id="comment-41982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41993"></span>

<div id="answer-container-41993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41993-score" class="post-score" title="current number of votes">0</div><span id="post-41993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at: <a href="http://serverfault.com/questions/303652/time-wait-connections-not-being-cleaned-up-after-timeout-period-expires">http://serverfault.com/questions/303652/time-wait-connections-not-being-cleaned-up-after-timeout-period-expires</a></p><p>In short, there seems to be code in the Linux kernel that limits the amount of TIME_WAIT connections that can be reaped per second. Setting tcp_tw_reuse to 1 will make the kernel accept a new connection on a port that is still in TIME_WAIT.</p><p>Also, you can increase the port range that can be used on the client, so it takes longer for the client to reuse the same port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-41993" class="comments-container"><span id="42059"></span><div id="comment-42059" class="comment"><div id="post-42059-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I tried this out to see if I can hit the limit on socket reaping but was unable to reproduce the condition described in the referenced URL.</p><p>Would setting SO_REUSEADDR within the server have the same effect as setting tcp_tw_reuse? If so I would prefer to set the socket option so as to limit this change to the service and not the whole server.</p></div><div id="comment-42059-info" class="comment-info"><span class="comment-age">(04 May '15, 09:29)</span> <span class="comment-user userinfo">peconnol</span></div></div></div><div id="comment-tools-41993" class="comment-tools"></div><div class="clear"></div><div id="comment-41993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

