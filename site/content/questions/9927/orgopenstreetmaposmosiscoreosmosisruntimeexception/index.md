+++
type = "question"
title = "org.openstreetmap.osmosis.core.OsmosisRuntimeException"
description = '''When I try to download osm data with the api using this link: http://jxapi.openstreetmap.org/xapi/api/0.6/map?bbox=-73.60100000000001,45.399,-73.559,45.440999999999995 I got an org.openstreetmap.osmosis.core.OsmosisRuntimeException? Someone could help me!? Thanks'''
date = "2012-01-12T18:53:00Z"
lastmod = "2012-01-12T19:15:00Z"
weight = 9927
keywords = [ "api", "xapi", "bug" ]
aliases = [ "/questions/9927" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [org.openstreetmap.osmosis.core.OsmosisRuntimeException](/questions/9927/orgopenstreetmaposmosiscoreosmosisruntimeexception)

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
<span id="post-9927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to download osm data with the api using this link:</p>
<p><a href="http://jxapi.openstreetmap.org/xapi/api/0.6/map?bbox=-73.60100000000001,45.399,-73.559,45.440999999999995">http://jxapi.openstreetmap.org/xapi/api/0.6/map?bbox=-73.60100000000001,45.399,-73.559,45.440999999999995</a></p>
<p>I got an org.openstreetmap.osmosis.core.OsmosisRuntimeException?</p>
<p>Someone could help me!?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '12, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5d557676b5fb871805d81da03442cdc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maxime&#39;s gravatar image" />
<p><span>Maxime</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maxime has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9927" class="comments-container">
&#10;</div>
<div id="comment-tools-9927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9927-form-container" class="comment-form-container">
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

<span id="9928"></span>

<div id="answer-container-9928" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9928-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Maxime has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few issues with that request. The first is that You need some square brackets around the bbox, the second is that you've got a spurious "map" in there and the third is that I don't think that <a href="http://jxapi.openstreetmap.org"></a><a href="http://jxapi.openstreetmap.org">jxapi.openstreetmap.org</a> has woken up from hibernation yet. If you try instead:</p>
<p><a href="http://open.mapquestapi.com/xapi/api/0.6/*%5Bbbox=-73.60100000000001,45.399,-73.559,45.440999999999995%5D">http://open.mapquestapi.com/xapi/api/0.6/*[bbox=-73.60100000000001,45.399,-73.559,45.440999999999995]</a></p>
<p>it should work.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '12, 19:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '12, 19:16</strong> </span></p>
</div>
</div>
<div id="comments-container-9928" class="comments-container">
&#10;</div>
<div id="comment-tools-9928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9928-form-container" class="comment-form-container">
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

