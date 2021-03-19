+++
type = "question"
title = "How can I draw a &quot;network graph&quot; with Wireshark?"
description = '''I have also same question, suppose we have captured network traffic and if i want see network graph of that traffic. how can we implement that in wireshark. for e.g. i want to see source address and destination address in graph. how to do that?'''
date = "2015-04-04T05:42:00Z"
lastmod = "2015-04-06T03:01:00Z"
weight = 41185
keywords = [ "graph", "network" ]
aliases = [ "/questions/41185" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I draw a "network graph" with Wireshark?](/questions/41185/how-can-i-draw-a-network-graph-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have also same question, suppose we have captured network traffic and if i want see network graph of that traffic. how can we implement that in wireshark. for e.g. i want to see source address and destination address in graph. how to do that?</p></div><div id="question-tags" class="tags-container tags">graph network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '15, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 06 Apr '15, 02:52</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-41185" class="comments-container"><span id="41204"></span><div id="comment-41204" class="comment"><div id="post-41204-score" class="comment-score"></div><div class="comment-text"><p>@ankit: I converted your comment to a question, as the OP of the other question might have lost interest in his question.</p></div><div id="comment-41204-info" class="comment-info"><span class="comment-age">(06 Apr '15, 02:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-41185" class="comment-tools"></div><div class="clear"></div><div id="comment-41185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41205"></span>

<div id="answer-container-41205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41205-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to similar questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/24163/network-topology-graph">https://ask.wireshark.org/questions/24163/network-topology-graph</a><br />
<a href="https://ask.wireshark.org/questions/26805/chart-network-traffic">https://ask.wireshark.org/questions/26805/chart-network-traffic</a><br />
</p></blockquote><p>In short, there are several graphs that you can draw with Wireshark, but probably none of them is what you are looking for. Your question sounds more like a way to create a infrastructure graph (nice image of the whole network, including routers, etc.) or a communication graph (who is talking to whom). In that case, that functionality is not implemented in Wireshark.</p><p>Please check etherape, which is able to draw "communication graphs".</p><blockquote><p><a href="http://etherape.sourceforge.net/">http://etherape.sourceforge.net/</a><br />
</p></blockquote><p>or some other tools/ways to create graphs from pcap files.</p><blockquote><p><a href="https://github.com/mateuszk87/PcapViz">https://github.com/mateuszk87/PcapViz</a><br />
<a href="http://nbviewer.ipython.org/github/SuperCowPowers/workbench/blob/master/workbench/notebooks/PCAP_to_Graph.ipynb">http://nbviewer.ipython.org/github/SuperCowPowers/workbench/blob/master/workbench/notebooks/PCAP_to_Graph.ipynb</a><br />
<a href="http://raffy.ch/blog/2012/03/21/visualizing-packet-captures-for-fun-and-profit/">http://raffy.ch/blog/2012/03/21/visualizing-packet-captures-for-fun-and-profit/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '15, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41205" class="comments-container"></div><div id="comment-tools-41205" class="comment-tools"></div><div class="clear"></div><div id="comment-41205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

