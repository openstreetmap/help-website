+++
type = "question"
title = "Restricted Turn Data in OSM?"
description = '''I&#x27;m new to OSM, and I&#x27;m creating a network dataset in ArcGIS pro using OSM data for Greater New Orleans. I&#x27;m wondering if OSM has any turn restriction data available already, or if I&#x27;d need to digitize and model turns manually :( If there is no data available through OSM and I do need to digitize/do...'''
date = "2021-07-24T00:16:00Z"
lastmod = "2021-07-24T03:16:00Z"
weight = 81074
keywords = [ "networkanalysis", "turn_restrictions" ]
aliases = [ "/questions/81074" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Restricted Turn Data in OSM?](/questions/81074/restricted-turn-data-in-osm)

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
<span id="post-81074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM, and I'm creating a network dataset in ArcGIS pro using OSM data for Greater New Orleans. I'm wondering if OSM has any turn restriction data available already, or if I'd need to digitize and model turns manually :(</p>
<p>If there is no data available through OSM and I do need to digitize/do everything manually, can anyone point me to any guide(s) related to best practices for restricting left turns and u-turns for city buses? Or any general rules of thumb</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-networkanalysis" rel="tag" title="see questions tagged &#39;networkanalysis&#39;">networkanalysis</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '21, 00:16</strong></p>
<img src="https://secure.gravatar.com/avatar/66567c25b8a5af94bdef892f832fabda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alittman7&#39;s gravatar image" />
<p><span>alittman7</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alittman7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81074" class="comments-container">
&#10;</div>
<div id="comment-tools-81074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81074-form-container" class="comment-form-container">
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

<span id="81076"></span>

<div id="answer-container-81076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81076-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Turn restrictions are generally modelled in OSM as relations. <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">This page</a> is probably the best starting point for how they are stored. The scheme supports limiting the applicable modes of transport if required.</p>
<p>Turn restrictions generally shouldn't be added to OSM explicitly when the turn is already prohibited by other data, e.g. when there a restriction on turning right to go backward up a oneway street. As for most things, OSM's level of completeness varies from place to place.</p>
<p>I'm not familiar with your software for how to convert to something you'll find useful. If ArcGIS's native tools don't parse OSM turn restrictions by default, then you <em>may</em> be able to integrate with a <a href="https://wiki.openstreetmap.org/wiki/Routing#Developers">routing engine</a> that does and avoid reinventing the wheel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '21, 03:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-81076" class="comments-container">
&#10;</div>
<div id="comment-tools-81076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81076-form-container" class="comment-form-container">
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

