+++
type = "question"
title = "How to get tram stops and lines (routes)"
description = '''Hi! I am new to OSM and I am trying to get tram stops and lines using overpass turbo but with no luck. What I did was writing this code: &amp;lt;osm-script&amp;gt;  &amp;lt;query type=&quot;node&quot;&amp;gt;  &amp;lt;has-kv k=&quot;railway&quot; v=&quot;tram_stop&quot;/&amp;gt;  &amp;lt;bbox-query {{bbox}}=&quot;&quot;/&amp;gt;  &amp;lt;/query&amp;gt;  &amp;lt;print limit=&quot;&quot; mode=...'''
date = "2014-10-09T15:59:00Z"
lastmod = "2014-10-10T19:14:00Z"
weight = 37461
keywords = [ "tram", "line", "stop", "tramway" ]
aliases = [ "/questions/37461" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get tram stops and lines (routes)](/questions/37461/how-to-get-tram-stops-and-lines-routes)

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
<span id="post-37461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am new to OSM and I am trying to get tram stops and lines using overpass turbo but with no luck. What I did was writing this code:</p>
<p>&lt;osm-script&gt; &lt;query type="node"&gt; &lt;has-kv k="railway" v="tram_stop"/&gt; &lt;bbox-query {{bbox}}=""/&gt; &lt;/query&gt; &lt;print limit="" mode="body" order="id"/&gt; &lt;/osm-script&gt;</p>
<p>But what it does is only showing all tram stops. What I need is:</p>
<ol>
<li>Getting all tram lines with their stops and only in one way.</li>
<li>Getting all lines tram stops in one way together but without doubling tram stops that are mutual/common for some tram lines.</li>
</ol>
<p>Of course those should be independent queries.</p>
<p>May someone help me or guide me? I did some other queries using overpass turbo wiki but to no avail.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tram" rel="tag" title="see questions tagged &#39;tram&#39;">tram</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-tramway" rel="tag" title="see questions tagged &#39;tramway&#39;">tramway</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '14, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d56191ad19135b7cd08abe5883e677ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yamet&#39;s gravatar image" />
<p><span>yamet</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yamet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '14, 16:34</strong> </span></p>
</div>
</div>
<div id="comments-container-37461" class="comments-container">
<span id="37477"></span>
<div id="comment-37477" class="comment">
<div id="post-37477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean by 'only in one way'? Can you give some concrete example with actual relations?<br />
Btw: there are plenty of overpass api threads around here. Did you already take a look at some of them involving 'rel' and '&gt;&gt;'?</p>
</div>
<div id="comment-37477-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 06:17)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="37498"></span>
<div id="comment-37498" class="comment">
<div id="post-37498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you have tram line from point A to B, there are almost always two lines for trams going one way and backwards. So almost everywhere where trains stops there are two tram stops, one for trams going forth and one for trams going backwards. I would like to stick to overpass turbo to visualise the result so I was not checking other overpass API's.</p>
</div>
<div id="comment-37498-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 15:33)</span> <span class="comment-user userinfo">yamet</span>
</div>
</div>
</div>
<div id="comment-tools-37461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37461-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="37464"></span>

<div id="answer-container-37464" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37464-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>please look at the anwers to this question: <a href="https://help.openstreetmap.org/questions/37216/how-to-download-data-bus-stations-with-locations-poi">https://help.openstreetmap.org/questions/37216/how-to-download-data-bus-stations-with-locations-poi</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '14, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span> </br></p>
</div>
</div>
<div id="comments-container-37464" class="comments-container">
<span id="37465"></span>
<div id="comment-37465" class="comment">
<div id="post-37465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This solution doesn't download routes, only stops and platforms.</p>
</div>
<div id="comment-37465-info" class="comment-info">
<span class="comment-age">(09 Oct '14, 17:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37502"></span>
<div id="comment-37502" class="comment">
<div id="post-37502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Escada thanks for help! Unfortunately this is not answer to my question. My query already displays tram stops. Do you know maybe what should I add to additionally display tram route?</p>
</div>
<div id="comment-37502-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 16:08)</span> <span class="comment-user userinfo">yamet</span>
</div>
</div>
</div>
<div id="comment-tools-37464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37464-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37505"></span>

<div id="answer-container-37505" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37505-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-37505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this one <a href="http://overpass-turbo.eu/s/5pa,">http://overpass-turbo.eu/s/5pa,</a> it's based upon an <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo/Examples#Part_of_a_.28route.29_relation">example</a> for part of a hiking route. That same page also has an example for the complete route, but then you have to specify the name or ref of the route</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '14, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-37505" class="comments-container">
&#10;</div>
<div id="comment-tools-37505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37505-form-container" class="comment-form-container">
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

