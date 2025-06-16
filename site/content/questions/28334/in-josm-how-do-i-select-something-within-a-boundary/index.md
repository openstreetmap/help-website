+++
type = "question"
title = "In JOSM how do i select something within a boundary?"
description = '''In JOSM how do i select something within a boundary? For example, I want to select all parks within the boundaries of a city excluding parks in other cities. Thanks'''
date = "2013-11-21T12:37:00Z"
lastmod = "2013-11-22T20:20:00Z"
weight = 28334
keywords = [ "boundaries", "josm", "selection" ]
aliases = [ "/questions/28334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [In JOSM how do i select something within a boundary?](/questions/28334/in-josm-how-do-i-select-something-within-a-boundary)

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
<span id="post-28334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28334-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM how do i select something within a boundary? For example, I want to select all parks within the boundaries of a city excluding parks in other cities. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '13, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/bee79aaecc19172aaba1738828da516d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emrekko&#39;s gravatar image" />
<p><span>emrekko</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emrekko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '13, 13:04</strong> </span></p>
</div>
</div>
<div id="comments-container-28334" class="comments-container">
&#10;</div>
<div id="comment-tools-28334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28334-form-container" class="comment-form-container">
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

<span id="28337"></span>

<div id="answer-container-28337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28337-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-28337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2">UtilsPlugin2</a> has an experimental feature "select all inside" that could be used to select everything that is inside some selected area or multipolygon. Then, with this selection made, you can filter using the regular search function (control+F), plus the "selected" modifier.</p>
<p>I tried it and found that when working with boundaries, it wouldn't work unless I used a trick before (<strong>very</strong> dangerous to the data integrity, will not describe here), but works OK with areas and multipolygons.</p>
<p>You can install the UtilsPlugin2 through the JOSM preferences page (F12), Plugins tab.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-28337" class="comments-container">
<span id="28408"></span>
<div id="comment-28408" class="comment">
<div id="post-28408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is pretty much the only automated answer.</p>
</div>
<div id="comment-28408-info" class="comment-info">
<span class="comment-age">(22 Nov '13, 20:20)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-28337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28337-form-container" class="comment-form-container">
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

