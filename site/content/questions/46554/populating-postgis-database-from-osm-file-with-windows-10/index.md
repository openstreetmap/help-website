+++
type = "question"
title = "Populating postgis database from osm file with windows 10"
description = '''Hello everyone. I have Windows 10 64bit installed on my pc. I want If i try to use  osm2pgsql.exe d:&#92;osm&#92;germany-filtered.osm -d osm -U postgres -P 5432 -S d:&#92;osm&#92;default.style --hstore --keep-coastlines  in the 32bit version it works for a while and then i get the error: Reading in file: d:&#92;osm&#92;ger...'''
date = "2015-11-12T20:40:00Z"
lastmod = "2015-11-13T10:40:00Z"
weight = 46554
keywords = [ "postgresql", "osm2pgsql" ]
aliases = [ "/questions/46554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Populating postgis database from osm file with windows 10](/questions/46554/populating-postgis-database-from-osm-file-with-windows-10)

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
<span id="post-46554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone. I have Windows 10 64bit installed on my pc. I want If i try to use</p>
<pre><code>osm2pgsql.exe d:\osm\germany-filtered.osm -d osm -U postgres -P 5432 -S d:\osm\default.style --hstore --keep-coastlines</code></pre>
<p>in the 32bit version it works for a while and then i get the error:</p>
<pre><code>Reading in file: d:\osm\germany-filtered.osm
Processing: Node(52420k 213.1k/s) Way(0k 0.00k/s) Relation(0 0.00/s)
Node cache size is too small to fit all nodes. Please increase cache size
Error occurred, cleaning up</code></pre>
<p>if i use 64bit and/or the -s switch, my Windows shows me a huge red banner that says that the app can't be executed on this pc and i should contact the software developer.</p>
<p>If i use the cygwin version i get the error:</p>
<pre><code>  0 [main] osm2pgsql 4576 find_fast_cwd: WARNING: Couldn&#39;t compute FAST_CWD pointer.  Please     report this problem to
the public mailing list cygwin@cygwin.com
osm2pgsql SVN version 0.83.0 (64bit id space)
&#10;Error: Connection to database failed: could not connect to server: No such file or directory
    Is the server running locally and accepting
    connections on Unix domain socket &quot;/tmp/.s.PGSQL.5432&quot;?</code></pre>
<p>Starting cmd.exe as an administrator delivers the same results.</p>
<p>How do i import my osm file into my postgrsql database for further usage?</p>
<p>Btw, i can't send the error to cygwin@cygwin.com because apparently my mail client sends as text/html and their server only accepts plain text -.-</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '15, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '15, 20:43</strong> </span></p>
</div>
</div>
<div id="comments-container-46554" class="comments-container">
<span id="46555"></span>
<div id="comment-46555" class="comment">
<div id="post-46555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The cygwin error at least has occurred for other people previously:</p>
<p><a href="https://www.google.co.uk/search?q=%22Couldn%27t+compute+FAST_CWD+pointer%22">https://www.google.co.uk/search?q=%22Couldn%27t+compute+FAST_CWD+pointer%22</a></p>
</div>
<div id="comment-46555-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 20:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46564"></span>
<div id="comment-46564" class="comment">
<div id="post-46564-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah I run osm2pgsql fine and get this message every time. Nothing to worry about.</p>
</div>
<div id="comment-46564-info" class="comment-info">
<span class="comment-age">(13 Nov '15, 10:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46554-form-container" class="comment-form-container">
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

<span id="46562"></span>

<div id="answer-container-46562" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46562-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>as it turned out the link to cygwin on the osm wiki page is outdated by 50 builds. The most current one works, with --host localhost.</p>
<p>I've updated the link on <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#Cygwin">https://wiki.openstreetmap.org/wiki/Osm2pgsql#Cygwin</a> so that others won't fall into that pit too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-46562" class="comments-container">
&#10;</div>
<div id="comment-tools-46562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46562-form-container" class="comment-form-container">
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

