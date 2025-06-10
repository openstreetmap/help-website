+++
type = "question"
title = "Osm carto multilingual tags"
description = '''Hello, Iis there an easy way to render osm names in a given language? Looked for it in settings but could not find it. Organic maps displays both english and local name in the default renderer'''
date = "2024-03-03T16:11:00Z"
lastmod = "2024-03-06T13:01:00Z"
weight = 88266
keywords = [ "#nametags", "#name_int", "#osmcarto" ]
aliases = [ "/questions/88266" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osm carto multilingual tags](/questions/88266/osm-carto-multilingual-tags)

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
<span id="post-88266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88266-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, Iis there an easy way to render osm names in a given language? Looked for it in settings but could not find it. Organic maps displays both english and local name in the default renderer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#nametags" rel="tag" title="see questions tagged &#39;#nametags&#39;">#nametags</span> <span class="post-tag tag-link-#name_int" rel="tag" title="see questions tagged &#39;#name_int&#39;">#name_int</span> <span class="post-tag tag-link-#osmcarto" rel="tag" title="see questions tagged &#39;#osmcarto&#39;">#osmcarto</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '24, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e7808c4eb2f9dc61870fa51aa4dbf31b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obraynt456&#39;s gravatar image" />
<p><span>obraynt456</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obraynt456 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88266" class="comments-container">
&#10;</div>
<div id="comment-tools-88266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88266-form-container" class="comment-form-container">
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

<span id="88273"></span>

<div id="answer-container-88273" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88273-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-88273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're rendering yourself then you need to render the <code>name:XX</code> tag where <code>XX</code> is replaced by the language code for the language you want to see. Not all named objects will have this so you may need to fallback to plain <code>name</code> if the language you want is missing. More info <a href="https://wiki.openstreetmap.org/wiki/Names">here</a>.</p>
<p>For something you can browse on line <a href="https://wiki.openstreetmap.org/wiki/Vector_tiles">vector tile</a> providers are the most likely to give you what you want see e.g. <a href="https://zelonewolf.github.io/openstreetmap-americana/#map=4/40.5/-94">OSM Americana</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '24, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-88273" class="comments-container">
&#10;</div>
<div id="comment-tools-88273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88273-form-container" class="comment-form-container">
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

