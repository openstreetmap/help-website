+++
type = "question"
title = "tcpdump output: FPU and R flags"
description = '''10:53:04.042608 IP 172.17.2.12.42654 &amp;gt; 172.17.2.6.6000: Flags [FPU], seq 3891587770, win 1024, urg 0, length 0 10:53:04.045939 IP 172.17.2.6.6000 &amp;gt; 172.17.2.12.42654: Flags [R.], seq 0, ack 3891587770, win 0, length 0 Between these two packets I am looking for the set flags and what they mean....'''
date = "2014-03-22T13:09:00Z"
lastmod = "2014-03-22T14:03:00Z"
weight = 31080
keywords = [ "tcpdump", "flags" ]
aliases = [ "/questions/31080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump output: FPU and R flags](/questions/31080/tcpdump-output-fpu-and-r-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31080-score" class="post-score" title="current number of votes">0</div><span id="post-31080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>10:53:04.042608 IP 172.17.2.12.42654 &gt; 172.17.2.6.6000: Flags [FPU], seq 3891587770, win 1024, urg 0, length 0</p><p>10:53:04.045939 IP 172.17.2.6.6000 &gt; 172.17.2.12.42654: Flags [R.], seq 0, ack 3891587770, win 0, length 0</p><p>Between these two packets I am looking for the set flags and what they mean... What I am assuming is the flags are FPU and R as the packets state, but I am not familiar with these flags and cannot seem to find an answer to what they are anywhere else. Would anyone know what flags they are?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '14, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/c532626018ac1121eceb977743e3bf0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cashmen&#39;s gravatar image" /><p><span>Cashmen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cashmen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '14, 14:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-31080" class="comments-container"></div><div id="comment-tools-31080" class="comment-tools"></div><div class="clear"></div><div id="comment-31080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31083"></span>

<div id="answer-container-31083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31083-score" class="post-score" title="current number of votes">0</div><span id="post-31083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you are showing is the output of tcpdump and the flags are documented in the <a href="http://www.tcpdump.org/manpages/tcpdump.1.html">man page of tcpdump</a>.</p><p>In short (from the man page):<br />
</p><blockquote><p><code>S (SYN), F (FIN), P (PUSH), R (RST), U (URG), W (ECN CWR), E (ECN-Echo) or . (ACK)</code></p></blockquote><p>For a better understanding of the flags, please visit online resources like the following, and <strong>many</strong> others.</p><blockquote><p><a href="http://www.tcpipguide.com/free/t_TCPIPTransmissionControlProtocolTCP.htm">http://www.tcpipguide.com/free/t_TCPIPTransmissionControlProtocolTCP.htm</a><br />
<a href="http://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/">http://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/</a><br />
<a href="http://www.firewall.cx/networking-topics/protocols/tcp/136-tcp-flag-options.html">http://www.firewall.cx/networking-topics/protocols/tcp/136-tcp-flag-options.html</a></p></blockquote><p>So, what you are seeing is:</p><ul><li>172.17.2.12 sends a TCP frame to 172.17.2.6:6000 with the flags FIN,PUSH,URG</li><li>the answer from 172.17.2.6 is a RST,ACK (RESET + ACK)</li></ul><p>So, one side is closing the connection with a FIN (plus other flags) and the other side 'answers' with a RESET. <strong>Why</strong> it happens in that way can only be answered by looking at the applications and operating systems in use.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '14, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '14, 14:17</strong> </span></p></div></div><div id="comments-container-31083" class="comments-container"></div><div id="comment-tools-31083" class="comment-tools"></div><div class="clear"></div><div id="comment-31083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

