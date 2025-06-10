+++
type = "question"
title = "osmcoastline / Land polygons"
description = '''Hello,  I have downloaded land polygons from https://osmdata.openstreetmap.de/download/land-polygons-split-4326.zip The data seems to be nice ordered in cells of size one degree. I however have a problem, that there is used a certain overlap-area between each cell. I would need the splitted land-pol...'''
date = "2020-05-16T19:05:00Z"
lastmod = "2020-05-17T08:07:00Z"
weight = 74855
keywords = [ "osmcoastline", "land", "polygons" ]
aliases = [ "/questions/74855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmcoastline / Land polygons](/questions/74855/osmcoastline-land-polygons)

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
<span id="post-74855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have downloaded land polygons from <a href="https://osmdata.openstreetmap.de/download/land-polygons-split-4326.zip">https://osmdata.openstreetmap.de/download/land-polygons-split-4326.zip</a> The data seems to be nice ordered in cells of size one degree.</p>
<p>I however have a problem, that there is used a certain overlap-area between each cell. I would need the splitted land-polygons without this overlap.</p>
<p>Is it possible for me to generate such polygons with osmcoastline ? If so any tips on roadmap ? Options to osmcoastline etc.</p>
<p>Best regards Håvard Holm</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmcoastline" rel="tag" title="see questions tagged &#39;osmcoastline&#39;">osmcoastline</span> <span class="post-tag tag-link-land" rel="tag" title="see questions tagged &#39;land&#39;">land</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '20, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/db5b7b23235694ee1b9ef036a4393416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HaavardHolm&#39;s gravatar image" />
<p><span>HaavardHolm</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HaavardHolm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74855" class="comments-container">
&#10;</div>
<div id="comment-tools-74855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74855-form-container" class="comment-form-container">
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

<span id="74857"></span>

<div id="answer-container-74857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74857-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll find the manual for osmcoastline at <a href="https://docs.osmcode.org/osmcoastline/latest/osmcoastline.html">https://docs.osmcode.org/osmcoastline/latest/osmcoastline.html</a> . See the --bbox-overlap option. You can also have a look at the scripts in <a href="https://github.com/fossgis/osmdata/tree/master/scripts/coastline">https://github.com/fossgis/osmdata/tree/master/scripts/coastline</a> . These are the scripts behind the web site which does splitting a bit differently then the osmcoastline-internal splitting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '20, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-74857" class="comments-container">
&#10;</div>
<div id="comment-tools-74857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74857-form-container" class="comment-form-container">
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

