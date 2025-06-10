+++
type = "question"
title = "Nominatim returning wrong city names for Puerto Rico"
description = '''I found a problem in a website using OSM for Puerto Rico. The websites uses the Nominatim reverse geolocation API and the API is returning the wrong CITY.  Puerto Rico is a Territory of the United States and the administrative boundaries seem ok to me. I checked the map against the documentation in ...'''
date = "2018-02-15T00:00:00Z"
lastmod = "2018-02-15T00:37:00Z"
weight = 62102
keywords = [ "nominatim" ]
aliases = [ "/questions/62102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim returning wrong city names for Puerto Rico](/questions/62102/nominatim-returning-wrong-city-names-for-puerto-rico)

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
<span id="post-62102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62102-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found a problem in a website using OSM for Puerto Rico. The websites uses the Nominatim reverse geolocation API and the API is returning the wrong CITY.</p>
<p>Puerto Rico is a Territory of the United States and the administrative boundaries seem ok to me. I checked the map against the documentation in this page:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/United_States_admin_level">https://wiki.openstreetmap.org/wiki/United_States_admin_level</a></p>
<p>For example:</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;addressdetails=1&amp;limit=1&amp;lat=18.438423379226933&amp;lon=-67.14555680751802">https://nominatim.openstreetmap.org/reverse?format=json&amp;addressdetails=1&amp;limit=1&amp;lat=18.438423379226933&amp;lon=-67.14555680751802</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '18, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/64ff8513e0e0d52ef30f184e6c9c79c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctkjose&#39;s gravatar image" />
<p><span>ctkjose</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctkjose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62102" class="comments-container">
&#10;</div>
<div id="comment-tools-62102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62102-form-container" class="comment-form-container">
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

<span id="62103"></span>

<div id="answer-container-62103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62103-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(is there a question?)</p>
<p>Nominatim treats every <code>admin_level=8</code> as city, <code>admin_level=6</code> as county when it returns results. If that needs to change because of <a href="https://wiki.openstreetmap.org/wiki/United_States_admin_level">https://wiki.openstreetmap.org/wiki/United_States_admin_level</a> then please add a feature request to <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '18, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '18, 00:38</strong> </span></p>
</div>
</div>
<div id="comments-container-62103" class="comments-container">
&#10;</div>
<div id="comment-tools-62103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62103-form-container" class="comment-form-container">
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

