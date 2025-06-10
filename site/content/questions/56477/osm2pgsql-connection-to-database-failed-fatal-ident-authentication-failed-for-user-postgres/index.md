+++
type = "question"
title = "osm2pgsql  Connection to database failed: FATAL:  Ident authentication failed for user &quot;postgres&quot;"
description = '''I have been trying to installed on centos 7 the osm map. I have followed this link http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c.  I tried to modify the last command and run this  osm2pgsql -c -d osm -U postgres -H localhost -S /usr/local/share/osm2pgsql/default.style malaysia-singapore-brune...'''
date = "2017-06-06T20:22:00Z"
lastmod = "2017-06-08T13:15:00Z"
weight = 56477
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/56477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql Connection to database failed: FATAL: Ident authentication failed for user "postgres"](/questions/56477/osm2pgsql-connection-to-database-failed-fatal-ident-authentication-failed-for-user-postgres)

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
<span id="post-56477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to installed on centos 7 the osm map. I have followed this link <a href="http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c.">http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c.</a></p>
<p>I tried to modify the last command and run this</p>
<pre><code>osm2pgsql -c -d osm -U postgres -H localhost -S /usr/local/share/osm2pgsql/default.style malaysia-singapore-brunei-latest.osm.bz2
osm2pgsql version 0.93.0-dev (64 bit id space)
&#10;Using built-in tag processing pipeline
Using projection SRS 3857 (Spherical Mercator)
Osm2pgsql failed due to ERROR: Connection to database failed: FATAL:  Ident authentication failed for user &quot;postgres&quot;</code></pre>
<p>When I ran this command sudo -u postgres psql postgres</p>
<pre><code>psql (9.6.3)
Type &quot;help&quot; for help.
&#10;This works perfectly.</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '17, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56477" class="comments-container">
<span id="56486"></span>
<div id="comment-56486" class="comment">
<div id="post-56486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have resolved this using this method osm2pgsql --slim -S /usr/local/share/osm2pgsql/default.style -d gis -C 1000 malaysia-singapore-brunei-latest.osm.bz2. I just had to lower the cache size and it started to work.</p>
</div>
<div id="comment-56486-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 03:51)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56529"></span>
<div id="comment-56529" class="comment">
<div id="post-56529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whilst I doubt that "authentication failed" would be fixed by changing the cache size, it's good that you've got this working!</p>
</div>
<div id="comment-56529-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 13:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

