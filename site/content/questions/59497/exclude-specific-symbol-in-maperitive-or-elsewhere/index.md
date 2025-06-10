+++
type = "question"
title = "Exclude specific symbol in Maperitive or elsewhere?"
description = '''Is there a way to do this in Maperitive - or in any other fashion? For example I need a map with all labels intact EXCEPT that one label that I want to remove/exclude/hide before exporting and printing as an image for a poster. Side question: how does one add custom symbols to a map? Asking because ...'''
date = "2017-09-09T01:29:00Z"
lastmod = "2017-09-11T14:50:00Z"
weight = 59497
keywords = [ "symbols", "symbol", "labels", "maperitive" ]
aliases = [ "/questions/59497" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Exclude specific symbol in Maperitive or elsewhere?](/questions/59497/exclude-specific-symbol-in-maperitive-or-elsewhere)

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
<span id="post-59497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to do this in Maperitive - or in any other fashion? For example I need a map with all labels intact EXCEPT that one label that I want to remove/exclude/hide before exporting and printing as an image for a poster.</p>
<p>Side question: how does one add custom symbols to a map? Asking because if I understand this I could indirectly figure out how to remove as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-symbols" rel="tag" title="see questions tagged &#39;symbols&#39;">symbols</span> <span class="post-tag tag-link-symbol" rel="tag" title="see questions tagged &#39;symbol&#39;">symbol</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '17, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/1be94d4bfe53c018b067f57b1add4f77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="montrealist&#39;s gravatar image" />
<p><span>montrealist</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="montrealist has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '17, 01:47</strong> </span></p>
</div>
</div>
<div id="comments-container-59497" class="comments-container">
&#10;</div>
<div id="comment-tools-59497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59497-form-container" class="comment-form-container">
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

<span id="59499"></span>

<div id="answer-container-59499" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59499-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="montrealist has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With Maperitive you have two options:</p>
<ul>
<li>before rendering: download the OSM data of interest, save to .osm file, open the file in an text editor (or even in JOSM) and remove the node/way/relation responsible for the feature (or maybe just remove the name tag or whatever it is that lends the label to it). Then open the OSM file in Maperitive and proceed as normal.</li>
<li>after rendering: Use Maperitive to render the map and save as SVG. Open in Inkscape, select the label and remove it.</li>
</ul>
<p>To my knowledge, unlike in a database-backed rendering process like Mapnik with OSM-Carto, you cannot actually build a rendering rule in Maperitive that would say "draw this label except when the content is X".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '17, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-59499" class="comments-container">
<span id="59539"></span>
<div id="comment-59539" class="comment">
<div id="post-59539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, so I can just edit the <code>.osm</code> file directly - how come this didn't occur to me? Thank you!</p>
</div>
<div id="comment-59539-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 14:04)</span> <span class="comment-user userinfo">montrealist</span>
</div>
</div>
<span id="59543"></span>
<div id="comment-59543" class="comment">
<div id="post-59543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just be sure not to accidentally upload your changes to OSM ;)</p>
</div>
<div id="comment-59543-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 14:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59499-form-container" class="comment-form-container">
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

