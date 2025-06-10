+++
type = "question"
title = "Is this considered Derivative Data?"
description = '''We are planning to use OSM but the licensing seems to be very complicated. I have read through several documents but unfortunately its still unclear if we will be producing derivative data which needs to be share. Some guidance would be greatlly appreciated by folks who are more experienced with OSM...'''
date = "2012-10-31T17:20:00Z"
lastmod = "2012-11-02T14:20:00Z"
weight = 17330
keywords = [ "derivative", "license" ]
aliases = [ "/questions/17330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is this considered Derivative Data?](/questions/17330/is-this-considered-derivative-data)

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
<span id="post-17330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17330-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are planning to use OSM but the licensing seems to be very complicated. I have read through several documents but unfortunately its still unclear if we will be producing derivative data which needs to be share. Some guidance would be greatlly appreciated by folks who are more experienced with OSM licensing.</p>
<p>We wish to show a Automotive Dealer, where their leads are originating from (geolocation) and which of those leads converted to sales (subset of leads). There are a few specific use cases where we will be leveraging OSM and so it would be great to know if we are producing derivative data under this circumstances:</p>
<p>1) We geocode addresses to lat/log and plot Leads, Sales and Car dealer locations. Does the leads and sales data need to be shared under the new licensing system?</p>
<p>2) Close Rate (#Sales/#Leads) for a dealership varies by the distance the leads are from the dealer. We want to show this relationship on a map by showing Concentric Circles (of avg close rates) with radius of 5, 10,15 miles from the dealership. Is this considered derivative data and does it need to be shared?</p>
<p>3) We want to acquire external data for zipcodes such as medium income, # of car per family and show that info on a map. Do we need to share this data with OSM?</p>
<p>Thanks in advance, Biren</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-derivative" rel="tag" title="see questions tagged &#39;derivative&#39;">derivative</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '12, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cb2210e98b28fbf96b5e9982c864aae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Biren&#39;s gravatar image" />
<p><span>Biren</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Biren has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17330" class="comments-container">
&#10;</div>
<div id="comment-tools-17330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17330-form-container" class="comment-form-container">
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

<span id="17337"></span>

<div id="answer-container-17337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17337-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to me that the question of derivative data might not be too relevant in your case.</p>
<p>Assuming for a moment that you <em>were</em> indeed creating a derivative database - which I'm not sure of - then this would mean that you have to offer the data under ODbL to the recipient of the "produced work". ODbL never requires sharing with the world - only that your data is available under ODbL to the recipient.</p>
<p>If I understand you correctly, then your clients will be the dealers whose business data you are visualizing; even if you had to make the data available to them, that would not affect your business since the dealers, while theoretically allowed to do so, would not have an interest to further distribute the data.</p>
<p>The "legal-talk" mailing list (lists.openstreetmap.org/listinfo/legal-talk) will probably yield more in-depth answers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '12, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17337" class="comments-container">
<span id="17414"></span>
<div id="comment-17414" class="comment">
<div id="post-17414-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>Thank you very much for providing some more clarity. Our legal team also reviewed the license document <a href="http://opendatacommons.org/licenses/odbl/1.0/">http://opendatacommons.org/licenses/odbl/1.0/</a> and come up with a similar conclusion.</p>
<p>Regards,</p>
<p>Biren</p>
</div>
<div id="comment-17414-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 14:20)</span> <span class="comment-user userinfo">Biren</span>
</div>
</div>
</div>
<div id="comment-tools-17337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17337-form-container" class="comment-form-container">
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

