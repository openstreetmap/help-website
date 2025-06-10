+++
type = "question"
title = "How to get coordinates along a specific road?"
description = '''I am trying to get a list of coordinates for a specified road by inputting the road name/number. Is there a way to do that? Thanks!'''
date = "2021-01-30T09:43:00Z"
lastmod = "2021-02-27T10:49:00Z"
weight = 78598
keywords = [ "road", "coordinates" ]
aliases = [ "/questions/78598" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get coordinates along a specific road?](/questions/78598/how-to-get-coordinates-along-a-specific-road)

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
<span id="post-78598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get a list of coordinates for a specified road by inputting the road name/number. Is there a way to do that? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '21, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/52ba920d754440cba5e55f6d8ea6416a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edenmaylie&#39;s gravatar image" />
<p><span>edenmaylie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edenmaylie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78598" class="comments-container">
&#10;</div>
<div id="comment-tools-78598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78598-form-container" class="comment-form-container">
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

<span id="79047"></span>

<div id="answer-container-79047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As an example with <a href="https://overpass-turbo.eu/#">overpass-turbo</a>:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query with id
  way(id:200820110)({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>or</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query with name
  way[name=&#39;Schmidtsdrift Road&#39;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>should give you what you want. Alternately after <code>//print results</code> you could have <code>out geom;</code> but as far as I am aware the output will not be 100% compatible with the normal OSM XML format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '21, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79047" class="comments-container">
&#10;</div>
<div id="comment-tools-79047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79047-form-container" class="comment-form-container">
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

