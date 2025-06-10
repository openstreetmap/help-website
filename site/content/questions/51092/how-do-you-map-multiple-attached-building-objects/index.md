+++
type = "question"
title = "How do you map multiple attached building objects?"
description = '''This is related to the question: https://help.openstreetmap.org/questions/36574/how-do-you-map-and-tag-a-screened-porch? In that question they answered that porches could be tagged with building:porch. With that in mind, how should I tag two building that share a wall with each other. This also come...'''
date = "2016-07-25T22:14:00Z"
lastmod = "2016-07-25T22:51:00Z"
weight = 51092
keywords = [ "building", "ways", "multiple", "tagging" ]
aliases = [ "/questions/51092" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do you map multiple attached building objects?](/questions/51092/how-do-you-map-multiple-attached-building-objects)

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
<span id="post-51092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51092-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is related to the question:</p>
<p><a href="https://help.openstreetmap.org/questions/36574/how-do-you-map-and-tag-a-screened-porch?">https://help.openstreetmap.org/questions/36574/how-do-you-map-and-tag-a-screened-porch?</a></p>
<p>In that question they answered that porches could be tagged with building:porch. With that in mind, how should I tag two building that share a wall with each other.</p>
<p>This also comes up in things like row homes and some building in commercial areas. The validator complains if I have a building that is an unclosed way, so I am assuming that I can't just make a building that only has three sides and shares its forth side with another building.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '16, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f0a0bbd14f78f8e0a40873cc6c769c33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zellfaze&#39;s gravatar image" />
<p><span>zellfaze</span><br />
<span class="score" title="141 reputation points">141</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zellfaze has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51092" class="comments-container">
&#10;</div>
<div id="comment-tools-51092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51092-form-container" class="comment-form-container">
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

<span id="51093"></span>

<div id="answer-container-51093" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zellfaze has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>talking of two four-sided buildings which share a wall:</p>
<p>The usual way: just let them share two nodes. Each four sides and one side of each uses the same nodes than the other building. Example <a href="https://www.openstreetmap.org/way/145005615">https://www.openstreetmap.org/way/145005615</a></p>
<p>If you do not really know the inner walls of a quite uniform (outside) big building, then rather just map it as a single building with possibly several housenumber nodes (if it has several numbers). If it is terraced houses, then <span>building=terrace</span> would be the tag to use on such a way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '16, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '16, 22:53</strong> </span></p>
</div>
</div>
<div id="comments-container-51093" class="comments-container">
&#10;</div>
<div id="comment-tools-51093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51093-form-container" class="comment-form-container">
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

