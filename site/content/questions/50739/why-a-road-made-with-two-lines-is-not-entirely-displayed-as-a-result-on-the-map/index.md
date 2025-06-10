+++
type = "question"
title = "Why a road made with two lines is not entirely displayed as a result on the map ?"
description = '''Why a road made with two lines is not entirely displayed as a result on the map ? An example is when you search &quot;avenue de la libération, plélan le grand&quot;. There is one result as expect. OK When you click on it, a node-line is selected and the map is centered on it. OK On the map, you can see an ora...'''
date = "2016-07-08T22:17:00Z"
lastmod = "2016-07-08T22:30:00Z"
weight = 50739
keywords = [ "highlight", "line", "result" ]
aliases = [ "/questions/50739" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why a road made with two lines is not entirely displayed as a result on the map ?](/questions/50739/why-a-road-made-with-two-lines-is-not-entirely-displayed-as-a-result-on-the-map)

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
<span id="post-50739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50739-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why a road made with two lines is not entirely displayed as a result on the map ?</p>
<p>An example is when you search "avenue de la libération, plélan le grand".</p>
<p>There is one result as expect. OK</p>
<p>When you click on it, a node-line is selected and the map is centered on it. OK</p>
<p>On the map, you can see an orange line to highlight the result. OK</p>
<p>But on the map, there are two nodes-line which define this road and it's impossible to have the other one in the result.</p>
<p>I would expect that the two nodes-lines were highlight and I ask why it is not.</p>
<p>I believe it's already a thing talked. Thanks for yours answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highlight" rel="tag" title="see questions tagged &#39;highlight&#39;">highlight</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-result" rel="tag" title="see questions tagged &#39;result&#39;">result</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '16, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c7f1749fc8d29adfc3fd18f8feb6bade?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freeroot2&#39;s gravatar image" />
<p><span>freeroot2</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freeroot2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '16, 22:19</strong> </span></p>
</div>
</div>
<div id="comments-container-50739" class="comments-container">
&#10;</div>
<div id="comment-tools-50739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50739-form-container" class="comment-form-container">
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

<span id="50740"></span>

<div id="answer-container-50740" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50740-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="freeroot2 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Streets in OSM tend to be split up in to many segments with unique tagging or relation membership, or in the case of dual carriageways, direction. The standard search engine available via the search box does not merge these ways on import so it will return whatever segment happens to be highest ranking first.</p>
<p>Fixing this is "a simple matter of programming", please do not hesitate to provide such code to: <a href="https://github.com/twain47/Nominatim">https://github.com/twain47/Nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '16, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50740" class="comments-container">
&#10;</div>
<div id="comment-tools-50740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50740-form-container" class="comment-form-container">
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

