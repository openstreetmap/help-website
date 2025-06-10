+++
type = "question"
title = "GPX import : how to avoid manual creation of node ?"
description = '''Dear all, I&#x27;m dead new in OSM. I gave a try with the GPX import(from my garmin 800). My trace is properly imported in blue (nice mountain bike tracks that do not exist so far in OSM). Is there any trick to avoid creating node for my track (I&#x27;m using potlatch2 in firefox) ? It is really time consumin...'''
date = "2013-07-06T11:09:00Z"
lastmod = "2013-07-06T16:25:00Z"
weight = 24029
keywords = [ "node", "import", "gpx" ]
aliases = [ "/questions/24029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GPX import : how to avoid manual creation of node ?](/questions/24029/gpx-import-how-to-avoid-manual-creation-of-node)

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
<span id="post-24029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24029-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>I'm dead new in OSM. I gave a try with the GPX import(from my garmin 800). My trace is properly imported in blue (nice mountain bike tracks that do not exist so far in OSM). Is there any trick to avoid creating node for my track (I'm using potlatch2 in firefox) ? It is really time consuming and there is no added value. I would prefer to concentrate on the proper tags to give to the tracks (which is already a though job since within few kilometres the category is changing from montain bike, to pedestrian or all terrain vehicule ...).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '13, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/bf0bc15dc33fddfcce702004ec473831?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SdW74&#39;s gravatar image" />
<p><span>SdW74</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SdW74 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24029" class="comments-container">
&#10;</div>
<div id="comment-tools-24029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24029-form-container" class="comment-form-container">
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

<span id="24030"></span>

<div id="answer-container-24030" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24030-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-24030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Potlatch 2, you can load a track, then press Alt and click on the track to convert it to a way (Windows/Mac OS) or Control+Shift click on Linux. That way can then be edited as usual.</p>
<p>Most GPS tracks have an excessive number of points, especially if you are recording at one point per second, so it is helpful to simplify this. In Potlatch 2, you can press Y to automatically simplify a way.</p>
<p>You should also make sure the new way is connected to any existing ways as required. And you can check to see if there any clearly inaccurate points from the GPS, eg obvious 'spikes', or clusters of points if you stopped somewhere, then delete or move those.</p>
<p>But still, it is often helpful to trace GPS tracks manually. This lets you place nodes where they are needed, ie an appropriate number to make curves realistic. And it lets you spot places where the GPS appears inaccurate, and avoid drawing those. You can load several GPS traces for the same route, and use those along with aerial imagery, to draw a more accurate way. So this does 'add value', though it can be time consuming for a long twisty path.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '13, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-24030" class="comments-container">
<span id="24035"></span>
<div id="comment-24035" class="comment">
<div id="post-24035-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>thanks, it works fine (on my Mac, it is "z" instead of "y" to simplify). You are right, a GPS trace is not accurate enough, it still requires some manual post-processing.</p>
</div>
<div id="comment-24035-info" class="comment-info">
<span class="comment-age">(06 Jul '13, 16:25)</span> <span class="comment-user userinfo">SdW74</span>
</div>
</div>
</div>
<div id="comment-tools-24030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24030-form-container" class="comment-form-container">
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

