+++
type = "question"
title = "Nominatim import data granularity"
description = '''Hello, When importing OSM data into one&#x27;s own Nominatim DB, is there a way to configure the level of granularity of geographic data to support in it? I&#x27;d really benefit from cutting import times if that&#x27;s so, since I can do with a much coarser resolution in search results for my use case. I really o...'''
date = "2020-05-14T20:46:00Z"
lastmod = "2020-05-14T21:07:00Z"
weight = 74813
keywords = [ "nominatim", "import", "level", "resolution", "granularity" ]
aliases = [ "/questions/74813" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim import data granularity](/questions/74813/nominatim-import-data-granularity)

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
<span id="post-74813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When importing OSM data into one's own Nominatim DB, is there a way to configure the level of granularity of geographic data to support in it? I'd really benefit from cutting import times if that's so, since I can do with a much coarser resolution in search results for my use case. I really only need city-level responses, but I'm not even sure if that makes sense conceptually.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-level" rel="tag" title="see questions tagged &#39;level&#39;">level</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-granularity" rel="tag" title="see questions tagged &#39;granularity&#39;">granularity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '20, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ede0a84ad576e5a6dc3b1b650869aa6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shai&#39;s gravatar image" />
<p><span>Shai</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74813" class="comments-container">
&#10;</div>
<div id="comment-tools-74813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74813-form-container" class="comment-form-container">
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

<span id="74814"></span>

<div id="answer-container-74814" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74814-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#choosing-the-data-to-import">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#choosing-the-data-to-import</a> explains how to choose countries and how to filter data, e.g. not importing streets and house numbers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74814" class="comments-container">
<span id="74816"></span>
<div id="comment-74816" class="comment">
<div id="post-74816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent, thanks!</p>
</div>
<div id="comment-74816-info" class="comment-info">
<span class="comment-age">(14 May '20, 21:07)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74814-form-container" class="comment-form-container">
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

