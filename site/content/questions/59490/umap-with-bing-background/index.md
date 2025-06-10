+++
type = "question"
title = "Umap with Bing background"
description = '''Hello, I want to create a map with Umap using Bing aerial image as the background. The map will display the places and related stories of the migrants who are now in Paris, France, but no geographical information. As I only intend to use the background image with no additional information (no names,...'''
date = "2017-09-08T15:08:00Z"
lastmod = "2017-09-11T20:00:00Z"
weight = 59490
keywords = [ "umap", "bing", "aerial_imagery" ]
aliases = [ "/questions/59490" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Umap with Bing background](/questions/59490/umap-with-bing-background)

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
<span id="post-59490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59490-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to create a map with Umap using Bing aerial image as the background. The map will display the places and related stories of the migrants who are now in Paris, France, but no geographical information. As I only intend to use the background image with no additional information (no names, no place, nothing) there shouldn't be any copyright problem with Bing. Does someone know what URL I should write for Bing in the related box in Umap ? Or does someone have an alternative solution / tool to create such a map ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '17, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d63bbe6f1b8aa365533b56ce79a18b38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThierryPayet974&#39;s gravatar image" />
<p><span>ThierryPayet974</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThierryPayet974 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59490" class="comments-container">
<span id="59492"></span>
<div id="comment-59492" class="comment">
<div id="post-59492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are using umap.openstreetmap.fr, there is an IGN background available.</p>
</div>
<div id="comment-59492-info" class="comment-info">
<span class="comment-age">(08 Sep '17, 16:02)</span> <span class="comment-user userinfo">ybon</span>
</div>
</div>
<span id="59550"></span>
<div id="comment-59550" class="comment">
<div id="post-59550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I did realize this and the IGN layer is my actual background. But the definition of the IGN aerial map is very good for France and very limited for the other countries which the migrants relate to (Africa, Europe, Asia). As my map is about "showing the ground" as a sensitive information, I'm trying to improve the IGN solution with Bing...</p>
</div>
<div id="comment-59550-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 19:50)</span> <span class="comment-user userinfo">ThierryPayet974</span>
</div>
</div>
</div>
<div id="comment-tools-59490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59490-form-container" class="comment-form-container">
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

<span id="59491"></span>

<div id="answer-container-59491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59491-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The operator of the umap instance needs to configure available background layers (well at least it was that way the last time I worked on umap), they will need to get an API key from bing to do add a bing layer (the free tier is reasonably large so that shouldn't be a big issue).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '17, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '17, 21:44</strong> </span></p>
</div>
</div>
<div id="comments-container-59491" class="comments-container">
<span id="59551"></span>
<div id="comment-59551" class="comment">
<div id="post-59551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. Any idea how to contact the people from Bing to get the API key ?</p>
</div>
<div id="comment-59551-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 20:00)</span> <span class="comment-user userinfo">ThierryPayet974</span>
</div>
</div>
</div>
<div id="comment-tools-59491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59491-form-container" class="comment-form-container">
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

