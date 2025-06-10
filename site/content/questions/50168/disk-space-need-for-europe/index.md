+++
type = "question"
title = "Disk space need for Europe"
description = '''I installed Openstreetmap on EC2 machine, i read that the whole world need something like 300GB, the hole word compressed is 32GB and Europe is 16GB, so i set 350GB to avoid problems, unfortunately in the the last steps on importing data to db, the process fail with out of space error. I use this co...'''
date = "2016-06-13T08:07:00Z"
lastmod = "2016-06-20T12:42:00Z"
weight = 50168
keywords = [ "rendering", "disk_usage", "tileserver" ]
aliases = [ "/questions/50168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disk space need for Europe](/questions/50168/disk-space-need-for-europe)

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
<span id="post-50168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed Openstreetmap on EC2 machine, i read that the whole world need something like 300GB, the hole word compressed is 32GB and Europe is 16GB, so i set 350GB to avoid problems, unfortunately in the the last steps on importing data to db, the process fail with out of space error. I use this command to extract:</p>
<p>sudo -u postgres osm2pgsql --append --database gis --slim -C 12000 /usr/local/share/maps/planet/europe-latest.osm.pbf</p>
<p>Did anyone set openstreetmaps maps and can tail how mach disk space i need for Europe ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '16, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/dbcda0aee716cc45f3ce2564ac7a54ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_N&#39;s gravatar image" />
<p><span>H_N</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_N has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '16, 19:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50168" class="comments-container">
<span id="50169"></span>
<div id="comment-50169" class="comment">
<div id="post-50169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim? Tile server? Overpass server...?</p>
</div>
<div id="comment-50169-info" class="comment-info">
<span class="comment-age">(13 Jun '16, 08:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="50170"></span>
<div id="comment-50170" class="comment">
<div id="post-50170-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> Mod_tile, renderd, mapnik, osm2pgsql and a postgresql/postgis database</p>
</div>
<div id="comment-50170-info" class="comment-info">
<span class="comment-age">(13 Jun '16, 08:18)</span> <span class="comment-user userinfo">H_N</span>
</div>
</div>
<span id="50318"></span>
<div id="comment-50318" class="comment">
<div id="post-50318-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suspect that, compared to what you've read, all bets are off once you specify "--append". I'd be very surprised if many people have tried appending Europe to whatever database they currently have.</p>
<p>It's also worth mentioning that people do keep mapping things, which means that the database keeps getting bigger. What might have fitted on a certain size of machine once won't any more.</p>
</div>
<div id="comment-50318-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 17:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50168-form-container" class="comment-form-container">
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

<span id="50326"></span>

<div id="answer-container-50326" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50326-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried in(16.6.2016) on difirrant disks:</p>
<ul>
<li>The first try 300 GB stop on no more space error.</li>
<li>The second try 350 GB also stop on no more space error.</li>
<li>Finally in the third try i succeed i put the disk on 400 GB, but in this try i also add the drop flag.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '16, 04:02</strong></p>
<img src="https://secure.gravatar.com/avatar/dbcda0aee716cc45f3ce2564ac7a54ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_N&#39;s gravatar image" />
<p><span>H_N</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_N has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '16, 12:15</strong> </span></p>
</div>
</div>
<div id="comments-container-50326" class="comments-container">
<span id="50327"></span>
<div id="comment-50327" class="comment">
<div id="post-50327-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How much free space is left? Bear SomeoneElse's comment in mind. The required disk space will increase with further updates, better leave some room or you will run into the same problem again.</p>
</div>
<div id="comment-50327-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 07:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50332"></span>
<div id="comment-50332" class="comment">
<div id="post-50332-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In the middle of the loading(sm2pgsql --append...) it reached 362GB(maximum).</p>
<p>After finish loading all Europe, disk usage is 110GB(include OS and 16GB compressed Europe).</p>
</div>
<div id="comment-50332-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 12:34)</span> <span class="comment-user userinfo">H_N</span>
</div>
</div>
<span id="50333"></span>
<div id="comment-50333" class="comment">
<div id="post-50333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Needing 3 times as much disk space during load compared to afterwards is due to "append" I think. I don't see that when I load without --append (I'd run out of space if I did).</p>
</div>
<div id="comment-50333-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 12:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50326-form-container" class="comment-form-container">
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

