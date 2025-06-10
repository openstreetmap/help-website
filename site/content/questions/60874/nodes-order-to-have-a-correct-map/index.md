+++
type = "question"
title = "nodes order to have a correct map"
description = '''i&#x27;ve import some osm data in my db with bulkDB.pl When i do a query i find a relation, then i find the ways in the relation and then i find nodes in the ways. For each nodes i get coordinates and with mapbox i try to make a map. It seems that the order of my nodes is incorrect. Which is the correct ...'''
date = "2017-11-29T15:24:00Z"
lastmod = "2017-11-29T16:01:00Z"
weight = 60874
keywords = [ "ways", "nodes", "order", "relations" ]
aliases = [ "/questions/60874" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nodes order to have a correct map](/questions/60874/nodes-order-to-have-a-correct-map)

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
<span id="post-60874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i've import some osm data in my db with bulkDB.pl When i do a query i find a relation, then i find the ways in the relation and then i find nodes in the ways. For each nodes i get coordinates and with mapbox i try to make a map. It seems that the order of my nodes is incorrect. Which is the correct order of the nodes to have a layer with a correct line?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '17, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ed98b20e9026f11453357af620ce686f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maurizio%20Proietti&#39;s gravatar image" />
<p><span>Maurizio Pro...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maurizio Proietti has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60874" class="comments-container">
&#10;</div>
<div id="comment-tools-60874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60874-form-container" class="comment-form-container">
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

<span id="60875"></span>

<div id="answer-container-60875" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60875-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not familiar with bulkDB.pl - Are you talking about this collection of scripts? <a href="http://wiki.openstreetmap.org/wiki/OsmDB.pm">http://wiki.openstreetmap.org/wiki/OsmDB.pm</a></p>
<p>If so, it looks like there is a table named <code>waynodes</code> which maps nodes to ways. The second column in this table (named "s" which is not very descriptive) indicates the order of the nodes in the way, starting at 0. So whatever query you are using to get the nodes out of the database needs to somehow include a <code>sort by s</code> clause in it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '17, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-60875" class="comments-container">
&#10;</div>
<div id="comment-tools-60875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60875-form-container" class="comment-form-container">
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

