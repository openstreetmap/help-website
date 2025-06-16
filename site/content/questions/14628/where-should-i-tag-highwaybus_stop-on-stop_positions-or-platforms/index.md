+++
type = "question"
title = "Where should I tag highway=bus_stop, on stop_positions or platforms?"
description = '''I wonder why some wiki pages suggest to add the tag highway=bus_stop to the stop_postion rather than to the platform nodes. To me it would make more sense to add this tag to the platform, since renders (or styles) that don&#x27;t support the new schema (such as the standard map displayed on osm.org, unfo...'''
date = "2012-07-26T20:18:00Z"
lastmod = "2014-12-19T09:35:00Z"
weight = 14628
keywords = [ "busstops", "public-transport", "bestpractice", "schema" ]
aliases = [ "/questions/14628" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Where should I tag highway=bus_stop, on stop_positions or platforms?](/questions/14628/where-should-i-tag-highwaybus_stop-on-stop_positions-or-platforms)

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
<span id="post-14628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14628-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-14628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wonder why some wiki pages suggest to add the tag <code>highway=bus_stop</code> to the <code>stop_postion</code> rather than to the <code>platform</code> nodes.</p>
<p>To me it would make more sense to add this tag to the platform, since renders (or styles) that don't support the new schema (such as the standard map displayed on osm.org, unfortunately) would display the platforms (which is more useful to people looking at the map, because only then it is visible which bus stop is on which side of the street) and renderers that do support the new schema could ignore that tag anyway.</p>
<p>Furthermore, if I ignore how the nodes are actually rendered ("Don't tag for the renderer") tagging the platform as <code>highway=bus_stop</code> still makes more sense to me, since what I (and I assume most other people) usually think of as a "bus stop" is the place beside the street where you wait for a bus, not the position on the street where it actually stops.</p>
<p>The only reason (that I could find) for putting the <code>highway=bus_stop</code> tag on the <code>stop_position</code> is that this simplifies routing (Source: <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop#Common_Usage_.28node_positioning.29">Tag:<code>highway=bus_stop</code></a>). However, this isn't a valid reason with the new schema, since for routing the stop_position tag can and should be used, not <code>highway=bus_stop</code>.</p>
<p>If someone knows a good reason why <code>highway=bus_stop</code> should be added to the nodes on the street I would be curious to hear it. Otherwise I think I'll just tag bus stops according to the <a href="https://wiki.openstreetmap.org/wiki/Public_Transport">public transport schema</a> and additionally add the <code>highway=bus_stop</code> tag to the platform.</p>
<hr />
<p>EDIT: The sections in the wiki I refer to are <a href="https://wiki.openstreetmap.org/wiki/Tag:highway=bus_stop#Stopping_Point">Tag:<code>highway=bus_stop#Stopping_Point</code></a> where it is described as "mandatory" to add <code>highway=bus_stop</code> to the node on the street and <a href="https://wiki.openstreetmap.org/wiki/Buses#Stops_and_Bus_Stations">Buses</a> which states that "For compatibility actually the tag <code>highway=bus_stop</code> is tagged together with <code>public_transport=stop_position</code> on the way."</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '12, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0d934186471fb2cc3e9b9447d3aa25bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhf&#39;s gravatar image" />
<p><span>dhf</span><br />
<span class="score" title="106 reputation points">106</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '12, 17:41</strong> </span></p>
</div>
</div>
<div id="comments-container-14628" class="comments-container">
<span id="14671"></span>
<div id="comment-14671" class="comment">
<div id="post-14671-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you for the links. I have corrected the misleading content of the wiki pages.</p>
</div>
<div id="comment-14671-info" class="comment-info">
<span class="comment-age">(27 Jul '12, 21:29)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-14628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14628-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="14644"></span>

<div id="answer-container-14644" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14644-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-14644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dhf has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just go ahead and tag the platform highway=bus_stop and additionally public_transport=platform.</p>
<p>The wiki has a conceptual pitfall. It often sounds normative, but it isn't, simply because it can be changed all the time. A look on the <a href="http://taginfo.openstreetmap.org/tags">taginfo</a> makes clear that tagging highway=bus_stop by far outweights any of the more complicated tagging schemes.</p>
<p>Moreover, there is common sense that the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport">2010 proposal</a> covers the broadest possible consent. It says in particular "The proposed tags can and do coexist with the well known tags. The usage of the new tags is recommended but not mandatory.". It then explains that the node beside the street should be tagged highway=bus_stop. The misinterpretation of putting highway=bus_stop on the node did happen so often in the past that it got its own interpretation and was the main driving force to invent a new, distictly different set of tags, tagging both.</p>
<p>If there are any wiki pages suggeesting to tag highway=bus_stop, in particular on the street, I would be happy for a hint such that they can be corrected to be in line to the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Public_Transport">2010 proposal</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '12, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '12, 11:13</strong> </span></p>
</div>
</div>
<div id="comments-container-14644" class="comments-container">
<span id="14663"></span>
<div id="comment-14663" class="comment">
<div id="post-14663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. I added links to the two pages I refered to at the end of the question. I'd be glad if you could correct them so that they don't contradict the approved proposal anymore.</p>
</div>
<div id="comment-14663-info" class="comment-info">
<span class="comment-age">(27 Jul '12, 17:50)</span> <span class="comment-user userinfo">dhf</span>
</div>
</div>
</div>
<div id="comment-tools-14644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14644-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14634"></span>

<div id="answer-container-14634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14634-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an often discussed item, not helped by the various public transport proposals, and the translation from language to language and back again. The <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop#Common_Usage_.28node_positioning.29">Common Usage</a> on the page you mention above, is what you are proposing to do and what has always been most common practice in the UK (even before the bus stops were imported in several areas as nodes either side of the way). I don't think I've ever knowingly encountered a highway=platform node.</p>
<p>And as you point out, anything which uses the new public_transport=* tagging shouldn't need to look at the highway=tags, so there is no problem with having highway=bus_stop and public_transport=platform on the same node, which combines the common current usage with the new tagging scheme.</p>
<p>Note though that a few European cities <strong>have</strong> adopted the old highway=platform to the side of the way, highway=bus_stop in the way tagging scheme and if you are tagging in one of those areas there is a chance local mappers might retag what you add to bring it in line with what happens in that area. I'd perhaps ignore such changes if they happen, as life is too short to worry...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '12, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-14634" class="comments-container">
&#10;</div>
<div id="comment-tools-14634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39713"></span>

<div id="answer-container-39713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of course highway=bus_stop outweighs anything else, as that's the only tag that will get rendered. Chicken and egg.</p>
<p>If I see a public_transport=stop_position with highway=bus_stop on it, I remove the highway=bus_stop/name/ref/etc tags. This is the node that's part of the way. Add bus=yes/tram=yes, as needed. Omit anything else.</p>
<p>If there are no nodes either side of the road yet, I'll add them and double tag them with highway=bus_stop (to get them rendered, to hell with statistics) and public_transport=platform/bus=yes. name/ref/route_ref/operator/network/zone are put on these nodes. Recently I converted this to ref:operator/route_ref:operator/zone:operator, since there will be overlap of operators in any region near the borders.</p>
<p>Polyglot</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a7dfce5853b949d2c4d04076890b4899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Polyglot&#39;s gravatar image" />
<p><span>Polyglot</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Polyglot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39713" class="comments-container">
&#10;</div>
<div id="comment-tools-39713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39713-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

