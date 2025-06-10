+++
type = "question"
title = "Overpass API: Diff from bbox"
description = '''I have an application which uses OSM data, but from one city only, which I got the data for using a query: http://overpass-api.de/api/map?bbox=20.8672,52.1010,21.2723,52.3668  I use information about nodes and ways, put them in my database and then do some calculations on them. Now time has passed a...'''
date = "2016-04-01T12:05:00Z"
lastmod = "2016-04-01T16:11:00Z"
weight = 48994
keywords = [ "download", "overpass", "api" ]
aliases = [ "/questions/48994" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Diff from bbox](/questions/48994/overpass-api-diff-from-bbox)

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
<span id="post-48994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48994-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an application which uses OSM data, but from one city only, which I got the data for using a query:</p>
<pre><code>http://overpass-api.de/api/map?bbox=20.8672,52.1010,21.2723,52.3668</code></pre>
<p>I use information about nodes and ways, put them in my database and then do some calculations on them. Now time has passed and the data changed. I'd like to see what changed, so that I can update (without dropping all the data and inserting it again)</p>
<p>Is there a way, to query <code>overpass-api</code> to give me diff of a selected area (and not only nodes or ways, but both) ? I've read the doc, but didn't find the way to combine <code>diff</code> and <code>bbox</code> in one query.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '16, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/3e73428522352ea6f8b8488b21e8fc24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prajmus&#39;s gravatar image" />
<p><span>prajmus</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prajmus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48994" class="comments-container">
<span id="48999"></span>
<div id="comment-48999" class="comment">
<div id="post-48999-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Cross posted: <a href="http://stackoverflow.com/questions/36350382/openstreetmap-diff-from-a-bounding-box">http://stackoverflow.com/questions/36350382/openstreetmap-diff-from-a-bounding-box</a></p>
</div>
<div id="comment-48999-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 16:11)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48994-form-container" class="comment-form-container">
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

<span id="48998"></span>

<div id="answer-container-48998" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48998-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="prajmus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The /map query is part of the XAPI compatibility layer:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer">http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer</a></p>
<p>Here's a roughly equivalent query using the Overpass API query language:</p>
<p><a href="http://overpass-turbo.eu/s/foV">http://overpass-turbo.eu/s/foV</a></p>
<p>(fetches nodes in the bounding box and also any parent objects. To see the query url, look under "Export" for the "raw data directly from Overpass API" link.)</p>
<p>A global diff statement can be added to that query:</p>
<p><a href="http://overpass-turbo.eu/s/foW">http://overpass-turbo.eu/s/foW</a></p>
<p>(returns nothing)</p>
<p>It'll probably be some work to figure out what's in the diff and so on, but the global diff setting is what you are looking for. You may also want to take a look at the augmented diff:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Delta_between_two_dates_.28.22diff.22.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Delta_between_two_dates_.28.22diff.22.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '16, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48998" class="comments-container">
&#10;</div>
<div id="comment-tools-48998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48998-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48997"></span>

<div id="answer-container-48997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48997-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am quite unfamiliar with overpass but by coincidence have been perusing the web documentation in the last few hours and I found that 'newer' and 'changed' under Filters at this site may be what you need if you can download Attic data. The difference block statement may be suitable if you can do your query on both todays data and the date you did your extract. <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
<p>Also as reference: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '16, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '16, 14:41</strong> </span></p>
</div>
</div>
<div id="comments-container-48997" class="comments-container">
&#10;</div>
<div id="comment-tools-48997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48997-form-container" class="comment-form-container">
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

