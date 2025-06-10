+++
type = "question"
title = "How to use geocodeArea: instead of bbox in an overpass-turbo query ?"
description = '''Hi, I&#x27;d like to run this query  way[building]({{bbox}})-&amp;gt;.a; foreach .a (  way.a(around:400);  way._(if:count(ways) == 1);  out center; ); I found here but using {{geocodeArea:&quot;Burlats&quot;}} or {{geocodeArea:&quot;Boissezon&quot;}} or {{geocodeArea:&quot;Noailhac&quot;}} instead of the {{bbox}}parameter....It seems I&#x27;m...'''
date = "2017-11-30T20:56:00Z"
lastmod = "2017-12-01T11:42:00Z"
weight = 60909
keywords = [ "building", "query", "overpass-turbo" ]
aliases = [ "/questions/60909" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use geocodeArea: instead of bbox in an overpass-turbo query ?](/questions/60909/how-to-use-geocodearea-instead-of-bbox-in-an-overpass-turbo-query)

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
<span id="post-60909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'd like to run this query</p>
<p><code>way[building]({{bbox}})-&gt;.a; foreach .a ( way.a(around:400); way._(if:count(ways) == 1); out center; );</code></p>
<p>I found <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Isolated_Buildings">here</a> but using <code>{{geocodeArea:"Burlats"}}</code> or <code>{{geocodeArea:"Boissezon"}}</code> or <code>{{geocodeArea:"Noailhac"}}</code> instead of the <code>{{bbox}}</code>parameter....It seems I'm doing something wrong because</p>
<p><code>way[building]({{geocodeArea:"Boissezon"}})-&gt;.a; foreach .a ( way.a(around:400); way._(if:count(ways) == 1); out center; );</code> just get me a syntax error message :)</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '17, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/bdcfe65b8bf0685f36b5f04ba0572875?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Serpico&#39;s gravatar image" />
<p><span>Serpico</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Serpico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60909" class="comments-container">
&#10;</div>
<div id="comment-tools-60909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60909-form-container" class="comment-form-container">
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

<span id="60917"></span>

<div id="answer-container-60917" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60917-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Overpass Turbo shortcut <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo/Extended_Overpass_Turbo_Queries#Available_Shortcuts">replaces the geocodeArea with an area query</a>, which is not valid syntax for specifying the area in the way query.</p>
<p>The fix is to save the area result to a set first:</p>
<pre><code>{{geocodeArea:&quot;Boissezon&quot;}}-&gt;.searchArea;
way[building](area.searchArea)-&gt;.a;
foreach .a (
  way.a(around:400);
  way._(if:count(ways) == 1);
  out center;
);</code></pre>
<p>An easy way to recall the structure of such queries is to put something like <code>amenity=* in Toledo</code> into the Wizard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '17, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-60917" class="comments-container">
&#10;</div>
<div id="comment-tools-60917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60917-form-container" class="comment-form-container">
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

