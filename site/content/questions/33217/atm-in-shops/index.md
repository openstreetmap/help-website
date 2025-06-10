+++
type = "question"
title = "ATM in Shops"
description = '''What is the best way to map ATMs that are inside shops and consequentially only accessible during the shops opening hours?  Is it better to tag them with the shop eg shop=convenience, atm=yes, fee=yes or separately eg amenity=atm, fee=yes, note=atm is in shop I don&#x27;t know all the shop opening hours'''
date = "2014-05-16T02:08:00Z"
lastmod = "2014-05-18T01:39:00Z"
weight = 33217
keywords = [ "atm", "mapping" ]
aliases = [ "/questions/33217" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ATM in Shops](/questions/33217/atm-in-shops)

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
<span id="post-33217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33217-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to map ATMs that are inside shops and consequentially only accessible during the shops opening hours?</p>
<p>Is it better to tag them with the shop</p>
<p>eg shop=convenience, atm=yes, fee=yes</p>
<p>or separately</p>
<p>eg amenity=atm, fee=yes, note=atm is in shop</p>
<p>I don't know all the shop opening hours</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-atm" rel="tag" title="see questions tagged &#39;atm&#39;">atm</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '14, 02:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7c24812608179f09b4374b3231cfb750?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YoP&#39;s gravatar image" />
<p><span>YoP</span><br />
<span class="score" title="506 reputation points">506</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YoP has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '14, 02:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33217" class="comments-container">
&#10;</div>
<div id="comment-tools-33217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33217-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="33228"></span>

<div id="answer-container-33228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33228-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can tag either the whole building (shop=convenience atm=yes) or a separate node (amenity=atm).</p>
<ul>
<li>The first has the advantage of implicitly sharing the shop's opening times and being simpler to map.</li>
<li>The second has the advantage of showing the precise location (but remember that in-shop atms can often move at the shop manager's whim) and enabling micromaping of atm characteristics. But you'll have to map the opening times separately unless openinghours-using programs are more advanced than I think.</li>
<li>Puting a note doesn't help much data-wise. It's useful for mappers but not to a program or a simple user. You can tag 'opening_hours=unknown || "same as shop"' (keep the double-quotes in the value) for a more parser-friendly way to say the same thing.</li>
</ul>
<p>Also, don't tag fee=yes unless you need to pay just to get access to the atm. In my region you can use the atm without paying the shopkeeper, I imagine that's the usual case. Atm transaction fees are a different thing altogether, and would be very complicated to map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-33228" class="comments-container">
<span id="33253"></span>
<div id="comment-33253" class="comment">
<div id="post-33253-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fee=yes is a very important tag. Most ATMs are operated by the banks and are free to use, but those that are privately operated, as opposed to owned by banks, often charge.</p>
<p>Whilst including the actual fee is complicated as this will change, suggesting that we leave out the information a map user requires to avoid these machines is vital.</p>
<p>Are you perhaps confusing bank charges here?</p>
</div>
<div id="comment-33253-info" class="comment-info">
<span class="comment-age">(16 May '14, 23:10)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
<span id="33258"></span>
<div id="comment-33258" class="comment">
<div id="post-33258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://en.wikipedia.org/wiki/ATM_usage_fees">ATM usage fees</a> seem to be a regional thing, some countries don't have any.</p>
</div>
<div id="comment-33258-info" class="comment-info">
<span class="comment-age">(17 May '14, 08:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33263"></span>
<div id="comment-33263" class="comment">
<div id="post-33263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ATM fees depend on the combination of the ATM operator, whether you're abroad and where, your card operator, and the options subscribed on your bank account. There's just no way it can be mapped reliably in OSM.</p>
</div>
<div id="comment-33263-info" class="comment-info">
<span class="comment-age">(17 May '14, 13:00)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="33264"></span>
<div id="comment-33264" class="comment">
<div id="post-33264-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Some ATMs <em>always</em> have a fee; it's possible to accurately say fee=yes for those.</p>
</div>
<div id="comment-33264-info" class="comment-info">
<span class="comment-age">(17 May '14, 13:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33278"></span>
<div id="comment-33278" class="comment">
<div id="post-33278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Charges for for using your card abroad are bank charges, not ATM fees.</p>
<p>Certainly in the UK some ATMs, often those in small shops and pubs charge a fee to use them. Often GBP 1.75 or 2.50. These can certainly be mapped accurately in OSM.</p>
<p>In these cases the request to your bank has the fee added, to your request. Personally I would never use an ATM that charges, and certainly want to be able to select a free one and not waste time walking into a shop to find the charge and to then walk out again. And if I find one tag it so others don't waste their time too.</p>
</div>
<div id="comment-33278-info" class="comment-info">
<span class="comment-age">(18 May '14, 01:39)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
</div>
<div id="comment-tools-33228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33228-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33221"></span>

<div id="answer-container-33221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33221-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have tagged them by:</p>
<ol>
<li>Tracing the building outline</li>
<li>Tagging the building with the shop information</li>
<li>Adding a node inside the building outline and tagging it with the atm information.</li>
</ol>
<p>I suppose putting a note saying "atm is in shop" would be useful too but the only time I've done that is when the building is so new that I don't have OSM compatible satellite imagery to trace the outline. In that case I have two nodes side by side. One for the shop and the second for the atm with a note tag on the atm saying it is in the shop.</p>
<p>For what it is worth, I do the same thing as tagging for an atm as I do for tagging things like a Starbucks inside a grocery store.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '14, 03:42</strong> </span></p>
</div>
</div>
<div id="comments-container-33221" class="comments-container">
&#10;</div>
<div id="comment-tools-33221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33221-form-container" class="comment-form-container">
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

