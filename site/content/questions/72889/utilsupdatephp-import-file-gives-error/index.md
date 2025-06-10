+++
type = "question"
title = "./utils/update.php --import-file gives error"
description = '''Hello Everyone,  I have successfully installed The Nominatim and the Postgresql db on my server. During the setup I imported the following dataset: kenya-latest.osm.pbf I now wanted to add the following dataset: nigeria-latest.osm.bz2 I was given the impression I could do it with the following comma...'''
date = "2020-02-06T13:49:00Z"
lastmod = "2020-03-15T19:25:00Z"
weight = 72889
keywords = [ "nominatim", "postgresql", "ubuntu" ]
aliases = [ "/questions/72889" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [./utils/update.php --import-file gives error](/questions/72889/utilsupdatephp-import-file-gives-error)

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
<span id="post-72889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72889-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone, I have successfully installed The Nominatim and the Postgresql db on my server. During the setup I imported the following dataset:</p>
<p>kenya-latest.osm.pbf</p>
<p>I now wanted to add the following dataset:</p>
<p>nigeria-latest.osm.bz2</p>
<p>I was given the impression I could do it with the following command:</p>
<p>./utils/update.php --import-file nigeria-latest.osm.bz2</p>
<p>but it is throwing the following error:</p>
<p>DB writer thread failed due to ERROR: Executing SQL ERROR: Error from osm2pgsql, 2</p>
<p>string(24) "Error from osm2pgsql, 2</p>
<p>I have tried googling but I have not found anything that could point out what was wrong. Please suggestions on how to fix the issue will be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '20, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c90b2bba1514cbd750b8fadf7e90b3da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imonike&#39;s gravatar image" />
<p><span>imonike</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imonike has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-72889" class="comments-container">
&#10;</div>
<div id="comment-tools-72889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72889-form-container" class="comment-form-container">
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

<span id="72891"></span>

<div id="answer-container-72891" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72891-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>update.php</code> is for incremental data updates in <a href="https://wiki.openstreetmap.org/wiki/OsmChange">https://wiki.openstreetmap.org/wiki/OsmChange</a> format only. See <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/diffs">https://wiki.openstreetmap.org/wiki/Planet.osm/diffs</a> for an explanation. It's useful for keeping Kenya up-to-date, but you can't use it to add a new country/region.</p>
<p>For importing two countries you need to first merge the files kenya+nigeria, then import. In your case that means first deleting the database and starting again.</p>
<p>See <a href="https://help.openstreetmap.org/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim">https://help.openstreetmap.org/questions/48843/merging-two-or-more-geographical-areas-to-import-two-or-more-osm-files-in-nominatim</a> and <a href="http://nominatim.org/release-docs/latest/admin/Faq/#can-i-import-multiple-countries-and-keep-them-up-to-date">http://nominatim.org/release-docs/latest/admin/Faq/#can-i-import-multiple-countries-and-keep-them-up-to-date</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '20, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72891" class="comments-container">
<span id="72893"></span>
<div id="comment-72893" class="comment">
<div id="post-72893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much. I guess I start again. Is there a maximum to the number of datasets I can merge?</p>
</div>
<div id="comment-72893-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 14:54)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
<span id="72894"></span>
<div id="comment-72894" class="comment">
<div id="post-72894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many people install the whole world, so only hardware (size of your harddrive) is the limit.</p>
</div>
<div id="comment-72894-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 14:57)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="72895"></span>
<div id="comment-72895" class="comment">
<div id="post-72895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. You have been a great help.</p>
</div>
<div id="comment-72895-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 15:08)</span> <span class="comment-user userinfo">imonike</span>
</div>
</div>
</div>
<div id="comment-tools-72891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72891-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73525"></span>

<div id="answer-container-73525" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73525-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not show my address</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '20, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e695cc6632e53e6dc169f6ca5cdfac24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AR%20FURNITURE&#39;s gravatar image" />
<p><span>AR FURNITURE</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AR FURNITURE has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73525" class="comments-container">
<span id="73532"></span>
<div id="comment-73532" class="comment">
<div id="post-73532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/239/artur-k">@ar</a>-furniture: please post a new question ("ask a question" on the top right hand corner of this page) describing exactly what you need help with. Your post here will be removed since you posted it as an answer to a totally unrelated question.</p>
</div>
<div id="comment-73532-info" class="comment-info">
<span class="comment-age">(15 Mar '20, 19:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-73525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73525-form-container" class="comment-form-container">
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

