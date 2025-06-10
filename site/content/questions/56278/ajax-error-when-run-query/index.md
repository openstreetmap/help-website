+++
type = "question"
title = "Ajax error when run query"
description = '''I&#x27;ve installed osm3s, database and web-gui on my server.  When I execute query will get this message  AJAX error  Request rejected. (e.g. server not found, request blocked by browser addon, request redirected, internal server errors, etc.) Error-Code: SyntaxError: The URI is malformed. (0)  default ...'''
date = "2017-05-24T11:19:00Z"
lastmod = "2017-05-28T15:20:00Z"
weight = 56278
keywords = [ "overpassapi", "overpass-turbo" ]
aliases = [ "/questions/56278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ajax error when run query](/questions/56278/ajax-error-when-run-query)

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
<span id="post-56278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've installed osm3s, database and web-gui on my server.</p>
<p>When I execute query will get this message</p>
<pre><code>AJAX error 
Request rejected. (e.g. server not found, request blocked by browser addon, request redirected, internal server errors, etc.)
Error-Code: SyntaxError: The URI is malformed. (0)</code></pre>
<p>default server /suggest server : <a href="http://myIP/api/">http://myIP/api/</a></p>
<p>The firebug message:</p>
<pre><code>TypeError: D.a.osmLayer is undefined
t/D.a.handlers.onDone     http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:576458
e                     http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:250432
error                 http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:264950
c                     http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:22404
fireWith              http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:23221
n                     http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:69077
ajax                  http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:71685
v&lt;/this.run_query     http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:264247
Y&lt;/this.update_map/&lt;  http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:611455
Y&lt;/this.getQuery/&lt;    http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:587967
i/e.parse             http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:265884
Y&lt;/this.getQuery      http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:587649
Y&lt;/this.update_map    http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:611291
Y&lt;/this.onRunClick    http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:590491
dispatch              http://myIP/overpass-turbo/turbo.720be03cf00e831513e9.js:29:34146
add/g.handle</code></pre>
<p>No matter what I query when I click the button I will get this message. Is there any config or setting should I change?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '17, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/adb24ae063869f3b1c62e61672cf087b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ob9619&#39;s gravatar image" />
<p><span>ob9619</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ob9619 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '17, 03:04</strong> </span></p>
</div>
</div>
<div id="comments-container-56278" class="comments-container">
<span id="56337"></span>
<div id="comment-56337" class="comment">
<div id="post-56337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you see in firebug's network tab? Does the api request return a proper HTTP/200 answer?</p>
</div>
<div id="comment-56337-info" class="comment-info">
<span class="comment-age">(28 May '17, 11:17)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="56340"></span>
<div id="comment-56340" class="comment">
<div id="post-56340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It returned 304 even when it get png file on overpass server was show 304.However, it works smoothly on my chrome browser.</p>
</div>
<div id="comment-56340-info" class="comment-info">
<span class="comment-age">(28 May '17, 15:20)</span> <span class="comment-user userinfo">ob9619</span>
</div>
</div>
</div>
<div id="comment-tools-56278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56278-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

