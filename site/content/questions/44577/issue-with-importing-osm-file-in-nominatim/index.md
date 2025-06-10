+++
type = "question"
title = "Issue with Importing osm-file in Nominatim"
description = '''Hello, We are getting the following error while importing OSM data during the installation of Nominatim on Centos 6.6 cPanel server: -- ./utils/setup.php --osm-file india-latest.osm.pbf --all --osm2pgsql-cache 18000 Create DB  Strict Standards: Non-static method PEAR::isError() should not be called ...'''
date = "2015-08-01T02:00:00Z"
lastmod = "2015-08-03T15:29:00Z"
weight = 44577
keywords = [ "import", "nominatim", "osm", "error" ]
aliases = [ "/questions/44577" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Issue with Importing osm-file in Nominatim](/questions/44577/issue-with-importing-osm-file-in-nominatim)

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
<span id="post-44577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44577-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We are getting the following error while importing OSM data during the installation of Nominatim on Centos 6.6 cPanel server:</p>
<p>--</p>
<h1 id="utilssetup.php---osm-file-india-latest.osm.pbf---all---osm2pgsql-cache-18000">./utils/setup.php --osm-file india-latest.osm.pbf --all --osm2pgsql-cache 18000</h1>
<p>Create DB<br />
<strong>Strict Standards</strong>: Non-static method PEAR::isError() should not be called statically in <strong>/home/fleetlink/public_html/Nominatim/utils/setup.php</strong> on line <strong>96</strong><br />
Password: createdb: database creation failed: ERROR: permission denied to create database Error executing external command: createdb -E UTF-8 -p 5432 nominatim --</p>
<p>Can any one please let us know how to resolve?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '15, 02:00</strong></p>
<img src="https://secure.gravatar.com/avatar/200527a878b092a0076b529cf7469019?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wizztechs&#39;s gravatar image" />
<p><span>wizztechs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wizztechs has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-44577" class="comments-container">
&#10;</div>
<div id="comment-tools-44577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44577-form-container" class="comment-form-container">
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

<span id="44580"></span>

<div id="answer-container-44580" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure you followed the instructions correctly, particularly</p>
<blockquote>
<p><strong>Creating the importer account</strong></p>
<p>The import needs to be done with a postgres superuser with the same name as the account doing the import. You can create such a postgres superuser account by running:</p>
<pre><code>sudo -u postgres createuser -s [your user name]</code></pre>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '15, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44580" class="comments-container">
<span id="44596"></span>
<div id="comment-44596" class="comment">
<div id="post-44596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik, Could you please give more enlighten help for this error? Would like also to see a solution for this type of errors.</p>
<p>Thank you.</p>
</div>
<div id="comment-44596-info" class="comment-info">
<span class="comment-age">(03 Aug '15, 15:29)</span> <span class="comment-user userinfo">gregosmartinez</span>
</div>
</div>
</div>
<div id="comment-tools-44580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44580-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44581"></span>

<div id="answer-container-44581" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this has been already done, but still no success.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '15, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/200527a878b092a0076b529cf7469019?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wizztechs&#39;s gravatar image" />
<p><span>wizztechs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wizztechs has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '15, 15:13</strong> </span></p>
</div>
</div>
<div id="comments-container-44581" class="comments-container">
&#10;</div>
<div id="comment-tools-44581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44581-form-container" class="comment-form-container">
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

