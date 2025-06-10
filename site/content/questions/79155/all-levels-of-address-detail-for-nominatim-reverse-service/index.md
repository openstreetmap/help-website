+++
type = "question"
title = "All levels of address detail for Nominatim reverse service"
description = '''In the documentation for the reverse service of Nominatim I just see partly some levels of the address. I see some other parts further in the example for geojson. zoom address detail 3 country 5 state 8 county 10 city 14 suburb 16 major streets 17 major and minor streets 18 building  What are the 18...'''
date = "2021-03-07T13:45:00Z"
lastmod = "2021-03-07T15:05:00Z"
weight = 79155
keywords = [ "nominatim" ]
aliases = [ "/questions/79155" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [All levels of address detail for Nominatim reverse service](/questions/79155/all-levels-of-address-detail-for-nominatim-reverse-service)

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
<span id="post-79155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the <a href="https://nominatim.org/release-docs/develop/api/Reverse/#result-limitation">documentation</a> for the reverse service of Nominatim I just see partly some levels of the address. I see some other parts further in the <a href="https://nominatim.org/release-docs/develop/api/Reverse/#example-with-formatgeojson">example for geojson</a>.</p>
<pre><code>zoom    address detail
3   country
5   state
8   county
10  city
14  suburb
16  major streets
17  major and minor streets
18  building</code></pre>
<p>What are the 18 levels of details for the address field, when we use the reverse API of Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '21, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/af81b55e4f9bd063e59e2a4e54bb5496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jo%C3%A3o&#39;s gravatar image" />
<p><span>João</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="João has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '21, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-79155" class="comments-container">
&#10;</div>
<div id="comment-tools-79155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79155-form-container" class="comment-form-container">
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

<span id="79156"></span>

<div id="answer-container-79156" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79156-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-79156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="João has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The other levels have no names. From the source code at <a href="https://github.com/osm-search/nominatim-ui/blob/master/src/lib/helpers.js#L129">https://github.com/osm-search/nominatim-ui/blob/master/src/lib/helpers.js#L129</a></p>
<p><code>const aZoomLevels = [ /* 0 */ 'Continent / Sea', /* 1 */ '', /* 2 */ '', /* 3 */ 'Country', /* 4 */ '', /* 5 */ 'State', /* 6 */ 'Region', /* 7 */ '', /* 8 */ 'County', /* 9 */ '', /* 10 */ 'City', /* 11 */ '', /* 12 */ 'Town / Village', /* 13 */ '', /* 14 */ 'Suburb', /* 15 */ '', /* 16 */ 'Street', /* 17 */ '', /* 18 */ 'Building', /* 19 */ '', /* 20 */ '', /* 21 */ '' ];</code></p>
<p>The number 1-18 are used because those are map zoom level. Map zoom 0,1,2 usually show the whole world (depending on size of the monitor), while 18 was the maximum zoom on the OpenStreetMap. These days the maximun zoom is 21.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '21, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-79156" class="comments-container">
<span id="79158"></span>
<div id="comment-79158" class="comment">
<div id="post-79158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, but I need to know what are really the exact object fields, such as seen <a href="https://nominatim.org/release-docs/develop/api/Reverse/#example-with-formatgeojson">here</a>. For example <code>house_number</code>, <code>road</code>, <code>county</code>, etc.</p>
</div>
<div id="comment-79158-info" class="comment-info">
<span class="comment-age">(07 Mar '21, 14:09)</span> <span class="comment-user userinfo">João</span>
</div>
</div>
<span id="79160"></span>
<div id="comment-79160" class="comment">
<div id="post-79160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Address levels for ranking are a bit more complex (<a href="https://nominatim.org/release-docs/develop/develop/Ranking/).">https://nominatim.org/release-docs/develop/develop/Ranking/).</a> <a href="https://github.com/osm-search/Nominatim/blob/master/settings/address-levels.json">https://github.com/osm-search/Nominatim/blob/master/settings/address-levels.json</a> lists the most common but they're mapped to different ranks depending on country. <a href="https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml">https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml</a> lists more, and still that list isn't complete because OpenStreetMap data can contain every tag, a restaurant will have the field name 'restaurant', too, so there is likely over 1000 possible field names. The components.yaml covers the most common, usually everything else can be seen as the name of a place.</p>
</div>
<div id="comment-79160-info" class="comment-info">
<span class="comment-age">(07 Mar '21, 14:16)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="79163"></span>
<div id="comment-79163" class="comment">
<div id="post-79163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Related Nominatim FAQ entry <a href="https://nominatim.org/release-docs/latest/api/Output/#addressdetails">https://nominatim.org/release-docs/latest/api/Output/#addressdetails</a></p>
</div>
<div id="comment-79163-info" class="comment-info">
<span class="comment-age">(07 Mar '21, 15:05)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-79156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79156-form-container" class="comment-form-container">
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

