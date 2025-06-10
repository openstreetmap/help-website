+++
type = "question"
title = "Import OSM file in MySQL on a Windows system (using PHP, maybe?)"
description = '''Hello, I have read all the documentation on osmosis and after that I tryed to import the OSM file into a MySQL database. It seems that I receive a lot of errors and I think that the database structure I am using is not complete, so there are conflicts even if I am am using &quot; validateSchemaVersion = ...'''
date = "2012-07-11T21:37:00Z"
lastmod = "2012-07-11T22:31:00Z"
weight = 14198
keywords = [ "php", "osmosis", "mysql" ]
aliases = [ "/questions/14198" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import OSM file in MySQL on a Windows system (using PHP, maybe?)](/questions/14198/import-osm-file-in-mysql-on-a-windows-system-using-php-maybe)

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
<span id="post-14198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
<br />
I have read all the documentation on osmosis and after that I tryed to import the OSM file into a MySQL database. It seems that I receive a lot of errors and I think that the database structure I am using is not complete, so there are conflicts even if I am am using " validateSchemaVersion = no".<br />
<br />
I tryed to use --write-mysql as well as --write-apidb but non of those worked.<br />
<br />
So, can someone tell me step by step how can I import the OSM file to a mysql database? I read something about some PHP scripts that can do this. Where can I find one of those scripts???<br />
<br />
<br />
Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/aeb7b59188c6d4ab1846362547839eb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandru&#39;s gravatar image" />
<p><span>Alexandru</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandru has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-14198" class="comments-container">
&#10;</div>
<div id="comment-tools-14198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14198-form-container" class="comment-form-container">
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

<span id="14200"></span>

<div id="answer-container-14200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The big question here is what do you want to do with the data? How do you want to get the data out of the database?</p>
<p>There are countless ways of importing and storing osm data in a database. Osmosis is able to read and write the deprecated MySql scheme that was used by the old website and editing api. If you are interesting in doing that for nostalgic reasons you can install an old version of the rails port that supported the MySql schema and then use osmosis to import the data to that. You can check out the old versions at <a href="http://git.openstreetmap.org/rails.git/tree/fb7f01b13cf57798b70ad13a62e5cace1074186b">git.osm.org</a>. That will give you a website that is like you would get if you visited www.osm.org in early 2009.</p>
<p>After some searching I have found some php classes that can deal with the osm editing api, for instance <a href="https://github.com/kenguest/Services_Openstreetmap/">Services_OpenStreetMap</a>. However that is an api for editors and have nothing with any databases (except the core database that powers the api).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 23:09</strong> </span></p>
</div>
</div>
<div id="comments-container-14200" class="comments-container">
&#10;</div>
<div id="comment-tools-14200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14200-form-container" class="comment-form-container">
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

