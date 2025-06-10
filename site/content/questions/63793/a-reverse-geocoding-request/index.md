+++
type = "question"
title = "a reverse geocoding request"
description = '''Good afternoon! What types of address components can contain a response to a reverse geocoding request? A complete list of types is required. What other types besides these: house_number road village town city county postcode country country_code Thank you in advance!'''
date = "2018-05-28T13:28:00Z"
lastmod = "2018-05-29T08:05:00Z"
weight = 63793
keywords = [ "reversegeocoding", "reverse" ]
aliases = [ "/questions/63793" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [a reverse geocoding request](/questions/63793/a-reverse-geocoding-request)

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
<span id="post-63793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63793-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good afternoon! What types of address components can contain a response to a reverse geocoding request? A complete list of types is required.</p>
<p>What other types besides these: house_number road village town city county postcode country country_code</p>
<p>Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '18, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5269774c1e533a68b8ea2ce63efafb88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Helen%20Kir&#39;s gravatar image" />
<p><span>Helen Kir</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Helen Kir has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '18, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-63793" class="comments-container">
&#10;</div>
<div id="comment-tools-63793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63793-form-container" class="comment-form-container">
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

<span id="63796"></span>

<div id="answer-container-63796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63796-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The full list is in the <code>getClassTypes</code> method in <a href="https://github.com/openstreetmap/Nominatim/blob/master/lib/lib.php">https://github.com/openstreetmap/Nominatim/blob/master/lib/lib.php</a> - look for the <code>Label</code> keys.</p>
<p>A better list is <a href="https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml">https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml</a> Anything not in this file you can treat as a name of a place, e.g. name of a restaurant, building name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '18, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '18, 16:34</strong> </span></p>
</div>
</div>
<div id="comments-container-63796" class="comments-container">
<span id="63798"></span>
<div id="comment-63798" class="comment">
<div id="post-63798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for such a prompt reply!</p>
<p>Unfortunately, I can not see the document: <a href="https://github.com/openstreetmap/Nominatim/blob/master/lib/lib.php,">https://github.com/openstreetmap/Nominatim/blob/master/lib/lib.php,</a> since I do not have access to Github.</p>
<p>How can I access?</p>
<p>Maybe you also know, how are the types of address components and administrative divisions request correlated?</p>
</div>
<div id="comment-63798-info" class="comment-info">
<span class="comment-age">(28 May '18, 14:44)</span> <span class="comment-user userinfo">Helen Kir</span>
</div>
</div>
<span id="63799"></span>
<div id="comment-63799" class="comment not_top_scorer">
<div id="post-63799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15179/helen-kir"></a><a href="https://help.openstreetmap.org/users/15179/helen-kir">@Helen Kir</a> Unfortunately you're going to struggle with OSM software more generally if you don't have access to github. Is that a technical problem at your end that you can resolve, some sort of political issue, or something else?</p>
</div>
<div id="comment-63799-info" class="comment-info">
<span class="comment-age">(28 May '18, 14:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63803"></span>
<div id="comment-63803" class="comment not_top_scorer">
<div id="post-63803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Our company only plans to use OSM for reverse geocoding.</p>
<p>I have only read open information: <a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a> I do not know about the obligatory access to the Github.</p>
<p>We will need to generate separate address parameters from the geocoding response.</p>
</div>
<div id="comment-63803-info" class="comment-info">
<span class="comment-age">(28 May '18, 15:27)</span> <span class="comment-user userinfo">Helen Kir</span>
</div>
</div>
<span id="63805"></span>
<div id="comment-63805" class="comment">
<div id="post-63805-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to make sure - have you seen <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> ?</p>
</div>
<div id="comment-63805-info" class="comment-info">
<span class="comment-age">(28 May '18, 15:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63807"></span>
<div id="comment-63807" class="comment">
<div id="post-63807-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Most likely we will install our own copy Nominatim.</p>
</div>
<div id="comment-63807-info" class="comment-info">
<span class="comment-age">(28 May '18, 15:54)</span> <span class="comment-user userinfo">Helen Kir</span>
</div>
</div>
<span id="63808"></span>
<div id="comment-63808" class="comment">
<div id="post-63808-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You don't need a GitHub account to view the document. Just remove the trailing comma from the URL.</p>
</div>
<div id="comment-63808-info" class="comment-info">
<span class="comment-age">(28 May '18, 16:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="63809"></span>
<div id="comment-63809" class="comment not_top_scorer">
<div id="post-63809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks scai, I edited my answer and removed the comma</p>
</div>
<div id="comment-63809-info" class="comment-info">
<span class="comment-age">(28 May '18, 16:35)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="63811"></span>
<div id="comment-63811" class="comment not_top_scorer">
<div id="post-63811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, how simple, thanks!</p>
<p>The local version of Nominatim allows you to refine the query using addressdetails = [0 | 1] (Include a breakdown of the address into elements)?</p>
</div>
<div id="comment-63811-info" class="comment-info">
<span class="comment-age">(28 May '18, 17:26)</span> <span class="comment-user userinfo">Helen Kir</span>
</div>
</div>
<span id="63812"></span>
<div id="comment-63812" class="comment">
<div id="post-63812-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, it will. Example: <a href="https://nominatim.openstreetmap.org/search.php?q=university%20ave,%20palo%20alto&amp;polygon_geojson=1&amp;viewbox=&amp;format=jsonv2&amp;addressdetails=1">https://nominatim.openstreetmap.org/search.php?q=university%20ave,%20palo%20alto&amp;polygon_geojson=1&amp;viewbox=&amp;format=jsonv2&amp;addressdetails=1</a></p>
</div>
<div id="comment-63812-info" class="comment-info">
<span class="comment-age">(28 May '18, 17:29)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="63828"></span>
<div id="comment-63828" class="comment not_top_scorer">
<div id="post-63828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all for your help!</p>
</div>
<div id="comment-63828-info" class="comment-info">
<span class="comment-age">(29 May '18, 08:05)</span> <span class="comment-user userinfo">Helen Kir</span>
</div>
</div>
</div>
<div id="comment-tools-63796" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63796-form-container" class="comment-form-container">
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

