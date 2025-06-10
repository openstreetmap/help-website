+++
type = "question"
title = "Merging identical nodes to rejoin ways"
description = '''Hi all, I&#x27;m building a wayfinding app with OSM data. I&#x27;m only working with a small subset, the Toronto PATH relation for Toronto&#x27;s underground walkway/malls. I found that 3 nodes had been created where there should be one, so the ways didn&#x27;t join up. I simply edited two of the ways in the OSM iD edi...'''
date = "2016-11-14T01:01:00Z"
lastmod = "2016-11-17T22:39:00Z"
weight = 52920
keywords = [ "merge", "nodes" ]
aliases = [ "/questions/52920" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Merging identical nodes to rejoin ways](/questions/52920/merging-identical-nodes-to-rejoin-ways)

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
<span id="post-52920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52920-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm building a wayfinding app with OSM data. I'm only working with a small subset, the Toronto PATH relation for Toronto's underground walkway/malls.</p>
<p>I found that 3 nodes had been created where there should be one, so the ways didn't join up. I simply edited two of the ways in the OSM iD editor, and it automatically deleted the unnecessary nodes. Does it look OK? <a href="https://www.openstreetmap.org/node/4026125389">https://www.openstreetmap.org/node/4026125389</a> <a href="https://www.openstreetmap.org/node/4026125390">https://www.openstreetmap.org/node/4026125390</a> <a href="https://www.openstreetmap.org/node/4026125391">https://www.openstreetmap.org/node/4026125391</a></p>
<p>Changeset: <a href="https://www.openstreetmap.org/changeset/43619260">https://www.openstreetmap.org/changeset/43619260</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/7da79e17c54facdd637f9b71b264abbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaron%20Lawrence%20-%20Umajin&#39;s gravatar image" />
<p><span>Aaron Lawren...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaron Lawrence - Umajin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52920" class="comments-container">
<span id="52971"></span>
<div id="comment-52971" class="comment">
<div id="post-52971-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>off topic: for those curious among us: no, "PATH" is not contrary to <a href="https://wiki.openstreetmap.org/wiki/Names#Name_is_the_name_only">Name is the name only</a>, but really the name of this foot path network, see <a href="https://en.wikipedia.org/wiki/PATH%20(Toronto)">Wikipedia</a>. I guess it just would be debatable (<a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>) if the name "PATH" really should be on each single way or just on <a href="https://www.openstreetmap.org/relation/5441759">the network relation</a> (where it currently is, too).</p>
</div>
<div id="comment-52971-info" class="comment-info">
<span class="comment-age">(15 Nov '16, 21:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52972"></span>
<div id="comment-52972" class="comment">
<div id="post-52972-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, I think its an awkward choice for a name because it's so ambiguous, but it's well settled into their branding now. I think it would be better on the relation only. But I'm not launching into major revisions since the business approach is still being approved.</p>
</div>
<div id="comment-52972-info" class="comment-info">
<span class="comment-age">(15 Nov '16, 21:34)</span> <span class="comment-user userinfo">Aaron Lawren...</span>
</div>
</div>
</div>
<div id="comment-tools-52920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52920-form-container" class="comment-form-container">
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

<span id="52970"></span>

<div id="answer-container-52970" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52970-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-52970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aaron Lawrence - Umajin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for asking here! :) Your edit looks fine. Thank you for catching and fixing a non-obvious data usability problem that affected routing. Also see <a href="https://wiki.openstreetmap.org/wiki/Editing_Standards_and_Conventions#Junctions">https://wiki.openstreetmap.org/wiki/Editing_Standards_and_Conventions#Junctions</a> .</p>
<p><span class="small">(Just in case Hendrik deletes his answer – I am writing another to sum up alester's and my comments)</span></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '16, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '16, 20:36</strong> </span></p>
</div>
</div>
<div id="comments-container-52970" class="comments-container">
<span id="53018"></span>
<div id="comment-53018" class="comment">
<div id="post-53018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. A bit annoyed we lost that history of comments on Hendrik's answer, oh well.</p>
</div>
<div id="comment-53018-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 22:39)</span> <span class="comment-user userinfo">Aaron Lawren...</span>
</div>
</div>
</div>
<div id="comment-tools-52970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52970-form-container" class="comment-form-container">
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

