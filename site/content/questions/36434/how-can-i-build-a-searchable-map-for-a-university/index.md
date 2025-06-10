+++
type = "question"
title = "How can I build a searchable map for a University?"
description = '''I am disappointed by the quality of the map on my University&#x27;s website. I was wondering if there was a way to develop a fairly simple searchable and scalable map for a non-developper like me? I can get into understanding a few lines of code if I am guided and the documentation is accessible. I also ...'''
date = "2014-08-31T01:54:00Z"
lastmod = "2014-08-31T13:07:00Z"
weight = 36434
keywords = [ "rendering", "university", "search", "build", "map" ]
aliases = [ "/questions/36434" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I build a searchable map for a University?](/questions/36434/how-can-i-build-a-searchable-map-for-a-university)

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
<span id="post-36434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36434-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am disappointed by the quality of the map on my University's website. I was wondering if there was a way to develop a fairly simple searchable and scalable map for a non-developper like me? I can get into understanding a few lines of code if I am guided and the documentation is accessible. I also understand GitHub.</p>
<p>What I want to achieve is to let people search for a building number (ref=) or building name (name=) or alternative name (alt_name=), in a limited area, possibly with a rendering that highlights the university's buildings (using the corresponding relationship for example?).</p>
<p>It's a pretty big question but I hoped that there might be a project out there that could get me fairly close to that without too much hassle! Even just a few pointers would be great!</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '14, 01:54</strong></p>
<img src="https://secure.gravatar.com/avatar/19c111f5c672fdb25353073c835f6a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephane-guillou&#39;s gravatar image" />
<p><span>stephane-gui...</span><br />
<span class="score" title="585 reputation points">585</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephane-guillou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36434" class="comments-container">
&#10;</div>
<div id="comment-tools-36434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36434-form-container" class="comment-form-container">
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

<span id="36451"></span>

<div id="answer-container-36451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36451-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect the simplest way to procede is to</p>
<ul>
<li>add the data to OSM (the standard nominatim search should find name and alt_name)</li>
<li>make a prototype with umap.openstreetmap.fr or any other umap instance</li>
</ul>
<p>The umap search box queries a nominatim instance (not the central one, but that is likely only an issue wrt updates), the important thing is that it prioritizes results from the currently viewed map segment. With other words you should be able to get reasonable results without specifying full addresses.</p>
<p>You could then simply query the overpass api for the campus building outlines and add that as an additional layer.</p>
<p>Naturally you could got the full custom route (custom map rendering etc.) but I suspect starting small may be a better strategy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '14, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '14, 23:03</strong> </span></p>
</div>
</div>
<div id="comments-container-36451" class="comments-container">
&#10;</div>
<div id="comment-tools-36451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36451-form-container" class="comment-form-container">
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

