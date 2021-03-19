+++
type = "question"
title = "How to use wireshark to plot traffic between 2 endpoint IP"
description = '''I have seen statistics in wireshark but what I really want is to plot a line graph showing the traffic between 1 source IP and 1 destination IP. Wonder if wireshark can help me plot this.'''
date = "2013-02-25T17:39:00Z"
lastmod = "2013-02-25T18:48:00Z"
weight = 18871
keywords = [ "plot", "nodes", "statistics", "graph" ]
aliases = [ "/questions/18871" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to use wireshark to plot traffic between 2 endpoint IP](/questions/18871/how-to-use-wireshark-to-plot-traffic-between-2-endpoint-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18871-score" class="post-score" title="current number of votes">0</div><span id="post-18871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have seen statistics in wireshark but what I really want is to plot a line graph showing the traffic between 1 source IP and 1 destination IP. Wonder if wireshark can help me plot this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plot" rel="tag" title="see questions tagged &#39;plot&#39;">plot</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '13, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/e0420cef772b3a3d1aed16780f6c0fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user5462&#39;s gravatar image" /><p><span>user5462</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user5462 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '13, 18:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-18871" class="comments-container"></div><div id="comment-tools-18871" class="comment-tools"></div><div class="clear"></div><div id="comment-18871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18872"></span>

<div id="answer-container-18872" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18872-score" class="post-score" title="current number of votes">0</div><span id="post-18872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Let me try to answer: Go to Statistics on Menu and scroll down for Flow_Graph.Click on that and it will give options for plotting the type of flow(General Flow or TCP Flow).If you are looking for tcp flow between client and server you can identify the stream you want to plot(Right click on SYN Packet and do follow tcp stream) and plot that particular conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '13, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-18872" class="comments-container"></div><div id="comment-tools-18872" class="comment-tools"></div><div class="clear"></div><div id="comment-18872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18873"></span>

<div id="answer-container-18873" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18873-score" class="post-score" title="current number of votes">0</div><span id="post-18873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have not used it myself, but <a href="http://www.honeynet.org/node/716">wireviz</a> looks interesting. It's not an official part of Wireshark (yet?), but you might be able to download the binary packages if you happen to be working on one of the supported distributions; otherwise you'd have to download the sources and compile Wireshark yourself. The author is a Wireshark core member, so maybe if there's sufficient interest, one or more of his projects will be incorporated into the official Wireshark distribution one day.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '13, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18873" class="comments-container"></div><div id="comment-tools-18873" class="comment-tools"></div><div class="clear"></div><div id="comment-18873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18874"></span>

<div id="answer-container-18874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18874-score" class="post-score" title="current number of votes">0</div><span id="post-18874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Select Statistics &gt; IO Graph. You will see a line graph of all traffic in the trace file. By default, it will show Packets per Second. You can change this to Bytes per Second or Bits per Second, as desired.</p><p>To limit the graph to traffic from one source IP address to one destination IP address, enter this filter in the Graph 1 filter area: "ip.src == <em>x.x.x.x</em> &amp;&amp; ip.dst == <em>y.y.y.y</em>", where <em>x.x.x.x</em> is the source IP address and <em>y.y.y.y</em> is the destination IP address. Click the Graph 1 button twice, once to turn it off, and again to turn it back on, which will apply the filter you just entered.</p><p>Note that this filter will show traffic in one direction only, which is what you asked for. If what you really want is to see all traffic between two IP addresses in both directions, then the filter would be "ip.addr == x.x.x.x &amp;&amp; ip.addr == y.y.y.y"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '13, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '13, 18:50</strong> </span></p></div></div><div id="comments-container-18874" class="comments-container"></div><div id="comment-tools-18874" class="comment-tools"></div><div class="clear"></div><div id="comment-18874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

