+++
type = "question"
title = "How do I get the ID of the newest GPX file uploaded to OpenStreetMap?"
description = '''I have a program that downloads and process GPX tracks from OpenStreetMap using: https://www.openstreetmap.org/traces/{ID}/data But how can I find the ID of the latest uploaded GPX file? Currently I get the ID from: https://www.openstreetmap.org/traces But that data is mostly meant to be read by human...'''
date = "2010-09-08T07:15:00Z"
lastmod = "2010-09-10T16:23:00Z"
weight = 752
keywords = [ "api", "gpx", "robot" ]
aliases = [ "/questions/752" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I get the ID of the newest GPX file uploaded to OpenStreetMap?](/questions/752/how-do-i-get-the-id-of-the-newest-gpx-file-uploaded-to-openstreetmap)

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
<span id="post-752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-752-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a program that downloads and process GPX tracks from OpenStreetMap using:</p>
<p><a href="https://www.openstreetmap.org/traces/%7BID%7D/data">https://www.openstreetmap.org/traces/{ID}/data</a></p>
<p>But how can I find the ID of the latest uploaded GPX file?</p>
<p>Currently I get the ID from:</p>
<p><a href="https://www.openstreetmap.org/traces">https://www.openstreetmap.org/traces</a></p>
<p>But that data is mostly meant to be read by humans, and needs a lot of parsing - is there a better way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-robot" rel="tag" title="see questions tagged &#39;robot&#39;">robot</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '10, 07:15</strong></p>
<img src="https://secure.gravatar.com/avatar/caab86c316876f87a66042c4a9553691?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Johnny%20Carlsen&#39;s gravatar image" />
<p><span>Johnny Carlsen</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Johnny Carlsen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-752" class="comments-container">
<span id="774"></span>
<div id="comment-774" class="comment">
<div id="post-774-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your question is fine as it is, but it's very specific. If you can tell us more about what you're trying to do in general, there may be a way of acheiving it without having to scrape the traces page.</p>
</div>
<div id="comment-774-info" class="comment-info">
<span class="comment-age">(10 Sep '10, 16:23)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-752-form-container" class="comment-form-container">
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

<span id="766"></span>

<div id="answer-container-766" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-766-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well you can always use <a href="https://www.openstreetmap.org/traces/rss">the rss feed</a>, just extracting the link element with a regexp will work.</p>
<pre><code>([0-9]*)&lt;/link&gt;</code></pre>
<p>e.g</p>
<pre><code>curl https://www.openstreetmap.org/traces/rss |
sed -r &#39;s|.+s/([0-9]+)&lt;/link&gt;|\1|;t;d&#39;|
head -1</code></pre>
<p>But compare that to parsing the html page there is almost no gain.</p>
<pre><code>href=&quot;/user/[^/]*/traces/([0-9]*)&quot;
href=&quot;/edit?gpx=([0-9]*)&quot;</code></pre>
<p>e.g.:</p>
<pre><code>wget -O - &quot;https://www.openstreetmap.org/traces&quot; |
sed &#39;/traces/!d; s|.* href=&quot;/user/[^/]*/traces/\([0-9]*\)&quot; .*|https://www.openstreetmap.org/traces/\1/data|;t;d&#39;|
head -1</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '10, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '10, 00:03</strong> </span></p>
</div>
</div>
<div id="comments-container-766" class="comments-container">
&#10;</div>
<div id="comment-tools-766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-766-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="753"></span>

<div id="answer-container-753" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-753-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_Traces">API</a> doesn't seem to have a way of retrieving the newest GPX trace ID, here is an example of a shell command to grab the ID from the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_Traces">traces page</a>:</p>
<pre><code>curl -s &quot;https://www.openstreetmap.org/traces&quot; | grep -m 1 &quot;/edit?gpx=&quot; | cut -d &quot;=&quot; -f3 | cut -d &quot;\&quot;&quot; -f1</code></pre>
<p>But of course this might stop working in the future as the layout of the page may change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '10, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-753" class="comments-container">
&#10;</div>
<div id="comment-tools-753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-753-form-container" class="comment-form-container">
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

