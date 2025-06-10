+++
type = "question"
title = "Do we add Turn Restriction tags in iD Editor?"
description = '''When mapping Turn Restrictions in iD Editor, is it sufficient to simply configure the arrows in the diagram, or do we also need to add tags?  I&#x27;m mostly unsure because adding a tag like restrictions = no _ left _ turn might only apply to one segment on a road intersection, not all segments. On the o...'''
date = "2018-06-22T07:54:00Z"
lastmod = "2018-06-22T10:40:00Z"
weight = 64315
keywords = [ "ideditor", "restrictions", "turn_restrictions" ]
aliases = [ "/questions/64315" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Do we add Turn Restriction tags in iD Editor?](/questions/64315/do-we-add-turn-restriction-tags-in-id-editor)

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
<span id="post-64315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64315-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When mapping Turn Restrictions in iD Editor, is it sufficient to simply configure the arrows in the diagram, or do we also need to add tags?</p>
<p>I'm mostly unsure because adding a tag like restrictions = no _ left _ turn might only apply to one segment on a road intersection, not all segments. On the other hand, the Restrictions Wiki page mentions many tags, which makes me inclined to add them.</p>
<p>If tags /are/ supposed to be added, how do I avoid indicating one tag for all segments (as mentioned above)?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '18, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/74ace9f12d8a8354d511ea87b04f4bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeghanKNg&#39;s gravatar image" />
<p><span>MeghanKNg</span><br />
<span class="score" title="171 reputation points">171</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeghanKNg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64315" class="comments-container">
&#10;</div>
<div id="comment-tools-64315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64315-form-container" class="comment-form-container">
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

<span id="64320"></span>

<div id="answer-container-64320" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64320-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MeghanKNg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding a turn restriction (in any editor) does not require adding any tags to the affected ways.</p>
<p>The restrictions are modelled by relation objects that contain references to the involved objects (typically a way with the "from" role, a "via" node and a "to" way). iD already sets this up correctly so in the majority of all cases there is nothing further to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '18, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '18, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-64320" class="comments-container">
&#10;</div>
<div id="comment-tools-64320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64320-form-container" class="comment-form-container">
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

