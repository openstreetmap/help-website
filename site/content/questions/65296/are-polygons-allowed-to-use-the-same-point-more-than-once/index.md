+++
type = "question"
title = "Are polygons allowed to use the same point more than once?"
description = '''The OGC Simple Feature spec says that the rings making up the boundaries of a polygon must be closed and simple, and its definition of &quot;simple&quot; includes that the ring may not pass through the same point more than once (except at the ends). However, Mapnik happily renders such polygons, for example (...'''
date = "2018-08-13T11:21:00Z"
lastmod = "2018-08-13T18:58:00Z"
weight = 65296
keywords = [ "validation", "polygon" ]
aliases = [ "/questions/65296" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Are polygons allowed to use the same point more than once?](/questions/65296/are-polygons-allowed-to-use-the-same-point-more-than-once)

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
<span id="post-65296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65296-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The OGC Simple Feature spec says that the rings making up the boundaries of a polygon must be closed and simple, and its definition of "simple" includes that the ring may not pass through the same point more than once (except at the ends). However, Mapnik happily renders such polygons, for example (at the time of writing this) <a href="https://www.openstreetmap.org/way/447865387">way 447865387</a>, which uses node 4449293245 twice.</p>
<p>Should I fix my import pipeline to convert this into a multipolygon (or simply two polygons) before loading it into PostGIS, or should I fix the data to remove the self-intersection?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '18, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '18, 11:22</strong> </span></p>
</div>
</div>
<div id="comments-container-65296" class="comments-container">
<span id="65302"></span>
<div id="comment-65302" class="comment">
<div id="post-65302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"However, Mapnik happily renders such polygons," I don't think it does: <a href="https://www.openstreetmap.org/way/447865387#map=19/63.27383/18.67055">https://www.openstreetmap.org/way/447865387#map=19/63.27383/18.67055</a></p>
</div>
<div id="comment-65302-info" class="comment-info">
<span class="comment-age">(13 Aug '18, 16:22)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="65310"></span>
<div id="comment-65310" class="comment">
<div id="post-65310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a>: Hm, no, you're right. My bad. What about this one, then? It has a "pocket" in it, but looks like it's rendering: <a href="https://www.openstreetmap.org/way/481643030">https://www.openstreetmap.org/way/481643030</a></p>
</div>
<div id="comment-65310-info" class="comment-info">
<span class="comment-age">(13 Aug '18, 18:58)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
</div>
<div id="comment-tools-65296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65296-form-container" class="comment-form-container">
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

<span id="65297"></span>

<div id="answer-container-65297" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65297-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="turepalsson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Self intersection is an error in the OSM data model too (insofar we actually have a notion of such), however most tools will undertake an effort to process not quite valid objects.</p>
<p>In summary IMHO you should fix the object in question in OSM. More reading: <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Valid_Multipolygon_conditions">https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Valid_Multipolygon_conditions</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '18, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '18, 14:47</strong> </span></p>
</div>
</div>
<div id="comments-container-65297" class="comments-container">
<span id="65298"></span>
<div id="comment-65298" class="comment">
<div id="post-65298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For multipolygon, the wiki (<a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/validity)">https://wiki.openstreetmap.org/wiki/Relation:multipolygon/validity)</a> explicitly allows some self-intersections. Perhaps that should be changed?</p>
</div>
<div id="comment-65298-info" class="comment-info">
<span class="comment-age">(13 Aug '18, 11:47)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="65301"></span>
<div id="comment-65301" class="comment">
<div id="post-65301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would consider the first variant "wrong" too, the thing is, as already mentioned there is no validation on input so you can essentially construct lots of things that you shouldn't do. JOSM will complain about a self-intersecting way in any case.</p>
<p>Note <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/validity">https://wiki.openstreetmap.org/wiki/Relation:multipolygon/validity</a> has essentially had one editor that added the original content 6 years ago, we would need to discuss if ire represents current thinking.</p>
</div>
<div id="comment-65301-info" class="comment-info">
<span class="comment-age">(13 Aug '18, 14:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65297-form-container" class="comment-form-container">
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

