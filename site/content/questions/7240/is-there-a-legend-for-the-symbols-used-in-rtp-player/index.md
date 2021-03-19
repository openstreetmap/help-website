+++
type = "question"
title = "Is there a legend for the symbols used in RTP player?"
description = '''In version 1.6, the release notes say &quot;The RTP player now shows why media interruptions occur.&quot; I&#x27;m now using 1.6.3, and I see the symbols where there are problems with the RTP stream but haven&#x27;t been able to find a legend for what the symbols mean. Thanks.'''
date = "2011-11-04T09:56:00Z"
lastmod = "2011-12-08T23:18:00Z"
weight = 7240
keywords = [ "player", "rtp" ]
aliases = [ "/questions/7240" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a legend for the symbols used in RTP player?](/questions/7240/is-there-a-legend-for-the-symbols-used-in-rtp-player)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7240-score" class="post-score" title="current number of votes">1</div><span id="post-7240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In version 1.6, the release notes say "The RTP player now shows why media interruptions occur." I'm now using 1.6.3, and I see the symbols where there are problems with the RTP stream but haven't been able to find a legend for what the symbols mean. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-player" rel="tag" title="see questions tagged &#39;player&#39;">player</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '11, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/444790a4f9fe50aba85f4e356f466f10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rdyaz&#39;s gravatar image" /><p><span>rdyaz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rdyaz has no accepted answers">0%</span></p></div></div><div id="comments-container-7240" class="comments-container"></div><div id="comment-tools-7240" class="comment-tools"></div><div class="clear"></div><div id="comment-7240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7241"></span>

<div id="answer-container-7241" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7241-score" class="post-score" title="current number of votes">4</div><span id="post-7241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Reasons for silence:</p><ul><li>D: Dropped by jitter</li><li>W: Wrong timestamp</li><li>S: Silence inserted</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '11, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7241" class="comments-container"><span id="7858"></span><div id="comment-7858" class="comment"><div id="post-7858-score" class="comment-score"></div><div class="comment-text"><p>what is "S silence inserted" exactly? would it be related to CN payload?</p></div><div id="comment-7858-info" class="comment-info"><span class="comment-age">(08 Dec '11, 15:51)</span> <span class="comment-user userinfo">piuslor</span></div></div><span id="7862"></span><div id="comment-7862" class="comment"><div id="post-7862-score" class="comment-score"></div><div class="comment-text"><p>Silence inserted follows from strange behavior of the timestamp (large jump for instance), then (a limited amount of) silence is inserted in order to allow you to listen to the rest of the speech. It messes up multi stream sync, but at least allows you to listen.</p></div><div id="comment-7862-info" class="comment-info"><span class="comment-age">(08 Dec '11, 23:18)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-7241" class="comment-tools"></div><div class="clear"></div><div id="comment-7241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

