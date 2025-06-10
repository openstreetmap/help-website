+++
type = "question"
title = "Find all airports between 50 and 100 kms from a location"
description = '''Hi all, I&#x27;m trying to find all airports in radius between 50 and 100 kms from given position. My approach is:  Find all airports in radius 100 kms &quot;Subtract&quot; all airports in radius 50 kms from result in (1.)  Is this a good way? If not, please, advise me how to do it. If yes, how do I subtract two r...'''
date = "2018-01-03T13:52:00Z"
lastmod = "2018-01-04T01:18:00Z"
weight = 61461
keywords = [ "subset", "overpass-turbo", "around" ]
aliases = [ "/questions/61461" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Find all airports between 50 and 100 kms from a location](/questions/61461/find-all-airports-between-50-and-100-kms-from-a-location)

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
<span id="post-61461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61461-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm trying to find all airports in radius between 50 and 100 kms from given position. My approach is:</p>
<ol>
<li>Find all airports in radius 100 kms</li>
<li>"Subtract" all airports in radius 50 kms from result in (1.)</li>
</ol>
<p>Is this a good way? If not, please, advise me how to do it. If yes, how do I subtract two result sets?</p>
<p><a href="http://overpass-turbo.eu/s/ube" title="Here">Here</a> is my attempt for airports in 50 km radius from 49.0294417N, 17.4397194E.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-subset" rel="tag" title="see questions tagged &#39;subset&#39;">subset</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '18, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ae53a8e3ecdb49745cdc50692124f8e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="postak420&#39;s gravatar image" />
<p><span>postak420</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="postak420 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61461" class="comments-container">
&#10;</div>
<div id="comment-tools-61461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61461-form-container" class="comment-form-container">
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

<span id="61469"></span>

<div id="answer-container-61469" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61469-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="postak420 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an example of naming the result sets and finding the difference:</p>
<p><a href="http://overpass-turbo.eu/s/ucd">http://overpass-turbo.eu/s/ucd</a></p>
<pre><code>[out:json];
(node[&quot;aeroway&quot;=&quot;aerodrome&quot;](around:50000,49.0294417,17.4397194);
)-&gt;.fifty;
(node[&quot;aeroway&quot;=&quot;aerodrome&quot;](around:100000,49.0294417,17.4397194);
)-&gt;.hundred;
(.hundred - .fifty);
out;</code></pre>
<p>I think the approach is fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '18, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-61469" class="comments-container">
<span id="61470"></span>
<div id="comment-61470" class="comment">
<div id="post-61470-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you. Not sure why I had to modify it to <a href="http://overpass-turbo.eu/s/ucs">http://overpass-turbo.eu/s/ucs</a> to show me all results.</p>
</div>
<div id="comment-61470-info" class="comment-info">
<span class="comment-age">(03 Jan '18, 22:29)</span> <span class="comment-user userinfo">postak420</span>
</div>
</div>
<span id="61471"></span>
<div id="comment-61471" class="comment">
<div id="post-61471-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just omitted ways and relations to save typing for my example.</p>
</div>
<div id="comment-61471-info" class="comment-info">
<span class="comment-age">(04 Jan '18, 01:18)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-61469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61469-form-container" class="comment-form-container">
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

