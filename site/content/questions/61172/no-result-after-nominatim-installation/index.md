+++
type = "question"
title = "No result after nominatim installation"
description = '''Hello, I&#x27;m trying to setup a nominatim server like https://nominatim.openstreetmap.org/ but something is going wrong. SCOPE:  Have a nominatim server with all the planet indexed, a copy of nominatim.openstreetmap.org SOFTWARE: RHEL 7 64bit PostgreSQL 9.6 Postigis 2.4 PHP 5.4.16 gcc-c++-4.8.5-16 libg...'''
date = "2017-12-13T14:04:00Z"
lastmod = "2018-01-23T18:27:00Z"
weight = 61172
keywords = [ "nominatim" ]
aliases = [ "/questions/61172" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No result after nominatim installation](/questions/61172/no-result-after-nominatim-installation)

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
<span id="post-61172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm trying to setup a nominatim server like <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a> but something is going wrong.</p>
<p><strong>SCOPE:</strong> Have a nominatim server with all the planet indexed, a copy of nominatim.openstreetmap.org</p>
<p><strong>SOFTWARE:</strong></p>
<pre><code>RHEL 7 64bit
PostgreSQL 9.6
Postigis 2.4
PHP 5.4.16
gcc-c++-4.8.5-16
libgcc-4.8.5-16
cpp-4.8.5-16
gcc-4.8.5-16
libgcc-4.8.5-16</code></pre>
<p><strong>HARDWARE:</strong></p>
<pre><code>32CPUs
64GB RAM
590GB storage</code></pre>
<p>Trying to install the version 3.0.1 of Nominatim I'm having some difficulties to index all the planet. I've followed the steps in the documentation <a href="http://nominatim.org/release-docs/3.0.1/Install-on-Centos-7.html">http://nominatim.org/release-docs/3.0.1/Install-on-Centos-7.html</a> and the compiler doesn't report any error.</p>
<p>List of main attempt:</p>
<ul>
<li><strong>First Attempt:</strong> I've imported the Central america region by using the setup command ./utils/setup.php --osm-file /data/nominatim/Nominatim-3.0.1/data/central-america-latest.osm.bz2 --all --osm2pgsql-cache 38000 2&gt;&amp;1 | tee setup.log The import was a success! Searching for central america region the result appear as expected. So I decided to import the Australia using the update command ./utils/update.php --import-file /data/nominatim/Nominatim-3.0.1/data/australia-oceania-latest.osm.bz2 --osm2pgsql-cache 38000 &amp;&gt; australia.log Unfortunately after the import, searching for "Perth" or other Australian city, the result was empty. I've also tried the command /utils/update.php --index --index-instances 30 but the result was the same</li>
<li><strong>Second Attempt:</strong> Removing the database I've imported the Antartica. After the import it works as expected, so I decided to import the Australia (again) but nothing. I've tried different times with different options but it was always a failure.</li>
<li><strong>Third Attempt:</strong> After many imports I decided to import directly all the planet (<a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-latest.osm.pbf)">http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-latest.osm.pbf)</a> with the setup script like the first attempt. The import miserably fails :(</li>
</ul>
<p>I'm struggling to have a nominatim server up and running but I've no clue how to solve this issue.</p>
<p>I'm doing the importing in some step wrong? I've to do other command or step after the import?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '17, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/b8b4cc76687a4bce35cf6aaf5720e102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="v0id_&#39;s gravatar image" />
<p><span>v0id_</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="v0id_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61172" class="comments-container">
<span id="61174"></span>
<div id="comment-61174" class="comment">
<div id="post-61174-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If importing one country works, then your setup is pretty complete. Best if you delete the database before trying another import. You say for the full planet it fails. Do you see any error messages? In which step and how long after starting the import does it fail? Does the Postgresql server logfiles show any errors?</p>
</div>
<div id="comment-61174-info" class="comment-info">
<span class="comment-age">(13 Dec '17, 19:51)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="61777"></span>
<div id="comment-61777" class="comment">
<div id="post-61777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you resolved the problem? I too have the same case as yours. I am not able to search any. It gives me no result.</p>
</div>
<div id="comment-61777-info" class="comment-info">
<span class="comment-age">(23 Jan '18, 17:17)</span> <span class="comment-user userinfo">swiftkey</span>
</div>
</div>
<span id="61779"></span>
<div id="comment-61779" class="comment">
<div id="post-61779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Swiftkey: the user never answered so we were unable to help. Please post any error messages, the query you run and output you see and if you see warnings in the postgresql or webserver logfiles as a new question on either help.openstreetmap.org or preferably <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a></p>
</div>
<div id="comment-61779-info" class="comment-info">
<span class="comment-age">(23 Jan '18, 18:27)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-61172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61172-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

