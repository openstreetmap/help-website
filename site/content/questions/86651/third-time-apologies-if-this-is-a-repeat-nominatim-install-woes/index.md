+++
type = "question"
title = "Third time? Apologies if this is a repeat: nominatim install woes"
description = '''Greetings. I&#x27;ve installed nominatim as per instructions here:  https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/ I&#x27;ve got the following files in my directory :/home/data/1941/nom$ ls -oh total 1.7T -rw-r--r-- 1 jp 9.3K Feb 8 13:05 .env -rw-r--r-- 1 jp 9.2K Feb 7 21:10 env.defa...'''
date = "2023-02-08T23:35:00Z"
lastmod = "2023-04-05T03:16:00Z"
weight = 86651
keywords = [ "nominatim" ]
aliases = [ "/questions/86651" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Third time? Apologies if this is a repeat: nominatim install woes](/questions/86651/third-time-apologies-if-this-is-a-repeat-nominatim-install-woes)

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
<span id="post-86651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings.</p>
<p>I've installed nominatim as per instructions here:</p>
<p><a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/</a></p>
<p>I've got the following files in my directory</p>
<pre><code>:/home/data/1941/nom$ ls -oh
total 1.7T
-rw-r--r-- 1 jp 9.3K Feb  8 13:05 .env
-rw-r--r-- 1 jp 9.2K Feb  7 21:10 env.defaults
-rw-r--r-- 1 jp  13M Nov 11 03:10 gb_postcodes.csv.gz
-rw-r--r-- 1 jp 1.7T Feb  7 22:16 planet-latest.osm
-rw-r--r-- 1 jp 1.9K Feb  8 15:59 setup.log
-rw-r--r-- 1 jp 394K Oct 24 04:20 us_postcodes.csv.gz
drwxr-xr-x 2 jp 4.0K Feb  8 15:59 website
-rw-r--r-- 1 jp 376M Nov 17  2019 wikimedia-importance.sql.gz</code></pre>
<p>I've tried to import the plant file as so:</p>
<pre><code>nominatim import --osm-file planet-latest.osm 2&gt;&amp;1 | tee setup.log</code></pre>
<p>And I've received the following error message:</p>
<pre><code>2023-02-08 17:28:32: Using project directory: /home/data/1941/nom
2023-02-08 17:28:34: Creating database
env.defaults
gb_postcodes.csv.gz
planet-latest.osm
setup.log
us_postcodes.csv.gz
website
wikimedia-importance.sql.gz
worldfile
2023-02-08 17:28:34: Setting up country tables
ERROR:  relation &quot;country_osm_grid&quot; already exists
Traceback (most recent call last):
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/db/utils.py&quot;, line 28, in _pipe_to_proc
    proc.stdin.write(chunk)
BrokenPipeError: [Errno 32] Broken pipe</code></pre>
<p>The above exception was the direct cause of the following exception:</p>
<pre><code>Traceback (most recent call last):
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/db/utils.py&quot;, line 62, in execute_file
    remain = _pipe_to_proc(proc, fdesc)
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/db/utils.py&quot;, line 30, in _pipe_to_proc
    raise UsageError(&quot;Failed to execute SQL file.&quot;) from exc
nominatim.errors.UsageError: Failed to execute SQL file.</code></pre>
<p>During handling of the above exception, another exception occurred:</p>
<pre><code>Traceback (most recent call last):
  File &quot;/usr/local/bin/nominatim&quot;, line 14, in &lt;module&gt;
    exit(cli.nominatim(module_dir=&#39;/usr/local/lib/nominatim/module&#39;,
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 264, in nominatim
    return parser.run(**kwargs)
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 126, in run
    return args.command.run(args)
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/clicmd/setup.py&quot;, line 89, in run
    country_info.setup_country_tables(args.config.get_libpq_dsn(),
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/data/country_info.py&quot;, line 118, in setup_country_tables
    db_utils.execute_file(dsn, sql_dir / &#39;country_osm_grid.sql.gz&#39;)
  File &quot;/usr/local/lib/nominatim/lib-python/nominatim/db/utils.py&quot;, line 70, in execute_file
    proc.stdin.close()
BrokenPipeError: [Errno 32] Broken pipe</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '23, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/3d4bc6a7d3647b301e080db833ce7ba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james000222&#39;s gravatar image" />
<p><span>james000222</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james000222 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '23, 08:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-86651" class="comments-container">
<span id="87057"></span>
<div id="comment-87057" class="comment">
<div id="post-87057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how long did your build take and what specs for your server ?</p>
</div>
<div id="comment-87057-info" class="comment-info">
<span class="comment-age">(05 Apr '23, 03:16)</span> <span class="comment-user userinfo">TrackTrace</span>
</div>
</div>
</div>
<div id="comment-tools-86651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86651-form-container" class="comment-form-container">
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

<span id="86654"></span>

<div id="answer-container-86654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86654-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Can you try deleting the database before the import? <code>dropdb nominatim</code> (<code>psql -l</code> can show the list of database names).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '23, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-86654" class="comments-container">
&#10;</div>
<div id="comment-tools-86654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86658"></span>

<div id="answer-container-86658" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your reply!</p>
<p>I've tried that already - but tried again to be consistent. Just to be sure I've done this correctly:</p>
<p>$: sudo su - postgres</p>
<p>postgres@_:~$ psql</p>
<p>postgres=# dropdb nominatim</p>
<p>postgres=# \q</p>
<p>postgres@_:~$ exit</p>
<p>$: nominatim import --osm-file planet-latest.osm 2&gt;&amp;1 | tee setup.log</p>
<p>(error message directly as before with this as the prime cause): ERROR: relation "country_osm_grid" already exists</p>
<p>I'm fairly experience with linux, but afraid I'm very new to working with databases in general, and never with postgresql. Thank you for your assistance!</p>
<p>This is on an HPC platform with several nodes, and this does add a layer of complexity.</p>
<p>J</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '23, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/3d4bc6a7d3647b301e080db833ce7ba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james000222&#39;s gravatar image" />
<p><span>james000222</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james000222 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '23, 21:33</strong> </span></p>
</div>
</div>
<div id="comments-container-86658" class="comments-container">
<span id="86659"></span>
<div id="comment-86659" class="comment">
<div id="post-86659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I THINK I GOT IT WORKING!</p>
<p>First I logged in as nominatim, then, I had to do this:</p>
<p>nominatim=# DROP SCHEMA public CASCADE; NOTICE: drop cascades to 5 other objects DETAIL: drop cascades to extension hstore drop cascades to extension postgis drop cascades to extension postgis_raster drop cascades to table country_osm_grid drop cascades to table country_name DROP SCHEMA nominatim=# CREATE SCHEMA public; CREATE SCHEMA nominatim=# \dt Did not find any relations.</p>
<p>Then I ran the command: nominatim import --osm-file planet-latest.osm 2&gt;&amp;1 | tee setup.log</p>
<p>And it's working! Or at least no errror messages. I understand this may take days to unpack and import, correct?</p>
</div>
<div id="comment-86659-info" class="comment-info">
<span class="comment-age">(09 Feb '23, 22:11)</span> <span class="comment-user userinfo">james000222</span>
</div>
</div>
<span id="86661"></span>
<div id="comment-86661" class="comment">
<div id="post-86661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I probably screwed things up, LOL.</p>
<p>No doubt I'll be back here, begging for help again!</p>
<p>Thanks for the tip though - it led me to the DROP command and that did it.</p>
</div>
<div id="comment-86661-info" class="comment-info">
<span class="comment-age">(09 Feb '23, 22:51)</span> <span class="comment-user userinfo">james000222</span>
</div>
</div>
</div>
<div id="comment-tools-86658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86658-form-container" class="comment-form-container">
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

