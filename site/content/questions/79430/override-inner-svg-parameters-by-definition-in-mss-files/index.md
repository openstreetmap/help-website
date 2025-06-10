+++
type = "question"
title = "Override inner SVG parameters by definition in .mss files"
description = '''Hi, In general I try to override colour of motorway shield, but there are many of SVG&#x27;s files with already defined background colour. What I want to achieve is not to edit all SVG&#x27;s but instead of that I would like to define that values directly in .mss files. I got familiar with mapnik documentatio...'''
date = "2021-03-29T10:30:00Z"
lastmod = "2021-03-30T11:09:00Z"
weight = 79430
keywords = [ "style", "carto", "mapnik" ]
aliases = [ "/questions/79430" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Override inner SVG parameters by definition in .mss files](/questions/79430/override-inner-svg-parameters-by-definition-in-mss-files)

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
<span id="post-79430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79430-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, In general I try to override colour of motorway shield, but there are many of <code>SVG</code>'s files with already defined background colour.<br />
What I want to achieve is not to edit all <code>SVG</code>'s but instead of that I would like to define that values directly in <code>.mss</code> files. I got familiar with <a href="https://cartocss.readthedocs.io/en/latest/mapnik_api.html#markers">mapnik documentation</a> but I couldn't find anything related to my problem.<br />
In general the <code>SVG</code> of road shield looks like that:<br />
<img src="https://help.openstreetmap.org/upfiles/SVG.png" alt="alt text" /><br />
(I'm sorry byt I've got problems with pasting that structure as a code..)<br />
And as you can see the colour of shield (fill) and stroke around (stroke) is already defined in file.<br />
Is there a way to override that values directly from style files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '21, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '21, 10:31</strong> </span></p>
</div>
</div>
<div id="comments-container-79430" class="comments-container">
&#10;</div>
<div id="comment-tools-79430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79430-form-container" class="comment-form-container">
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

<span id="79433"></span>

<div id="answer-container-79433" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79433-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="engopy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using openstreetmap-carto as a base for your custom style, there is a script called generate_shields.py ( <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/scripts/generate_shields.py">https://github.com/gravitystorm/openstreetmap-carto/blob/master/scripts/generate_shields.py</a> ) that is responsible for the generation of those svg files. And that script refers to generate_road_colours.py ( <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/scripts/generate_road_colours.py">https://github.com/gravitystorm/openstreetmap-carto/blob/master/scripts/generate_road_colours.py</a> ) and that one uses values as defined in road-colors.yaml ( <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/road-colors.yaml">https://github.com/gravitystorm/openstreetmap-carto/blob/master/road-colors.yaml</a> ).</p>
<p>So to change the appearance of road colours and attached shields, you would have to edit the road-colors.yaml and than run those scripts again to get the svg shield files and the road-colours-generated.mss</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '21, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-79433" class="comments-container">
<span id="79446"></span>
<div id="comment-79446" class="comment">
<div id="post-79446-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes I use carto by gravitystorm. Thanks, it completely solved my problem.</p>
</div>
<div id="comment-79446-info" class="comment-info">
<span class="comment-age">(30 Mar '21, 11:09)</span> <span class="comment-user userinfo">engopy</span>
</div>
</div>
</div>
<div id="comment-tools-79433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79433-form-container" class="comment-form-container">
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

