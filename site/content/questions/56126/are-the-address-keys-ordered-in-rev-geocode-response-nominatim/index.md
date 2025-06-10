+++
type = "question"
title = "Are the address keys ordered in rev geocode response? [nominatim]"
description = '''When performing a reverse geocode in nominatim the response consists of address jsonObject, are the keys in this json ordered based on the address hierarchy ? Eg: http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;limit=1&amp;amp;lat=12.8441574&amp;amp;lon=80.0599055 This responds with display name ...'''
date = "2017-05-11T14:50:00Z"
lastmod = "2017-05-11T15:42:00Z"
weight = 56126
keywords = [ "nominatim" ]
aliases = [ "/questions/56126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Are the address keys ordered in rev geocode response? \[nominatim\]](/questions/56126/are-the-address-keys-ordered-in-rev-geocode-response-nominatim)

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
<span id="post-56126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When performing a reverse geocode in nominatim the response consists of address jsonObject, are the keys in this json ordered based on the address hierarchy ?</p>
<p>Eg: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;limit=1&amp;lat=12.8441574&amp;lon=80.0599055">http://nominatim.openstreetmap.org/reverse?format=json&amp;limit=1&amp;lat=12.8441574&amp;lon=80.0599055</a></p>
<p>This responds with display name : "display_name":"D3 Guduvancheri Police Station, Grand Southern Trunk Road, Guduvancheri, Potheri, Kanchipuram district, Tamil Nadu, 603202, India"</p>
<p>The address json is : "address":{"police":"D3 Guduvancheri Police Station","road":"Grand Southern Trunk Road","suburb":"Guduvancheri","village":"Potheri","state_district":"Kanchipuram district","state":"Tamil Nadu","postcode":"603202","country":"India","country_code":"in"}</p>
<p>I see the order is preserved. I wanted to know if this can be assumed to work with any input, i.e is this the intended way?</p>
<p>Thanks in advance for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '17, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56126" class="comments-container">
&#10;</div>
<div id="comment-tools-56126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56126-form-container" class="comment-form-container">
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

<span id="56128"></span>

<div id="answer-container-56128" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56128-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's more coincidence since PHP's hash table implementation keeps the order of elements when inserted (<a href="http://nikic.github.io/2014/12/22/PHPs-new-hashtable-implementation.html)">http://nikic.github.io/2014/12/22/PHPs-new-hashtable-implementation.html)</a> and not guaranteed.</p>
<p>If you want to order the elements you can have a look at this list of keys <a href="https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml">https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml</a> (where anything not in the list should go in the first position)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '17, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-56128" class="comments-container">
&#10;</div>
<div id="comment-tools-56128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56128-form-container" class="comment-form-container">
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

