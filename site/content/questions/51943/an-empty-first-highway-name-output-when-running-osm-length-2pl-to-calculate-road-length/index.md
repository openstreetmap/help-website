+++
type = "question"
title = "An empty first highway name output when running osm-length-2.pl to calculate road length"
description = '''Hello, I am using osm-length-2.pl script to summarize road length of a country. The script is working well except it outputs the first type of highway with an empty name: highway length sums (metres):  38856413m track 7762817m secondary 1941725m residential 1747145m service 1315326m path 1080010m pr...'''
date = "2016-09-08T04:34:00Z"
lastmod = "2016-09-09T14:25:00Z"
weight = 51943
keywords = [ "highway_name", "osm-length" ]
aliases = [ "/questions/51943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [An empty first highway name output when running osm-length-2.pl to calculate road length](/questions/51943/an-empty-first-highway-name-output-when-running-osm-length-2pl-to-calculate-road-length)

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
<span id="post-51943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51943-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am using osm-length-2.pl script to summarize road length of a country. The script is working well except it outputs the first type of highway with an empty name:</p>
<p>highway length sums (metres):</p>
<pre><code>                  38856413m
track              7762817m
secondary          1941725m
residential        1747145m
service            1315326m
path               1080010m
primary             927921m
footway             881391m
...
TOTAL             56823848m</code></pre>
<p>Does anyone have this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highway_name" rel="tag" title="see questions tagged &#39;highway_name&#39;">highway_name</span> <span class="post-tag tag-link-osm-length" rel="tag" title="see questions tagged &#39;osm-length&#39;">osm-length</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '16, 04:34</strong></p>
<img src="https://secure.gravatar.com/avatar/91e7b688c24bfa1a86b1b30c66098fa8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trungnk&#39;s gravatar image" />
<p><span>trungnk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trungnk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '16, 04:45</strong> </span></p>
</div>
</div>
<div id="comments-container-51943" class="comments-container">
&#10;</div>
<div id="comment-tools-51943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51943-form-container" class="comment-form-container">
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

<span id="51944"></span>

<div id="answer-container-51944" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51944-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The script sums up the lengths of all ways, not only highways, and the first number is the length of all non-highway ways. I have modified the script in SVN to stop doing that, so if you check out a new version the first line will be gone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '16, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51944" class="comments-container">
<span id="51950"></span>
<div id="comment-51950" class="comment">
<div id="post-51950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik. I can see the filters are updated. From osm highway definition almost covers all the type of road. Do the non-highways ways you mentioned are relations?</p>
</div>
<div id="comment-51950-info" class="comment-info">
<span class="comment-age">(09 Sep '16, 00:53)</span> <span class="comment-user userinfo">trungnk</span>
</div>
</div>
<span id="51951"></span>
<div id="comment-51951" class="comment">
<div id="post-51951-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ways and relations are different things, see <a href="https://wiki.openstreetmap.org/wiki/Elements">elements</a>. Non-highway ways can be buildings, landuses, water bodies, forests, parks, railways, walls and fences, ways for administrative boundaries and so on.</p>
</div>
<div id="comment-51951-info" class="comment-info">
<span class="comment-age">(09 Sep '16, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51965"></span>
<div id="comment-51965" class="comment">
<div id="post-51965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the non-highway ways are not ways. They take a significant amount of length when the script calculates length of roads. Thus when comparing to the statistic data obtainted we see there are a half kilometres amout deducted after removing non-highways "things"</p>
</div>
<div id="comment-51965-info" class="comment-info">
<span class="comment-age">(09 Sep '16, 13:55)</span> <span class="comment-user userinfo">trungnk</span>
</div>
</div>
<span id="51966"></span>
<div id="comment-51966" class="comment">
<div id="post-51966-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They are ways, <a href="https://wiki.openstreetmap.org/wiki/Way">OSM ways</a> :)</p>
</div>
<div id="comment-51966-info" class="comment-info">
<span class="comment-age">(09 Sep '16, 14:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51944-form-container" class="comment-form-container">
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

