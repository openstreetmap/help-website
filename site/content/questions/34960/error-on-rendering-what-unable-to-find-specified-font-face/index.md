+++
type = "question"
title = "Error on rendering: what():  Unable to find specified font face &#x27;&#x27;"
description = '''Hi! I&#x27;ve been converting a Mapnik XML export which I created with TileMill on my desktop. I have now implemented it into renderd/mapnik, but when rendering some parts of the map it triggers the error below. what(): Unable to find specified font face &#x27;&#x27;  I assume this is as a result of a part of the ...'''
date = "2014-07-18T11:37:00Z"
lastmod = "2014-07-18T17:11:00Z"
weight = 34960
keywords = [ "tilemill", "font", "osm", "renderd", "mapnik" ]
aliases = [ "/questions/34960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error on rendering: what(): Unable to find specified font face ''](/questions/34960/error-on-rendering-what-unable-to-find-specified-font-face)

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
<span id="post-34960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34960-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I've been converting a Mapnik XML export which I created with TileMill on my desktop. I have now implemented it into renderd/mapnik, but when rendering some parts of the map it triggers the error below.</p>
<pre><code>what():  Unable to find specified font face &#39;&#39;</code></pre>
<p>I assume this is as a result of a part of the map requiring some font which fails.</p>
<p>Does anyone have a tip to hw I should address finding what causes this error? I've tried searching through the config for font-faces which could contain an error, but I haven't found anything.</p>
<p><strong>EDIT:</strong> It seems like when removing all font-face references it works. Is there a wrong way to reference fonts?</p>
<p><strong>EDIT2:</strong> <a href="http://pastebin.com/8VzRTbRz">http://pastebin.com/8VzRTbRz</a> This would be a relevant example of using fonts in Mapnik XML and Carto.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-font" rel="tag" title="see questions tagged &#39;font&#39;">font</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '14, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/2dca8d9579d6899ae2d831776fdfb21b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoMs&#39;s gravatar image" />
<p><span>JoMs</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoMs has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '14, 16:32</strong> </span></p>
</div>
</div>
<div id="comments-container-34960" class="comments-container">
<span id="34973"></span>
<div id="comment-34973" class="comment">
<div id="post-34973-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You'll need to provide either the relevant part of the CartoCSS or the relevant part of the mapnik XML file for anyone to be able to figure out what's going on.</p>
</div>
<div id="comment-34973-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 16:21)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="34974"></span>
<div id="comment-34974" class="comment">
<div id="post-34974-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://pastebin.com/8VzRTbRz">http://pastebin.com/8VzRTbRz</a> This would be a relevant example of using fonts.</p>
</div>
<div id="comment-34974-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 16:27)</span> <span class="comment-user userinfo">JoMs</span>
</div>
</div>
<span id="34976"></span>
<div id="comment-34976" class="comment">
<div id="post-34976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You haven't provided either the definition for @sans_italic nor the &lt;fontset&gt; sections of the xml!</p>
</div>
<div id="comment-34976-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 16:41)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="34977"></span>
<div id="comment-34977" class="comment">
<div id="post-34977-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry about that. Here's the definition for the fonts <a href="http://pastebin.com/0Xr1BRgU">http://pastebin.com/0Xr1BRgU</a></p>
</div>
<div id="comment-34977-info" class="comment-info">
<span class="comment-age">(18 Jul '14, 16:44)</span> <span class="comment-user userinfo">JoMs</span>
</div>
</div>
</div>
<div id="comment-tools-34960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34960-form-container" class="comment-form-container">
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

<span id="34979"></span>

<div id="answer-container-34979" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34979-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>User error of dimensions!</p>
<p>The problem was that the fonts called Italic in the XML should be Oblique.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '14, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2dca8d9579d6899ae2d831776fdfb21b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoMs&#39;s gravatar image" />
<p><span>JoMs</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoMs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34979" class="comments-container">
&#10;</div>
<div id="comment-tools-34979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34979-form-container" class="comment-form-container">
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

