+++
type = "question"
title = "Overpass API Union doesn&#x27;t work"
description = '''Hi, I use the overpass api for QA a lot. But somehow I can&#x27;t get the union statement working. I tried it as described in the Wiki but I only receive the data from the first statement.  area[name=&quot;Sankt Andreasberg&quot;]; (  node[amenity=recycling](area);  node[amenity=bench](area); ) -&amp;gt; .a; .a out; '''
date = "2016-03-23T18:12:00Z"
lastmod = "2016-03-24T17:47:00Z"
weight = 48794
keywords = [ "union", "overpass" ]
aliases = [ "/questions/48794" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API Union doesn't work](/questions/48794/overpass-api-union-doesnt-work)

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
<span id="post-48794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48794-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I use the overpass api for QA a lot. But somehow I can't get the union statement working. I tried it as described in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union">Wiki</a> but I only receive the data from the first statement.</p>
<pre><code>area[name=&quot;Sankt Andreasberg&quot;];
(
  node[amenity=recycling](area);
  node[amenity=bench](area);
) -&gt; .a;
.a out;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-union" rel="tag" title="see questions tagged &#39;union&#39;">union</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '16, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-48794" class="comments-container">
&#10;</div>
<div id="comment-tools-48794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48794-form-container" class="comment-form-container">
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

<span id="48795"></span>

<div id="answer-container-48795" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48795-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>node[amenity=recycling](area);</code> statement overwrites the default input set so there are no areas for the second node query.</p>
<p>You just need to save the area to a set and pass it to the node queries (untested):</p>
<pre><code>area[name=&quot;Sankt Andreasberg&quot;]-&gt;.searchArea;
(
  node[amenity=recycling](area.searchArea);
  node[amenity=bench](area.searchArea);
) -&gt; .a;
.a out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '16, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '16, 19:09</strong> </span></p>
</div>
</div>
<div id="comments-container-48795" class="comments-container">
<span id="48796"></span>
<div id="comment-48796" class="comment">
<div id="post-48796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Knowing that could have spared me a lot of trying and searching.</p>
</div>
<div id="comment-48796-info" class="comment-info">
<span class="comment-age">(23 Mar '16, 19:09)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
<span id="48827"></span>
<div id="comment-48827" class="comment">
<div id="post-48827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As this is a really common issue, can somebody here please update the wiki page accordingly to make this a bit clearer? Thanks!</p>
</div>
<div id="comment-48827-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 17:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48795-form-container" class="comment-form-container">
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

