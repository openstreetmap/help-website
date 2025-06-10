+++
type = "question"
title = "Calculate bbox from current gps position"
description = '''Hello,  My question is perhaps simple but I&#x27;m beginning in GIS development.  I want to query all nodes with a specific attribute set around my device, all I know is my current GPS position.  For example, I want to find all nodes in a radius of 300 meters around me. I think I have to create a boundin...'''
date = "2013-01-29T17:16:00Z"
lastmod = "2013-01-30T12:38:00Z"
weight = 19421
keywords = [ "bounding", "overpass", "development" ]
aliases = [ "/questions/19421" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate bbox from current gps position](/questions/19421/calculate-bbox-from-current-gps-position)

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
<span id="post-19421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19421-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>My question is perhaps simple but I'm beginning in GIS development. I want to query all nodes with a specific attribute set around my device, all I know is my current GPS position.</p>
<p>For example, I want to find all nodes in a radius of 300 meters around me. I think I have to create a bounding box with coordinates matching this circle of 300 meters but I wanna know if a service exists in the api to create this box or if not, what is the formula I can use.</p>
<p>My known input parameters are the current position location (coordinates) and the radius in which I want to query and I want the list of all availables nodes or at least the coordinates of the bounding box suitable for overpass api queries.</p>
<p>Thanks in advance,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '13, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/b024c177304cc72662d35c9a2374a180?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fievel&#39;s gravatar image" />
<p><span>fievel</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fievel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19421" class="comments-container">
&#10;</div>
<div id="comment-tools-19421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19421-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="19436"></span>

<div id="answer-container-19436" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19436-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "great circle" distance between two points on the Earth's surface can be calculated using the <a href="https://en.wikipedia.org/wiki/Haversine_formula">Haversine Formula</a>. There may well be an implementation of that available to you in whatever toolkit you're using.</p>
<p>If not (or if it looks too complicated), and if you're only interested in a small area (say around your local city) then you could just cheat and use whatever longitude-to-metres conversion works at your latitude (just measure it) to ensure that your BBOX is big enough to return all of the data that you might be interested in.</p>
<p>Obviously a bounding box is by its very nature rectangular rather than circular, so if "within 300m" is an exact requirement rather than just a way of saying "fairly close" you'll need to do some calculations with the data that you get back.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '13, 11:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19436" class="comments-container">
<span id="19438"></span>
<div id="comment-19438" class="comment">
<div id="post-19438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will check for the formula, thanks. For your last remark, I'm conscious about that, in fact I think the bounding box will be something like the smallest square englobing the circle of 300m radius from my location.</p>
</div>
<div id="comment-19438-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 11:41)</span> <span class="comment-user userinfo">fievel</span>
</div>
</div>
</div>
<div id="comment-tools-19436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19436-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19444"></span>

<div id="answer-container-19444" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19444-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think this is related to this : <a href="http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters">http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '13, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b024c177304cc72662d35c9a2374a180?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fievel&#39;s gravatar image" />
<p><span>fievel</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fievel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19444" class="comments-container">
&#10;</div>
<div id="comment-tools-19444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19444-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19434"></span>

<div id="answer-container-19434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you have seen this recent question and you also want do it in an app. The wiki as quite a lot of info reguarding bounding boxes,tiles and zoom levels. have you looked carefully at that? <a href="https://help.openstreetmap.org/questions/19227/find-coordinates-of-bounding-box">https://help.openstreetmap.org/questions/19227/find-coordinates-of-bounding-box</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '13, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-19434" class="comments-container">
<span id="19435"></span>
<div id="comment-19435" class="comment">
<div id="post-19435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well that's not exactly the same problem because he have the map, I don't want to display the map at all, just find nodes that are interesting to me around my position.</p>
</div>
<div id="comment-19435-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 11:28)</span> <span class="comment-user userinfo">fievel</span>
</div>
</div>
</div>
<div id="comment-tools-19434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19434-form-container" class="comment-form-container">
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

