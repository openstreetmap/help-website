+++
type = "question"
title = "osm2pgsql stalled?"
description = '''Hi, I&#x27;m doing a full planet ingest using osm2pgsql on an Amazon AWS instance. I&#x27;ve given it a 25 gb cache using slim mode, and it&#x27;s been very speedy. I started the process yesterday morning and now we&#x27;re at the &quot;Going over pending ways&quot; portion. I&#x27;m concerned however that the process has stalled out...'''
date = "2015-06-11T16:23:00Z"
lastmod = "2015-06-13T19:52:00Z"
weight = 43534
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/43534" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql stalled?](/questions/43534/osm2pgsql-stalled)

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
<span id="post-43534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43534-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm doing a full planet ingest using osm2pgsql on an Amazon AWS instance. I've given it a 25 gb cache using slim mode, and it's been very speedy. I started the process yesterday morning and now we're at the "Going over pending ways" portion.</p>
<p>I'm concerned however that the process has stalled out. My log file has not updated for 2 hours and I am stuck at</p>
<pre><code>    Going over pending ways...
    191006558 ways are pending
&#10;    Using 1 helper-processes</code></pre>
<p>And that's the end of my log file. When it was processing the nodes/ways/rels, at least I got an update of how far it was, but now it seems to have possibly stalled since nothing has updated in 2 hours.</p>
<p>How can I tell how far along this portion of the process is? Or, how can I tell if it has stalled out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '15, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/db78026ad30fff15a88f62ab986c464a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pixelk8e&#39;s gravatar image" />
<p><span>pixelk8e</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pixelk8e has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43534" class="comments-container">
<span id="43539"></span>
<div id="comment-43539" class="comment">
<div id="post-43539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you already check CPU usage and I/O load of your osm2pgsql process?</p>
</div>
<div id="comment-43539-info" class="comment-info">
<span class="comment-age">(11 Jun '15, 18:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43540"></span>
<div id="comment-43540" class="comment">
<div id="post-43540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it is using ~10-20% of the cpu at any given time (averaging at about 14%), but i/o seems to be nonexistent (I'm running osm2pgsql to a database on another instance, so that makes sense to me). But I'm still concerned it's chugging away at nothing.</p>
</div>
<div id="comment-43540-info" class="comment-info">
<span class="comment-age">(11 Jun '15, 18:17)</span> <span class="comment-user userinfo">pixelk8e</span>
</div>
</div>
<span id="43560"></span>
<div id="comment-43560" class="comment">
<div id="post-43560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "wa" (I/O wait) say in <code>top</code>?</p>
</div>
<div id="comment-43560-info" class="comment-info">
<span class="comment-age">(13 Jun '15, 19:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43534-form-container" class="comment-form-container">
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

<span id="43553"></span>

<div id="answer-container-43553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are current versions of osm2pgsql that don't provide any output during that stage.</p>
<p>For estimated times for import see <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks</a></p>
<p>Note that due to OSM data growth these are always out of date (but can give you a rough indication).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '15, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-43553" class="comments-container">
&#10;</div>
<div id="comment-tools-43553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43553-form-container" class="comment-form-container">
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

