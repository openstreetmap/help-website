+++
type = "question"
title = "How to include the boundary roads in a query for roads within a town?"
description = '''A suburb called Beaconsfield (NSW, Australia) is bounded by six streets and four other suburbs. The following query lists a total of nine streets in the suburb, None of the bounding streets are included in that list. [out:csv(&quot;name&quot;;false)] [bbox:-33.9142158, 151.1919887, -33.9066269, 151.2080568]; ...'''
date = "2020-08-19T06:57:00Z"
lastmod = "2020-08-19T06:57:00Z"
weight = 76204
keywords = [ "town", "boundary", "inside" ]
aliases = [ "/questions/76204" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to include the boundary roads in a query for roads within a town?](/questions/76204/how-to-include-the-boundary-roads-in-a-query-for-roads-within-a-town)

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
<span id="post-76204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76204-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A suburb called Beaconsfield (NSW, Australia) is bounded by six streets and four other suburbs. The following query lists a total of nine streets in the suburb, None of the bounding streets are included in that list.</p>
<p>[out:csv("name";false)] [bbox:-33.9142158, 151.1919887, -33.9066269, 151.2080568]; area[name="Beaconsfield"]; way(area)[highway][name]; out;</p>
<p>Visual inspection of the map confirms the presence of the nine streets in Beaconsfield and six boundary streets.</p>
<p>Similar queries of the adjoining suburbs demonstrates that five of the six boundary streets are not included in those suburbs either. The one exception occurs because that street projects past the boundary into the adjoining suburb.</p>
<p>What is the query for listing roads within and on the boundary of a town?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-inside" rel="tag" title="see questions tagged &#39;inside&#39;">inside</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '20, 06:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76204" class="comments-container">
&#10;</div>
<div id="comment-tools-76204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76204-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

