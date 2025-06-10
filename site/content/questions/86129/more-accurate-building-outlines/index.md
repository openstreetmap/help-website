+++
type = "question"
title = "More accurate building outlines"
description = '''Years ago, I manually drew most of the building outlines for the main campus of my employer, the University of Melbourne. The were OK for the time (aerial imagery wasn&#x27;t very good back then), and have served well enough, however, we now use an mapping overlay that exposes many inaccuracies in that o...'''
date = "2022-11-10T04:16:00Z"
lastmod = "2022-11-16T16:00:00Z"
weight = 86129
keywords = [ "building", "editing", "bulk_editing", "data_import" ]
aliases = [ "/questions/86129" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [More accurate building outlines](/questions/86129/more-accurate-building-outlines)

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
<span id="post-86129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86129-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Years ago, I manually drew most of the building outlines for the main campus of my employer, the University of Melbourne. The were OK for the time (aerial imagery wasn't very good back then), and have served well enough, however, we now use an mapping overlay that exposes many inaccuracies in that original data.</p>
<p>I now have access to accurate building outlines, and would like to explore a workflow that would allow me to replace my old manual edits with this shiny new geojson.</p>
<p>So, I have some questions:</p>
<ol>
<li>First one, obviously, is suggestions for a nice workflow - doesn't have to be fully automated, and want to avoid losing any other data/tagging that might have been added to these buildings in the past. So, I'm happy for the process to be semi automated, with manual oversight, as it were.</li>
<li>I will have permission to use the data for this purpose, but what should I do to ensure that permission is recorded? I don't want someone in the future saying I shouldn't have done that, or questioning where the data came from.</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span> <span class="post-tag tag-link-data_import" rel="tag" title="see questions tagged &#39;data_import&#39;">data_import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '22, 04:16</strong></p>
<img src="https://secure.gravatar.com/avatar/e995b919df1004dfbfaf4b7e944e9fcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="woowoowoo&#39;s gravatar image" />
<p><span>woowoowoo</span><br />
<span class="score" title="190 reputation points">190</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="woowoowoo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86129" class="comments-container">
<span id="86167"></span>
<div id="comment-86167" class="comment">
<div id="post-86167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Regarding the second question: One of the steps in the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a> is documenting permission on the OSM wiki.</p>
</div>
<div id="comment-86167-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 16:00)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-86129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86129-form-container" class="comment-form-container">
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

<span id="86132"></span>

<div id="answer-container-86132" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86132-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="woowoowoo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am sure that there are ways of scripting this but if the project is relatively small, maybe less than a few hundred buildings, then I think JOSM and a couple of its plug-ins could be of use to you.</p>
<p>There is a feature called "Replace Geometry" which I think is part of the utilsplugin2 plug in. And the opendata plug in allows you to load things like shape files from a GIS system into a new layer.</p>
<ul>
<li>Load the existing OSM data for the area.</li>
<li>Load the improved building data into a new layer.</li>
<li>Select a new/improved building outline in your new data layer and merge it into the OSM data layer.</li>
<li>Select the new and old outlines and then select "replace geometry"</li>
</ul>
<p>The outline is now updated but has all the old history.</p>
<p>Rinse and repeat for each building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '22, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-86132" class="comments-container">
<span id="86137"></span>
<div id="comment-86137" class="comment">
<div id="post-86137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use the todo pluin to step through the original buildings which will help organise the workflow.</p>
</div>
<div id="comment-86137-info" class="comment-info">
<span class="comment-age">(11 Nov '22, 15:11)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="86155"></span>
<div id="comment-86155" class="comment">
<div id="post-86155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, yes. That sounds exactly the sort of thing I'm after. Going to test that asap - thanks so much. I'm not much of a JOSM user, so I'd never have worked that out.</p>
</div>
<div id="comment-86155-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 06:24)</span> <span class="comment-user userinfo">woowoowoo</span>
</div>
</div>
</div>
<div id="comment-tools-86132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86132-form-container" class="comment-form-container">
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

