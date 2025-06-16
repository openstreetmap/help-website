+++
type = "question"
title = "How can I remove/merge duplicate relations?"
description = '''I found an area (around Vesuvius national park in Italy) where there are lots of duplicate relations (they have slightly different name, but they refer to the same hiking path, like these two: https://www.openstreetmap.org/relation/2672045#map=15/40.8100/14.4386 and https://www.openstreetmap.org/rel...'''
date = "2022-10-31T16:51:00Z"
lastmod = "2022-11-03T13:00:00Z"
weight = 86041
keywords = [ "relations" ]
aliases = [ "/questions/86041" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I remove/merge duplicate relations?](/questions/86041/how-can-i-removemerge-duplicate-relations)

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
<span id="post-86041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86041-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found an area (around Vesuvius national park in Italy) where there are lots of duplicate relations (they have slightly different name, but they refer to the same hiking path, like these two: <a href="https://www.openstreetmap.org/relation/2672045#map=15/40.8100/14.4386">https://www.openstreetmap.org/relation/2672045#map=15/40.8100/14.4386</a> and <a href="https://www.openstreetmap.org/relation/9278294#map=15/40.7982/14.4421">https://www.openstreetmap.org/relation/9278294#map=15/40.7982/14.4421</a> ).</p>
<p>Is there a better way to merge them/remove the duplicate one without manually removing all the member paths from one of them?</p>
<p>There is a similar question here: <a href="/questions/2014/is-it-possible-to-merge-relations">https://help.openstreetmap.org/questions/2014/is-it-possible-to-merge-relations</a> but it is old and does not provide an answer for the web editor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '22, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/cab682a6ffb50d9c8bc0054625dd8ce8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%C3%A1%C5%A1%20Hnyk&#39;s gravatar image" />
<p><span>Tomáš Hnyk</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomáš Hnyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86041" class="comments-container">
&#10;</div>
<div id="comment-tools-86041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86041-form-container" class="comment-form-container">
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

<span id="86055"></span>

<div id="answer-container-86055" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86055-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tomáš Hnyk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you have already found out iD (the default "web" editor) requires you to empty relations before deleting them, this is a design decision based on the target user base.</p>
<p>Any kind of more involved relation maintenance, particularly because you will want to compare the contents of one editor with another should be done with JOSM (there are other editors that allow you to delete a non-empty relation, but as said, probably not useful in your use case).</p>
<p>See <a href="https://josm.openstreetmap.de/">https://josm.openstreetmap.de/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '22, 07:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-86055" class="comments-container">
<span id="86080"></span>
<div id="comment-86080" class="comment">
<div id="post-86080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, it was reasonably easy with JOSM, after I got over the steep learning curve how to even download the data in question.</p>
<p>As for merging, there sdoes not seem to be a one-click way to do that, but one can copy all tags of a relation at once and I guess I could select all members of one relation and add it to the other, but I in the end did not need to do that.</p>
</div>
<div id="comment-86080-info" class="comment-info">
<span class="comment-age">(03 Nov '22, 13:00)</span> <span class="comment-user userinfo">Tomáš Hnyk</span>
</div>
</div>
</div>
<div id="comment-tools-86055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86055-form-container" class="comment-form-container">
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

