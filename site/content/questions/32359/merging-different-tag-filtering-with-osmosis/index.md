+++
type = "question"
title = "Merging different tag filtering with Osmosis"
description = '''I&#x27;m trying to filter sport, leisure and amenity keys and then merge them with Osmosis: osmosis --read-pbf file=switzerland.pbf --tf accept-nodes sport=* --tf accept-ways sport=* --tf reject-relations outPipe.0=&quot;sport&quot; --read-pbf file=switzerland.pbf --tf accept-nodes amenity=* --tf accept-ways ameni...'''
date = "2014-04-14T10:35:00Z"
lastmod = "2016-02-06T18:43:00Z"
weight = 32359
keywords = [ "osmosis" ]
aliases = [ "/questions/32359" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Merging different tag filtering with Osmosis](/questions/32359/merging-different-tag-filtering-with-osmosis)

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
<span id="post-32359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32359-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to filter sport, leisure and amenity keys and then merge them with Osmosis:</p>
<pre><code>osmosis --read-pbf file=switzerland.pbf --tf accept-nodes sport=* --tf accept-ways sport=* --tf reject-relations outPipe.0=&quot;sport&quot; --read-pbf file=switzerland.pbf --tf accept-nodes amenity=* --tf accept-ways amenity=* --tf reject-relations outPipe.0=&quot;amenity&quot; --read-pbf file=switzerland.pbf --tf accept-nodes leisure=* --tf accept-ways leisure=* --tf reject-relations outPipe.0=&quot;leisure&quot; --merge inPipe.0=&quot;sport&quot; inPipe.1=&quot;amenity&quot; inPipe.2=&quot;leisure&quot; --write-pgsql host=128.178.1.1 database=myDB user=myUsn password=myPwd</code></pre>
<p>I have this error message that I don't understand:</p>
<pre><code>The following named pipes (leisure) and 0 default pipes have not been terminated with appropriate output sinks.</code></pre>
<p>I'm new with Osmosis. Sorry if this is a stupid question. But I cannot find the error.</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '14, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/65da3e87020b1932ba6fc144a74394f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antonind&#39;s gravatar image" />
<p><span>antonind</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antonind has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 10:38</strong> </span></p>
</div>
</div>
<div id="comments-container-32359" class="comments-container">
&#10;</div>
<div id="comment-tools-32359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32359-form-container" class="comment-form-container">
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

<span id="32361"></span>

<div id="answer-container-32361" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32361-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="antonind has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>--merge</code> can only merge two pipes, not more; you must use two instances of <code>--merge</code> to merge three pipes. Try this:</p>
<pre><code>osmosis \
  --read-pbf switzerland.osm.pbf --tf accept-nodes sport=* --tf accept-ways sport=* --tf reject-relations \
 --read-pbf file=switzerland.osm.pbf --tf accept-nodes amenity=* --tf accept-ways amenity=* --tf reject-relations \
 --read-pbf file=switzerland.osm.pbf --tf accept-nodes leisure=* --tf accept-ways leisure=* --tf reject-relations  \
 --merge --merge --write-pgsql host=128.178.1.1 database=myDB user=myUsn password=myPwd</code></pre>
<p>You might want to give <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> a try, it is less complicated for use cases like this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '14, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 11:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-32361" class="comments-container">
&#10;</div>
<div id="comment-tools-32361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32361-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47986"></span>

<div id="answer-container-47986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your error message is explained in another answer (the merge task can merge only two pipes, so you need two merge tasks). But there's another way to address your problem, which is to avoid merging entirely: You're filtering one tag pattern in each of three parallel pipelines, then merging those pipelines. In fact, each tag-filter task can accept more than one tag pattern, and will accept/reject entities if they match any of those supplied tag patterns. Here is an alternative command creating a single pipeline that should produce exactly the same results as your three-pipeline approach:</p>
<pre><code>osmosis \
 --read-pbf switzerland.osm.pbf \
 --tf accept-nodes sport=* amenity=* leisure=* \
 --tf accept-ways sport=* amenity=* leisure=* \
 --tf reject-relations \
 --write-pgsql host=128.178.1.1 database=myDB user=myUsn password=myPwd</code></pre>
<p>However, both your command and the one I proposed will probably not produce the output you are expecting. Both commands are retaining all nodes and ways that have a sport, amenity, or leisure tag, but they are not retaining any nodes referenced by these ways if the referenced nodes don't also have a sport, amenity, or leisure tag. This is the purpose of the used-node task: it will retain any nodes that are referenced by a retained way.</p>
<p>We can't just insert a used-node task into this single pipeline, because we want to retain both the nodes with certain tags and the nodes used by ways with those tags. So here you need two pipelines, but only one merge task:</p>
<pre><code>osmosis \
 --read-pbf switzerland.osm.pbf \
 --tf accept-nodes sport=* amenity=* leisure=* \
 --tf reject-ways \
 --tf reject-relations \
 --read-pbf switzerland.osm.pbf \
 --tf accept-ways sport=* amenity=* leisure=* \
 --tf reject-relations \
 --used-node \
 --merge \
 --write-pgsql host=128.178.1.1 database=myDB user=myUsn password=myPwd</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '16, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/aa89cac4eb961da882e29b31fac16ab9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abyrd&#39;s gravatar image" />
<p><span>abyrd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abyrd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47986" class="comments-container">
&#10;</div>
<div id="comment-tools-47986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47986-form-container" class="comment-form-container">
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

