+++
type = "question"
title = "How can I get the Polygon ID from lat/long?"
description = '''Hi...can any one plz tell me, how can I get the polygon ID from coordinates for certain towns.Thank you.'''
date = "2013-07-02T18:46:00Z"
lastmod = "2013-07-04T16:47:00Z"
weight = 23908
keywords = [ "id", "coordinates" ]
aliases = [ "/questions/23908" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get the Polygon ID from lat/long?](/questions/23908/how-can-i-get-the-polygon-id-from-latlong)

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
<span id="post-23908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23908-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi...can any one plz tell me, how can I get the polygon ID from coordinates for certain towns.Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '13, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7dfb73700c5e1accbe2cdf4cc0da7f4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uma%20Maheswari%20K&#39;s gravatar image" />
<p><span>Uma Maheswari K</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uma Maheswari K has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23908" class="comments-container">
&#10;</div>
<div id="comment-tools-23908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23908-form-container" class="comment-form-container">
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

<span id="23912"></span>

<div id="answer-container-23912" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23912-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to do such a query by hand, try the following:</p>
<p>go to <a href="http://nominatim.openstreetmap.org/">nominatim.openstreetmap.org</a> and type the name of the town in there.</p>
<p>See the results whether you get an entry with a little symbol like this: <img src="http://help.openstreetmap.org/upfiles/poi_boundary_administrative.glow.32.png" alt="alt text" /></p>
<p>Then choose "details" about it and you will see its OSM id.</p>
<p>Be aware: not all towns in the world have a valid boundary relation around.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '13, 21:04</strong> </span></p>
</div>
</div>
<div id="comments-container-23912" class="comments-container">
<span id="23953"></span>
<div id="comment-23953" class="comment">
<div id="post-23953-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,I want to get polygon ID for some towns in Canada. 'nominatim.openstreetmap.org' ,this link only gave me the polygon ID for states in Canada...When I looking for towns it will give town node ID only..How can get polygon ID for towns...Please clear doubt. Thank you.</p>
</div>
<div id="comment-23953-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 07:46)</span> <span class="comment-user userinfo">Uma Maheswari K</span>
</div>
</div>
<span id="23958"></span>
<div id="comment-23958" class="comment">
<div id="post-23958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you give some examples of what queries you've tried and what they return?</p>
</div>
<div id="comment-23958-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 09:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23969"></span>
<div id="comment-23969" class="comment">
<div id="post-23969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ya,sure I searched for a town named 'Calmar' ( It is situated in Alberta,Canada) It returns the following,</p>
<p>"Address</p>
<p>Calmar (Type: place:town, node 1135364356, 15, 0 GOTO)<br />
</p>
<p>Alberta (Type: boundary:administrative, relation 391186, 4, 2.03038389612396 GOTO)</p>
<p>Canada (Type: boundary:administrative, relation 1428125, 2, 20.1577291628353 GOTO"</p>
<p>When I click GOTO for Alberta it gives the boundary. But for Calmar it gives a node.I want boundary for Calmar But it returns node only.I want Polygon ID for this town to get that town boundary. Could you plz guide me...?</p>
</div>
<div id="comment-23969-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 11:35)</span> <span class="comment-user userinfo">Uma Maheswari K</span>
</div>
</div>
<span id="23972"></span>
<div id="comment-23972" class="comment">
<div id="post-23972-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Some settlements/places may only have been mapped with a node, not a polygon. Since the boundaries of some settlements are vague or ambiguous, some mappers feel this is a less misleading way of showing towns and villages. This means the polygon you're looking for simply may not exist.</p>
</div>
<div id="comment-23972-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 12:38)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="23991"></span>
<div id="comment-23991" class="comment">
<div id="post-23991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Uma, you can try webservices like <a href="http://www.flosm.de/en/Administrative-Boundaries.html">http://www.flosm.de/en/Administrative-Boundaries.html</a> or <a href="http://openmapsurfer.uni-hd.de">http://openmapsurfer.uni-hd.de</a> to see whether there are already any administartive boundaries around the towns you are looking for.</p>
<p>If is quite possible that not all towns or places in Canada have already boundary relations.</p>
</div>
<div id="comment-23991-info" class="comment-info">
<span class="comment-age">(04 Jul '13, 16:47)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-23912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23912-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23909"></span>

<div id="answer-container-23909" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23909-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can import the data into a PostGIS database (using <code>osm2pgsql</code> for example), then run a query that goes like</p>
<pre><code>select osm_id from planet_osm_polygon 
where 
   boundary=&#39;administrative&#39; and
   admin_level=&#39;8&#39; and
   ST_CONTAINS(way, ST_TRANSFORM(ST_SETSRID(ST_POINT(my_longitude,my_latitude), 4326), 900913));</code></pre>
<p>A similar query is possible with a database imported for Nominatim use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-23909" class="comments-container">
&#10;</div>
<div id="comment-tools-23909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23909-form-container" class="comment-form-container">
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

