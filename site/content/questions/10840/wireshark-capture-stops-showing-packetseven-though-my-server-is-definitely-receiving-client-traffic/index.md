+++
type = "question"
title = "Wireshark capture stops showing packets…even though my server is definitely receiving client traffic"
description = '''0 down vote favorite share [g+] share [fb] share [tw] I&#x27;m looking into a potential network issue. On a dev box I&#x27;ve been noticing mysteriously FIN/ACK and RST/ACKs that are breaking comm between my client and server. However, before I can start to tackle that I need to know why a capture session jus...'''
date = "2012-05-09T08:07:00Z"
lastmod = "2012-05-10T01:38:00Z"
weight = 10840
keywords = [ "windows", "tcp", "wireshark" ]
aliases = [ "/questions/10840" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture stops showing packets…even though my server is definitely receiving client traffic](/questions/10840/wireshark-capture-stops-showing-packetseven-though-my-server-is-definitely-receiving-client-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10840-score" class="post-score" title="current number of votes">0</div><span id="post-10840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>0 down vote favorite share [g+] share [fb] share [tw]</p><p>I'm looking into a potential network issue. On a dev box I've been noticing mysteriously FIN/ACK and RST/ACKs that are breaking comm between my client and server. However, before I can start to tackle that I need to know why a capture session just seems to go dead. Both endpoints are 2008.</p><p>Problem: I'll start a capture session and see all the expected traffic, then after a short period of time, not packets come through anymore...which is wrong because I can see the client's request in my server logs, and my server is taking actions that I can observe based upon these requests. Where are these packets, why can't I see them?</p><p>Here's the filter I'm using when I run wireshark at the server:</p><p>ip.src == [client IP] &amp;&amp; ip.dst == [server IP] &amp;&amp; tcp.port == [listener port on server]</p><p>Note 1: One other note: If I kill WireShark and start it back up it works again for a little bit then stops.</p><p>Note 2: The RST/ACK frames have a win=0, len=0. What should I deduce from this?</p><p>Note 3: There is only one client and one server, so I should be having to worry about organizing chatter between discrete clients.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/c4acaf99aaab88c17accc9ab8ef2f18f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KMarks&#39;s gravatar image" /><p><span>KMarks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KMarks has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '12, 08:13</strong> </span></p></div></div><div id="comments-container-10840" class="comments-container"></div><div id="comment-tools-10840" class="comment-tools"></div><div class="clear"></div><div id="comment-10840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10876"></span>

<div id="answer-container-10876" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10876-score" class="post-score" title="current number of votes">0</div><span id="post-10876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, you should never capture data on either client or server, but use a third device to listen in on the conversation (by using SPAN/Monitor Ports, TAPs, etc). Too many strange things can happen if you do local captures, for example what you're experiencing with the capture showing no further packets. It can be related to local firewalling, too much load on the server, or other things where the OS keeps Wireshark/Dumpcap out of the loop.</p><p>To address your note number 2: RST (Reset) packets always have a window size of zero, and a length of zero. They terminate a communication, and window=0 means "no more receive buffer available", which is consistent with a session termination. Len=0 means "no TCP payload", which is also correct, because a session termination does not have any.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10876" class="comments-container"></div><div id="comment-tools-10876" class="comment-tools"></div><div class="clear"></div><div id="comment-10876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

