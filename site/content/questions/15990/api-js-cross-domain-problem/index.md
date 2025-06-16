+++
type = "question"
title = "API: JS cross-domain problem"
description = '''OSM has an API to query data. Like this: https://www.openstreetmap.org/api/0.6/map?bbox=7.012854,51.450317,7.016477,51.452105 However, you can&#x27;t do this query from javascript, because this would violate the &quot;cross-domain policy&quot;. If I understood it right, OSM could remove this policy by adding these ...'''
date = "2012-09-12T09:41:00Z"
lastmod = "2021-04-02T08:03:00Z"
weight = 15990
keywords = [ "ajax", "api", "javascript" ]
aliases = [ "/questions/15990" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [API: JS cross-domain problem](/questions/15990/api-js-cross-domain-problem)

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
<span id="post-15990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15990-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OSM has an API to query data. Like this: <a href="https://www.openstreetmap.org/api/0.6/map?bbox=7.012854,51.450317,7.016477,51.452105">https://www.openstreetmap.org/api/0.6/map?bbox=7.012854,51.450317,7.016477,51.452105</a></p>
<p>However, you can't do this query from javascript, because this would violate the "cross-domain policy". If I understood it right, OSM could remove this policy by adding these HTTP headers to the API answer:</p>
<p>response['Access-Control-Allow-Origin'] = "*" response['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS" response['Access-Control-Allow-Headers'] = "X-Requested-With"</p>
<p>(Taken from Stackoverflow-question "Cross domain POST query using Cross-Origin Resource Sharing getting no data back")</p>
<p><strong>My questions:</strong> 1. Is this limitation (as it currently is) intentional? 2. Would be possible for you to add these headers to support js queries? (Please?)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ajax" rel="tag" title="see questions tagged &#39;ajax&#39;">ajax</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '12, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c3479b3eb33f3603f61be12d328a58f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tt40&#39;s gravatar image" />
<p><span>tt40</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tt40 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '12, 07:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-15990" class="comments-container">
&#10;</div>
<div id="comment-tools-15990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15990-form-container" class="comment-form-container">
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

<span id="16002"></span>

<div id="answer-container-16002" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16002-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-16002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tt40 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use Overpass API instead. Just replace</p>
<pre><code>https://www.openstreetmap.org/api/0.6/</code></pre>
<p>by</p>
<pre><code>http://overpass-api.de/api/xapi?</code></pre>
<p>So you get e.g. <a href="http://overpass-api.de/api/xapi?map?bbox=7.012854,51.450317,7.016477,51.452105">http://overpass-api.de/api/xapi?map?bbox=7.012854,51.450317,7.016477,51.452105</a></p>
<p>Overpass API sets a cross-origin header.</p>
<p>The rationale behind this is that the OSM main API is for editing, not for data reading. By contrast, <a href="https://wiki.openstreetmap.org/wiki/XAPI">the mirrors</a> (one of which is Overpass API) serve beside a small time lag the same data, are intended for read only operations, and usually answer much faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '12, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-16002" class="comments-container">
<span id="16004"></span>
<div id="comment-16004" class="comment">
<div id="post-16004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect!!!!!!</p>
</div>
<div id="comment-16004-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 14:10)</span> <span class="comment-user userinfo">tt40</span>
</div>
</div>
</div>
<div id="comment-tools-16002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16002-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15991"></span>

<div id="answer-container-15991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15991-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know anything about this headers features and if they can be fixed in the HTTP response. But, there is a classical workaround: you can put a proxy script (php or python for example( on your webserver that will download the data and serve it locally. You can find some examples on the web, like <a href="http://bazaar.launchpad.net/~nicolas-dumoulin/+junk/xapiviewer/view/head:/proxy.cgi">mine</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '12, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15991" class="comments-container">
<span id="15992"></span>
<div id="comment-15992" class="comment">
<div id="post-15992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point, I should have thought of that myself. Do I need a registration or API key? I don't want to be blocked suddenly if I do too many queries...</p>
<p>Nevertheless:</p>
<p>If anybody knows the answers to the original questions, I'd still be interested to solve this without a proxy. Might be useful for other JS developers, too.</p>
</div>
<div id="comment-15992-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 10:01)</span> <span class="comment-user userinfo">tt40</span>
</div>
</div>
<span id="15993"></span>
<div id="comment-15993" class="comment">
<div id="post-15993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is an <a href="https://wiki.openstreetmap.org/wiki/API_usage_policy">API usage policy</a> - it's the usual issue of shared resources. Depending on what you actually want to do, there may well be better alternatives to hitting the API directly.</p>
</div>
<div id="comment-15993-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 11:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15991-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79492"></span>

<div id="answer-container-79492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In 2021, the OSM API <strong>is</strong> setting CORS header! For example:</p>
<pre><code>const r = await fetch(&quot;https://api.openstreetmap.org/api/0.6/notes/100.json&quot;);
const note = await r.json();</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '21, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/65359a03fc9d192b1186866349f9cf31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darthwalsh&#39;s gravatar image" />
<p><span>darthwalsh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darthwalsh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79492" class="comments-container">
&#10;</div>
<div id="comment-tools-79492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79492-form-container" class="comment-form-container">
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

