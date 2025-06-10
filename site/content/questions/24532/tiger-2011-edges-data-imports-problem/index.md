+++
type = "question"
title = "[closed] Tiger 2011 edges data imports problem"
description = '''Hi guys, I downloaded tiger 2011 edges data for USA map. After unziping them (about 3000 files), I used the following commands to import them: ./utils/imports.php --parse-tiger-2011 ../tiger2011 (the place where the files are) ./utils/setup.php --import-tiger-data It finished in a blink of eye and w...'''
date = "2013-07-24T14:31:00Z"
lastmod = "2015-07-23T06:40:00Z"
weight = 24532
keywords = [ "tiger", "nominatim" ]
aliases = [ "/questions/24532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Tiger 2011 edges data imports problem](/questions/24532/tiger-2011-edges-data-imports-problem)

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
<span id="post-24532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24532-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I downloaded tiger 2011 edges data for USA map. After unziping them (about 3000 files), I used the following commands to import them: ./utils/imports.php --parse-tiger-2011 ../tiger2011 (the place where the files are) ./utils/setup.php --import-tiger-data</p>
<p>It finished in a blink of eye and without telling me whether failed or succeeded, just showed some lines of CREATE TABLE, DROP TABLE. Since there are so many files, I doubt it did any change on nominatim database. I checked the database. It looked only one table related to tiger which is "location_property_tiger", and it is empty. So can someone tell me whether it succeeded or not, if not, how should I import tiger data correctly? The following is the detailed output I got (again, in less than a second):</p>
<hr />
<p>DROP TABLE</p>
<p>CREATE TABLE</p>
<p>CREATE FUNCTION</p>
<p>Creating indexes</p>
<p>CREATE INDEX</p>
<p>CREATE INDEX</p>
<p>GRANT</p>
<p>DROP TABLE</p>
<p>ALTER TABLE</p>
<p>ALTER INDEX</p>
<p>ALTER INDEX</p>
<p>DROP FUNCTION</p>
<hr />
<p>Thanks in advance! TJ</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '13, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Jul '13, 02:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24532" class="comments-container">
&#10;</div>
<div id="comment-tools-24532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24532-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is self-answered, "accepting" not possible - closing therefore." by aseerel4c26 25 Jul '13, 02:53

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24537"></span>

<div id="answer-container-24537" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24537-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never mind guys. I checked the imports.php. It seems looking for zip files instead of unzipped. But I moved zip files to somewhere else after unzipping. Silly me!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '13, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24537" class="comments-container">
<span id="44382"></span>
<div id="comment-44382" class="comment">
<div id="post-44382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi to all, I am also get the the same problem, even my zip files not moved to anywhere. Refer the following:</p>
<p>[sas@<em>.</em>.<em>.</em>~/Nominatim-2.2.0]$ php utils/imports.php --parse-tiger-2011 /home/sas/rajavelu/tigerdata/edges/</p>
<p>Processing 15005...</p>
<p>[sas@<em>.</em>.<em>.</em>~/Nominatim-2.2.0]$ php utils/setup.php --import-tiger- data</p>
<p>DROP TABLE CREATE TABLE CREATE FUNCTION /home/sas/Nominatim-2.2.0/data/tiger2011/15005.sql: Creating indexes CREATE INDEX CREATE INDEX GRANT DROP TABLE ALTER TABLE ALTER INDEX ALTER INDEX DROP FUNCTION [sas@<em>.</em>.<em>.</em>~/Nominatim-2.2.0]$</p>
</div>
<div id="comment-44382-info" class="comment-info">
<span class="comment-age">(23 Jul '15, 06:40)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-24537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24537-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

