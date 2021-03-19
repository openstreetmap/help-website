+++
type = "question"
title = "Is it the network? ActiveMQ problem"
description = '''Tracking an issue with apache/activeMQ where some messages are expiring in queue rather than being retrieved by the member servers. I don&#x27;t see many errors on the associated interfaces and I seem to have connectivity between all the servers any time I check. I did 5 minute capture of all the TCP 180...'''
date = "2010-12-21T07:27:00Z"
lastmod = "2010-12-22T14:38:00Z"
weight = 1438
keywords = [ "dup", "ack", "tcp" ]
aliases = [ "/questions/1438" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it the network? ActiveMQ problem](/questions/1438/is-it-the-network-activemq-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1438-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tracking an issue with apache/activeMQ where some messages are expiring in queue rather than being retrieved by the member servers.</p><p>I don't see many errors on the associated interfaces and I seem to have connectivity between all the servers any time I check. I did 5 minute capture of all the TCP 18080 traffic and I see alot of TCP DUP ACK and TCP resets. In about 5000 packets I had:</p><p>2591 Chats 835 Notes 349 warnings 0 errors</p><p>Does this look normal or suspect? I know dup acks can represent packet loss. If I assume all of those 349 warnings are packet loss that is about 12.5%.</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags">dup ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '10, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/2289fa3718446717043ac8721eada546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc%20Abel&#39;s gravatar image" /><p>Marc Abel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc Abel has no accepted answers">0%</span></p></div></div><div id="comments-container-1438" class="comments-container"><span id="1463"></span><div id="comment-1463" class="comment"><div id="post-1463-score" class="comment-score"></div><div class="comment-text"><p>You can't have a 12% pkt loss. That's an impossibly high number. If you type "tcp.analysis.flags" display filter, what do you see?</p></div><div id="comment-1463-info" class="comment-info"><span class="comment-age">(22 Dec '10, 17:19)</span> hansangb</div></div><span id="1471"></span><div id="comment-1471" class="comment"><div id="post-1471-score" class="comment-score"></div><div class="comment-text"><p>I see 1184 out of 5037 packets which is closer to 25%. These packets are all duplicate acks and out of order messages.</p></div><div id="comment-1471-info" class="comment-info"><span class="comment-age">(23 Dec '10, 09:25)</span> Marc Abel</div></div><span id="1474"></span><div id="comment-1474" class="comment"><div id="post-1474-score" class="comment-score"></div><div class="comment-text"><p>It's possible that you have a duplex mismatch causing pkt loss. Have you ruled that out? Also, keep in mind that duplicate acks are just that...duplicates. So you may have 25% "error/notices" but you don't have 25% pkt loss.</p><p>There are other possible answers, but rule out the duplex mismatch first.</p></div><div id="comment-1474-info" class="comment-info"><span class="comment-age">(23 Dec '10, 16:51)</span> hansangb</div></div><span id="1480"></span><div id="comment-1480" class="comment"><div id="post-1480-score" class="comment-score"></div><div class="comment-text"><p>If you have a load of duplicate acks and out-of-order packets, then they are most likely duplicates. This can be caused by the way the capture file has been generated (did you span a vlan and inlcuded both directions for instance?).</p><p>Could you run "editcap -d &lt;infile&gt; &lt;outfile&gt;" on the file to remove duplicate packets? Do you still see that many duplicate acks and out-of-order packets when you load &lt;outfile&gt; in Wireshark?</p></div><div id="comment-1480-info" class="comment-info"><span class="comment-age">(24 Dec '10, 17:51)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1438" class="comment-tools"></div><div class="clear"></div><div id="comment-1438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1458"></span>

<div id="answer-container-1458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1458-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a feature from the JMS spec. The reason that messages expire in the queue instead of being delivered to consumers is because they have been marked with a <code>timeToLive</code> by the sender. Check out the JMS docs on this feature via the <a href="http://download.oracle.com/javaee/6/api/javax/jms/MessageProducer.html#setTimeToLive(long)">MessageProducer.html#setTimeToLive() method</a>. By setting the <code>timeToLive</code> on a message, this instructs ActiveMQ to only hold the message for the given amount of time. If the message is not consumed in that amount of time, then it is expired by ActiveMQ and discarded, i.e., consumers will not receive it.</p><p>Bruce</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '10, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/6628a1d00769000acdd5a67686723820?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bsnyder&#39;s gravatar image" /><p>bsnyder<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bsnyder has no accepted answers">0%</span></p></div></div><div id="comments-container-1458" class="comments-container"><span id="1472"></span><div id="comment-1472" class="comment"><div id="post-1472-score" class="comment-score"></div><div class="comment-text"><p>Thank you this is very helpful. Let me get with the developers and see what they say.</p></div><div id="comment-1472-info" class="comment-info"><span class="comment-age">(23 Dec '10, 09:26)</span> Marc Abel</div></div></div><div id="comment-tools-1458" class="comment-tools"></div><div class="clear"></div><div id="comment-1458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

