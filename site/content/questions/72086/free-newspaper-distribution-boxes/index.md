+++
type = "question"
title = "Free newspaper distribution boxes"
description = '''How can I tag correctly those boxes used for distribution of free newspapers (see image below from Commons)?  The closest solution I thought of is something like: amenity=vending_machine + vending=newspapers + payment=no but it doesn&#x27;t sound 100% right.  '''
date = "2019-12-12T17:07:00Z"
lastmod = "2019-12-13T14:08:00Z"
weight = 72086
keywords = [ "newspaper", "box", "distribution" ]
aliases = [ "/questions/72086" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Free newspaper distribution boxes](/questions/72086/free-newspaper-distribution-boxes)

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
<span id="post-72086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72086-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I tag correctly those boxes used for distribution of free newspapers (see image below from Commons)? The closest solution I thought of is something like: amenity=vending_machine + vending=newspapers + payment=no but it doesn't sound 100% right.</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Take_our_picture_please_0073.jpg/800px-Take_our_picture_please_0073.jpg" alt="example from" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newspaper" rel="tag" title="see questions tagged &#39;newspaper&#39;">newspaper</span> <span class="post-tag tag-link-box" rel="tag" title="see questions tagged &#39;box&#39;">box</span> <span class="post-tag tag-link-distribution" rel="tag" title="see questions tagged &#39;distribution&#39;">distribution</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '19, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1148662ffe4381ae83b991b9f8d52e6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Torredibabele&#39;s gravatar image" />
<p><span>Torredibabele</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Torredibabele has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-72086" class="comments-container">
&#10;</div>
<div id="comment-tools-72086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72086-form-container" class="comment-form-container">
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

<span id="72092"></span>

<div id="answer-container-72092" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72092-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Torredibabele has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:vending=newspapers.">https://wiki.openstreetmap.org/wiki/Tag:vending=newspapers.</a> You can refer to <a href="https://overpass-turbo.eu/s/OWI">https://overpass-turbo.eu/s/OWI</a> for combinations.</p>
<blockquote>
<p>something like: amenity=vending_machine + vending=newspapers + payment=no but it doesn't sound 100% right.</p>
</blockquote>
<p>What doesn't sound right is tagging <code>payment=no</code> only. These should be <code>fee=no</code> upfront.</p>
<p>Theoretically, such a box is already a "machine". Although the implication of "vending" ia questionable, there's already 6923 (4.95%) of <code>amenity=vending_machine</code> with <code>fee=yes</code>. Will do until anyone raises a better idea in general.</p>
<p>Personal thoughts:</p>
<p>Perhaps one can say an <code>amenity=letter_box</code> is an kind of such box with an address and <code>access=private</code>, seeing how free newspapers are distributed.</p>
<p>This is a good question for dispeners that are not directly payable too, for example coffee machines, and even something as minor as disinfectant alcohol. We have <code>amenity=drinking_water</code> (although I'm not sure what kind of <code>man_made=</code> a water machine itself would be, same for <code>amenity=vending_machine</code>), and <code>amenity=compressed_air</code> specifically.</p>
<p>Adding to my actual answer, I suppose a <code>amenity=vending_machine</code> would be purpose-built for <code>payment=yes</code> (thus could be optionally made <code>fee=no</code>). A dispenser could have <code>payment=no</code> but <code>fee=yes</code>, requiring the user to pay somewhere else (eg at the counter). Whether this constituent a vending machine should be debatable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '19, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Dec '19, 11:34</strong> </span></p>
</div>
</div>
<div id="comments-container-72092" class="comments-container">
<span id="72093"></span>
<div id="comment-72093" class="comment">
<div id="post-72093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, also for the links. I found there is quite a few vending machines with vending=newspapers + fee=no so I'll be using that.</p>
</div>
<div id="comment-72093-info" class="comment-info">
<span class="comment-age">(13 Dec '19, 14:08)</span> <span class="comment-user userinfo">Torredibabele</span>
</div>
</div>
</div>
<div id="comment-tools-72092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72092-form-container" class="comment-form-container">
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

