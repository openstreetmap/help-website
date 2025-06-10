+++
type = "question"
title = "Why are editable maps different from the viewable maps?"
description = '''Hello, I want to use maps for an Indian city. When I view the maps there is not much detail on it but when I attempt to edit the map, there are more details available which were not visible when I was viewing the map. Why is this the case? Please advice. Thanks Siddharth'''
date = "2011-09-06T09:14:00Z"
lastmod = "2011-09-06T11:06:00Z"
weight = 7657
keywords = [ "map", "details" ]
aliases = [ "/questions/7657" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why are editable maps different from the viewable maps?](/questions/7657/why-are-editable-maps-different-from-the-viewable-maps)

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
<span id="post-7657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7657-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to use maps for an Indian city. When I view the maps there is not much detail on it but when I attempt to edit the map, there are more details available which were not visible when I was viewing the map. Why is this the case? Please advice.</p>
<p>Thanks Siddharth</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-details" rel="tag" title="see questions tagged &#39;details&#39;">details</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '11, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/239813d5b2c171b5875e084b72ccbccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sid%20I4GY&#39;s gravatar image" />
<p><span>Sid I4GY</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sid I4GY has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7657" class="comments-container">
<span id="7660"></span>
<div id="comment-7660" class="comment">
<div id="post-7660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A link to the city in question might be useful (using the permalink button at the bottom-right of the map) - that we can have a look at it.</p>
</div>
<div id="comment-7660-info" class="comment-info">
<span class="comment-age">(06 Sep '11, 11:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7657-form-container" class="comment-form-container">
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

<span id="7658"></span>

<div id="answer-container-7658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7658-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-7658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is not a map in the first place; it is a database. An editor will usually show you all objects present in the database, whereas a map will usually only show a selection of features. This selection may be made for reasons of cartography, or rendering speed, or interest - a map for cyclists will certainly show other features than one for motorists.</p>
<p>The map style used on the main "mapnik" layer on <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> is the same for every place in the world, so if the Indian city you are looking at has a relatively low feature density in OSM you might be tempted to think: "Why aren't restaurants shown sooner, there's enough room on zoom level 12 but they only show up when I toom in to zoom level 17!" - but think of what that would do to a densely mapped place like central London.</p>
<p>You are free to create your own rendering though, based on the same OpenStreetMap database, that shows any (or all) features. Some pointers are given in the answer to <a href="http://help.openstreetmap.org/questions/136/how-do-i-render-my-own-maps-for-my-website">"How do I render my own maps for my Website?"</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '11, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7658" class="comments-container">
&#10;</div>
<div id="comment-tools-7658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7658-form-container" class="comment-form-container">
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

