+++
type = "question"
title = "tirex rendering child terminates"
description = '''Hello, I have installed on Ubuntu 12.04 the following components:  Postgres 9.1  Mapnik 2.1  Tirex from source with patch  After importing germany.osm using osm2pgsql I try to render the planet using zoom level 3 and 4 with the following command: tirex-batch --prio=25 map=osm bbox=-180,-90,180,90 z=...'''
date = "2013-01-14T02:26:00Z"
lastmod = "2013-02-06T11:48:00Z"
weight = 19058
keywords = [ "tirex", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/19058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tirex rendering child terminates](/questions/19058/tirex-rendering-child-terminates)

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
<span id="post-19058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19058-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have installed on Ubuntu 12.04 the following components:</p>
<ul>
<li>Postgres 9.1</li>
<li>Mapnik 2.1</li>
<li>Tirex from source with patch</li>
</ul>
<p>After importing germany.osm using osm2pgsql I try to render the planet using zoom level 3 and 4 with the following command:</p>
<pre><code>tirex-batch --prio=25 map=osm bbox=-180,-90,180,90 z=2-3</code></pre>
<p>But tirex/mapnik doesn't render anything. The lines in my syslog are:</p>
<pre><code>Jan 14 03:08:12 h2113648 tirex-master[11037]: tirex-master started with cmd line options: 
Jan 14 03:08:12 h2113648 tirex-master[11037]: Config bucket=[{maxload=20 maxproc=4 minprio=1 name=live},{maxload=8 maxproc=3 minprio=10 name=important},{maxload=4 maxproc=2 minprio=20 name=background}]
Jan 14 03:08:12 h2113648 tirex-master[11037]: Renderer mapnik: port=9331 procs=3 path=/usr/lib/tirex/backends/mapnik syslog_facility=daemon debug=0 fontdir=/usr/lib/mapnik/fonts plugindir=/usr/lib/mapnik/input
Jan 14 03:08:12 h2113648 tirex-master[11037]:   Map example: renderer=mapnik tiledir=/var/lib/tirex/tiles/example zoom=0-4 mapfile=/usr/share/tirex/example-map/example.xml
Jan 14 03:08:12 h2113648 tirex-master[11037]:   Map osm: renderer=mapnik tiledir=/var/lib/tirex/tiles/osm zoom=0-18 mapfile=/usr/share/osm-mapnik2/osm.xml
Jan 14 03:08:12 h2113648 tirex-master[11037]:   Map surveillance: renderer=mapnik tiledir=/var/lib/tirex/tiles/surveillance zoom=0-18 mapfile=/usr/share/osm-styles/surveillance/common.xml
Jan 14 03:08:12 h2113648 tirex-master[11037]: Renderer test: port=9330 procs=2 path=/usr/lib/tirex/backends/test syslog_facility=daemon debug=0
Jan 14 03:08:12 h2113648 tirex-master[11037]:   Map test: renderer=test tiledir=/var/lib/tirex/tiles/test zoom=0-10
Jan 14 03:08:12 h2113648 tirex-master[11037]: Listening for commands on socket /var/run/tirex/master.sock
Jan 14 03:08:12 h2113648 tirex-master[11037]: Listening for mod_tile connections on /var/lib/tirex/modtile.sock (UNIX)
Jan 14 03:08:12 h2113648 tirex-master[11038]: Listening for backend responses
Jan 14 03:08:55 h2113648 tirex-backend-manager[11008]: child 11013 terminated (exit_code=0, signal=6)
Jan 14 03:08:55 h2113648 tirex-backend-manager[11008]: disabled renderer mapnik
Jan 14 03:08:55 h2113648 tirex-backend-manager[11008]: child 11010 terminated (exit_code=0, signal=6)
Jan 14 03:08:55 h2113648 tirex-backend-manager[11008]: disabled renderer mapnik
Jan 14 03:17:00 h2113648 tirex-backend-manager[11008]: sending HUP to worker &#39;mapnik&#39; with pid 11012 (due to timeout)
Jan 14 03:17:00 h2113648 tirex-backend-manager[11008]: child 11012 terminated (exit_code=9, signal=0)
Jan 14 03:19:12 h2113648 tirex-master[11038]: Job with id=1358129333_24434048 timed out on rendering list (map=osm z=3 x=0 y=0)
Jan 14 03:19:12 h2113648 tirex-master[11038]: Job with id=1358129333_22285488 timed out on rendering list (map=osm z=2 x=0 y=0)</code></pre>
<p>What is the child process? Is this mapnik crashing? I tried yesterday same setup on a debian Squeeze box with exactly the same result!?</p>
<p>Here is a log of all my installation actions: <a href="https://gist.github.com/4527318">https://gist.github.com/4527318</a></p>
<p>Please help :-)</p>
<p>THANX!</p>
<p>Steffen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '13, 02:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d4932a3cd5ad24413b27adf3d69b43ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kieste&#39;s gravatar image" />
<p><span>kieste</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kieste has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19058" class="comments-container">
<span id="19059"></span>
<div id="comment-19059" class="comment">
<div id="post-19059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw. the machine is a 32 GB 6core HT xeon</p>
</div>
<div id="comment-19059-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 02:34)</span> <span class="comment-user userinfo">kieste</span>
</div>
</div>
<span id="19060"></span>
<div id="comment-19060" class="comment">
<div id="post-19060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw 2: before I tried using tirex I used a setup with renderd (on debian 6) and started a batch using render_list. But render_list also ran into a timeout. Same problem I guess. It must be a mapnik 2.1 issue.</p>
</div>
<div id="comment-19060-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 02:41)</span> <span class="comment-user userinfo">kieste</span>
</div>
</div>
</div>
<div id="comment-tools-19058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19058-form-container" class="comment-form-container">
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

<span id="19066"></span>

<div id="answer-container-19066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19066-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>tirex-backend-manager</code> is a process that forks rendering processes. You have configured it to fork three, two of whom died immediately with SIGABRT, and one tried to render something but was killed when it took longer than the configured timeout. During these 10 minutes you should have seen on process called "mapnik" on your machine that indicated it was rendering something (ps auxw|grep mapnik) - if not then that has died too but unnoticed.</p>
<p>You can try running the tirex-backend-manager with the <code>--debug</code> flag from a command line window instead of running it as a service; it will not detach then, and be more verbose. At your zoom level 2-3 I'd somehow expect problems with shape files which could throw an exception and make the process abort but you'd normally expect that to show up in the logs. (At higher zooms one would want to configure PostgreSQL to <code>log_statement='all'</code> and watch if any queries show up there.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '13, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '13, 07:31</strong> </span></p>
</div>
</div>
<div id="comments-container-19066" class="comments-container">
<span id="19133"></span>
<div id="comment-19133" class="comment">
<div id="post-19133-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello Frederik,</p>
<p>thanx for the clarification. I started the tirex backend manager in debug mode and got a long backtrace and memory dump. At the moment I can't figure out the root cause but I will check it. Maybe you can see something obvious? Log file: <a href="https://gist.github.com/4542719">https://gist.github.com/4542719</a></p>
<p>Postgres executes lots of statements. (I guess the log is not very helpfull. But here it is: <a href="https://gist.github.com/4542748">https://gist.github.com/4542748</a>)</p>
<p>Maybe I will substitute tirex with renderd if I can't get it to work.</p>
<p>I ran the command:</p>
<pre><code>render -s /usr/share/osm-mapnik2/osm.xml --file berlin --bbox 12.88,52.67,13.8,52.35</code></pre>
<p>and got a beautiful map of berlin. So mapnik seem to work fine.</p>
<p>Regards Steffen</p>
</div>
<div id="comment-19133-info" class="comment-info">
<span class="comment-age">(15 Jan '13, 22:33)</span> <span class="comment-user userinfo">kieste</span>
</div>
</div>
<span id="19604"></span>
<div id="comment-19604" class="comment">
<div id="post-19604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Steffen, Frederik,</p>
<p>I've got the same problem (ubuntu 11.10, postgre 8.4, mapnik 2.1, tirex from source with patch, boost 1.49). Any progress in this problem? In my case, mapnik-backend fails in metatilehandler.cc:</p>
<pre><code> line 158: rawpng[index] = mapnik::save_to_string(view, &quot;png256&quot;);</code></pre>
<p>I tried to change the format parameter without success. Mapnik works well, when I use it with python bindings.</p>
<p>Kindly regards, Martin</p>
</div>
<div id="comment-19604-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 11:48)</span> <span class="comment-user userinfo">mattesCZ</span>
</div>
</div>
</div>
<div id="comment-tools-19066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19066-form-container" class="comment-form-container">
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

