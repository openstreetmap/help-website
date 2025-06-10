+++
type = "question"
title = "How to tag multipolygon building to render as place_of_worship?"
description = '''I&#x27;ve created a place of worship relation, comprised of 4 ways - 2 containing building=church and 2 containing building=roof tags only. The relation contains name of church, address, etc. All for ways are physically touching at least one of the others. Is this the correct way to collect this object? ...'''
date = "2018-11-30T19:14:00Z"
lastmod = "2018-12-02T12:17:00Z"
weight = 67016
keywords = [ "building", "relation" ]
aliases = [ "/questions/67016" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag multipolygon building to render as place_of_worship?](/questions/67016/how-to-tag-multipolygon-building-to-render-as-place_of_worship)

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
<span id="post-67016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67016-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've created a place of worship relation, comprised of 4 ways - 2 containing building=church and 2 containing building=roof tags only. The relation contains name of church, address, etc. All for ways are physically touching at least one of the others. Is this the correct way to collect this object?</p>
<p>If so, how can I get the whole building footprint to render as a place of worship? Currently it only renders as a building. Should I add place of worship tags to each way? This seems redundant.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '18, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/95ff57b6d571cffa00600d67c0e0b81b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wcwalker&#39;s gravatar image" />
<p><span>wcwalker</span><br />
<span class="score" title="81 reputation points">81</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wcwalker has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '18, 19:30</strong> </span></p>
</div>
</div>
<div id="comments-container-67016" class="comments-container">
<span id="67021"></span>
<div id="comment-67021" class="comment">
<div id="post-67021-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You've come upon one of the big problems in OSM and that is, how do I make my object show up in a map display? It sounds like you did everything correctly when you created the relation but a major principle of OSM is that one must not fiddle with things just to make them render. Definitely, do not add place of worship tags to every way.</p>
<p>Certain relations and multipolygons simply don't yet render properly on OSM. Mappers have tried all sorts of tricks over the years, like adding tags to every way in a relation, to force the rendering to agree with what they want to see but this is a bad habit.</p>
<p>You might also provide a reference or ID for your church relation so others can have a look.</p>
</div>
<div id="comment-67021-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 02:09)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-67016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67016-form-container" class="comment-form-container">
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

<span id="67027"></span>

<div id="answer-container-67027" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67027-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the 'building' ways are touching because they are actually part of the same building then you may want to consider tagging them using <a href="https://wiki.openstreetmap.org/wiki/Key:building:part">building:part=* tags</a> and adding another way for the outline as a whole with the relevant tags.</p>
<p>Ignore me if they are actually separate buildings that touch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '18, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-67027" class="comments-container">
&#10;</div>
<div id="comment-tools-67027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67027-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67039"></span>

<div id="answer-container-67039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67039-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure from your question if you have used the amenity=place_of_worship tag on the relation.</p>
<p>Example of a multipolygon with amenity=place_of_worship tag, which does appear to render in the standard map style: <a href="https://www.openstreetmap.org/relation/1110358">https://www.openstreetmap.org/relation/1110358</a></p>
<p>As AlaskaDave said it would be useful if you could provide a link to the object that is giving you problems.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '18, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-67039" class="comments-container">
&#10;</div>
<div id="comment-tools-67039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67039-form-container" class="comment-form-container">
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

