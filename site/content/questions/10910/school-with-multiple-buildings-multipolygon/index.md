+++
type = "question"
title = "School with multiple buildings: multipolygon?"
description = '''I am currently working on mapping a city school that has various buildings. The buildings are spread around a few streets and have other unrelated buildings (e.g. houses and shops) and public roads in between them, so I can&#x27;t just draw an area around the buildings and tag it. I have mapped out the b...'''
date = "2012-03-01T18:16:00Z"
lastmod = "2012-03-01T19:58:00Z"
weight = 10910
keywords = [ "building", "josm", "amenity", "role", "multipolygon" ]
aliases = [ "/questions/10910" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [School with multiple buildings: multipolygon?](/questions/10910/school-with-multiple-buildings-multipolygon)

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
<span id="post-10910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10910-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently working on mapping a city school that has various buildings. The buildings are spread around a few streets and have other unrelated buildings (e.g. houses and shops) and public roads in between them, so <strong>I can't just draw an area around the buildings and tag it</strong>. I have mapped out the buildings - sometimes using closed ways and sometimes using multipolygons for adjoining buildings - and tagged them as <em>building=school</em>. Some of these buildings have specific names e.g. Old Block, so I have tagged the closed way or multipolygon as, for example, <em>name=Old Block</em>.</p>
<p>Currently there is a node positioned at the school's reception to hold the <em>amenity=school</em>, address and website tags. However, this does not show exactly which buildings belong to this school, so I would like to use a multipolygon. (There is also another school nearby, with another set of buildings.)</p>
<p>I am using JOSM to edit. Should I create a new multipolygon for the entire school by selecting all the buildings (so that I have child multipolygons)? Or should I select all the outer ways for each set of adjoined buildings and use these to create a multipolygon? Or should I stick with what I have already?</p>
<p>If I go for a multipolygon approach, do I need to tag all the buildings with role=outer?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/96c2522da1dee70df309c3bf9d279ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greg&#39;s gravatar image" />
<p><span>Greg</span><br />
<span class="score" title="141 reputation points">141</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greg has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-10910" class="comments-container">
&#10;</div>
<div id="comment-tools-10910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10910-form-container" class="comment-form-container">
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

<span id="10912"></span>

<div id="answer-container-10912" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10912-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Greg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check this widely used relation type "site":<br />
<a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site">https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site</a></p>
<p>instead of nesting multipolygons relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '12, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-10912" class="comments-container">
<span id="10925"></span>
<div id="comment-10925" class="comment">
<div id="post-10925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems to be a good solution. I will edit the wiki page for amenity=school as I wasn't aware that this relation type existed. Thanks.</p>
</div>
<div id="comment-10925-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 19:54)</span> <span class="comment-user userinfo">Greg</span>
</div>
</div>
</div>
<div id="comment-tools-10912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10912-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10923"></span>

<div id="answer-container-10923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use amenity=school like you would a land use, encompassing the entire campus.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '12, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-10923" class="comments-container">
<span id="10924"></span>
<div id="comment-10924" class="comment">
<div id="post-10924-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The campus is spread around so there are a number of other buildings in between which are not part of the campus. I don't really want to map the whole area as a school when it is just part of the city with school buildings in amongst others.</p>
</div>
<div id="comment-10924-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 19:53)</span> <span class="comment-user userinfo">Greg</span>
</div>
</div>
<span id="10927"></span>
<div id="comment-10927" class="comment">
<div id="post-10927-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So, it seems like you can manage that landuse of the school by creating a multipolygon for the amenity area, with the donut holes as inner. This would limit areas inside the whole that are not "on campus" as not being part of the school.</p>
</div>
<div id="comment-10927-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 19:58)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-10923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10923-form-container" class="comment-form-container">
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

