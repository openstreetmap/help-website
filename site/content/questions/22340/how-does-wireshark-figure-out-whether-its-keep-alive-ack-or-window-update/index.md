+++
type = "question"
title = "How does WireShark figure out whether it&#x27;s keep-alive ack or window update??"
description = '''A tcp keep-alive ack packet is transmitted after a tcp keep-alive packet is received. WireShark usually analyzes and indicates both packets correctly. For example, #428 and #429.  However, I guess sometimes WireShark&#x27;s analysis regards a keep-alive ack packet as a window update packet. For example, ...'''
date = "2013-06-25T22:53:00Z"
lastmod = "2013-06-26T01:42:00Z"
weight = 22340
keywords = [ "flags", "analysis", "tcp" ]
aliases = [ "/questions/22340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does WireShark figure out whether it's keep-alive ack or window update??](/questions/22340/how-does-wireshark-figure-out-whether-its-keep-alive-ack-or-window-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22340-score" class="post-score" title="current number of votes">0</div><span id="post-22340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A tcp keep-alive ack packet is transmitted after a tcp keep-alive packet is received. WireShark usually analyzes and indicates both packets correctly. For example, #428 and #429. However, I guess sometimes WireShark's analysis regards a keep-alive ack packet as a window update packet. For example, look at #2286 which is supposed to be a keep-alive ack packet.</p><pre><code>428  1404.64744  A.ip  B.ip  TCP  68  **[TCP Keep-Alive]** swtp-port2 &gt; 44103 [ACK] Seq=1821 Ack=1261 Win=18 Len=0 TSval=2238040615 TSecr=9119404

429  1404.64761  B.ip  A.ip  TCP  68  **[TCP Keep-Alive ACK]** 44103 &gt; swtp-port2 [ACK] Seq=1261 Ack=1822 Win=308 Len=0 TSval=9209541 TSecr=2237140547

2285 2304.82955  A.ip  B.ip  TCP  52  **[TCP Keep-Alive]** swtp-port2 &gt; 65000 [ACK] Seq=1392 Ack=893 Win=8192 Len=0 TSval=589947877 TSecr=495405251

2286 2304.83016  B.ip  A.ip  TCP  52  **[TCP Window Update]** 65000 &gt; swtp-port2 [ACK] Seq=893 Ack=1393 Win=131072 Len=0 TSval=496304961 TSecr=589047846</code></pre><p>So, does anyone know how WireShark figues out a packet is TCP Keep-Alive ACK or TCP Window Update? or any difference between those two??? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '13, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/5917f634000f6d34e381d42f575ce098?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackBox&#39;s gravatar image" /><p><span>JackBox</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackBox has no accepted answers">0%</span></p></div></div><div id="comments-container-22340" class="comments-container"></div><div id="comment-tools-22340" class="comment-tools"></div><div class="clear"></div><div id="comment-22340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22347"></span>

<div id="answer-container-22347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22347-score" class="post-score" title="current number of votes">0</div><span id="post-22347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your quote is missing a vital information, and that is the packet coming from B.ip of the second conversation before the packet with the Window Update. A Window Update is diagnosed when a TCP packet arrives that has the same sequence number as the last packet and it's only new information is a different window size than the previous packet did. Maybe that packet is also a keep alive ack, but I think only one expert message is shown per info row.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22347" class="comments-container"></div><div id="comment-tools-22347" class="comment-tools"></div><div class="clear"></div><div id="comment-22347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

