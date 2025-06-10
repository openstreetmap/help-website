+++
type = "question"
title = "Conflict Dialog"
description = '''Hi, is it possible to temporarily disable the tag conflict reporting? It would be useful e.g. when importing new buildings, when I know I want to replace the original buildings with new ones... Via UtilsPlugin2 I have to transfer the history one building at a time... It would also be useful for addr...'''
date = "2022-09-27T13:43:00Z"
lastmod = "2022-09-27T14:31:00Z"
weight = 85738
keywords = [ "josm" ]
aliases = [ "/questions/85738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conflict Dialog](/questions/85738/conflict-dialog)

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
<span id="post-85738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is it possible to temporarily disable the tag conflict reporting? It would be useful e.g. when importing new buildings, when I know I want to replace the original buildings with new ones... Via UtilsPlugin2 I have to transfer the history one building at a time... It would also be useful for addresses</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '22, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/176f2567c3da5fb061d49a9027c1db2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klerik7&#39;s gravatar image" />
<p><span>Klerik7</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klerik7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85738" class="comments-container">
&#10;</div>
<div id="comment-tools-85738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85738-form-container" class="comment-form-container">
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

<span id="85743"></span>

<div id="answer-container-85743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85743-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The conflict dialog should only appear if the object you are modifying has been changed in the mean time by someone else. It would not typically appear if you are importing buildings on top of an already existing building. The error dialog shown in that situation would come from the validator, and it can be clicked away - or you can even reconfigure the validator not to run on uploads.</p>
<p><strong>However</strong> please be aware that imports into OSM are governed by guidelines (<a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines)">https://wiki.openstreetmap.org/wiki/Import/Guidelines)</a> which include, among other things, that a plan for the import has to be discussed with the community beforehand. Any such plan that involved, even temporarily, uploading new buildings over old buildings, or the outright deletion of old buildings, would almost certainly be rejected, and any import performed violating these guidelines would almost certainly be reverted without further discussion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '22, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85743" class="comments-container">
<span id="85744"></span>
<div id="comment-85744" class="comment">
<div id="post-85744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The dialog appears because I need to transfer the history and if the old building has the tag building=yes and the new building=detached then of course there will be a conflict... But I would like to use the newer tags automatically... I am aware of the second part</p>
</div>
<div id="comment-85744-info" class="comment-info">
<span class="comment-age">(27 Sep '22, 14:31)</span> <span class="comment-user userinfo">Klerik7</span>
</div>
</div>
</div>
<div id="comment-tools-85743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85743-form-container" class="comment-form-container">
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

