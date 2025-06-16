+++
type = "question"
title = "Long changing from positive to negative when parsing"
description = '''I&#x27;m parsing OSM XML data into c#. I have a weird problem, each node has an id that is a long datatype. When parsing, if the id is 9 or less digits long, it seems to work just fine. However once it reaches 10 digits long, for some reason I start to get negative number from the parsing. Is there a rea...'''
date = "2015-03-26T18:17:00Z"
lastmod = "2015-03-26T20:52:00Z"
weight = 41929
keywords = [ "c#", "xml", "osmsharp", "parsing" ]
aliases = [ "/questions/41929" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Long changing from positive to negative when parsing](/questions/41929/long-changing-from-positive-to-negative-when-parsing)

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
<span id="post-41929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41929-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm parsing OSM XML data into c#.</p>
<p>I have a weird problem, each node has an id that is a long datatype. When parsing, if the id is 9 or less digits long, it seems to work just fine. However once it reaches 10 digits long, for some reason I start to get negative number from the parsing. Is there a reason for why this might be.</p>
<p>I'm using a library called OSMSharp for parsing. Language is c#.</p>
<p>An example of this: This way has 2 nodes:</p>
<pre><code>way id=&quot;313281300&quot; 
nd ref=&quot;248877110&quot;
nd ref=&quot;3191908562&quot;*</code></pre>
<p>After being parsed, I get this:</p>
<p>way: 313281300</p>
<p>248877110</p>
<p>-1103058734</p>
<p>Could this be a bug from the parsing library, or is it caused by c#?</p>
<p>Thank you in advance</p>
<p>*I made this xml short for ease of read. It's the full xml for the way in the file I'm parsing from</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-osmsharp" rel="tag" title="see questions tagged &#39;osmsharp&#39;">osmsharp</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '15, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a759928a25662633a5d3ba0288eb1561?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="echoalphapapa&#39;s gravatar image" />
<p><span>echoalphapapa</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="echoalphapapa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '15, 18:24</strong> </span></p>
</div>
</div>
<div id="comments-container-41929" class="comments-container">
<span id="41931"></span>
<div id="comment-41931" class="comment">
<div id="post-41931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/29285779/long-changing-from-positive-to-negative-when-parsing">https://stackoverflow.com/questions/29285779/long-changing-from-positive-to-negative-when-parsing</a></p>
</div>
<div id="comment-41931-info" class="comment-info">
<span class="comment-age">(26 Mar '15, 20:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41929-form-container" class="comment-form-container">
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

<span id="41930"></span>

<div id="answer-container-41930" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41930-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="echoalphapapa has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure you are using the latest version of OSMSharp and long definitions throughout? It looks like it is having problems relayed to <a href="https://wiki.openstreetmap.org/wiki/64-bit_Identifiers">https://wiki.openstreetmap.org/wiki/64-bit_Identifiers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '15, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-41930" class="comments-container">
<span id="41932"></span>
<div id="comment-41932" class="comment">
<div id="post-41932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this might be it actually. The only problem is the newer versions of OSMSharp don't support parsing. I will investigate further. Thanks</p>
</div>
<div id="comment-41932-info" class="comment-info">
<span class="comment-age">(26 Mar '15, 20:52)</span> <span class="comment-user userinfo">echoalphapapa</span>
</div>
</div>
</div>
<div id="comment-tools-41930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41930-form-container" class="comment-form-container">
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

