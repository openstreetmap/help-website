+++
type = "question"
title = "Overpass: is_in and how to recurse to all nodes and ways for areas found"
description = '''I have a simple overpass query based on is_in that does half of what I need - finds an area tagged as a building if one surrounds my input co-ordinates. So here&#x27;s what the query looks like for &quot;The Shard&quot; in London: is_in(51.5041386,-0.0862526); foreach(area._[&quot;building&quot;];out;); I&#x27;d like to also pul...'''
date = "2013-02-20T17:27:00Z"
lastmod = "2016-10-22T09:10:00Z"
weight = 20069
keywords = [ "overpass" ]
aliases = [ "/questions/20069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: is_in and how to recurse to all nodes and ways for areas found](/questions/20069/overpass-is_in-and-how-to-recurse-to-all-nodes-and-ways-for-areas-found)

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
<span id="post-20069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20069-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a simple overpass query based on is_in that does half of what I need - finds an area tagged as a building if one surrounds my input co-ordinates. So here's what the query looks like for "The Shard" in London:</p>
<p>is_in(51.5041386,-0.0862526); foreach(area._["building"];out;);</p>
<p>I'd like to also pull back the full geometry (ways and nodes) of the outline (indeed it'd be nice for this to work for buildings made as relations too, but let's not be greedy just yet). It seemed like one of the recurse options might do that, but I tried all I could think of to no avail. I'm guessing I'm missing an important piece. Can anybody show me what?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '13, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/15a9df48f5cf95563dcad2891eff3b38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mackerski&#39;s gravatar image" />
<p><span>mackerski</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mackerski has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20069" class="comments-container">
&#10;</div>
<div id="comment-tools-20069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20069-form-container" class="comment-form-container">
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

<span id="20099"></span>

<div id="answer-container-20099" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20099-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mackerski has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm sorry, there exists no direct implementation yet for this feature.</p>
<p>However, there are two effective workarounds for this: You could query the ways that are inside the area and have appropriate tags:</p>
<pre><code>is_in(51.5041386,-0.0862526);foreach(area._[&quot;building&quot;][&quot;name&quot;];way(area)[&quot;building&quot;][&quot;name&quot;];out;);</code></pre>
<p>As buildings usually don't overlap, this should almost always return the right object. And it would work for relations as well if there were any:</p>
<pre><code>is_in(51.5041386,-0.0862526);foreach(area._[&quot;building&quot;][&quot;name&quot;];rel(area)[&quot;building&quot;][&quot;name&quot;];out;);</code></pre>
<p>The downside is that this doesn't work properly with terraced houses, because the neighbouring house is considered as inside the area if it touches the area with a complete edge.</p>
<p>The second workaround would be to evaluate the area id: - An area with an id between 2.4 billion and 3.6 billion is always created from the way with area id minus 2.4 billion. - An area with an id of more than 3.6 billion is always created from the relation with area id minus 3.6 billion.</p>
<p>You would have to do two requests to use this workaround: the first fetches the ids, and then the second, like</p>
<pre><code>(way(31110737);&gt;;);out;</code></pre>
<p>fetches the actual geometry.</p>
<p>As this could be easily done on the server, I'll include a command for this workaround in the next version. This would also be sustainable if the numbering scheme for areas changes in the future. I'll post details here once a beta version is operational, in a couple of days.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '13, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-20099" class="comments-container">
<span id="20104"></span>
<div id="comment-20104" class="comment">
<div id="post-20104-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Helps a lot, thanks! I modified my basic query to this:</p>
<pre><code>is_in(51.5041386,-0.0862526);foreach(area._[&quot;building&quot;];out;
way(area)[&quot;building&quot;];out;
&gt;;out;);</code></pre>
<p>This does something very like what I want:</p>
<ul>
<li>Data includes the area ID of the shape I actually want, so I can apply simple post-processing to discard any non-matching ways</li>
<li>I get full geometry back in a single query</li>
</ul>
<p>Open question: the revised query above will match only building ways, not relations. I can run a second copy, but is there a nice way to also include relations in the same query?</p>
</div>
<div id="comment-20104-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 10:36)</span> <span class="comment-user userinfo">mackerski</span>
</div>
</div>
<span id="52629"></span>
<div id="comment-52629" class="comment">
<div id="post-52629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This answer doesn't seem to work any more? Trying this query on the Overpass Turbo site (<a href="http://overpass-turbo.eu/s/jxk),">http://overpass-turbo.eu/s/jxk),</a> it returns an empty set. The original question's query does return the appropriate <code>area</code> object, but converting back to the way that represents it isn't working.</p>
</div>
<div id="comment-52629-info" class="comment-info">
<span class="comment-age">(21 Oct '16, 21:56)</span> <span class="comment-user userinfo">Midnightligh...</span>
</div>
</div>
<span id="52631"></span>
<div id="comment-52631" class="comment">
<div id="post-52631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please try</p>
<p><code>is_in(51.5041386,-0.0862526); foreach( area._["building"]["name"]; way(pivot);out geom; );</code></p>
</div>
<div id="comment-52631-info" class="comment-info">
<span class="comment-age">(22 Oct '16, 09:10)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-20099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20099-form-container" class="comment-form-container">
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

