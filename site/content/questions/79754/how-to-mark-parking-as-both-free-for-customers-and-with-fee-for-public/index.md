+++
type = "question"
title = "How to mark parking as both free for customers and with fee for public?"
description = '''There are several pubs locally with parking with ANPR and you give the pub your registration if you&#x27;re a customer or you can pay to park through some app. Is this taggable? Some combination of https://wiki.openstreetmap.org/wiki/Key:parking:condition perhaps, but I couldn&#x27;t figure out what, or I won...'''
date = "2021-04-19T23:29:00Z"
lastmod = "2021-04-21T10:03:00Z"
weight = 79754
keywords = [ "access", "fee", "parking" ]
aliases = [ "/questions/79754" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to mark parking as both free for customers and with fee for public?](/questions/79754/how-to-mark-parking-as-both-free-for-customers-and-with-fee-for-public)

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
<span id="post-79754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are several pubs locally with parking with ANPR and you give the pub your registration if you're a customer or you can pay to park through some app. Is this taggable? Some combination of <a href="https://wiki.openstreetmap.org/wiki/Key:parking:condition">https://wiki.openstreetmap.org/wiki/Key:parking:condition</a> perhaps, but I couldn't figure out what, or I wondered about access=public fee=yes fee:customers=no</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-fee" rel="tag" title="see questions tagged &#39;fee&#39;">fee</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '21, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/09dd5995d85d7b0636ebd94e1f49c463?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrekClimbing&#39;s gravatar image" />
<p><span>TrekClimbing</span><br />
<span class="score" title="161 reputation points">161</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrekClimbing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79754" class="comments-container">
&#10;</div>
<div id="comment-tools-79754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79754-form-container" class="comment-form-container">
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

<span id="79759"></span>

<div id="answer-container-79759" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79759-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>customers=</code> is not a user mode for legal restrictions that's as commonly used as others yet, which is furthermore different from the vehicle modes usually tagged. <code>parking:condition=</code> is for <code>parking:lane=</code>, not <code>amenity=parking</code> carparks.</p>
<p><code>access=yes</code> + <code>fee=yes</code> + <code>fee:conditional=no @ (customers)</code> may be better supported.</p>
<p>There's a generic <code>payment:app=yes</code>, and <code>surveillance:type=ALPR</code> for the other attributes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '21, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '21, 09:51</strong> </span></p>
</div>
</div>
<div id="comments-container-79759" class="comments-container">
<span id="79771"></span>
<div id="comment-79771" class="comment">
<div id="post-79771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:fee">wiki</a> suggests <code>fee=yes</code> + <code>fee:conditional=no @ customer</code> (customer in singular). Although, I personally would also have suggested <code>customers</code> as plural in analogy to the <code>access</code> value.</p>
</div>
<div id="comment-79771-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 20:34)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79772"></span>
<div id="comment-79772" class="comment">
<div id="post-79772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you both. I hadn't looked at the fee key wiki page. Nor had I come across anything to do with payment methods or AL/NPR.</p>
</div>
<div id="comment-79772-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 21:51)</span> <span class="comment-user userinfo">TrekClimbing</span>
</div>
</div>
<span id="79779"></span>
<div id="comment-79779" class="comment">
<div id="post-79779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn"></a><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> I wonder whether this is an error on the <code>fee</code> wiki page. The wiki page for <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> lists <code>customers</code> (plural) as a possible value, not <code>customer</code> (singular).</p>
</div>
<div id="comment-79779-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 09:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="79785"></span>
<div id="comment-79785" class="comment">
<div id="post-79785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> On the page you link <code>customers</code> is used as a value, not as a condition. We could check if there are any other usages of <code>customer(s)</code> as condition or other than an access value.</p>
</div>
<div id="comment-79785-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 10:03)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-79759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79759-form-container" class="comment-form-container">
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

