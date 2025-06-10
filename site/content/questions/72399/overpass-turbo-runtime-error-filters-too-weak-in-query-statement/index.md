+++
type = "question"
title = "Overpass turbo: &quot;runtime error: Filters too weak in query statement&quot;"
description = '''I&#x27;m trying to count how many pistes are there in a given country: //[out:csv(::count, ::&quot;count:nodes&quot;, ::&quot;count:ways&quot;, ::&quot;count:relations&quot;, ::&quot;count:areas&quot;)]; area[&quot;ISO3166-1&quot;=&quot;EE&quot;]; (  way(area)[&quot;piste:type&quot;];  node(area)[&quot;piste:type&quot;];  area(area)[&quot;piste:type&quot;];  relation(area)[&quot;piste:type&quot;]; ); o...'''
date = "2020-01-07T11:03:00Z"
lastmod = "2020-01-08T15:27:00Z"
weight = 72399
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/72399" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass turbo: "runtime error: Filters too weak in query statement"](/questions/72399/overpass-turbo-runtime-error-filters-too-weak-in-query-statement)

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
<span id="post-72399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72399-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to count how many pistes are there in a given country:</p>
<pre><code>//[out:csv(::count, ::&quot;count:nodes&quot;, ::&quot;count:ways&quot;, ::&quot;count:relations&quot;, ::&quot;count:areas&quot;)];
area[&quot;ISO3166-1&quot;=&quot;EE&quot;];
(
  way(area)[&quot;piste:type&quot;];
  node(area)[&quot;piste:type&quot;];
  area(area)[&quot;piste:type&quot;];
  relation(area)[&quot;piste:type&quot;];
);
out;// count;</code></pre>
<p>(<a href="https://overpass-turbo.eu/s/Pwy">link</a>) When I run this commented one, I get an error:</p>
<blockquote>
<p>runtime error: Filters too weak in query statement: specify in addition a bbox, a tag filter, or similar.</p>
</blockquote>
<p>When I uncomment the rest, I get just the count of ways or whatever is the first statement in parenthesis.</p>
<p>How to do this correctly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '20, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/87a3753fcb288d735cda25a2806f2dd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V0174&#39;s gravatar image" />
<p><span>V0174</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V0174 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '20, 11:04</strong> </span></p>
</div>
</div>
<div id="comments-container-72399" class="comments-container">
&#10;</div>
<div id="comment-tools-72399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72399-form-container" class="comment-form-container">
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

<span id="72433"></span>

<div id="answer-container-72433" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72433-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="V0174 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The area needs to be stored ina variable &amp; passed to each way type:</p>
<pre><code>[out:csv(::count,::&quot;count:nodes&quot;,::&quot;count:ways&quot;,::&quot;count:relations&quot;)];
area[&quot;ISO3166-1&quot;=&quot;EE&quot;]-&gt;.a;
(
  way(area.a)[&quot;piste:type&quot;];
  node(area.a)[&quot;piste:type&quot;];
  relation(area.a)[&quot;piste:type&quot;];
);
out count;</code></pre>
<p>However, it's much easier to amalgamate them to <code>nwr</code>:</p>
<pre><code>[out:csv(::count,::&quot;count:nodes&quot;,::&quot;count:ways&quot;,::&quot;count:relations&quot;)];
area[&quot;ISO3166-1&quot;=EE]; // Estonia
nwr(area)[&quot;piste:type&quot;];
out count;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '20, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '20, 21:35</strong> </span></p>
</div>
</div>
<div id="comments-container-72433" class="comments-container">
<span id="72436"></span>
<div id="comment-72436" class="comment">
<div id="post-72436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again, this does exactly what I need.</p>
</div>
<div id="comment-72436-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 15:27)</span> <span class="comment-user userinfo">V0174</span>
</div>
</div>
</div>
<div id="comment-tools-72433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72433-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72425"></span>

<div id="answer-container-72425" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72425-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Remove the <code>area</code> type.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '20, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72425" class="comments-container">
<span id="72432"></span>
<div id="comment-72432" class="comment">
<div id="post-72432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that was the reason for the error. However it still doesn't print all the counts separately, only the one that is stated as the first one in the union: <a href="https://overpass-turbo.eu/s/PzB">https://overpass-turbo.eu/s/PzB</a> Any idea?</p>
</div>
<div id="comment-72432-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 13:43)</span> <span class="comment-user userinfo">V0174</span>
</div>
</div>
</div>
<div id="comment-tools-72425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72425-form-container" class="comment-form-container">
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

