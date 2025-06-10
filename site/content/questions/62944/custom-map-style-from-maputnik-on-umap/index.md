+++
type = "question"
title = "Custom map style from Maputnik on Umap"
description = '''I am trying to import a custom map style from Maputnik into Umap. But importing the Json file containing the map style into Umap does not work, and the custom background settings seems to only take images. Is it possible to replace the normal style by a custom one in Umap?'''
date = "2018-04-08T13:56:00Z"
lastmod = "2018-04-09T18:31:00Z"
weight = 62944
keywords = [ "umap", "style", "mapnik" ]
aliases = [ "/questions/62944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Custom map style from Maputnik on Umap](/questions/62944/custom-map-style-from-maputnik-on-umap)

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
<span id="post-62944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62944-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to import a custom map style from Maputnik into Umap. But importing the Json file containing the map style into Umap does not work, and the custom background settings seems to only take images. Is it possible to replace the normal style by a custom one in Umap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '18, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ba15159175b5ecfe87e00b917ff4a51e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oulifu&#39;s gravatar image" />
<p><span>Oulifu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oulifu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62944" class="comments-container">
&#10;</div>
<div id="comment-tools-62944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62944-form-container" class="comment-form-container">
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

<span id="62955"></span>

<div id="answer-container-62955" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62955-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't believe that umap currently supports vector tile layers which are required is you want to use mapbox-gl for styling. It definitely would be interesting functionality to have and maybe you should open an issue on the umap issue tracker: <a href="https://github.com/umap-project/umap/issues">https://github.com/umap-project/umap/issues</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '18, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62955" class="comments-container">
<span id="62961"></span>
<div id="comment-62961" class="comment">
<div id="post-62961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So there is no existing way to edit the Umap map style?</p>
</div>
<div id="comment-62961-info" class="comment-info">
<span class="comment-age">(09 Apr '18, 18:31)</span> <span class="comment-user userinfo">Oulifu</span>
</div>
</div>
</div>
<div id="comment-tools-62955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62955-form-container" class="comment-form-container">
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

