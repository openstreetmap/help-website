+++
type = "question"
title = "Why is OSM using GeoNames?"
description = '''The wiki says the OSM front end on openstreetmap.org is using GeoNames for the search. https://wiki.openstreetmap.org/wiki/Geonames Wondering because I might implement search functionality for a map myself, and because I&#x27;m curious.  How come GeoNames is used? Are there any benefits of doing this, ins...'''
date = "2014-03-23T14:17:00Z"
lastmod = "2014-03-23T18:24:00Z"
weight = 31793
keywords = [ "osm.org", "search", "frontend", "geonames", "names" ]
aliases = [ "/questions/31793" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is OSM using GeoNames?](/questions/31793/why-is-osm-using-geonames)

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
<span id="post-31793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31793-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The wiki says the OSM front end on openstreetmap.org is using GeoNames for the search. <a href="https://wiki.openstreetmap.org/wiki/Geonames">https://wiki.openstreetmap.org/wiki/Geonames</a> Wondering because I might implement search functionality for a map myself, and because I'm curious.</p>
<p>How come GeoNames is used? Are there any benefits of doing this, instead of pulling the data from OSM? I mean locations and names are in the OSM dataset.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-frontend" rel="tag" title="see questions tagged &#39;frontend&#39;">frontend</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '14, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ef5c6a363605aa3dd51a6faa998052b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niklas&#39;s gravatar image" />
<p><span>Niklas</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niklas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '14, 19:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31793" class="comments-container">
&#10;</div>
<div id="comment-tools-31793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31793-form-container" class="comment-form-container">
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

<span id="31796"></span>

<div id="answer-container-31796" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31796-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-31796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Niklas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We use OpenStreetMap (Nominatim) and a range of other sources (if you enter a British postcode data from Free the Postcode are also returned). Geonames is used as well as Nominatim because:</p>
<ul>
<li>it is open</li>
<li>created to be comprehensive, whereas OSM may depend on how well an area is mapped. 5 years ago when I joined OSM large areas of the UK, Spain etc didnt have place names let alone street names. Geonames did. So at least one could find an area for editing.</li>
<li>it's a useful supplement (particularly when OSM naming gets <em>too</em> detailed, try searching for the now non-existent administrative districts of Middlesex, Berkshire and Sussex on OSM - they dont appear from Nominatim because we have no objects tagged with these places</li>
<li>geonames may well be faster because of how it is run</li>
</ul>
<p>So it's not either/or; Geonames is a supplementary, but useful, source for locations on OSM.</p>
<p>P.S. I suspect the wiki page is a 'living fossil'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '14, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '14, 16:54</strong> </span></p>
</div>
</div>
<div id="comments-container-31796" class="comments-container">
<span id="31797"></span>
<div id="comment-31797" class="comment">
<div id="post-31797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great answer. Thank you!</p>
</div>
<div id="comment-31797-info" class="comment-info">
<span class="comment-age">(23 Mar '14, 18:24)</span> <span class="comment-user userinfo">Niklas</span>
</div>
</div>
</div>
<div id="comment-tools-31796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31796-form-container" class="comment-form-container">
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

