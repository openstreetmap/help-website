+++
type = "question"
title = "batch customising maps"
description = '''Hi all - I need to print several maps of towns for an organisation, but they need to be styled a certain way (just roads and rivers, and certain colours). Is there away to do this programatically without having to export each map and edit the pdf&#x27;s? I&#x27;ve seen a few forums which point me to third par...'''
date = "2017-02-11T22:35:00Z"
lastmod = "2017-02-11T22:43:00Z"
weight = 54612
keywords = [ "print", "export", "batch", "customization", "custom" ]
aliases = [ "/questions/54612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [batch customising maps](/questions/54612/batch-customising-maps)

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
<span id="post-54612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54612-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all -</p>
<p>I need to print several maps of towns for an organisation, but they need to be styled a certain way (just roads and rivers, and certain colours). Is there away to do this programatically without having to export each map and edit the pdf's? I've seen a few forums which point me to third party sites, but a lot of them are offline and even then there's so many red herrings it seems. Is there a really common method people use?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '17, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/655b6c5be75badb5cd22f5c73b0a8761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dilby00&#39;s gravatar image" />
<p><span>dilby00</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dilby00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54612" class="comments-container">
&#10;</div>
<div id="comment-tools-54612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54612-form-container" class="comment-form-container">
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

<span id="54613"></span>

<div id="answer-container-54613" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54613-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the maps don't cover too large an area, then your easiest option might be doing this with Maperitive. Maperitive allows you to load data for an area from the Overpass data service, then have it styled with a map style you defined beforehand, and export as SVG or PNG. Best thing about this, it is scriptable, so you could generate a script that repeats this action for all the towns you're interested in. Of course you'll have to invest some time before hand to come up with the right style definition.</p>
<p>An alternative is using the Mapnik rendering engine with a commandline frontend like nik4.py. This works well even with larger areas but requires importing all OSM data into a PostGIS database first. And of course the styling work, too, albeit in a different styling language than Maperitive's.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '17, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54613" class="comments-container">
&#10;</div>
<div id="comment-tools-54613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54613-form-container" class="comment-form-container">
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

