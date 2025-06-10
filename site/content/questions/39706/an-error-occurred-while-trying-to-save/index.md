+++
type = "question"
title = "An error occurred while trying to save"
description = '''Thi is the message:  Placeholder Relation not found for reference -6 in relation -3. I don&#x27;t understand, this is the url: https://www.openstreetmap.org/edit#map=18/45.57738/12.26610 I am trying to add an historical building (a 5 star hotel) its restaurant and its park! Help me please,  Elisa'''
date = "2014-12-18T22:54:00Z"
lastmod = "2014-12-20T10:03:00Z"
weight = 39706
keywords = [ "newbie", "reference", "error" ]
aliases = [ "/questions/39706" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [An error occurred while trying to save](/questions/39706/an-error-occurred-while-trying-to-save)

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
<span id="post-39706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39706-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thi is the message:</p>
<p>Placeholder Relation not found for reference -6 in relation -3.</p>
<p>I don't understand, this is the url: <a href="https://www.openstreetmap.org/edit#map=18/45.57738/12.26610">https://www.openstreetmap.org/edit#map=18/45.57738/12.26610</a></p>
<p>I am trying to add an historical building (a 5 star hotel) its restaurant and its park!</p>
<p>Help me please,</p>
<p>Elisa</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-reference" rel="tag" title="see questions tagged &#39;reference&#39;">reference</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '14, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/afe54de316bde8fa53b1e32b3859513b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Villa%20Condulmer&#39;s gravatar image" />
<p><span>Villa Condulmer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Villa Condulmer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39706" class="comments-container">
<span id="39707"></span>
<div id="comment-39707" class="comment">
<div id="post-39707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Elisa, why do you have the buildings divided up into so many sections?</p>
</div>
<div id="comment-39707-info" class="comment-info">
<span class="comment-age">(18 Dec '14, 23:02)</span> <span class="comment-user userinfo">baghaii</span>
</div>
</div>
<span id="39708"></span>
<div id="comment-39708" class="comment">
<div id="post-39708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No idea... It was divided when I found it... I tried to create a unique building, but it is not working, I suppose...</p>
</div>
<div id="comment-39708-info" class="comment-info">
<span class="comment-age">(18 Dec '14, 23:06)</span> <span class="comment-user userinfo">Villa Condulmer</span>
</div>
</div>
</div>
<div id="comment-tools-39706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39706-form-container" class="comment-form-container">
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

<span id="39736"></span>

<div id="answer-container-39736" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39736-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've had a look at the data. The two building were actually multiple overlapping ways and multi-polygons and needed some effort to sort out.</p>
<p>iD (the online editor) will create a multi-polygon from a simple building polygon if that is split and it seems that this went so far that iD became confused. Likely this is simply a bug and I'll open an issue on the id issue tracker referencing this.</p>
<p>The area is now cleaned up so I wouldn't expect any immediate problems straight away now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '14, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-39736" class="comments-container">
&#10;</div>
<div id="comment-tools-39736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39736-form-container" class="comment-form-container">
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

