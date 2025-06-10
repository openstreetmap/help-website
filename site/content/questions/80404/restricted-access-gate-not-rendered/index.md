+++
type = "question"
title = "Restricted access gate not rendered"
description = '''Hi folks This is probably a rather minor, even pedantic point but I do like to understand things! I put a gate in a fence to a recreation ground but OSM is just showing a gap in the fence. https://www.openstreetmap.org/#map=19/52.09148/-0.24885 - to the leftside parking area. The gate is for grounds...'''
date = "2021-06-03T17:49:00Z"
lastmod = "2021-06-03T19:28:00Z"
weight = 80404
keywords = [ "gate", "rendering" ]
aliases = [ "/questions/80404" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Restricted access gate not rendered](/questions/80404/restricted-access-gate-not-rendered)

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
<span id="post-80404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80404-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks This is probably a rather minor, even pedantic point but I do like to understand things! I put a gate in a fence to a recreation ground but OSM is just showing a gap in the fence. <a href="https://www.openstreetmap.org/#map=19/52.09148/-0.24885">https://www.openstreetmap.org/#map=19/52.09148/-0.24885</a> - to the leftside parking area. The gate is for grounds maintenance vehicles and so closed for public access. I marked it no access. In comparison, the gate does show as a thicker line on the following map which I think is a better representation <a href="https://map.atownsend.org.uk/maps/map/map.html#zoom=14&amp;lat=52.08781&amp;lon=-0.24703">https://map.atownsend.org.uk/maps/map/map.html#zoom=14&amp;lat=52.08781&amp;lon=-0.24703</a></p>
<p>Could someone please explain? Should I make any changes?</p>
<p>Upon re-reading my query, I apologise if it comes over as critical of OSM. I suppose I ought not to compare with other derived maps. Having said that, I still don't understand why the gate doesn't show at all when the related fence does.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '21, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/79aa23be5da724de729c2ccc899b7473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terry&#39;s gravatar image" />
<p><span>Terry</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terry has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '21, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-80404" class="comments-container">
&#10;</div>
<div id="comment-tools-80404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80404-form-container" class="comment-form-container">
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

<span id="80409"></span>

<div id="answer-container-80409" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80409-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terry has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue seems to be the mapping of the gate as a way rather than a node (compare the rendering of the gate on the right of the parking).</p>
<p>Mapping a gate as a way as you have done, while much less common than mapping as a node, is valid according to the wiki page for barrier=gate. And as the second map shows, at least some renderers interpret it in a meaningful way.</p>
<p>However it looks like the maintainers of the standard layer have decided not to render gates mapped as ways, see discussion at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3929">https://github.com/gravitystorm/openstreetmap-carto/issues/3929</a> and also at <a href="https://wiki.openstreetmap.org/wiki/Talk:Tag:barrier%3Dgate#Mapping_on_a_way_instead_of_a_node.3F">https://wiki.openstreetmap.org/wiki/Talk:Tag:barrier%3Dgate#Mapping_on_a_way_instead_of_a_node.3F</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '21, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '21, 19:23</strong> </span></p>
</div>
</div>
<div id="comments-container-80409" class="comments-container">
<span id="80410"></span>
<div id="comment-80410" class="comment">
<div id="post-80410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for replying. I've taken a look at the discussion links; some of the points went over my head - lol! I take your main point about different map renderings. I suppose I don't want to spend time adding things to OSM if they're not going to be seen. However, as you point out it's still useful for derived maps targetting particular users.</p>
</div>
<div id="comment-80410-info" class="comment-info">
<span class="comment-age">(03 Jun '21, 19:28)</span> <span class="comment-user userinfo">Terry</span>
</div>
</div>
</div>
<div id="comment-tools-80409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80409-form-container" class="comment-form-container">
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

