+++
type = "question"
title = "Overpass / Overpass turbo - how to search for recent changes only?"
description = '''I&#x27;d like to look for recent nodes on exactly latitude -1. That&#x27;s something a bit like this: [out:json][timeout:25]; (  node(-1.0,-180.0,-1.0,180.0); ); // print results out body; &amp;gt;; out skel qt;  Which nearly works, except that it&#x27;s not looking for recent nodes. The documentation leads me to beli...'''
date = "2016-11-24T18:12:00Z"
lastmod = "2017-03-18T10:53:00Z"
weight = 53100
keywords = [ "overpass" ]
aliases = [ "/questions/53100" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass / Overpass turbo - how to search for recent changes only?](/questions/53100/overpass-overpass-turbo-how-to-search-for-recent-changes-only)

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
<span id="post-53100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53100-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to look for recent nodes on exactly latitude -1. That's something a bit like this:</p>
<pre><code>[out:json][timeout:25];
(
  node(-1.0,-180.0,-1.0,180.0);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>Which nearly works, except that it's not looking for recent nodes. The documentation leads me to believe that something like</p>
<pre><code>[out:json][timeout:25];
(
  node(-1.0,-180.0,-1.0,180.0)._(changed:&quot;2016-01-01T00:00:00Z&quot;);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>ought to work, but unfortunately that gives:</p>
<pre><code>An error occured during the execution of the overpass query! This is what overpass API returned:
runtime error: Query run out of memory using about 2048 MB of RAM.</code></pre>
<p>Presumably, that is because the bounding box is counted as "large" (because it covers every latitude) rather than "small" (only one longitude) and therefore the "changed" part is being executed first, and obviously every node on the planet added this year results in an "out of memory" error.</p>
<p>Is there any way to rephrase this query to only return nodes in that bounding box that were modified this year?</p>
<p>(edit: spelling)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '16, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '16, 19:06</strong> </span></p>
</div>
</div>
<div id="comments-container-53100" class="comments-container">
&#10;</div>
<div id="comment-tools-53100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53100-form-container" class="comment-form-container">
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

<span id="53102"></span>

<div id="answer-container-53102" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try using the <code>newer:</code> filter (instead of <code>changed:</code>)! -&gt; <a href="http://overpass-turbo.eu/s/kio">http://overpass-turbo.eu/s/kio</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '16, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-53102" class="comments-container">
<span id="53103"></span>
<div id="comment-53103" class="comment">
<div id="post-53103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - that works!</p>
</div>
<div id="comment-53103-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 19:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53106"></span>
<div id="comment-53106" class="comment">
<div id="post-53106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a logic to having to use "diff" before the actual query (in []) and "changed" at the level of the queried items (in () )?</p>
</div>
<div id="comment-53106-info" class="comment-info">
<span class="comment-age">(25 Nov '16, 08:45)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="53127"></span>
<div id="comment-53127" class="comment">
<div id="post-53127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2850/joostenmies">@joost</a>: Hmm, as far as I know, the operations of the two operations are actually quite different: <code>changed</code> is basically just a beefed-up version of the <code>newer</code> statement (but which is still a bit slower than that in many use cases). Whereas <code>[diff:…]</code> (and <code>[adiff:…]</code>) actually performs the following query twice and outputs only the difference between the two results (and also uses a different output format).</p>
</div>
<div id="comment-53127-info" class="comment-info">
<span class="comment-age">(26 Nov '16, 14:21)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="53135"></span>
<div id="comment-53135" class="comment">
<div id="post-53135-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK thanks, just realized I've been using diff when I could have used the lighter changed or newer</p>
</div>
<div id="comment-53135-info" class="comment-info">
<span class="comment-age">(27 Nov '16, 08:55)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="55172"></span>
<div id="comment-55172" class="comment">
<div id="post-55172-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just for completeness, an example combining with a bounding box:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “waterway=stream”
  //node[&quot;waterway&quot;=&quot;stream&quot;]({{bbox}});
  way[&quot;waterway&quot;=&quot;stream&quot;]({{bbox}})(newer:&quot;2017-03-18T00:00:00Z&quot;);
  //relation[&quot;waterway&quot;=&quot;stream&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="comment-55172-info" class="comment-info">
<span class="comment-age">(18 Mar '17, 10:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53102-form-container" class="comment-form-container">
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

