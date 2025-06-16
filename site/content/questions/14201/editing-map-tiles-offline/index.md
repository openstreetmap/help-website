+++
type = "question"
title = "Editing map tiles offline"
description = '''I am trying to dynamically add and update overlays on a map. Currently I am using mapping API&#x27;s and javascript to accomplish this. However, I want a way to still do this even without internet access. Is there a way to use the API&#x27;s offline? Or is there a suitable program I can use to accomplish the ...'''
date = "2012-07-11T22:51:00Z"
lastmod = "2012-07-11T23:20:00Z"
weight = 14201
keywords = [ "offline", "api" ]
aliases = [ "/questions/14201" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Editing map tiles offline](/questions/14201/editing-map-tiles-offline)

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
<span id="post-14201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to dynamically add and update overlays on a map. Currently I am using mapping API's and javascript to accomplish this. However, I want a way to still do this even without internet access. Is there a way to use the API's offline? Or is there a suitable program I can use to accomplish the same dynamic structure be serving up my own tiles offline?</p>
<p>Thank you for any advice</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c885f57a2b31354461e362485e0b026b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d_norm&#39;s gravatar image" />
<p><span>d_norm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d_norm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14201" class="comments-container">
&#10;</div>
<div id="comment-tools-14201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14201-form-container" class="comment-form-container">
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

<span id="14203"></span>

<div id="answer-container-14203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you (and google) call an "api" is probably nothing more then a javascript library (probably OpenLayers or Leaflet). You can download these libraries and host them yourself if you want.</p>
<p>However the tile layers you use is tiled images that are hosted by other services. Theese might not be available for offline use. It is possible to install a service to render the tiles on the local machine, or you could use the <a href="https://wiki.openstreetmap.org/wiki/Kothic_JS">Kothic JS</a> plugin for Leaflet to render the tiles in the browser.</p>
<p>In both cases you need to download the vector data before you can use it offline and that will require some space and bandwidth and for your users to select areas to be available for offline use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 23:20</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 23:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14203" class="comments-container">
&#10;</div>
<div id="comment-tools-14203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14203-form-container" class="comment-form-container">
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

