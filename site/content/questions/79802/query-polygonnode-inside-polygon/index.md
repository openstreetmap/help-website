+++
type = "question"
title = "Query polygon/node inside polygon"
description = '''Hello List, is there a way to get amenity=school polygons or nodes inside amenity=school polygons?'''
date = "2021-04-22T09:19:00Z"
lastmod = "2021-04-26T11:07:00Z"
weight = 79802
keywords = [ "qa", "overpass" ]
aliases = [ "/questions/79802" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query polygon/node inside polygon](/questions/79802/query-polygonnode-inside-polygon)

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
<span id="post-79802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79802-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello List, is there a way to get amenity=school polygons or nodes inside amenity=school polygons?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qa" rel="tag" title="see questions tagged &#39;qa&#39;">qa</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '21, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79802" class="comments-container">
&#10;</div>
<div id="comment-tools-79802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79802-form-container" class="comment-form-container">
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

<span id="79806"></span>

<div id="answer-container-79806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79806-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use Overpass, find all school polygons in an area and then for each one see if there is a school within it. This <a href="https://overpass-turbo.eu/s/16tT">example</a> is based on the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#golf.3Dfairway_outside_leisure.3Dgolf_course">fairways exampl</a>e from the OSM Wiki;</p>
<pre><code>{{geocodeArea:Nottingham}}-&gt;.searchArea;
wr[&quot;amenity&quot;=&quot;school&quot;](area.searchArea);
map_to_area-&gt;.schools;
nwr(area.schools)[&quot;amenity&quot;=&quot;school&quot;];
out; &gt; ; out geom;</code></pre>
<p>I happen to know of at least one school within a school (which in this case is not a bug, so please don't 'fix' it) within this city.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '21, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-79806" class="comments-container">
<span id="79822"></span>
<div id="comment-79822" class="comment">
<div id="post-79822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm aware there are some discussions about considering it an issue. I commented school wiki page [1] and I hope conclusions will go for landuse=school.</p>
<p>Thanks for the fast and clear example... and don't worry for your school ;-)</p>
<p>[1] <a href="https://wiki.openstreetmap.org/wiki/Talk:Tag:amenity%3Dschool#Use_of_landuse.3Dschool">https://wiki.openstreetmap.org/wiki/Talk:Tag:amenity%3Dschool#Use_of_landuse.3Dschool</a></p>
</div>
<div id="comment-79822-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 12:27)</span> <span class="comment-user userinfo">Cascafico</span>
</div>
</div>
<span id="79823"></span>
<div id="comment-79823" class="comment">
<div id="post-79823-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This is an extreme minority view about amenity=school, unsubstantiated by any meaningful discussion. All educational institutions can be assumed to have an implicit landuse of education, but there is nothing to be gained from adding it explicitly, and "school" would be the wrong value anyway.</p>
</div>
<div id="comment-79823-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 12:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="79870"></span>
<div id="comment-79870" class="comment">
<div id="post-79870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In OSM I think there is a fundamental difference between phisical objects and functional ones:<br />
- landuse is phisical<br />
- amenity is functional<br />
Hence IMHO there is no redundancy in using a tagging schema like this:</p>
<p>building=school (inner poly)<br />
amenity=school (whatever primitive your knowledge represents better the function)<br />
landuse=school (outer poly)</p>
<p>I came to this schema trying to map a school which I know very well. An area used by 3 different inner schools, each with its own isced:level and name.</p>
</div>
<div id="comment-79870-info" class="comment-info">
<span class="comment-age">(26 Apr '21, 11:07)</span> <span class="comment-user userinfo">Cascafico</span>
</div>
</div>
</div>
<div id="comment-tools-79806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79806-form-container" class="comment-form-container">
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

