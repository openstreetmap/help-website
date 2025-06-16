+++
type = "question"
title = "Feature not found in Map Key"
description = '''With reference the following  https://www.openstreetmap.org/?minlon=-1.4948992729187&amp;amp;minlat=52.4003982543945&amp;amp;maxlon=-1.49384331703186&amp;amp;maxlat=52.4012298583984 zoomed to -1 of maximum zoom, I cannot find the reference to the grey dashed line in the Map Key. Not unless this line is represent...'''
date = "2012-06-07T19:45:00Z"
lastmod = "2012-06-07T20:09:00Z"
weight = 13312
keywords = [ "unrecognised", "map", "feature", "key" ]
aliases = [ "/questions/13312" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Feature not found in Map Key](/questions/13312/feature-not-found-in-map-key)

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
<span id="post-13312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13312-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With reference the following</p>
<p><a href="https://www.openstreetmap.org/?minlon=-1.4948992729187&amp;minlat=52.4003982543945&amp;maxlon=-1.49384331703186&amp;maxlat=52.4012298583984">https://www.openstreetmap.org/?minlon=-1.4948992729187&amp;minlat=52.4003982543945&amp;maxlon=-1.49384331703186&amp;maxlat=52.4012298583984</a></p>
<p>zoomed to -1 of maximum zoom, I cannot find the reference to the grey dashed line in the Map Key. Not unless this line is represented by 'Track' but this looks like a dark purple colour rather than grey.</p>
<p>Please advise</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-unrecognised" rel="tag" title="see questions tagged &#39;unrecognised&#39;">unrecognised</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-feature" rel="tag" title="see questions tagged &#39;feature&#39;">feature</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '12, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/73b493657d462fe0be2e749201ca70b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="surfing69&#39;s gravatar image" />
<p><span>surfing69</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="surfing69 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13312" class="comments-container">
&#10;</div>
<div id="comment-tools-13312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13312-form-container" class="comment-form-container">
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

<span id="13314"></span>

<div id="answer-container-13314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a "<a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpath">highway=path</a>". You can find that out by selecting "browse map data" from below the "edit" menu and clicking on it. Basically, it's something that's not wide enough to be a track (i.e. not wide enough for a four-wheeled vehicle), and normally other tags provide other information (Are you allowed to walk down it? Cycle along it?) but in this case there aren't any. There has been some discussion over the use of highway=path vs e.g. highway=footway - if you're interested you can search the mailing lists and the wiki for that.</p>
<p>It does appear to be missing from the map key. If you want to see if anyone's logged this as a bug before, you can search <a href="https://trac.openstreetmap.org/">trac</a> for it, and if they haven't, log a bug there against component "mapnik". However, the usual caveat applies - the maintainers are all volunteers, and might not get around to adding it to the map key immediately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '12, 20:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13314" class="comments-container">
&#10;</div>
<div id="comment-tools-13314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13314-form-container" class="comment-form-container">
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

