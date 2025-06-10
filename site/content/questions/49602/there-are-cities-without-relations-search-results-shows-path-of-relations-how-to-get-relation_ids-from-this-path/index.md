+++
type = "question"
title = "There are cities without relations. &#x27;Search results&#x27; shows path of relations. How to get relation_ids from this path?"
description = '''Hello. There are cities without relations. &#x27;Search results&#x27; shows path of relations. How to get relation_ids from this path? For example I am looking for &#x27;Wislon&#x27;. In Search results I see City: &#x27;Wilson, Wilson County, North Carolina, United States of America&#x27;, ie Wilson is part of Wilson County and ...'''
date = "2016-05-06T22:42:00Z"
lastmod = "2016-05-07T13:22:00Z"
weight = 49602
keywords = [ "relations" ]
aliases = [ "/questions/49602" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [There are cities without relations. 'Search results' shows path of relations. How to get relation_ids from this path?](/questions/49602/there-are-cities-without-relations-search-results-shows-path-of-relations-how-to-get-relation_ids-from-this-path)

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
<span id="post-49602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>There are cities without relations. 'Search results' shows path of relations. How to get relation_ids from this path?</p>
<p>For example I am looking for 'Wislon'. In Search results I see City: 'Wilson, Wilson County, North Carolina, United States of America', ie Wilson is part of Wilson County and Wilson County is part of North Carolina and so on. If I go to the details of the city (click the link), at the bottom of the page I see there is no any relation.</p>
<p>How can I get relation_ids for Wilson County, North Carolina, United States of America? Usually I use <a href="http://www.openstreetmap.org/api/0.6/relation/">http://www.openstreetmap.org/api/0.6/relation/</a><strong><em>relation_id</em></strong>, but this is not the case.</p>
<p>As I can guess, this path is based on latitude\longitude of a place, and map\engine checks the next bigger territory untill the country level is reached. Is there any API call which I can use to get relation_ids of this tree? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '16, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1565cd50c70d1108a514e12877171c5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bear_ukraine&#39;s gravatar image" />
<p><span>bear_ukraine</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bear_ukraine has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '16, 22:53</strong> </span></p>
</div>
</div>
<div id="comments-container-49602" class="comments-container">
&#10;</div>
<div id="comment-tools-49602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49602-form-container" class="comment-form-container">
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

<span id="49603"></span>

<div id="answer-container-49603" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49603-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bear_ukraine has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The county relation is available:</p>
<p><a href="http://www.openstreetmap.org/relation/2528757">http://www.openstreetmap.org/relation/2528757</a></p>
<p>To obtain the county relation from another object, you could synthesize a coordinate for the object (maybe the center or use some method to select a child node) and use reverse geocoding to obtain the admin hierarchy for that point. Nominatim and Overpass API both have support for such queries:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding">http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '16, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-49603" class="comments-container">
<span id="49604"></span>
<div id="comment-49604" class="comment">
<div id="post-49604-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your information + some additional search + re-read few times Overpass API (lack of examples) and I have finally what I want :) Nominatim is cool thing, lots of example, but lack of functionality :)</p>
<p>Here is the example of the solution: <a href="http://overpass-api.de/api/interpreter?data=rel(4084902);%3E;is_in;out;">http://overpass-api.de/api/interpreter?data=rel(4084902);&gt;;is_in;out;</a></p>
<p>Also related info: <a href="http://help.openstreetmap.org/questions/20053/locating-an-osm-object-eg-finding-town-relation-name/20055">http://help.openstreetmap.org/questions/20053/locating-an-osm-object-eg-finding-town-relation-name/20055</a></p>
</div>
<div id="comment-49604-info" class="comment-info">
<span class="comment-age">(07 May '16, 00:11)</span> <span class="comment-user userinfo">bear_ukraine</span>
</div>
</div>
<span id="49605"></span>
<div id="comment-49605" class="comment">
<div id="post-49605-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Don't miss <a href="http://overpass-turbo.eu/">Overpass Turbo</a> when working Overpas API queries.</p>
</div>
<div id="comment-49605-info" class="comment-info">
<span class="comment-age">(07 May '16, 02:31)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-49603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49603-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49611"></span>

<div id="answer-container-49611" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49611-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alternatively, you could go to <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a>. Search for Wilson, pick the one you want, click on details and you get a page like <a href="http://nominatim.openstreetmap.org/details.php?place_id=144418235">http://nominatim.openstreetmap.org/details.php?place_id=144418235</a></p>
<p>On that page you will find all the links of the relations used by Nominatim to calculate the address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '16, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-49611" class="comments-container">
<span id="49612"></span>
<div id="comment-49612" class="comment">
<div id="post-49612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow. This method is also cool. Is there any way how can I get the data from details page via API?</p>
</div>
<div id="comment-49612-info" class="comment-info">
<span class="comment-age">(07 May '16, 13:22)</span> <span class="comment-user userinfo">bear_ukraine</span>
</div>
</div>
</div>
<div id="comment-tools-49611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49611-form-container" class="comment-form-container">
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

