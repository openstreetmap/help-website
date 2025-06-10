+++
type = "question"
title = "Process JOSM saved Files with osmosis (version attribute missing)"
description = '''I am trying to merge an OSM saved file (new POIs) with a current planet extract. Osmosis complains, that the file saved by JOSM is not propper API v0.6 format because the version attribute is missing. Is there a way to process such files with Osmosis? If I use osmosis-0.35 which supports API 0.5 and...'''
date = "2018-07-16T12:30:00Z"
lastmod = "2018-07-31T23:35:00Z"
weight = 64747
keywords = [ "osmosis" ]
aliases = [ "/questions/64747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Process JOSM saved Files with osmosis (version attribute missing)](/questions/64747/process-josm-saved-files-with-osmosis-version-attribute-missing)

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
<span id="post-64747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64747-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to merge an OSM saved file (new POIs) with a current planet extract.</p>
<p>Osmosis complains, that the file saved by JOSM is not propper API v0.6 format because the version attribute is missing.</p>
<p>Is there a way to process such files with Osmosis?</p>
<p>If I use osmosis-0.35 which supports API 0.5 and change the API version tag manually in the XML, osmosis complains about the timestamp attribute being missing.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '18, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64747" class="comments-container">
<span id="65037"></span>
<div id="comment-65037" class="comment">
<div id="post-65037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've found this:</p>
<p>Osmosis is not compatible with JOSM format OSM files. JOSM OSM files are editor oriented and deviate from Osmosis in a number of ways (version and action attributes at least ...) If you wish to discuss this in more detail please post to the osmosis-dev mailing list, but for now there are no plans to rectify this.</p>
<p><a href="https://trac.openstreetmap.org/ticket/2620">https://trac.openstreetmap.org/ticket/2620</a></p>
</div>
<div id="comment-65037-info" class="comment-info">
<span class="comment-age">(31 Jul '18, 02:04)</span> <span class="comment-user userinfo">xronos</span>
</div>
</div>
</div>
<div id="comment-tools-64747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64747-form-container" class="comment-form-container">
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

<span id="65048"></span>

<div id="answer-container-65048" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65048-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The underlying problem is that newly created data in editors typically has neither a valid version nor id attribute (as these are allocated on upload by the OSM API). But it isn't difficult to simply renumber an XML file and add a version="1" attribute argument to objects that don't have one and an id that doesn't conflict with existing ones.</p>
<p>Naturally you won't be able to use the resulting data for uploading, or anything similar, to the OSM API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '18, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65048" class="comments-container">
&#10;</div>
<div id="comment-tools-65048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65048-form-container" class="comment-form-container">
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

