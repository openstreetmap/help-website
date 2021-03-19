+++
type = "question"
title = "data visualization options in Wireshark"
description = '''Hi, I am wondering what types of data visualization options Wireshark offers beyond IO and Flow graphs. It would be nice to have a &quot;birds-eye view&quot; option in the Statistics menu that let you see network traffic as a true network in link diagram form. And perhaps be able to dynamically change the net...'''
date = "2012-04-01T04:54:00Z"
lastmod = "2012-04-01T11:05:00Z"
weight = 9884
keywords = [ "graph", "visualization" ]
aliases = [ "/questions/9884" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [data visualization options in Wireshark](/questions/9884/data-visualization-options-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9884-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am wondering what types of data visualization options Wireshark offers beyond IO and Flow graphs. It would be nice to have a "birds-eye view" option in the Statistics menu that let you see network traffic as a true network in link diagram form. And perhaps be able to dynamically change the network diagram in response to arbitrary BPF. It is much easier to catch odd / interesting network behavior when looking at the data this way.</p><p>A while back I wrote up a crude POC of this in Perl: see <a href="https://sourceforge.net/projects/netxtract/.">https://sourceforge.net/projects/netxtract/.</a> I find very useful , but the workflow to generate the graphs is very inefficient and ideally the graph would be displayed directly by some in-built Wireshark engine. Is this something other people would find interesting enough for me to begin working on? Thanks,- dorklord.</p></div><div id="question-tags" class="tags-container tags">graph visualization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '12, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/4ba25d97b94eae5fd21e1f4635e88ddf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dorklord&#39;s gravatar image" /><p>dorklord<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dorklord has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '12, 11:06</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9884" class="comments-container"><span id="9888"></span><div id="comment-9888" class="comment"><div id="post-9888-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7018">enhancement request</a> submitted</p></div><div id="comment-9888-info" class="comment-info"><span class="comment-age">(01 Apr '12, 11:07)</span> helloworld</div></div></div><div id="comment-tools-9884" class="comment-tools"></div><div class="clear"></div><div id="comment-9884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9885"></span>

<div id="answer-container-9885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9885-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This isn't really a suitable question for Ask Wireshark. The best thing to do is check the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bug Tracker</a> for any similar requests, and if there is one add your comments to it, else create a new enhancement request.</p><p>Discussions about any such enhancement would then occur on the <a href="https://www.wireshark.org/mailman/listinfo/wireshark-dev">developers mailing list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '12, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9885" class="comments-container"></div><div id="comment-tools-9885" class="comment-tools"></div><div class="clear"></div><div id="comment-9885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9887"></span>

<div id="answer-container-9887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out <a href="https://honeynet.org/node/716">WireViz</a> (a Google Summer of Code 2011 project), which has a pretty straightforward workflow. The user accesses WireViz through a Wireshark menu.</p><ul><li><a href="https://honeynet.org/node/716">More info and source</a></li><li><a href="http://www.youtube.com/watch?v=fU8w0jooIwE">YouTube screencast</a></li></ul><p>This was <a href="http://www.wireshark.org/lists/wireshark-dev/201108/msg00010.html">announced</a> on the Wireshark developers mailing list last year.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '12, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-9887" class="comments-container"><span id="9889"></span><div id="comment-9889" class="comment"><div id="post-9889-score" class="comment-score"></div><div class="comment-text"><p>Cool! Kinda does something similar but graphviz isn't interactive like pajek is. But thanks I'll look at the code whichll probably save me a lot of time figuring out the API, thanks</p></div><div id="comment-9889-info" class="comment-info"><span class="comment-age">(01 Apr '12, 14:37)</span> dorklord</div></div></div><div id="comment-tools-9887" class="comment-tools"></div><div class="clear"></div><div id="comment-9887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

