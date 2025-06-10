+++
type = "question"
title = "Point geometries not shown"
description = '''Hi everyone I just added some geometries to OSM. Polygons and lines are now visible in the brwoser. However, the point geometries (for instance parking garages) are not displayed: https://www.openstreetmap.org/query?lat=47.18589&amp;amp;lon=8.45825#map=19/47.18588/8.45911 In the editing mode they are vi...'''
date = "2022-09-21T09:51:00Z"
lastmod = "2022-09-22T10:03:00Z"
weight = 85674
keywords = [ "parking_entrance", "points" ]
aliases = [ "/questions/85674" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Point geometries not shown](/questions/85674/point-geometries-not-shown)

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
<span id="post-85674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85674-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone</p>
<p>I just added some geometries to OSM. Polygons and lines are now visible in the brwoser. However, the point geometries (for instance parking garages) are not displayed: <a href="https://www.openstreetmap.org/query?lat=47.18589&amp;lon=8.45825#map=19/47.18588/8.45911">https://www.openstreetmap.org/query?lat=47.18589&amp;lon=8.45825#map=19/47.18588/8.45911</a></p>
<p>In the editing mode they are visible: <a href="https://www.openstreetmap.org/edit#map=18/47.18615/8.45898">https://www.openstreetmap.org/edit#map=18/47.18615/8.45898</a></p>
<p>How can I get to be showed in the browser?</p>
<p>Thank you for your help in advance!</p>
<p>Cheers, Jana</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parking_entrance" rel="tag" title="see questions tagged &#39;parking_entrance&#39;">parking_entrance</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '22, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c77bdecc64d74f7a947ad5f64e95c101?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brja&#39;s gravatar image" />
<p><span>brja</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brja has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '22, 09:52</strong> </span></p>
</div>
</div>
<div id="comments-container-85674" class="comments-container">
&#10;</div>
<div id="comment-tools-85674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85674-form-container" class="comment-form-container">
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

<span id="85676"></span>

<div id="answer-container-85676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85676-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you mean <a href="https://www.openstreetmap.org/node/10041358339#map=19/47.18590/8.45871">https://www.openstreetmap.org/node/10041358339#map=19/47.18590/8.45871</a> I suspect the issue may be the layer tag. Note that the layer value is defintely wrong in any case if it is lower than an object covering it it should get a negative value or at least one that is lower than the other object.</p>
<p>Note that layer tags are for indicating the relative ordering of objects, not for indicating the level/floor the object is on, that would require the level tag.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Key:layer">https://wiki.openstreetmap.org/wiki/Key:layer</a> and <a href="https://wiki.openstreetmap.org/wiki/Key:level">https://wiki.openstreetmap.org/wiki/Key:level</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '22, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-85676" class="comments-container">
<span id="85678"></span>
<div id="comment-85678" class="comment">
<div id="post-85678-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Simon</p>
<p>Thanks a lot for your answer! Is there any way I can find out what level I must define?</p>
<p>I also defined point geometries of other types (e.g. parking_entry (<a href="https://www.openstreetmap.org/node/10041349956)">https://www.openstreetmap.org/node/10041349956)</a> and noexit (<a href="https://www.openstreetmap.org/node/10041389399)).">https://www.openstreetmap.org/node/10041389399)).</a> These do not have a layer value. How do I go about this?</p>
</div>
<div id="comment-85678-info" class="comment-info">
<span class="comment-age">(21 Sep '22, 15:02)</span> <span class="comment-user userinfo">brja</span>
</div>
</div>
<span id="85679"></span>
<div id="comment-85679" class="comment">
<div id="post-85679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After some more checking I suspect the reason why the icons are not rendered is that one of the many other objects that are layered on top of each other there are hiding them.</p>
<p>As a tendency I wouldn't be concerned that they are not being shown on a specific map, the objects are in the database and there is nothing specifically wrong with them.</p>
</div>
<div id="comment-85679-info" class="comment-info">
<span class="comment-age">(21 Sep '22, 15:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85681"></span>

<div id="answer-container-85681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like <code>amenity=parking</code> + <code>parking=underground</code> is not rendered in the standard style ¹:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/pull/3600">openstreetmap-carto#3600 Hide underground parking</a></p>
<p>The positions of the nodes <a href="https://www.openstreetmap.org/node/10041358339">10041358339</a> and <a href="https://www.openstreetmap.org/node/10041276960">10041276960</a> suggest that those are actually entrances and should probably be tagged as <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_entrance"><code>amenity=parking_entrance</code></a> + <code>parking=underground</code> (those should be rendered).</p>
<p>¹ found by searching "underground" in the source code repository of the standard style: <a href="https://github.com/gravitystorm/openstreetmap-carto/search?q=underground">https://github.com/gravitystorm/openstreetmap-carto/search?q=underground</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '22, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-85681" class="comments-container">
&#10;</div>
<div id="comment-tools-85681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85681-form-container" class="comment-form-container">
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

