+++
type = "question"
title = "Tool for creating vector tiles"
description = '''Hi, I am planning to render the osm data on the mobile devices which do not have a connection to the internet. This means that all data will be locally stored on the device. The thing I am looking for is a tool which can generate for me vector tiles for specific zoom levels. I will have a number of ...'''
date = "2011-10-02T19:51:00Z"
lastmod = "2011-10-03T14:10:00Z"
weight = 8238
keywords = [ "tiles", "vector" ]
aliases = [ "/questions/8238" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tool for creating vector tiles](/questions/8238/tool-for-creating-vector-tiles)

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
<span id="post-8238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8238-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am planning to render the osm data on the mobile devices which do <strong>not</strong> have a connection to the internet. This means that all data will be locally stored on the device.</p>
<p>The thing I am looking for is a tool which can generate for me <strong>vector</strong> tiles for specific zoom levels. I will have a number of zoom levels (let's say from 1 to 100) and vector tiles will specify which nodes/ways should be visible for a specific zoom level. It is not an option for me to generate raster tiles because of space limitation on the device.</p>
<p>Could anyone recommend a tool for generating the vector tiles? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '11, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/8e6d66cfd97b0b1d61b2833aa82d45fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dennisk&#39;s gravatar image" />
<p><span>dennisk</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dennisk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8238" class="comments-container">
&#10;</div>
<div id="comment-tools-8238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8238-form-container" class="comment-form-container">
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

<span id="8259"></span>

<div id="answer-container-8259" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8259-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dennisk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several open source <a href="https://wiki.openstreetmap.org/wiki/Android">Android Apps</a> that do offline vector rendering, like <a href="http://osmand.net">OsmAnd</a> or <a href="http://gpsmid.sourceforge.net/">GpsMid</a>. You might get some hints looking at how they do it.</p>
<p><a href="http://code.google.com/p/mapsforge/">mapsforge</a> is a vector based Android map library intended to be used as a basis for own map applications. The vector data is stored in a <a href="http://code.google.com/p/mapsforge/wiki/ConceptualDesignMapFileFormat">binary file format</a>.</p>
<p>There is also a new project <a href="https://wiki.openstreetmap.org/wiki/OSMT">OSMT</a> for tiling OSM XML files, but that is in early stages and does not support relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '11, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8259" class="comments-container">
&#10;</div>
<div id="comment-tools-8259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8259-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8244"></span>

<div id="answer-container-8244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8244-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> is pretty much the first port of call for loading OSM data into a database, getting it out again, and chopping and changing along the way. You should investigate that as your first port of call.</p>
<p>Note that other providers, such as <a href="http://developers.cloudmade.com/projects/show/vector-tiles">CloudMade</a>, have already produced vector tiles. You may find it worthwhile seeing what they've done, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '11, 01:09</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8244" class="comments-container">
&#10;</div>
<div id="comment-tools-8244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8244-form-container" class="comment-form-container">
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

