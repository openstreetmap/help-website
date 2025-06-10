+++
type = "question"
title = "Font size and adding scale to map"
description = '''Hi, I am using my own tiles. How to increase font size of placenames being displayed on map? How to add scale?'''
date = "2011-10-16T08:16:00Z"
lastmod = "2011-10-17T08:41:00Z"
weight = 8467
keywords = [ "and", "font", "tags", "size" ]
aliases = [ "/questions/8467" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Font size and adding scale to map](/questions/8467/font-size-and-adding-scale-to-map)

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
<span id="post-8467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8467-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using my own tiles. How to increase font size of placenames being displayed on map?</p>
<p>How to add scale?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-font" rel="tag" title="see questions tagged &#39;font&#39;">font</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '11, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8467" class="comments-container">
<span id="8469"></span>
<div id="comment-8469" class="comment">
<div id="post-8469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would help if you could add a link to the instructions that you followed to create those tiles - that people will know what tools to give advice about.</p>
</div>
<div id="comment-8469-info" class="comment-info">
<span class="comment-age">(16 Oct '11, 11:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8470"></span>
<div id="comment-8470" class="comment">
<div id="post-8470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a></p>
<p>I have used followed insructions given on this link. I am using mapnik to generate tiles.</p>
</div>
<div id="comment-8470-info" class="comment-info">
<span class="comment-age">(16 Oct '11, 11:04)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-8467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8467-form-container" class="comment-form-container">
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

<span id="8472"></span>

<div id="answer-container-8472" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8472-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The font size comes from the style file <em>osm.xml</em>. This includes several lines on the form "<em><code>&lt;textsymbolizer name="name" fontset_name="bold-fonts" size="11"/&gt;</code></em>". You can edit the <em>size</em> parameter in the wanted areas to generate a new style with other font sizes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '11, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8472" class="comments-container">
&#10;</div>
<div id="comment-tools-8472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8472-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8481"></span>

<div id="answer-container-8481" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8481-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the scale, if you are using OpenLayers, you have to add the <a href="http://dev.openlayers.org/addins/scalebar/trunk/examples/scalebar.html">ScaleLine control</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '11, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-8481" class="comments-container">
&#10;</div>
<div id="comment-tools-8481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8481-form-container" class="comment-form-container">
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

