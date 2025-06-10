+++
type = "question"
title = "id editor: changing points into lines or areas"
description = '''https://www.openstreetmap.org/node/2271287182 is a barrier=gate that I would like to change into a linear feature. https://www.openstreetmap.org/node/2271903985 is a building=yes that I would like to change into a area feature. Must I delete each point first, or is there some way to give a second po...'''
date = "2017-08-24T04:48:00Z"
lastmod = "2017-08-24T16:23:00Z"
weight = 58691
keywords = [ "ideditor", "conversion", "points", "lines", "areas" ]
aliases = [ "/questions/58691" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [id editor: changing points into lines or areas](/questions/58691/id-editor-changing-points-into-lines-or-areas)

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
<span id="post-58691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/node/2271287182">https://www.openstreetmap.org/node/2271287182</a> is a barrier=gate that I would like to change into a linear feature. <a href="https://www.openstreetmap.org/node/2271903985">https://www.openstreetmap.org/node/2271903985</a> is a building=yes that I would like to change into a area feature. Must I delete each point first, or is there some way to give a second point to the gate, and more points to the building?</p>
<p>When I right click on the point, the only choice that comes up is Delete.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '17, 04:48</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '17, 04:49</strong> </span></p>
</div>
</div>
<div id="comments-container-58691" class="comments-container">
&#10;</div>
<div id="comment-tools-58691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58691-form-container" class="comment-form-container">
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

<span id="58780"></span>

<div id="answer-container-58780" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58780-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-58780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jidanni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if making the gate a linear feature is a good idea. Typically gates should be points that are part of the way where the gate can affect the accessibility of the road/path. That way routing software can take it into account. The way it is mapped right now, off to the side of the road means it probably won't be taken into account by routing software.</p>
<p>However to answer your original question, you can draw a blank line or area and then select both the point and the line/area at the same time (holding shift to select the second one) and then right click. There will now be a "Merge" option in the menu that will move all the tags from the point to the line or area. Note however that the point you are trying to merge can not be part of the line or area you are trying to merge it into.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '17, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-58780" class="comments-container">
<span id="58783"></span>
<div id="comment-58783" class="comment">
<div id="post-58783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK but now the gates render as a tiny dot not in the center of the road, and not even in all layers (which all have roads.) How is anyone going to notice them before setting off on a trip, only to have it end at a gate they didn't notice? <a href="https://www.openstreetmap.org/changeset/51398998#map=19/24.18386/120.86837">https://www.openstreetmap.org/changeset/51398998#map=19/24.18386/120.86837</a></p>
</div>
<div id="comment-58783-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 09:40)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="58784"></span>
<div id="comment-58784" class="comment">
<div id="post-58784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I moved the gates to a node on the way, but they still render to the side a little, and not blocking the whole road, like a nice linear feature would.</p>
</div>
<div id="comment-58784-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 09:42)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-58780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58780-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58799"></span>

<div id="answer-container-58799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58799-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is a way to do that in iD right now. The functionality to turn a node into an area--keeping the tags--does exist in Potlatch and I use it all the time:</p>
<ol>
<li>Select node</li>
<li>Shift click near node</li>
<li>Make further edits to the resulting rectangle</li>
</ol>
<p>Won't work for the node-to-line case, but is great for converting buildings from nodes to areas!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '17, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-58799" class="comments-container">
<span id="58801"></span>
<div id="comment-58801" class="comment">
<div id="post-58801-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>With ID merging deletes the point while creating the area. Which works fine but involves bloodshed. Does Potlatch spare the slaughter?</p>
</div>
<div id="comment-58801-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 15:26)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="58807"></span>
<div id="comment-58807" class="comment">
<div id="post-58807-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I understand your question correctly, Potlatch does keep the original node's ID, the other nodes all get new IDs.</p>
</div>
<div id="comment-58807-info" class="comment-info">
<span class="comment-age">(24 Aug '17, 16:23)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-58799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58799-form-container" class="comment-form-container">
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

