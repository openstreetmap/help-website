+++
type = "question"
title = "Show coordinates in uMap popup"
description = '''I would like to create a uMap popup that also shows the coordinates of a marker. I tried to create a Popup content template in uMap with the placeholders {name}, {description}, {latitude} and {longitude}, but that does not work. Only the name and the description are shown. Am I using the wrong place...'''
date = "2023-03-18T21:24:00Z"
lastmod = "2023-07-29T07:27:00Z"
weight = 86947
keywords = [ "umap", "popup", "placeholder", "coordinates" ]
aliases = [ "/questions/86947" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Show coordinates in uMap popup](/questions/86947/show-coordinates-in-umap-popup)

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
<span id="post-86947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86947-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to create a uMap popup that also shows the coordinates of a marker. I tried to create a Popup content template in uMap with the placeholders {name}, {description}, {latitude} and {longitude}, but that does not work. Only the name and the description are shown. Am I using the wrong placeholders for the coordinates? Is there another way of showing the coordinates in the popup?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-placeholder" rel="tag" title="see questions tagged &#39;placeholder&#39;">placeholder</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '23, 21:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2a43518266c8fd4b14f73c75624d0850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Palthe&#39;s gravatar image" />
<p><span>Palthe</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Palthe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Mar '23, 23:41</strong> </span></p>
</div>
</div>
<div id="comments-container-86947" class="comments-container">
&#10;</div>
<div id="comment-tools-86947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86947-form-container" class="comment-form-container">
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

<span id="87565"></span>

<div id="answer-container-87565" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87565-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Palthe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the remote data in umap retrieved from overpass-turbo I use {lat} and {lon} for <em>nodes</em>:</p>
<p><img src="https://github.com/openstreetmap/openstreetmap-website/assets/8467903/2b0d7c21-075b-4487-b3b7-5d2d4028c137" alt="properties of a node retrieved from overpass-turbo" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '23, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/5b2d680cd0c22a32517db07ed16eeaf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iriman&#39;s gravatar image" />
<p><span>iriman</span><br />
<span class="score" title="297 reputation points">297</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iriman has one accepted answer">33%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '23, 08:57</strong> </span></p>
</div>
</div>
<div id="comments-container-87565" class="comments-container">
<span id="87567"></span>
<div id="comment-87567" class="comment">
<div id="post-87567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear Iriman,</p>
<p>Thanks for your answer. Using {lat} and {lon} works perfectly!<br />
I did not thought about using the abbreviated versions of the names.<br />
Do you know if there is some kind of list with all the placeholder-codes one can use?</p>
<p>Best regards,<br />
Boudewijn.</p>
</div>
<div id="comment-87567-info" class="comment-info">
<span class="comment-age">(27 Jul '23, 22:04)</span> <span class="comment-user userinfo">Palthe</span>
</div>
</div>
<span id="87572"></span>
<div id="comment-87572" class="comment">
<div id="post-87572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're welcome. We can use any key name from key:value pairs in our data in the form {key} as placeholder. In the example data in picture above we can use {name}, {shop}, {lat}, {lon} and {id}. {id} will generate a mix of type and id values: {type}/{id}. I didn't find a list of placeholders. Happy that my suggestion also works for manual markers!</p>
</div>
<div id="comment-87572-info" class="comment-info">
<span class="comment-age">(29 Jul '23, 07:27)</span> <span class="comment-user userinfo">iriman</span>
</div>
</div>
</div>
<div id="comment-tools-87565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87565-form-container" class="comment-form-container">
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

