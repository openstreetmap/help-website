+++
type = "question"
title = "A lake and a forest share a large stretch of outline; how to change part of only one?"
description = '''Hi, I tried to add a feature which was left out at the position 52.04035° N, 9.53146°W. The forest has a long, narrow, rectangular indentation; apparently whoever mapped this forest (via Bing, I suppose) could see that there is no forest in this area, but no more. There is actually a basin there wit...'''
date = "2017-08-02T21:13:00Z"
lastmod = "2017-08-02T22:00:00Z"
weight = 57426
keywords = [ "shared_nodes", "separate" ]
aliases = [ "/questions/57426" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [A lake and a forest share a large stretch of outline; how to change part of only one?](/questions/57426/a-lake-and-a-forest-share-a-large-stretch-of-outline-how-to-change-part-of-only-one)

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
<span id="post-57426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57426-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I tried to add a feature which was left out at the position 52.04035° N, 9.53146°W.</p>
<p>The forest has a long, narrow, rectangular indentation; apparently whoever mapped this forest (via Bing, I suppose) could see that there is no forest in this area, but no more. There is actually a basin there with a narrow channel connecting it to the lake; a kind of micro marina.</p>
<p>My problem is that to the west of the basin the lake and the forest share a number of nodes.</p>
<p>Is there a way (preferrably in Potlatch 2) to extend the lake to encompass that basin, without extending the forest as well?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shared_nodes" rel="tag" title="see questions tagged &#39;shared_nodes&#39;">shared_nodes</span> <span class="post-tag tag-link-separate" rel="tag" title="see questions tagged &#39;separate&#39;">separate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '17, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/06b2f5d4fa9884ae47333da22b6f2662?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marabu_Too&#39;s gravatar image" />
<p><span>Marabu_Too</span><br />
<span class="score" title="210 reputation points">210</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marabu_Too has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57426" class="comments-container">
&#10;</div>
<div id="comment-tools-57426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57426-form-container" class="comment-form-container">
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

<span id="57427"></span>

<div id="answer-container-57427" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57427-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-57427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marabu_Too has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can disconnect nodes in Potlatch 2 using Shift-J (J will join them again).</p>
<p>When I want to do something like this, I usually follow these steps:</p>
<ol>
<li>Draw the new part of the outline as a separate way. Do not tag it. Make sure it joins to the nodes of the existing way.</li>
<li>Select the way you wish to extend (the lake), and cut that way (keypress X) at the two points where you are extending it.</li>
<li>Delete the section which is not longer needed.</li>
<li>Select the remaining portions (there may be more than 1) of the original way <strong>AND</strong> the new untagged way and join them using keypress J. The existing tags should now be applied to the whole way.</li>
<li>In your case you need to repeat the process with the forest. You do not need to do point 1. Instead cut the forest way, delete the unneeded part, and then make sure the original way is in a single piece. Then select one of the nodes where the way ends, extend it to the next node of what you have added, and then use the follow function (keypress F) to keep extending the way until it once more forms a closed way.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '17, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-57427" class="comments-container">
&#10;</div>
<div id="comment-tools-57427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57427-form-container" class="comment-form-container">
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

