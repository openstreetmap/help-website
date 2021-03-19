+++
type = "question"
title = "Identifying traffic bursts"
description = '''Hello! I have an issue in our LAN (ca. 50 clients). I encounter high traffic bursts (traffic peaks at a very short timeframe). The problem is, that because of that we have quality issues with our VoIP lines as the router cannot handle the QoS queues during these bursts. The bursts come irregularly e...'''
date = "2013-01-04T02:44:00Z"
lastmod = "2013-01-04T02:52:00Z"
weight = 17431
keywords = [ "qos", "bursts", "traffic", "peak", "voip" ]
aliases = [ "/questions/17431" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying traffic bursts](/questions/17431/identifying-traffic-bursts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17431-score" class="post-score" title="current number of votes">0</div><span id="post-17431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I have an issue in our LAN (ca. 50 clients).</p><p>I encounter high traffic bursts (traffic peaks at a very short timeframe). The problem is, that because of that we have quality issues with our VoIP lines as the router cannot handle the QoS queues during these bursts.</p><p>The bursts come irregularly every 10 seconds. I can use a monitoring port to monitor the total traffic in the LAN with Wireshark.</p><p>I would like to find out where these bursts come from. How can I set the filters in order to see these bursts?</p><p>The bursts apply to the QoS filter, which detects every transfer to the VOIP-provides-servers...</p><p>Many Thanks!</p><p>Henry</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-bursts" rel="tag" title="see questions tagged &#39;bursts&#39;">bursts</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-peak" rel="tag" title="see questions tagged &#39;peak&#39;">peak</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/e30fa72e2bb413e1fab235199633333e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henry%20B&#39;s gravatar image" /><p><span>Henry B</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henry B has no accepted answers">0%</span></p></div></div><div id="comments-container-17431" class="comments-container"></div><div id="comment-tools-17431" class="comment-tools"></div><div class="clear"></div><div id="comment-17431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17432"></span>

<div id="answer-container-17432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17432-score" class="post-score" title="current number of votes">2</div><span id="post-17432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could start by using the I/O Graph in the statistics menu to see if there are spikes in the traffic. You might have to reduce the tick time to values below 1 second to be able to see very short bursts, and play around with the packets/tick and bits/tick settings as well. When you find a peak that is suspicious you can click on the graph and Wireshark will jump into that area in the packet list. In there you'll have to determine who is doing the most traffic, for example by using the conversation and endpoint statistics menu. I would probably set a filter on start and end time of the burst and then open these statistics. In there, you can select "limit to display filter" to force the statistics to only show you values for the time range you filtered on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17432" class="comments-container"></div><div id="comment-tools-17432" class="comment-tools"></div><div class="clear"></div><div id="comment-17432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

