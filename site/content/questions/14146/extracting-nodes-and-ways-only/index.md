+++
type = "question"
title = "Extracting nodes and ways only"
description = '''I am looking to extract only the nodes and ways on streets in my city, I have been looking for methods to do this but I am quite new to programming and do not know where to start reading. Can somebody please point me in the right direction? Thanks very much'''
date = "2012-07-10T18:49:00Z"
lastmod = "2012-07-12T16:55:00Z"
weight = 14146
keywords = [ "ways", "nodes" ]
aliases = [ "/questions/14146" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting nodes and ways only](/questions/14146/extracting-nodes-and-ways-only)

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
<span id="post-14146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking to extract only the nodes and ways on streets in my city, I have been looking for methods to do this but I am quite new to programming and do not know where to start reading. Can somebody please point me in the right direction? Thanks very much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '12, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/60f88b68b05449060d0744671d8cf758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="somedude&#39;s gravatar image" />
<p><span>somedude</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="somedude has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14146" class="comments-container">
&#10;</div>
<div id="comment-tools-14146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14146-form-container" class="comment-form-container">
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

<span id="14160"></span>

<div id="answer-container-14160" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14160-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-14160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="somedude has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First get your just your city. If your city is <a href="http://metro.teczno.com/">one of these</a>, then it's very easy. Otherwise see the various options on <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">downloading data page</a></p>
<p>Then filter by highway tag. You might do this with an <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29">Osmosis tag filter</a></p>
<pre><code>osmosis \
  --read-xml input.osm \
  --tf accept-ways highway=* \ 
  --tf reject-relations \
  --used-node \
  --write-xml output.osm</code></pre>
<p>Or other filtering tools are available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 01:25</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-14160" class="comments-container">
<span id="14232"></span>
<div id="comment-14232" class="comment">
<div id="post-14232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... yes, like <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> :-)</p>
</div>
<div id="comment-14232-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 16:55)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-14160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14160-form-container" class="comment-form-container">
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

