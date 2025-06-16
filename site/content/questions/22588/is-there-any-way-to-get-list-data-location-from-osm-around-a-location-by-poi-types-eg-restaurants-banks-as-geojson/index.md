+++
type = "question"
title = "Is there any way to get list data location from OSM around a location by POI types (e.g: restaurants , banks , ...) as geoJson?"
description = '''Hi everyone I am a beginer with OSM dev I am currently working with different technologies for searching and showing OSM data in by search POI types . Like Google map , we have : https://maps.googleapis.com/maps/api/place/nearbysearch/json? and then put parameter to this URL so we can get a JSON Arr...'''
date = "2013-05-21T03:58:00Z"
lastmod = "2013-05-21T19:19:00Z"
weight = 22588
keywords = [ "osm", "geojson" ]
aliases = [ "/questions/22588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to get list data location from OSM around a location by POI types (e.g: restaurants , banks , ...) as geoJson?](/questions/22588/is-there-any-way-to-get-list-data-location-from-osm-around-a-location-by-poi-types-eg-restaurants-banks-as-geojson)

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
<span id="post-22588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone</p>
<p>I am a beginer with OSM dev I am currently working with different technologies for searching and showing OSM data in by search POI types . Like Google map , we have : <a href="https://maps.googleapis.com/maps/api/place/nearbysearch/json?">https://maps.googleapis.com/maps/api/place/nearbysearch/json?</a></p>
<p>and then put parameter to this URL so we can get a JSON Array with location data in types and nearby a location</p>
<p>Does anyone know if there exists something ? and any one have idead to help me Sorry about my English . I am not good at english. Thank you very much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '13, 03:58</strong></p>
<img src="https://secure.gravatar.com/avatar/380319feffefcd9263465a1414850662?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TuanDM&#39;s gravatar image" />
<p><span>TuanDM</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TuanDM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22588" class="comments-container">
&#10;</div>
<div id="comment-tools-22588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22588-form-container" class="comment-form-container">
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

<span id="22590"></span>

<div id="answer-container-22590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22590-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-22590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> supports an <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Something_near_something_else">around</a> keyword (see <a href="http://overpass-turbo.eu/?Q=%3Cosm-script%3E%0A%20%20%3Cquery%20type%3D%22node%22%3E%0A%20%20%20%20%3Chas-kv%20k%3D%22name%22%20v%3D%22Bonn%22%2F%3E%0A%20%20%3C%2Fquery%3E%0A%20%20%3Cquery%20type%3D%22node%22%3E%0A%20%20%20%20%3Caround%20radius%3D%221000%22%2F%3E%0A%20%20%20%20%3Chas-kv%20k%3D%22name%22%20v%3D%22Gielgen%22%2F%3E%0A%20%20%3C%2Fquery%3E%0A%20%20%3Cprint%2F%3E%0A%3C%2Fosm-script%3E&amp;C=50.74033;7.19436;16&amp;R">Overpass Turbo</a> for a visualization of the example) and of course instead of a place you can also <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#All_kind_of_objects">specify a bounding box</a>. <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Control_output_format">Various output formats</a> are supported.</p>
<p>Example:</p>
<pre><code>[out:json]
;
node[&quot;name&quot;=&quot;Leipzig&quot;];
(
  node
    (around:150)
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;];
  way
    (around:150)
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;];
  relation
    (around:150)
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;];
);
out body;
&gt;;
out skel;</code></pre>
<p>This query <a href="http://overpass-turbo.eu/s/cx">returns</a> all bank and restaurant within a distance of 150 meter around any node with the name <em>Leipzig</em>.</p>
<p>Or <a href="http://overpass-turbo.eu/s/cw">another query</a> using a <a href="https://wiki.openstreetmap.org/wiki/Bounding_Box">bounding box</a> instead of an object:</p>
<pre><code>[out:json]
;
(
  node
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;]
    (51.335,12.368,51.345,12.378);
  way
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;]
    (51.335,12.368,51.345,12.378);
  relation
    [&quot;amenity&quot;~&quot;bank|restaurant&quot;]
    (51.335,12.368,51.345,12.378);
);
out body;
&gt;;
out skel;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '13, 06:26</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '13, 19:19</strong> </span></p>
</div>
</div>
<div id="comments-container-22590" class="comments-container">
<span id="22594"></span>
<div id="comment-22594" class="comment">
<div id="post-22594-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>First, thank for your answer.It's very helpful to me . One more question.How about Search with exactly lat and long , not an exactly node's name. Thanks</p>
</div>
<div id="comment-22594-info" class="comment-info">
<span class="comment-age">(21 May '13, 10:21)</span> <span class="comment-user userinfo">TuanDM</span>
</div>
</div>
<span id="22596"></span>
<div id="comment-22596" class="comment">
<div id="post-22596-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can also specify a bounding box as already explained. I updated my answer with a bbox example.</p>
</div>
<div id="comment-22596-info" class="comment-info">
<span class="comment-age">(21 May '13, 12:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22605"></span>
<div id="comment-22605" class="comment">
<div id="post-22605-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Might want to add ways to that query. If the buildings are mapped then, as I understand it, the POI (restaurant, bank, etc.) may (should) be tagged on the way instead of on a node.</p>
</div>
<div id="comment-22605-info" class="comment-info">
<span class="comment-age">(21 May '13, 17:04)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="22607"></span>
<div id="comment-22607" class="comment">
<div id="post-22607-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I updated both examples to search for nodes, ways and relations.</p>
</div>
<div id="comment-22607-info" class="comment-info">
<span class="comment-age">(21 May '13, 19:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22590-form-container" class="comment-form-container">
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

