+++
type = "question"
title = "Get way based on direction of travel"
description = '''I have this simple query, assuming that we know which direction and road the user travelling (heading), I want to get only that side of the highway, if it&#x27;s a two way road that should also be selected. Picture example of what I&#x27;m looking for {{geocodeArea:Hamburg}}-&amp;gt;.searchArea; way[name=&quot;Sülldor...'''
date = "2021-09-24T21:32:00Z"
lastmod = "2021-09-24T21:32:00Z"
weight = 81943
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/81943" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get way based on direction of travel](/questions/81943/get-way-based-on-direction-of-travel)

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
<span id="post-81943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this simple query, assuming that we know which direction and road the user travelling (heading), I want to get only that side of the highway, if it's a two way road that should also be selected.</p>
<p><span>Picture example of what I'm looking for</span></p>
<pre><code>{{geocodeArea:Hamburg}}-&gt;.searchArea;
way[name=&quot;Sülldorfer Landstraße&quot;](area.searchArea);
out geom;</code></pre>
<p><a href="http://overpass-turbo.eu/s/1btn">overpass-turbo query above</a></p>
<p>How do I achieve this? If this requires post processing that would also be a viable option.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '21, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/b0a0e0831b05e3dd9a24e805b38b38c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="this%20is%20jack&#39;s gravatar image" />
<p><span>this is jack</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="this is jack has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81943" class="comments-container">
&#10;</div>
<div id="comment-tools-81943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81943-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

