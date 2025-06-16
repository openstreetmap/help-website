+++
type = "question"
title = "How to get bbox of city"
description = '''Hi ! I have 1000 cities that I want to make a list of bboxes, where they fit in then to generate tiles for them 1 by 1. The problem is that manually to find out and insert in system database the bboxes are very time consuming and annoying. Is there any API that I can find out the city bbox ??  Lets ...'''
date = "2013-02-09T10:58:00Z"
lastmod = "2017-12-22T01:49:00Z"
weight = 19774
keywords = [ "boundaries", "bbox" ]
aliases = [ "/questions/19774" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to get bbox of city](/questions/19774/how-to-get-bbox-of-city)

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
<span id="post-19774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi ! I have 1000 cities that I want to make a list of bboxes, where they fit in then to generate tiles for them 1 by 1. The problem is that manually to find out and insert in system database the bboxes are very time consuming and annoying. Is there any API that I can find out the city bbox ??</p>
<p>Lets say with geonames.org I can find the center of map, but how to find appropriate bbox ???</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19774" class="comments-container">
<span id="19785"></span>
<div id="comment-19785" class="comment">
<div id="post-19785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to find the "city polygon", which may or may not be tagged as belonging to the city.</p>
<p>I think it is a very hard task to extract city bboxes from a OSM dataset. You could probably do this easier using some sort of national dataset provided by your national geographic agency.</p>
</div>
<div id="comment-19785-info" class="comment-info">
<span class="comment-age">(09 Feb '13, 20:06)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-19774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19774-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="19832"></span>

<div id="answer-container-19832" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19832-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gevork has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could extract the boundary=administrative areas for the cities you want with the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> (or <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a>, but that has more limitations on use), convert the .osm file to a shapefile, then use <a href="http://www.gdal.org/ogr/">ogr</a> to extract the bounding box. In python, all you'd need would be something like the following, which you could then write to a new file. Note that many of the boundaries will be relations, but you can query for those too.</p>
<pre><code>ds = ogr.Open(&quot;DatasourceName&quot;)
lyr = ds.GetLayerByName(&quot;LayerName&quot;)   
lyr.ResetReading()
&#10;feat = lyr.GetNextFeature()
while feat is not None:
    env = feat.GetGeometryRef().GetEnvelope()
    ## env returns  [0]=minX,[1]=maxX,[2]=minY,[3]=maxY</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '13, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-19832" class="comments-container">
&#10;</div>
<div id="comment-tools-19832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19832-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61320"></span>

<div id="answer-container-61320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61320-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding to <a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a>'s answer, here is an example Overpass query to return the bounding box of the AU-NSW admin boundary, then you can see the bounding box in the Data tab at <a href="https://overpass-turbo.eu/.">https://overpass-turbo.eu/.</a></p>
<pre><code>[out:json];
(
relation[&quot;ISO3166-2&quot;=&quot;AU-NSW&quot;][boundary=administrative];
);
out skel bb qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '17, 01:49</strong></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharvey has 4 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61320" class="comments-container">
&#10;</div>
<div id="comment-tools-61320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61320-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19818"></span>

<div id="answer-container-19818" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to have boundingboxes for ceratin places, there is so far no other way to define them manually, because there is no such information in the OSM data about boundingboxes around cities or places.</p>
<p>BUT you can try to find boundary polygons for many cities that are stores in data relations within the OSM data.</p>
<p>Go to <a href="http://nominatim.openstreetmap.org"></a><a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a> and type in a name of a wanted place. If the result list gives back a place with this special icon: <img src="http://nominatim.openstreetmap.org/images/mapicons/poi_boundary_administrative.p.20.png" alt="alt text" /> ... then this can be the right boundary. Verify this by hand for some examples.</p>
<p>In theory, now you can create a boundingbox where the boundary polygon is fitting in. Maybe it is even possible to run Nominatim in a kind of batch modus and to create that bboxes automatically.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '13, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</img>
</div>
</div>
<div id="comments-container-19818" class="comments-container">
&#10;</div>
<div id="comment-tools-19818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19818-form-container" class="comment-form-container">
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

