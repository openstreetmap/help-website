+++
type = "question"
title = "How to correctly mark the Independent Cities of Virginia?"
description = '''I would like to use the data from Open Street Map to identify which county I am in, but I noticed something unusual with the Independent Cities of Virginia. Essentially, there are a few cities that are independent of counties, even if they are completely contained within a county. When I do a query ...'''
date = "2013-11-14T17:50:00Z"
lastmod = "2014-12-05T11:20:00Z"
weight = 28110
keywords = [ "county", "admin_boundary", "virginia" ]
aliases = [ "/questions/28110" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to correctly mark the Independent Cities of Virginia?](/questions/28110/how-to-correctly-mark-the-independent-cities-of-virginia)

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
<span id="post-28110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28110-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to use the data from Open Street Map to identify which county I am in, but I noticed something unusual with the Independent Cities of Virginia. Essentially, there are a few cities that are independent of counties, even if they are completely contained within a county. When I do a query (Via the Map Quest Geocoding API), it returns that I am in the surrounding county, and not the city. For instance, here is Augusta County, which contains two independent cities, Staunton and Waynesboro. I've seen this for a half dozen other independent cities, BTW.</p>
<p><img src="http://i.stack.imgur.com/G4Vni.png" alt="enter image description here" /></p>
<p>It's a bit tricky to see, but Staunton has a county boundary approximating the city boundaries. When I call Staunton, it correctly shows Staunton City as the county. When I look at Waynesboro, it stays it is in Augusta, not Waynesboro City. What I'm trying to do is to figure out how to make the appropriate correction. I can see a couple of possibilities, including:</p>
<ol>
<li>Somehow trace an interior boundary that matches the city of Waynesboro, and identify that county as Waynesboro City.</li>
<li>Somehow make the existing Waynesboro think it's a county.</li>
</ol>
<p>I'm not quite sure how either of those could be done, or which is the best, or even if there's a better solution all together. How can I make this correction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-county" rel="tag" title="see questions tagged &#39;county&#39;">county</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-virginia" rel="tag" title="see questions tagged &#39;virginia&#39;">virginia</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '13, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ada90dc82e9546879ac95847117d1a3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kd7uiy&#39;s gravatar image" />
<p><span>kd7uiy</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kd7uiy has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '13, 18:52</strong> </span></p>
</div>
</div>
<div id="comments-container-28110" class="comments-container">
<span id="28112"></span>
<div id="comment-28112" class="comment">
<div id="post-28112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already tried to help him <a href="http://gis.stackexchange.com/questions/77447/how-to-correctly-set-the-independent-cities-of-virginia-in-open-street-map">here</a> but I'm not sure about the correct solution.</p>
</div>
<div id="comment-28112-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 19:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28110-form-container" class="comment-form-container">
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

<span id="28641"></span>

<div id="answer-container-28641" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28641-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kd7uiy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A couple parts to make this happen: one, adjust the administrative level of Waynesboro to be county-equivalent. That is, for the boundary=administrative that is around Waynesboro, set it to admin_level=6. Then, select all of the ways that make up the relation that is the boundary of Waynesboro (they will all be in role "outer" for this one) and add them to the relation that is the boundary of Augusta County (and they will be in the role "inner" for this one).</p>
<p>I'll assume you know enough about OSM editors to do the first thing. Editing relations is a little trickier; here's a quick runthrough for Potlatch2: first, find the relation number for Augusta County. Do this by (in Potlatch2) clicking on some part of the boundary, click "Advanced", and then double-click the relations it's in until you find the one for Augusta County. Write down the ID of this relation. Then, click on some part of the Waynesboro boundary, click the downward arrow and "select all members" of the Waynesboro boundary relation. Click "Add to", and in the ensuing popup, select the relation for Augusta County. After it's added, make sure to designed the Role as "inner" for the ways that you've just added.</p>
<p>Hope this helps!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '13, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-28641" class="comments-container">
<span id="28724"></span>
<div id="comment-28724" class="comment">
<div id="post-28724-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This did the trick! Truth be told, Stauton isn't set up either. I'm going to have to check all of the Independent Cities in Virginia carefully, but I think this will do the trick!</p>
</div>
<div id="comment-28724-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 16:29)</span> <span class="comment-user userinfo">kd7uiy</span>
</div>
</div>
<span id="39071"></span>
<div id="comment-39071" class="comment">
<div id="post-39071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For independent cities, should they have both an admin_level 8 and admin_level 6 boundary, or just the admin_level 6? St. Louis currently has both.</p>
</div>
<div id="comment-39071-info" class="comment-info">
<span class="comment-age">(05 Dec '14, 11:20)</span> <span class="comment-user userinfo">brianegge</span>
</div>
</div>
</div>
<div id="comment-tools-28641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28111"></span>

<div id="answer-container-28111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28111-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So the city is a hole in the county? This is the same type of thing as a building with an atrium or empty space in the middle and can be described using a multi-polygon.</p>
<p>And, in general administrative boundaries should be multi-polygons already. If the county in question isn't then make it one with the boundary ways having a role of outer.</p>
<p>Then add the city boundary to the county as a "inner". That will punch a hole out of the county so things in the city are not also in the county.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '13, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '13, 18:51</strong> </span></p>
</div>
</div>
<div id="comments-container-28111" class="comments-container">
<span id="28603"></span>
<div id="comment-28603" class="comment">
<div id="post-28603-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While I understand the general concept of the answer to this question, I would appreciate more details as to how to make such things happen.</p>
</div>
<div id="comment-28603-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 14:17)</span> <span class="comment-user userinfo">kd7uiy</span>
</div>
</div>
</div>
<div id="comment-tools-28111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28111-form-container" class="comment-form-container">
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

