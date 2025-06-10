+++
type = "question"
title = "API method for obtaining the nearest settlement to the specified coordinates"
description = '''Good afternoon! Does the OSM have an API method for obtaining the nearest settlement to the specified coordinates? The method for reverse geocoding returns only the exact address of the object with the given coordinates:https://nominatim.openstreetmap.org/reverse The problem arises when the given co...'''
date = "2018-05-30T08:25:00Z"
lastmod = "2018-05-30T10:47:00Z"
weight = 63860
keywords = [ "geocoding" ]
aliases = [ "/questions/63860" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [API method for obtaining the nearest settlement to the specified coordinates](/questions/63860/api-method-for-obtaining-the-nearest-settlement-to-the-specified-coordinates)

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
<span id="post-63860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good afternoon!</p>
<p>Does the OSM have an API method for obtaining the nearest settlement to the specified coordinates?</p>
<p>The method for reverse geocoding returns only the exact address of the object with the given coordinates:<a href="https://nominatim.openstreetmap.org/reverse">https://nominatim.openstreetmap.org/reverse</a></p>
<p>The problem arises when the given coordinates do not have a specific locality, but the region is very large.</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '18, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/5269774c1e533a68b8ea2ce63efafb88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Helen%20Kir&#39;s gravatar image" />
<p><span>Helen Kir</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Helen Kir has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63860" class="comments-container">
&#10;</div>
<div id="comment-tools-63860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63860-form-container" class="comment-form-container">
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

<span id="63861"></span>

<div id="answer-container-63861" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63861-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The focus of OSM is providing data - not so much providing data access APIs. It is possible that you could do something with Overpass that gets you halfway there, but if you need to make these kinds of queries often, it would be a good idea to</p>
<ul>
<li>download the full "planet file" with all OSM data,</li>
<li>import it into a PostGIS database using e.g. <code>osm2pgsql</code> with a modified "style file" that essentially tells <code>osm2pgsql</code> you're only interested in place names or settlements (alternatively: use <code>osmium-tool</code> to filter the planet file for place names or settlements, then use plain <code>osm2pgsql</code> to import the resulting file)</li>
<li>use a PostGIS query to find the nearest place to a given pair of coordinates</li>
</ul>
<p>Since you're only interested in a fraction of OSM data, you shouldn't need too much disk space or memory for this, and you'll be able to make fast queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '18, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63861" class="comments-container">
&#10;</div>
<div id="comment-tools-63861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63861-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63864"></span>

<div id="answer-container-63864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63864-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With Nominatim you can try the &amp;zoom parameter. Default is trying to find an exact address (house number) 18. With 2 it looks just for the country. You can see the possible values in the dropdown field on <a href="https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=35.62534009803395&amp;lon=-95.48938751220705&amp;zoom=12">https://nominatim.openstreetmap.org/reverse.php?format=html&amp;lat=35.62534009803395&amp;lon=-95.48938751220705&amp;zoom=12</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '18, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-63864" class="comments-container">
&#10;</div>
<div id="comment-tools-63864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63864-form-container" class="comment-form-container">
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

