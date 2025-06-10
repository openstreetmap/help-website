+++
type = "question"
title = "Buildings in route relation"
description = '''Religiour routea typically contain wayside crosses as &quot;stops&quot; on the route. That is ok until the wayside cross is not a small chaple marked like a building rather than a point. See for example https://www.openstreetmap.org/relation/1571254 Than the question is - what is the best way to include these...'''
date = "2018-11-30T02:56:00Z"
lastmod = "2018-11-30T16:33:00Z"
weight = 66994
keywords = [ "routes" ]
aliases = [ "/questions/66994" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Buildings in route relation](/questions/66994/buildings-in-route-relation)

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
<span id="post-66994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Religiour routea typically contain wayside crosses as "stops" on the route. That is ok until the wayside cross is not a small chaple marked like a building rather than a point. See for example</p>
<p><a href="https://www.openstreetmap.org/relation/1571254">https://www.openstreetmap.org/relation/1571254</a></p>
<p>Than the question is - what is the best way to include these buildings (as stops) in the relation. Just including them may be confusing, because any "way" included in route relation is considered currently part of the route itself.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '18, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e6dd88ec54643689069f97f0d52398ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorn&#39;s gravatar image" />
<p><span>gorn</span><br />
<span class="score" title="542 reputation points">542</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorn has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '18, 12:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-66994" class="comments-container">
&#10;</div>
<div id="comment-tools-66994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66994-form-container" class="comment-form-container">
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

<span id="67003"></span>

<div id="answer-container-67003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67003-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is simply a tagging issue, relation members can have "roles" in this case useful values might be "halt" or "infrastructure" data consumers should not do anything with values/roles they don't understand so this in principle should be safe.</p>
<p>Unluckily JOSM suggests adding such values without a role, something that is clearly defective.</p>
<p>Now the other part of the equation is getting data consumers to actually do something reasonable with the members with such role values. The best way to achieve that is to get buy in to whatever role values you are proposing on the <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging mailing list</a> and by documenting the role values you propose to use in the <a href="https://wiki.openstreetmap.org/">wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '18, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-67003" class="comments-container">
<span id="67011"></span>
<div id="comment-67011" class="comment">
<div id="post-67011-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would be great if it is like you write it, however I beleive that the empty role is a part the specification - see <a href="https://wiki.openstreetmap.org/wiki/Relation:route">https://wiki.openstreetmap.org/wiki/Relation:route</a></p>
</div>
<div id="comment-67011-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 16:19)</span> <span class="comment-user userinfo">gorn</span>
</div>
</div>
<span id="67012"></span>
<div id="comment-67012" class="comment">
<div id="post-67012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The empty role is for the ways that make up the route according to the specification, not for anything else.</p>
</div>
<div id="comment-67012-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 16:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67003-form-container" class="comment-form-container">
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

