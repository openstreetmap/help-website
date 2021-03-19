+++
type = "question"
title = "Strange results from Statistics"
description = '''Hi, I need to have a graph for bandwith usage while the client uses a webapp. I captured all packets from the client to the proxy (on the proxy). But the graph in IO Graph show much more traffic for the one client as the router, between all clients and the proxy, for the whole net. Then I tried to g...'''
date = "2013-10-28T08:32:00Z"
lastmod = "2013-10-29T04:15:00Z"
weight = 26469
keywords = [ "bandwidth", "statistics" ]
aliases = [ "/questions/26469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange results from Statistics](/questions/26469/strange-results-from-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26469-score" class="post-score" title="current number of votes">0</div><span id="post-26469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need to have a graph for bandwith usage while the client uses a webapp. I captured all packets from the client to the proxy (on the proxy).</p><p>But the graph in IO Graph show much more traffic for the one client as the router, between all clients and the proxy, for the whole net.</p><p>Then I tried to get the usage per second from tshark</p><pre><code>tshark.exe -nr &quot;&lt;File&gt;&quot;  -z &quot;io,stat,1,ip.dst==client&amp;&amp;ip.src==proxy&quot;</code></pre><p>But the result is strange too. I often have very huge numbers at the end which can't be true. For example:</p><pre><code>=======================================================  
| IO Statistics                                       |  
|                                                     |  
| Interval size: 1 secs                               |  
| Col 1: Frames and bytes                             |  
|     2: ip.dst==client&amp;&amp;ip.src==proxy                |  
|-----------------------------------------------------|  
|              |1                 |2                | |  
| Interval     | Frames |  Bytes  | Frames |  Bytes | |  
|---------------------------------------------------| |  
...  
| 138  4 &lt;&gt; 1385 |    0 |       0 |    0 | 64848607 | |  
| 1385 &lt;&gt; 1386 |     27 |   24532 |    0 | 64848607 | |  
| 1386 &lt;&gt; 1387 |    450 |  425266 |    0 | 64848607 | |  
| 1387 &lt;&gt; 1388 |    891 |  836781 |    0 | 64848607 | |  
| 1388 &lt;&gt; 1389 |    234 |  227972 |    0 | 64848607 | |  
| 1389 &lt;&gt; 1390 |    261 |  253114 |    0 | 64848607 | |  
| 1390 &lt;&gt; 1391 |   1588 | 1514653 |    0 | 64848607 | |  
| 1391 &lt;&gt; 1391 |    170 |  163242 |    0 | 13248269094487389 | |  
=======================================================</code></pre><p>Also, why there is an amount of 0 Frames but still a value for Bytes?</p><p>The client used only the webapp while capture.</p><p>My goal is to see the peaks for traffic. The average usage I got from Summary already.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/7eb556c7e91a900e15fbd0827e372d35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crocom&#39;s gravatar image" /><p><span>crocom</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crocom has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '13, 08:36</strong> </span></p></div></div><div id="comments-container-26469" class="comments-container"></div><div id="comment-tools-26469" class="comment-tools"></div><div class="clear"></div><div id="comment-26469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26477"></span>

<div id="answer-container-26477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26477-score" class="post-score" title="current number of votes">1</div><span id="post-26477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Also, why there is an amount of 0 Frames but still a value for Bytes?</p></blockquote><p>That's obviously a bug. What is your</p><ul><li>OS and version</li><li>Wireshark version (tshark -v)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-26477" class="comments-container"><span id="26499"></span><div id="comment-26499" class="comment"><div id="post-26499-score" class="comment-score"></div><div class="comment-text"><p>Version 1.8.6 (SVN Rev 48142 from /trunk-1.8) <a href="http://pastebin.com/tv5Q14N7">http://pastebin.com/tv5Q14N7</a></p><p>I have updated to the last stable 1.10.2 and now I get 0 Bytes for 0 Frames. Merci :)</p><p>But the IO Graph is still wrong. There are peaks at over 1mbit although the ethernet line only has a max. of 1mbit <a href="http://picload.org/image/ocpglrg/iograph.png">http://picload.org/image/ocpglrg/iograph.png</a></p></div><div id="comment-26499-info" class="comment-info"><span class="comment-age">(29 Oct '13, 01:24)</span> <span class="comment-user userinfo">crocom</span></div></div><span id="26507"></span><div id="comment-26507" class="comment"><div id="post-26507-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But the IO Graph is still wrong.</p></blockquote><p>There are some possible reason for this. Please see here:</p><blockquote><p><a href="http://ask.wireshark.org/questions/25349/utilization-graph-shows-more-than-the-actual-bandwidth">http://ask.wireshark.org/questions/25349/utilization-graph-shows-more-than-the-actual-bandwidth</a></p></blockquote></div><div id="comment-26507-info" class="comment-info"><span class="comment-age">(29 Oct '13, 04:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26477" class="comment-tools"></div><div class="clear"></div><div id="comment-26477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

