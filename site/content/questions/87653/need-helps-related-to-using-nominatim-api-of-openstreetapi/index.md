+++
type = "question"
title = "Need helps related to using Nominatim API of OpenStreetAPI"
description = '''Hello. I hope you are doing well. I encountered some problems with using Nominatim API and I need your help. I hope you kindly help me. The issues are the following. Now I have almost 50000 records related to Country, State and City data of the United States. Using this data, I should get all polygo...'''
date = "2023-08-11T15:01:00Z"
lastmod = "2023-08-11T16:14:00Z"
weight = 87653
keywords = [ "nominatim", "database" ]
aliases = [ "/questions/87653" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Need helps related to using Nominatim API of OpenStreetAPI](/questions/87653/need-helps-related-to-using-nominatim-api-of-openstreetapi)

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
<span id="post-87653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87653-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I hope you are doing well. I encountered some problems with using Nominatim API and I need your help. I hope you kindly help me.</p>
<p>The issues are the following. Now I have almost 50000 records related to Country, State and City data of the United States. Using this data, I should get all polygon data of these regions and store the polygon data to my local database. So I used Nominatim API repeatedly for getting all polygon data but there are some problems. After calling Nominatim API 20 times, I can't get any result from Nominatim API. Could you kindly let me know the reason of this issue? Also, I would be very happy if you kindly let me know how to implement this issue.</p>
<p>On the other hand, I should make a CRON job for updating all polygon data for all regions in the United States. So I would be happy if you kindly let me know the best way how to implement this CRON job, too.</p>
<p>Looking forward to hearing from you. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '23, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e16b56a5bb50491bf075ad415052f696?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shinydev&#39;s gravatar image" />
<p><span>shinydev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shinydev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87653" class="comments-container">
&#10;</div>
<div id="comment-tools-87653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87653-form-container" class="comment-form-container">
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

<span id="87654"></span>

<div id="answer-container-87654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87654-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Make sure you adhere to the usage guidelines <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> You should probably install your own server or use a third party (usually paid) service. 500.000 API requests to fill your database seems like a lot.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '23, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-87654" class="comments-container">
&#10;</div>
<div id="comment-tools-87654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87655"></span>

<div id="answer-container-87655" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Agree with <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>, get an OSM data file and load it into a PostGIS database and then you can extract all the polygons you want in a batch job rather than having to rely on a third-party, donation-funded free service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '23, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87655" class="comments-container">
<span id="87656"></span>
<div id="comment-87656" class="comment">
<div id="post-87656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I get an OSM data file for all my records?</p>
</div>
<div id="comment-87656-info" class="comment-info">
<span class="comment-age">(11 Aug '23, 15:44)</span> <span class="comment-user userinfo">shinydev</span>
</div>
</div>
<span id="87657"></span>
<div id="comment-87657" class="comment">
<div id="post-87657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can download a world-wide data file from planet.openstreetmap.org or one that covers e.g. just the US from download.geofabrik.de. After that you'll be using the free osm2pgsql utility to load the data into a PostGIS database from where you can then use standard SQL statements to select/export various polygons on different administrative levels.</p>
</div>
<div id="comment-87657-info" class="comment-info">
<span class="comment-age">(11 Aug '23, 15:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="87658"></span>
<div id="comment-87658" class="comment">
<div id="post-87658-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you kindly let me know if there is a way for using MySQL, not PostgreSQL?</p>
</div>
<div id="comment-87658-info" class="comment-info">
<span class="comment-age">(11 Aug '23, 16:14)</span> <span class="comment-user userinfo">shinydev</span>
</div>
</div>
</div>
<div id="comment-tools-87655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87655-form-container" class="comment-form-container">
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

