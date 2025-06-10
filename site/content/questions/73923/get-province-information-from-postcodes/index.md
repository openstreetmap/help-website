+++
type = "question"
title = "Get Province information from postcodes"
description = '''Hi! I have some postcodes and I want to et the following information: city, province and region. I did the following query using Nominatim: loca = geocode(query = row[&#x27;CAP&#x27;], country_codes = country, addressdetails = True, language = &#x27;it,en&#x27;) To retrieve the city I found out that there can be varoiu...'''
date = "2020-04-01T13:47:00Z"
lastmod = "2020-04-01T15:21:00Z"
weight = 73923
keywords = [ "python", "province", "nominatim", "geopy", "city" ]
aliases = [ "/questions/73923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get Province information from postcodes](/questions/73923/get-province-information-from-postcodes)

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
<span id="post-73923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I have some postcodes and I want to et the following information: city, province and region.</p>
<p>I did the following query using Nominatim: <code>loca = geocode(query = row['CAP'], country_codes = country, addressdetails = True, language = 'it,en')</code></p>
<p>To retrieve the city I found out that there can be varoius information in the addressdetails: loca.raw['address']['city'], loca.raw['address']['hamlet'], loca.raw['address']['village']. To retrieve the region I found out that the information is stored in loca.raw['address']['state']. For the province I have found the information under loca.raw['address']['county'], but it is not always correct.</p>
<p>I'll make you an example: postcode 47122, it is a city in Italy, province Forlì. When I search this postcode in nominatim.openstreetmap I get this result:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Immagine_0kGFmbe.png" alt="alt text" /></p>
<p>So my question is: Is this workflow correct or there are better ways to retrieve city, province and region? How can I get a more detailed address that includes all the information I need?</p>
<p>Thanks, Carlotta.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-province" rel="tag" title="see questions tagged &#39;province&#39;">province</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geopy" rel="tag" title="see questions tagged &#39;geopy&#39;">geopy</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '20, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/dba77ed68b48f13134f0ade205307d59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlotta&#39;s gravatar image" />
<p><span>Carlotta</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlotta has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73923" class="comments-container">
&#10;</div>
<div id="comment-tools-73923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73923-form-container" class="comment-form-container">
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

<span id="73924"></span>

<div id="answer-container-73924" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73924-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, that's the approach.</p>
<p>In the response a place <code>admin_level=6</code> becomes <code>['address']['county']</code>. The details.php page shows 'province' because the relation <a href="https://www.openstreetmap.org/relation/42609,">https://www.openstreetmap.org/relation/42609,</a> or rather the linked node <a href="https://www.openstreetmap.org/node/4404418359">https://www.openstreetmap.org/node/4404418359</a> because Nominatim merges them into one in its database, has a <code>place=province</code> tag. Getting province disabled on the details.php is relative new, I think since last week.</p>
<p><a href="https://wiki.openstreetmap.org/w/index.php?title=Tag:boundary%3Dadministrative&amp;uselang=en-US">https://wiki.openstreetmap.org/w/index.php?title=Tag:boundary%3Dadministrative&amp;uselang=en-US</a> shows what admin_level numbers mean in the various countries. In Italy 6 it is provinces.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '20, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-73924" class="comments-container">
<span id="73925"></span>
<div id="comment-73925" class="comment">
<div id="post-73925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! So to have the province detail I need to specify boundary=administrative + admin_level=6 in the geocode?</p>
<p>Thanks again, Carlotta.</p>
</div>
<div id="comment-73925-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 14:16)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
<span id="73926"></span>
<div id="comment-73926" class="comment">
<div id="post-73926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not clear which software library you use. Check its documentation or <a href="http://nominatim.org/release-docs/latest/api/Search/">http://nominatim.org/release-docs/latest/api/Search/</a> for possible parameters/filters. To get the details about a province you'd need to search for the province name.</p>
</div>
<div id="comment-73926-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 15:17)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="73927"></span>
<div id="comment-73927" class="comment">
<div id="post-73927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I haven't specified that! I am using Geopy Nominatim in python. I tried to search for documentation on it, but I haven't found anything useful yet.</p>
</div>
<div id="comment-73927-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 15:21)</span> <span class="comment-user userinfo">Carlotta</span>
</div>
</div>
</div>
<div id="comment-tools-73924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73924-form-container" class="comment-form-container">
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

