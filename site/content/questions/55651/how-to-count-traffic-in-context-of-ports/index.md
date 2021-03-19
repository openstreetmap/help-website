+++
type = "question"
title = "How to count traffic in context of ports?"
description = '''In statisctics I can see amount of packets, grouped by ports, but I need to get amount of traffic through these ports. For example: port size 53 - 40 KB 21 - 100 MB 80 - 50 MB  and so on. How I can achieve stats like this?'''
date = "2016-09-19T05:52:00Z"
lastmod = "2016-09-19T06:54:00Z"
weight = 55651
keywords = [ "statistics" ]
aliases = [ "/questions/55651" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to count traffic in context of ports?](/questions/55651/how-to-count-traffic-in-context-of-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55651-score" class="post-score" title="current number of votes">0</div><span id="post-55651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In statisctics I can see amount of packets, grouped by ports, but I need to get amount of traffic through these ports.</p><p>For example:</p><pre><code>port   size
53 - 40 KB
21 - 100 MB
80 - 50 MB</code></pre><p>and so on. How I can achieve stats like this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '16, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/8cf64a31b7c1eee5491de3c5e5339182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ostolop&#39;s gravatar image" /><p><span>Ostolop</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ostolop has no accepted answers">0%</span></p></div></div><div id="comments-container-55651" class="comments-container"><span id="55654"></span><div id="comment-55654" class="comment"><div id="post-55654-score" class="comment-score"></div><div class="comment-text"><p>Use 'Endpoints' feature, TCP tab, then copy and import into Excel. Perhaps a pivot table could then roll it up for you as a total? The Endpoints table has Bytes and Packets available for summary.</p></div><div id="comment-55654-info" class="comment-info"><span class="comment-age">(19 Sep '16, 06:52)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="55655"></span><div id="comment-55655" class="comment"><div id="post-55655-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-55655-info" class="comment-info"><span class="comment-age">(19 Sep '16, 06:54)</span> <span class="comment-user userinfo">Ostolop</span></div></div></div><div id="comment-tools-55651" class="comment-tools"></div><div class="clear"></div><div id="comment-55651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

