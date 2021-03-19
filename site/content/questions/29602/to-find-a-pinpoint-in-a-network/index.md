+++
type = "question"
title = "To find a pinpoint in a Network."
description = '''I have 3 sites, in which I am getting some latency accessing the remote server from third location to first server. Just to elaborate.  Lets say, I have three site A, B &amp;amp; C. Flow id from C-&amp;gt;B-&amp;gt;A. where C to B is a point to point connection and B to A is MPLS network. My users from C are ac...'''
date = "2014-02-10T02:08:00Z"
lastmod = "2014-02-10T06:33:00Z"
weight = 29602
keywords = [ "traffic-flow", "traffic-analysis", "bottleneck", "pinpoint" ]
aliases = [ "/questions/29602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [To find a pinpoint in a Network.](/questions/29602/to-find-a-pinpoint-in-a-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29602-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 3 sites, in which I am getting some latency accessing the remote server from third location to first server. Just to elaborate. Lets say, I have three site A, B &amp; C. Flow id from C-&gt;B-&gt;A. where C to B is a point to point connection and B to A is MPLS network. My users from C are accessing servers located at A, for which I am getting some issues. I used WIRESHARK at C site with port-mirroring to find out the flow of traffic. Will that be helpful..?</p></div><div id="question-tags" class="tags-container tags">traffic-flow traffic-analysis bottleneck pinpoint</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/15b6ec1317158903835d87041ee62481?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NBT&#39;s gravatar image" /><p>NBT<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NBT has no accepted answers">0%</span></p></div></div><div id="comments-container-29602" class="comments-container"></div><div id="comment-tools-29602" class="comment-tools"></div><div class="clear"></div><div id="comment-29602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29631"></span>

<div id="answer-container-29631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29631-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I used WIRESHARK at C site with port-mirroring to find out the flow of traffic. <strong>Will that be helpful..?</strong></p></blockquote><p>It depends on the problem.</p><p>It would be better to capture traffic at site C and A at the same time. Then you will be able to figure out if there are any frames missing (dropped somewhere).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29631" class="comments-container"></div><div id="comment-tools-29631" class="comment-tools"></div><div class="clear"></div><div id="comment-29631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

