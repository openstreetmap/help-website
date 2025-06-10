+++
type = "question"
title = "How do I batch download my GPS traces from OpenStreetmap"
description = '''I&#x27;ve uploaded hundreds of GPS Traces to OSM throughout 2011 and 2012. Until a few months ago, I forgot to save them locally on my computer after uploading them to OSM.  I&#x27;d like to do some Visualizations with them. (Ideally, I&#x27;d like to select ones by tag as well).  How could I download all of them ...'''
date = "2012-04-22T22:45:00Z"
lastmod = "2013-03-23T01:59:00Z"
weight = 12263
keywords = [ "api", "traces", "gps" ]
aliases = [ "/questions/12263" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I batch download my GPS traces from OpenStreetmap](/questions/12263/how-do-i-batch-download-my-gps-traces-from-openstreetmap)

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
<span id="post-12263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12263-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've uploaded hundreds of GPS Traces to OSM throughout 2011 and 2012. Until a few months ago, I forgot to save them locally on my computer after uploading them to OSM.</p>
<p>I'd like to do some <a href="http://avtanski.net/projects/gps/">Visualizations</a> with them. (Ideally, I'd like to select ones by tag as well).</p>
<p>How could I download all of them (besides manually opening every individual trace and then manually downloading them in a web browser) ?</p>
<p>If this isn't easily feasible at the moment, is there anything else in the API (I'm just beginning to look into <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Downloading_Trace_Metadata">Downloading Trace Metadata</a>) that would help me to do this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '12, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '12, 22:46</strong> </span></p>
</div>
</div>
<div id="comments-container-12263" class="comments-container">
&#10;</div>
<div id="comment-tools-12263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12263-form-container" class="comment-form-container">
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

<span id="12302"></span>

<div id="answer-container-12302" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12302-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="skorasaurus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no one-click way of downloading all your traces, but a little scripting work can get them for you. The list of traces you've uploaded is available in XML format at <a href="http://api.openstreetmap.org/api/0.6/user/gpx_files">http://api.openstreetmap.org/api/0.6/user/gpx_files</a> (you might be prompted for your username and password). Extract the URLs from that XML and feed them into something like curl or wget, and you should be able to get all your traces back without having to click on each one in the web interface.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '12, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-12302" class="comments-container">
&#10;</div>
<div id="comment-tools-12302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12302-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20928"></span>

<div id="answer-container-20928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20928-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The latest version of Viking v1.4 has a feature to download ones own GPS Traces.</p>
<p><a href="http://sourceforge.net/projects/viking">http://sourceforge.net/projects/viking</a></p>
<p>In the program itself use File-&gt;Acquire-&gt;My OSM Traces...</p>
<p>This will get a list of all your traces, from this list one can then select the traces you want to get and they will be downloaded into Viking.</p>
<p>Admittedly ATM there is no simple way to then export all traces out to GPX files (other than doing it one by one).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '13, 01:59</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-20928" class="comments-container">
&#10;</div>
<div id="comment-tools-20928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20928-form-container" class="comment-form-container">
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

