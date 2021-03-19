+++
type = "question"
title = "IO Graph ICMP response times?"
description = '''So what I&#x27;d like is a graph of the average response time (given by the icmp.resptime field). This seems to work fine in the main capture window, but in the IO graphs I get odd results. When I use &#x27;AVG(Y Field)&#x27;, the line stays pegged to 0, and the only way I can get it to show up at all is with &#x27;SUM...'''
date = "2016-04-08T06:35:00Z"
lastmod = "2016-04-08T06:35:00Z"
weight = 51510
keywords = [ "response", "iograph" ]
aliases = [ "/questions/51510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IO Graph ICMP response times?](/questions/51510/io-graph-icmp-response-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So what I'd like is a graph of the average response time (given by the <code>icmp.resptime</code> field). This seems to work fine in the main capture window, but in the IO graphs I get odd results. When I use 'AVG(Y Field)', the line stays pegged to 0, and the only way I can get it to show up at all is with 'SUM(Y Field)' (shown here) or 'MAX(Y Field)' which just generates a dozen or so spikes (they all seem to hit exactly 1, or exactly 2). EDIT: I should clarify that in the actual trace file, there's 5000+ responses that I'd expect to be averaged into the graph.</p><p>This seems pretty wacky to me, but maybe I'm doing it wrong. Ideas? <img src="http://imgur.com/UiUTymm.png" alt="alt text" /></p><p><img src="http://imgur.com/j0z2uzT.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">response iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/8c8bb4331d25d8ed8241358cecc41b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="W-George&#39;s gravatar image" /><p>W-George<br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="W-George has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '16, 06:38</p></div></div><div id="comments-container-51510" class="comments-container"><span id="51514"></span><div id="comment-51514" class="comment"><div id="post-51514-score" class="comment-score"></div><div class="comment-text"><p>Perhaps this has to do with the scale. What happens when you try using <code>AVG</code> but deselect "All packets" so that <strong>only</strong> the ICMP response times are graphed? If you really want "All packets" displayed as well, then you could try using a <code>Log scale</code> to see if that helps.</p></div><div id="comment-51514-info" class="comment-info"><span class="comment-age">(08 Apr '16, 07:36)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-51510" class="comment-tools"></div><div class="clear"></div><div id="comment-51510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

