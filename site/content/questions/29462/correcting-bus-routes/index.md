+++
type = "question"
title = "Correcting Bus Routes"
description = '''I am very much a newbie so probably I am doing something stupid... I have successfully edited a few roads and footpaths on the Standard layer, both additions and minor re-alignments. However I have not been able to edit Bus Routes on the Transport layer, using iD, Potlatch 2 or JOSM. Is the Transpor...'''
date = "2013-12-30T15:56:00Z"
lastmod = "2013-12-30T18:11:00Z"
weight = 29462
keywords = [ "layer", "public-transport", "transport" ]
aliases = [ "/questions/29462" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Correcting Bus Routes](/questions/29462/correcting-bus-routes)

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
<span id="post-29462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29462-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am very much a newbie so probably I am doing something stupid... I have successfully edited a few roads and footpaths on the Standard layer, both additions and minor re-alignments. However I have not been able to edit Bus Routes on the Transport layer, using iD, Potlatch 2 or JOSM. Is the Transport layer 'closed', or am I just not selecting it correctly? I have found a couple of errors on my local Bus Routes which definitely should be corrected - if ordinary users cannot do this is there a way of pointing out errors to the 'person in charge'. Cheers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-transport" rel="tag" title="see questions tagged &#39;transport&#39;">transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '13, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ecf5bb01d3c28b5df1ce3fb190023a2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cageywoolf&#39;s gravatar image" />
<p><span>cageywoolf</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cageywoolf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29462" class="comments-container">
&#10;</div>
<div id="comment-tools-29462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29462-form-container" class="comment-form-container">
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

<span id="29464"></span>

<div id="answer-container-29464" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29464-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cageywoolf has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bus Routes are generally relations, which are more complex in OSM. I would recommend you not try to edit them in iD as it's more difficult. You may find it easier to view (and edit) routes in Potlatch 2. (can't speak for JOSM, personally, sorry) In P2, you can select a way that's in a route relation (it'll probably have a blue outline), then it should display the routes in the sidebar. You can double click on one to view the relation, and switch to the Advanced view (scroll to the bottom) to see all the tags.</p>
<p>To modify a route, conceptually, you add a way to a given route and optionally give it a role. See the <a href="https://wiki.openstreetmap.org/wiki/Route_relation">Route Relation</a> wiki page for details. Of course, you can remove a route from a way too.</p>
<p>The other thing to remember is that the Transport map may not be updated as quickly as the other maps, so your changes may not be displayed right away. If you view a relation by ID, however (ie <a href="https://www.openstreetmap.org/relation/1878715">https://www.openstreetmap.org/relation/1878715</a>) it should be updated pretty instantly, however.</p>
<p>One other option would be to add a Note on the OSM.org site, and hope that someone comes along to make the change for you, but I urge you to go for it! :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '13, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-29464" class="comments-container">
<span id="29472"></span>
<div id="comment-29472" class="comment">
<div id="post-29472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. It's the Route Relation that I missed out on. I shall give it a go and see if I can master it. Thanks again.</p>
</div>
<div id="comment-29472-info" class="comment-info">
<span class="comment-age">(30 Dec '13, 18:11)</span> <span class="comment-user userinfo">cageywoolf</span>
</div>
</div>
</div>
<div id="comment-tools-29464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29464-form-container" class="comment-form-container">
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

