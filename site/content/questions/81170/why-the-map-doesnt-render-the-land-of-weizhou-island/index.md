+++
type = "question"
title = "Why the map doesn&#x27;t render the land of Weizhou island?"
description = ''''''
date = "2021-08-02T12:55:00Z"
lastmod = "2021-08-03T04:43:00Z"
weight = 81170
keywords = [ "render" ]
aliases = [ "/questions/81170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why the map doesn't render the land of Weizhou island?](/questions/81170/why-the-map-doesnt-render-the-land-of-weizhou-island)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81170-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="https://osm.bio/images/4/49/%E6%B6%A0%E6%B4%B2%E5%B2%9BOSM.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '21, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/cac2465c1d2a0fd0e194ff2053013de0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E5%AE%AB%E6%9C%AC%E5%AE%87%E6%A3%AE&#39;s gravatar image" />
<p><span>宫本宇森</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="宫本宇森 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-81170" class="comments-container">
&#10;</div>
<div id="comment-tools-81170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81170-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="81172"></span>

<div id="answer-container-81172" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81172-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="宫本宇森 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There could be several reasons for this.</p>
<p>If this is in a lake, then it needs to be set as the inner boundary of the lake multipolygon. If if is not a multipolygon yet then it will need to be turned into one.</p>
<p>If this is in the ocean then it <a href="https://wiki.openstreetmap.org/wiki/Coastline">needs</a> and unbroken sequence of ways with <code>natural=coastline</code> around the perimeter so that it has the land on the left side of the ways and ocean on the right. An error in this can break rendering. If the island is newly mapped then it may take a while for it to appear as coastline rendering is special and has a bit of a delay.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '21, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-81172" class="comments-container">
<span id="81175"></span>
<div id="comment-81175" class="comment">
<div id="post-81175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK! Work out successfully! Thanks</p>
</div>
<div id="comment-81175-info" class="comment-info">
<span class="comment-age">(03 Aug '21, 04:43)</span> <span class="comment-user userinfo">宫本宇森</span>
</div>
</div>
</div>
<div id="comment-tools-81172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81172-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

