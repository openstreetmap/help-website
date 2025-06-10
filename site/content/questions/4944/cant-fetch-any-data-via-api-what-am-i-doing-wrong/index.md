+++
type = "question"
title = "Can&#x27;t fetch any data via API, what am I doing wrong?"
description = '''Hello, Is there any particular reason the following request return nothing: http://api06.dev.openstreetmap.org/api/0.6/map?bbox=25.4649353,42.1389684,25.8892822,42.5075400? Actually it is not &quot;nothing&quot;, but this: &amp;lt;osm version=&#x27;0.6&#x27; generator=&#x27;OpenStreetMap server&#x27;&amp;gt;&amp;lt;/osm&amp;gt; I tried using XA...'''
date = "2011-05-03T07:07:00Z"
lastmod = "2011-05-04T07:31:00Z"
weight = 4944
keywords = [ "api", "xapi" ]
aliases = [ "/questions/4944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't fetch any data via API, what am I doing wrong?](/questions/4944/cant-fetch-any-data-via-api-what-am-i-doing-wrong)

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
<span id="post-4944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4944-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Is there any particular reason the following request return nothing: <strong><a href="http://api06.dev.openstreetmap.org/api/0.6/map?bbox=25.4649353,42.1389684,25.8892822,42.5075400">http://api06.dev.openstreetmap.org/api/0.6/map?bbox=25.4649353,42.1389684,25.8892822,42.5075400</a></strong>? Actually it is not "nothing", but this:</p>
<p><code>&lt;osm version='0.6' generator='OpenStreetMap server'&gt;&lt;/osm&gt;</code></p>
<p>I tried using XAPI with this request: <strong><a href="http://xapi.openstreetmap.org/api/0.6/node%5Bplace=city%5D%5Bbbox=25.4649353,42.1389684,25.8892822,42.5075400%5D">http://xapi.openstreetmap.org/api/0.6/node[place=city][bbox=25.4649353,42.1389684,25.8892822,42.5075400]</a></strong> but this time I really got nothing. As I can see the XAPI servers are pretty overloaded. Is there any way to use it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '11, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-4944" class="comments-container">
&#10;</div>
<div id="comment-tools-4944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4944-form-container" class="comment-form-container">
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

<span id="4946"></span>

<div id="answer-container-4946" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4946-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-4946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first request is being made to the "api06" testing server - it doesn't contain much map data so it's quite likely that there won't be data in that area. You can edit the testing server to add some test data for whichever area you're interested in.</p>
<p>The XAPI link is to servers using the "live" data from <a href="http://www.osm.org">www.osm.org</a> - but they are often overloaded. You can try the <a href="http://wiki.openstreetmap.org/wiki/Xapi">alternative XAPI servers</a> listed on the wiki - try the ones running the Java version of XAPI.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '11, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-4946" class="comments-container">
<span id="4976"></span>
<div id="comment-4976" class="comment">
<div id="post-4976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What happens if I edit to the test server? How long will the data be kept? I suppose it is cleared at some intervals?</p>
</div>
<div id="comment-4976-info" class="comment-info">
<span class="comment-age">(04 May '11, 06:39)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="4977"></span>
<div id="comment-4977" class="comment">
<div id="post-4977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For all I know the dev server isn't cleared regularily so the data will probably linger at least till development on the API 0.7 starts in a large scale way. Depending what you want to do (you don't really say) this might be plenty of time.</p>
</div>
<div id="comment-4977-info" class="comment-info">
<span class="comment-age">(04 May '11, 07:31)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-4946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4946-form-container" class="comment-form-container">
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

