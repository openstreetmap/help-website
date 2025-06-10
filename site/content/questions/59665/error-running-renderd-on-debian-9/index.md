+++
type = "question"
title = "Error running renderd on debian 9"
description = '''Hey I updated my debian to debian 9. When I am now trying to run renderd I got this error message:  renderd: error while loading shared libraries: libmapnik.so.2.2: cannot open shared object file: No such file or directory  It seems renderd want to use the wrong libmapnik library. My System has the ...'''
date = "2017-09-18T10:27:00Z"
lastmod = "2019-06-03T08:43:00Z"
weight = 59665
keywords = [ "renderd", "debian", "mapnik" ]
aliases = [ "/questions/59665" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error running renderd on debian 9](/questions/59665/error-running-renderd-on-debian-9)

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
<span id="post-59665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59665-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey I updated my debian to debian 9. When I am now trying to run renderd I got this error message:</p>
<pre><code>renderd: error while loading shared libraries: libmapnik.so.2.2: cannot open shared object file: No such file or directory</code></pre>
<p>It seems renderd want to use the wrong libmapnik library. My System has the following libmapnik libraries installed:</p>
<pre><code>/usr/local/lib/libmapnik.so.3.1.0
/usr/local/lib/libmapnik.so.3.1
/usr/local/lib/libmapnik.so
/usr/lib/libmapnik.so.3.0.12
/usr/lib/libmapnik.so.3.0
/usr/lib/libmapnik.so</code></pre>
<p>My renderd.conf looks like:</p>
<pre><code>[renderd]
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;
[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input/
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile
XML=/opt/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256</code></pre>
<p>So maybe I need to update the version of renderd. But how do I do this?</p>
<p>Any help would be nice :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '17, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f2ff5fbe76b699a58bc64acd0ccb8cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nevyen&#39;s gravatar image" />
<p><span>Nevyen</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nevyen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59665" class="comments-container">
<span id="59666"></span>
<div id="comment-59666" class="comment">
<div id="post-59666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like you have two mapnik installations, one via the package manager and one self-compiled version. Do you really need both? If not, try removing the conflicting one.</p>
</div>
<div id="comment-59666-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 10:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59665-form-container" class="comment-form-container">
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

<span id="59668"></span>

<div id="answer-container-59668" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First things first - make sure you've got a restorable backup of where you are currently :)</p>
<p>Secondly - try and investigate why renderd thinks <code>"libmapnik.so.2.2"</code> is missing yet the renderd.conf file is trying to use a 3.0 plugins directory: <code>"plugins_dir=/usr/lib/mapnik/3.0/input/"</code>.</p>
<p>If you have the opportunity, try setting up renderd with Debian 9 in a virtual machine - that way you can see what's supposed to link to what (and even if it works at all!) before tinkering with your main machine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '17, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '19, 09:07</strong> </span></p>
</div>
</div>
<div id="comments-container-59668" class="comments-container">
&#10;</div>
<div id="comment-tools-59668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59668-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69417"></span>

<div id="answer-container-69417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello! I just copied all files libiniparser.* to /usr/lib/ and it worked. Note that some of them are just symlincs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '19, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/657d9febd933cef716766c89a3d4446a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lokks&#39;s gravatar image" />
<p><span>lokks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lokks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69417" class="comments-container">
&#10;</div>
<div id="comment-tools-69417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69417-form-container" class="comment-form-container">
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

