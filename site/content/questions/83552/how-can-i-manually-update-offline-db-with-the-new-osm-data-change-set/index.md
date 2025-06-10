+++
type = "question"
title = "How can I manually update offline db with the new osm data change set"
description = '''I&#x27;ve built a working tile server from the switch2osm instructions.  Since the server has no internet access, I need to find a way to keep the data up to date.  I found many scripts/services that fetch the new data from osm and update the db automatically but since I have no internet connection they ...'''
date = "2022-02-22T14:21:00Z"
lastmod = "2022-02-22T14:32:00Z"
weight = 83552
keywords = [ "osm2pgsql", "offline", "postgres", "postgis", "update" ]
aliases = [ "/questions/83552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I manually update offline db with the new osm data change set](/questions/83552/how-can-i-manually-update-offline-db-with-the-new-osm-data-change-set)

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
<span id="post-83552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've built a working tile server from the switch2osm instructions.<br />
Since the server has no internet access, I need to find a way to keep the data up to date.<br />
I found many scripts/services that fetch the new data from osm and update the db automatically but since I have no internet connection they can not be used<br />
Is there any way to manually download the xml change set from internet access computer and update the db (<a href="https://planet.openstreetmap.org/planet/changesets-latest.osm.bz2)?">https://planet.openstreetmap.org/planet/changesets-latest.osm.bz2)?</a><br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '22, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/eecf99cd3ec710b9123fff32ade65c07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aviram-s&#39;s gravatar image" />
<p><span>aviram-s</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aviram-s has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '22, 14:26</strong> </span></p>
</div>
</div>
<div id="comments-container-83552" class="comments-container">
&#10;</div>
<div id="comment-tools-83552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83552-form-container" class="comment-form-container">
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

<span id="83553"></span>

<div id="answer-container-83553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have the wrong file - what you need is not the changeset file but a series of "diffs" from <a href="https://planet.openstreetmap.org/replication/">https://planet.openstreetmap.org/replication/</a> that cover the whole time from when you did the server setup to now.</p>
<p>The manual process is:</p>
<ul>
<li>download all files individually</li>
<li>optionally merge them into a larger file with <code>osmosis</code> or <code>osmium</code></li>
<li>copy the individual files or the combined file onto the tile server machine</li>
<li>apply the individual files or the combined file to your database with <code>osm2pgsql</code> using the exact same command line flags as on the initial import but use the <code>--append</code> flag instead of <code>--create</code> (which is the default)</li>
</ul>
<p>You could also use <code>osmosis</code> or <code>pyosmium-get-changes</code> to make this easier for you, as these tools have the option of saving their last replication state, so you could let them "download all since last time" and you would not have to go through the hassle of downloading individual files.</p>
<p>Note that updating with diffs only makes sense as long as your data is not older than three or four weeks; once your data is older than that, a full new import is faster than trying diff updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '22, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-83553" class="comments-container">
&#10;</div>
<div id="comment-tools-83553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83553-form-container" class="comment-form-container">
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

