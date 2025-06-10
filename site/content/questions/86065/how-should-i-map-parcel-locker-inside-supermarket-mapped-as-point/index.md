+++
type = "question"
title = "How should I map parcel locker inside supermarket mapped as point"
description = '''There some supermarkets in the area I&#x27;m trying to map that have parcel lockers from courier companies inside them. These parcel lockers can only be accessed when the supermarket is open. Due to many of them being in a metropolitan area the supermarkets are mapped as shop=supermarket points and there...'''
date = "2022-11-02T17:14:00Z"
lastmod = "2022-11-03T07:25:00Z"
weight = 86065
keywords = [ "mapping", "supermarket", "parcel_locker" ]
aliases = [ "/questions/86065" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How should I map parcel locker inside supermarket mapped as point](/questions/86065/how-should-i-map-parcel-locker-inside-supermarket-mapped-as-point)

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
<span id="post-86065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86065-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There some supermarkets in the area I'm trying to map that have parcel lockers from courier companies inside them. These parcel lockers can only be accessed when the supermarket is open.</p>
<p>Due to many of them being in a metropolitan area the supermarkets are mapped as <code>shop=supermarket</code> points and therefore cannot contain another point for the parcel locker <code>amenity=parcel_locker</code> inside them.</p>
<p>Is there a way to map this relation of the parcel locker being inside the supermarket? The open hours problem can be solved with the <code>opening_hours</code> tag but that still doesn't make it clear that a customer should look for the locker <em>inside</em> the supermarket.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-supermarket" rel="tag" title="see questions tagged &#39;supermarket&#39;">supermarket</span> <span class="post-tag tag-link-parcel_locker" rel="tag" title="see questions tagged &#39;parcel_locker&#39;">parcel_locker</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '22, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/07ae5d8bdbd343cdf659320e00b606c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapper97882&#39;s gravatar image" />
<p><span>mapper97882</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapper97882 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86065" class="comments-container">
&#10;</div>
<div id="comment-tools-86065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86065-form-container" class="comment-form-container">
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

<span id="86066"></span>

<div id="answer-container-86066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86066-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-86066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the supermarket is mapped as a node, then I'd either change the supermarket into some sort of area feature and add the parcel locker node inside that, or just add the parcel locker as another node.</p>
<p>I wouldn't even think about trying to create a relation between the two.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '22, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86066" class="comments-container">
<span id="86075"></span>
<div id="comment-86075" class="comment">
<div id="post-86075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Additionally I would add the tag <code>description="located inside supermarket &lt;name&gt;"</code> or something similar.</p>
</div>
<div id="comment-86075-info" class="comment-info">
<span class="comment-age">(03 Nov '22, 07:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86066-form-container" class="comment-form-container">
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

