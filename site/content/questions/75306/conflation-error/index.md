+++
type = "question"
title = "Conflation error"
description = '''Hi, I have a question about conflation in JOSM.  I want to merge info and shape of a multipolygon that represents a natural area using JOSM/Conflation plugin. The reference was imported and edited from an shp file and the subject is multipolygon object in an osm file. I prepare the merge (unlink mul...'''
date = "2020-06-12T15:11:00Z"
lastmod = "2020-06-14T07:10:00Z"
weight = 75306
keywords = [ "josm", "conflation" ]
aliases = [ "/questions/75306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conflation error](/questions/75306/conflation-error)

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
<span id="post-75306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75306-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a question about conflation in JOSM.</p>
<p>I want to merge info and shape of a multipolygon that represents a natural area using JOSM/Conflation plugin. The reference was imported and edited from an shp file and the subject is multipolygon object in an osm file. I prepare the merge (unlink multipolygon, configure matches and so on) and when I press conflate I see:</p>
<p>"The way to be replaced cannot have any nodes with properties or relation memberships unless they belong to both ways."</p>
<p>How can I see what elements are linked to the subject? This is, how can I know what are those nodes that block the merge?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-conflation" rel="tag" title="see questions tagged &#39;conflation&#39;">conflation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '20, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/7d273e3aa3a888fb089420e6f5e5b2c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mglbranco&#39;s gravatar image" />
<p><span>mglbranco</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mglbranco has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75306" class="comments-container">
&#10;</div>
<div id="comment-tools-75306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75306-form-container" class="comment-form-container">
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

<span id="75319"></span>

<div id="answer-container-75319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would start by visually following the polygon. In most cases, you will encounter an icon on one of the nodes. It is also possible that the node is coloured differently (I thought a white dot) when it has tags that do not lead to the display of an icon.</p>
<p>You can also select all nodes of the polygon (requires utilsplugin2): select polygon, CTRL-SHIFT-N Then search with tags:1- and "search in selection". This should find all nodes with at least one tag in the current selection</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '20, 07:10</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-75319" class="comments-container">
&#10;</div>
<div id="comment-tools-75319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75319-form-container" class="comment-form-container">
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

