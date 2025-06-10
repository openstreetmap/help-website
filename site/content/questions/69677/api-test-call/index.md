+++
type = "question"
title = "API test call"
description = '''Trying to get this to work in the test environment and keep getting connection failure. Is there a test API for Geocoding with http? &amp;lt;cfhttp method=&quot;get&quot; url=&quot;https://nominatim.openstreetmap.org/search?city=oxford,&amp;amp;amp;country=New Zealand&amp;amp;amp;format=geojson&quot; getasbinary=&quot;never&quot;&amp;gt;  &amp;lt;c...'''
date = "2019-06-20T02:51:00Z"
lastmod = "2019-07-08T15:25:00Z"
weight = 69677
keywords = [ "test", "coldfusion", "api", "call" ]
aliases = [ "/questions/69677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [API test call](/questions/69677/api-test-call)

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
<span id="post-69677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69677-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Trying to get this to work in the test environment and keep getting connection failure. Is there a test API for Geocoding with http?</p>
<p>&lt;cfhttp method="get" url="https://nominatim.openstreetmap.org/search?city=oxford,&amp;amp;country=New Zealand&amp;amp;format=geojson" getasbinary="never"&gt; &lt;cfoutput&gt; &lt;cfdump var="#cfhttp.filecontent#"&gt; &lt;/cfoutput&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-test" rel="tag" title="see questions tagged &#39;test&#39;">test</span> <span class="post-tag tag-link-coldfusion" rel="tag" title="see questions tagged &#39;coldfusion&#39;">coldfusion</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-call" rel="tag" title="see questions tagged &#39;call&#39;">call</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '19, 02:51</strong></p>
<img src="https://secure.gravatar.com/avatar/22eb061ab863f91b06a11ec653d27102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LoganOSM&#39;s gravatar image" />
<p><span>LoganOSM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LoganOSM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69677" class="comments-container">
<span id="69892"></span>
<div id="comment-69892" class="comment">
<div id="post-69892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do I create User-Agent identifying the application so API call will work?</p>
</div>
<div id="comment-69892-info" class="comment-info">
<span class="comment-age">(05 Jul '19, 15:13)</span> <span class="comment-user userinfo">LoganOSM</span>
</div>
</div>
<span id="69896"></span>
<div id="comment-69896" class="comment">
<div id="post-69896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How will depend on how you're making the https call. Is that via a web framework for a particular environment or language, or something else?</p>
<p>Edit: Richard has spotted that you're using Cold Fusion - best to follow his suggestion.</p>
</div>
<div id="comment-69896-info" class="comment-info">
<span class="comment-age">(05 Jul '19, 16:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69931"></span>
<div id="comment-69931" class="comment">
<div id="post-69931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>User-agent still not working. Can I provide an IP address to you to be granted permission? Or do you have one sample call that uses address to obtain lat/lng in geocode that does not require useragent or valid HTTP referer?</p>
</div>
<div id="comment-69931-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 15:25)</span> <span class="comment-user userinfo">LoganOSM</span>
</div>
</div>
</div>
<div id="comment-tools-69677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69677-form-container" class="comment-form-container">
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

<span id="69679"></span>

<div id="answer-container-69679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Read the Nominatim usage policy:</p>
<p><a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a></p>
<p>You need to "Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agents as set by http libraries will not do)". If you do not, then it's very likely your requests will be blocked.</p>
<p>(Learning how to set a user-agent in ColdFusion is outwith the scope of this help site and you'd probably need to ask on a ColdFusion support site.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '19, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69679" class="comments-container">
&#10;</div>
<div id="comment-tools-69679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69679-form-container" class="comment-form-container">
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

