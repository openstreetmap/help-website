+++
type = "question"
title = "Calculate the number of place_of_worship in a specific county / city"
description = '''The Overpass Api never worked for me, it only gives me a file called interpret, without an extension . that i do not know how to process and load in Qgis or JOSM Or another alternative would be to filter from the database extract of a country, but i do not know how to filter only a specific county i...'''
date = "2013-08-24T09:45:00Z"
lastmod = "2013-08-25T18:21:00Z"
weight = 25716
keywords = [ "overpassapi", "overpass", "statistics", "county" ]
aliases = [ "/questions/25716" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate the number of place_of_worship in a specific county / city](/questions/25716/calculate-the-number-of-place_of_worship-in-a-specific-county-city)

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
<span id="post-25716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Overpass Api never worked for me, it only gives me a file called interpret, without an extension . that i do not know how to process and load in Qgis or JOSM</p>
<p>Or another alternative would be to filter from the database extract of a country, but i do not know how to filter only a specific county in QGIS from a planet of country file</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-county" rel="tag" title="see questions tagged &#39;county&#39;">county</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '13, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/92a51d3af99ee124bb9e06dd35249910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badita%20Florin&#39;s gravatar image" />
<p><span>Badita Florin</span><br />
<span class="score" title="112 reputation points">112</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badita Florin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25716" class="comments-container">
<span id="25719"></span>
<div id="comment-25719" class="comment">
<div id="post-25719-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your question title does not bear much relation to the text underneath. Perhaps you would consider explicitly stating what you want to do, and move things like "Overpass API not working for you" somewhere else (preferably by deletion).</p>
<p>Try something like, I would like to determine the number of places of worship in a given regions (city, or country) contained in an OSM extract. The tools which I am familiar with are JOSM and QGIS.</p>
</div>
<div id="comment-25719-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 12:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25716-form-container" class="comment-form-container">
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

<span id="25736"></span>

<div id="answer-container-25736" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25736-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This <a href="http://overpass-turbo.eu/s/SG">overpass-turbo query</a> gives for Wien (Vienna):</p>
<p>110 nodes, 245 ways, 5 relations</p>
<p>that have amenity=place_of_worship set. Or for Roma: 200 nodes, 526 ways, 33 relations. Or for Austria: 2800 nodes, 4663 ways, 21 relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '13, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-25736" class="comments-container">
<span id="25778"></span>
<div id="comment-25778" class="comment">
<div id="post-25778-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>... see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> for documentation.</p>
</div>
<div id="comment-25778-info" class="comment-info">
<span class="comment-age">(25 Aug '13, 18:21)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-25736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25736-form-container" class="comment-form-container">
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

