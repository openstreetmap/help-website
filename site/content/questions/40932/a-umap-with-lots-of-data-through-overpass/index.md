+++
type = "question"
title = "a umap with lots of data through overpass"
description = '''I&#x27;m trying to make a umap to show the most important paved roads in South America (or globally). It works, through a connected Overpass query. But the problem is, this is a lot to ask the poor Overpass server. Which means that a) the user thinks nothing is happening, b) that you can only reasonably ...'''
date = "2015-02-10T14:50:00Z"
lastmod = "2015-02-22T00:32:00Z"
weight = 40932
keywords = [ "umap", "overpass-turbo", "overpass" ]
aliases = [ "/questions/40932" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [a umap with lots of data through overpass](/questions/40932/a-umap-with-lots-of-data-through-overpass)

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
<span id="post-40932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40932-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://umap.openstreetmap.fr/en/map/untitled-map_27663#11/-16.4884/-68.1001">I'm trying to make a umap to show the most important paved roads in South America</a> (or globally). It works, through a connected <a href="http://overpass-turbo.eu/s/7AU">Overpass query</a>. But the problem is, this is a lot to ask the poor Overpass server. Which means that a) the user thinks nothing is happening, b) that you can only reasonably query the data once you zoomed in close enough. That defeats the purpose, as the map is meant to give you an overview of how you could plan a transcontinental trip.</p>
<p>A possible solution would be to just run the query a few times on my own computer, then upload the data to umap. This again defeats the purpose: the idea of the map is also to get people to map more surface info in OSM, so the quicker the update the better.</p>
<p>Is there a way to query the data for the whole continent when the Overpass server is having a chilled out time, then having the data cached for umap for a couple of days until the next chance to query the data again?</p>
<p>A different approach might be to tell overpass to just query a very low 'resolution' version of the needed ways, to soften up the server load.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '15, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-40932" class="comments-container">
&#10;</div>
<div id="comment-tools-40932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40932-form-container" class="comment-form-container">
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

<span id="41208"></span>

<div id="answer-container-41208" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41208-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding a low resolution version of the overpass response, there's already a GitHub issue out there for this topic: <a href="https://github.com/drolbr/Overpass-API/issues/171">https://github.com/drolbr/Overpass-API/issues/171</a> If you like, you can add further details/requirements in that ticket.</p>
<p>For uMap, there also seems to be some kind of caching request: <a href="https://bitbucket.org/yohanboniface/umap/issue/160/update-periodicity-with-remote-data">https://bitbucket.org/yohanboniface/umap/issue/160/update-periodicity-with-remote-data</a></p>
<p>BTW: To get developer's attention on your ideas and requirements, I would always recommend to check the relevant bug trackers and file a new issue if needed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '15, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '15, 16:18</strong> </span></p>
</div>
</div>
<div id="comments-container-41208" class="comments-container">
<span id="41222"></span>
<div id="comment-41222" class="comment">
<div id="post-41222-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
<p>Before posting a feature request, I prefer to check if the problem isn't me. Which it often is.</p>
</div>
<div id="comment-41222-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 00:32)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-41208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41208-form-container" class="comment-form-container">
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

