+++
type = "question"
title = "Find all amenities with name and address around a given location"
description = '''I would like to find all objects with an amenity tag within the radius of a location given by coordinates. E.g. I have a location and want to find what restaurants, bars, cafes, cinemas, etc. are around. For each found object I need its name and its address. As far as I have found out I can query No...'''
date = "2016-12-10T10:36:00Z"
lastmod = "2016-12-13T04:45:00Z"
weight = 53455
keywords = [ "query", "amenity", "nominatim", "find", "overpass" ]
aliases = [ "/questions/53455" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Find all amenities with name and address around a given location](/questions/53455/find-all-amenities-with-name-and-address-around-a-given-location)

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
<span id="post-53455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53455-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to find all objects with an amenity tag within the radius of a location given by coordinates. E.g. I have a location and want to find what restaurants, bars, cafes, cinemas, etc. are around. For each found object I need its name and its address.</p>
<p>As far as I have found out I can query Nominatim for special phrases and specific amenities but I'm not sure how to query for all amenities.</p>
<p>Is this possible with Nominatim and how is it done? Or should I rather use Overpass or something different for such a scenario?</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '16, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/184999104034d85f3b6114f1dd685fa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acgjheeb&#39;s gravatar image" />
<p><span>acgjheeb</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acgjheeb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53455" class="comments-container">
&#10;</div>
<div id="comment-tools-53455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53455-form-container" class="comment-form-container">
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

<span id="53519"></span>

<div id="answer-container-53519" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53519-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="acgjheeb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> suggested use 'around' filter with overpass api for all <a href="https://wiki.openstreetmap.org/wiki/Key:amenity">amenities</a>. Here is the example:</p>
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“aminity=*”
*/
[out:json];
// gather results
(
  // query part for: “aminity=*”
  node[&quot;amenity&quot;](around:2000,51.5,0.01);
  way[&quot;amenity&quot;](around:2000,51.5,0.01);
  relation[&quot;amenity&quot;](around:2000,51.5,0.01);
);
// print results
&#10;out;
&gt;;
out skel qt;</code></pre>
<p>With get method same request to overpass API:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];(node[%22amenity%22](around:2000,51.5,0.01);way[%22amenity%22](around:2000,51.5,0.01);relation[%22amenity%22](around:2000,51.5,0.01););out;%3E;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '16, 04:45</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53519" class="comments-container">
&#10;</div>
<div id="comment-tools-53519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53519-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53460"></span>

<div id="answer-container-53460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53460-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-53460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Definitely use Overpass which has an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">around</a> operator.</p>
<p>This is an example of such a query: <a href="http://overpass-turbo.eu/s/kzx">http://overpass-turbo.eu/s/kzx</a>.</p>
<p>Note that not every POI will have address information in OSM: it really depends on how much detail local mappers have entered into OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53460" class="comments-container">
<span id="53464"></span>
<div id="comment-53464" class="comment">
<div id="post-53464-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>sometimes the address information is there, but on the building, not on the POI itself. Overpass cannot solve this I think</p>
</div>
<div id="comment-53464-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 15:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53466"></span>
<div id="comment-53466" class="comment">
<div id="post-53466-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Regarding addresses: Maybe an <code>is_in</code> query can help but not sure if it includes unnamed areas with address tags.</p>
</div>
<div id="comment-53466-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 15:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53471"></span>
<div id="comment-53471" class="comment">
<div id="post-53471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, looks like <code>is_in</code> finds only named areas. It doesn't returns buildings with addresses but without a name. But a reverse-geocoding call to Nominatim would help do determine the address.</p>
</div>
<div id="comment-53471-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 22:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53487"></span>
<div id="comment-53487" class="comment">
<div id="post-53487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! I will dive into Overpass and try it out. If the address is not always there, is there at least a reliable way to determine the POIs city?</p>
</div>
<div id="comment-53487-info" class="comment-info">
<span class="comment-age">(11 Dec '16, 19:49)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
<span id="53488"></span>
<div id="comment-53488" class="comment">
<div id="post-53488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess separate reverse geocoding of the results with Nominatim won't be an option as it would produce a lot of traffic for Nominatim...</p>
</div>
<div id="comment-53488-info" class="comment-info">
<span class="comment-age">(11 Dec '16, 19:51)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
</div>
<div id="comment-tools-53460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53460-form-container" class="comment-form-container">
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

