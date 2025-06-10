+++
type = "question"
title = "Nominatim - Certain postcodes not being recognised (e.g. Manchester, Edinburgh)"
description = '''We are finding that with specific postcodes, Nominatim returns incorrect results for the location. Example 1 Some postcodes in Edinburgh are geolocated to London. It appears to miss a crucial &#x27;H&#x27; in the postcode. EH1 1JX is geocoded as E1 1JX Example 2 M5 4SW is a Manchester postcode. It is geocodin...'''
date = "2016-04-21T11:01:00Z"
lastmod = "2016-04-26T09:36:00Z"
weight = 49332
keywords = [ "error", "nominatim", "postcode", "bug", "postcodes" ]
aliases = [ "/questions/49332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - Certain postcodes not being recognised (e.g. Manchester, Edinburgh)](/questions/49332/nominatim-certain-postcodes-not-being-recognised-eg-manchester-edinburgh)

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
<span id="post-49332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are finding that with specific postcodes, Nominatim returns incorrect results for the location.</p>
<p><strong>Example 1</strong></p>
<p>Some postcodes in Edinburgh are geolocated to London. It appears to miss a crucial 'H' in the postcode.</p>
<p>EH1 1JX is geocoded as E1 1JX</p>
<p><strong>Example 2</strong></p>
<p>M5 4SW</p>
<p>is a Manchester postcode. It is geocoding to somewhere in Walsall, as it is on the M5 motorway and the M5 is being picked up.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-postcodes" rel="tag" title="see questions tagged &#39;postcodes&#39;">postcodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '16, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/70fcea9783126f5fe1027fc2c671e4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evvntdev&#39;s gravatar image" />
<p><span>evvntdev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evvntdev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49332" class="comments-container">
&#10;</div>
<div id="comment-tools-49332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49332-form-container" class="comment-form-container">
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

<span id="49432"></span>

<div id="answer-container-49432" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49432-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure exactly, but it's important to notice this part of the <a href="http://wiki.openstreetmap.org/wiki/Nominatim/FAQ#My_postcode_is_missing.2Fwrong_but_I.27ve_fixed_it_in_the_OSM_data._What_is_wrong.3F">Nominatim FAQ about postcodes</a>:</p>
<blockquote>
<p>My postcode is missing/wrong but I've fixed it in the OSM data. What is wrong?</p>
<p>Support for post codes in Nominatim currently is very primitive. The post codes you see have been computed from OSM data in October 2012 and they are not updated. Postcodes from addr:postcode and similar tags are largely ignored. Please don't report bugs about postcodes. Better support for them is planned and will arrive at some time in the future.</p>
</blockquote>
<p>Which implies it's not going to work at all, sorry. :(</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '16, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-49432" class="comments-container">
&#10;</div>
<div id="comment-tools-49432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49432-form-container" class="comment-form-container">
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

