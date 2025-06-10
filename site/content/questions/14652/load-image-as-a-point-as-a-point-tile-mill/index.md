+++
type = "question"
title = "Load image as a point as a point Tile Mill"
description = '''Ok so I&#x27;m trying to load an image as a point on a blank map canvas. Earlier I tried loading an image as a background using: Map {  background-image: url(somefolder/someimage.jpg); }  This worked but I got the same image repeated ad-infinitum. So someone suggested loading the image as a point. I made...'''
date = "2012-07-27T14:08:00Z"
lastmod = "2014-05-20T22:09:00Z"
weight = 14652
keywords = [ "point", "map", "image", "loading", "custom" ]
aliases = [ "/questions/14652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Load image as a point as a point Tile Mill](/questions/14652/load-image-as-a-point-as-a-point-tile-mill)

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
<span id="post-14652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14652-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ok so I'm trying to load an image as a point on a blank map canvas. Earlier I tried loading an image as a background using:</p>
<pre><code>Map {
    background-image: url(somefolder/someimage.jpg);
}</code></pre>
<p>This worked but I got the same image repeated ad-infinitum. So someone suggested loading the image as a point. I made a CSV file with lat and lon of zero and added a new layer, I attempted to load the image using the same relative address as before:</p>
<pre><code>Map {
    background-color: #b8dee6;
}
#pointlayer {
    point-file: url(somefolder/someimage.jpg);
}</code></pre>
<p>But nothing shows up with this method. Can anyone shed some light as to whats going wrong here? Is the background hiding the image? I've tried flushing the cache.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-loading" rel="tag" title="see questions tagged &#39;loading&#39;">loading</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '12, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ed4841db0e878edf4fe1fa9d46f63757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DamoPock&#39;s gravatar image" />
<p><span>DamoPock</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DamoPock has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '12, 19:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-14652" class="comments-container">
&#10;</div>
<div id="comment-tools-14652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14652-form-container" class="comment-form-container">
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

<span id="14666"></span>

<div id="answer-container-14666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14666-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are sure that the image file is on the right path, you can try to use the <code>point-allow-overlap: true</code> command.</p>
<pre><code>#pointlayer {
     point-file: url(somefolder/someimage.jpg);
     point-allow-overlap: true;
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '12, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/b4c566bb2435d700fef4a64bf39842b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gilliard%20Lopes&#39;s gravatar image" />
<p><span>Gilliard Lopes</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gilliard Lopes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14666" class="comments-container">
&#10;</div>
<div id="comment-tools-14666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14666-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33331"></span>

<div id="answer-container-33331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Does it work with the default styling? See if a red dot shows up (it does for me, TileMill 0.10.1, Mac OS X). If it does, your CSS or jpg is at fault; if it doesn't, your CSV is at fault.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '14, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0815777a5dffaa23be873e95a1ed930f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josephcheek&#39;s gravatar image" />
<p><span>josephcheek</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josephcheek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33331" class="comments-container">
&#10;</div>
<div id="comment-tools-33331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33331-form-container" class="comment-form-container">
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

