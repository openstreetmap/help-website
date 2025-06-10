+++
type = "question"
title = "osm2pgsql: password authentication failed"
description = '''I can&#x27;t get osm2pgsql to work on Windows, though I have the same import process working on wsl. I have installed Windows postgresql (13.2.2) and osm2pgsql (1.4.2) using defaults mostly; pgadmin4 can see the postgresql databases and I can talk to postgres from psql (using defaults of localhost, postg...'''
date = "2021-05-14T10:32:00Z"
lastmod = "2021-05-14T15:40:00Z"
weight = 80174
keywords = [ "import", "password", "osm2pgsql" ]
aliases = [ "/questions/80174" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: password authentication failed](/questions/80174/osm2pgsql-password-authentication-failed)

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
<span id="post-80174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80174-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't get osm2pgsql to work on Windows, though I have the same import process working on wsl.</p>
<p>I have installed Windows postgresql (13.2.2) and osm2pgsql (1.4.2) using defaults mostly; pgadmin4 can see the postgresql databases and I can talk to postgres from psql (using defaults of localhost, postgres, 5433, postgres and the password). I am running osm2pgsql with</p>
<pre><code> osm2pgsql.exe -c -d gis -U postgres -W -H localhost -P 5433 -S &quot;C:\Dev\2021\Carto\openstreetmap-carto.style&quot; &quot;C:\Temp\england-latest.osm.pbf&quot;</code></pre>
<p>and have tried every combination of parameters:</p>
<ul>
<li>the above gives <code>ERROR: Connecting to database failed: FATAL: password authentication failed for user "postgres"</code></li>
<li>if I omit the <code>P 5433</code> (which matches the port number in postgresql.conf), I get <code>Is the server running on host "localhost" (::1) and accepting TCP/IP connections on port 5432?</code></li>
<li>if I omit the <code>-W</code>, I get <code>ERROR: Connecting to database failed: fe_sendauth: no password supplied</code></li>
</ul>
<p>I never get asked for a password, ie, the -W appears not to behave as documented.</p>
<p>Is this a bug? Is there a workround? Or have I just got it wrong (very possible!)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '21, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad7e45ca7e2a4532a07f10968d2e8545?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ANDREW&#39;s gravatar image" />
<p><span>ANDREW</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ANDREW has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80174" class="comments-container">
&#10;</div>
<div id="comment-tools-80174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80174-form-container" class="comment-form-container">
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

<span id="80175"></span>

<div id="answer-container-80175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80175-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Postgres authentication is often a bit fiddly even on Unix. You are right, it sounds like the -W does not behave as advertised. One thing that might help as a workaround is creating a database user with the same name as your Windows account (and making that account the owner of the gis database OR give that account postgres superuser rights). The pg_hba.conf which controls authentication should normally let you in without a password if you are the same user on the system that you try to connect to in postgres. Although I am worried by the "fe_sendauth: no password supplied" which, I believe, is issued by the client library and not the server, which would then of course mean that password-less login will never work because the client doesn't even try to connect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '21, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80175" class="comments-container">
<span id="80182"></span>
<div id="comment-80182" class="comment">
<div id="post-80182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but as you suspected. Creating a database user with the same name as the Windows user results in the same behaviour: without the -W option, I get "fe_sendauth: no password supplied" and with the -W option: "password authentication failed" and without any chance of actually entering a password.</p>
</div>
<div id="comment-80182-info" class="comment-info">
<span class="comment-age">(14 May '21, 15:05)</span> <span class="comment-user userinfo">ANDREW</span>
</div>
</div>
</div>
<div id="comment-tools-80175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80175-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80180"></span>

<div id="answer-container-80180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First: You should probably not use the "postgres" database user for day-to-day work, because it has superuser privileges.</p>
<p>I don't know why the "-W" doesn't work in your case. I just checked on Linux and it does work there. It might well be that it doesn't work on Windows for some reason, but none of the developers have a Windows machine to check. Instead of the command line options you can use environment variables to specify how to access the database. See the docs here: <a href="https://www.postgresql.org/docs/current/libpq-envars.html">https://www.postgresql.org/docs/current/libpq-envars.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '21, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-80180" class="comments-container">
<span id="80184"></span>
<div id="comment-80184" class="comment">
<div id="post-80184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, using environment variables does get round the problem.</p>
</div>
<div id="comment-80184-info" class="comment-info">
<span class="comment-age">(14 May '21, 15:40)</span> <span class="comment-user userinfo">ANDREW</span>
</div>
</div>
</div>
<div id="comment-tools-80180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80180-form-container" class="comment-form-container">
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

