+++
type = "question"
title = "Resource to Learn How to Upload Shapefile"
description = '''Hello,  What&#x27;s the best resource to learn how to upload a shapefile into OSM? For context, I work with Parks and Recreation departments and use OSM to validate their community boundaries. I have access to shapefiles or web service URL&#x27;s, but that information is not always up to date in OSM. I&#x27;ve rea...'''
date = "2020-05-20T22:06:00Z"
lastmod = "2020-05-21T10:17:00Z"
weight = 74936
keywords = [ "shapefile", "import" ]
aliases = [ "/questions/74936" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Resource to Learn How to Upload Shapefile](/questions/74936/resource-to-learn-how-to-upload-shapefile)

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
<span id="post-74936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>What's the best resource to learn how to upload a shapefile into OSM?</p>
<p>For context, I work with Parks and Recreation departments and use OSM to validate their community boundaries. I have access to shapefiles or web service URL's, but that information is not always up to date in OSM.</p>
<p>I've read other threads and know that imports are done with JOSM and that the shapefile can be open in JOSM using opendata. However, after reading import guidelines I understand that there is probably some manipulation that needs to be done to the file prior to any kind of upload happening. Where can I learn what to look for/change?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '20, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/23ffd17d06fd5448a36a0902a8649652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guerinjamie&#39;s gravatar image" />
<p><span>guerinjamie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guerinjamie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74936" class="comments-container">
&#10;</div>
<div id="comment-tools-74936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74936-form-container" class="comment-form-container">
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

<span id="74940"></span>

<div id="answer-container-74940" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74940-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Only a small part of data imports is about the purely technical side (the most important technical issue for working with boundaries probably are that you need to split touching polygons into their constituting linework, load the individual lines into OSM and then reconstruct the polygons from these lines in OSM with multipolygon relations - so that any line separating one boundary from another is only in OSM once, and not twice).</p>
<p>More importantly, you need to take into account the data that is already there in OSM; only very rarely would it be acceptable to simply delete something from OSM and replace it with an "up to date" version - you would be expected to modify the existing object to bring it up to date instead. Also, you will want to check the data that you upload against unrelated data that OSM already has in the same location - eg if you upload a park boundary and there is already a residential area in OSM that kind-of ends where your park begins but not quite, then it is very likely that in reality the residential area ends exactly where the park begins, and not 10ft in, and so on.</p>
<p>It is also tremendously helpful for a would-be data importer to gather a minimum amount of non-import OSM mapping experience before they attempt an import since this strengthens the understanding of how things work in OSM. Park boundaries in the US are among the most complex and error-prone kinds of data we have in OSM, and more than once a haphazard import of broken boundaries in the US has had negative effects on OSM data consumers everywhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '20, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-74940" class="comments-container">
&#10;</div>
<div id="comment-tools-74940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74940-form-container" class="comment-form-container">
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

