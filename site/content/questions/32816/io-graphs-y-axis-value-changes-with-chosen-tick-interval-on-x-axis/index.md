+++
type = "question"
title = "IO Graphs: Y-axis value changes with chosen Tick interval on X-Axis"
description = '''Does anybody know (not just &quot;suspect or think&quot;) why the IO Graph for a given source-destination IP changes it&#x27;s value on the X-axis when chosing different Tick intervals on the X-Axis? I need to measure the max bandwidth taken by a new application that we want to roll-out on our corporate laptops, b...'''
date = "2014-05-15T03:40:00Z"
lastmod = "2014-05-15T06:01:00Z"
weight = 32816
keywords = [ "iographs" ]
aliases = [ "/questions/32816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IO Graphs: Y-axis value changes with chosen Tick interval on X-Axis](/questions/32816/io-graphs-y-axis-value-changes-with-chosen-tick-interval-on-x-axis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32816-score" class="post-score" title="current number of votes">0</div><span id="post-32816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anybody know (not just "suspect or think") why the IO Graph for a given source-destination IP changes it's value on the X-axis when chosing different Tick intervals on the X-Axis?</p><p>I need to measure the max bandwidth taken by a new application that we want to roll-out on our corporate laptops, before we deploy it, as to analyse the impact on the WAN. The application is called DLO from symantec and makes automated backups to a NAS, using incremental backups (also for Outlook PST files). It uses SMB2 protocol.</p><p>So, if I open the IO Graphs, I use a source-destination filter to see the traffic between client and the server, but I find different peak-values when changing the Tick-Interval for the X-Axis. How come? I don't see anything explained in the 2nd edition of Laura Chappell's "Wireshark Network analysis" book. the peak-values on the X-axis increase when decreasing the tick-interval, I would have expected the opposite; i.e. by decreasing the Tick-interval the "sampling" frequence decreases, hence statistically missing more short peaks.</p><p>I've seen comments about the IO Graphs doing averages between two tick-intervals, but is that confirmed officially? Thx!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iographs" rel="tag" title="see questions tagged &#39;iographs&#39;">iographs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p><span>profke</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></div></div><div id="comments-container-32816" class="comments-container"></div><div id="comment-tools-32816" class="comment-tools"></div><div class="clear"></div><div id="comment-32816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32822"></span>

<div id="answer-container-32822" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32822-score" class="post-score" title="current number of votes">0</div><span id="post-32822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I think I found the answer myself; because the amount of traffic is measured over the time-interval (Tick interval), i.e. if time between ticks is shorter, the amount of traffic is less of course, because bandwidth=amount of traffic per time unit (per second actually). If the Tick interval is e.g. 10 x shorter, the amount of traffic will be 10x less, so the "peaks" will be 10x smaller. Laura's book litteraly says (Chapter 21, p500): "... The tick interval indicates how often traffic should be plotted on the graph. If the interval is set to 1 second (the default), data will be examined for one full second and then plotted. ..." Sorry Laura, it just didn't get into my brains at first. Hope you excuse me for quoting a phraze in your book!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p><span>profke</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></div></div><div id="comments-container-32822" class="comments-container"></div><div id="comment-tools-32822" class="comment-tools"></div><div class="clear"></div><div id="comment-32822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

