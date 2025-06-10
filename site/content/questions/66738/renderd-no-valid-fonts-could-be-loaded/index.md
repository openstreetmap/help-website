+++
type = "question"
title = "Renderd : no valid fonts could be loaded"
description = '''Hi everyone, I am installing a OSM tile server under Strech and I am in trouble : when I run service renderd status I have :  renderd.service - LSB: Mapnik rendering daemon Loaded: loaded (/etc/init.d/renderd; generated; vendor preset: enabled) Active: active (running) since Sat 2018-11-10 15:46:41 ...'''
date = "2018-11-10T05:34:00Z"
lastmod = "2018-11-12T00:43:00Z"
weight = 66738
keywords = [ "font", "rendered" ]
aliases = [ "/questions/66738" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Renderd : no valid fonts could be loaded](/questions/66738/renderd-no-valid-fonts-could-be-loaded)

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
<span id="post-66738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, I am installing a OSM tile server under Strech and I am in trouble : when I run <strong>service renderd status</strong> I have :</p>
<blockquote>
<p>renderd.service - LSB: Mapnik rendering daemon Loaded: loaded (/etc/init.d/renderd; generated; vendor preset: enabled) Active: active (running) since Sat 2018-11-10 15:46:41 +11; 34min ago Docs: man:systemd-sysv-generator(8)<br />
Process: 1799 ExecStart=/etc/init.d/renderd start (code=exited, status=0/SUCCESS) Tasks: 4 (limit: 4915) CGroup: /system.slice/renderd.service └─1806 /usr/local/bin/renderd -c /usr/local/etc/renderd.conf</p>
<p>nov. 10 15:46:41 carto renderd[1805]: config mapnik: font_dir_recurse=1 nov. 10 15:46:41 carto renderd[1805]: config renderd(0): Active nov. 10 15:46:41 carto renderd[1805]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock nov. 10 15:46:41 carto renderd[1799]: Starting Mapnik rendering daemon: renderd. nov. 10 15:46:41 carto systemd[1]: Started LSB: Mapnik rendering daemon. nov. 10 15:46:41 carto renderd[1806]: Loading parameterization function for nov. 10 15:46:41 carto renderd[1806]: Loading parameterization function for nov. 10 15:46:41 carto renderd[1806]: Starting stats thread nov. 10 15:46:42 carto renderd[1806]: An error occurred while loading the map layer 'default': no valid fonts could be loaded in FontSet 'fontset-1' in FontSet at line 90 of '/home/data/osm/styles/openstreetmap-carto/style.xml' nov. 10 15:46:42 carto renderd[1806]: An error occurred while loading the map layer 'default': no valid fonts could be loaded in FontSet 'fontset-1' in FontSet at line 90 of '/home/data/osm/styles/openstreetmap-carto/style.xml'</p>
</blockquote>
<p>Does anyone have an idea to fix it ? Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-font" rel="tag" title="see questions tagged &#39;font&#39;">font</span> <span class="post-tag tag-link-rendered" rel="tag" title="see questions tagged &#39;rendered&#39;">rendered</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '18, 05:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c678c5c86456016f2fffb941f31d8818?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brunogee&#39;s gravatar image" />
<p><span>brunogee</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brunogee has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-66738" class="comments-container">
&#10;</div>
<div id="comment-tools-66738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66738-form-container" class="comment-form-container">
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

<span id="66751"></span>

<div id="answer-container-66751" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66751-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brunogee has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The font directory is set in /etc/renderd.conf</p>
<p>In this directory you should have the fonts used in your style (home/data/osm/styles/openstreetmap-carto/style.xml)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '18, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-66751" class="comments-container">
<span id="66753"></span>
<div id="comment-66753" class="comment">
<div id="post-66753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you yvecai,</p>
<p>You were very helpful ;-)</p>
<p>I have found a solution : sudo apt-get install fonts-noto-cjk fonts-noto-hinted fonts-noto-unhinted fonts-hanazono ttf-unifont</p>
<p>Now, I have a new message :(</p>
<p>So it's close ;-)</p>
</div>
<div id="comment-66753-info" class="comment-info">
<span class="comment-age">(12 Nov '18, 00:43)</span> <span class="comment-user userinfo">brunogee</span>
</div>
</div>
</div>
<div id="comment-tools-66751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66751-form-container" class="comment-form-container">
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

