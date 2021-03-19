+++
type = "question"
title = "Bytes in flight calculation/plotting"
description = '''I&#x27;m trying to plot Bytes in flight using the I/O graph but i&#x27;m not sure what i&#x27;m getting is correct. How does wireshark calculates bytes in flight ? How come when I plot tcp.analysis.bytes_in_flight and ip.dst == &amp;lt; receiver ip&amp;gt;&amp;amp;&amp;amp;tcp.window_size_value I get the same graph?'''
date = "2011-11-24T22:47:00Z"
lastmod = "2011-11-25T14:41:00Z"
weight = 7622
keywords = [ "graph", "tcp" ]
aliases = [ "/questions/7622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in flight calculation/plotting](/questions/7622/bytes-in-flight-calculationplotting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7622-score" class="post-score" title="current number of votes">0</div><span id="post-7622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to plot Bytes in flight using the I/O graph but i'm not sure what i'm getting is correct. How does wireshark calculates bytes in flight ? How come when I plot tcp.analysis.bytes_in_flight and ip.dst == &lt; receiver ip&gt;&amp;&amp;tcp.window_size_value I get the same graph?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p><span>ddayan</span><br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div></div><div id="comments-container-7622" class="comments-container"></div><div id="comment-tools-7622" class="comment-tools"></div><div class="clear"></div><div id="comment-7622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7638"></span>

<div id="answer-container-7638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7638-score" class="post-score" title="current number of votes">1</div><span id="post-7638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you are using the "advanced" graphs to plot the mentioned fields? If not, the IO graph by default will just count packets in each interval that match the given filters. So the values of those fields will not be used in the graph, just amount of packtes.</p><p>If you do use the "advanced" setting in the graphs, which aggregator function are you using? MAX(*)? If so, then plotting the (maximum) value of tcp.analysis.butes_in_fligt will indeed be the same as the (maximum) tcp.window_size value if the sender is filling the pipe completely (and only if you capture on the sender's side of the pipe).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7638" class="comments-container"></div><div id="comment-tools-7638" class="comment-tools"></div><div class="clear"></div><div id="comment-7638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

