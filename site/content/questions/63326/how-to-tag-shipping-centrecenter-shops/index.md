+++
type = "question"
title = "How to tag shipping centre/center shops?"
description = '''Distinct from public post offices, these shops are private businesses that ship parcels. Many shops offer other services -- the rental of mailbox addresses to receive and hold mail, and office services similar to shop=copyshop. It seems like the most common tagging in use is simply amenity=post_offi...'''
date = "2018-05-05T17:34:00Z"
lastmod = "2018-06-07T00:25:00Z"
weight = 63326
keywords = [ "post_office", "dhl", "ups", "shipping", "fedex" ]
aliases = [ "/questions/63326" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag shipping centre/center shops?](/questions/63326/how-to-tag-shipping-centrecenter-shops)

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
<span id="post-63326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63326-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Distinct from public post offices, these shops are private businesses that ship parcels. Many shops offer other services -- the rental of mailbox addresses to receive and hold mail, and office services similar to <a href="https://wiki.openstreetmap.org/wiki/Tag:shop=copyshop">shop=copyshop</a>.</p>
<p>It seems like the most common tagging in use is simply <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpost_office">amenity=post_office</a> but I feel it would be preferable to distinguish public postal services from these private shops. Maybe add <strong>post_office:type=private</strong> or <strong>post_office:type=shipping_centre</strong>? Or is there some value of the <a href="https://wiki.openstreetmap.org/wiki/Key:shop">shop</a> key that would be better? <strong>shop=shipping</strong>?</p>
<p>In the USA there are chains of shops branded and operated by a particular shipping company (eg <a href="https://www.theupsstore.com">The UPS Store</a>) but there are thousands of independent shops that will offer customers various shipping choices such as FedEx, UPS, DHL, standard US Mail, and sometimes local couriers. Is there a way to tag which shipping services a shop offers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-post_office" rel="tag" title="see questions tagged &#39;post_office&#39;">post_office</span> <span class="post-tag tag-link-dhl" rel="tag" title="see questions tagged &#39;dhl&#39;">dhl</span> <span class="post-tag tag-link-ups" rel="tag" title="see questions tagged &#39;ups&#39;">ups</span> <span class="post-tag tag-link-shipping" rel="tag" title="see questions tagged &#39;shipping&#39;">shipping</span> <span class="post-tag tag-link-fedex" rel="tag" title="see questions tagged &#39;fedex&#39;">fedex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '18, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '18, 17:46</strong> </span></p>
</div>
</div>
<div id="comments-container-63326" class="comments-container">
&#10;</div>
<div id="comment-tools-63326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63326-form-container" class="comment-form-container">
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

<span id="63412"></span>

<div id="answer-container-63412" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63412-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After some pondering and querying, I've come to the conclusion that it's better not to use <strong>amenity=post_offce</strong> for these shipping stores. One clear reason for me is that the tagging on post offices is so inconsistent that there would be no reliable way to distinguish USPS post offices from shipping stores tagged with <strong>amenity=post_office</strong>. I've gone with <strong>shop=shipping</strong>, which isn't on the wiki but seems to have a lot of use already.</p>
<p>Here's how I plan to tag a USP Store:<br />
<strong>name=The UPS Store<br />
brand=UPS<br />
shop=shipping<br />
shipping=UPS</strong></p>
<p>And an independent shipping shop:<br />
<strong>name=Shelly's Shipping Shop<br />
shop=shipping<br />
shipping=DHL;FedEx;UPS;USPS;courier<br />
mailbox_rental=yes</strong></p>
<p>I'll try to get around to writing a proper proposal when I get a chance...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '18, 02:12</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-63412" class="comments-container">
<span id="63423"></span>
<div id="comment-63423" class="comment">
<div id="post-63423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You ask a good question about how to tag the different postal/shipping services places offer, but using shop=shipping doesn't resolve that and (as you say) contradicts the wiki and current practice. 70 uses of shop=shipping is not very large, and even some of those seem to be companies shipping freight, not individual parcels</p>
</div>
<div id="comment-63423-info" class="comment-info">
<span class="comment-age">(11 May '18, 14:52)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="63428"></span>
<div id="comment-63428" class="comment">
<div id="post-63428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with much of the logic, degrading the meaning of post office would be detrimental for many uses of OSM. Thinking about the same issue, I would probably have chosen amenity=shipping_office or amenity=parcel_office (an old phrase now) to keep the relationship with post offices clearer.</p>
</div>
<div id="comment-63428-info" class="comment-info">
<span class="comment-age">(12 May '18, 14:13)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="64069"></span>
<div id="comment-64069" class="comment">
<div id="post-64069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As far as I can tell, shop=shipping does <em>not</em> contradict the wiki. Neither the post_office page nor the shop page addresses the issue at all. I found shop=shipping discussed on the talk page of the shop tag. It's not widely used, but it seems to be the best fit of what is in use.</p>
<p>The wiki's definition of shop is "A place selling retail products or services" and I feel these qualify. Certainly they feel like shops to me. Amenity would be fine too, but I feel that shop=shipping is succinct and clearer in meaning.</p>
<p>(A commercial freight shipping company should not be tagged shop=*, as it's not a retail service. Maybe office=shipping or industrial=shipping would be appropriate.)</p>
</div>
<div id="comment-64069-info" class="comment-info">
<span class="comment-age">(07 Jun '18, 00:25)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-63412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63412-form-container" class="comment-form-container">
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

