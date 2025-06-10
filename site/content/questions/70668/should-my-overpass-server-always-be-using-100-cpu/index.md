+++
type = "question"
title = "Should my Overpass server always be using 100% CPU?"
description = '''I&#x27;ve recently created my own Overpass server on an m5.large EC2 instance in AWS (2 vCPU, 8GB Memory). It&#x27;s continually at 100% CPU usage, and I&#x27;m wondering if that&#x27;s normal or if I should be using a larger EC2 instance or if something isn&#x27;t working properly. I&#x27;m about to run many queries against thi...'''
date = "2019-09-06T18:41:00Z"
lastmod = "2019-09-10T23:58:00Z"
weight = 70668
keywords = [ "overpass" ]
aliases = [ "/questions/70668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should my Overpass server always be using 100% CPU?](/questions/70668/should-my-overpass-server-always-be-using-100-cpu)

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
<span id="post-70668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70668-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently created my own Overpass server on an m5.large EC2 instance in AWS (2 vCPU, 8GB Memory). It's continually at 100% CPU usage, and I'm wondering if that's normal or if I should be using a larger EC2 instance or if something isn't working properly. I'm about to run <em>many</em> queries against this server for thousands of city's street data, so I want to make sure it's as healthy as possible.</p>
<p>Truncated output of <code>top</code>: <code>%CPU %MEM TIME+ COMMAND 99.0 65.2 953:11.45 ./osm3s_query --progress --rules 73.4 1.1 0:20.51 ./update_from_dir --osc-dir=/tmp/osm-3s_update_O9Zfhz --version=2019-09-06T17\:32\:01Z --meta --flush-size=0</code></p>
<p>Contents of my <code>rules_loop.log</code> file: <code>2019-09-04 00:41:05: update started 2019-09-05 00:42:02: update finished 2019-09-05 00:42:05: update started 2019-09-06 00:43:12: update finished 2019-09-06 00:43:15: update started</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '19, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '19, 18:44</strong> </span></p>
</div>
</div>
<div id="comments-container-70668" class="comments-container">
&#10;</div>
<div id="comment-tools-70668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70668-form-container" class="comment-form-container">
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

<span id="70729"></span>

<div id="answer-container-70729" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70729-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had to resize my EC2 instance, so I stopped the server by running:</p>
<ul>
<li><code>bin/dispatcher --osm-base --terminate</code></li>
<li><code>bin/dispatcher --areas --terminate</code></li>
<li><code>sudo shutdown now -h</code></li>
</ul>
<p>Then I started the server back up and ran these commands:</p>
<ul>
<li><code>rm -f db/osm3s_v0.7.55_osm_base</code></li>
<li><code>nohup bin/dispatcher --osm-base --meta --db-dir="db/" &gt;&gt; osm_base.out &amp;</code></li>
<li><code>chmod 666 "db/osm3s_v0.7.55_osm_base"</code></li>
<li><code>nohup bin/fetch_osc.sh `cat db/replicate_id` "http://planet.openstreetmap.org/replication/minute/" "diffs/" &gt;&gt; fetch_osc.out &amp;</code></li>
<li><code>nohup bin/apply_osc_to_db.sh "diffs/" `cat db/replicate_id` --meta=yes &gt;&gt; apply_osc_to_db.out &amp;</code></li>
<li><code>rm -f db/osm3s_v0.7.54_areas</code></li>
<li><code>nohup bin/dispatcher --areas --db-dir="db/" &gt;&gt; areas.out &amp;</code></li>
</ul>
<p>I did not re-run <code>nohup bin/rules_loop.sh "db" &amp;</code> after reboot. I'm unsure if I need to, and things seem to be working well without it. The server does not run at continuous 100% CPU usage any more, after the reboot.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '19, 23:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '19, 00:00</strong> </span></p>
</div>
</div>
<div id="comments-container-70729" class="comments-container">
&#10;</div>
<div id="comment-tools-70729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70729-form-container" class="comment-form-container">
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

