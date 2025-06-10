+++
type = "question"
title = "use polygon for an overpass turbo query"
description = '''Hey, is it possible to add a polygon (for example the shape of a city) in overpass turbo, so that the output only contains data from the city (inside of the polygon)? Can I drag and drop or open a shapefile in overpass turbo for that? Or is there a way to draw one? Thanks for your help! '''
date = "2022-06-07T11:00:00Z"
lastmod = "2022-06-07T14:32:00Z"
weight = 84723
keywords = [ "shapefile", "overpass", "polygon" ]
aliases = [ "/questions/84723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [use polygon for an overpass turbo query](/questions/84723/use-polygon-for-an-overpass-turbo-query)

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
<span id="post-84723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, is it possible to add a polygon (for example the shape of a city) in overpass turbo, so that the output only contains data from the city (inside of the polygon)? Can I drag and drop or open a shapefile in overpass turbo for that? Or is there a way to draw one? Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '22, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/749db2750393b3be709a6e9a2c654b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milo22948392&#39;s gravatar image" />
<p><span>milo22948392</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milo22948392 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84723" class="comments-container">
&#10;</div>
<div id="comment-tools-84723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84723-form-container" class="comment-form-container">
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

<span id="84727"></span>

<div id="answer-container-84727" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Edit: You can't import data into overpass &amp; it doesn't really understand true polygons, just closed ways, but you can use existing OSM data.</p>
<p>There's quite a few ways to achieve this depending on what data you have for the area to be searched:</p>
<pre><code>{{geocodeArea:Greater London}};
rel(pivot)-&gt;.Bound; //change to way to render
way(r.Bound)-&gt;.Bound;
.Bound out geom;
nwr[amenity=police](area);
out center;</code></pre>
<p>These three lines are only to display the search area's boundary &amp; can be removed if desired:</p>
<pre><code>rel(pivot)-&gt;.Bound; //change to way to render
way(r.Bound)-&gt;.Bound;
.Bound out geom;</code></pre>
<p>The boundary's ID:</p>
<pre><code>rel(175342); map_to_area;
nwr[amenity=police](area);
out center;</code></pre>
<p>The IDs for relations start at 3600000000 so by adding the id value to it allows</p>
<pre><code>area(3600175342);
nwr[amenity=police](area);
out center;</code></pre>
<p>Note the different brackets used:</p>
<pre><code>area[name=&#39;Greater London&#39;];
nwr[amenity=police](area);
out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '22, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '22, 15:52</strong> </span></p>
</div>
</div>
<div id="comments-container-84727" class="comments-container">
&#10;</div>
<div id="comment-tools-84727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84727-form-container" class="comment-form-container">
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

