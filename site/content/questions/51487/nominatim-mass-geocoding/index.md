+++
type = "question"
title = "Nominatim Mass Geocoding"
description = '''Hello, I managed to set up my own Nominatim Server.   I would like to run mass geocoding, for example 100.000 Adresses that I want to enrich with lat/ lon. What would be the fastest / most efficient way to realize that via Nominatim? Can I run a script, that calculates me every adress in germany wit...'''
date = "2016-08-17T13:09:00Z"
lastmod = "2016-08-18T09:45:00Z"
weight = 51487
keywords = [ "nominatim", "geocoding" ]
aliases = [ "/questions/51487" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Mass Geocoding](/questions/51487/nominatim-mass-geocoding)

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
<span id="post-51487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51487-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I managed to set up my own Nominatim Server.</p>
<ol>
<li>I would like to run mass geocoding, for example 100.000 Adresses that I want to enrich with lat/ lon. What would be the fastest / most efficient way to realize that via Nominatim?</li>
<li>Can I run a script, that calculates me every adress in germany with lat / lon? In which language would that script be and could you maybe lead me to some helpful links?</li>
</ol>
<p>Thanks in advance, yours truly, Stephano</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeaae6ed1cbb7581b9338affb59e4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephano007&#39;s gravatar image" />
<p><span>Stephano007</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephano007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51487" class="comments-container">
&#10;</div>
<div id="comment-tools-51487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51487-form-container" class="comment-form-container">
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

<span id="51491"></span>

<div id="answer-container-51491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51491-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim isn't different from other geocoders in that regard. There is an API, you request a URL in the programming language of your choice and receive a JSON or XML data structure back. Every programming language can do that.</p>
<p>The search parameters are documented here <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Search">https://wiki.openstreetmap.org/wiki/Nominatim#Search</a> and you would run a query against your own Nominatim server, e.g. <a href="http://localhost:8080/nominatim/search.php?...&amp;format=json">http://localhost:8080/nominatim/search.php?...&amp;format=json</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-51491" class="comments-container">
<span id="51492"></span>
<div id="comment-51492" class="comment">
<div id="post-51492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Although not for <em>mass geocoding</em>, see <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">Nominatim's usage policy</a>.</p>
</div>
<div id="comment-51492-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 14:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51493"></span>
<div id="comment-51493" class="comment">
<div id="post-51493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok thanks, if I want to enrich 100.000 adresses, I guess I have to make 100.000 single Querys, but I can automatize that via JavaScript, right?</p>
</div>
<div id="comment-51493-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 14:09)</span> <span class="comment-user userinfo">Stephano007</span>
</div>
</div>
<span id="51494"></span>
<div id="comment-51494" class="comment">
<div id="post-51494-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Stephano007 wrote he setup his own Nominatim Server.</p>
</div>
<div id="comment-51494-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 14:25)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="51496"></span>
<div id="comment-51496" class="comment">
<div id="post-51496-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. With Javascript you need to watch out not to send too many requests at the same time because Javascript will not wait for a request to finish and start with the next request immediately. Limit it to 2-5 parallel requests as a start.http://caolan.github.io/async/ may help.</p>
</div>
<div id="comment-51496-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 14:31)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="51515"></span>
<div id="comment-51515" class="comment">
<div id="post-51515-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> They have set up their own Nominatim server, so the Nominatim usage policy doesn't apply. (Wanting to do mass geocoding is one good reason for setting up your own server).</p>
</div>
<div id="comment-51515-info" class="comment-info">
<span class="comment-age">(18 Aug '16, 09:43)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="51516"></span>
<div id="comment-51516" class="comment not_top_scorer">
<div id="post-51516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@Stephan007 Yes you can do that with Javascript. It's just a loop.</p>
</div>
<div id="comment-51516-info" class="comment-info">
<span class="comment-age">(18 Aug '16, 09:45)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-51491" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-51491-form-container" class="comment-form-container">
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

