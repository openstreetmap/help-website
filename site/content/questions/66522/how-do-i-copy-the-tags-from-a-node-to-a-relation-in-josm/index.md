+++
type = "question"
title = "How do I copy the tags from a node to a relation in JOSM"
description = '''Often I create a relation for an object and want to copy the tags from a node that was used to describe the object. This often happens when I want to use the tags from a GNIS node that was meant for an area but was imported years ago as a simple node. I&#x27;ve tried many things (Copy tags, Paste tags, e...'''
date = "2018-10-28T12:08:00Z"
lastmod = "2020-03-04T10:20:00Z"
weight = 66522
keywords = [ "josm", "copy-paste", "relations", "tags" ]
aliases = [ "/questions/66522" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I copy the tags from a node to a relation in JOSM](/questions/66522/how-do-i-copy-the-tags-from-a-node-to-a-relation-in-josm)

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
<span id="post-66522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66522-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Often I create a relation for an object and want to copy the tags from a node that was used to describe the object. This often happens when I want to use the tags from a GNIS node that was meant for an area but was imported years ago as a simple node.</p>
<p>I've tried many things (Copy tags, Paste tags, etc.) but nothing seems to give me the desired result. I can get the tags to the "outside" of the relation but cannot get them applied to the inside.</p>
<p>It's hard to explain exactly what I mean but many of you work with relations all the time and might have some method or insight to share.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-copy-paste" rel="tag" title="see questions tagged &#39;copy-paste&#39;">copy-paste</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '18, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-66522" class="comments-container">
&#10;</div>
<div id="comment-tools-66522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66522-form-container" class="comment-form-container">
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

<span id="66524"></span>

<div id="answer-container-66524" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66524-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this:</p>
<ol>
<li>Select/activate the node from which you want to copy the tags</li>
<li>Press CTRL+C</li>
<li>Select/activate the new relation and open the relation editor</li>
<li>Press "paste tags from buffer" (the symbol below the dust bin on the left side)</li>
</ol>
<p>The new tags should now be visible "inside" the relation, or more precisely in the relation editor as shown here <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor</a> .</p>
<p>I hope this solves it. It took me years to figure that out ...</p>
<p>Regards</p>
<p>BAK365</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '18, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/952db4d34eb11523053fd818edc87322?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BAK365&#39;s gravatar image" />
<p><span>BAK365</span><br />
<span class="score" title="226 reputation points">226</span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BAK365 has 2 accepted answers">66%</span></p>
</div>
</div>
<div id="comments-container-66524" class="comments-container">
<span id="66526"></span>
<div id="comment-66526" class="comment">
<div id="post-66526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I find it more useful and easy to <em>not</em> use the relation editor pop-up window. But likely that is a matter of taste. See my adapted answer.</p>
</div>
<div id="comment-66526-info" class="comment-info">
<span class="comment-age">(28 Oct '18, 15:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66524-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66525"></span>

<div id="answer-container-66525" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66525-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following works with all types of objects, but also for your special case (node→relation).</p>
<ol>
<li>Select the node from which you want to copy the tags</li>
<li>Press Ctrl+C (to copy the currently selected object to the clipboard)</li>
<li>Select the new relation (check your current selection in the <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/SelectionList">selection window</a>)</li>
<li>Press Ctrl+Shift+V (to paste the tags from the object in the clipboard to the currently selected object)</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '18, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '18, 15:34</strong> </span></p>
</div>
</div>
<div id="comments-container-66525" class="comments-container">
<span id="66528"></span>
<div id="comment-66528" class="comment">
<div id="post-66528-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I learned how to do this, the critical UI hurdle was figuring out how to select a relation. (There are several options, such as right click -&gt; select relation when you have one of the relation's members selected, or alternatively, double-clicking the relation in the relations window.) Your answer is already helpful, but I believe it would be improved by explaining that particular step in more detail.</p>
</div>
<div id="comment-66528-info" class="comment-info">
<span class="comment-age">(28 Oct '18, 20:02)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="66529"></span>
<div id="comment-66529" class="comment">
<div id="post-66529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to all. During the night after I asked the question the answer came to me because I had read it somewhere else a couple weeks ago. The "three pluses button" on the left side do the pasting. Unfortunately, it's not at all obvious how to do it when you're looking at the Relation Editor.</p>
</div>
<div id="comment-66529-info" class="comment-info">
<span class="comment-age">(28 Oct '18, 23:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="66530"></span>
<div id="comment-66530" class="comment">
<div id="post-66530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@Tordanik</a>: yes, it is a bit tricky to find how to select an relation, but how-to depends on if the relation is already existing or was/will be created newly. An own question for this site. ;-)</p>
</div>
<div id="comment-66530-info" class="comment-info">
<span class="comment-age">(29 Oct '18, 06:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="73356"></span>
<div id="comment-73356" class="comment">
<div id="post-73356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Both ways will overwrite(!) possible existing values of tags.</p>
<p>Is there a way to merge values like Crtl+Shift+G for merging nodes in ways with warning if there are conflicts?</p>
</div>
<div id="comment-73356-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 10:20)</span> <span class="comment-user userinfo">PHerison</span>
</div>
</div>
</div>
<div id="comment-tools-66525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66525-form-container" class="comment-form-container">
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

