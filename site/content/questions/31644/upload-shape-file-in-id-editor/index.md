+++
type = "question"
title = "Upload Shape file in iD editor"
description = '''I want to upload the shape file into iD editor and Download it after editing. Is there any way to do this? Please help me in this regard..Eagerly waiting for ur reply.'''
date = "2014-03-18T04:05:00Z"
lastmod = "2014-03-18T11:57:00Z"
weight = 31644
keywords = [ "shapefile", "ideditor" ]
aliases = [ "/questions/31644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Upload Shape file in iD editor](/questions/31644/upload-shape-file-in-id-editor)

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
<span id="post-31644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to upload the shape file into iD editor and Download it after editing. Is there any way to do this? Please help me in this regard..Eagerly waiting for ur reply.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '14, 04:05</strong></p>
<img src="https://secure.gravatar.com/avatar/43980e56796fcfb6ad274541198a38e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mobina&#39;s gravatar image" />
<p><span>Mobina</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mobina has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '14, 13:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31644" class="comments-container">
<span id="31645"></span>
<div id="comment-31645" class="comment">
<div id="post-31645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you looking for a plain shapefile editor?</p>
</div>
<div id="comment-31645-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 07:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31644-form-container" class="comment-form-container">
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

<span id="31647"></span>

<div id="answer-container-31647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31647-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM has it's own datamodel and isn't compatible with default GIS formats out-of-the-box. Esp. the iD editor is very limited to make OSM editing for new users very easy. AFAIK it doesn't offer shapefile import.</p>
<p>What you can do is to <a href="https://wiki.openstreetmap.org/wiki/Shapefile">convert/import your shapefile</a> to an OSM structure, edit it with JOSM and convert the OSM XML back to shapefile.</p>
<p>Personally I would recommend to use QGIS or OpenJUMP to work directly with your shapefile and avoid OSM editors (if you don't have very good reasons to use them).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '14, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-31647" class="comments-container">
<span id="31653"></span>
<div id="comment-31653" class="comment">
<div id="post-31653-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can use shapefiles in Potlatch 2 without any conversion.</p>
</div>
<div id="comment-31653-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 11:57)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31647-form-container" class="comment-form-container">
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

