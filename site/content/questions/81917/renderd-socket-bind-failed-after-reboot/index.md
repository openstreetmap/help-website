+++
type = "question"
title = "renderd &quot;socket bind failed&quot; after reboot"
description = '''I have followed the instructions of https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/ and it worked initially, but after rebooting I get the following error message: el@openstreetmap:~$ renderd -f -c /usr/local/etc/renderd.conf renderd[1591]: Rendering daemon started re...'''
date = "2021-09-24T08:31:00Z"
lastmod = "2021-09-24T11:11:00Z"
weight = 81917
keywords = [ "bind", "renderd", "socket", "failed" ]
aliases = [ "/questions/81917" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [renderd "socket bind failed" after reboot](/questions/81917/renderd-socket-bind-failed-after-reboot)

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
<span id="post-81917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have followed the instructions of <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> and it worked initially, but after rebooting I get the following error message:</p>
<pre><code>el@openstreetmap:~$ renderd -f -c /usr/local/etc/renderd.conf
renderd[1591]: Rendering daemon started
renderd[1591]: Initiating request_queue
renderd[1591]: Parsing section renderd
renderd[1591]: Parsing render section 0
renderd[1591]: Parsing section mapnik
renderd[1591]: Parsing section ajt
renderd[1591]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[1591]: config renderd: num_threads=4
renderd[1591]: config renderd: num_slaves=0
renderd[1591]: config renderd: tile_dir=/var/lib/mod_tile
renderd[1591]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[1591]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[1591]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[1591]: config mapnik:  font_dir_recurse=1
renderd[1591]: config renderd(0): Active
renderd[1591]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[1591]: config renderd(0): num_threads=4
renderd[1591]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[1591]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[1591]: config map 0:   name(ajt) file(/home/renderaccount/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[1591]: Initialising unix server socket on /var/run/renderd/renderd.sock
socket bind failed for: /var/run/renderd/renderd.sock
el@openstreetmap:~$</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bind" rel="tag" title="see questions tagged &#39;bind&#39;">bind</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '21, 08:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f4cb81381bfcd34569db79158d738a06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elnur09&#39;s gravatar image" />
<p><span>elnur09</span><br />
<span class="score" title="9 reputation points">9</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elnur09 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '21, 10:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-81917" class="comments-container">
&#10;</div>
<div id="comment-tools-81917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81917-form-container" class="comment-form-container">
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

<span id="81921"></span>

<div id="answer-container-81921" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure that the UNIX user you are running this under ("el") actually has write permissions on /var/run/renderd? Try the command <code>touch /var/run/renderd/testfile</code> to check. If that gives you an error messsage, you need to "su" into a different account or change the permissions or ownership of /var/run/renderd.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81921" class="comments-container">
&#10;</div>
<div id="comment-tools-81921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81922"></span>

<div id="answer-container-81922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "Running renderd in the background" part of <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> ensures that access to /var/run is maintained. After a reboot, if you want to run</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>again you'll need to do</p>
<pre><code>sudo mkdir /var/run/renderd
sudo chown renderaccount /var/run/renderd</code></pre>
<p>again first. <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> doesn't mention this because it doesn't expect you to want to run "Running renderd for the first time" more than once.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81922" class="comments-container">
&#10;</div>
<div id="comment-tools-81922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81922-form-container" class="comment-form-container">
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

