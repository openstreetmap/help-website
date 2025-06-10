+++
type = "question"
title = "Trail-Stream Crossing - Best Practice"
description = '''We have a number of hiking trails that cross small streams without the aid of any bridges (people just cross the stream by stepping from stone to stone). If I create a line feature that crosses an existing stream feature in OpenStreetMap iD I get a warning message. Should I ignore this warning or sh...'''
date = "2021-04-24T23:52:00Z"
lastmod = "2021-04-25T02:26:00Z"
weight = 79854
keywords = [ "trail", "stream" ]
aliases = [ "/questions/79854" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trail-Stream Crossing - Best Practice](/questions/79854/trail-stream-crossing-best-practice)

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
<span id="post-79854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a number of hiking trails that cross small streams without the aid of any bridges (people just cross the stream by stepping from stone to stone). If I create a line feature that crosses an existing stream feature in OpenStreetMap iD I get a warning message. Should I ignore this warning or should I insert a bridge feature, even though there is no actual bridge present?</p>
<p>Thanks! --Rob</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '21, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/63e6efaf5ae5774b948eb0e6bf40c84f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob009&#39;s gravatar image" />
<p><span>Rob009</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob009 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '21, 02:08</strong> </span></p>
</div>
</div>
<div id="comments-container-79854" class="comments-container">
&#10;</div>
<div id="comment-tools-79854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79854-form-container" class="comment-form-container">
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

<span id="79855"></span>

<div id="answer-container-79855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79855-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-79855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I join the crossing ways (stream and trail) and on the node I put <a href="https://wiki.openstreetmap.org/wiki/Tag:ford%3Dyes">"ford=yes"</a>. If it is a seasonal or intermittent waterway then I also tag the node (and waterway) with <a href="https://wiki.openstreetmap.org/wiki/Key:intermittent">"intermittent=yes"</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '21, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-79855" class="comments-container">
<span id="79856"></span>
<div id="comment-79856" class="comment">
<div id="post-79856-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/Tag:ford%3Dstepping_stones"><code>ford=stepping_stones</code></a> subtag too.</p>
</div>
<div id="comment-79856-info" class="comment-info">
<span class="comment-age">(25 Apr '21, 02:26)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-79855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79855-form-container" class="comment-form-container">
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

