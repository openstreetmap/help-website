+++
type = "question"
title = "Editing permission on UMap"
description = '''I am a journalist. I want to publish a map in my website news story and ask my readers to pin locations. On Umap, I have to allow everyone to edit the map. But what if someone decides to delete the entries of others? Can I restrict the permissions so that the user with the link to my map will only a...'''
date = "2022-06-22T15:27:00Z"
lastmod = "2022-06-22T17:59:00Z"
weight = 84847
keywords = [ "permission" ]
aliases = [ "/questions/84847" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Editing permission on UMap](/questions/84847/editing-permission-on-umap)

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
<span id="post-84847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a journalist. I want to publish a map in my website news story and ask my readers to pin locations. On Umap, I have to allow everyone to edit the map. But what if someone decides to delete the entries of others? Can I restrict the permissions so that the user with the link to my map will only add pins and not delete others' or edit the caption and description of the map itself?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-permission" rel="tag" title="see questions tagged &#39;permission&#39;">permission</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '22, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/6623566a6a0e8911a54d4b9d8d3deb54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jishnu%20EN&#39;s gravatar image" />
<p><span>Jishnu EN</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jishnu EN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84847" class="comments-container">
&#10;</div>
<div id="comment-tools-84847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84847-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="84849"></span>

<div id="answer-container-84849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84849-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't do it. You have already described some of the risks, but even if you could limit contributions in the way you describe (you cannot), you would still end up with users combining lots of markers into penis shapes or marking some location and adding a derogatory caption.</p>
<p>The only option to keep this sane is embedding a little Leaflet map with a GeoJSON file that contains locations into your map, and write a few lines of code that will allow the user to place a marker and trigger some sort of message to you, so that you get to review the marker manually and include it in your GeoJSON if it makes sense.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '22, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84849" class="comments-container">
&#10;</div>
<div id="comment-tools-84849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84849-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84853"></span>

<div id="answer-container-84853" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84853-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://gogocarto.fr/">Gogocarto</a> allows collaborative edition of map markers, with moderation and so on. It might suit your needs.</p>
<p>I'm not sure there is much documentation except in French, but it's quite simple to use...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '22, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-84853" class="comments-container">
&#10;</div>
<div id="comment-tools-84853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84853-form-container" class="comment-form-container">
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

