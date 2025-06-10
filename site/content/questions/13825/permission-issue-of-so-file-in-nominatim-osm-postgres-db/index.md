+++
type = "question"
title = "Permission issue of .so file in Nominatim osm postgres DB"
description = '''I am following the steps as described in http://wiki.openstreetmap.org/wiki/Nominatim/Installation to install the nominatim osm db on my own server. I need to create some functions before doing  ./utils/setup.php &amp;lt;my-planet-file&amp;gt; --load-data  So to create those functions I am running this comm...'''
date = "2012-06-27T07:24:00Z"
lastmod = "2016-01-06T12:06:00Z"
weight = 13825
keywords = [ "function", "nominatim", "osm", "postgres" ]
aliases = [ "/questions/13825" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Permission issue of .so file in Nominatim osm postgres DB](/questions/13825/permission-issue-of-so-file-in-nominatim-osm-postgres-db)

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
<span id="post-13825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13825-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am following the steps as described in <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> to install the nominatim osm db on my own server. I need to create some functions before doing</p>
<p><code>./utils/setup.php &lt;my-planet-file&gt; --load-data</code></p>
<p>So to create those functions I am running this command:</p>
<pre><code>./utils/setup.php --create-functions</code></pre>
<p>But, it gives me following error:</p>
<pre><code>Error in query: ERROR: could not access file &quot;/home/nominati/public_html/Nominatim/module/nominatim.so&quot;: Permission denied</code></pre>
<p>As I can see error occurs while running the following query:</p>
<pre><code>CREATE OR REPLACE FUNCTION transliteration(text) RETURNS text  AS &#39;/home/nominati/public_html/Nominatim/module/nominatim.so&#39;, &#39;transliteration&#39; LANGUAGE c IMMUTABLE STRICT;</code></pre>
<p>I am running the commands with root user and nominatim.so file owner is also root. I already changed the file owner to postgres and tried but the same error is there. Please guide what to do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '12, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13825" class="comments-container">
&#10;</div>
<div id="comment-tools-13825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13825-form-container" class="comment-form-container">
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

<span id="13828"></span>

<div id="answer-container-13828" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13828-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ravi Kotwani has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found on <a href="http://www.postgresql.org/docs/8.3/static/xfunc-c.html">postgreSQL doc</a>:</p>
<p>"The user ID the PostgreSQL server runs as must be able to traverse the path to the file you intend to load. Making the file or a higher-level directory not readable and/or not executable by the postgres user is a common mistake."</p>
<p>If the full path is reachable, perhaps you need the 'executable' flag on the .so file as well (chmod +x)...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '12, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13828" class="comments-container">
<span id="13833"></span>
<div id="comment-13833" class="comment">
<div id="post-13833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have already applied the 777 permission to module folder (Directory of .so file). And owner of nominatim.so file is root, I have also already tried it by changing the owner (chown) as postgres, nominatim and etc. But still facing the same problem? Is it a way I can delete this nominatim.so file and get new one with some easy steps?</p>
</div>
<div id="comment-13833-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 10:49)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="13834"></span>
<div id="comment-13834" class="comment">
<div id="post-13834-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You need to check the permissions not just of the directory, but of the directory's parent, and that directories parent, and... etc.</p>
<p>They all need to be accessible by which ever user you are running postgresql as.</p>
<p>To confirm if this is the case it maybe be helpful to switch to the postgres user and attempt to access the nominatim.so file using the full path. i.e.</p>
<p>su -l postgres ls -alh /home/user/path/path/nominatim.so</p>
</div>
<div id="comment-13834-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 10:51)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="13835"></span>
<div id="comment-13835" class="comment">
<div id="post-13835-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yeah, and don't forget the execution permission flag on the .so file itself. Rebuilding the .so file is not your current problem since postgreSQL is even not able to access the file.</p>
</div>
<div id="comment-13835-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 10:59)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="13839"></span>
<div id="comment-13839" class="comment">
<div id="post-13839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Twain</span>: Thanks for guiding, I just checked the owner of parent -&gt; parent -&gt; parent etc. and set the parent directory permission same as you told and its working fine now. Thanks.</p>
</div>
<div id="comment-13839-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 12:05)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="47391"></span>
<div id="comment-47391" class="comment">
<div id="post-47391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had the same problem. I checked all privileges and they were ok. I restarted postgres (/usr/bin/pg_ctl stop|start) and then it worked.</p>
</div>
<div id="comment-47391-info" class="comment-info">
<span class="comment-age">(06 Jan '16, 12:06)</span> <span class="comment-user userinfo">dusiema</span>
</div>
</div>
</div>
<div id="comment-tools-13828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13828-form-container" class="comment-form-container">
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

