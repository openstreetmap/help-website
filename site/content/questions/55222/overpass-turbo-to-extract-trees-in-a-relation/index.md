+++
type = "question"
title = "Overpass Turbo to extract trees in a relation"
description = '''I am trying to extract all &quot;natural=tree in Bergenhus&quot;, but there are two relation called Bergenhus nested inside each other (this is how it is suposed to be). The question is how I can get data from within this multipolygon https://www.openstreetmap.org/relation/114938 and not this multipolygon htt...'''
date = "2017-03-21T21:31:00Z"
lastmod = "2017-09-23T18:27:00Z"
weight = 55222
keywords = [ "overpass-turbo", "trees" ]
aliases = [ "/questions/55222" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo to extract trees in a relation](/questions/55222/overpass-turbo-to-extract-trees-in-a-relation)

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
<span id="post-55222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55222-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extract all "natural=tree in Bergenhus", but there are two relation called Bergenhus nested inside each other (this is how it is suposed to be). The question is how I can get data from within this multipolygon <a href="https://www.openstreetmap.org/relation/114938">https://www.openstreetmap.org/relation/114938</a> and not this multipolygon <a href="https://www.openstreetmap.org/relation/6492161">https://www.openstreetmap.org/relation/6492161</a> with overpass turbo.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-trees" rel="tag" title="see questions tagged &#39;trees&#39;">trees</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '17, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '17, 22:00</strong> </span></p>
</div>
</div>
<div id="comments-container-55222" class="comments-container">
&#10;</div>
<div id="comment-tools-55222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55222-form-container" class="comment-form-container">
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

<span id="55231"></span>

<div id="answer-container-55231" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55231-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FredrikLindseth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simplest thing is probably to set the search area directly to the relation like <code>area(3600114938)-&gt;.searchArea;</code>.</p>
<p>Working example here: <a href="http://overpass-turbo.eu/s/nGY">http://overpass-turbo.eu/s/nGY</a></p>
<p>There's <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">some information in the Overpass documentation about how OSM ids are mapped to Overpass area ids</a>.</p>
<p>Overpass Turbo uses <a href="http://nominatim.openstreetmap.org/">the public nominatim service</a> to fill in queries like <code>in Bergenhus</code>, so another possibility would be to craft a search there that returned the correct place as the first result. This might be the way to go if you have other similar nested areas to deal with, though I didn't find such a phrase with a few simple tries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '17, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55231" class="comments-container">
<span id="59802"></span>
<div id="comment-59802" class="comment">
<div id="post-59802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A comment for future viewers: find the ID of the relation (114938 in this case) and add 3600000000 to get to the overpass area ID of 3600114938</p>
</div>
<div id="comment-59802-info" class="comment-info">
<span class="comment-age">(23 Sep '17, 18:27)</span> <span class="comment-user userinfo">FredrikLindseth</span>
</div>
</div>
</div>
<div id="comment-tools-55231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55231-form-container" class="comment-form-container">
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

