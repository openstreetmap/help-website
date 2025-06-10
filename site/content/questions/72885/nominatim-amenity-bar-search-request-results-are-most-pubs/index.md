+++
type = "question"
title = "Nominatim amenity bar search request results are most pubs"
description = '''I wanted to search for bars in a viewbox, but most of them are pubs. This is my search request: https://nominatim.openstreetmap.org/search?q=[bar]&amp;amp;format=json&amp;amp;bounded=true&amp;amp;viewbox=6.408,51.197,6.474,51.231&amp;amp;limit=50'''
date = "2020-02-06T08:35:00Z"
lastmod = "2020-02-06T12:03:00Z"
weight = 72885
keywords = [ "amenity", "nominatim", "search" ]
aliases = [ "/questions/72885" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim amenity bar search request results are most pubs](/questions/72885/nominatim-amenity-bar-search-request-results-are-most-pubs)

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
<span id="post-72885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wanted to search for bars in a viewbox, but most of them are pubs. This is my search request: <a href="https://nominatim.openstreetmap.org/search?q=%5Bbar%5D&amp;format=json&amp;bounded=true&amp;viewbox=6.408,51.197,6.474,51.231&amp;limit=50">https://nominatim.openstreetmap.org/search?q=[bar]&amp;format=json&amp;bounded=true&amp;viewbox=6.408,51.197,6.474,51.231&amp;limit=50</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '20, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/dcc21a76b6706730dfab7d3a68272f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arthurle&#39;s gravatar image" />
<p><span>Arthurle</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arthurle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72885" class="comments-container">
&#10;</div>
<div id="comment-tools-72885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72885-form-container" class="comment-form-container">
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

<span id="72888"></span>

<div id="answer-container-72888" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arthurle has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The syntax is <a href="https://nominatim.openstreetmap.org/search?q=%5Bamenity=bar%5D&amp;format=json&amp;bounded=true&amp;viewbox=6.408,51.197,6.474,51.231&amp;limit=50">https://nominatim.openstreetmap.org/search?q=[amenity=bar]&amp;format=json&amp;bounded=true&amp;viewbox=6.408,51.197,6.474,51.231&amp;limit=50</a> and it works only for a selection of tags, see <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases</a></p>
<p>I agree with SomeoneElse though, Overpass API is the best tool for bounded/nearby POI searches.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '20, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-72888" class="comments-container">
&#10;</div>
<div id="comment-tools-72888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72888-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72886"></span>

<div id="answer-container-72886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to search for something that is explicitly tagged as amenity=bar, I'd suggest using Overpass for that. There's plenty of information on the <a href="https://wiki.openstreetmap.org/wiki/Overpass">wiki</a>, but a quick way to find what it will return for a particular area is to click through to it from <a href="https://taginfo.openstreetmap.org/tags/amenity=bar">taginfo</a>. In this case the query looks similar to <a href="https://overpass-turbo.eu/s/QsG">this</a>, depending on your search area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '20, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72886" class="comments-container">
&#10;</div>
<div id="comment-tools-72886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72886-form-container" class="comment-form-container">
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

