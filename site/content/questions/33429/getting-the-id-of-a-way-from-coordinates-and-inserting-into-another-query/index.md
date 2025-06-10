+++
type = "question"
title = "Getting the Id of a Way from coordinates and inserting into another query"
description = '''Hello,  I am making an application that uses the Overpass API.  I want a query that returns the roads for any given way that connect to that road. Is there a way to retrieve a single way id for a given coordinate/ boundary box, then storing this in a variable and running it in another query?  Here i...'''
date = "2014-05-23T16:09:00Z"
lastmod = "2014-05-23T16:09:00Z"
weight = 33429
keywords = [ "overpass", "id", "way", "query" ]
aliases = [ "/questions/33429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting the Id of a Way from coordinates and inserting into another query](/questions/33429/getting-the-id-of-a-way-from-coordinates-and-inserting-into-another-query)

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
<span id="post-33429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33429-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-33429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am making an application that uses the Overpass API.</p>
<p>I want a query that returns the roads for any given way that connect to that road.</p>
<p>Is there a way to retrieve a single way id for a given coordinate/ boundary box, then storing this in a variable and running it in another query?</p>
<p>Here is an example query:</p>
<pre><code>way(4419793);
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;path|track|cycleway|footway|service|residential|bridleway&quot;];(._;&gt;;))-&gt;.a;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;unclassified|path|track|cycleway|footway|residential|service|bridleway&quot;];(._;&gt;;))-&gt;.b;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;unclassified|path|track|cycleway|footway|residential|service|bridleway&quot;];(._;&gt;;))-&gt;.c;
(way(around:0)[highway~&quot;.&quot;][highway!~&quot;unclassified|path|track|cycleway|footway|residential|service|bridleway&quot;];(._;&gt;;))-&gt;.d;
(.a;.b;.c;.d;);out;</code></pre>
<p>What I want to do is find a way to get the way id automatically from a bounding box/ pair of coordinates and run the new query in the form:</p>
<pre><code>.var =  (node(51.249,7.148,51.251,7.152);&lt;;);out;
&#10;way(.var);</code></pre>
<p>(and the .var contains the first returned way id for example) ....</p>
<p>Cheers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '14, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '14, 18:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span></p>
</div>
</div>
<div id="comments-container-33429" class="comments-container">
&#10;</div>
<div id="comment-tools-33429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

