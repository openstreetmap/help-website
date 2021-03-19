+++
type = "question"
title = "Network Topology Graph"
description = '''Is there any wireshark plugin to get network topology graph ????????????'''
date = "2013-08-29T05:43:00Z"
lastmod = "2013-08-30T04:30:00Z"
weight = 24163
keywords = [ "graph", "topolgy" ]
aliases = [ "/questions/24163" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Network Topology Graph](/questions/24163/network-topology-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24163-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any wireshark plugin to get network topology graph ????????????</p></div><div id="question-tags" class="tags-container tags">graph topolgy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/efae611d18abd263ac8cbc9b44368bdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkbeginner&#39;s gravatar image" /><p>wiresharkbeg...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkbeginner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 29 Aug '13, 06:13</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24163" class="comments-container"><span id="24164"></span><div id="comment-24164" class="comment"><div id="post-24164-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-24164-info" class="comment-info"><span class="comment-age">(29 Aug '13, 06:14)</span> grahamb ♦</div></div></div><div id="comment-tools-24163" class="comment-tools"></div><div class="clear"></div><div id="comment-24163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24185"></span>

<div id="answer-container-24185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24185-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no feature in Wireshark to create a <strong>network topology graph</strong>.</p><p>The best you can do is to have a look at</p><blockquote><p>Statistics -&gt; Endpoints<br />
Statistics -&gt; Conversations</p></blockquote><p>See also the answers to other, similar questions.</p><blockquote><p><a href="http://ask.wireshark.org/questions/20777/how-to-determine-the-network-topology-in-a-capture">http://ask.wireshark.org/questions/20777/how-to-determine-the-network-topology-in-a-capture</a><br />
<a href="http://ask.wireshark.org/questions/249/topology-map-gui-or-otherwise">http://ask.wireshark.org/questions/249/topology-map-gui-or-otherwise</a></p></blockquote><p>Furthermore it (usually) does not make much sense to build a topology map from a single capture file, as in the vast majority of cases you will have only traffic of one network segment in a capture file, and with that data the map would be a flat picture of the nodes in that segment and possibly some communication endpoints outside that segment. This is basically what the both Statistics methods return (see above).</p><p>To be able to build a '<a href="http://en.wikipedia.org/wiki/Network_topology">network topology map</a>' of a larger network, you would need a lot of information (capture data) from every segment.</p><p>However, instead of using capture data it is probably much easier to use (commercial) tools that probe the network and try to create a map from that data. Google will list some of those tools: <a href="https://www.google.com/?q=automatic+network+topology+mapping+tools">https://www.google.com/?q=automatic+network+topology+mapping+tools</a></p><p>One interesting free tool is <a href="http://nmap.org/">nmap</a> with its topology map in the GUI.</p><blockquote><p><a href="http://nmap.org/book/zenmap-topology.html">http://nmap.org/book/zenmap-topology.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '13, 01:53</p></div></div><div id="comments-container-24185" class="comments-container"></div><div id="comment-tools-24185" class="comment-tools"></div><div class="clear"></div><div id="comment-24185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24194"></span>

<div id="answer-container-24194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I run EtherApe at the same time to <em>see</em> the topology, then compare its log to the concurrent wireshark log to see what data was sent. It could be made simpler, but its something. Just a quick thought.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/14f060b714d9f178abe918e5f391dedb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdrianThePhotog&#39;s gravatar image" /><p>AdrianThePhotog<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdrianThePhotog has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-24194" class="comments-container"></div><div id="comment-tools-24194" class="comment-tools"></div><div class="clear"></div><div id="comment-24194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

