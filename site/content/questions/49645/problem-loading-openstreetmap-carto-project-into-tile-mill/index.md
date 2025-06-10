+++
type = "question"
title = "Problem loading openstreetmap-carto project into Tile Mill"
description = '''I got the following error when I tried to load openstreetmap-carto project into Tile Mill: roads.mss:2691:10 Property shield-face-name required for defining shield styles. roads.mss:2688:10 Property shield-face-name required for defining shield styles. and more ... Is there any way to fix this error...'''
date = "2016-05-10T10:04:00Z"
lastmod = "2017-11-26T04:15:00Z"
weight = 49645
keywords = [ "rendering", "stylesheet", "carto", "mapnik" ]
aliases = [ "/questions/49645" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Problem loading openstreetmap-carto project into Tile Mill](/questions/49645/problem-loading-openstreetmap-carto-project-into-tile-mill)

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
<span id="post-49645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I got the following error when I tried to load openstreetmap-carto project into Tile Mill:</p>
<p><em>roads.mss:2691:10 Property shield-face-name required for defining shield styles.</em><br />
<em>roads.mss:2688:10 Property shield-face-name required for defining shield styles.</em><br />
and more ...</p>
<p>Is there any way to fix this error? is there any other IDE to experiment with openstreetmap-carto project?</p>
<p>Since I'm preparing this environment for designers, I prefer to have a WYSIWYG solution rather than running python scripts after each update to get the output.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '16, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span> </br></br></p>
</div>
</div>
<div id="comments-container-49645" class="comments-container">
<span id="56598"></span>
<div id="comment-56598" class="comment">
<div id="post-56598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Se pudo encontrar solución a este problema? Estoy teniendo el mismo mensaje de error.</p>
</div>
<div id="comment-56598-info" class="comment-info">
<span class="comment-age">(12 Jun '17, 21:23)</span> <span class="comment-user userinfo">jvelazquez</span>
</div>
</div>
</div>
<div id="comment-tools-49645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49645-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="60653"></span>

<div id="answer-container-60653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a similar problem. I got the same error with 'text-margin' and 'shield-margin'. I opened all of the openstreetmap-carto stylesheets and searched for text-margin and shield-margin. Then, I commented out the lines that had either of that text. I believe TileMill is not being updated and the openstreetmap-carto stylesheets are. So sometimes there are updates made to the stylesheets that TileMill can't handle. Of course commenting these lines out will cause your data to display differently in TileMill but, it will load and be usable. Hope that helps</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '17, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/41a7fedf2793f657dcef6efefeb10b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeattleHeather&#39;s gravatar image" />
<p><span>SeattleHeather</span><br />
<span class="score" title="220 reputation points">220</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeattleHeather has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60653" class="comments-container">
&#10;</div>
<div id="comment-tools-60653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60653-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60654"></span>

<div id="answer-container-60654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60654-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option is <a href="https://wiki.openstreetmap.org/wiki/Kosmtik">Kosmtik</a> - depending on what else is installed on yor PC, that may or may not work.</p>
<p>Alternatively, just set up mod_tile and renderd outside of tilemill as per the <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">switch2osm</a> guide, edit the stylesheet with a text editor, run a script that runs "carto" and restarts renderd and apache2, and shoft-reload tiles in your web browser.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '17, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60654" class="comments-container">
&#10;</div>
<div id="comment-tools-60654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51198"></span>

<div id="answer-container-51198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Did you manage to solve this case? I have a similar problem...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '16, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/8faf1b1820811a2e0efab811dbaad914?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wojtas82&#39;s gravatar image" />
<p><span>Wojtas82</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wojtas82 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51198" class="comments-container">
<span id="51199"></span>
<div id="comment-51199" class="comment">
<div id="post-51199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At what line number (i.e. what was the actual error)?</p>
</div>
<div id="comment-51199-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 10:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51202"></span>
<div id="comment-51202" class="comment">
<div id="post-51202-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><img src="http://help.openstreetmap.org/upfiles/Przechwytywanie.PNG" alt="alt text" /></p>
<pre><code> roads.mss:2681:10 Property shield-face-name required for defining shield styles.
 roads.mss:2678:10 Property shield-face-name required for defining shield styles.</code></pre>
<p>etc..</p>
</div>
<div id="comment-51202-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 11:10)</span> <span class="comment-user userinfo">Wojtas82</span>
</div>
</div>
</div>
<div id="comment-tools-51198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51198-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60794"></span>

<div id="answer-container-60794" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60794-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm using Kosmtik for rendering osm-carto with some text editor (like Gedit or Atom), but I tried to open current version of osm-carto version with TileOven from git repo just to check if it works:</p>
<p>"TileOven is a maintained fork of TileMill, tested on Linux with Node 0.10.25, 4.2.6, 4.5.0 and 6.9.1 TileOven works only in server mode, no native packages are provided. Platforms other than Linux should theoretically work, but aren't tested."</p>
<p><a href="https://github.com/florianf/tileoven">https://github.com/florianf/tileoven</a></p>
<p>I was able to run it on Ubuntu 17.10, but unfortunately opening osm-carto was not possible:</p>
<p>[tilemill] Started [Server Core:20009].</p>
<p>[tilemill] [tilemill] skipped loading project: Error: Could not open project.mml file for "openstreetmap-carto". Error was:</p>
<p>[tilemill]</p>
<p>[tilemill] "Unexpected token s in JSON at position 0"</p>
<p>[tilemill]</p>
<p>[tilemill] (in /home/kocio/Dokumenty/MapBox/project/openstreetmap-carto/project.mml)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '17, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-60794" class="comments-container">
&#10;</div>
<div id="comment-tools-60794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60794-form-container" class="comment-form-container">
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

