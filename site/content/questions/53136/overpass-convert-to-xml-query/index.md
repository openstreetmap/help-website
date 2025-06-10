+++
type = "question"
title = "Overpass - convert to XML query"
description = '''I want to extract housenumber nodes that are contained in a closed way tagged with &quot;building&quot;. I&#x27;ve been able to get the job done with OQ: it was a lucky shot, since I never ever used this syntax before. Now I would like to convert it to XML Overpass. I&#x27;ve tryed with no result (I&#x27;m having trouble wi...'''
date = "2016-11-27T22:05:00Z"
lastmod = "2016-11-28T10:34:00Z"
weight = 53136
keywords = [ "overpass", "query" ]
aliases = [ "/questions/53136" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass - convert to XML query](/questions/53136/overpass-convert-to-xml-query)

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
<span id="post-53136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53136-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to extract housenumber nodes that are contained in a closed way tagged with "building". I've been able to get the job done with OQ: it was a lucky shot, since I never ever used this syntax before. Now I would like to convert it to XML Overpass. I've tryed with no result (I'm having trouble with the recursion way). This is the query:</p>
<pre><code>[bbox:{{bbox}}];
way[building];
node(w)[&quot;addr:housenumber&quot;];
out meta;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '16, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/b88a31e4097701d418799b31e1892771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davide_sd&#39;s gravatar image" />
<p><span>Davide_sd</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davide_sd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53136" class="comments-container">
&#10;</div>
<div id="comment-tools-53136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53136-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="53139"></span>

<div id="answer-container-53139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53139-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a converter available:</p>
<p><a href="http://overpass-api.de/convert_form.html">http://overpass-api.de/convert_form.html</a></p>
<p>Note that this Overpass script will only find nodes which are members of the building way ('contained' to me implies that you also want to find unconnected addresses that are located inside the building).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '16, 02:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-53139" class="comments-container">
<span id="53142"></span>
<div id="comment-53142" class="comment">
<div id="post-53142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want only the nodes that are members of the building way ! :)</p>
<p>Nice, a converter... Unfortunately the converted query doesn't work, Overpass runs out of memory.</p>
</div>
<div id="comment-53142-info" class="comment-info">
<span class="comment-age">(28 Nov '16, 10:17)</span> <span class="comment-user userinfo">Davide_sd</span>
</div>
</div>
</div>
<div id="comment-tools-53139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53139-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53143"></span>

<div id="answer-container-53143" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53143-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, found it! I post the complete query: this return the nodes that are members of the <em>building</em> way and that have the <em>addr:housenumber</em> tag.</p>
<pre><code>&lt;osm-script&gt;
  &lt;query into=&quot;&lt;Name of the city&gt;&quot; type=&quot;area&quot;&gt;
    &lt;has-kv k=&quot;admin_level&quot; v=&quot;8&quot;/&gt;
    &lt;has-kv k=&quot;name&quot; v=&quot;&lt;Name of the city&gt;&quot;/&gt;
  &lt;/query&gt;
  &lt;query type=&quot;way&quot;&gt;
    &lt;area-query from=&quot;&lt;Name of the city&gt;&quot; /&gt;
    &lt;has-kv k=&quot;building&quot;/&gt;
  &lt;/query&gt;
  &lt;query type=&quot;node&quot;&gt;
    &lt;recurse type=&quot;way-node&quot;/&gt;
    &lt;has-kv k=&quot;addr:housenumber&quot;/&gt;
  &lt;/query&gt;
  &lt;print mode=&quot;meta&quot; /&gt;
&lt;/osm-script&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '16, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b88a31e4097701d418799b31e1892771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davide_sd&#39;s gravatar image" />
<p><span>Davide_sd</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davide_sd has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '16, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-53143" class="comments-container">
&#10;</div>
<div id="comment-tools-53143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53143-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53138"></span>

<div id="answer-container-53138" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53138-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There has been a recent <a href="https://help.openstreetmap.org/questions/52932/how-to-get-nodes-into-a-closed-way-in-a-single-overpass-query">similar query</a> regarding extracting nodes within a closed way that may help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '16, 01:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-53138" class="comments-container">
&#10;</div>
<div id="comment-tools-53138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53138-form-container" class="comment-form-container">
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

