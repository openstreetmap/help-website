+++
type = "question"
title = "OpenTopoMap Without Labels"
description = '''Does anyone know if there is a bare bones copy of OpenTopoMap without any labels (ex. for mountains) or human elements (ex. roads) baked in? While the thought is appreciated, the labels typically render themselves in poor resolution and interfere with overlying content and have no option to disable ...'''
date = "2020-06-30T07:05:00Z"
lastmod = "2020-07-07T09:29:00Z"
weight = 75471
keywords = [ "topo", "labels", "opentopomap" ]
aliases = [ "/questions/75471" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenTopoMap Without Labels](/questions/75471/opentopomap-without-labels)

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
<span id="post-75471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone know if there is a bare bones copy of OpenTopoMap without any labels (ex. for mountains) or human elements (ex. roads) baked in? While the thought is appreciated, the labels typically render themselves in poor resolution and interfere with overlying content and have no option to disable in the OpenTopoMap settings. Meanwhile, the roads, particularly FSRs, are incorrect or outdated.</p>
<p>Would the renderer kindly consider publishing a plain topographic map without any anthropogenic or textual content? Otherwise, the geographic symbology is superb.</p>
<p>Alternatively, is there a way to access the OpenTopoMap baselayer file to manually make changes? Even if it, or a section, could be cloned for offline use it would be terrific.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topo" rel="tag" title="see questions tagged &#39;topo&#39;">topo</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-opentopomap" rel="tag" title="see questions tagged &#39;opentopomap&#39;">opentopomap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '20, 07:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5002503bcba2372c86c8e86d3895c8b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KFOB&#39;s gravatar image" />
<p><span>KFOB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KFOB has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '20, 07:07</strong> </span></p>
</div>
</div>
<div id="comments-container-75471" class="comments-container">
&#10;</div>
<div id="comment-tools-75471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75471-form-container" class="comment-form-container">
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

<span id="75472"></span>

<div id="answer-container-75472" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75472-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As those are raster tiles, you can't change what you see.</p>
<p>Only way would be to get hold of the cartoCSS/mapnik style files <a href="https://github.com/der-stefan/OpenTopoMap">here</a> (see licence, haven't checked), work on them to remove all labels etc. and than render them on your own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '20, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '20, 10:08</strong> </span></p>
</div>
</div>
<div id="comments-container-75472" class="comments-container">
<span id="75503"></span>
<div id="comment-75503" class="comment">
<div id="post-75503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gotcha, thanks for the input! Looks like it's a pretty intensive undertaking.</p>
<p>Quick question in reference to the Virtual Computer Requirements: "Generation 2 Memory: 32000MB (not dynamic) Virtual Harddisk: 1024GB"</p>
<p>What does Generation 2 refer to? Does 'Memory' here refer to 32 GB of RAM? Is the 1024 GB of space for the virtual harddisk for the Ubuntu server? Is that a kind of system partition?</p>
</div>
<div id="comment-75503-info" class="comment-info">
<span class="comment-age">(01 Jul '20, 23:31)</span> <span class="comment-user userinfo">KFOB</span>
</div>
</div>
<span id="75574"></span>
<div id="comment-75574" class="comment">
<div id="post-75574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Those requirements sound pretty dated, at least if it's for planet (will work for a smaller region/excerpt imho). Generation 2 probably means DDR2, by that you see what I mean by "dated". For a planet covering map, you would at least need 64 GB of mem and (more than) 1TB ssd for the postgresql database and up to 2TB for the mod_tile cache.</p>
</div>
<div id="comment-75574-info" class="comment-info">
<span class="comment-age">(07 Jul '20, 09:29)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-75472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75472-form-container" class="comment-form-container">
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

