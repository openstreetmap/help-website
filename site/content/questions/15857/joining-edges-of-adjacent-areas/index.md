+++
type = "question"
title = "Joining Edges of Adjacent Areas"
description = '''Let me give two personal examples, and then I&#x27;ll ask my question: 1) I was trying to correct the border of large park area but ran into a ton of problems because most of the points (nodes?) in that section were joined to that of a street, which was also joined together with the border of a jurisdict...'''
date = "2012-09-06T19:10:00Z"
lastmod = "2012-09-06T22:55:00Z"
weight = 15857
keywords = [ "boundaries", "join", "border", "area" ]
aliases = [ "/questions/15857" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Joining Edges of Adjacent Areas](/questions/15857/joining-edges-of-adjacent-areas)

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
<span id="post-15857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15857-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let me give two personal examples, and then I'll ask my question:</p>
<p>1) I was trying to correct the border of large park area but ran into a ton of problems because most of the points (nodes?) in that section were joined to that of a street, which was also joined together with the border of a jurisdiction. It wasn't possible to simply adjust the park boundary without incorrectly changing the street or the jurisdiction border too. I was able to accomplish my goal by using the scissors tool to unlink the items, which became very tricky to separate what I wanted but leave the other two joined.</p>
<p>2) I want to adjust the boundaries of an airport apron. Right now the apron encircles the entire airport terminal, which is kind of ridiculous since planes can't taxi through the gift shop. So I may opt to correct the shape to go loosely around the terminal, but another (more precise) method could be to retrace the entire airport terminal (building) border whereas I would join all those points (nodes?). That would be nice and precise but I really worry about the situation I described above, in that it would be a nightmare if for some reason anybody ever needed to separate the two.</p>
<p>So my question is this: What is the recommended standard procedure for properly "drawing" two or more adjacent areas? Should they share the same points so they fit nice and snuggly, or should they remain independent (even if the nodes overlap)? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-join" rel="tag" title="see questions tagged &#39;join&#39;">join</span> <span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '12, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/228a09e620f374c61a25e546d76bc6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopanthers&#39;s gravatar image" />
<p><span>gopanthers</span><br />
<span class="score" title="366 reputation points">366</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopanthers has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '12, 19:52</strong> </span></p>
</div>
</div>
<div id="comments-container-15857" class="comments-container">
&#10;</div>
<div id="comment-tools-15857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15857-form-container" class="comment-form-container">
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

<span id="15860"></span>

<div id="answer-container-15860" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15860-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Potlatch 2, if a node is shared by several ways, you can separate it into a separate node for each way, by selecting the node and pressing 'shift-J'. You can then select the way that you want to change, and move the node for just that way.</p>
<p>If a node is shared by more than two ways, and you want to edit only one of the ways, you can separate the shared node into one node for each way using 'shift-J', move the node in one of the ways, and then select one of the unmoved nodes and press 'J' to re-combine them.</p>
<p>So one possible answer is: If the same nodes define two ways (e.g. if a stream forms the boundary of a wood, or a road forms the boundary of a residential area), use shared nodes. If two ways just happen to run very close to each other, use different nodes for the two ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '12, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15860" class="comments-container">
&#10;</div>
<div id="comment-tools-15860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15870"></span>

<div id="answer-container-15870" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15870-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the case of the airport apron, a cleaner option is to use a <a href="https://wiki.openstreetmap.org/wiki/Multipolygon">multypolygon relation</a>. Leave the builing ways as-is, but remove the tags fron the apron way (except maybe source=Bing for example) and put them in a relation. So that you do not have extra ways, yet the data is semantically correct.</p>
<p>If two nodes are conceptually at the same location, then they should be a single node. Having "overlaping nodes" is dirty and unnecessary. Overlaping ways are more subjective : They are arguably dirty too but they can be oh-so-pratical. Using relations for the same purpose often sound like too much work. I use relations for complicated stuff, and overlaping ways for simpler ones. YMMV.</p>
<p>In any case, overlaps/relations should only be used if the real-life objects actually "touch". A forest alongside a lake or an administrative boundary following a road/river are good examples, but a park alongside a road most certainly isn't (unless the road is mapped as an area). Said differently, only glue ways together if they are both areas/2D or both lines/1D, but not if you have a mix.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '12, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '12, 23:05</strong> </span></p>
</div>
</div>
<div id="comments-container-15870" class="comments-container">
&#10;</div>
<div id="comment-tools-15870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15870-form-container" class="comment-form-container">
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

