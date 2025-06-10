+++
type = "question"
title = "Fixing landuse overlap"
description = '''Is there tools to help fixing landuse (or landcover) overlaps? Here is an example: osm.org/way/436248091 the lake overlaps a wide landcover=forest multipolygon (as deduced from the rendering: notice the tree symbols rendered on the water area). As described here: Forest with lake (One outer and one ...'''
date = "2019-03-29T03:15:00Z"
lastmod = "2019-04-08T02:23:00Z"
weight = 68537
keywords = [ "josm", "landuse", "polygon", "overlap", "multipolygon" ]
aliases = [ "/questions/68537" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Fixing landuse overlap](/questions/68537/fixing-landuse-overlap)

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
<span id="post-68537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68537-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there tools to help fixing landuse (or landcover) overlaps?</p>
<p>Here is an example: <a href="https://www.openstreetmap.org/way/436248091#map=15/4.3184/-51.9759">osm.org/way/436248091</a><br />
the lake overlaps a wide <em>landcover=forest</em> multipolygon<br />
(as deduced from the rendering: notice the tree symbols rendered on the water area).</p>
<p>As described here: <a href="https://wiki.openstreetmap.org%20%20/wiki/Multipolygon_Examples#Forest_with_lake_.28One_outer_and_one_inner_ring.29">Forest with lake (One outer and one inner ring)</a><br />
the lake way should be added to the wide multipolygon relation with a inner role.</p>
<p>If i try to fix this with JOSM, only <a href="http://osm.org/way/436248091">way 436248091</a> will be downloaded and displayed.<br />
Are there tools to<br />
* find the wide multipolygon ID<br />
* given the 2 polygon IDs, automatically propose a fix to the JOSM user<br />
* detect overlap cases (Overpass maybe?) ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '19, 03:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9cf4a749f5b36bdb33a0cf10bf121f4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrienandrem&#39;s gravatar image" />
<p><span>adrienandrem</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrienandrem has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '19, 17:08</strong> </span></p>
</div>
</div>
<div id="comments-container-68537" class="comments-container">
&#10;</div>
<div id="comment-tools-68537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68537-form-container" class="comment-form-container">
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

<span id="68539"></span>

<div id="answer-container-68539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68539-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you zoom out enough in JOSM, you will find way <a href="https://www.openstreetmap.org/way/436800951#map=12/4.2834/-52.0013">https://www.openstreetmap.org/way/436800951#map=12/4.2834/-52.0013</a> that represents the surrounding forest.</p>
<p>I doubt you can do that in iD.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '19, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span> </br></br></p>
</div>
</div>
<div id="comments-container-68539" class="comments-container">
<span id="68594"></span>
<div id="comment-68594" class="comment">
<div id="post-68594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is the way to do it manually yes. The question is about helper tools, like plugins, for this use case.</p>
</div>
<div id="comment-68594-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 00:49)</span> <span class="comment-user userinfo">adrienandrem</span>
</div>
</div>
<span id="68609"></span>
<div id="comment-68609" class="comment">
<div id="post-68609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is a problem with natural=water on a landuse in the Carto CSS rendering. There is not always problem with 2 overlapping polygons.</p>
<p>Furthermore, the question remains whether the lake is part of the forest or not. IMHO, it is part of the forest, it is not part of the tree covered area though. So should it really be cut out of the forest polygon ?</p>
</div>
<div id="comment-68609-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 12:32)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="68697"></span>
<div id="comment-68697" class="comment">
<div id="post-68697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for pointing out that a natural=* overlapping a landuse=* might be justified. I hadn't spotted the landuse key in this case. But as natural=wood describes better what is really there, i corrected the map.</p>
</div>
<div id="comment-68697-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 00:35)</span> <span class="comment-user userinfo">adrienandrem</span>
</div>
</div>
</div>
<div id="comment-tools-68539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68539-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68625"></span>

<div id="answer-container-68625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68625-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your last comment indicates that you are interested in a general/algorithmic solution of the issue. With a high probability you will not find any editors with such function. There are many reasons to that. The outer polygon might be very large, the lake polygon is over the borders of several neighbouring larger forest polygons, then the opposite – a forest polygon over a lake or river polygon, a generalized case of the former cases, just to mention some. But it is not the end. Assume there was a hole under the lake in your example but the borders do not coincide. So, the problem starts long before we come to the issue you have met.<br />
While in the raster image based map-making the issue is almost irrelevant the situation is quite different in the modern GIS and digital cartography. There, users should (and they do) have functions that resolve the mentioned issues. These issues were several times up to discussion on some OSM forums and I have also presented a possible solution in the articles here <a href="https://lists.openstreetmap.org/pipermail/talk/2017-March/077710.html">https://lists.openstreetmap.org/pipermail/talk/2017-March/077710.html</a> and here <a href="https://lists.openstreetmap.org/pipermail/talk/2017-April/077824.html.">https://lists.openstreetmap.org/pipermail/talk/2017-April/077824.html.</a> The first one contains some theoretical hints. The second one is a complete demonstration example using forest and other necessary OSM data from Japan. Some people would naively like to have such complex issue described in several sentences what is impossible. So, if you have patience read them and have a special focus on the Japanese forests examples. There you have a full answer to your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '19, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-68625" class="comments-container">
<span id="68699"></span>
<div id="comment-68699" class="comment">
<div id="post-68699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What i am looking for are functionalities to help the mapper gather information, as relevant as possible.<br />
Keeping things simple, my question could be rewritten as:<br />
- Quality Assurance tools already detect building overlaps, does something similar exist for natural=* polygons, in KeepRight for example?<br />
- on the website the Query Feature tool returns Enclosing features, in JOSM would there be a way to get this kind of result when selecting an element?</p>
<p>N.B.: limiting overlaps to A.contains(B) would be good enough.</p>
</div>
<div id="comment-68699-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 02:23)</span> <span class="comment-user userinfo">adrienandrem</span>
</div>
</div>
</div>
<div id="comment-tools-68625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68625-form-container" class="comment-form-container">
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

