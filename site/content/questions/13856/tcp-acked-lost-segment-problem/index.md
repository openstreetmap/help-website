+++
type = "question"
title = "TCP ACKed lost segment problem"
description = '''Hi Guys, i am using wireshark check an issue we have with slow connectivity to our server and sometimes server have to restart. I am see a lot of the following lines in the capture and i wondered if anyone could explain what they are: 39 TCP src &amp;gt; 38378 [PSH, ACK] Seq=1786 Ack=1726 Win=32768 Len=...'''
date = "2012-08-24T00:10:00Z"
lastmod = "2012-08-24T12:42:00Z"
weight = 13856
keywords = [ "connectivity", "psh", "problem", "tcp", "capture" ]
aliases = [ "/questions/13856" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed lost segment problem](/questions/13856/tcp-acked-lost-segment-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13856-score" class="post-score" title="current number of votes">0</div><span id="post-13856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>i am using wireshark check an issue we have with slow connectivity to our server and sometimes server have to restart. I am see a lot of the following lines in the capture and i wondered if anyone could explain what they are:</p><p>39 TCP src &gt; 38378 [PSH, ACK] Seq=1786 Ack=1726 Win=32768 Len=119</p><p>40 TCP 38378 &gt; src [ACK] Seq=1726 Ack=1905 Win=54 Len=0</p><p>41 TCP [TCP ACKed lost segment] src &gt; 38378 [PSH, ACK] Seq=1905 Ack=1841 Win=32768 Len=119</p><p>42 TCP [TCP ACKed lost segment] src &gt; 38378 [PSH, ACK] Seq=2024 Ack=1956 Win=32768 Len=119</p><p>43 TCP [TCP ACKed lost segment] src &gt; 38378 [PSH, ACK] Seq=2143 Ack=2071 Win=32768 Len=119</p><p>44 TCP [TCP ACKed lost segment] src &gt; 38378 [PSH, ACK] Seq=2262 Ack=2186 Win=32768 Len=119</p><p>Best Regards</p><p>Spyros</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-connectivity" rel="tag" title="see questions tagged &#39;connectivity&#39;">connectivity</span> <span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '12, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/529dc11980b2a0b9331d7724f05f7df8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaito7&#39;s gravatar image" /><p><span>kaito7</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaito7 has no accepted answers">0%</span></p></div></div><div id="comments-container-13856" class="comments-container"></div><div id="comment-tools-13856" class="comment-tools"></div><div class="clear"></div><div id="comment-13856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13859"></span>

<div id="answer-container-13859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13859-score" class="post-score" title="current number of votes">0</div><span id="post-13859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"ACKed lost segment" means that Wireshark has found a packet acknowledging another packet it hasn't seen. Kind of a "I know the packet must have been there but I didn't see it". If that happens it usually means that you either captured on a link that didn't transport all packets (for example when there is asynchronous routing or an etherchannel where you only sniffed on one leg), or your capture device was too slow to record all packets in time that arrived at the NIC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13859" class="comments-container"><span id="13863"></span><div id="comment-13863" class="comment"><div id="post-13863-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and sometimes server have to restart</p></blockquote><p>additionally to what Jasper said: If the servers have to <strong>restart</strong>, there could be a problem with IP stack or NIC driver of that server.</p></div><div id="comment-13863-info" class="comment-info"><span class="comment-age">(24 Aug '12, 02:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13881"></span><div id="comment-13881" class="comment"><div id="post-13881-score" class="comment-score"></div><div class="comment-text"><p>Ping google and check if you have packet loss, I,e..</p><p><strong>"ping <a href="http://google.com">google.com</a> -t"</strong></p></div><div id="comment-13881-info" class="comment-info"><span class="comment-age">(24 Aug '12, 12:42)</span> <span class="comment-user userinfo">Harsha</span></div></div></div><div id="comment-tools-13859" class="comment-tools"></div><div class="clear"></div><div id="comment-13859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

