+++
type = "question"
title = "Get city nodes within a country using Overpass API"
description = '''Is it possible to get all city nodes within a country using the overpass api? Preferably using relations rather than a bounding box. If I have to do this using a bounding box, is it possible to get a country bounding box through the overpass api too? https://help.openstreetmap.org/questions/13872/ho...'''
date = "2013-01-14T04:32:00Z"
lastmod = "2013-01-14T04:55:00Z"
weight = 19063
keywords = [ "overpass" ]
aliases = [ "/questions/19063" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get city nodes within a country using Overpass API](/questions/19063/get-city-nodes-within-a-country-using-overpass-api)

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
<span id="post-19063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19063-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to get all city nodes within a country using the overpass api? Preferably using relations rather than a bounding box.</p>
<p>If I have to do this using a bounding box, is it possible to get a country bounding box through the overpass api too?</p>
<p><a href="/questions/13872/how-to-find-list-of-cities-in-a-state-with-overpass-osm-api">https://help.openstreetmap.org/questions/13872/how-to-find-list-of-cities-in-a-state-with-overpass-osm-api</a> shows how to do this within a bounding box. I would rather do this using relations to get a more accurate list of cities (especially since overpass doesn't appear to return a bounding box for the country node to start with)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '13, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/dc70b9b3858aa8dd032f0699d926e8e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjmackay&#39;s gravatar image" />
<p><span>rjmackay</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjmackay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19063" class="comments-container">
&#10;</div>
<div id="comment-tools-19063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19063-form-container" class="comment-form-container">
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

<span id="19064"></span>

<div id="answer-container-19064" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19064-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-19064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rjmackay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following overpass query returns the list of all cities in Belgium:</p>
<p>area[name="België - Belgique - Belgien"];(node[place="city"](area););out;</p>
<p>You can replace the name with any country (or other administrative level) you want. Areas are explained here: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">https://wiki.openstreetmap.org/wiki/Overpass_API/Areas</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '13, 04:47</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '13, 04:49</strong> </span></p>
</div>
</div>
<div id="comments-container-19064" class="comments-container">
<span id="19065"></span>
<div id="comment-19065" class="comment">
<div id="post-19065-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Brilliant, thanks! Areas are what I need and what I'd missed in the docs.</p>
</div>
<div id="comment-19065-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 04:55)</span> <span class="comment-user userinfo">rjmackay</span>
</div>
</div>
</div>
<div id="comment-tools-19064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19064-form-container" class="comment-form-container">
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

