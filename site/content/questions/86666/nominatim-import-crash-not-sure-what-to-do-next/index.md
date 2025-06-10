+++
type = "question"
title = "Nominatim import crash - not sure what to do next"
description = '''Greetings again! For reference, here&#x27;s my previous thread. Newbie here with this software.  https://help.openstreetmap.org/questions/86651/third-time-apologies-if-this-is-a-repeat-nominatim-install-woes I was doing so great! I thought I was gonna break some kind of speed record, because this was goi...'''
date = "2023-02-10T17:37:00Z"
lastmod = "2023-02-11T22:15:00Z"
weight = 86666
keywords = [ "nominatim" ]
aliases = [ "/questions/86666" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim import crash - not sure what to do next](/questions/86666/nominatim-import-crash-not-sure-what-to-do-next)

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
<span id="post-86666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86666-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings again!</p>
<p>For reference, here's my previous thread. Newbie here with this software. <a href="https://help.openstreetmap.org/questions/86651/third-time-apologies-if-this-is-a-repeat-nominatim-install-woes">https://help.openstreetmap.org/questions/86651/third-time-apologies-if-this-is-a-repeat-nominatim-install-woes</a></p>
<p>I was doing so great! I thought I was gonna break some kind of speed record, because this was going to complete in like one day (or so I thought). But it didn't - crashed and burned. (crys)</p>
<p>Below is the output...any help? What do I do now?</p>
<p>$ nominatim import --osm-file planet-latest.osm 2&gt;&amp;1 | tee setup.log</p>
<p>2023-02-09 16:09:11: Using project directory: /home/data/1941/nom 2023-02-09 16:09:13: Creating database env.defaults gbpostcodes.csv.gz planet-latest.osm setup.log uspostcodes.csv.gz website wikimedia-importance.sql.gz worldfile</p>
<p>2023-02-09 16:09:14: Setting up country tables 2023-02-09 16:09:15: Importing OSM data file 2023-02-09 16:09:15 osm2pgsql version 1.7.1 2023-02-09 16:09:15 Database version: 12.13 (Ubuntu 12.13-0ubuntu0.20.04.1) 2023-02-09 16:09:15 PostGIS version: 3.0 2023-02-09 16:09:16 Parsing gazetteer style file '/usr/local/etc/nominatim/import-extratags.style'. NOTICE: table "place" does not exist, skipping 2023-02-10 11:05:12 Reading input files done in 68156s (18h 55m 56s).</p>
<p>2023-02-10 11:05:12 Processed 8172948111 nodes in 20393s (5h 39m 53s) - 401k/s 2023-02-10 11:05:12 Processed 915512510 ways in 36157s (10h 2m 37s) - 25k/s</p>
<p>2023-02-10 11:05:12 Processed 10604686 relations in 11606s (3h 13m 26s) - 914/s 2023-02-10 11:05:12 Done postprocessing on table 'planetosmnodes' in 0s 2023-02-10 11:05:12 Done postprocessing on table 'planetosmways' in 0s 2023-02-10 11:05:12 Done postprocessing on table 'planetosmrels' in 0s 2023-02-10 11:05:12 osm2pgsql took 68157s (18h 55m 57s) overall. 2023-02-10 11:05:13: Importing wikipedia importance data 2023-02-10 11:07:11: Importing secondary importance raster data 2023-02-10 11:07:11: Secondary importance file not imported. Falling back to default ranking. 2 023-02-10 11:07:11: Create functions (1st pass) 2023-02-10 11:07:11: Create tables 2023-02-10 11:13:59: Create functions (2nd pass) 2023-02-10 11:14:00: Create table triggers 2023-02-10 11:14:00: Create partition tables 2023-02-10 11:14:01: Create functions (3rd pass) 2023-02-10 11:14:01: Initialise tables 2023-02-10 11:14:01: Load data into placex table</p>
<p>Traceback (most recent call last): File "/usr/local/bin/nominatim", line 14, in &lt;module&gt; exit(cli.nominatim(module_dir='/usr/local/lib/nominatim/module', File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 264, in nominatim return parser.run(**kwargs) File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 126, in run return args.command.run(args) File "/usr/local/lib/nominatim/lib-python/nominatim/clicmd/setup.py", line 121, in run database_import.load_data(args.config.get_libpq_dsn(), num_threads) File "/usr/local/lib/nominatim/lib-python/nominatim/tools/database_import.py", line 195, in load_data conn = DBConnection(dsn) File "/usr/local/lib/nominatim/lib-python/nominatim/db/async_connection.py", line 74, in <strong>init</strong> self.connect(cursor_factory=cursor_factory) File "/usr/local/lib/nominatim/lib-python/nominatim/db/async_connection.py", line 99, in connect self.wait() File "/usr/local/lib/nominatim/lib-python/nominatim/db/async_connection.py", line 128, in wait wait_select(self.conn) File "/home/jpatterson/anaconda3/envs/jpconda/lib/python3.8/site-packages/psycopg2/extras.py", line 758, in wait_select state = conn.poll() psycopg2.OperationalError: FATAL: sorry, too many clients already</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '23, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3d4bc6a7d3647b301e080db833ce7ba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james000222&#39;s gravatar image" />
<p><span>james000222</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james000222 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86666" class="comments-container">
<span id="86667"></span>
<div id="comment-86667" class="comment">
<div id="post-86667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also my posts do not seem to be formatting correctly. Am I posting things wrong? I'm sorry I don't know why the hard returns are not carrying over.</p>
</div>
<div id="comment-86667-info" class="comment-info">
<span class="comment-age">(10 Feb '23, 17:38)</span> <span class="comment-user userinfo">james000222</span>
</div>
</div>
<span id="86668"></span>
<div id="comment-86668" class="comment">
<div id="post-86668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thisforum understands Markdown, so indent e.g. server errror logs by 4 spaces.</p>
<p>Also, when editing xml text what you see in the preview does not match what you get on the page!</p>
</div>
<div id="comment-86668-info" class="comment-info">
<span class="comment-age">(10 Feb '23, 17:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86666-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="86669"></span>

<div id="answer-container-86669" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To clarify, I did the recommended psql tweaks recommended here: <a href="https://nominatim.org/release-docs/latest/admin/Installation/">https://nominatim.org/release-docs/latest/admin/Installation/</a></p>
<p>shared_buffers = 2GB maintenance_work_mem = (10GB) autovacuum_work_mem = 2GB work_mem = (50MB) effective_cache_size = (24GB) synchronous_commit = off max_wal_size = 1GB checkpoint_timeout = 10min checkpoint_completion_target = 0.9</p>
<p>But i found a reference here to increase max_connections.</p>
<p><a href="https://support.infoworks.io/support/solutions/articles/14000122840-psycopg2-operationalerror-fatal-sorry-too-many-clients-already">https://support.infoworks.io/support/solutions/articles/14000122840-psycopg2-operationalerror-fatal-sorry-too-many-clients-already</a></p>
<p>I could try that...but do I just restart the import after that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '23, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3d4bc6a7d3647b301e080db833ce7ba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james000222&#39;s gravatar image" />
<p><span>james000222</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james000222 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86669" class="comments-container">
&#10;</div>
<div id="comment-tools-86669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86675"></span>

<div id="answer-container-86675" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SO, I increased this: max_connections=500 Restarted the DB server, and tried this: /home/data/1941/nom$ nominatim add-data --file planet-latest.osm</p>
<p>And it died...</p>
<p>2023-02-10 14:58:08: Using project directory: /home/data/1941/nom 2023-02-10 14:58:08 osm2pgsql version 1.7.1 2023-02-10 14:58:08 Database version: 12.13 (Ubuntu 12.13-0ubuntu0.20.04.1) 2023-02-10 14:58:08 PostGIS version: 3.0 2023-02-10 14:58:09 Parsing gazetteer style file '/usr/local/etc/nominatim/import-extratags.style'. Processing: Node(1210k 1.2k/s) Way(0k 0.00k/s) Relation(0 0.0/s) 2023-02-10 15:15:20 ERROR: DB copy thread failed: Ending COPY mode for 'place' failed: ERROR: relation "place_to_be_deleted" does not exist LINE 1: DELETE FROM place_to_be_deleted pdel ^ QUERY: DELETE FROM place_to_be_deleted pdel WHERE pdel.osm_type = NEW.osm_type and pdel.osm_id = NEW.osm_id and pdel.class = NEW.class CONTEXT: PL/pgSQL function place_insert() line 25 at SQL statement COPY place, line 1: "1 N man_made mast "name"=&gt;"Monte Piselli - San Giacomo" 15 \N "communication:microwave"=&gt;"yes","comm..." . Traceback (most recent call last): File "/usr/local/bin/nominatim", line 14, in &lt;module&gt; exit(cli.nominatim(module_dir='/usr/local/lib/nominatim/module', File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 264, in nominatim return parser.run(**kwargs) File "/usr/local/lib/nominatim/lib-python/nominatim/cli.py", line 126, in run return args.command.run(args) File "/usr/local/lib/nominatim/lib-python/nominatim/clicmd/add_data.py", line 79, in run return add_osm_data.add_data_from_file(cast(str, args.file or args.diff), File "/usr/local/lib/nominatim/lib-python/nominatim/tools/add_osm_data.py", line 25, in add_data_from_file run_osm2pgsql(options) File "/usr/local/lib/nominatim/lib-python/nominatim/tools/exec_utils.py", line 159, in run_osm2pgsql subprocess.run(cmd, cwd=options.get('cwd', '.'), File "/home/jpatterson/anaconda3/envs/jpconda/lib/python3.8/subprocess.py", line 516, in run raise CalledProcessError(retcode, process.args, subprocess.CalledProcessError: Command '['/usr/local/lib/nominatim/osm2pgsql', '--hstore', '--latlon', '--slim', '--log-progress', 'true', '--number-processes', '1', '--cache', '1000', '--style', '/usr/local/etc/nominatim/import-extratags.style', '--output', 'gazetteer', '--append', '--flat-nodes', '/home/data/1941/nom/worldfile', '--with-forward-dependencies', 'false', 'planet-latest.osm']' returned non-zero exit status 2.</p>
<p>NO love?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '23, 01:12</strong></p>
<img src="https://secure.gravatar.com/avatar/3d4bc6a7d3647b301e080db833ce7ba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="james000222&#39;s gravatar image" />
<p><span>james000222</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="james000222 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86675" class="comments-container">
&#10;</div>
<div id="comment-tools-86675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86675-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86681"></span>

<div id="answer-container-86681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"FATAL: sorry, too many clients already"</p>
<p>Increasing the <code>max_connections</code> was good. The osm2pgsql step of the import runs only 1 processed. Then follows the indexng step where python will create one process per CPU core. That's where the original error occured.</p>
<p>Recovering from that doesn't seem to work. I'd recommend deleting the whole database again and use <code>nominatim import</code> instead of <code>nominatim add-data</code>. The add-data already assumes whatever is in the database finished importing.</p>
<p>When you see lines like <code>Done 40691108 in 14984 @ 2715.599 per second - rank 26 ETA (seconds): 21999.57</code> That is usually recoverable by running <code>nominatim index</code>. It's really only useful if it crashed near the end and advanced because <code>nominatim import</code> does many steps one would have to run manually. Thus in this case dropping the database and starting with <code>nominatim import</code> is more straight forward.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '23, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-86681" class="comments-container">
&#10;</div>
<div id="comment-tools-86681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86681-form-container" class="comment-form-container">
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

