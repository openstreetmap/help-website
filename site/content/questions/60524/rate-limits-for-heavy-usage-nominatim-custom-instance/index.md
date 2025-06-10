+++
type = "question"
title = "Rate Limits for heavy usage Nominatim custom instance"
description = '''Hi , We run our own nominatim instance because we make heavy use for a custom gps system. ( 14 Million aprox requests per day, that is 10,000 clients requesting reverse geocoding every 1 minute ) , Could someone please point me to the reference documents or explain me how the connection buckets cons...'''
date = "2017-11-09T18:18:00Z"
lastmod = "2017-11-13T22:41:00Z"
weight = 60524
keywords = [ "config", "nominatim", "rates", "limits", "heavy_usage" ]
aliases = [ "/questions/60524" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rate Limits for heavy usage Nominatim custom instance](/questions/60524/rate-limits-for-heavy-usage-nominatim-custom-instance)

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
<span id="post-60524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60524-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi ,</p>
<p>We run our own nominatim instance because we make heavy use for a custom gps system. ( 14 Million aprox requests per day, that is 10,000 clients requesting reverse geocoding every 1 minute ) , Could someone please point me to the reference documents or explain me how the connection buckets constants affect my rate limits etc . I want to have no limits on requests per second , per ip , etc. It seems that after a couple of hours the nominatim server stops working , but all the cpu , memory metrics etc are fine . We have even tried with super size configuration ( We run it on Amazon web services ).</p>
<p>Thanks</p>
<p>This are found in /settings/settings.php</p>
<pre><code> // Connection buckets to rate limit people being nasty
    @define(&#39;CONST_ConnectionBucket_MemcacheServerAddress&#39;, false);
    @define(&#39;CONST_ConnectionBucket_MemcacheServerPort&#39;, 11211);
    @define(&#39;CONST_ConnectionBucket_MaxBlockList&#39;, 100);
    @define(&#39;CONST_ConnectionBucket_LeakRate&#39;, 1);
    @define(&#39;CONST_ConnectionBucket_BlockLimit&#39;, 10);
    @define(&#39;CONST_ConnectionBucket_WaitLimit&#39;, 6);
    @define(&#39;CONST_ConnectionBucket_MaxSleeping&#39;, 10);
    @define(&#39;CONST_ConnectionBucket_Cost_Reverse&#39;, 1);
    @define(&#39;CONST_ConnectionBucket_Cost_Search&#39;, 2);
    @define(&#39;CONST_ConnectionBucket_Cost_Details&#39;, 3);
    @define(&#39;CONST_ConnectionBucket_Cost_Status&#39;, 1);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-config" rel="tag" title="see questions tagged &#39;config&#39;">config</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-rates" rel="tag" title="see questions tagged &#39;rates&#39;">rates</span> <span class="post-tag tag-link-limits" rel="tag" title="see questions tagged &#39;limits&#39;">limits</span> <span class="post-tag tag-link-heavy_usage" rel="tag" title="see questions tagged &#39;heavy_usage&#39;">heavy_usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '17, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1c09d5877ba75bd717c9d58103237ac5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GUIMO&#39;s gravatar image" />
<p><span>GUIMO</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GUIMO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '17, 20:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-60524" class="comments-container">
&#10;</div>
<div id="comment-tools-60524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60524-form-container" class="comment-form-container">
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

<span id="60529"></span>

<div id="answer-container-60529" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60529-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to provide a memcached server to enable rate limiting. If you have a line like this</p>
<pre><code>@define(&#39;CONST_ConnectionBucket_MemcacheServerAddress&#39;, false);</code></pre>
<p>then rate limiting is off (which is the default). Also note that the rate limiting code has been completely removed since Nominatim 3.0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '17, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-60529" class="comments-container">
<span id="60602"></span>
<div id="comment-60602" class="comment">
<div id="post-60602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It means that by default it is not applying any rate limit and my issue is somewhere else. Thanks for your knowledge</p>
</div>
<div id="comment-60602-info" class="comment-info">
<span class="comment-age">(13 Nov '17, 22:41)</span> <span class="comment-user userinfo">GUIMO</span>
</div>
</div>
</div>
<div id="comment-tools-60529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60529-form-container" class="comment-form-container">
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

