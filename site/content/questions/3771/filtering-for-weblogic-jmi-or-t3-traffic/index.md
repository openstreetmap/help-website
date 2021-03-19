+++
type = "question"
title = "Filtering for Weblogic JMI or t3 traffic"
description = '''I&#x27;d like to know if there is an easy way to filter for Oracle Weblogic t3 traffic, which sits atop the Java RMI protocol. I am losing heartbeat messages and experiencing various application timeouts. I have captured the traffic between the offending systems and would like to be able to determine if,...'''
date = "2011-04-27T18:12:00Z"
lastmod = "2015-11-12T03:30:00Z"
weight = 3771
keywords = [ "oracle", "filter", "jmi", "weblogic", "t3" ]
aliases = [ "/questions/3771" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering for Weblogic JMI or t3 traffic](/questions/3771/filtering-for-weblogic-jmi-or-t3-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3771-score" class="post-score" title="current number of votes">0</div><span id="post-3771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to know if there is an easy way to filter for Oracle Weblogic t3 traffic, which sits atop the Java RMI protocol.</p><p>I am losing heartbeat messages and experiencing various application timeouts. I have captured the traffic between the offending systems and would like to be able to determine if, for example, plackets are being sent but not received by the admin server.</p><ul><li>CDM</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-oracle" rel="tag" title="see questions tagged &#39;oracle&#39;">oracle</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-jmi" rel="tag" title="see questions tagged &#39;jmi&#39;">jmi</span> <span class="post-tag tag-link-weblogic" rel="tag" title="see questions tagged &#39;weblogic&#39;">weblogic</span> <span class="post-tag tag-link-t3" rel="tag" title="see questions tagged &#39;t3&#39;">t3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '11, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/5b29981fa2ec94c398241ddc28deb04e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cdmonline&#39;s gravatar image" /><p><span>cdmonline</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cdmonline has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '11, 09:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3771" class="comments-container"></div><div id="comment-tools-3771" class="comment-tools"></div><div class="clear"></div><div id="comment-3771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47540"></span>

<div id="answer-container-47540" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47540-score" class="post-score" title="current number of votes">0</div><span id="post-47540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>t3 is at the application layer and sits on top of tcp. Therefore you can filter t3 traffic just as you normally do with other tcp packets. for instance interface lo (127.0.0.1) and filter "tcp.stream eq 7001" (7001 is the default port for weblogic)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/ca39f357ddb489030c3d511788af831f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iammyr&#39;s gravatar image" /><p><span>iammyr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iammyr has no accepted answers">0%</span></p></div></div><div id="comments-container-47540" class="comments-container"></div><div id="comment-tools-47540" class="comment-tools"></div><div class="clear"></div><div id="comment-47540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

