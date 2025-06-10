+++
type = "question"
title = "Delete interpolations if all addresses are known?"
description = '''I have seen a case or two when all the buildings on a particular street are mapped. Assuming buildings all had the correct metadata (address etc...), would you delete the address interpolation lines?'''
date = "2014-09-04T14:16:00Z"
lastmod = "2014-09-04T14:36:00Z"
weight = 36593
keywords = [ "delete", "interpolation" ]
aliases = [ "/questions/36593" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Delete interpolations if all addresses are known?](/questions/36593/delete-interpolations-if-all-addresses-are-known)

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
<span id="post-36593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36593-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have seen a case or two when all the buildings on a particular street are mapped. Assuming buildings all had the correct metadata (address etc...), would you delete the address interpolation lines?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a8460f1891830c4cfdfb6707d8cb56ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikewilliamson&#39;s gravatar image" />
<p><span>mikewilliamson</span><br />
<span class="score" title="81 reputation points">81</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikewilliamson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36593" class="comments-container">
&#10;</div>
<div id="comment-tools-36593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36593-form-container" class="comment-form-container">
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

<span id="36595"></span>

<div id="answer-container-36595" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36595-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikewilliamson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes. Address interpolation is just a method to identify large address range in a row. If each address is then mapped individually, it is not anymore necessary to keep the lower accurate elements (the address interpolation lines).</p>
<p>This is happening daily in OSM : for instance, a first contributor creates a 'school' with a node (POI). Then somebody else is adding the school building polygon. Then he moves the 'school' tags to the building polygon (or even better, to surending polygon covering exactly the school property) and removes the original POI. The polygon is more accurate than a simple node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '14, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-36595" class="comments-container">
&#10;</div>
<div id="comment-tools-36595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36595-form-container" class="comment-form-container">
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

