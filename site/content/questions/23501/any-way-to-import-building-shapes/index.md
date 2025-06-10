+++
type = "question"
title = "Any way to import building shapes?"
description = '''I&#x27;m just getting started here to see if we can use OSM for our campus maps. Anyway, I&#x27;m in the middle of a large project creating a map of our campuses for print using Adobe Illustrator. needless to say, all of the building shapes are drawn already in Illustrator. Is there any way to make use of tho...'''
date = "2013-06-18T19:39:00Z"
lastmod = "2013-06-18T19:58:00Z"
weight = 23501
keywords = [ "import", "illustrator" ]
aliases = [ "/questions/23501" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Any way to import building shapes?](/questions/23501/any-way-to-import-building-shapes)

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
<span id="post-23501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm just getting started here to see if we can use OSM for our campus maps. Anyway, I'm in the middle of a large project creating a map of our campuses for print using Adobe Illustrator. needless to say, all of the building shapes are drawn already in Illustrator. Is there any way to make use of those shapes in OSM, or should I just resign myself to redrawing everything that is missing, and editing what is there already.</p>
<p>I'm loving the editing tools so far BTW.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-illustrator" rel="tag" title="see questions tagged &#39;illustrator&#39;">illustrator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '13, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/6f197a6bc17c8c55f68a1102707b7247?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="URcommunications&#39;s gravatar image" />
<p><span>URcommunicat...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="URcommunications has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23501" class="comments-container">
&#10;</div>
<div id="comment-tools-23501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23501-form-container" class="comment-form-container">
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

<span id="23502"></span>

<div id="answer-container-23502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23502-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, this isn't really practical. Illustrator files aren't georeferenced in any way - that is, there's no way of stating within the file that a certain point on the map relates to a certain location in the world. So you'd have to find some way of getting that information in, then translating to a format that an OSM editor can read (say, shapefiles).</p>
<p>It might be possible for really clever people with maximum GDAL-fu, or by using an Illustrator plug-in such as the (paid-for) <a href="http://www.avenza.com/mapublisher">MAPublisher</a>. But even as an inveterate Illustrator user and author of one of OSM's editor programs, I wouldn't attempt it.</p>
<p>One possible compromise is to save the maps from Illustrator as raster images (using the Save For Web... command), then use the <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/PicLayer">PicLayer plugin</a> for the JOSM editor to help you trace them into OSM. You'll still have to do the laborious tracing work, but at least you'll have your original maps to work from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '13, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '13, 19:47</strong> </span></p>
</div>
</div>
<div id="comments-container-23502" class="comments-container">
<span id="23503"></span>
<div id="comment-23503" class="comment">
<div id="post-23503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I'm not worried about tracing work; at least it would be more accurate than me just having a printout next to me while I stare at the screen. :) Thanks.</p>
<p>Mike O</p>
</div>
<div id="comment-23503-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 19:50)</span> <span class="comment-user userinfo">URcommunicat...</span>
</div>
</div>
<span id="23504"></span>
<div id="comment-23504" class="comment">
<div id="post-23504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This Q may help if any shapes are repeated <a href="https://help.openstreetmap.org/questions/5753/can-shapes-be-copied">https://help.openstreetmap.org/questions/5753/can-shapes-be-copied</a></p>
</div>
<div id="comment-23504-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 19:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-23502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23502-form-container" class="comment-form-container">
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

