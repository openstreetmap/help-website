+++
type = "question"
title = "List Allowed Access tags"
description = '''I&#x27;m in the UK and I want to be able to use OSM to plot routes (using Plotaroute.com). I&#x27;ve seen on another post ... https://help.openstreetmap.org/questions/35124/how-to-go-about-resolving-the-uk-trunk-tag-issue that trunk roads in the UK have the wrong defaults. That means that trunk roads are mark...'''
date = "2021-02-21T18:11:00Z"
lastmod = "2021-02-21T21:27:00Z"
weight = 78968
keywords = [ "access", "trunk" ]
aliases = [ "/questions/78968" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [List Allowed Access tags](/questions/78968/list-allowed-access-tags)

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
<span id="post-78968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78968-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm in the UK and I want to be able to use OSM to plot routes (using Plotaroute.com). I've seen on another post ... <a href="https://help.openstreetmap.org/questions/35124/how-to-go-about-resolving-the-uk-trunk-tag-issue">https://help.openstreetmap.org/questions/35124/how-to-go-about-resolving-the-uk-trunk-tag-issue</a> that trunk roads in the UK have the wrong defaults. That means that trunk roads are marked as not suitable for bikes, for example</p>
<p>Is there a way to list all the trunk roads within an area, such as a UK County, with their Allowed Access tags - or simply a list of all the ones which look as if they could be wrong.</p>
<p>If that list also acted as a front end to update those Allowed Access tags, that would be even better</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-trunk" rel="tag" title="see questions tagged &#39;trunk&#39;">trunk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '21, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/8a214017f7a8bd3ab63ec6498f3bf23f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Winding_Road&#39;s gravatar image" />
<p><span>Winding_Road</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Winding_Road has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78968" class="comments-container">
<span id="78971"></span>
<div id="comment-78971" class="comment">
<div id="post-78971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My answer to that help question was written with a certain amount of "British Reserve". If you took away from that "that trunk roads in the UK have the wrong defaults" clearly I should have been a bit more forthright!</p>
<p>Perhaps: "OSM is correct - if some &lt;expletive&gt; router is giving the wrong answer please log a bug with that router, don't try and change the data in OSM to match it".</p>
</div>
<div id="comment-78971-info" class="comment-info">
<span class="comment-age">(21 Feb '21, 21:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78968-form-container" class="comment-form-container">
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

<span id="78969"></span>

<div id="answer-container-78969" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78969-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Per the responses on the page you link; the <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access_restrictions#United_Kingdom">advice for routing engines</a> says trunk roads should be considered permissible for bicycle use etc.</p>
<p>OSM was started in the UK and its UK road data is fairly mature. If plotaroute is giving odd routing results I would try one of the <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services#Routing">other routing services</a> before making changes.</p>
<p>I'm not aware of a general overlay for access tags, <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo</a> is probably your best bet for constructing your own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '21, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-78969" class="comments-container">
&#10;</div>
<div id="comment-tools-78969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78969-form-container" class="comment-form-container">
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

