+++
type = "question"
title = "Is there a command line tool that auto-remove a region from GPS traces"
description = '''The background, I may have what I think is a specific data privacy case. I have many GPS traces (~500 gpx files), between 3 locations. where i live, work &amp;amp; remote work. Most records are 10-60Km, more than a hundred are +100K (max 800Km). Currently on OSM, Those 3 location lack GPS traces. If I u...'''
date = "2021-10-10T11:37:00Z"
lastmod = "2021-10-11T08:16:00Z"
weight = 82103
keywords = [ "gps-traces", "tools", "gps" ]
aliases = [ "/questions/82103" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a command line tool that auto-remove a region from GPS traces](/questions/82103/is-there-a-command-line-tool-that-auto-remove-a-region-from-gps-traces)

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
<span id="post-82103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82103-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The background, I may have what I think is a specific data privacy case.</p>
<p>I have many GPS traces (~500 gpx files), between 3 locations. where i live, work &amp; remote work. Most records are 10-60Km, more than a hundred are +100K (max 800Km).</p>
<p>Currently on OSM, Those 3 location lack GPS traces. If I upload these traces even 'public', they will show and centralize exactly where I am based.</p>
<p>So to fix this, I just want to automatically cut out a GPS range (square or circle) like 1-5Km radius (like a blind area). So is there a tool, command-line preferred, that make that easy for me? Or is there other easier way around it?</p>
<p>I already tried GPSPrune (GUI) manually cut edges and high error sections, but that was a strenuous task. Really took me 3-4h to cleanup ±100 traces.</p>
<p>Also, I probably end up writing a script using <code>gpxpy</code> python module to delete all point in a custom range, if there is no tool yet for such specific job.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gps-traces" rel="tag" title="see questions tagged &#39;gps-traces&#39;">gps-traces</span> <span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '21, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e92fe66c5f5cf0346f5f9ddc01b93711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bean&#39;s gravatar image" />
<p><span>Bean</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bean has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '21, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-82103" class="comments-container">
&#10;</div>
<div id="comment-tools-82103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82103-form-container" class="comment-form-container">
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

<span id="82104"></span>

<div id="answer-container-82104" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82104-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bean has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>gpsbabel (<a href="https://www.gpsbabel.org">https://www.gpsbabel.org</a>) is your friend! It has a method to "include only points within a polygon" and that has a flag that says "uh, change the logic, <em>exclude</em> these points please".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '21, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82104" class="comments-container">
<span id="82118"></span>
<div id="comment-82118" class="comment">
<div id="post-82118-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I checked its GUI before I overpass it. Surprised to how advanced its CLI ( <a href="https://www.gpsbabel.org/htmldoc-development/filter_polygon.html">https://www.gpsbabel.org/htmldoc-development/filter_polygon.html</a> ). Thank you.</p>
</div>
<div id="comment-82118-info" class="comment-info">
<span class="comment-age">(11 Oct '21, 08:16)</span> <span class="comment-user userinfo">Bean</span>
</div>
</div>
</div>
<div id="comment-tools-82104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82104-form-container" class="comment-form-container">
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

