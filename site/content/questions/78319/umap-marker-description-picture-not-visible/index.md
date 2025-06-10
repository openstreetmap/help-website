+++
type = "question"
title = "uMap Marker description: picture not visible"
description = '''Hello together, I&#x27;m working with uMap and want to add descriptions to my markers which include images. Syntax help gives 2 possibilities:   1. Image only: {{http://image.url.com}}   2. Image and width in pixels: {{http://image.url.com|pixels}}  I tried both types but as a result the marker descripti...'''
date = "2021-01-10T21:13:00Z"
lastmod = "2021-01-27T08:30:00Z"
weight = 78319
keywords = [ "marker", "umap", "images", "description" ]
aliases = [ "/questions/78319" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [uMap Marker description: picture not visible](/questions/78319/umap-marker-description-picture-not-visible)

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
<span id="post-78319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello together,</p>
<p>I'm working with uMap and want to add descriptions to my markers which include images.</p>
<p>Syntax help gives 2 possibilities:</p>
<p>1. Image only: <strong>{{http://image.url.com}}</strong></p>
<p>2. Image and width in pixels: <strong>{{http://image.url.com|pixels}}</strong></p>
<p>I tried both types but as a result the marker description doesn't show the image but only the place holder for missing link.</p>
<p>As type for the marker popup description I tried both "pop up (big)" and "sitebar". In the example I refer to a wikipedia picture just to ensure open access.</p>
<p>Can somebody help?</p>
<p>Error and code snippet (sorry for partial german):</p>
<p><img src="https://help.openstreetmap.org/upfiles/MissingPic.PNG" alt="alt text" /></p>
<p><img src="https://help.openstreetmap.org/upfiles/MissingPicCode.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-images" rel="tag" title="see questions tagged &#39;images&#39;">images</span> <span class="post-tag tag-link-description" rel="tag" title="see questions tagged &#39;description&#39;">description</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '21, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c586526d376f66b78a38f0cd3c8e6dec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="04Wank07&#39;s gravatar image" />
<p><span>04Wank07</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="04Wank07 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-78319" class="comments-container">
&#10;</div>
<div id="comment-tools-78319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78319-form-container" class="comment-form-container">
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

<span id="78536"></span>

<div id="answer-container-78536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to add a property (a column) in layer table calling for instance: "imgurl" and then in pop-up content template, insert <code>{{{imgurl}|300}}</code>.</p>
<p>Once you are done, add marker inserting the image url (I usually set the url of <a href="https://upload.wikimedia.org/wikipedia/commons/8/8c/Austria_1044_semmering.jpg">wikipedia raw image</a>, known as "Original size").</p>
<p>In <a href="http://umap.openstreetmap.fr/en/map/untitled-map_553981#8/46.680/14.049">this example</a>, the marker on the right works fine (I set 240 width size).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '21, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '21, 09:02</strong> </span></p>
</div>
</div>
<div id="comments-container-78536" class="comments-container">
&#10;</div>
<div id="comment-tools-78536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78536-form-container" class="comment-form-container">
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

