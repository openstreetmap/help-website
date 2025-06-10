+++
type = "question"
title = "Tagging a kiosk with additional logistics services (pick-up, drop-off etc)"
description = '''How do I tag a regular kiosk selling candy, tobacco etc. as having additional services for pickup/dropoff of packages? For example, if they have self-service for parcel pickup connected to certain carriers (Instabox, Budbee, DHL, Schenker, you name it).'''
date = "2022-08-10T11:14:00Z"
lastmod = "2022-08-11T13:22:00Z"
weight = 85301
keywords = [ "tagging" ]
aliases = [ "/questions/85301" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging a kiosk with additional logistics services (pick-up, drop-off etc)](/questions/85301/tagging-a-kiosk-with-additional-logistics-services-pick-up-drop-off-etc)

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
<span id="post-85301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I tag a regular kiosk selling candy, tobacco etc. as having additional services for pickup/dropoff of packages? For example, if they have self-service for parcel pickup connected to certain carriers (Instabox, Budbee, DHL, Schenker, you name it).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '22, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/adbb6f115760a11e11accbd75f490ddc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malvo&#39;s gravatar image" />
<p><span>malvo</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malvo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85301" class="comments-container">
<span id="85303"></span>
<div id="comment-85303" class="comment">
<div id="post-85303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are these machines? If so see <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparcel_locker.">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparcel_locker.</a> If over-the-counter type services, I'm not so sure.</p>
</div>
<div id="comment-85303-info" class="comment-info">
<span class="comment-age">(10 Aug '22, 12:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="85305"></span>
<div id="comment-85305" class="comment">
<div id="post-85305-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still new to this so maybe I've misunderstood, but 1) that seems correct, but parcel lockers are often (always?) vendor exclusive, so a binary piece of information that a parcel locker exists isn't very helpful if you don't know what logistics company operates it, and 2) over-counter service is sometimes a thing also, sometimes vendors have only that option, sometimes they have both options at different premises (over-counter on one, then a box at another venue, or even outside). Perhaps it makes more sense to have the box as a completely separate object, so it can be outside, but if inside have a relation to the venue (much like an ATM?) -- and in case of over-counter it should be an amenity of the venue like <code>amenity=servicepoint dhl</code> or something?</p>
</div>
<div id="comment-85305-info" class="comment-info">
<span class="comment-age">(10 Aug '22, 13:04)</span> <span class="comment-user userinfo">malvo</span>
</div>
</div>
<span id="85310"></span>
<div id="comment-85310" class="comment">
<div id="post-85310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, map the box as a separate object. I'll be doing one soon located in the back of a shop.</p>
</div>
<div id="comment-85310-info" class="comment-info">
<span class="comment-age">(11 Aug '22, 09:07)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="85311"></span>
<div id="comment-85311" class="comment">
<div id="post-85311-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>do you have an example of what object type to choose, and how to specify operator?</p>
</div>
<div id="comment-85311-info" class="comment-info">
<span class="comment-age">(11 Aug '22, 09:09)</span> <span class="comment-user userinfo">malvo</span>
</div>
</div>
<span id="85315"></span>
<div id="comment-85315" class="comment">
<div id="post-85315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is the one I've just mapped: <a href="https://www.openstreetmap.org/node/9947325550">https://www.openstreetmap.org/node/9947325550</a></p>
</div>
<div id="comment-85315-info" class="comment-info">
<span class="comment-age">(11 Aug '22, 13:22)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

