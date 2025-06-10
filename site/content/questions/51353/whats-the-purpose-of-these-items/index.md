+++
type = "question"
title = "What&#x27;s the purpose of these items ?"
description = '''Hi, If i search for &quot;Corse&quot; (a french region) in nominatim, I get all these results   A node for the center of the island : http://www.openstreetmap.org/node/61083317 The administrative boundaries : http://www.openstreetmap.org/relation/76910 A way for the boundary of a small island that is away fro...'''
date = "2016-08-11T16:41:00Z"
lastmod = "2016-08-11T21:45:00Z"
weight = 51353
keywords = [ "newbie", "france" ]
aliases = [ "/questions/51353" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What's the purpose of these items ?](/questions/51353/whats-the-purpose-of-these-items)

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
<span id="post-51353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51353-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>If i search for "Corse" (a french region) in nominatim, I get all these results</p>
<ul>
<li>A node for the center of the island : <a href="http://www.openstreetmap.org/node/61083317">http://www.openstreetmap.org/node/61083317</a></li>
<li>The administrative boundaries : <a href="http://www.openstreetmap.org/relation/76910">http://www.openstreetmap.org/relation/76910</a></li>
<li>A way for the boundary of a small island that is away from corse but part of it : <a href="http://www.openstreetmap.org/way/239142487#map=17/42.96388/9.34187">http://www.openstreetmap.org/way/239142487#map=17/42.96388/9.34187</a></li>
<li>Another one <a href="http://www.openstreetmap.org/way/239132562">http://www.openstreetmap.org/way/239132562</a></li>
</ul>
<p>I'm new in OSM and I don't really know what i'm supposed to do here : - Is it normal to have a node and a relation for the same entity ? (I don't have this for all the french regions) - Is it normal to create a way with a name that reference it's parent entity when it's just here for having the shape of the island - Is it normal that these ways are not in the main relationship (<a href="http://www.openstreetmap.org/relation/76910)">http://www.openstreetmap.org/relation/76910)</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '16, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5315b6ec74cb3e60c60497cc5448c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r%C3%A9mi%20ctv&#39;s gravatar image" />
<p><span>rémi ctv</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rémi ctv has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 16:42</strong> </span></p>
</div>
</div>
<div id="comments-container-51353" class="comments-container">
&#10;</div>
<div id="comment-tools-51353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51353-form-container" class="comment-form-container">
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

<span id="51359"></span>

<div id="answer-container-51359" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51359-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The node is for example used for label placing (is has a role "label" in the relation below). The administrative boundary is the mainland territory The small islands are also part of Corsica (they are members of the administrative boundary relation above)</p>
<p>If you're new to OSM... starting with administrative boundaries may not be the easiest way to start. Relations are used heavily and multiple relations are usually defined using the same ways for each administrative level. If you're using iD (online OSM editor in your browser) you can get lost very quickly with relations especially big ones line that.</p>
<p>If you need help in french, or want to get in touch with active french contributors, join us at <a href="http://forum.openstreetmap.fr/">http://forum.openstreetmap.fr/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '16, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/53496360a70e1dc9e05f4f0ffb2c13c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cquest&#39;s gravatar image" />
<p><span>cquest</span><br />
<span class="score" title="691 reputation points">691</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cquest has 5 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-51359" class="comments-container">
&#10;</div>
<div id="comment-tools-51359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51359-form-container" class="comment-form-container">
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

