+++
type = "question"
title = "Keep node/way IDs when copying a relation"
description = '''I&#x27;m not sure if this is the right place to ask this, but figured there are a lot of people around here that are familiar with JOSM, so it can&#x27;t hurt to try.  I am copying a relation to another layer so I can cut the file size down of the data I&#x27;m importing. However, when I copy the relation, create ...'''
date = "2014-10-21T03:02:00Z"
lastmod = "2014-10-21T21:58:00Z"
weight = 37816
keywords = [ "josm", "relation" ]
aliases = [ "/questions/37816" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Keep node/way IDs when copying a relation](/questions/37816/keep-nodeway-ids-when-copying-a-relation)

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
<span id="post-37816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm not sure if this is the right place to ask this, but figured there are a lot of people around here that are familiar with JOSM, so it can't hurt to try.</p>
<p>I am copying a relation to another layer so I can cut the file size down of the data I'm importing. However, when I copy the relation, create a new layer and paste it, the relation's ways and nodes all have an id of 0. How can I copy the relation while saving the original ids? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '14, 03:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c65379ac4d3643b962db28626128b27a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chillNZ&#39;s gravatar image" />
<p><span>chillNZ</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chillNZ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '14, 22:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37816" class="comments-container">
&#10;</div>
<div id="comment-tools-37816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37816-form-container" class="comment-form-container">
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

<span id="37823"></span>

<div id="answer-container-37823" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37823-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chillNZ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you copy nodes and/or relations, they are new objects (and therefore have temporary id 0 until they get assigned their definitive id after uploading). I don't think there's a way around that, but you could use other techniques:</p>
<ul>
<li>Delete stuff you don't want from the current layer instead of copying stuff you want to a different layer. You might find the search function (Ctrl-F) helpfull for that.</li>
<li>Edit the *.osm file mannually (in a text editor, with tools like grep, or even with <a href="http://wiki.openstreetmap.org/wiki/Category:OSM_processing">osm parsing libs</a>) to remove the bits you don't want, instead of using josm.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '14, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-37823" class="comments-container">
<span id="37854"></span>
<div id="comment-37854" class="comment">
<div id="post-37854-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, I had tried the deleting method but turns out JOSM doesn't like actually deleting the nodes and ways from the source file either. I understand why, but it means deleting the nodes does effectively nothing for me as the program I'm using still tries to parse the nodes with tag action=delete. After a bit of research I think I'll just use <a href="http://wiki.openstreetmap.org/wiki/XMLStarlet">XMLStarlet</a> to remove the deleted nodes from the file to reduce the import time.</p>
</div>
<div id="comment-37854-info" class="comment-info">
<span class="comment-age">(21 Oct '14, 21:58)</span> <span class="comment-user userinfo">chillNZ</span>
</div>
</div>
</div>
<div id="comment-tools-37823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37823-form-container" class="comment-form-container">
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

