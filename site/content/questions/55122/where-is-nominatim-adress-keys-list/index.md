+++
type = "question"
title = "Where is nominatim adress keys list?"
description = '''The example request:  http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=45.468401928178&amp;amp;lon=9.1730680478755&amp;amp;accept-language=en  Answer:  {  ...  &quot;address&quot; : {  &quot;cafe&quot; : &quot;Fiorio 1780&quot;,  &quot;house_number&quot; : &quot;26&quot;,  &quot;road&quot; : &quot;Via Vincenzo Monti&quot;,  &quot;suburb&quot; : &quot;Porta Vercellina&quot;,  &quot;city&quot;...'''
date = "2017-03-16T10:39:00Z"
lastmod = "2017-03-16T11:04:00Z"
weight = 55122
keywords = [ "nominatim" ]
aliases = [ "/questions/55122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where is nominatim adress keys list?](/questions/55122/where-is-nominatim-adress-keys-list)

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
<span id="post-55122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The example request:</p>
<pre><code>http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=45.468401928178&amp;lon=9.1730680478755&amp;accept-language=en</code></pre>
<p>Answer:</p>
<pre><code>{
    ...
    &quot;address&quot; : {
        &quot;cafe&quot; : &quot;Fiorio 1780&quot;,
        &quot;house_number&quot; : &quot;26&quot;,
        &quot;road&quot; : &quot;Via Vincenzo Monti&quot;,
        &quot;suburb&quot; : &quot;Porta Vercellina&quot;,
        &quot;city&quot; : &quot;Milan&quot;,
        &quot;county&quot; : &quot;Milan&quot;,
        &quot;state&quot; : &quot;Lombardy&quot;,
        &quot;postcode&quot; : &quot;20123&quot;,
        &quot;country&quot; : &quot;Italy&quot;,
        &quot;country_code&quot; : &quot;it&quot;
    },
    &quot;boundingbox&quot; : [&quot;45.4681247&quot;, &quot;45.4683247&quot;, &quot;9.172875&quot;, &quot;9.173075&quot;]
}</code></pre>
<p>The address keys are: cafe, house_number, road, suburb, city, county, state, postcode, country, country_code.</p>
<p>I want to find the list of all available address keys. If this list doesn't exists, I want to know relation between this keys and osm tags.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '17, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/91f51616367436f400039e73daac62cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kz_sergey&#39;s gravatar image" />
<p><span>kz_sergey</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kz_sergey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55122" class="comments-container">
&#10;</div>
<div id="comment-tools-55122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55122-form-container" class="comment-form-container">
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

<span id="55123"></span>

<div id="answer-container-55123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55123-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the function <a href="https://github.com/openstreetmap/Nominatim/blob/1542a006cbb315812316e6788ad68f7f3010e557/lib/lib.php#L121"><code>getClassTypes()</code> in lib.php</a>. The relation between address key and OSM tags is purely defined by Nominatim internals.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '17, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55123" class="comments-container">
&#10;</div>
<div id="comment-tools-55123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55123-form-container" class="comment-form-container">
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

