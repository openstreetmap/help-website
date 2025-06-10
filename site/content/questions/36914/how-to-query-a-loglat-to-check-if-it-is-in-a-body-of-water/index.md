+++
type = "question"
title = "How to query a log/lat to check if it is in a body of water?"
description = '''I would like to query OpenStreetMap with a given longitude and latitude and check to see if it is in a body of water (i.e. if the location is in the ocean or in a lake, etc.). Is this possible? If so, can someone give me an example on how to do this? My goal is to place markers on a map at random po...'''
date = "2014-09-18T19:41:00Z"
lastmod = "2014-09-21T10:32:00Z"
weight = 36914
keywords = [ "water", "marker", "ocean" ]
aliases = [ "/questions/36914" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query a log/lat to check if it is in a body of water?](/questions/36914/how-to-query-a-loglat-to-check-if-it-is-in-a-body-of-water)

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
<span id="post-36914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36914-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to query OpenStreetMap with a given longitude and latitude and check to see if it is in a body of water (i.e. if the location is in the ocean or in a lake, etc.). Is this possible? If so, can someone give me an example on how to do this?</p>
<p>My goal is to place markers on a map at random positions, however, I do not want the markers out in the middle of an ocean.</p>
<p>I am not trying to build a map with OSM. I just want to retrieve the data for use in another program.</p>
<p>I am very new to OpenStreetMap and would appreciate any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-ocean" rel="tag" title="see questions tagged &#39;ocean&#39;">ocean</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '14, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/89c3ce5350cd3e1332b22cf31084e573?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponchoman1&#39;s gravatar image" />
<p><span>ponchoman1</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponchoman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '14, 19:50</strong> </span></p>
</div>
</div>
<div id="comments-container-36914" class="comments-container">
<span id="36930"></span>
<div id="comment-36930" class="comment">
<div id="post-36930-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you need this for the whole planet ? Do you have some skills on postGIS database and queries ?</p>
</div>
<div id="comment-36930-info" class="comment-info">
<span class="comment-age">(19 Sep '14, 13:18)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-36914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36914-form-container" class="comment-form-container">
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

<span id="36948"></span>

<div id="answer-container-36948" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36948-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, I am not sure how much these short answers may help “beginners” but at least as kind of guidelines should show the complexity of the issue. Note also that OSM is not a map but data used for creating maps (after complex preparation processing).<br />
1. If you have a raster map you should detect the water colour code(s) from the stiles/decorations specification. Then, you should place your point(s) into the corresponding pixel(s) in the map and check the pixels colour code. If this is equal to the waters’ code, your point is in a water body. Of course, you may have many versions of this raster approach. As a rule, on large areas you need scales 1:4-5,000,000 or lower and the results are less accurate.<br />
2. In a vector version you should have a vector-area data layers for the planet_sea (or planet_land), rivers, lakes, channels… (or a layer for union of these). Besides, you should have a function point-in-polygon (that returns info whether a point is inside, on the border or outside a polygon). There are many versions of this function with varying efficiency (you may find versions even in student books). The best ones are those close to hardware and consist of just a several lines of code. How to use this function is rather strait forward. Again, a tiled version of the water area data layers may radically increase the efficiency of you search. This, because you may apply a simple early filtering.<br />
Here is an example, a case, similar to your issue for illustration. The river-line data contains roughly 250,000,000 (250 million) nodes. The river area objects around 53,000,000. Assume, you don’t want the river-line sections that are covered with the river areas (huge number of redundant points). If we run the search function for the nods on the large (none tiled) river objects it takes many, many hours on a powerful laptop. The same procedure on a tiled river objects takes only several (3-4) minutes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '14, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-36948" class="comments-container">
&#10;</div>
<div id="comment-tools-36948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36948-form-container" class="comment-form-container">
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

