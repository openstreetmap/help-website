+++
type = "question"
title = "ValueError when using pyosmium-get-changes to update Nominatim data"
description = '''I&#x27;m setting up my own Nominatim server for 2 countries being Belgium and The Netherlands. Therefore I used the following online manual: Importing multiple regions (with updates) I started by adjusting the COUNTRIES to COUNTRIES=&quot;europe/belgium europe/netherlands&quot; in import_multiple_regions.sh and up...'''
date = "2021-11-16T09:19:00Z"
lastmod = "2021-11-16T15:04:00Z"
weight = 82599
keywords = [ "pyosmium-get-changes", "nominatim", "pyosmium" ]
aliases = [ "/questions/82599" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ValueError when using pyosmium-get-changes to update Nominatim data](/questions/82599/valueerror-when-using-pyosmium-get-changes-to-update-nominatim-data)

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
<span id="post-82599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82599-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm setting up my own Nominatim server for 2 countries being Belgium and The Netherlands. Therefore I used the following online manual: <a href="https://nominatim.org/release-docs/latest/admin/Advanced-Installations/#importing-multiple-regions-with-updates">Importing multiple regions (with updates)</a></p>
<p>I started by adjusting the <code>COUNTRIES</code> to <code>COUNTRIES="europe/belgium europe/netherlands"</code> in <code>import_multiple_regions.sh</code> and <code>update_database.sh</code>.</p>
<p>Running the import script worked, it ended (after about 2 days) without any errors. But when I try to run the update script, it constantly logs a runtime exception and I have no clue how I can fix it.</p>
<p>This is a part of the output I get. It's the same for both countries:</p>
<pre><code>rm -f update/europe/belgium/europe_belgium.osc.gz pyosmium-get-changes -o update/europe/belgium/europe_belgium.osc.gz
-f update/europe/belgium/sequence.state
--server https://download.geofabrik.de/europe/belgium-updates
-v Traceback (most recent call last):   File &quot;/usr/bin/pyosmium-get-changes&quot;, line 70, in from_id
    seq_id=int(idstr) ValueError: invalid literal for int() with base 10: &#39;&#39;
&#10;During handling of the above exception, another exception occurred:
&#10;Traceback (most recent call last):   File &quot;/usr/bin/pyosmium-get-changes&quot;, line 243, in &lt;module&gt;
    exit(main(sys.argv[1:]))   File &quot;/usr/bin/pyosmium-get-changes&quot;, line 188, in main
    options.start = ReplicationStart.from_id(seq)   File &quot;/usr/bin/pyosmium-get-changes&quot;, line 72, in from_id
    raise ArgumentTypeError(&quot;Sequence id &#39;%s&#39; is not a number&quot; % idstr) argparse.ArgumentTypeError: Sequence id &#39;&#39; is not a number
+ echo &#39;Attempting to import diffs&#39; Attempting to import diffs
+ nominatim add-data --diff update/europe/belgium/europe_belgium.osc.gz 2021-11-16 08:58:43: Using project directory: /srv/nominatim/nominatim-project 2021-11-16 08:58:43  osm2pgsql version
1.5.1 (1.5.1-4-gbd7b4440-changed) 2021-11-16 08:58:43  Database version:
12.9 (Ubuntu 12.9-0ubuntu0.20.04.1) 2021-11-16 08:58:43  PostGIS version:
3.0 2021-11-16 08:58:43  Parsing gazetteer style file &#39;/usr/local/etc/nominatim/import-extratags.style&#39;. 2021-11-16 08:58:43  ERROR: Open failed for &#39;update/europe/belgium/europe_belgium.osc.gz&#39;: No such file or directory Traceback (most recent call last):   File &quot;/usr/local/bin/nominatim&quot;, line 11, in &lt;module&gt;
    exit(cli.nominatim(module_dir=&#39;/usr/local/lib/nominatim/module&#39;, File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 235, in nominatim
    return parser.run(**kwargs)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/cli.py&quot;, line 96, in run
    return args.command.run(args)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/clicmd/add_data.py&quot;, line 70, in run
    return add_osm_data.add_data_from_file(args.file or args.diff,   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/tools/add_osm_data.py&quot;, line 18, in add_data_from_file
    run_osm2pgsql(options)   File &quot;/usr/local/lib/nominatim/lib-python/nominatim/tools/exec_utils.py&quot;, line 139, in run_osm2pgsql
    subprocess.run(cmd, cwd=options.get(&#39;cwd&#39;, &#39;.&#39;),   File &quot;/usr/lib/python3.8/subprocess.py&quot;, line 516, in run
    raise CalledProcessError(retcode, process.args, subprocess.CalledProcessError: Command &#39;[&#39;/usr/local/lib/nominatim/osm2pgsql&#39;, &#39;--hstore&#39;, &#39;--latlon&#39;, &#39;--slim&#39;, &#39;--with-forward-dependencies&#39;, &#39;false&#39;, &#39;--log-progress&#39;, &#39;true&#39;, &#39;--number-processes&#39;, &#39;1&#39;, &#39;--cache&#39;, &#39;1000&#39;, &#39;--output&#39;, &#39;gazetteer&#39;, &#39;--style&#39;, &#39;/usr/local/etc/nominatim/import-extratags.style&#39;, &#39;--append&#39;, &#39;update/europe/belgium/europe_belgium.osc.gz&#39;]&#39; returned non-zero exit status 1.</code></pre>
<p>So does anyone have any idea what I'm doing wrong? I'm doing this on an Ubuntu 20.04.3 Server.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pyosmium-get-changes" rel="tag" title="see questions tagged &#39;pyosmium-get-changes&#39;">pyosmium-get-changes</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '21, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '21, 09:22</strong> </span></p>
</div>
</div>
<div id="comments-container-82599" class="comments-container">
<span id="82602"></span>
<div id="comment-82602" class="comment">
<div id="post-82602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What are the contents of <code>update/europe/belgium/sequence.state</code> ? It should look something like <a href="https://download.geofabrik.de/europe/belgium-updates/state.txt">https://download.geofabrik.de/europe/belgium-updates/state.txt</a></p>
</div>
<div id="comment-82602-info" class="comment-info">
<span class="comment-age">(16 Nov '21, 15:04)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-82599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82599-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

