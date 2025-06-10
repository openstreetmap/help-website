+++
type = "question"
title = "Why do I get the wrong city name from Nominatim?"
description = '''I am using a java library which uses Nominatim to extract the city names for a given latitude and longitude. I am looking for Node with id 108042 but I get &quot;London Borough of Camden&quot; as the city which is wrong. I am wondering why it happens. I even tried this link to ensure that the problem is not w...'''
date = "2020-06-02T10:05:00Z"
lastmod = "2020-06-02T11:23:00Z"
weight = 75089
keywords = [ "nominatim", "cityname" ]
aliases = [ "/questions/75089" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why do I get the wrong city name from Nominatim?](/questions/75089/why-do-i-get-the-wrong-city-name-from-nominatim)

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
<span id="post-75089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using a java <a href="https://www.daniel-braun.com/technik/reverse-geocoding-library-for-java/">library</a> which uses Nominatim to extract the city names for a given latitude and longitude. I am looking for Node with id 108042 but I get "London Borough of Camden" as the city which is wrong. I am wondering why it happens.</p>
<p>I even tried <a href="https://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=51.5235613&amp;lon=-0.1355134&amp;zoom=18&amp;addressdetails=1">this link</a> to ensure that the problem is not with the third party library that I am using but it also gives me the same information.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-cityname" rel="tag" title="see questions tagged &#39;cityname&#39;">cityname</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '20, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/971716cd3434ffdc38817bc0b4bf61ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anika%20H&#39;s gravatar image" />
<p><span>Anika H</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anika H has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75089" class="comments-container">
&#10;</div>
<div id="comment-tools-75089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75089-form-container" class="comment-form-container">
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

<span id="75093"></span>

<div id="answer-container-75093" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75093-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-75093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Anika H has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative</a> lists what admin_level values represent in different countries. Look for United Kingdom and <code>admin_level=8</code>.</p>
<p>London is so big, everything moves up a level. London is tagged <code>admin_level=6</code> (in the rest of the country that would be a district/county). The level below (boroughs) are tagged <code>admin_level=8</code> (in the rest of the country that would be a city). Bouroughs are so big and self-administering they another two levels of boroughs/neighborhoods/suburbs of their own. Paris and their 20 arrodissimonts are similar and I believe New York City.</p>
<p>"London consists of a collection of boroughs, two of which are Cities. They are not towns" That's City of Westminster and City of London.</p>
<p>Nominatim currently can't set different labels based on region, here: inside London. You'd have to identify London (maybe by postcode) and apply that.</p>
<p><a href="https://nominatim.openstreetmap.org/details.php?osmtype=N&amp;osmid=108042">https://nominatim.openstreetmap.org/details.php?osmtype=N&amp;osmid=108042</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '20, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75093" class="comments-container">
&#10;</div>
<div id="comment-tools-75093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75093-form-container" class="comment-form-container">
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

