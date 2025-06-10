+++
type = "question"
title = "How can I get/extract the names of cities with their latitude and longitude details and their boundaries?"
description = '''How can I get/extract the names of cities in Nigeria with their latitude, longitude and boundaries (Max Lat, Max long, min lat and min long). Any help (in the simplest words) will be highly appreciated.'''
date = "2015-10-23T22:17:00Z"
lastmod = "2015-10-28T12:25:00Z"
weight = 46087
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/46087" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get/extract the names of cities with their latitude and longitude details and their boundaries?](/questions/46087/how-can-i-getextract-the-names-of-cities-with-their-latitude-and-longitude-details-and-their-boundaries)

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
<span id="post-46087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I get/extract the names of cities in Nigeria with their latitude, longitude and boundaries (Max Lat, Max long, min lat and min long). Any help (in the simplest words) will be highly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '15, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/b7089f235fcbcdccd86e11665f1aef73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sprime&#39;s gravatar image" />
<p><span>Sprime</span><br />
<span class="score" title="37 reputation points">37</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sprime has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46087" class="comments-container">
&#10;</div>
<div id="comment-tools-46087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46087-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="46088"></span>

<div id="answer-container-46088" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I must say that Nigeria will be a tough region. I'm afraid the boundaries you want probably won't be complete in Nigeria.</p>
<p>Secondly, it would depend on which boundaries you want. I see that most rough residential areas are available, but I see no administrative boundaries.</p>
<p>In any case, you can start with the city names, their lat and lon. It's rather simple with overpass, just execute this query: <a href="http://overpass-turbo.eu/s/ceG">http://overpass-turbo.eu/s/ceG</a></p>
<p>Getting the bounding box will quite be a bit harder. You could use Overpass to extract all residential landuses from OSM, and bind them to the city names using some GIS software (like qGIS). But Overpass doesn't seem to treat landuse areas as areas, so you can't perform is_in queries on it, which makes it a whole lot harder.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '15, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-46088" class="comments-container">
<span id="46173"></span>
<div id="comment-46173" class="comment">
<div id="post-46173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much</p>
</div>
<div id="comment-46173-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 12:25)</span> <span class="comment-user userinfo">Sprime</span>
</div>
</div>
</div>
<div id="comment-tools-46088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46088-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46135"></span>

<div id="answer-container-46135" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46135-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can go to the <a href="https://osm.wno-edv-service.de/boundaries/">webservice</a> from user Wambacher and download some boundary data in different format, like raw OSM XML, shapefile or geoJSON.</p>
<p>Choose "Nigeria" from the tree menu on the left screen side, and open its subtree structure to select smaller regions with higher admin_level.</p>
<p>You have to be logged in to that webservice with your OSM account credentials via OAuth to download data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '15, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-46135" class="comments-container">
<span id="46174"></span>
<div id="comment-46174" class="comment">
<div id="post-46174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much</p>
</div>
<div id="comment-46174-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 12:25)</span> <span class="comment-user userinfo">Sprime</span>
</div>
</div>
</div>
<div id="comment-tools-46135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46135-form-container" class="comment-form-container">
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

