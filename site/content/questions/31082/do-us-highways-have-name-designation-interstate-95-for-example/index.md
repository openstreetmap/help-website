+++
type = "question"
title = "Do US highways have name designation -  interstate 95 for example?"
description = '''I am interested in extracting a few US highway and railway routes from planet.osm. Do highways - and/or railways - include highway number designations? Interstate 95 - running down the east coast. Or, here in Boston the MBTA Red Line? Thanks, Doug'''
date = "2014-02-27T12:56:00Z"
lastmod = "2014-02-27T15:48:00Z"
weight = 31082
keywords = [ "railway", "highway" ]
aliases = [ "/questions/31082" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Do US highways have name designation - interstate 95 for example?](/questions/31082/do-us-highways-have-name-designation-interstate-95-for-example)

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
<span id="post-31082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31082-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested in extracting a few US highway and railway routes from planet.osm. Do highways - and/or railways - include highway number designations? Interstate 95 - running down the east coast. Or, here in Boston the MBTA Red Line?</p>
<p>Thanks, Doug</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '14, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/07d688a0c3f08059d5172b188222d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dugla&#39;s gravatar image" />
<p><span>dugla</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dugla has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31082" class="comments-container">
&#10;</div>
<div id="comment-tools-31082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31082-form-container" class="comment-form-container">
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

<span id="31090"></span>

<div id="answer-container-31090" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31090-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dugla has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Data is in OSM that people put into OSM. Highways and railways may include something in the name tag, but they may not. For highway numbers, you want to look in the ref tag. You can find more detail about <a href="https://wiki.openstreetmap.org/wiki/Highway">highway tagging</a> on the OSM wiki.</p>
<p>In addition, many major highways will be collected in relations, such as this one for <a href="https://www.openstreetmap.org/relation/396358">I-95 in Massachusetts</a>. Some bus/train routes are also collected in relations, such as this one for <a href="https://www.openstreetmap.org/relation/1617343">Route 1 in Boston</a>. You can find more info on <a href="https://wiki.openstreetmap.org/wiki/Route_relation">route relations</a> on the OSM wiki. Transit routes are also viewable on the Transportation layer on the main OSM website.</p>
<p>To one of your specific questions, I don't see the Red Line in OSM, which is a little surprising as Mass GIS has released a lot of data under an open license, and much of it has been imported in. If that's a specific need, you can get it from <a href="http://www.mass.gov/anf/research-and-tech/it-serv-and-support/application-serv/office-of-geographic-information-massgis/datalayers/mbta.html">MassGIS</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '14, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-31090" class="comments-container">
<span id="31092"></span>
<div id="comment-31092" class="comment">
<div id="post-31092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Super helpful @neuhauser. Hang on, my mind is a bit blown here, how was the I-95/Mass map created? Is this a specific trace created by jremillard (the author)? Can I create one myself?</p>
</div>
<div id="comment-31092-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 15:26)</span> <span class="comment-user userinfo">dugla</span>
</div>
</div>
<span id="31093"></span>
<div id="comment-31093" class="comment">
<div id="post-31093-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>jremillard is just the most recent editor of this relation--you can see that this is version 40. Each way that is part of the relation has its own version history too. Many roads in the US started as imports from TIGER, but others have been traced from imagery, collected via GPS, or imported from other sources (like MassGIS). You can edit OSM if you sign up, just make sure to follow the editing guidelines and use proper sources. If you want to extract data, look through questions tagged export or download.</p>
</div>
<div id="comment-31093-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 15:48)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-31090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31090-form-container" class="comment-form-container">
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

