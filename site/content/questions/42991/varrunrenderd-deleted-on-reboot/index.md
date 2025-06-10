+++
type = "question"
title = "/var/run/renderd/ deleted on reboot"
description = '''I have everything working now on Ubuntu 15.04 w/ OSM bright, but on each reboot /var/run/renderd is automatically deleted and renderd fails to start as it can&#x27;t find it&#x27;s socket directory. I have to manually create this directory each reboot. Is there a way to do this in the service file? I attempte...'''
date = "2015-05-09T14:32:00Z"
lastmod = "2015-05-09T19:18:00Z"
weight = 42991
keywords = [ "renderd", "osm", "ubuntu" ]
aliases = [ "/questions/42991" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [/var/run/renderd/ deleted on reboot](/questions/42991/varrunrenderd-deleted-on-reboot)

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
<span id="post-42991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42991-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have everything working now on Ubuntu 15.04 w/ OSM bright, but on each reboot /var/run/renderd is automatically deleted and renderd fails to start as it can't find it's socket directory. I have to manually create this directory each reboot.</p>
<p>Is there a way to do this in the service file? I attempted the following:</p>
<pre><code>[Unit]
Description=Rendering daemon for Openstreetmap tiles
&#10;[Service]
User=astump
Type=forking
ExecStart=sudo mkdir /var/run/renderd
ExecStart=sudo chown -R astump /var/run/renderd
ExecStart=/usr/local/bin/renderd -c /usr/local/etc/renderd.conf
ExecStop=/bin/kill -s QUIT $MAINPID
&#10;[Install]
WantedBy=multi-user.target</code></pre>
<p>But it still fails to create the /var/run/renderd folder</p>
<pre><code>astump@astump15:~$ sudo systemctl status renderd.service 
● renderd.service - Rendering daemon for Openstreetmap tiles
Loaded: loaded (/etc/systemd/system/renderd.service; enabled; vendor preset: enabled)
Active: failed (Result: exit-code) since Sat 2015-05-09 08:26:33 CDT; 1min 46s ago
Process: 6368 ExecStart=/usr/local/bin/renderd -c /usr/local/etc/renderd.conf (code=exited,     status=3)
May 09 08:26:33 astump15 renderd[6368]: config renderd(0): Active
May 09 08:26:33 astump15 renderd[6368]: config renderd(0): unix socketname=/var/run/renderd
/renderd.sock
May 09 08:26:33 astump15 renderd[6368]: config renderd(0): num_threads=4
May 09 08:26:33 astump15 renderd[6368]: config renderd(0): tile_dir=/var/lib/mod_tile
May 09 08:26:33 astump15 renderd[6368]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
May 09 08:26:33 astump15 renderd[6368]: config map 0:   name(default) file(/usr/local/share/maps/style/OSMBright/OSMBright.xml) uri(/osm_tiles/) htcp() host(localhost)
May 09 08:26:33 astump15 systemd[1]: renderd.service: control process exited, code=exited status=3
May 09 08:26:33 astump15 systemd[1]: Failed to start Rendering daemon for Openstreetmap tiles.
May 09 08:26:33 astump15 systemd[1]: Unit renderd.service entered failed state.
May 09 08:26:33 astump15 systemd[1]: renderd.service failed.
&#10;astump@astump15:~$ la /var/run/renderd
ls: cannot access /var/run/renderd: No such file or directory</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '15, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-42991" class="comments-container">
&#10;</div>
<div id="comment-tools-42991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42991-form-container" class="comment-form-container">
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

<span id="42997"></span>

<div id="answer-container-42997" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42997-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>... another question I answered on my own!</p>
<p>Typo in the tmpfiles.d/renderd.conf file - fixed it and it's working.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '15, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1afe4bf83008befdcf7bdf5c6abfa195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="f00dl3a&#39;s gravatar image" />
<p><span>f00dl3a</span><br />
<span class="score" title="171 reputation points">171</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="f00dl3a has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-42997" class="comments-container">
&#10;</div>
<div id="comment-tools-42997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42997-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42992"></span>

<div id="answer-container-42992" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42992-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's how I do it with upstart: <a href="http://blog.systemed.net/post/6">http://blog.systemed.net/post/6</a>. You may be able to adapt it to systemd. (Domain name similarity coincidental!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '15, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '15, 15:21</strong> </span></p>
</div>
</div>
<div id="comments-container-42992" class="comments-container">
&#10;</div>
<div id="comment-tools-42992" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42992-form-container" class="comment-form-container">
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

