+++
type = "question"
title = "changing the color of a line"
description = '''Hi, we have 2 ports in our management. We have used &#x27;lines&#x27; to put the piers and jetties on the map. Is there any way to change the colour of the lines as we have piers of different lengths?'''
date = "2022-01-06T16:13:00Z"
lastmod = "2022-01-07T12:23:00Z"
weight = 82974
keywords = [ "line" ]
aliases = [ "/questions/82974" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changing the color of a line](/questions/82974/changing-the-color-of-a-line)

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
<span id="post-82974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82974-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, we have 2 ports in our management. We have used 'lines' to put the piers and jetties on the map. Is there any way to change the colour of the lines as we have piers of different lengths?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '22, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/afe12d3e9f76ff609a7acebec09eb871?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koen%20Prikken&#39;s gravatar image" />
<p><span>Koen Prikken</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koen Prikken has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82974" class="comments-container">
<span id="82977"></span>
<div id="comment-82977" class="comment">
<div id="post-82977-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what software you are asking about?</p>
</div>
<div id="comment-82977-info" class="comment-info">
<span class="comment-age">(06 Jan '22, 21:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82974-form-container" class="comment-form-container">
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

<span id="82981"></span>

<div id="answer-container-82981" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82981-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>Usually, the color of a line is only based on the tags applied, that is its typology. Especially on the default tile layer (called osm-carto), which is mainly designed to help mappers validate their work.</p>
<p>Depending on your needs, you could overlay a new color, for example using mapCSS in overpass-turbo or using uMap, or you can design a new map style based on your specific needs (Mapbox Studio does that with a GUI, or you could set up a full rendering server with a modified version of osm-carto).</p>
<p>If you don't understand the propositions, please have a look at the wiki, and ask a more detailed question.</p>
<p>Warning, you can't change the tags of a line to change the color on the map. The tags are meant to represent the on-the-ground truth, renderers (and maps styles' creators) makes their own choice as to how to represent the tags.</p>
<p>That being said, I've never heard of features represented differently based on their length.</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '22, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82981" class="comments-container">
&#10;</div>
<div id="comment-tools-82981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82981-form-container" class="comment-form-container">
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

