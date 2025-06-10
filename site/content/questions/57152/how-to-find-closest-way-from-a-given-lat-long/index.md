+++
type = "question"
title = "How to find closest way from a given lat, long"
description = '''Nominatim api gives me road name given a lat, long value which I guess is the nearest one but it doesnot provide wayId.  Is there any way to get that information. Or does any of osm v0.6 apis provide this feature.'''
date = "2017-07-18T12:29:00Z"
lastmod = "2017-07-18T13:15:00Z"
weight = 57152
keywords = [ "nominatim", "osm", "osm2pgsql" ]
aliases = [ "/questions/57152" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find closest way from a given lat, long](/questions/57152/how-to-find-closest-way-from-a-given-lat-long)

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
<span id="post-57152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Nominatim api gives me road name given a lat, long value which I guess is the nearest one but it doesnot provide wayId. Is there any way to get that information. Or does any of osm v0.6 apis provide this feature.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '17, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ac0dd91ec334a38434646d7effb4ac10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shashank&#39;s gravatar image" />
<p><span>shashank</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shashank has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '17, 12:30</strong> </span></p>
</div>
</div>
<div id="comments-container-57152" class="comments-container">
&#10;</div>
<div id="comment-tools-57152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57152-form-container" class="comment-form-container">
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

<span id="57153"></span>

<div id="answer-container-57153" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57153-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim returns an "osm_type" and "osm_id" which point to the street, if the street is what your query found. Of course your query could also find a bus shelter or a building! You should be able to influence what types of objects are returned if you fiddle with the "zoom" parameter.</p>
<p>Just to be clear, do not use that in any kind of "production" app or website where you want to make a larger number of requests (like displaying the "road you are currently on" in a moving car or so). That would be a surefire way to have you and your app blocked from using the server. If you are envisaging that kind of use, download the Nominatim software and the OSM data and set up your own server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '17, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57153" class="comments-container">
<span id="57155"></span>
<div id="comment-57155" class="comment">
<div id="post-57155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>nominatim returns osm_type and osm_id for the point(lat,long) I am searching and not for the nearest road. So I cant use that osm id for getting road information later.</p>
<p>P.S: I have setup my local nominatim server with my osm dataset.</p>
</div>
<div id="comment-57155-info" class="comment-info">
<span class="comment-age">(18 Jul '17, 13:15)</span> <span class="comment-user userinfo">shashank</span>
</div>
</div>
</div>
<div id="comment-tools-57153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57153-form-container" class="comment-form-container">
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

