+++
type = "question"
title = "Difference between v1.4 and v2.2 in checksum fields"
description = '''In WireShark v1.4, Within a package the branch expands and in the Header value it shows the following: Header checksum: 0x5dd [incorrect, should be 0x5e16]  [Good: False]  [Bad: True]  [Expert Info (Error/checksum): Bad checksum]  [Message: Bad checksum]  [Severity level: Error]  [Group: Checksum]  ...'''
date = "2016-12-29T15:27:00Z"
lastmod = "2016-12-30T04:00:00Z"
weight = 58426
keywords = [ "header", "cksum", "characteristics" ]
aliases = [ "/questions/58426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between v1.4 and v2.2 in checksum fields](/questions/58426/difference-between-v14-and-v22-in-checksum-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58426-score" class="post-score" title="current number of votes">0</div><span id="post-58426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In WireShark v1.4, Within a package the branch expands and in the Header value it shows the following:</p><pre><code>Header checksum: 0x5dd [incorrect, should be 0x5e16]
  [Good: False]
  [Bad: True]
     [Expert Info (Error/checksum): Bad checksum]
           [Message: Bad checksum]
           [Severity level: Error]
           [Group: Checksum]</code></pre>While in v2.2 only show me:<pre><code>Header checksum: 0x0bc8
[Header checksum status: Unverfied]</code></pre><p>Why ? Somebody knows how enable this information ? Please I need your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-cksum" rel="tag" title="see questions tagged &#39;cksum&#39;">cksum</span> <span class="post-tag tag-link-characteristics" rel="tag" title="see questions tagged &#39;characteristics&#39;">characteristics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '16, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/977e431029cdda1990151bea135f6acb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hunapuh&#39;s gravatar image" /><p><span>Hunapuh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hunapuh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Dec '16, 06:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58426" class="comments-container"></div><div id="comment-tools-58426" class="comment-tools"></div><div class="clear"></div><div id="comment-58426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58433"></span>

<div id="answer-container-58433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58433-score" class="post-score" title="current number of votes">1</div><span id="post-58433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The way checksum check information is presented has a been extended to allow for more variations. What used to be two binary flags (checksum.good and checksum.bad) is now an single value (checksum.status).</p><p>In your first example (of v1.4) checksum checking is enabled(!) and the result is that it is not good. In your second example (of v2.2) checksum checking is disabled(!) and therefore the result is 'Unverified'.</p><p>What you at least should do is enable checksum checking in the second example to get comparable situations. This checksum checking is defined by the protocol preferences of the protocol including this checksum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '16, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58433" class="comments-container"></div><div id="comment-tools-58433" class="comment-tools"></div><div class="clear"></div><div id="comment-58433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

