+++
type = "question"
title = "osmosis help for reverse geocoding (unable to geocode)"
description = '''Hi there, We are setting up a Nominatim server for the specific purpose of turning coordinates into City/Country data. We have managed to set it up with below parameters, but we are getting &quot;unable to geocode&quot; for a major city Melbourne in Australia, while it works fine for a major city in USA. Work...'''
date = "2017-12-20T22:03:00Z"
lastmod = "2017-12-20T22:19:00Z"
weight = 61304
keywords = [ "geocode", "osmosis" ]
aliases = [ "/questions/61304" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis help for reverse geocoding (unable to geocode)](/questions/61304/osmosis-help-for-reverse-geocoding-unable-to-geocode)

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
<span id="post-61304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>We are setting up a Nominatim server for the specific purpose of turning coordinates into City/Country data. We have managed to set it up with below parameters, but we are getting "unable to geocode" for a major city Melbourne in Australia, while it works fine for a major city in USA. Works fine for Moscow but not other cities in Russia.</p>
<p>Can anyone point us in the right direction here as we are wanting to filter down to only City/Country data to help reduce the size of things, but we want it to work anywhere.</p>
<hr />
<p>time osmosis \ --read-pbf-fast workers=${WORKERS} "${TMP_DIR}/source.osm.pbf" \ --buffer bufferCapacity=12000 \ --tf accept-relations boundary=administrative \ --tf accept-relations admin_level=8 \ --write-pbf file="${TMP_DIR}/step1.osm.pbf"</p>
<p>rm "${TMP_DIR}/source.osm.pbf"</p>
<p>time osmosis \ --read-pbf-fast workers=${WORKERS} "${TMP_DIR}/step1.osm.pbf" \ --buffer bufferCapacity=12000 \ --used-way \ --write-pbf file="${TMP_DIR}/step2.osm.pbf"</p>
<p>rm "${TMP_DIR}/step1.osm.pbf"</p>
<p>time osmosis \ --read-pbf-fast workers=${WORKERS} "${TMP_DIR}/step2.osm.pbf" \ --buffer bufferCapacity=12000 \ --used-node \ --write-pbf file="${TMP_DIR}/step3.osm.pbf"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocode" rel="tag" title="see questions tagged &#39;geocode&#39;">geocode</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Dec '17, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/50b099a979b02728c4af845ffd24ffed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbyter&#39;s gravatar image" />
<p><span>cbyter</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbyter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61304" class="comments-container">
&#10;</div>
<div id="comment-tools-61304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61304-form-container" class="comment-form-container">
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

<span id="61305"></span>

<div id="answer-container-61305" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61305-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The City of Melbourne has an admin_level=6 boundary: <a href="https://www.openstreetmap.org/relation/2404870">https://www.openstreetmap.org/relation/2404870</a> - the same is the case for many cities where I live; once they're large enough to not be "in" a county any more but "be" a county, they become one. Some cities in Germany - Berlin, Hamburg, Bremen - even have an admin_level of 4. Your code only extracts cities with admin_level=8.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '17, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-61305" class="comments-container">
&#10;</div>
<div id="comment-tools-61305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61305-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

