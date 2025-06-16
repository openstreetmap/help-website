+++
type = "question"
title = "Is there any way to use OSM geocoder and get the location of places in any part of the street, not only at the vertices?"
description = '''Is there any way to use OSM geocode and get the location of places in any part of the street, not only at the vertices?  I&#x27;m using the OSM API geocoder, Nominatim.'''
date = "2014-08-13T14:11:00Z"
lastmod = "2014-08-13T19:49:00Z"
weight = 35785
keywords = [ "nominatim", "geocoder" ]
aliases = [ "/questions/35785" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to use OSM geocoder and get the location of places in any part of the street, not only at the vertices?](/questions/35785/is-there-any-way-to-use-osm-geocoder-and-get-the-location-of-places-in-any-part-of-the-street-not-only-at-the-vertices)

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
<span id="post-35785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35785-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to use OSM geocode and get the location of places in any part of the street, not only at the vertices?</p>
<p>I'm using the OSM API geocoder, Nominatim.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '14, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/043588bd817508d63c1e79a4c4d151ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cassia&#39;s gravatar image" />
<p><span>cassia</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cassia has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '14, 19:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-35785" class="comments-container">
&#10;</div>
<div id="comment-tools-35785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35785-form-container" class="comment-form-container">
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

<span id="35786"></span>

<div id="answer-container-35786" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35786-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim will report the precise position of an address if this address is mapped in OpenStreetMap <em>or</em> if an additionally imported dataset like TIGER contains the address.</p>
<p>If the address is not mapped, then there is no way how Nominatim can report a precise position. In these cases it will usually report a street midpoint, not a vertex as you seem to assume.</p>
<p>The suggested method to get around this limitation is mapping more house numbers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '14, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-35786" class="comments-container">
<span id="35791"></span>
<div id="comment-35791" class="comment">
<div id="post-35791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... also have a look at the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> in general.</p>
</div>
<div id="comment-35791-info" class="comment-info">
<span class="comment-age">(13 Aug '14, 19:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-35786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35786-form-container" class="comment-form-container">
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

