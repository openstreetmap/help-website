+++
type = "question"
title = "here is a bridge style pier drawn as an area that is rendering with water on the inside"
description = '''here is a bridge style pier drawn as an area that is rendering with water on the inside I was wondering if [this][1] is an known issue/bug or if there is a standardized way of dealing with piers with two or more ways for example making it a multipolygon relation. thanks. [1]: &amp;lt;iframe width=&quot;425&quot; ...'''
date = "2014-03-27T16:02:00Z"
lastmod = "2014-03-27T20:04:00Z"
weight = 31948
keywords = [ "rendering", "marine", "openseamap" ]
aliases = [ "/questions/31948" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [here is a bridge style pier drawn as an area that is rendering with water on the inside](/questions/31948/here-is-a-bridge-style-pier-drawn-as-an-area-that-is-rendering-with-water-on-the-inside)

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
<span id="post-31948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>here is a bridge style pier drawn as an area that is rendering with water on the inside</p>
<p>I was wondering if [this][1] is an known issue/bug or if there is a standardized way of dealing with piers with two or more ways for example making it a multipolygon relation.</p>
<p>thanks.</p>
<p>[1]: &lt;iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.openstreetmap.org/export/embed.html?bbox=-117.17080682516097%2C32.69890634180274%2C-117.16898828744887%2C32.70030801191927&amp;amp;layer=mapnik&amp;amp;marker=32.69960605105383%2C-117.16989755630493" style="border: 1px solid black"&gt;&lt;/iframe&gt;<br />
<span class="small"><a href="http://www.openstreetmap.org/?mlat=32.69961&amp;mlon=-117.16990#map=19/32.69961/-117.16990&amp;layers=N">View Larger Map</a></span></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-marine" rel="tag" title="see questions tagged &#39;marine&#39;">marine</span> <span class="post-tag tag-link-openseamap" rel="tag" title="see questions tagged &#39;openseamap&#39;">openseamap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '14, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/fb26a824cf424005e029fc893f4fb106?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flockfinder&#39;s gravatar image" />
<p><span>flockfinder</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flockfinder has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-31948" class="comments-container">
&#10;</div>
<div id="comment-tools-31948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31948-form-container" class="comment-form-container">
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

<span id="31952"></span>

<div id="answer-container-31952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31952-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Right now it's being rendered correctly for how it's mapped: as two separate linear piers lying end-to-end. I don't see any reason for having the pier made up of two ways. Simply join them into a single closed loop way to make it into an area.</p>
<p>Yes, a multipolygon could be used to make the two ways into one pier area, but that's overkill when it could simply be mapped as a single way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '14, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-31952" class="comments-container">
<span id="31960"></span>
<div id="comment-31960" class="comment">
<div id="post-31960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks alester, I deleted the shorter of the two ways and extended the longer way to form a closed way. It appears to be rendering correctly now. If I recall correctly, when I first worked on this pier months ago it was a single way. I came along and felt like making it an area, so I closed the way thinking it would form a solid platform area. For some reason, it created two ways rather than continuing the already existing single way. But today I noted that it didn't make a single platform area. Fortunately when I extended the way today it just continued the way enabling me to make it a single closed way.</p>
</div>
<div id="comment-31960-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 20:04)</span> <span class="comment-user userinfo">flockfinder</span>
</div>
</div>
</div>
<div id="comment-tools-31952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31952-form-container" class="comment-form-container">
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

