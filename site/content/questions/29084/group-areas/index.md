+++
type = "question"
title = "Group Areas"
description = '''Is there a way to group several different closed ways so that they display as one closed way on the OSM layers and in Nominatim? Example- Neighborhoods sometimes have parts of them that don&#x27;t really link to each other but are still part of one large neighborhood.'''
date = "2013-12-15T04:48:00Z"
lastmod = "2014-01-18T18:38:00Z"
weight = 29084
keywords = [ "relations" ]
aliases = [ "/questions/29084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Group Areas](/questions/29084/group-areas)

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
<span id="post-29084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29084-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to group several different closed ways so that they display as one closed way on the OSM layers and in Nominatim? Example- Neighborhoods sometimes have parts of them that don't really link to each other but are still part of one large neighborhood.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '13, 04:48</strong></p>
<img src="https://secure.gravatar.com/avatar/64737535e14942bd57d0b3aa318d06ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ItalianMustache&#39;s gravatar image" />
<p><span>ItalianMustache</span><br />
<span class="score" title="201 reputation points">201</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ItalianMustache has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29084" class="comments-container">
&#10;</div>
<div id="comment-tools-29084" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29084-form-container" class="comment-form-container">
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

<span id="29088"></span>

<div id="answer-container-29088" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>OSM is very clear you shouldn't add data or tags just so something displays on a certain renderer. I think that concept would apply to Nominatim too: add and tag the things that exist.</li>
<li>That said, a multipolygon relation should do the trick, ie <a href="http://nominatim.openstreetmap.org/details.php?place_id=9151190154">http://nominatim.openstreetmap.org/details.php?place_id=9151190154</a> :)</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '13, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-29088" class="comments-container">
<span id="29944"></span>
<div id="comment-29944" class="comment">
<div id="post-29944-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This doesn't seem to do the trick for rendering in all layers after searching with Nominatim. In some cases, I am trying to map neighborhoods as residential areas that span across islands that don't touch. Is what I did in <a href="http://nominatim.openstreetmap.org/details.php?place_id=9151190154">http://nominatim.openstreetmap.org/details.php?place_id=9151190154</a> going to do the trick for this?</p>
</div>
<div id="comment-29944-info" class="comment-info">
<span class="comment-age">(18 Jan '14, 18:38)</span> <span class="comment-user userinfo">ItalianMustache</span>
</div>
</div>
</div>
<div id="comment-tools-29088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29088-form-container" class="comment-form-container">
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

