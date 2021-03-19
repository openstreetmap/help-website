+++
type = "question"
title = "Plotting TCP Sequence Number Against Timestamp Option Value?"
description = '''Hi there, Does anyone know of a way to take a packet capture and plot TCP sequence numbers against timestamp option values? Thanks, Harry'''
date = "2014-12-07T11:56:00Z"
lastmod = "2014-12-08T05:12:00Z"
weight = 38418
keywords = [ "timestamp", "graph", "plot", "tcp", "sequence" ]
aliases = [ "/questions/38418" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Plotting TCP Sequence Number Against Timestamp Option Value?](/questions/38418/plotting-tcp-sequence-number-against-timestamp-option-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38418-score" class="post-score" title="current number of votes">0</div><span id="post-38418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Does anyone know of a way to take a packet capture and plot TCP sequence numbers against timestamp option values?</p><p>Thanks, Harry</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-plot" rel="tag" title="see questions tagged &#39;plot&#39;">plot</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '14, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/a5fa5410170c0aa99b8373cb4aaf72e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pottedcactus&#39;s gravatar image" /><p><span>pottedcactus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pottedcactus has no accepted answers">0%</span></p></div></div><div id="comments-container-38418" class="comments-container"></div><div id="comment-tools-38418" class="comment-tools"></div><div class="clear"></div><div id="comment-38418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38431"></span>

<div id="answer-container-38431" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38431-score" class="post-score" title="current number of votes">1</div><span id="post-38431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pottedcactus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try the standard TCP Stream Graph, maybe that's "good enough" for your purpose.</p><blockquote><p>Statistics -&gt; TCP Stream Graph -&gt; Time Sequence Graph</p></blockquote><p>Please be aware, that you will get different graphs, if you choose a frame from C-&gt;S versus S-&gt;C!</p><p>If you really need a graph the the TCP timestamp option, you'll have to create the graph yourself.</p><blockquote><p>tshark -nr input.pcap -Y "display filter" -T fields -e frame.number -e tcp.seq -e tcp.options.timestamp.tsval</p></blockquote><p>Please replace "display filter" with the <strong>wireshark display filter</strong> you need to extract data from the right connection in the pcap file.</p><p>Then take that output and feed it into Excel or another spreadsheet software to create the graph.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '14, 05:13</strong> </span></p></div></div><div id="comments-container-38431" class="comments-container"></div><div id="comment-tools-38431" class="comment-tools"></div><div class="clear"></div><div id="comment-38431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

