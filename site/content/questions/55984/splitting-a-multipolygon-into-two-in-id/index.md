+++
type = "question"
title = "Splitting a multipolygon into two in iD"
description = '''In the area I am working on there are a number of large multi polygons that were originally created that could really do with being split down to more correctly reflect the actual sub-areas, such as individual fields. If mapped as individual fields their boundaries show up - otherwise you just get o...'''
date = "2017-05-01T23:10:00Z"
lastmod = "2017-06-21T15:10:00Z"
weight = 55984
keywords = [ "ideditor", "multipolygon", "split", "splitting" ]
aliases = [ "/questions/55984" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Splitting a multipolygon into two in iD](/questions/55984/splitting-a-multipolygon-into-two-in-id)

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
<span id="post-55984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55984-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the area I am working on there are a number of large multi polygons that were originally created that could really do with being split down to more correctly reflect the actual sub-areas, such as individual fields. If mapped as individual fields their boundaries show up - otherwise you just get one very large area of arable land with no clear boundaries except where there are hedges.</p>
<p>I am using iD and am happy with it apart from one problem - if I click on a node and the semi-circular palette appears, and then I click on the scissors icon to split the line nothing visually changes. The scissors icon gets greyed out and the pop-up text changes to say "Lines can't be split at their beginning or end", so it looks like the line has been split, but I can't work out how to pick up each end of the line to move them. I have hunted through the Help and tried Googling for this, but I can't find out how to separate the two split ends. I have tried all sorts of modifier keys but none of them seem to work either.</p>
<p>Pleas advise how I can separate the two split ends in order to create two separate multipolygons.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '17, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a3175e6a29c8c0e004ea5d7f31493908?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickc&#39;s gravatar image" />
<p><span>nickc</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '17, 23:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55984" class="comments-container">
&#10;</div>
<div id="comment-tools-55984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55984-form-container" class="comment-form-container">
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

<span id="56068"></span>

<div id="answer-container-56068" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56068-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After using the scissors to split the line at the node, you now have 2 line ends that share a node. If you move the node, both lines move, because they are both connected to the node. You need to disconnect the 2 line ends from each other before you can separate them. The disconnect button in iD looks like arrows pointing left and right.</p>
<p>However, iD does not let you disconnect two lines that are members of a relation (such as the multipolygon). So you have to remove one of the parts from the relation first. Which you probably need to do anyway, if you want it to be in a new multipolygon. After you make your 1 or more likely 2 node splits, select one segment and delete its membership in the multipolygon relation (trash can on sidebar under All Relations). Now you can use disconnect on the two split nodes, close them up and/or move them, and make a new multipolygon relation for the split-off part. Or, you can put the split-off part back into the same multipolygon relation if that was your goal.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '17, 03:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-56068" class="comments-container">
<span id="56082"></span>
<div id="comment-56082" class="comment">
<div id="post-56082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much for your answer, although I couldn't quite follow it - in particular I can't see anything in a sidebar labelled All Relations. I have now just about worked out how to do it, but it felt like more luck than judgment!</p>
<p>Here is how it works for anyone else needing to do this:</p>
<ol>
<li>Click on the node at which you want to split the multipolygon.</li>
<li>Click on the scissors split icon on the palette.</li>
<li>Click on the trashcan icon - the node at which you are splitting disappears and the two adjoining nodes become the end points.</li>
</ol>
<p>You can then extend these lines using the Continue this line icon on the palette. If you want to create two separate multi polygons you have to split the first one at another point, then you can join the split ends of the two parts together, again using the Continue this line icon on the palette.</p>
</div>
<div id="comment-56082-info" class="comment-info">
<span class="comment-age">(07 May '17, 23:30)</span> <span class="comment-user userinfo">nickc</span>
</div>
</div>
</div>
<div id="comment-tools-56068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56068-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56710"></span>

<div id="answer-container-56710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56710-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/13656/nickc">@nickc</a>, yes I really want this feature too!<br />
We're tracking it here: <a href="https://github.com/openstreetmap/iD/issues/3934">https://github.com/openstreetmap/iD/issues/3934</a></p>
<p>In the meantime, the best solution is to use JOSM to split up large areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '17, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span> </br></p>
</div>
</div>
<div id="comments-container-56710" class="comments-container">
&#10;</div>
<div id="comment-tools-56710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56710-form-container" class="comment-form-container">
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

