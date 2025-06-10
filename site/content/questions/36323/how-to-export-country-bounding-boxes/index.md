+++
type = "question"
title = "How to export country bounding boxes"
description = '''Hi, I would like to use the OSM data in my application but I&#x27;m not sure if it is feasible in an easy way. I need to extract country bounding boxes. My use case looks like: user sends his coordinate to my app and the app should return a country name where the user is. The app must run in offline mode...'''
date = "2014-08-28T08:08:00Z"
lastmod = "2016-10-13T09:33:00Z"
weight = 36323
keywords = [ "boundaries", "country", "bbox" ]
aliases = [ "/questions/36323" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How to export country bounding boxes](/questions/36323/how-to-export-country-bounding-boxes)

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
<span id="post-36323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36323-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I would like to use the OSM data in my application but I'm not sure if it is feasible in an easy way.</p>
<p>I need to extract country bounding boxes. My use case looks like: user sends his coordinate to my app and the app should return a country name where the user is. The app must run in offline mode, so it's not possible to send request to the OSM. I know that bounding boxes do not give me very good accuracy, but I think it should be enough, because it's a trade off between accuracy and performance. If you have any hints or advices for me, I would be very grateful.</p>
<p>So my question is: Is it possible in an easy way to extract from the OSM country bounding boxes as a set of boxes for each country (including islands and other country areas)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '14, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7305943add5bf2447319eb4f07cf4229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisOPL&#39;s gravatar image" />
<p><span>ChrisOPL</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisOPL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36323" class="comments-container">
<span id="37198"></span>
<div id="comment-37198" class="comment">
<div id="post-37198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>[meta] Why am I not able to convert this answer to a comment to the first answer?? On other threads its works for me here!</p>
</div>
<div id="comment-37198-info" class="comment-info">
<span class="comment-age">(01 Oct '14, 17:00)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="37211"></span>
<div id="comment-37211" class="comment">
<div id="post-37211-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan75</a> Unfortunately OSQA has been updated recently and is now full of bugs ;( Converting answers to comments doesn't always work anymore.</p>
</div>
<div id="comment-37211-info" class="comment-info">
<span class="comment-age">(02 Oct '14, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36323-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="37196"></span>

<div id="answer-container-37196" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37196-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ChrisOPL has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This site <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> allows you to download all boundaries (countries, but also other admin levels) in a variety of formats. Is that what you are looking for ? Data is extracted from OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '14, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '17, 08:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-37196" class="comments-container">
<span id="37226"></span>
<div id="comment-37226" class="comment">
<div id="post-37226-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>yes, it looks good for me. Thank you very much!</p>
</div>
<div id="comment-37226-info" class="comment-info">
<span class="comment-age">(02 Oct '14, 16:38)</span> <span class="comment-user userinfo">ChrisOPL</span>
</div>
</div>
</div>
<div id="comment-tools-37196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37196-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36347"></span>

<div id="answer-container-36347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36347-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim returns the bounding box for relations in its XML output, for instance <a href="http://nominatim.openstreetmap.org/search?q=United+Kingdom&amp;format=xml">http://nominatim.openstreetmap.org/search?q=United+Kingdom&amp;format=xml</a>. You can make sure you’ve got the relation for the country as it will be tagged as <code>class="boundary" type="administrative"</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '14, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8d2104911958906e2105c27461780d2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wynndale&#39;s gravatar image" />
<p><span>Wynndale</span><br />
<span class="score" title="565 reputation points">565</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wynndale has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-36347" class="comments-container">
<span id="36365"></span>
<div id="comment-36365" class="comment">
<div id="post-36365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. You assumed that I have a country name. Unfortunately I'm looking for a solution where I have boundaries for all countries. It means that I need to extract all boundaries, because in my app I have to check if a user coordinate is inside a country.</p>
<p>One more thing here is that "United+Kingdom" query doesn't return for example islands of the UK.</p>
</div>
<div id="comment-36365-info" class="comment-info">
<span class="comment-age">(29 Aug '14, 16:20)</span> <span class="comment-user userinfo">ChrisOPL</span>
</div>
</div>
</div>
<div id="comment-tools-36347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36347-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37171"></span>

<div id="answer-container-37171" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37171-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does anyone know other solution than Wynndale wrote above? I tried to use data from <a href="http://www.naturalearthdata.com/">http://www.naturalearthdata.com/</a> but it is not good enough for me (e.g. there are missing islands).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '14, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7305943add5bf2447319eb4f07cf4229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisOPL&#39;s gravatar image" />
<p><span>ChrisOPL</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisOPL has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '14, 08:38</strong> </span></p>
</div>
</div>
<div id="comments-container-37171" class="comments-container">
&#10;</div>
<div id="comment-tools-37171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37171-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52524"></span>

<div id="answer-container-52524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can go to your database directly and query for country polygons like so</p>
<pre><code>SELECT name-&gt;&#39;name&#39; as name, geometry 
FROM placex 
WHERE class=&#39;boundary&#39; AND type=&#39;administrative&#39; AND admin_level=2;</code></pre>
<p>(This query will run for a while, add "LIMIT 5" or so to test it without waiting.)</p>
<p>This query returns multipolygons for the countries, but you could further refine the query to use something like</p>
<pre><code>SELECT ... st_astext(st_envelope((st_dump(geometry)).geom)</code></pre>
<p>which would then give you a series of bounding boxes for each country.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '16, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '16, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-52524" class="comments-container">
&#10;</div>
<div id="comment-tools-52524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52524-form-container" class="comment-form-container">
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

