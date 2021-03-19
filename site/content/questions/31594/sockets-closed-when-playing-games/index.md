+++
type = "question"
title = "Sockets closed when playing games"
description = '''I&#x27;ve been having this issue lately where I am playing two games(EVE Online and Diablo 3) and at random times for EVE Online I will get the error that the Sockets were closed and for Diablo 3 I get Error 3007(Which happens at the same time) The customer support of CCP told me that when sockets close ...'''
date = "2014-04-07T04:28:00Z"
lastmod = "2014-04-08T05:36:00Z"
weight = 31594
keywords = [ "closes", "game", "sockets" ]
aliases = [ "/questions/31594" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sockets closed when playing games](/questions/31594/sockets-closed-when-playing-games)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31594-score" class="post-score" title="current number of votes">0</div><span id="post-31594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been having this issue lately where I am playing two games(EVE Online and Diablo 3) and at random times for EVE Online I will get the error that the Sockets were closed and for Diablo 3 I get Error 3007(Which happens at the same time)</p><p>The customer support of CCP told me that when sockets close it means I was unable to send or receive 5 consecutive packages. Error 3007 can occur when a computer is unable to maintain a stable connection to the Battle.net servers.</p><p>When this occurs I don't seem to loose internet connection. I ran Wireshark and close to the before receiving error 3007 I sent out an ARP to the address of my modem. Shortly after I sent out an TCP (RST, ACK) package and lost connection.</p><p>I also get allot of TCP Retransmissions close to when this occurs.</p><p>Is any of this related to eachother?</p><p>I would be very grateful if anyone could help me in resolving this issue!</p><p>Thanks in advance</p><ul><li>Xavier</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-closes" rel="tag" title="see questions tagged &#39;closes&#39;">closes</span> <span class="post-tag tag-link-game" rel="tag" title="see questions tagged &#39;game&#39;">game</span> <span class="post-tag tag-link-sockets" rel="tag" title="see questions tagged &#39;sockets&#39;">sockets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '14, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/6335481025ba9e5ab8535e24af5beda3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XavierCZBE&#39;s gravatar image" /><p><span>XavierCZBE</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XavierCZBE has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '14, 04:37</strong> </span></p></div></div><div id="comments-container-31594" class="comments-container"><span id="31598"></span><div id="comment-31598" class="comment"><div id="post-31598-score" class="comment-score"></div><div class="comment-text"><p>Please upload a packet capture.</p></div><div id="comment-31598-info" class="comment-info"><span class="comment-age">(07 Apr '14, 11:47)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31627"></span><div id="comment-31627" class="comment"><div id="post-31627-score" class="comment-score"></div><div class="comment-text"><p>321584 2766.266395000 192.168.0.184 80.239.208.193 TCP 65 [TCP Retransmission] 19345 &gt; bnetgame [PSH, ACK] Seq=1661 Ack=4396 Win=62955 Len=11</p><pre><code>321636  2766.974108000  AsrockIn_3b:57:5f   CompalBr_aa:5a:40   ARP 42  Who has 192.168.0.1?  Tell 192.168.0.184

321637  2766.974440000  CompalBr_aa:5a:40   AsrockIn_3b:57:5f   ARP 60  192.168.0.1 is at 5c:35:3b:aa:5a:40

321674  2767.549450000  192.168.0.184   80.239.210.248  TCP 54  21098 &gt; bnetgame [RST, ACK] Seq=122846 Ack=3862090 Win=0 Len=0

321740  2771.068117000  192.168.0.184   80.239.208.193  TCP 65  [TCP Retransmission] 19345 &gt; bnetgame [PSH, ACK] Seq=1661 Ack=4396 Win=62955 Len=11

321745  2771.434462000  192.168.0.184   173.194.65.138  TCP 55  [TCP Keep-Alive] 20987 &gt; https [ACK] Seq=29221 Ack=13431 Win=65536 Len=1

321746  2771.463004000  173.194.65.138  192.168.0.184   TCP 66  [TCP Keep-Alive ACK] https &gt; 20987 [ACK] Seq=13431 Ack=29222 Win=42880 Len=0 SLE=29221 SRE=29222</code></pre></div><div id="comment-31627-info" class="comment-info"><span class="comment-age">(08 Apr '14, 04:21)</span> <span class="comment-user userinfo">XavierCZBE</span></div></div></div><div id="comment-tools-31594" class="comment-tools"></div><div class="clear"></div><div id="comment-31594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31632"></span>

<div id="answer-container-31632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31632-score" class="post-score" title="current number of votes">0</div><span id="post-31632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like the client has exhausted its retransmission retries and therefore closes its socket after not having received an ACKnowledgment from the bnetgame server.</p><p>So, to answer your question: Yes, the retransmissions and the RST packets are related.</p><p>Why don't you get ACKs back?</p><ul><li>either the server never saw your segments as they were dropped in the network</li><li>or the server saw your segment and did not respond to it (dropped it internally)</li><li>or the server sent the ACKs and they were dropped in the network</li></ul><p>Not an easy task to figure this one out - from a client's perspective</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '14, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '14, 06:31</strong> </span></p></div></div><div id="comments-container-31632" class="comments-container"><span id="31634"></span><div id="comment-31634" class="comment"><div id="post-31634-score" class="comment-score"></div><div class="comment-text"><p>I see. You have any idea what could be causing this?</p></div><div id="comment-31634-info" class="comment-info"><span class="comment-age">(08 Apr '14, 05:36)</span> <span class="comment-user userinfo">XavierCZBE</span></div></div></div><div id="comment-tools-31632" class="comment-tools"></div><div class="clear"></div><div id="comment-31632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

