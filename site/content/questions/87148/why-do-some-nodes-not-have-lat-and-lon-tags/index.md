+++
type = "question"
title = "Why do some nodes not have &#x27;lat&#x27; and &#x27;lon&#x27; tags?"
description = '''I&#x27;m trying to download data for a &quot;way&quot;, but the individual nodes only have a &#x27;ref&#x27; tag - not &#x27;lat&#x27; or &#x27;lon&#x27;. If I click on the individual node it will display the lat/lon data, but how do I download the entire &quot;way&quot; in such a manner that it includes this data and can be converted into gpx, kml, etc...'''
date = "2023-04-19T18:32:00Z"
lastmod = "2023-04-19T20:58:00Z"
weight = 87148
keywords = [ "ways", "latitude", "longitude" ]
aliases = [ "/questions/87148" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do some nodes not have 'lat' and 'lon' tags?](/questions/87148/why-do-some-nodes-not-have-lat-and-lon-tags)

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
<span id="post-87148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87148-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to download data for a "way", but the individual nodes only have a 'ref' tag - not 'lat' or 'lon'. If I click on the individual node it will display the lat/lon data, but how do I download the entire "way" in such a manner that it includes this data and can be converted into gpx, kml, etc? It really feels like there is something obvious I'm missing... Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '23, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1f610e467c994eb67dd3edfd276e4b3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgruss1234&#39;s gravatar image" />
<p><span>jgruss1234</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgruss1234 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87148" class="comments-container">
&#10;</div>
<div id="comment-tools-87148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87148-form-container" class="comment-form-container">
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

<span id="87149"></span>

<div id="answer-container-87149" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87149-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is normal. What you see in an XML way object is not nodes, but references to nodes; you will have to look them up to find the coordinates. If you use the "full" modifier on an API query, e.g. <a href="https://www.openstreetmap.org/api/0.6/way/123/full">https://www.openstreetmap.org/api/0.6/way/123/full</a> then the nodes are present in the response.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '23, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87149" class="comments-container">
&#10;</div>
<div id="comment-tools-87149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87149-form-container" class="comment-form-container">
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

