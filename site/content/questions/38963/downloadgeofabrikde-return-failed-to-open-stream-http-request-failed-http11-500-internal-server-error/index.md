+++
type = "question"
title = "download.geofabrik.de return  failed to open stream: HTTP request failed! HTTP/1.1 500 Internal Server Error"
description = '''i have installed nominatim(europe) but not yet started update process for more than 5 months.  Now i started update process for europe from download.geofabrik.de.  this is my configuration  @define(&#x27;CONST_Replication_Url&#x27;, &#x27;http://download.geofabrik.de/europe-updates&#x27;);  @define(&#x27;CONST_Replication_M...'''
date = "2014-12-01T11:44:00Z"
lastmod = "2014-12-01T13:03:00Z"
weight = 38963
keywords = [ "osm", "geofabrik", "osmosis" ]
aliases = [ "/questions/38963" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [download.geofabrik.de return failed to open stream: HTTP request failed! HTTP/1.1 500 Internal Server Error](/questions/38963/downloadgeofabrikde-return-failed-to-open-stream-http-request-failed-http11-500-internal-server-error)

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
<span id="post-38963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38963-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i have installed nominatim(europe) but not yet started update process for more than 5 months. Now i started update process for europe from download.geofabrik.de.</p>
<p><strong>this is my configuration</strong> <em>@define('CONST_Replication_Url', 'http://download.geofabrik.de/europe-updates'); @define('CONST_Replication_MaxInterval', '40000'); // Process each update separately, osmosis cannot merge multiple updates @define('CONST_Replication_Update_Interval', '86400'); // How often upstream publishes diffs @define('CONST_Replication_Recheck_Interval', '900'); // How long to sleep if no update found yet</em></p>
<p>its keep on download and index data for 8 to 10 days. After that it shows error that <em>failed to open stream: HTTP request failed! HTTP/1.1 500 Internal Server Error</em></p>
<p>there is any restriction in number of downloads in download.geofabrik.de server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '14, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38963" class="comments-container">
&#10;</div>
<div id="comment-tools-38963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38963-form-container" class="comment-form-container">
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

<span id="38967"></span>

<div id="answer-container-38967" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>downloading five months of updates and applying them will probably take <em>longer</em> than downloading the full data file and importing it afresh!</p>
<p>The server will let you download about 30 files a day so you would have to space your downloads a bit.</p>
<p>thank you Frederik Ramm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '14, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38967" class="comments-container">
&#10;</div>
<div id="comment-tools-38967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38967-form-container" class="comment-form-container">
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

