+++
type = "question"
title = "Compile errors installing Nominatim"
description = '''I am trying to install Nominatim from its source on github. PostgreSQL 9.1 and PostGIS 2 has already been installed using yum. The system is running CentOS 6.3 with cPanel. git clone --recursive https://github.com/twain47/Nominatim.git cd Nominatim ./autogen.sh  Problem: This is when the error occur...'''
date = "2012-09-10T06:13:00Z"
lastmod = "2012-09-10T06:13:00Z"
weight = 15926
keywords = [ "nominatim", "postgresql", "postgis", "linux" ]
aliases = [ "/questions/15926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compile errors installing Nominatim](/questions/15926/compile-errors-installing-nominatim)

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
<span id="post-15926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to install Nominatim from its source on <a href="https://github.com/twain47/Nominatim">github</a>. PostgreSQL 9.1 and PostGIS 2 has already been installed using <code>yum</code>. The system is running CentOS 6.3 with cPanel.</p>
<pre><code>git clone --recursive https://github.com/twain47/Nominatim.git
cd Nominatim
./autogen.sh</code></pre>
<p><strong>Problem:</strong> This is when the error occurs as shown below. Any suggestions/idea how this can be fixed? Thanks!!!</p>
<pre><code>autoreconf: Entering directory `.&#39;
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal -I osm2pgsql/m4 --output=aclocal.m4t
/usr/share/automake-1.11/Automake/ChannelDefs.pm line 23:
&#10;This Perl hasn&#39;t been configured and built properly for the threads
module to work.  (The &#39;useithreads&#39; configuration option hasn&#39;t been used.)
&#10;Having threads support requires all of Perl and all of the XS modules in
the Perl installation to be rebuilt, it is not just a question of adding
the threads module.  (In other words, threaded and non-threaded Perls
are binary incompatible.)
&#10;If you want to the use the threads module, please contact the people
who built your Perl.
&#10;Cannot continue, aborting.
BEGIN failed--compilation aborted at /usr/local/lib/perl5/5.8.8/i686-linux/threads.pm line 28.
Compilation failed in require at /usr/share/automake-1.11/Automake/ChannelDefs.pm line 23.
BEGIN failed--compilation aborted at /usr/share/automake-1.11/Automake/ChannelDefs.pm line 26.
Compilation failed in require at /usr/share/automake-1.11/Automake/Configure_ac.pm line 26.
BEGIN failed--compilation aborted at /usr/share/automake-1.11/Automake/Configure_ac.pm line 26.
Compilation failed in require at /usr/bin/aclocal line 39.
BEGIN failed--compilation aborted at /usr/bin/aclocal line 39.
autoreconf: aclocal failed with exit status: 255</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '12, 06:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9a7101fe3ba50e621e91ee1edf9d27bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyxynyx&#39;s gravatar image" />
<p><span>nyxynyx</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyxynyx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15926" class="comments-container">
&#10;</div>
<div id="comment-tools-15926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15926-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

