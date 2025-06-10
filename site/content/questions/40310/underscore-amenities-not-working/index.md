+++
type = "question"
title = "Underscore Amenities Not Working"
description = '''Hello, I&#x27;m trying to locate the drinking_water amenity to no avail. When I run the following query: http://nominatim.openstreetmap.org/search?q=Washington+DC+[parking]&amp;amp;addressdetails=1&amp;amp;format=json&amp;amp;bounded=1 I have no problems. I get an actual response. However, upon running  http://nomin...'''
date = "2015-01-13T19:05:00Z"
lastmod = "2016-10-24T09:26:00Z"
weight = 40310
keywords = [ "query", "amenity", "nominatim" ]
aliases = [ "/questions/40310" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Underscore Amenities Not Working](/questions/40310/underscore-amenities-not-working)

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
<span id="post-40310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40310-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to locate the <code>drinking_water</code> amenity to no avail. When I run the following query:</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=Washington+DC+%5Bparking%5D&amp;addressdetails=1&amp;format=json&amp;bounded=1"></a><a href="http://nominatim.openstreetmap.org/search?q=Washington+DC+%5Bparking%5D&amp;addressdetails=1&amp;format=json&amp;bounded=1"><code>http://nominatim.openstreetmap.org/search?q=Washington+DC+[parking]&amp;addressdetails=1&amp;format=json&amp;bounded=1</code></a></p>
<p>I have no problems. I get an actual response. However, upon running</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=Washington+DC+%5Bparking%5D&amp;addressdetails=1&amp;format=json&amp;bounded=1"></a><a href="http://nominatim.openstreetmap.org/search?q=Washington+DC+%5Bdrinking_water%5D&amp;addressdetails=1&amp;format=json&amp;bounded=1"><code>http://nominatim.openstreetmap.org/search?q=Washington+DC+[drinking_water]&amp;addressdetails=1&amp;format=json&amp;bounded=1</code></a></p>
<p>I get no results. I've tried various other tags with underscores: <code>charging_station</code>, <code>car_rental</code>, etc. to no avail. Is there some trick I'm missing? I'd just like to be able to query for things with underscores.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '15, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcf754909ab6d8152e25fac2c53a0d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjkaufer&#39;s gravatar image" />
<p><span>mjkaufer</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjkaufer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40310" class="comments-container">
&#10;</div>
<div id="comment-tools-40310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40310-form-container" class="comment-form-container">
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

<span id="40313"></span>

<div id="answer-container-40313" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40313-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-40313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mjkaufer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try with space instead of the underscore, e.g. <a href="http://nominatim.openstreetmap.org/search?q=Washington+DC+%5Bdrinking%20water%5D&amp;addressdetails=1&amp;format=json&amp;bounded=1">this</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '15, 20:12</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '15, 20:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40313" class="comments-container">
<span id="40321"></span>
<div id="comment-40321" class="comment">
<div id="post-40321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. This should be updated in the wiki, as it's out of date and rather misleading...</p>
</div>
<div id="comment-40321-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 03:40)</span> <span class="comment-user userinfo">mjkaufer</span>
</div>
</div>
<span id="40329"></span>
<div id="comment-40329" class="comment">
<div id="post-40329-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Feel free to update the wiki yourself, anybody is allowed to edit it :)</p>
</div>
<div id="comment-40329-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 07:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40334"></span>
<div id="comment-40334" class="comment">
<div id="post-40334-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>What you type for nominatim is plain text, not tags. Then nominatim tries to convert some of key words into tags equivalence. This is called "special phrases" and is documented here in the wiki <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases</a></p>
</div>
<div id="comment-40334-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 09:31)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-40313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40313-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52626"></span>

<div id="answer-container-52626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Interesting, that your example is working. It does not work with [charging_station] or [charging station] or [charging+station], which is an amenity (not in the special phrases).</p>
<p>There is a station at<br />
49,9120536, 10,0017795 but the request</p>
<p><a href="http://nominatim.openstreetmap.org/?format=json&amp;addressdetails=1&amp;viewbox=9.95%2C49.86%2C10.04%2C49.94&amp;q=%5Bcharging_station%5D&amp;bounded=1">http://nominatim.openstreetmap.org/?format=json&amp;addressdetails=1&amp;viewbox=9.95%2C49.86%2C10.04%2C49.94&amp;q=[charging_station]&amp;bounded=1</a></p>
<p>does not return anything.</p>
<p>In my opinion the request should be valid according to the description <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters">here</a> (under "bounded"): charging_station is an amenity and bounded=1 with a viewbox allows the search for it.</p>
<p>At the same address as the charging station there is a fuel station, which is returned</p>
<p><a href="http://nominatim.openstreetmap.org/?format=json&amp;addressdetails=1&amp;viewbox=9.95%2C49.86%2C10.04%2C49.94&amp;q=%5Bfuel%5D&amp;bounded=1">http://nominatim.openstreetmap.org/?format=json&amp;addressdetails=1&amp;viewbox=9.95%2C49.86%2C10.04%2C49.94&amp;q=[fuel]&amp;bounded=1</a></p>
<p>Can anyone tell me, what is wrong?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '16, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-52626" class="comments-container">
<span id="52627"></span>
<div id="comment-52627" class="comment">
<div id="post-52627-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There aren't any special phrases for charging stations in the list that Pieren linked to, so I have to assume that Nominatim just won't search for charging stations.</p>
</div>
<div id="comment-52627-info" class="comment-info">
<span class="comment-age">(21 Oct '16, 16:39)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="52656"></span>
<div id="comment-52656" class="comment">
<div id="post-52656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. But then description is a bit misleading to me. I understand it as two different features (1) The search for special phrases, which are translated into amenities and (2) the search for amenities, if you use a bounding box and the 'bounded' property. Thanks anyway.</p>
</div>
<div id="comment-52656-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 07:21)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
<span id="52657"></span>
<div id="comment-52657" class="comment">
<div id="post-52657-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For everybody who is interested: After some more investigation after the hint from alester (thanks again) I finally found out the source for the special phrases: TheSpecial Phrases page in the Wiki (quite obvious and it looks like I missed that several times ). This lists are imported from time to time. I inserted charging station in English and German and as I have a self hosted Nominatim, I have initialized the skript by hand and now it is working.</p>
</div>
<div id="comment-52657-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 09:26)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
</div>
<div id="comment-tools-52626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52626-form-container" class="comment-form-container">
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

