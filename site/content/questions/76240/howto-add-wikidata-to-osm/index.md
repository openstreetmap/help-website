+++
type = "question"
title = "Howto add wikidata to OSM?"
description = '''My main question: how should I tag wikidata to the OSM map? I found that there are 2 main tags: &quot;wikidata&quot; and &quot;subject:wikidata&quot;, but have a hard time figuring out which one to use. As an example, I have this wikidata street: https://www.wikidata.org/wiki/Q19395563 It matches with 2 ways in OSM: ht...'''
date = "2020-08-20T17:10:00Z"
lastmod = "2020-08-20T18:57:00Z"
weight = 76240
keywords = [ "wikidata" ]
aliases = [ "/questions/76240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Howto add wikidata to OSM?](/questions/76240/howto-add-wikidata-to-osm)

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
<span id="post-76240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My main question: how should I tag wikidata to the OSM map? I found that there are 2 main tags: "wikidata" and "subject:wikidata", but have a hard time figuring out which one to use.</p>
<p>As an example, I have this wikidata street: <a href="https://www.wikidata.org/wiki/Q19395563">https://www.wikidata.org/wiki/Q19395563</a></p>
<p>It matches with 2 ways in OSM: <a href="https://www.openstreetmap.org/way/36192298">https://www.openstreetmap.org/way/36192298</a> and <a href="https://www.openstreetmap.org/way/7010849">https://www.openstreetmap.org/way/7010849</a></p>
<p>My current idea is to add a "wikidata":"Q19395563" to both those ways. Would that be okay?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '20, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/60b3480b9416628d1dc42c9abacfaa3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koen%20Rijnsent&#39;s gravatar image" />
<p><span>Koen Rijnsent</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koen Rijnsent has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76240" class="comments-container">
&#10;</div>
<div id="comment-tools-76240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76240-form-container" class="comment-form-container">
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

<span id="76241"></span>

<div id="answer-container-76241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76241-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-76241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Placing <code>wikidata=Q19395563</code> on the ways seems reasonable.</p>
<p><code>subject:wikidata</code> is used for items like statues where the statue itself may not have a wikidata tag, but there is a wikidata tag for what it depicts. See <a href="https://wiki.openstreetmap.org/wiki/Key:wikidata">here</a> for further details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '20, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76241" class="comments-container">
&#10;</div>
<div id="comment-tools-76241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76241-form-container" class="comment-form-container">
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

