+++
type = "question"
title = "What is the oldest object on OSM?"
description = '''I try to maintain the history of objects when editing, for example putting consideration which half of a way gets the history when splitting it. This led me to wonder what is the oldest object on OSM, and what are the oldest basic types of objects (node, way, relation). Does anyone with more skills ...'''
date = "2017-11-26T02:26:00Z"
lastmod = "2017-11-26T11:49:00Z"
weight = 60790
keywords = [ "curiosity", "history" ]
aliases = [ "/questions/60790" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the oldest object on OSM?](/questions/60790/what-is-the-oldest-object-on-osm)

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
<span id="post-60790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60790-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to maintain the history of objects when editing, for example putting consideration which half of a way gets the history when splitting it.</p>
<p>This led me to wonder what is the oldest object on OSM, and what are the oldest basic types of objects (node, way, relation). Does anyone with more skills than me know how to figure this out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-curiosity" rel="tag" title="see questions tagged &#39;curiosity&#39;">curiosity</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '17, 02:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-60790" class="comments-container">
&#10;</div>
<div id="comment-tools-60790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60790-form-container" class="comment-form-container">
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

<span id="60803"></span>

<div id="answer-container-60803" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60803-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-60803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ways and Relations are more difficult than nodes because they've undergone changes in their data model, respectively been invented, sometime along the road. Nodes are the oldest data type that survives (largely) unchanged but even there the ancient history can be murky.</p>
<p>In theory it would be as easy as looking at the objects with the lowest numerical IDs. However, not only have many mappers playfully repurposed those prestigious IDs during the life of the project (just study the <a href="https://www.openstreetmap.org/node/1/history">history of node #1</a>), but also (due to the aforementioned murkiness) the smallest ID doesn't necessarily mean the oldest age. The license change also additionally complicates such research as some old edits may be beyond reach today.</p>
<p>The oldest currently-recorded edit is <a href="https://www.openstreetmap.org/node/5/history">version 1 of node #5</a> created in April 2005 by Steve Coast, the founder of OpenStreetMap. The oldest edit where tags were used on a node was <a href="https://www.openstreetmap.org/node/262695/history">Marley Common</a> in November 2005 by Nick Whitelegg, and this oldest tagged node has indeed survived - minus small changes to the tagging scheme - until today.</p>
<p>If you want to do further research, grab a "full history" PBF and run it through the osmium command line tool like so:</p>
<pre><code>osmium cat history-latest.osh.pbf -f opl -o history.opl</code></pre>
<p>The resulting "OPL" text file can easily be processed with text-based utilities, e.g. to find all edits in 2005 and sort them,</p>
<pre><code>grep &quot; t2005&quot; history.opl | sort -k5 | less</code></pre>
<p>As I said initially, the concept of ways as we know them didn't exist back in 2005; we had "segments" for a while and they could be grouped into "ways", but none of that will be reflected in today's history files. You would have to get hold of a very old planet.osm.bz2 file to dive into that part of history.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '17, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60803" class="comments-container">
<span id="60804"></span>
<div id="comment-60804" class="comment">
<div id="post-60804-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Which backs up the oral history that the first nodes in OSM were added in Regent's Park, London, by Steve.</p>
</div>
<div id="comment-60804-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 11:49)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60803" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60803-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60802"></span>

<div id="answer-container-60802" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60802-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-60802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well Steve Coast started the project see <a href="https://wiki.openstreetmap.org/wiki/User:Steve">https://wiki.openstreetmap.org/wiki/User:Steve</a> I haven't been able to find his edits. The editing and recording system must have evolved a lot since (2004?). But the link above does have a contact for him so you could ask him, but he is probably quite a busy guy. If you do contact him and get the answer please let us know.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '17, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Nov '17, 09:59</strong> </span></p>
</div>
</div>
<div id="comments-container-60802" class="comments-container">
&#10;</div>
<div id="comment-tools-60802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60802-form-container" class="comment-form-container">
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

