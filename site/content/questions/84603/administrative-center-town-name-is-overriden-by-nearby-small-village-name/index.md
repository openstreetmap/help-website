+++
type = "question"
title = "Administrative center town name is overriden by nearby small village name"
description = '''Hello, I&#x27;m wondering what should I do to change this behaviour. When I zoom to my municipality (Moravče, Slovenia) all the surrounding smaller villages are shown first, only if I zoom further the administrative center town name (Moravče) is shown later. For example village &quot;Zalog pri Moravčah&quot; (popu...'''
date = "2022-05-27T23:16:00Z"
lastmod = "2022-05-29T14:44:00Z"
weight = 84603
keywords = [ "zoomlevel", "placenames", "municipality" ]
aliases = [ "/questions/84603" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Administrative center town name is overriden by nearby small village name](/questions/84603/administrative-center-town-name-is-overriden-by-nearby-small-village-name)

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
<span id="post-84603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84603-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm wondering what should I do to change this behaviour. When I zoom to my municipality (Moravče, Slovenia) all the surrounding smaller villages are shown first, only if I zoom further the administrative center town name (Moravče) is shown later. For example village "Zalog pri Moravčah" (population: 188) is visible before town "Moravče" (population: 911) which is administrative center of municipality.</p>
<p>Why is that and how to fix it?</p>
<p>Best regards, Greg</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-placenames" rel="tag" title="see questions tagged &#39;placenames&#39;">placenames</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '22, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/07b071c7225915a29f5d4515430e5690?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrunner&#39;s gravatar image" />
<p><span>mrunner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrunner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84603" class="comments-container">
&#10;</div>
<div id="comment-tools-84603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84603-form-container" class="comment-form-container">
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

<span id="84610"></span>

<div id="answer-container-84610" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84610-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the standard layer, I am seeing Zalog pri Moravčah appearing at level 12 and both villages then appear from level 13 onwards, so there is only one zoom level of difference.</p>
<p>Looking at zoom level 12 on other layers accessible from the openstreetmap.org home page: - CyclOSM displays both labels (with Zalog pri Moravčah displaced a bit to the east I think) - Cycle Map, Transport Map, OPNVKarte all display only Moravče - Humanitarian displays neither.</p>
<p>I don't think there is anything particularly wrong, just slightly different algorithms used by different renders to prioritise label placement (perhaps partly affected by Zalog pri Moravčah being a fairly long name located very close to Moravče).</p>
<p>I note you referred to Moravče as a "town". That might suggest you could upgrade its tag from place=village to place=town. However looking at the history of <a href="https://www.openstreetmap.org/node/2759151033/history">https://www.openstreetmap.org/node/2759151033/history</a> , another mapped changed it from place=town to place=village, so I wouldn't advise that unless you are sure you can justify the change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '22, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84610" class="comments-container">
&#10;</div>
<div id="comment-tools-84610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84610-form-container" class="comment-form-container">
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

