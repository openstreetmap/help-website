+++
type = "question"
title = "API / Overpass API"
description = '''Using the api or the Overpass API :  For a given node : How could I retrieve the city where the node is ? '''
date = "2014-06-08T14:55:00Z"
lastmod = "2014-06-08T16:06:00Z"
weight = 33803
keywords = [ "overpass", "nodes" ]
aliases = [ "/questions/33803" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [API / Overpass API](/questions/33803/api-overpass-api)

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
<span id="post-33803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33803-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using the api or the Overpass API :</p>
<p>For a given node : How could I retrieve the city where the node is ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '14, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33803" class="comments-container">
<span id="33805"></span>
<div id="comment-33805" class="comment">
<div id="post-33805-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Why not just use Nominatim?</p>
</div>
<div id="comment-33805-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 15:49)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="33806"></span>
<div id="comment-33806" class="comment">
<div id="post-33806-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Because i'm a noob and don't really know all the tools around OSM :)</p>
</div>
<div id="comment-33806-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 16:02)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
</div>
<div id="comment-tools-33803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33803-form-container" class="comment-form-container">
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

<span id="33807"></span>

<div id="answer-container-33807" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33807-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the answer myself using Nominatim thanks to <span>@Tyr_asd</span> :</p>
<pre><code>http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_type=N&amp;osm_id=136221</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '14, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33807" class="comments-container">
&#10;</div>
<div id="comment-tools-33807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33807-form-container" class="comment-form-container">
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

