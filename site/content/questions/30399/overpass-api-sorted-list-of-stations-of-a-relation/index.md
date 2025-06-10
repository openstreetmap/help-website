+++
type = "question"
title = "Overpass API : Sorted list of stations of a relation"
description = '''Hi, I&#x27;m pretty new a OSM &amp;amp; the Overpass API.  I was looking for, how to retrieve a list a stations of a given relation.  Here is what came up with :  &amp;lt; id-query ref=&quot;2418275&quot; type=&quot;relation&quot; /&amp;gt;  &amp;lt; recurse type=&quot;relation-node&quot; /&amp;gt;  &amp;lt; print/&amp;gt;  It works great but the station nodes ...'''
date = "2014-02-02T16:49:00Z"
lastmod = "2014-02-03T01:02:00Z"
weight = 30399
keywords = [ "overpass" ]
aliases = [ "/questions/30399" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API : Sorted list of stations of a relation](/questions/30399/overpass-api-sorted-list-of-stations-of-a-relation)

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
<span id="post-30399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30399-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm pretty new a OSM &amp; the Overpass API.</p>
<p>I was looking for, how to retrieve a list a stations of a given relation.</p>
<p>Here is what came up with :</p>
<pre><code>&lt; id-query ref=&quot;2418275&quot; type=&quot;relation&quot; /&gt;
  &lt; recurse type=&quot;relation-node&quot; /&gt;  
&lt; print/&gt;</code></pre>
<p>It works great but the station nodes are sorted by IDs in the XML. I was looking to get them sorted by the orientation (first station as first element, last station as last element).</p>
<p>Do you know how can I can achieve this ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '14, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30399" class="comments-container">
&#10;</div>
<div id="comment-tools-30399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30399-form-container" class="comment-form-container">
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

<span id="30400"></span>

<div id="answer-container-30400" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30400-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kyro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, this is currently not possible with the Overpass API alone. What you can do is print the relation also and then sort the stations in a post-processing step.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '14, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-30400" class="comments-container">
<span id="30402"></span>
<div id="comment-30402" class="comment">
<div id="post-30402-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok thanks, I went with a bash script to do this :</p>
<p><code> for i in </code><code>curl 'http://api.openstreetmap.org/api/0.6/relation/2418275' | grep stop | awk '{print $3}' | cut -d '"' -f2</code><code>; do curl </code><a href="http://api.openstreetmap.org/api/0.6/node/$%7Bi%7D"><code>http://api.openstreetmap.org/api/0.6/node/${i}</code></a><code> ; done` </code></p>
</div>
<div id="comment-30402-info" class="comment-info">
<span class="comment-age">(03 Feb '14, 01:02)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
</div>
<div id="comment-tools-30400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30400-form-container" class="comment-form-container">
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

