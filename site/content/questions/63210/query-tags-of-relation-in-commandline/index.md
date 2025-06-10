+++
type = "question"
title = "Query tags of relation (in commandline)"
description = '''I&#x27;ve got a list of relations of power plants and would like to query the &quot;plant:output:electricity&quot; tag. Is there any generic tool (for Linux commandline) which queries the content of an arbitrary tag from Overpass? So e.g. I would like to do: ./querytool -relation 368946 -tag &quot;plant:output:electric...'''
date = "2018-04-29T11:34:00Z"
lastmod = "2018-05-01T15:35:00Z"
weight = 63210
keywords = [ "overpass" ]
aliases = [ "/questions/63210" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query tags of relation (in commandline)](/questions/63210/query-tags-of-relation-in-commandline)

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
<span id="post-63210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63210-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a list of relations of power plants and would like to query the "plant:output:electricity" tag.</p>
<p>Is there any generic tool (for Linux commandline) which queries the content of an arbitrary tag from Overpass?</p>
<p>So e.g. I would like to do:</p>
<p>./querytool -relation 368946 -tag "plant:output:electricity"</p>
<p>and get out "150 MW".</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '18, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/8e0867aa963fc989a200f2f35144d3c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="landuse&#39;s gravatar image" />
<p><span>landuse</span><br />
<span class="score" title="116 reputation points">116</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="landuse has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63210" class="comments-container">
<span id="63257"></span>
<div id="comment-63257" class="comment">
<div id="post-63257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why are you not answering?</p>
</div>
<div id="comment-63257-info" class="comment-info">
<span class="comment-age">(01 May '18, 11:43)</span> <span class="comment-user userinfo">landuse</span>
</div>
</div>
<span id="63258"></span>
<div id="comment-63258" class="comment">
<div id="post-63258-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I’m still trying to find an answer for you.</p>
</div>
<div id="comment-63258-info" class="comment-info">
<span class="comment-age">(01 May '18, 12:00)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="63260"></span>
<div id="comment-63260" class="comment">
<div id="post-63260-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14837/landuse">@landuse</a> please be polite. All answers are provided by volunteers in their free time and you have no "right" to an answer in any form.</p>
</div>
<div id="comment-63260-info" class="comment-info">
<span class="comment-age">(01 May '18, 15:35)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63210-form-container" class="comment-form-container">
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

<span id="63259"></span>

<div id="answer-container-63259" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63259-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not a ready made tool, but you can pipe curl into something like jq:</p>
<pre><code>curl -s -g http://overpass-api.de/api/interpreter --data-urlencode &#39;data=[out:json];rel(368946);out;&#39; | jq &#39;.elements[0].tags.&quot;plant:output:electricity&quot;&#39;</code></pre>
<p>I guess that won't work well if you want a lot of flexibility, but for simple queries it should be fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '18, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63259" class="comments-container">
&#10;</div>
<div id="comment-tools-63259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63259-form-container" class="comment-form-container">
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

