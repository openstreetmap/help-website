+++
type = "question"
title = "Change Street and Highway color?"
description = '''Is is possible to change the color of the lines representing roads and highways to black or possibly blue?'''
date = "2015-11-17T00:39:00Z"
lastmod = "2015-11-17T09:23:00Z"
weight = 46642
keywords = [ "rendering", "colors", "style", "highway" ]
aliases = [ "/questions/46642" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change Street and Highway color?](/questions/46642/change-street-and-highway-color)

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
<span id="post-46642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is is possible to change the color of the lines representing roads and highways to black or possibly blue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '15, 00:39</strong></p>
<img src="https://secure.gravatar.com/avatar/35b524a6ab63e74fa2dc18f3ac3464c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralphjh&#39;s gravatar image" />
<p><span>ralphjh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralphjh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '15, 09:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-46642" class="comments-container">
<span id="46645"></span>
<div id="comment-46645" class="comment">
<div id="post-46645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it's possible, but complicated. For us to give you useful information you need to provide more information about your goals.</p>
</div>
<div id="comment-46645-info" class="comment-info">
<span class="comment-age">(17 Nov '15, 06:00)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-46642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46642-form-container" class="comment-form-container">
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

<span id="46649"></span>

<div id="answer-container-46649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short: No it's not possible to change the colors on osm.org itself. You might want to checkout <a href="https://wiki.openstreetmap.org/wiki/Maps">other maps</a> which rely on OSM data.</p>
<p>Long: OSM.org uses a rendered 'raster map' to display information, which can't be altered that way. Instead you have to tweak the map style, which is part of the <a href="https://wiki.openstreetmap.org/wiki/Rendering">rendering stack</a>. As <a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a> mentioned, this is pretty complex, and if you really like to do your own map style, you should rely on simple desktop renderer solutions as maperitive, tilemill, ... . IMHO creating an own style just for colouring the ways makes no sense ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '15, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-46649" class="comments-container">
&#10;</div>
<div id="comment-tools-46649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46649-form-container" class="comment-form-container">
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

