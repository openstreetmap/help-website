+++
type = "question"
title = "sync-ack process not completing on windows 2012"
description = '''Hi! From windows 2012 I am trying to telnet to destination on specific port and its not working. I can do telnet from win 7 win 2008 from the same network. I did capture on win 2012 and looks like the win 2012 is not sending ACK. 19452 0.000270000 5.730763000 SRC Dst 64569 25000 TCP 64569 &amp;gt; 25000...'''
date = "2014-04-11T07:53:00Z"
lastmod = "2014-04-14T03:00:00Z"
weight = 31753
keywords = [ "windows", "sync-ack", "2012" ]
aliases = [ "/questions/31753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [sync-ack process not completing on windows 2012](/questions/31753/sync-ack-process-not-completing-on-windows-2012)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31753-score" class="post-score" title="current number of votes">1</div><span id="post-31753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>From windows 2012 I am trying to telnet to destination on specific port and its not working. I can do telnet from win 7 win 2008 from the same network. I did capture on win 2012 and looks like the win 2012 is not sending ACK.</p><pre><code>19452   0.000270000 5.730763000 SRC Dst 64569   25000   TCP 64569 &gt; 25000 [SYN, ECN, CWR] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1  19452

29390   0.000100000 8.737071000 SRC Dst 64569   25000   TCP [TCP Retransmission] 64569 &gt; 25000 [SYN, ECN, CWR] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 29390

29753   0.000484000 8.849849000 DST SRC 25000   64569   TCP 25000 &gt; 64569 [ACK] Seq=1 Ack=1 Win=32775 Len=0 29753

48941   0.000538000 14.734428000    SRC DST 64569   25000   TCP [TCP Retransmission] 64569 &gt; 25000 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1  48941

49454   0.000033000 14.847287000    DST SRC 25000   64569   TCP [TCP Dup ACK 29753#1] 25000 &gt; 64569 [ACK] Seq=1 Ack=1 Win=32775 Len=0   49454</code></pre><p>I have changed the IP address to SRC and DST</p><p>Src = windows 2012 from where i am doing telnet dst 25000</p><p>Anyone can help.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-sync-ack" rel="tag" title="see questions tagged &#39;sync-ack&#39;">sync-ack</span> <span class="post-tag tag-link-2012" rel="tag" title="see questions tagged &#39;2012&#39;">2012</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '14, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/4da86d80e318819f883001822857d369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="capricorn800&#39;s gravatar image" /><p><span>capricorn800</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="capricorn800 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Apr '14, 03:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31753" class="comments-container"></div><div id="comment-tools-31753" class="comment-tools"></div><div class="clear"></div><div id="comment-31753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31758"></span>

<div id="answer-container-31758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31758-score" class="post-score" title="current number of votes">2</div><span id="post-31758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try disabling ECN on windows 2012 by issuing</p><p>netsh interface tcp set global ecncapability=disabled</p><p>See <a href="http://serverfault.com/questions/526377/is-ecn-explicit-congestion-notification-turned-on-by-default-on-windows-server">http://serverfault.com/questions/526377/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '14, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-31758" class="comments-container"><span id="31780"></span><div id="comment-31780" class="comment"><div id="post-31780-score" class="comment-score"></div><div class="comment-text"><p>Thanks the answer helped and fixed the problem.</p></div><div id="comment-31780-info" class="comment-info"><span class="comment-age">(14 Apr '14, 02:04)</span> <span class="comment-user userinfo">capricorn800</span></div></div><span id="31784"></span><div id="comment-31784" class="comment"><div id="post-31784-score" class="comment-score"></div><div class="comment-text"><p><span>@capricorn800</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-31784-info" class="comment-info"><span class="comment-age">(14 Apr '14, 03:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-31758" class="comment-tools"></div><div class="clear"></div><div id="comment-31758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

