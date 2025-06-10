+++
type = "question"
title = "Noob question on nodes at intersection of pedestrian crosswalks &amp; roads"
description = '''This is a pretty basic question, as I&#x27;m new to OSM, and have been adding some normal sidewalks and their street crossings/pedestrian crosswalks (I think those two terms are used interchangeably in OSM; both set highway=footway and footway=crossing by default). Many of the existing street crossings o...'''
date = "2018-03-15T21:16:00Z"
lastmod = "2018-03-20T00:51:00Z"
weight = 62695
keywords = [ "crossing", "nodes" ]
aliases = [ "/questions/62695" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Noob question on nodes at intersection of pedestrian crosswalks & roads](/questions/62695/noob-question-on-nodes-at-intersection-of-pedestrian-crosswalks-roads)

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
<span id="post-62695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62695-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a pretty basic question, as I'm new to OSM, and have been adding some normal sidewalks and their street crossings/pedestrian crosswalks (I think those two terms are used interchangeably in OSM; both set highway=footway and footway=crossing by default). Many of the existing street crossings on the map have a node just labeled "other" (no tags or other attributes, and they're not used to make a bend in the crossing or road) where the sidewalk intersects the road that it crosses, but some others don't have a node where they cross. Is there correct, or more accepted way, to do this? Also, what is the purpose of the node?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '18, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/56e42ec4ed9aba4fbff1c7d427c60458?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aaarbie&#39;s gravatar image" />
<p><span>Aaarbie</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aaarbie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62695" class="comments-container">
<span id="62696"></span>
<div id="comment-62696" class="comment">
<div id="post-62696-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Can you point to an example? (as in find it on the map and copy paste the browser adress line here)</p>
</div>
<div id="comment-62696-info" class="comment-info">
<span class="comment-age">(15 Mar '18, 22:29)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="62736"></span>
<div id="comment-62736" class="comment">
<div id="post-62736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you include a picture or an example of the location you're talking about?</p>
</div>
<div id="comment-62736-info" class="comment-info">
<span class="comment-age">(20 Mar '18, 00:51)</span> <span class="comment-user userinfo">Mxdanger</span>
</div>
</div>
</div>
<div id="comment-tools-62695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62695-form-container" class="comment-form-container">
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

<span id="62701"></span>

<div id="answer-container-62701" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62701-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When two ways cross at the same level there should be a node. This is irrespective of whether one or both are roads or footways. If they are on different levels, such as in the case of a bridge going over a road, or a tunnel going under, then there should be no node.</p>
<p>Errors are made sometimes, and should be fixed, if found.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '18, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '18, 03:32</strong> </span></p>
</div>
</div>
<div id="comments-container-62701" class="comments-container">
<span id="62704"></span>
<div id="comment-62704" class="comment">
<div id="post-62704-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>(hopefully to make it even clearer) the reason why things that join in real life should have a joining node in real life is so that things like routers that calculate how to get from one place to another know that you can get from one way (the road) to another (the crossing footpath). If there wasn't a joining node they simply would not know.</p>
</div>
<div id="comment-62704-info" class="comment-info">
<span class="comment-age">(16 Mar '18, 21:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62701-form-container" class="comment-form-container">
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

