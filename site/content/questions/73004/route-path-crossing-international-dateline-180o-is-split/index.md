+++
type = "question"
title = "Route path crossing international dateline (180º) is split"
description = '''Hi ! There is a form to modify a map created in OSM to avoid the splitting of a route that crosses the International Dateline...? The resulting map looks ugly.  Thanks in advance '''
date = "2020-02-11T09:46:00Z"
lastmod = "2020-02-11T22:02:00Z"
weight = 73004
keywords = [ "antimeridian", "180º" ]
aliases = [ "/questions/73004" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Route path crossing international dateline (180º) is split](/questions/73004/route-path-crossing-international-dateline-180o-is-split)

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
<span id="post-73004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73004-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi !</p>
<p>There is a form to modify a map created in OSM to avoid the splitting of a route that crosses the International Dateline...? The resulting map looks ugly.</p>
<p>Thanks in advance</p>
<p><img src="/upfiles/Clipboard02_eoJm4Sc.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-antimeridian" rel="tag" title="see questions tagged &#39;antimeridian&#39;">antimeridian</span> <span class="post-tag tag-link-180º" rel="tag" title="see questions tagged &#39;180º&#39;">180º</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '20, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/03e8f977ef973cadc48fde64258e2c55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StratoCat&#39;s gravatar image" />
<p><span>StratoCat</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StratoCat has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73004" class="comments-container">
<span id="73012"></span>
<div id="comment-73012" class="comment">
<div id="post-73012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, what tool are you using to create this map ?</p>
</div>
<div id="comment-73012-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 15:26)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73016"></span>
<div id="comment-73016" class="comment">
<div id="post-73016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm importing location coordinates (Lat, Long) in uMap (<a href="https://umap.openstreetmap.fr/en/)">https://umap.openstreetmap.fr/en/)</a></p>
</div>
<div id="comment-73016-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 15:53)</span> <span class="comment-user userinfo">StratoCat</span>
</div>
</div>
</div>
<div id="comment-tools-73004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73004-form-container" class="comment-form-container">
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

<span id="73026"></span>

<div id="answer-container-73026" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73026-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="StratoCat has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After a number of tries, I finally found it ! You have to subtract 360 to all positive longitudes (the reverse might also work).</p>
<p>Here is your <a href="https://gist.github.com/hamlet/a7726db414a99a3762c7edc8667b9e9b">updated file</a></p>
<p>I used some <a href="https://stackoverflow.com/questions/37805433/vim-substitution-with-mathematical-expression">vim magic</a> to do it, first conversion from tsv to csv, then calculation :</p>
<pre><code>:%s/\t/,/
:%s/,\(1[^&quot;]\+\)/\=&#39;,&#39;.string(eval(submatch(1))-360)/</code></pre>
<p>You probably can do it with any spreadsheet software, but I'm glad I've learned to do it with vim. ;-)</p>
<p>Side note, gpsbabel is great for converting positions, especially to gpx as track, but was not needed after all. I just exported my already shown try, and looked at the data. When I found a longitude of -247 I guessed this would work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '20, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73026" class="comments-container">
<span id="73027"></span>
<div id="comment-73027" class="comment">
<div id="post-73027-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It also works by adding 360 to negative longitudes, and this is the command :</p>
<pre><code> :%s/,\(-[^\n]\+\)/\=&#39;,&#39;.string(eval(submatch(1))+360)/</code></pre>
</div>
<div id="comment-73027-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 18:07)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73028"></span>
<div id="comment-73028" class="comment">
<div id="post-73028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Absolutelly Awesome. You saved my day ... really.</p>
<p>A BIG thank you!</p>
</div>
<div id="comment-73028-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 19:51)</span> <span class="comment-user userinfo">StratoCat</span>
</div>
</div>
<span id="73031"></span>
<div id="comment-73031" class="comment">
<div id="post-73031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're welcome. :-) It should be documented somewhere...</p>
</div>
<div id="comment-73031-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 22:02)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73026-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73018"></span>

<div id="answer-container-73018" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73018-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you try to manually center your map on the pacific ?</p>
<p>I've created a polyline across this ocean, and it looks alright, see below.</p>
<p>You might share your map URL, or the original data, for further experimentation.</p>
<p>Regards</p>
<p><img src="/upfiles/2020-02-11_17-01-15.png" alt="umap across pacific" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '20, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '20, 16:07</strong> </span></p>
</div>
</div>
<div id="comments-container-73018" class="comments-container">
<span id="73019"></span>
<div id="comment-73019" class="comment">
<div id="post-73019-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure... the URL is <a href="https://umap.openstreetmap.fr/en/map/project-loon-hbal011_418121">https://umap.openstreetmap.fr/en/map/project-loon-hbal011_418121</a></p>
<p>The data are lat,lon locations</p>
</div>
<div id="comment-73019-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 16:12)</span> <span class="comment-user userinfo">StratoCat</span>
</div>
</div>
<span id="73022"></span>
<div id="comment-73022" class="comment">
<div id="post-73022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Lat Lon 41.090046 -117.24723 41.246807 -116.93441 41.386356 -116.76473 41.585396 -116.60854 41.72139 -116.30826</p>
</div>
<div id="comment-73022-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 16:14)</span> <span class="comment-user userinfo">StratoCat</span>
</div>
</div>
</div>
<div id="comment-tools-73018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73018-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73024"></span>

<div id="answer-container-73024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like an old unsolved problem : <a href="https://github.com/umap-project/umap/issues/33">https://github.com/umap-project/umap/issues/33</a>.</p>
<p>It's sad if it works only with a manual polyline. You might try to convert your csv to a GPX "track", and import, to force it to display as a line.</p>
<p>Or try to draw a line across the pacific, before the import ?</p>
<p>Please send a CSV file if you want me to try these things.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '20, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73024" class="comments-container">
<span id="73025"></span>
<div id="comment-73025" class="comment">
<div id="post-73025-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any help on this will be very welcome.</p>
<p>How I can convert it to GPX?</p>
<p>The CSV file can be found here <a href="https://stratocat.com.ar/hbal011.csv">https://stratocat.com.ar/hbal011.csv</a></p>
</div>
<div id="comment-73025-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 16:40)</span> <span class="comment-user userinfo">StratoCat</span>
</div>
</div>
</div>
<div id="comment-tools-73024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73024-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73029"></span>

<div id="answer-container-73029" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks so nice now...</p>
<p><img src="/upfiles/map_hbal011good_qPccmb5.jpg" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '20, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/03e8f977ef973cadc48fde64258e2c55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StratoCat&#39;s gravatar image" />
<p><span>StratoCat</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StratoCat has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73029" class="comments-container">
&#10;</div>
<div id="comment-tools-73029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73029-form-container" class="comment-form-container">
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

