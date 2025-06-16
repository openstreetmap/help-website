+++
type = "question"
title = "How to draw residential and industrial area of a city/town?"
description = '''Hallo, I&#x27;m trying to display differentiate symbols between big cities and small town, the filter is based on the place tag and population: For big cities, I would like to display the residential and industrial areas belonging to these cities. I do not see how to get all the polygons (tagged with lan...'''
date = "2012-12-03T16:38:00Z"
lastmod = "2012-12-04T15:05:00Z"
weight = 18169
keywords = [ "landuse", "place" ]
aliases = [ "/questions/18169" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to draw residential and industrial area of a city/town?](/questions/18169/how-to-draw-residential-and-industrial-area-of-a-citytown)

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
<span id="post-18169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18169-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo,</p>
<p>I'm trying to display differentiate symbols between big cities and small town, the filter is based on the place tag and population: For big cities, I would like to display the residential and industrial areas belonging to these cities.</p>
<p>I do not see how to get all the polygons (tagged with landuse) belonging to a given city.</p>
<p>Starting from <a href="https://www.openstreetmap.org/browse/node/1559853166">https://www.openstreetmap.org/browse/node/1559853166</a></p>
<p>I get the boundaries of the city at <a href="https://www.openstreetmap.org/browse/relation/62407">https://www.openstreetmap.org/browse/relation/62407</a></p>
<p>but not the polygons inside it like this one <a href="https://www.openstreetmap.org/browse/relation/1394163">https://www.openstreetmap.org/browse/relation/1394163</a></p>
<p>Any ideas how to get it right?</p>
<p>regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '12, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/adab53006c1f6745dee5edbfb1d3c5f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Groquik&#39;s gravatar image" />
<p><span>Groquik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Groquik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '12, 16:38</strong> </span></p>
</div>
</div>
<div id="comments-container-18169" class="comments-container">
&#10;</div>
<div id="comment-tools-18169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18169-form-container" class="comment-form-container">
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

<span id="18170"></span>

<div id="answer-container-18170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18170-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know there is no connection between the unice place node of a city together with its boundary relataion AND any are that cobers a specific landuse.</p>
<p>So you have to build the connection on your own.</p>
<p>One possibility to solve this is to use the online service <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass_API</a>.</p>
<p>There you can query for any kind of OSM objects, either limited by a bounding box OR limited by an area relation. The key parameter is area_query like described here: <a href="/questions/12608/extract-pois-for-a-region">extract-pois-for-a-region</a></p>
<p>Or read all guides and examples about overpass API in the OSM wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '12, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-18170" class="comments-container">
<span id="18187"></span>
<div id="comment-18187" class="comment">
<div id="post-18187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the hint.</p>
<p>Since I want to do it over a bigger area, I'm not sure that the overpass API would be a suitable tool, but the overall idea remains applicable.</p>
<p>I'll try to "enhance" the relation landuse and to add some private tags to link them to their respective "place" based on "does the relation polygon crosses the city boundaries"</p>
</div>
<div id="comment-18187-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 09:19)</span> <span class="comment-user userinfo">Groquik</span>
</div>
</div>
<span id="18188"></span>
<div id="comment-18188" class="comment">
<div id="post-18188-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It depends on the size of the area but the Overpass API is usually better suited for large requests than most (if not all) other APIs. You can also increase the timeout as explained in the documentation if the default value is too low. But for really large requests you should better get a <a href="https://wiki.openstreetmap.org/wiki/Extract#Country_and_area_extracts">country or area extract</a>.</p>
</div>
<div id="comment-18188-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 09:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="18191"></span>
<div id="comment-18191" class="comment">
<div id="post-18191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You cannot add your own "private tags" just to solve a spatial query.</p>
</div>
<div id="comment-18191-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 15:05)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-18170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18170-form-container" class="comment-form-container">
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

