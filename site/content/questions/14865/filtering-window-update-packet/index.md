+++
type = "question"
title = "Filtering Window Update-packet"
description = '''Is it possible to filter Window Update-packets with tcpdump? I know that in wireshark the filter is &quot;tcp.analysis.window_update&quot; but I&#x27;m capturing traffic from a server and I can&#x27;t use wireshark. For example the Zero Window packet (tcp.analysis.zero_window) can be filtered with &quot;tcp[14] = 0 &amp;amp;&amp;am...'''
date = "2012-10-10T02:12:00Z"
lastmod = "2012-10-12T00:57:00Z"
weight = 14865
keywords = [ "filter", "window", "tcpdump", "update" ]
aliases = [ "/questions/14865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Window Update-packet](/questions/14865/filtering-window-update-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14865-score" class="post-score" title="current number of votes">0</div><span id="post-14865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to filter Window Update-packets with tcpdump? I know that in wireshark the filter is "tcp.analysis.window_update" but I'm capturing traffic from a server and I can't use wireshark.</p><p>For example the Zero Window packet (tcp.analysis.zero_window) can be filtered with "tcp[14] = 0 &amp;&amp; tcp[15] = 0" in tcpdump. Is there something similar for Window Update?</p><p>-Rakki</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/387f58c09269aee8709bb3d68f33ea93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakki&#39;s gravatar image" /><p><span>rakki</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakki has no accepted answers">0%</span></p></div></div><div id="comments-container-14865" class="comments-container"></div><div id="comment-tools-14865" class="comment-tools"></div><div class="clear"></div><div id="comment-14865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14870"></span>

<div id="answer-container-14870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14870-score" class="post-score" title="current number of votes">1</div><span id="post-14870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>unfortunately that's not possible within tcpdump. There is no special flag or byte you can filter on with a capture filter. A window update is just an ACK with a new window size. tcpdump would need to build internal state about the connection (e.g. the previous window size), to detect the window update, and that is not implemented.</p><p>Why do you need to filter/detect that during the capture process? Can't you just capture everything and then analyse the capture file later? With the text output of tcpdump and scripting, you should be able to detect the window update.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14870" class="comments-container"><span id="14873"></span><div id="comment-14873" class="comment"><div id="post-14873-score" class="comment-score"></div><div class="comment-text"><p>The problem is that there's a lot of traffic and I'll get a 300MB dump file in ~4 minutes if I capture everything. I need only the window update packets from 24 hours of traffic.</p></div><div id="comment-14873-info" class="comment-info"><span class="comment-age">(10 Oct '12, 03:54)</span> <span class="comment-user userinfo">rakki</span></div></div><span id="14878"></span><div id="comment-14878" class="comment"><div id="post-14878-score" class="comment-score"></div><div class="comment-text"><p>o.k. some ideas:</p><p>are you just interested in the fact, that there is a window update (not the packet itself)? If so, a little (perl) script might help. Dump the text output of tcpdump to the perl script, parse everything and build your own state within that perl script for every tcp connection. Then print the timestamp for every window update (plus any other information you need). It's a bit of work, but doable.</p><p>Or even better, use a perl module that can access the packets directly via libpcap, if that's possible on your system.</p></div><div id="comment-14878-info" class="comment-info"><span class="comment-age">(10 Oct '12, 04:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14882"></span><div id="comment-14882" class="comment"><div id="post-14882-score" class="comment-score"></div><div class="comment-text"><p>Not quite. We have a load balancer in front of our servers which generates its own zero window packets (like thousands of them). I need to find out how much delay it generates to the traffic and to do that I need the window update packets too. So what I actually need is the time between each zero window packet and the next window update. I've already done this for a 4 minute capture and it was around 60%.</p><p>I figured I can just capture all ack packets (length 60) and the dump file should stay small enough.</p></div><div id="comment-14882-info" class="comment-info"><span class="comment-age">(10 Oct '12, 05:08)</span> <span class="comment-user userinfo">rakki</span></div></div><span id="14887"></span><div id="comment-14887" class="comment"><div id="post-14887-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I figured I can just capture all ack packets (length 60) and the dump file should stay small enough.</p></blockquote><p>after the tcp session is established almost every packet contains an ACK flag ;-) Anway, if you capture only up to the TCP header, you will limit the amout of data to a level that should work for you and you would still be able to analyze the data.</p></div><div id="comment-14887-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14951"></span><div id="comment-14951" class="comment"><div id="post-14951-score" class="comment-score"></div><div class="comment-text"><p>That would do the trick. Thanks, Kurt.</p></div><div id="comment-14951-info" class="comment-info"><span class="comment-age">(12 Oct '12, 00:57)</span> <span class="comment-user userinfo">rakki</span></div></div></div><div id="comment-tools-14870" class="comment-tools"></div><div class="clear"></div><div id="comment-14870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

