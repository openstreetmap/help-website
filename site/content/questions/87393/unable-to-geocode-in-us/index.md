+++
type = "question"
title = "Unable to geocode in US"
description = '''This query doesn&#x27;t work https://nominatim.openstreetmap.org/reverse?lat=33.485333&amp;amp;lon=-77.590667 It seems this place is Frying Pan Shoals Light Tower which is a decommissioned lighthouse located approximately 39 miles (63 km) southeast of Southport, North Carolina and 32 miles (51 km) from Bald ...'''
date = "2023-06-26T08:23:00Z"
lastmod = "2023-06-26T10:56:00Z"
weight = 87393
keywords = [ "nominatim" ]
aliases = [ "/questions/87393" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to geocode in US](/questions/87393/unable-to-geocode-in-us)

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
<span id="post-87393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This query doesn't work</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?lat=33.485333&amp;lon=-77.590667">https://nominatim.openstreetmap.org/reverse?lat=33.485333&amp;lon=-77.590667</a></p>
<p>It seems this place is Frying Pan Shoals Light Tower which is a decommissioned lighthouse located approximately 39 miles (63 km) southeast of Southport, North Carolina and 32 miles (51 km) from Bald Head Island, North Carolina.</p>
<p>Still it should belong to US but Nominatim can't resolve this place</p>
<p>Is it a bug or a well known behavior in such case?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '23, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e5d478cc65b107551951de470d3b8d52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Toucouleur&#39;s gravatar image" />
<p><span>Toucouleur</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Toucouleur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87393" class="comments-container">
&#10;</div>
<div id="comment-tools-87393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87393-form-container" class="comment-form-container">
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

<span id="87396"></span>

<div id="answer-container-87396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87396-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-87396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The lighthouse is in a different position in OSM. If you use OSM's position, reverse geocoding will work: <a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=33.4831&amp;lon=-77.5834&amp;zoom=18">https://nominatim.openstreetmap.org/ui/reverse.html?lat=33.4831&amp;lon=-77.5834&amp;zoom=18</a> It will not show it as being in the US though, because OSM has the lighthouse outside the US boundaries in international waters.</p>
<p>There is the open question if Nominatim should return the appropriate ocean in international waters (see <a href="https://github.com/osm-search/Nominatim/issues/510">this open issue</a>) but a solution to that problem has never materialized.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '23, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-87396" class="comments-container">
&#10;</div>
<div id="comment-tools-87396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87396-form-container" class="comment-form-container">
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

