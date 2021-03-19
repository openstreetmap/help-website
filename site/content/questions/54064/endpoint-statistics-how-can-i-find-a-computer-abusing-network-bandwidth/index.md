+++
type = "question"
title = "Endpoint Statistics-how can i find a computer abusing network bandwidth"
description = '''Statistics-&amp;gt;Endpoints using this tool how can i tell if a computer is abusing network If not this way which tool can i use on wireshark to find a computer that is slowing up the network. I am trying to resolve issues on different networks and want to find out which computers maybe causing the iss...'''
date = "2016-07-14T07:45:00Z"
lastmod = "2016-07-15T12:53:00Z"
weight = 54064
keywords = [ "traffic-analysis", "network" ]
aliases = [ "/questions/54064" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Endpoint Statistics-how can i find a computer abusing network bandwidth](/questions/54064/endpoint-statistics-how-can-i-find-a-computer-abusing-network-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54064-score" class="post-score" title="current number of votes">0</div><span id="post-54064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Statistics-&gt;Endpoints</p><p>using this tool how can i tell if a computer is abusing network</p><p>If not this way which tool can i use on wireshark to find a computer that is slowing up the network. I am trying to resolve issues on different networks and want to find out which computers maybe causing the issues or find out why the network is slow</p><p>thanks</p><p><span class="__cf_email__" data-cfemail="96dcf7fbf3e5a4a6a6a6fdd6fef9e2fbf7fffab8f5f9fb">[email protected]</span> ( email me if you want to contact me directly thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic-analysis" rel="tag" title="see questions tagged &#39;traffic-analysis&#39;">traffic-analysis</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '16, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/518648addfc15c3294ea3944b44547cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James2000k&#39;s gravatar image" /><p><span>James2000k</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James2000k has no accepted answers">0%</span></p></div></div><div id="comments-container-54064" class="comments-container"></div><div id="comment-tools-54064" class="comment-tools"></div><div class="clear"></div><div id="comment-54064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54083"></span>

<div id="answer-container-54083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54083-score" class="post-score" title="current number of votes">0</div><span id="post-54083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are likely better tools for this, like simple network managers working with SNMP stats from edge-switch ports or a tool like ntopng. Wireshark, though would give you similar results with a lot of effort, is likely too precise a tool for this. I think you might want some aggregating of data to start before you deploy Wireshark. Maybe the end clients have some builtin tools to help as well.</p><p>Some links:</p><ol><li><a href="http://sourceforge.net/projects/bandwidthd/">bandwidthd</a></li><li><a href="http://www.ntop.org/products/traffic-analysis/ntop/">ntopng</a></li><li><a href="https://www.paessler.com/network_utilization_monitoring">https://www.paessler.com/network_utilization_monitoring</a></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-54083" class="comments-container"></div><div id="comment-tools-54083" class="comment-tools"></div><div class="clear"></div><div id="comment-54083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

