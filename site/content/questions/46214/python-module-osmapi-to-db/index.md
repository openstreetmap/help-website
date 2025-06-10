+++
type = "question"
title = "Python Module OsmApi to DB"
description = '''Hello again, How can i use Python Module OsmApi to acess information an insert it on a Database (PostgreSQL). My idea was to access the tags of osm and make a conection betteween the id of the Osm to the id of the DB. For example (Node=&quot;123&quot;) to DB Id. Thank you again for all the help, Francisco Cos...'''
date = "2015-10-29T12:08:00Z"
lastmod = "2015-10-29T13:04:00Z"
weight = 46214
keywords = [ "newbie", "osmapi_python", "postgresql", "database" ]
aliases = [ "/questions/46214" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Python Module OsmApi to DB](/questions/46214/python-module-osmapi-to-db)

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
<span id="post-46214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello again,</p>
<p>How can i use Python Module OsmApi to acess information an insert it on a Database (PostgreSQL). My idea was to access the tags of osm and make a conection betteween the id of the Osm to the id of the DB. For example (Node="123") to DB Id.</p>
<p>Thank you again for all the help,</p>
<p>Francisco Costa</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '15, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/2d5201d8b00ecd21e515f37b627df3b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FrancisCosta&#39;s gravatar image" />
<p><span>FrancisCosta</span><br />
<span class="score" title="0 reputation points">0</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FrancisCosta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '17, 09:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46214" class="comments-container">
&#10;</div>
<div id="comment-tools-46214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46214-form-container" class="comment-form-container">
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

<span id="46216"></span>

<div id="answer-container-46216" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46216-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API accessed by the Python Module OsmApi is not meant to be an API for reading information from OSM; it is an editing API. If you want to extract information from OSM, process a planet file or data extract, or use the Overpass API. -- There are ready-made tools like osm2pgsql or imposm that will take an OSM data file and load it into a PostGIS database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '15, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46216" class="comments-container">
&#10;</div>
<div id="comment-tools-46216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46216-form-container" class="comment-form-container">
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

