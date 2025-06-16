+++
type = "question"
title = "Display of amenity symbol for buildings"
description = '''When using keepright to check for errors, I notice that there are quite a few entries of the type, &quot;This node has tags in common with the surrounding way&quot; in my locality. These appear to typically be schools or other amenities with both a polygon tagged as a school and a single node also tagged as a...'''
date = "2012-10-24T21:35:00Z"
lastmod = "2012-10-25T02:44:00Z"
weight = 17168
keywords = [ "node", "amenity", "tag", "polygon" ]
aliases = [ "/questions/17168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display of amenity symbol for buildings](/questions/17168/display-of-amenity-symbol-for-buildings)

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
<span id="post-17168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using keepright to check for errors, I notice that there are quite a few entries of the type, "This node has tags in common with the surrounding way" in my locality. These appear to typically be schools or other amenities with both a polygon tagged as a school and a single node also tagged as a school. If the single node is removed, the school symbol is no longer displayed. Is there a way to get both the outline and the symbol rendered without having duplicate information?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '12, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d78e2fca033a03b6bae93d35a7934ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Baggaley&#39;s gravatar image" />
<p><span>Mike Baggaley</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Baggaley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17168" class="comments-container">
&#10;</div>
<div id="comment-tools-17168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17168-form-container" class="comment-form-container">
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

<span id="17173"></span>

<div id="answer-container-17173" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17173-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-17173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is wrong to have both the area way <em>and</em> central node. If you see this, then generally the <strong>correct thing to do is delete the central node</strong>. <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">One feature, one OSM element</a>.</p>
<p>I tend to draw in a large area encompassing the building or buildings, and car parks and sports pitches. The amenity=school tag goes on this encompassing area. Something like this illustration from the <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">amenity=school docs</a></p>
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/6/6d/Amenity_school_usage_example.svg/375px-Amenity_school_usage_example.svg.png" alt="alt text" /></p>
<p>But you were asking about the symbols.</p>
<p>In the "standard" OpenStreetMap map rendering, the map doesn't currently display a school symbol regardless of whether the school is mapped as a node or an area. So I guess you mean in the Potlatch editor the symbol is no longer displayed, or maybe in JOSM. They both do this actually.</p>
<p>None of this is a problem though. You're not doing it wrong if you don't see the school symbol.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '12, 02:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</img>
</div>
</div>
<div id="comments-container-17173" class="comments-container">
&#10;</div>
<div id="comment-tools-17173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17173-form-container" class="comment-form-container">
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

