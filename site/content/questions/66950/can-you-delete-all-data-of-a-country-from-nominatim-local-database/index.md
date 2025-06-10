+++
type = "question"
title = "Can you delete all data of a country from Nominatim local database?"
description = '''I was able to succesfully install Nominatim locally and now want to get all the data for addresses and cities using it. The problem is i don&#x27;t have have enough space to hold a large quantity of data for multiple countries. So i want to import a data, get all the information I need and then delete it...'''
date = "2018-11-28T07:56:00Z"
lastmod = "2018-11-28T12:02:00Z"
weight = 66950
keywords = [ "data", "nominatim", "osm", "remove", "delete" ]
aliases = [ "/questions/66950" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can you delete all data of a country from Nominatim local database?](/questions/66950/can-you-delete-all-data-of-a-country-from-nominatim-local-database)

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
<span id="post-66950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66950-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was able to succesfully install Nominatim locally and now want to get all the data for addresses and cities using it. The problem is i don't have have enough space to hold a large quantity of data for multiple countries. So i want to import a data, get all the information I need and then delete it and import new data. I know you can update the database with new data using update.php.</p>
<p>So is there a safe clean way to delete data of a country?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '18, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/031f394153cdfa809dc58e042d919c25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muntean%20Octavian&#39;s gravatar image" />
<p><span>Muntean Octa...</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muntean Octavian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66950" class="comments-container">
&#10;</div>
<div id="comment-tools-66950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66950-form-container" class="comment-form-container">
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

<span id="66962"></span>

<div id="answer-container-66962" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66962-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Muntean Octavian has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Data is split in 300 tables. It's easier to delete the postgresql database and import the next country.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '18, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-66962" class="comments-container">
&#10;</div>
<div id="comment-tools-66962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66962-form-container" class="comment-form-container">
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

