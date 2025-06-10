+++
type = "question"
title = "Out of Memory on a simple request"
description = '''This simple request return: &quot;error: Query run out of memory using about 2048 MB of RAM.&quot; The bbox could very small 1km2. It does not matter. The bbox location could be everywhere it does not matter. If the date constraint is not set everything is fine. If removing =&quot;yes&quot;, just with building, everyth...'''
date = "2022-05-13T08:09:00Z"
lastmod = "2022-05-15T22:51:00Z"
weight = 84459
keywords = [ "building", "overpass-turbo" ]
aliases = [ "/questions/84459" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Out of Memory on a simple request](/questions/84459/out-of-memory-on-a-simple-request)

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
<span id="post-84459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84459-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This simple request return: "error: Query run out of memory using about 2048 MB of RAM." The bbox could very small 1km2. It does not matter. The bbox location could be everywhere it does not matter. If the date constraint is not set everything is fine. If removing ="yes", just with building, everything is fine as well.</p>
<pre><code>[out:xml][timeout:900][date:&quot;2021-08-10T12:00:00Z&quot;];
(
  nwr[building=&quot;yes&quot;]({{bbox}});
);
(._;&gt;;);
out body;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '22, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/357c2bfb40b8a695f7458ed4dc1942fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michel%20BENET&#39;s gravatar image" />
<p><span>Michel BENET</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michel BENET has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '22, 11:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-84459" class="comments-container">
<span id="84486"></span>
<div id="comment-84486" class="comment">
<div id="post-84486-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This doesn't seem to be a question.</p>
</div>
<div id="comment-84486-info" class="comment-info">
<span class="comment-age">(15 May '22, 22:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84459-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

