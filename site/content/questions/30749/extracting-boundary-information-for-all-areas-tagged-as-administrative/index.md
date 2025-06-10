+++
type = "question"
title = "Extracting boundary information for all areas tagged as administrative"
description = '''Is there is a way to extract only those reference points along with node id for locations tagged as administration boundary. That is no street information just node id with the latitude, longitude reading of the boundary area?'''
date = "2014-02-15T09:44:00Z"
lastmod = "2014-02-15T12:07:00Z"
weight = 30749
keywords = [ "extract", "admin_boundary", "tags" ]
aliases = [ "/questions/30749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting boundary information for all areas tagged as administrative](/questions/30749/extracting-boundary-information-for-all-areas-tagged-as-administrative)

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
<span id="post-30749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there is a way to extract only those reference points along with node id for locations tagged as administration boundary.</p>
<p>That is no street information just node id with the latitude, longitude reading of the boundary area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '14, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/1a7106e1bd2d5ab3edf26035a27e7b90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichaB&#39;s gravatar image" />
<p><span>RichaB</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichaB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30749" class="comments-container">
&#10;</div>
<div id="comment-tools-30749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30749-form-container" class="comment-form-container">
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

<span id="30751"></span>

<div id="answer-container-30751" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30751-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure exactly what you mean by "reference points" here, so taking a step back:</p>
<p>Admin boundaries in OSM are typically relations, and are tagged with an admin level. Here's one for <a href="http://www.openstreetmap.org/relation/189890">Leicestershire</a> in England, for example. You can see there that it's composed of lots of ways, with a role of "outer" (bordering neighbouring counties) or "inner" (defining a "hole" in the middle where Leicester is). Each of those <a href="http://www.openstreetmap.org/way/213211964">ways</a> has <a href="http://www.openstreetmap.org/node/1651493833">nodes</a>, and those nodes, and those nodes have a latitude and longitude.</p>
<p>Although it would be perfectly possible to obtain a set of node IDs and lat/longs for all nodes that are part of admin boundary relations, it wouldn't be useful - you'd have nodes for both outer and inner ways for all sorts of admin levels. What you probably want to do first is to look for nodes and their role in a particular administrative boundary - with Leicestershire you'd probably want to process the nodes in the "outers" and the nodes in the "inners" separately. Things get more complicated when there are more complicated enclaves and exclaves, obviously.</p>
<p>The next question is how to extract the data. One option is to start with the full details about the relation - <a href="https://help.openstreetmap.org/questions/17365/overpass-is-it-possible-to-use-it-as-an-alternative-to-the-api-relation-full-call">Overpass</a> is probably the best way to do this. That will return all constituent ways and their constituent nodes, but it'll return all nodes for outers and inners, so you'll need to find some way of separating those. More useful might be an Overpass query for "all outer ways" or even "all nodes in all outer ways" - there are lots of examples on the <a href="http://wiki.osm.org/wiki/Overpass_API">wiki page</a>, and the chances are that you can adapt one of those to your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '14, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-30751" class="comments-container">
<span id="30752"></span>
<div id="comment-30752" class="comment">
<div id="post-30752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for that <span></span><span>@SomeoneElse</span> really useful information. Sorry if I wasn't very clear, to give you an example. Leicestershire is enclosed with a tag boundary=administrative. All I am looking for is the lat, long info of all boundry=administrative nodes. I am trying to use the XAPI API <a href="http://open.mapquestapi.com/xapi/">http://open.mapquestapi.com/xapi/</a> but that only gives me the reference number for the nodes and filters out the actual latitude, longitude information.</p>
<p>Can you advice on this please. Thank you very much.</p>
</div>
<div id="comment-30752-info" class="comment-info">
<span class="comment-age">(15 Feb '14, 11:04)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
<span id="30754"></span>
<div id="comment-30754" class="comment">
<div id="post-30754-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The server that you're using isn't "the XAPI server"; merely one of several options (OSM can be particularly confusing sometimes).<br />
</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI wiki page</a> suggests that even if running, the data returned by the Mapquest XAPI server would be from 2012, so I wouldn't recommend using it. I've also noticed it being down occasionally; I'm not sure how common that is. Overpass's <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer">XAPI compatibility layer</a> returns most of the same data, and sounds like a much better bet for what you want.</p>
<p>However, what query are you using? If you're trying to extract every node out of every admin boundary on the planet it's not feasible to use XAPI for that; you'd want to extract from a downloaded dataset. Actually, depending on what you actually want to use the data for and what data you want, there may well be downloadable shapefiles available somewhere already</p>
</div>
<div id="comment-30754-info" class="comment-info">
<span class="comment-age">(15 Feb '14, 11:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30755"></span>
<div id="comment-30755" class="comment">
<div id="post-30755-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> you are a gem thank you very much for that. Helped me a lot!!!</p>
</div>
<div id="comment-30755-info" class="comment-info">
<span class="comment-age">(15 Feb '14, 12:07)</span> <span class="comment-user userinfo">RichaB</span>
</div>
</div>
</div>
<div id="comment-tools-30751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30751-form-container" class="comment-form-container">
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

