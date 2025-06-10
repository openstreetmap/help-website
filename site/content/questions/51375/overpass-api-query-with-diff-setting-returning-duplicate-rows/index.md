+++
type = "question"
title = "Overpass API query with diff setting returning duplicate rows"
description = '''Hi, Can anybody please explain to me why this Overpass API query returns in part duplicate rows? Is there anyway I can automatically remove the duplicates? [timeout:500][out:csv(::&quot;id&quot;, amenity, name; true; &quot;;&quot;)] [diff:&quot;2016-01-05T00:00:00Z&quot;,&quot;2016-05-31T24:00:00Z&quot;]; area[&quot;name&quot;=&quot;Groningen&quot;][&quot;admin_l...'''
date = "2016-08-12T19:20:00Z"
lastmod = "2016-08-12T20:13:00Z"
weight = 51375
keywords = [ "overpass", "api", "diff" ]
aliases = [ "/questions/51375" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API query with diff setting returning duplicate rows](/questions/51375/overpass-api-query-with-diff-setting-returning-duplicate-rows)

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
<span id="post-51375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Can anybody please explain to me why this Overpass API query returns in part duplicate rows? Is there anyway I can automatically remove the duplicates?</p>
<pre><code>[timeout:500][out:csv(::&quot;id&quot;, amenity, name; true; &quot;;&quot;)]
[diff:&quot;2016-01-05T00:00:00Z&quot;,&quot;2016-05-31T24:00:00Z&quot;];
area[&quot;name&quot;=&quot;Groningen&quot;][&quot;admin_level&quot;=&quot;10&quot;];
node[&quot;amenity&quot;=&quot;cafe&quot;](area);
out;</code></pre>
<p>Best regards,</p>
<p>Willy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '16, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/45dda8733f1636de07c44e39dee439c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friesewoudloper&#39;s gravatar image" />
<p><span>friesewoudloper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friesewoudloper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51375" class="comments-container">
&#10;</div>
<div id="comment-tools-51375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51375-form-container" class="comment-form-container">
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

<span id="51376"></span>

<div id="answer-container-51376" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51376-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I've got the answer. I changed the output format to xml. Then I saw in the output that all the duplicate rows have a parameter <code>type="modify"</code> and the non-duplicate ones <code>type="create"</code>. So I guess the duplicate rows are nodes that were modified during the time period and the non-duplicate ones were newly created. Am I right?</p>
<p>Willy</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '16, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/45dda8733f1636de07c44e39dee439c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friesewoudloper&#39;s gravatar image" />
<p><span>friesewoudloper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friesewoudloper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51376" class="comments-container">
<span id="51378"></span>
<div id="comment-51378" class="comment">
<div id="post-51378-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The main issue here is that CSV output doesn't really play well with the <code>diff</code> setting. You probably should file an issue for that: <a href="https://github.com/drolbr/Overpass-API/issues">https://github.com/drolbr/Overpass-API/issues</a></p>
</div>
<div id="comment-51378-info" class="comment-info">
<span class="comment-age">(12 Aug '16, 20:13)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51376-form-container" class="comment-form-container">
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

