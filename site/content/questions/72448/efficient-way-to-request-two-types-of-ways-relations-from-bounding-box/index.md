+++
type = "question"
title = "Efficient way to request two types of ways + relations from bounding box?"
description = '''If I want to search for the ways and relations of highways and buildings within a bounding box, is this the most efficient way to write that query? &quot;[out:xml];(way[highway]({bbox});way[building]({bbox}););(._;&amp;gt;;);out;&quot;  Or is there a more efficient way to specify the bounding box and the ways/rel...'''
date = "2020-01-08T20:35:00Z"
lastmod = "2020-01-13T13:41:00Z"
weight = 72448
keywords = [ "query", "overpass-api" ]
aliases = [ "/questions/72448" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Efficient way to request two types of ways + relations from bounding box?](/questions/72448/efficient-way-to-request-two-types-of-ways-relations-from-bounding-box)

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
<span id="post-72448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72448-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I want to search for the ways and relations of highways and buildings within a bounding box, is this the most efficient way to write that query?</p>
<pre><code>&quot;[out:xml];(way[highway]({bbox});way[building]({bbox}););(._;&gt;;);out;&quot;</code></pre>
<p>Or is there a more efficient way to specify the bounding box and the ways/relations I want within it? I'm using <a href="https://lz4.overpass-api.de/api/interpreter">https://lz4.overpass-api.de/api/interpreter</a></p>
<p>Thanks for taking the time.</p>
<p><strong>edit</strong></p>
<p>To add some more context, we have an application where a user can toggle buildings, roads, railways...etc. So I need to be able to programatically peice together the query. So we get variations like:</p>
<pre><code>&quot;[out:xml];(way[railway]({bbox});way[building]({bbox}););(._;&gt;;);out;&quot;
&quot;[out:xml];(way[highway]({bbox});way[building]({bbox}););(._;&gt;;);out;&quot;
&quot;[out:xml];(way[building]({bbox}););(._;&gt;;);out;&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '20, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/2bf2921024c31d2d4f66c4b4573f19c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kida001&#39;s gravatar image" />
<p><span>kida001</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kida001 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '20, 14:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-72448" class="comments-container">
<span id="72489"></span>
<div id="comment-72489" class="comment">
<div id="post-72489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think this is already the most efficient and most concise query. However I'm not an Overpass API expert.</p>
</div>
<div id="comment-72489-info" class="comment-info">
<span class="comment-age">(13 Jan '20, 13:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72448-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

