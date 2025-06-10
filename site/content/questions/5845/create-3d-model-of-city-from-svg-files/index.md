+++
type = "question"
title = "Create 3D model of city from SVG files?"
description = '''How do I create 3D model of a city from SVG files? '''
date = "2011-06-17T12:00:00Z"
lastmod = "2011-06-21T12:13:00Z"
weight = 5845
keywords = [ "city", "svg", "3d" ]
aliases = [ "/questions/5845" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Create 3D model of city from SVG files?](/questions/5845/create-3d-model-of-city-from-svg-files)

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
<span id="post-5845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5845-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-5845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I create 3D model of a city from SVG files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '11, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/df9d3b90ceceb51ff03ab438b7207d08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeffmorris&#39;s gravatar image" />
<p><span>jeffmorris</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeffmorris has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '11, 15:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-5845" class="comments-container">
<span id="5849"></span>
<div id="comment-5849" class="comment">
<div id="post-5849-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please edit your question and tell us why you want to create from SVG files? What is your data source?</p>
</div>
<div id="comment-5849-info" class="comment-info">
<span class="comment-age">(17 Jun '11, 12:23)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-5845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5845-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="5852"></span>

<div id="answer-container-5852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5852-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible to create 3D city models from OpenStreetMap data. However, it doesn't make sense to convert OSM data to SVG first, because by doing so you will lose almost all of the information that you will need for your city model: for example, SVG files usually don't contain any height, incline, or elevation information.</p>
<p>Instead, software that creates 3D models from OSM will directly work with files or databases containing OpenStreetMap data. See <a href="http://wiki.openstreetmap.org/wiki/3D_Development">3D Development</a> and the <a href="http://wiki.openstreetmap.org/wiki/Renderers#3D_Rendering">3D Rendering</a> section in the OSM wiki for some attempts to create 3D models in various formats based on OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '11, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-5852" class="comments-container">
&#10;</div>
<div id="comment-tools-5852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5852-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5846"></span>

<div id="answer-container-5846" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5846-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely answer: You don't.</p>
<p>What kind of model do you want to create, and what kind of SVG files do you have? Do these SVG files contain height information at all?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '11, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-5846" class="comments-container">
&#10;</div>
<div id="comment-tools-5846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5848"></span>

<div id="answer-container-5848" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One hint about creating 3D models out of <strong>OSM</strong> data:</p>
<p>Have a look at the OSM wiki at <a href="http://wiki.openstreetmap.org/wiki/3D_Development">3D_Development</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '11, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-5848" class="comments-container">
&#10;</div>
<div id="comment-tools-5848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5848-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5864"></span>

<div id="answer-container-5864" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5864-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-5864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried to use SketchUp program to create 3D model of a city but if I use the "Geo-Location" command to get the images of the city that I want to model, the trees in the images block the view of the streets and roads that I want to model. Also, the auto-snapping feature in SketchUp always gets in the way and I think that there's no way of disabling the auto-snapping feature. I want to use images from Open Street Maps, Google Maps, or NYCityMap but the only way to get the images from those websites is to use the "Print Screen" key, load the images into Paint Shop Pro program, and combine the images into one large image.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '11, 01:13</strong></p>
<img src="https://secure.gravatar.com/avatar/df9d3b90ceceb51ff03ab438b7207d08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeffmorris&#39;s gravatar image" />
<p><span>jeffmorris</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeffmorris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5864" class="comments-container">
<span id="5919"></span>
<div id="comment-5919" class="comment">
<div id="post-5919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You should ask these questions in a Sketchup-Forum, not in the openstreetmap forum.</p>
<p>There are other methods to automatically download the images in question, but it is forbidden by the usage terms of the entities that offer the service, at least if you do it in significant quantity.</p>
</div>
<div id="comment-5919-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 12:13)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-5864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5864-form-container" class="comment-form-container">
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

