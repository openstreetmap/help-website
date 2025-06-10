+++
type = "question"
title = "Renderd conf file, datasource postgis error"
description = '''Hi there. I&#x27;m currently trying to run the tutorial on https://switch2osm.org/manually-building-a-tile-server-18-04-lts/, but am having some issues with the section on &#x27;Running renderd for the first time&#x27;.  This is my terminal output: renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/did...'''
date = "2019-11-25T23:34:00Z"
lastmod = "2019-11-26T00:57:00Z"
weight = 71827
keywords = [ "renderd", "switch2osm" ]
aliases = [ "/questions/71827" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Renderd conf file, datasource postgis error](/questions/71827/renderd-conf-file-datasource-postgis-error)

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
<span id="post-71827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. I'm currently trying to run the tutorial on <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a>, but am having some issues with the section on 'Running renderd for the first time'.</p>
<p>This is my terminal output:</p>
<pre><code>renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/didot/GFSDidotBold.otf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/chandas1-2.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/kalimati.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/samanata.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-oriya/Lohit-Odia.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-telu-extra/Pothana2000.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-telu-extra/vemana2000.ttf
renderd[28593]: DEBUG: Loading font: /usr/share/fonts/truetype/didot-classic/GFSDidotClassic.otf
Running in foreground mode...
renderd[28593]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[28593]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[28593]: Loading parameterization function for 
renderd[28593]: Loading parameterization function for 
renderd[28593]: Loading parameterization function for 
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[28593]: An error occurred while loading the map layer &#39;default&#39;: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 819 of &#39;/home/isaacw/osm/openstreetmap-carto/mapnik.xml&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
renderd[28593]: An error occurred while loading the map layer &#39;default&#39;: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 819 of &#39;/home/isaacw/osm/openstreetmap-carto/mapnik.xml&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Serif Tibetan Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2019-11-26 12:23:30: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[28593]: An error occurred while loading the map layer &#39;default&#39;: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 819 of &#39;/home/isaacw/osm/openstreetmap-carto/mapnik.xml&#39;
renderd[28593]: An error occurred while loading the map layer &#39;default&#39;: Could not create datasource for type: &#39;postgis&#39; (no datasource plugin directories have been successfully registered)  encountered during parsing of layer &#39;landcover-low-zoom&#39; in Layer at line 819 of &#39;/home/isaacw/osm/openstreetmap-carto/mapnik.xml&#39;</code></pre>
<p>I believe my problem may be to do with not having an 'ajt' section in my renderd.conf file. So I ended up adding the URI and XML changes to the default section. Am I doing this correctly? Please help :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '19, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7667a914ae24787fc4c6fa5790a45bb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itworsley&#39;s gravatar image" />
<p><span>itworsley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itworsley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71827" class="comments-container">
&#10;</div>
<div id="comment-tools-71827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71827-form-container" class="comment-form-container">
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

<span id="71828"></span>

<div id="answer-container-71828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your renderd.conf needs to have a section like this:</p>
<p><code>[mapnik] plugins_dir=/usr/lib/mapnik/input font_dir=/usr/share/fonts/truetype font_dir_recurse=1</code></p>
<p>And the directory listed as "plugins_dir" needs to contain a file called <code>postgis.input</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '19, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71828" class="comments-container">
&#10;</div>
<div id="comment-tools-71828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71828-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71829"></span>

<div id="answer-container-71829" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Frederik, thanks for your reply.</p>
<p>I was actually using the incorrect version of PostgreSQL and PostGIS. Perhaps should've followed the correct tutorial for Ubuntu 18.04 rather than 16.04.</p>
<p>Cheers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '19, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7667a914ae24787fc4c6fa5790a45bb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itworsley&#39;s gravatar image" />
<p><span>itworsley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itworsley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71829" class="comments-container">
&#10;</div>
<div id="comment-tools-71829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71829-form-container" class="comment-form-container">
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

