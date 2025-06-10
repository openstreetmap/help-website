+++
type = "question"
title = "Using OSM to plot survey data - is this possible?"
description = '''I have a beekeeping survey from Nigeria and wish to plot some of it on a map. Is OSM amenable to add locations where different types of beehive are used? Thanks.'''
date = "2021-04-23T11:48:00Z"
lastmod = "2021-04-23T14:31:00Z"
weight = 79819
keywords = [ "survey" ]
aliases = [ "/questions/79819" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using OSM to plot survey data - is this possible?](/questions/79819/using-osm-to-plot-survey-data-is-this-possible)

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
<span id="post-79819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a beekeeping survey from Nigeria and wish to plot some of it on a map. Is OSM amenable to add locations where different types of beehive are used? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-survey" rel="tag" title="see questions tagged &#39;survey&#39;">survey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '21, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/89333c727df8cd6bc1922a912fd01a66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Barmingmag&#39;s gravatar image" />
<p><span>Barmingmag</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Barmingmag has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79819" class="comments-container">
&#10;</div>
<div id="comment-tools-79819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79819-form-container" class="comment-form-container">
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

<span id="79820"></span>

<div id="answer-container-79820" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79820-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible to record beehives in OpenStreetMap (almost 50,000 beehives are in OSM right now). However, you would not simply be able to upload them, you would be expected to ensure they match existing OSM data - e.g. that you don't upload a beehive where one already is, or you don't upload a beehive in the middle of a river or a building and so on. Additionally, bee hives are not currently shown on the standard map style used on www.opensteetmap.org i.e. even if you record your beehives in OSM, you would have to write a custom map style.</p>
<p>A more promising approach might be creating a map of your survey locations with umap.openstreetmap.fr which uses OSM as a base map but allows you to draw data on top (that would then not be uploaded to OSM proper).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '21, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79820" class="comments-container">
<span id="79821"></span>
<div id="comment-79821" class="comment">
<div id="post-79821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. I've taken a look at umap and it looks like it provides what I need. I'm hoping that it can use custom icons and possibly (though not of necessity) associate photos.</p>
</div>
<div id="comment-79821-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 12:16)</span> <span class="comment-user userinfo">Barmingmag</span>
</div>
</div>
<span id="79824"></span>
<div id="comment-79824" class="comment">
<div id="post-79824-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When you use uMap make sure to log in first before creating a new map. Otherwise you run a riks not being able to edit the map later.</p>
<p>You can definitely associate images and link to them. I'm not sure if you can display them in the map.</p>
</div>
<div id="comment-79824-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 13:33)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79826"></span>
<div id="comment-79826" class="comment">
<div id="post-79826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good tip. Thanks. Looks like I can load custom icons using urls eg via Wikimedia Commons.</p>
</div>
<div id="comment-79826-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 14:31)</span> <span class="comment-user userinfo">Barmingmag</span>
</div>
</div>
</div>
<div id="comment-tools-79820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79820-form-container" class="comment-form-container">
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

