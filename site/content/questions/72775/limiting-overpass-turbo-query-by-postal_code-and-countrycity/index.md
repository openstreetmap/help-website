+++
type = "question"
title = "Limiting overpass turbo query by postal_code and country/city"
description = '''I&#x27;d like to limit a query (for highways) by postal_code and country (since the postal_codes are only unique on a national level). Let&#x27;s say that is my query: area[postal_code=&quot;19300&quot;]-&amp;gt;.searchArea; area.searchArea[name=&quot;Germany&quot;]; way(area.searchArea)[highway][name]; (._;&amp;gt;;); out;  http://over...'''
date = "2020-01-30T14:04:00Z"
lastmod = "2020-01-30T14:58:00Z"
weight = 72775
keywords = [ "osm", "overpass-turbo" ]
aliases = [ "/questions/72775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Limiting overpass turbo query by postal_code and country/city](/questions/72775/limiting-overpass-turbo-query-by-postal_code-and-countrycity)

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
<span id="post-72775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to limit a query (for highways) by postal_code and country (since the postal_codes are only unique on a national level).</p>
<p>Let's say that is my query:</p>
<pre><code>area[postal_code=&quot;19300&quot;]-&gt;.searchArea;
area.searchArea[name=&quot;Germany&quot;];
way(area.searchArea)[highway][name];
(._;&gt;;);
out;</code></pre>
<p><a href="http://overpass-turbo.eu/s/QeG">http://overpass-turbo.eu/s/QeG</a></p>
<p>By that I get highways in Germany and in France.</p>
<p>I thought about something like</p>
<pre><code>area.searchArea[name=&quot;Germany&quot;].-&gt;searchArea2;
way(area.searchArea2)[highway][name];</code></pre>
<p>But this doesn't work.</p>
<p>What would be the correct syntax?</p>
<p>Or how could I link something like</p>
<pre><code>{{geocodeArea:Germany}}</code></pre>
<p>to this kind of query?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '20, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/df59efd5a42c57c0a08274b519c82e49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="entenbein&#39;s gravatar image" />
<p><span>entenbein</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="entenbein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72775" class="comments-container">
<span id="72776"></span>
<div id="comment-72776" class="comment">
<div id="post-72776-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost, including an answer: <a href="https://gis.stackexchange.com/questions/349037/limiting-overpass-turbo-query-by-postal-code-and-country">https://gis.stackexchange.com/questions/349037/limiting-overpass-turbo-query-by-postal-code-and-country</a></p>
</div>
<div id="comment-72776-info" class="comment-info">
<span class="comment-age">(30 Jan '20, 14:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="72777"></span>
<div id="comment-72777" class="comment">
<div id="post-72777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, that one solved it!</p>
</div>
<div id="comment-72777-info" class="comment-info">
<span class="comment-age">(30 Jan '20, 14:57)</span> <span class="comment-user userinfo">entenbein</span>
</div>
</div>
</div>
<div id="comment-tools-72775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72775-form-container" class="comment-form-container">
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

<span id="72778"></span>

<div id="answer-container-72778" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72778-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That one solved it <a href="https://gis.stackexchange.com/a/349089/157271">https://gis.stackexchange.com/a/349089/157271</a></p>
<p>Thanks <a href="https://help.openstreetmap.org/users/8708/mmd">@mmd</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '20, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/df59efd5a42c57c0a08274b519c82e49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="entenbein&#39;s gravatar image" />
<p><span>entenbein</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="entenbein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72778" class="comments-container">
&#10;</div>
<div id="comment-tools-72778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72778-form-container" class="comment-form-container">
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

