+++
type = "question"
title = "Visibility of roads in multiple layers"
description = '''Good morning: I am relatively new to OSM, but not new to map creation. Struggling with making a road appear in more than one layer. When you create the road (painfully hand traced from GPS data), you assign it a layer. However, when you zoom on the &#x27;view map&#x27;, the road only appears in a particular z...'''
date = "2012-07-11T05:41:00Z"
lastmod = "2012-07-11T07:03:00Z"
weight = 14161
keywords = [ "layer", "copy", "visibility" ]
aliases = [ "/questions/14161" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Visibility of roads in multiple layers](/questions/14161/visibility-of-roads-in-multiple-layers)

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
<span id="post-14161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good morning:</p>
<p>I am relatively new to OSM, but not new to map creation. Struggling with making a road appear in more than one layer.</p>
<p>When you create the road (painfully hand traced from GPS data), you assign it a layer. However, when you zoom on the 'view map', the road only appears in a particular zoom level.</p>
<p>How, short of repeating the tracing exercise, does one create the road so that it can appear in both low level and higher level zooms?</p>
<p>Cheers</p>
<p>Eric</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-copy" rel="tag" title="see questions tagged &#39;copy&#39;">copy</span> <span class="post-tag tag-link-visibility" rel="tag" title="see questions tagged &#39;visibility&#39;">visibility</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 05:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e0c55610b67eb7f23b6b765f25b95c11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AHSommer&#39;s gravatar image" />
<p><span>AHSommer</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AHSommer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14161" class="comments-container">
&#10;</div>
<div id="comment-tools-14161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14161-form-container" class="comment-form-container">
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

<span id="14162"></span>

<div id="answer-container-14162" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14162-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AHSommer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect you are seeing cached tiles that were generated before you added the road. If you try clearing your browser cache (sometimes shift-F5 works) then you might see your road at all zoom levels. For example, <a href="https://www.openstreetmap.org/browse/way/170999347/history">this way</a> I currently see as an unclassified road (v2) at some zoom levels and the track (v1) at others. Choosing one of the areas where I could see it as a track, clicking permalink to remember where I was looking, then clicking shift-refresh changed the track to an unclassified road.</p>
<p>Tracks don't appear on as many levels as unclassified roads, however, and this is down to the rendering rules used, and could differ for every different rendering of the data. The four renderings available on the <a href="http://www.osm.org">www.osm.org</a> homepage are just some examples.</p>
<p>Edit: I did note while looking at the area that if you zoom right in, some of the roads in the area are almost joined, but not quite, e.g. <a href="http://osm.org/go/k09dt6DVO--">here</a>. If you've not watched <a href="http://vimeo.com/24984085">this video</a> about adding ways before, then it might be worth a quick look - I found it mentioned on <a href="https://wiki.openstreetmap.org/wiki/Potlatch2#How_to_use_Potlatch_2">the wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 06:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 06:55</strong> </span></p>
</div>
</div>
<div id="comments-container-14162" class="comments-container">
<span id="14163"></span>
<div id="comment-14163" class="comment">
<div id="post-14163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - silly of me not to have thought of that!</p>
</div>
<div id="comment-14163-info" class="comment-info">
<span class="comment-age">(11 Jul '12, 07:03)</span> <span class="comment-user userinfo">AHSommer</span>
</div>
</div>
</div>
<div id="comment-tools-14162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14162-form-container" class="comment-form-container">
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

