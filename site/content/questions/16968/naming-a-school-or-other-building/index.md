+++
type = "question"
title = "Naming a school (or other building)"
description = '''I recently added a school to OSM (via Potlatch2). I outlined the school property and named it &quot;XYZ Elementary School&quot;. I outlined the school building and named it &quot;XYZ Elementary School&quot;. I outlined a 2nd school building (the gym) and named it &quot;XYZ Elementary School&quot;. And finally I know that there i...'''
date = "2012-10-17T19:10:00Z"
lastmod = "2015-03-11T11:48:00Z"
weight = 16968
keywords = [ "school", "name" ]
aliases = [ "/questions/16968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Naming a school (or other building)](/questions/16968/naming-a-school-or-other-building)

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
<span id="post-16968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16968-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added a school to OSM (via Potlatch2). I outlined the school property and named it "XYZ Elementary School". I outlined the school building and named it "XYZ Elementary School". I outlined a 2nd school building (the gym) and named it "XYZ Elementary School". And finally I know that there is a single point (a node?) for a school that I also added on the center of the building and named it "XYZ Elementary School" too. None of these were wrong to name, but at different zoom levels I got a whole bunch of overlapping text of the exact same redundant name.</p>
<p>Now I know I can easily remove the name from the school gym building and I can also remove that single point school designation (a node?), but that still leaves both the building and the property with the same exact name. My question is mostly that of best practices:</p>
<ul>
<li>Is it a problem to redundantly name both the property and the building? To me they are both valid and should be labeled.</li>
<li>Should one add a single point identifier (like that school node) to a building if the building itself is drawn out?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '12, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/228a09e620f374c61a25e546d76bc6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopanthers&#39;s gravatar image" />
<p><span>gopanthers</span><br />
<span class="score" title="366 reputation points">366</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopanthers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16968" class="comments-container">
&#10;</div>
<div id="comment-tools-16968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16968-form-container" class="comment-form-container">
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

<span id="16970"></span>

<div id="answer-container-16970" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16970-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-16970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gopanthers has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The usual practice is <a href="http://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one feature, one OSM element</a>.</p>
<p>In your specific case you should add an <em>area</em> outlining the whole school territory and add <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">amenity=school</a>, <em>name=</em>, <em><a href="http://wiki.openstreetmap.org/wiki/Key:addr">addr</a></em> and whatever you like. Tag each single building with <a href="http://wiki.openstreetmap.org/wiki/Key:building">building=school</a> (<em>building=yes</em> would also suffice) and remove the single school <em>node</em> as there is absolutely no need for it (see my first sentence).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16970" class="comments-container">
<span id="16984"></span>
<div id="comment-16984" class="comment">
<div id="post-16984-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is also a graphical example on the amenity=school page scai links above.</p>
</div>
<div id="comment-16984-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 21:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="41637"></span>
<div id="comment-41637" class="comment">
<div id="post-41637-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that streets are one notable exception to the "one feature, one element" rule. One street often consists of multiple OSM ways, which have the same <code>name=</code> tag. However, this usage is probably for historic reasons.</p>
</div>
<div id="comment-41637-info" class="comment-info">
<span class="comment-age">(11 Mar '15, 11:48)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-16970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16970-form-container" class="comment-form-container">
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

