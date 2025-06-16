+++
type = "question"
title = "Can an inner relation be used to &#x27;remove&#x27; 1 tag?"
description = '''There&#x27;s a park that&#x27;s also a forest. I tagged the area with both Leisure:Park &amp;amp; Landuse:Forest. However, there&#x27;s a smaller section within the park that isn&#x27;t forested. How do I use a relation polygon to disable just the Landuse:Forest tag for that area? And if that can&#x27;t be done with relations, ...'''
date = "2018-11-13T12:59:00Z"
lastmod = "2018-11-21T20:00:00Z"
weight = 66762
keywords = [ "relations", "beginner", "tagging" ]
aliases = [ "/questions/66762" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can an inner relation be used to 'remove' 1 tag?](/questions/66762/can-an-inner-relation-be-used-to-remove-1-tag)

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
<span id="post-66762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's a park that's also a forest. I tagged the area with both Leisure:Park &amp; Landuse:Forest. However, there's a smaller section within the park that isn't forested. How do I use a relation polygon to disable just the Landuse:Forest tag for that area? And if that can't be done with relations, what is the recommended way to do it?</p>
<p>This is the polygon I'm having trouble with (I think I may have done it wrong):<br />
<a href="https://www.openstreetmap.org/way/643748249">https://www.openstreetmap.org/way/643748249</a></p>
<p>Visual explanation:<br />
<img src="https://i.imgur.com/hUs73xl.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '18, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f94d0f3a61f5eaade1b0fc4269dacb0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cambroulet&#39;s gravatar image" />
<p><span>Cambroulet</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cambroulet has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '18, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-66762" class="comments-container">
&#10;</div>
<div id="comment-tools-66762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66762-form-container" class="comment-form-container">
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

<span id="66763"></span>

<div id="answer-container-66763" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66763-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cambroulet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems like a legitimate solution in this case. Now you just need to move park tag for the whole area (not for multipolygon):</p>
<p><a href="https://www.openstreetmap.org/way/84689580">https://www.openstreetmap.org/way/84689580</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '18, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-66763" class="comments-container">
<span id="66765"></span>
<div id="comment-66765" class="comment">
<div id="post-66765-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think what you're saying here is that the outer way should have the leisure and name tags as they apply to the whole area, then the multipolygon relation have only the landuse and type tags (but the same outer and inner members) as it is only the forest that has the hole. If so I'd agree.</p>
</div>
<div id="comment-66765-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 16:19)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="66766"></span>
<div id="comment-66766" class="comment">
<div id="post-66766-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, this is what I meant.</p>
</div>
<div id="comment-66766-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 16:21)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="66768"></span>
<div id="comment-66768" class="comment">
<div id="post-66768-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Concur that the park tag can go on the outer way and that a multipolygon with an inner will exclude the area without trees.</p>
<p>However I am in the camp that landuse=forest implies trees grown for producing wood products which seems unlikely for a park. I usually double tag with natural=wood and my preferred (but not supported by the renderer at www.openstreetmap.org) landcover=trees. See, among other parts of the wiki <a href="https://wiki.openstreetmap.org/wiki/Forest">https://wiki.openstreetmap.org/wiki/Forest</a> I prefer landcover as I can see there are trees but don't know if they are there "naturally" or if they are being managed for harvesting for wood products.</p>
</div>
<div id="comment-66768-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 17:16)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="66884"></span>
<div id="comment-66884" class="comment">
<div id="post-66884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Disregard my previous message in case it's in your inbox - I've figured it out. I figured out how to follow your directions and have accomplished what I wanted to do. My misunderstanding was that I wasn't aware that the outer way and multipolygon relation were separate things that can have attributes tagged to them individually.</p>
</div>
<div id="comment-66884-info" class="comment-info">
<span class="comment-age">(21 Nov '18, 20:00)</span> <span class="comment-user userinfo">Cambroulet</span>
</div>
</div>
</div>
<div id="comment-tools-66763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66763-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66767"></span>

<div id="answer-container-66767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66767-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you have there are really two areas:</p>
<ul>
<li>A park, which is named "Alice Park". This is tagged <code>leisure=park + name=Alice Park</code>.</li>
<li>A forest. This is tagged <code>landuse=forest</code>. It covers most of the park.</li>
</ul>
<p>So you <strong>draw a park</strong>:</p>
<p><img src="/upfiles/park.png" alt="Closed polygon representing a park" /></p>
<p>This only requires a closed way that carries the park's tags, i.e. <code>leisure=park + name=Alice Park</code>.</p>
<p>And you <strong>draw a forest</strong>:</p>
<p><img src="/upfiles/forest.png" alt="Polygon with a hole, representing a forest" /></p>
<p>Because it has a hole, we need to use a multipolygon relation. So it consists of two closed ways (the outer ring and the inner ring), plus the relation that holds them together and gives them meaning. The forest's tags (i.e. <code>landuse=forest</code>) go onto the relation, and – like all multipolygon relations – it also gets a <code>type=multipolygon</code> tag.</p>
<p><strong>That's it.</strong></p>
<p>There's one more thing that may be causing confusion here, though: The way we've drawn for the park, and the way we've drawn as the outer ring of the forest, have the exact same shape. This isn't necessarily always the case, as you could easily imagine a park where there's some grassy area without trees at the edge. But in our example, it is.</p>
<p>So to save effort while creating and maintaining this kind of data, mappers will usually choose to re-use the park way as the outer ring of the multipolygon relation instead of drawing a second way with the same shape. Doing that is allowed and common practice. But note that this does <em>not</em> have any special meaning compared to creating a second way. It's purely for convenience.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '18, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '18, 17:12</strong> </span></p>
</div>
</div>
<div id="comments-container-66767" class="comments-container">
&#10;</div>
<div id="comment-tools-66767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66767-form-container" class="comment-form-container">
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

