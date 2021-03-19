+++
type = "question"
title = "Strange TCP RST with sslscan"
description = '''I&#x27;m using sslscan to scan a https-site for supported SSL/TLS-versions. If I scan the site via IPv4 I noticed strange pauses between the scans of the different cipher suits. I then scaned the host via IPv6 and no pauses. I then run tcpdump and discovered some strange RST, TCP Retransmission and TCP D...'''
date = "2014-02-16T07:47:00Z"
lastmod = "2014-02-16T10:15:00Z"
weight = 29913
keywords = [ "rst", "ssl", "tcp", "https", "retransmission" ]
aliases = [ "/questions/29913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange TCP RST with sslscan](/questions/29913/strange-tcp-rst-with-sslscan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using <a href="https://github.com/rbsec/sslscan/">sslscan</a> to scan a https-site for supported SSL/TLS-versions. If I scan the site via IPv4 I noticed strange pauses between the scans of the different cipher suits. I then scaned the host via IPv6 and no pauses. I then run tcpdump and discovered some strange RST, TCP Retransmission and TCP DUP ACK?!?. Have a look at <a href="https://www.cloudshark.org/captures/2ec3e51ce9a7">the capture file</a>, especialy starting at line number 63.</p><p>Any idea what can cause this and maybe how to fix the application/my system to faster scan the site?</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags">rst ssl tcp https retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/899541e1a69a524f400a8bd3d6559d27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0xAFFE&#39;s gravatar image" /><p>0xAFFE<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0xAFFE has no accepted answers">0%</span></p></div></div><div id="comments-container-29913" class="comments-container"></div><div id="comment-tools-29913" class="comment-tools"></div><div class="clear"></div><div id="comment-29913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29916"></span>

<div id="answer-container-29916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29916-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please use the following filter</p><blockquote><p>tcp.port == 46639</p></blockquote><p>Then select</p><blockquote><p>Statistics -&gt; Flow Graph</p></blockquote><p>You will see what's going on in that conversation.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/sslscan_small.png" alt="alt text" /></p><p>As you can see, the client sends a SYN and receives an ACK instead of a SYN-ACK. As a result, the client sends a RESET. Then the client tries again, <strong>unfortunately</strong> by using the same source port. That game repeats several times, until the server finally 'recovers' and sends a SYN-ACK.</p><p>There are two problems, that eventually lead to that long scan duration.</p><ul><li>the server does not answer with a SYN-ACK, but instead with an ACK. That's not good ;-) The reason for this is unknown</li><li>the client reuses the same port for the retry (it does not close the socket), which leads to an unnecessary delay, as the wait time for the next retry gets increased (it doubles) by TCP for every retry.</li></ul><p>Now, what can you do to speed things up?</p><ul><li>if you have access to the server (or the firewall/loadbalancer in front of it) you can try to figure out what's wrong with the server</li><li>you can change the code of <a href="https://github.com/rbsec/sslscan/">sslscan</a> in a way that it uses a new connection after it detects that kind of problem, which will lead to a much shorter scan time, even if the problem on the server persists.</li><li>you can write a wrapper for sslscan. As soon as the wrapper detects that specific problem, it will kill the sslscan process and restart it. However, it's probably not that easy to detect the problem.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '14, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-29916" class="comments-container"></div><div id="comment-tools-29916" class="comment-tools"></div><div class="clear"></div><div id="comment-29916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

