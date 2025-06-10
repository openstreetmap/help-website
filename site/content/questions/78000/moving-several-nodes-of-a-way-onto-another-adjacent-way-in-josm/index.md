+++
type = "question"
title = "Moving several nodes of a way onto another adjacent way in JOSM"
description = '''I am having trouble finding a way on how to move several nodes of a way onto another way or polygon. I am able to achieve this in JOSM using Tools &amp;gt; Move Node onto Way, but the tool seems to work only for single nodes. In the image below, I want to move the nodes of the forest (within the red out...'''
date = "2020-12-19T08:06:00Z"
lastmod = "2020-12-31T14:26:00Z"
weight = 78000
keywords = [ "ways", "josm", "nodes", "move" ]
aliases = [ "/questions/78000" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Moving several nodes of a way onto another adjacent way in JOSM](/questions/78000/moving-several-nodes-of-a-way-onto-another-adjacent-way-in-josm)

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
<span id="post-78000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78000-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am having trouble finding a way on how to move several nodes of a way onto another way or polygon. I am able to achieve this in JOSM using Tools &gt; Move Node onto Way, but the tool seems to work only for single nodes. In the image below, I want to move the nodes of the forest (within the red outline) onto the road so that the forest nodes are exactly aligned with or are on top of the road nodes:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_at_2020-12-19_15-38-27.png" alt="JOSM nodes of two ways before" /></p>
<p>The following is what I want to achieve:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_at_2020-12-19_15-51-08.png" alt="JOSM nodes of two ways after" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-move" rel="tag" title="see questions tagged &#39;move&#39;">move</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '20, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-78000" class="comments-container">
<span id="78008"></span>
<div id="comment-78008" class="comment">
<div id="post-78008-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>In the case of areas to landuse/natural areas to roads: please do not do this.</p>
<p>It is both less accurate mapping and a pain for subsequent editors.</p>
</div>
<div id="comment-78008-info" class="comment-info">
<span class="comment-age">(19 Dec '20, 14:21)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="78010"></span>
<div id="comment-78010" class="comment">
<div id="post-78010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you to all for the enlightenment. Can you please suggest on how to select those (forest) nodes in bulk (I tried Shift+Click to select multiple nodes at once but in JOSM this acts like CTRL+Shift instead as it selects only single nodes) and move these nodes out of the road in bulk?</p>
</div>
<div id="comment-78010-info" class="comment-info">
<span class="comment-age">(19 Dec '20, 20:06)</span> <span class="comment-user userinfo">JAT86</span>
</div>
</div>
<span id="78012"></span>
<div id="comment-78012" class="comment">
<div id="post-78012-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would use the lasso select in JOSM to select a group of nodes that need shifting, then shift+select the forest way they belong to, then Tools&gt;Unglue Ways, then hover over one of the selected nodes, left click+drag that group of selected nodes to a more correct position.<br />
I find it works best to select groups of nodes that are aligned horizontally or vertically or diagonally and do each axis separately.<br />
It takes time and is a frustrating task to correct the mess if large.<br />
-using Mac</p>
</div>
<div id="comment-78012-info" class="comment-info">
<span class="comment-age">(20 Dec '20, 03:19)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="78046"></span>
<div id="comment-78046" class="comment">
<div id="post-78046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for the very helpful information.</p>
</div>
<div id="comment-78046-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 17:28)</span> <span class="comment-user userinfo">JAT86</span>
</div>
</div>
<span id="78059"></span>
<div id="comment-78059" class="comment">
<div id="post-78059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Potlatch 2 as a parallel line tool in the tool box, bottom right symbol looks like a domino six.</p>
</div>
<div id="comment-78059-info" class="comment-info">
<span class="comment-age">(22 Dec '20, 22:18)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="78165"></span>
<div id="comment-78165" class="comment not_top_scorer">
<div id="post-78165-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ul>
<li>For selecting way nodes, see the plugin <a href="https://josm.openstreetmap.de/wiki/Help/Plugin/UtilsPlugin2#Selection">utilsplugin2</a>.</li>
<li>For mapping in more details there is the <a href="https://josm.openstreetmap.de/wiki/Help/Action/ImproveWayAccuracy">improve way accuracy mode</a></li>
<li>For new objects there is the <a href="https://josm.openstreetmap.de/wiki/Help/Action/Parallel">parallel mode</a></li>
</ul>
</div>
<div id="comment-78165-info" class="comment-info">
<span class="comment-age">(31 Dec '20, 14:26)</span> <span class="comment-user userinfo">skyper</span>
</div>
</div>
</div>
<div id="comment-tools-78000" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-78000-form-container" class="comment-form-container">
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

<span id="78001"></span>

<div id="answer-container-78001" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78001-score" class="post-score" title="current number of votes">
14
</div>
<span id="post-78001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JAT86 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several methods to do this but I'm not going to discuss them because it's not a good mapping technique.</p>
<p>The road is not part of the forest and should not be included in it. In addition, it will make future edits of the highway more complicated. It is tricky enough to work with properly mapped multipolygons that legitimately share a way with a highway or boundary line. This sharing is not legitimate.</p>
<p>Repeating myself: The forest is mapped correctly in the first image. Please don't proceed with your idea. And, if I can be so bold to ask, please undo any other wooded areas that you have mapped this way in the past.</p>
<p>Best,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '20, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span> </br></br></p>
</img>
</div>
</div>
<div id="comments-container-78001" class="comments-container">
&#10;</div>
<div id="comment-tools-78001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78001-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78002"></span>

<div id="answer-container-78002" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78002-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-78002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, What you're trying to do is actually incorrect mapping. The ground truth (from the image) looks like the forest does not extend to the center line of the highway. It looks like the forest line there is parallel to the highway. A IMHO rather complicated way achieve this paralleling is explained here :- <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/AlignWayS">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/AlignWayS</a> An easy way is to copy a section of the highway and paste it to the side, then use that as part of the forest way (amending the tags) or use it as a template of part of the forest way to later remove.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '20, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '20, 08:44</strong> </span></p>
</div>
</div>
<div id="comments-container-78002" class="comments-container">
&#10;</div>
<div id="comment-tools-78002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78002-form-container" class="comment-form-container">
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

