+++
type = "question"
title = "Help updating OSM data using flat nodes file"
description = '''Can someone help me on this question? I&#x27;m importing the OSM planet to my PostgreSQL using the flat file option. Now I have my database and my flat nodes file, I want to apply some diffs files. After reading this :  Lastly, since you have to reimport for --flat-nodes, you should make sure to download...'''
date = "2017-04-05T01:28:00Z"
lastmod = "2017-04-10T13:22:00Z"
weight = 55478
keywords = [ "openstreetmap", "flatnode", "data_import" ]
aliases = [ "/questions/55478" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help updating OSM data using flat nodes file](/questions/55478/help-updating-osm-data-using-flat-nodes-file)

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
<span id="post-55478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can someone help me on this question?</p>
<p>I'm importing the OSM planet to my PostgreSQL using the flat file option.</p>
<p>Now I have my database and my flat nodes file, I want to apply some diffs files.</p>
<p>After reading <a href="http://gis.stackexchange.com/questions/94352/update-database-via-osmosis-and-osm2pgsql-too-slow">this</a> :</p>
<blockquote>
<p>Lastly, since you have to reimport for --flat-nodes, you should make sure to download a new Europe extract, and make sure to download PBF, not bzipped XML.</p>
</blockquote>
<p>I understood I need to download the diff file and ALL planet file again. Is it correct? By importing without the flat file option and keeping all temp tables in database, I just need the diff file to do the update.</p>
<p>Please explain the correct process to apply diff updates using the flat nodes file.</p>
<p><a href="http://gis.stackexchange.com/questions/233988/how-to-update-osm-planet-diffs-using-flat-nodes-file">http://gis.stackexchange.com/questions/233988/how-to-update-osm-planet-diffs-using-flat-nodes-file</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-flatnode" rel="tag" title="see questions tagged &#39;flatnode&#39;">flatnode</span> <span class="post-tag tag-link-data_import" rel="tag" title="see questions tagged &#39;data_import&#39;">data_import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '17, 01:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c348fb62735602366d2d22d94482bd90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlos%20M%20Abreu&#39;s gravatar image" />
<p><span>Carlos M Abreu</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlos M Abreu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55478" class="comments-container">
&#10;</div>
<div id="comment-tools-55478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55478-form-container" class="comment-form-container">
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

<span id="55480"></span>

<div id="answer-container-55480" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55480-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carlos M Abreu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "since you have to reimport..." quote above was in response to someone who had <em>not</em> used the <code>--flatnodes</code> option during import hence it doesn't apply to you.</p>
<p>Applying diff updates with or without flat nodes is the same procedure, just that one needs the <code>--flatnodes</code> option on initial import <em>and</em> update, the other not.</p>
<p>You need to download all the diffs since your planet file was created, and apply them. For best performance, combine the diffs into one before you run osm2pgsql (using e.g. osmosis). If you want to configure continuous updates, use the <code>--rrii</code> Osmosis option initially and then <code>--rri</code> for each update. If you don't like to take guesses about when to start your replication, you can find out the highest node ID in your flat node file (osm2pgsql, when started in append mode, will usually say "highest node id in flat nodes file is ..."), then use the <a href="https://svn.openstreetmap.org/applications/utils/whichdiff/">https://svn.openstreetmap.org/applications/utils/whichdiff/</a> utility to find the matching state.txt.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Apr '17, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55480" class="comments-container">
<span id="55544"></span>
<div id="comment-55544" class="comment">
<div id="post-55544-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Very well explained! Many thanks. I spent 50 points of my reputation in GIS S.E. for nothing .... <code>:-(</code></p>
</div>
<div id="comment-55544-info" class="comment-info">
<span class="comment-age">(10 Apr '17, 13:22)</span> <span class="comment-user userinfo">Carlos M Abreu</span>
</div>
</div>
</div>
<div id="comment-tools-55480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55480-form-container" class="comment-form-container">
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

