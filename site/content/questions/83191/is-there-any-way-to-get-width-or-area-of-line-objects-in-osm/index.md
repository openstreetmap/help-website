+++
type = "question"
title = "Is there any way to get width or area of line objects in OSM?"
description = '''I want to get width or area of the road data in OSM. All of the road data from OSM are lines, so I cannot get the width or area info of these roads. If these were polygon data, I would have calculated the area using QGIS.. But these are in lines, so I can&#x27;t know how wide the road is. If there is a w...'''
date = "2022-01-25T18:02:00Z"
lastmod = "2023-05-11T19:52:00Z"
weight = 83191
keywords = [ "width", "line", "road" ]
aliases = [ "/questions/83191" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to get width or area of line objects in OSM?](/questions/83191/is-there-any-way-to-get-width-or-area-of-line-objects-in-osm)

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
<span id="post-83191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83191-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get width or area of the road data in OSM. All of the road data from OSM are lines, so I cannot get the width or area info of these roads. If these were polygon data, I would have calculated the area using QGIS.. But these are in lines, so I can't know how wide the road is. If there is a way to check the width of the road, please let me know... Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '22, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/5428847fcf430062f12fce828104022a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hshshshshshs&#39;s gravatar image" />
<p><span>hshshshshshs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hshshshshshs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83191" class="comments-container">
&#10;</div>
<div id="comment-tools-83191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83191-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="83195"></span>

<div id="answer-container-83195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83195-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-83195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:width">width</a> tag is used to describe how wide a way is. However, the width tag isn't used very often on highways (about 1% of highway ways have this tag). I also tend to see this tag used more often on trails than on roads.</p>
<p>Beyond that, you would have to come up with other methods to approximate the width. For example, you could use the number of <a href="https://wiki.openstreetmap.org/wiki/Key:lanes">lanes</a> along with an average lane width to come up with a close approximation. If a way doesn't even have the lanes tagged, then you might have to come up with an approximation based on the highway=* tag (e.g. define residential as 9m, trunk as 20m, etc.).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '22, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-83195" class="comments-container">
<span id="83215"></span>
<div id="comment-83215" class="comment">
<div id="post-83215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In addition to lanes using simple rules of thumb for width of each road class can work well: I used this approach for land cover data in 2011.</p>
</div>
<div id="comment-83215-info" class="comment-info">
<span class="comment-age">(26 Jan '22, 13:03)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-83195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83207"></span>

<div id="answer-container-83207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83207-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a high resolution image, it's possible to get a approximate value by measure the width of the road on the screen with a ruler and compare this with the scale in the upper corner of JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '22, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83207" class="comments-container">
<span id="87249"></span>
<div id="comment-87249" class="comment">
<div id="post-87249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and do that a million times ?</p>
</div>
<div id="comment-87249-info" class="comment-info">
<span class="comment-age">(11 May '23, 19:52)</span> <span class="comment-user userinfo">MartinMTB</span>
</div>
</div>
</div>
<div id="comment-tools-83207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87248"></span>

<div id="answer-container-87248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87248-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>if you want to know how wide the road is drawn, vs how wide it really is, i would take a look at the source code of the tile servers, because that code obviously knows.</p>
<p>i used lanes, that doesn't work, i looked around in LA where some highways have 6 lanes, they are drawn the same way as 3 lane roads</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '23, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/2ba037c7b539df6385ec6f1c6c25b184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinMTB&#39;s gravatar image" />
<p><span>MartinMTB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinMTB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87248" class="comments-container">
&#10;</div>
<div id="comment-tools-87248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87248-form-container" class="comment-form-container">
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

