+++
type = "question"
title = "How to select ways that are NOT in specific areas?"
description = '''Hi, I am trying this for hours now.  How to select ways that are OUTSIDE an area (polygon) with a certain tag? The following code prints out tracks (overpass turbo). Now, I want the subset of Tracks that are NOT part of polygons with tags like (&quot;boundary&quot;=&quot;protected_area&quot;): [out:json][timeout:25]; (...'''
date = "2018-04-05T11:29:00Z"
lastmod = "2018-04-08T10:34:00Z"
weight = 62918
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/62918" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to select ways that are NOT in specific areas?](/questions/62918/how-to-select-ways-that-are-not-in-specific-areas)

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
<span id="post-62918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62918-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying this for hours now.</p>
<p>How to select ways that are OUTSIDE an area (polygon) with a certain tag?</p>
<p>The following code prints out tracks (<a href="https://overpass-turbo.eu/s/xBx">overpass turbo</a>). Now, I want the subset of Tracks that are NOT part of polygons with tags like ("boundary"="protected_area"):</p>
<pre><code>[out:json][timeout:25];
(
 way
   [&quot;highway&quot;=&quot;track&quot;]
   ({{bbox}}); 
   // remove ways outside of area with tag &quot;boundary&quot;=&quot;protected_area&quot;
);
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '18, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/bc0f1c3258b1fcf7447344eebbf8f88f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StefanFreilig&#39;s gravatar image" />
<p><span>StefanFreilig</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StefanFreilig has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62918" class="comments-container">
&#10;</div>
<div id="comment-tools-62918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62918-form-container" class="comment-form-container">
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

<span id="62937"></span>

<div id="answer-container-62937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62937-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some unclear issues related to your question like: what is the "outside" to your original area (the complementary area relative to the whole Planet or to a larger rectangular polygon enclosing you area), what with the ways crossing the area... just to mention some. Anyway, assuming that the query/filtering model you have mentioned works properly here are some hints/options:<br />
-Using a larger rectangular polygon and your query model select the ways inside the rectangle. So, subtract from that set of ways the ways you have already as a result from before.<br />
-Create a complementary area to your original area and run your query using this as the area argument. To create the complement area is rather simple. Take the larger rectangular polygon and tag it as outer. Add to this the polygons from your original area with opposite rules. This multipolygon now probably represents the "outside" of your original area.<br />
However, be careful. If the set of ways to filter is large and so is the outer polygon of your original area, the procedure to accomplish may take many, many hours. In similar cases you need much more robust and specialized filtering/extracting models than the one you have described.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '18, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-62937" class="comments-container">
&#10;</div>
<div id="comment-tools-62937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62937-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62942"></span>

<div id="answer-container-62942" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the solution I am working with. It is quite slow though.</p>
<pre><code>[out:json];
area
  [&quot;boundary&quot;=&quot;protected_area&quot;]
  ({{bbox}})-&gt;.searchArea;
&#10;way
  [&quot;highway&quot;=&quot;track&quot;]
  ({{bbox}})
  (area.searchArea)-&gt;.badTracks;
&#10;way
  [&quot;highway&quot;=&quot;track&quot;]
  [&quot;tracktype&quot;!~&quot;^grade1$&quot;]
  ({{bbox}})-&gt;.allTracks;
&#10;(.allTracks - .badTracks;);
(._;&gt;;);
out skel;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '18, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/bc0f1c3258b1fcf7447344eebbf8f88f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StefanFreilig&#39;s gravatar image" />
<p><span>StefanFreilig</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StefanFreilig has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-62942" class="comments-container">
&#10;</div>
<div id="comment-tools-62942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62942-form-container" class="comment-form-container">
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

