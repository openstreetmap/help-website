+++
type = "question"
title = "get around ways - more data"
description = '''I&#x27;m trying to get the ways around me using this API query: (overpass-turbo.au) &amp;lt;query type=&quot;way&quot;&amp;gt;  &amp;lt;around lat=&quot;52.002362&quot; lon=&quot;-1.271373&quot; radius=&quot;20&quot;/&amp;gt;  &amp;lt;has-kv k=&quot;highway&quot;/&amp;gt; &amp;lt;/query&amp;gt; &amp;lt;union&amp;gt; &amp;lt;item/&amp;gt;  &amp;lt;recurse type=&quot;down&quot;/&amp;gt; &amp;lt;/union&amp;gt; &amp;lt;print/&amp;gt;  It...'''
date = "2017-10-22T10:39:00Z"
lastmod = "2017-10-24T10:16:00Z"
weight = 60210
keywords = [ "ways", "overpass", "api" ]
aliases = [ "/questions/60210" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get around ways - more data](/questions/60210/get-around-ways-more-data)

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
<span id="post-60210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60210-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get the ways around me using this API query: (overpass-turbo.au)</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;
    &lt;around lat=&quot;52.002362&quot; lon=&quot;-1.271373&quot; radius=&quot;20&quot;/&gt;
 &lt;has-kv k=&quot;highway&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;  &lt;item/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
<p>Its returns data but i want to get more nodes, in this example more of road M40 so I can reduce the API calls. is it possible using this query with other parameters or by query for the specific road (M40) by another API call?</p>
<p>Thnak's</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '17, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/663a45374a1761302899764bb54aac8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alto&#39;s gravatar image" />
<p><span>alto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60210" class="comments-container">
<span id="60236"></span>
<div id="comment-60236" class="comment">
<div id="post-60236-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is there any reason you're looking for an API for this? Why not just download the data that you are interested in, load it into a database and query that?</p>
</div>
<div id="comment-60236-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 12:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60237"></span>
<div id="comment-60237" class="comment">
<div id="post-60237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm working on a POC application that need to know ahead the road I'm on it. The DB can't be downloaded to the mobile device - too big. For now I'm using the public (overpass-turbo.au) API server, but in the moment it will work, I'll use my own servers for that of course.</p>
</div>
<div id="comment-60237-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 12:22)</span> <span class="comment-user userinfo">alto</span>
</div>
</div>
<span id="60238"></span>
<div id="comment-60238" class="comment">
<div id="post-60238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can't the mobile app contact an app server of yours? Then it can do any query it wants and not be limited by a third-party API (which you presumably don't have an SLA for).</p>
</div>
<div id="comment-60238-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 12:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60239"></span>
<div id="comment-60239" class="comment not_top_scorer">
<div id="post-60239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure, that the plan, after I'll see that it's working. For now it's simple to work with the public API servers than build my own servers. Time to market and proof of concept first :)</p>
</div>
<div id="comment-60239-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 12:38)</span> <span class="comment-user userinfo">alto</span>
</div>
</div>
<span id="60240"></span>
<div id="comment-60240" class="comment">
<div id="post-60240-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just be careful you don't get into <a href="https://xkcd.com/1150/">https://xkcd.com/1150/</a> territory :)</p>
</div>
<div id="comment-60240-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 12:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60256"></span>
<div id="comment-60256" class="comment">
<div id="post-60256-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14342/alto">@alto</a>: what do you think of apps such as OsmAnd, maps.me, Magic Earth, etc. They all put a database on a mobile device. That database contains streets, addresses, POIs, opening hours, etc. and information to render, navigate and search. They do not put the whole world on your device, but allow you to download the country/state/provinces of interest. No need to pay for mobile data.</p>
</div>
<div id="comment-60256-info" class="comment-info">
<span class="comment-age">(24 Oct '17, 04:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="60261"></span>
<div id="comment-60261" class="comment not_top_scorer">
<div id="post-60261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>: totally correct, I even uses some of them but as I said, for now I'm working on POC project only, it's easier to work for now with public API. in the feature, if this project will became something 'real', we'll have to decide how to set/get the data, I assume that its will be online also, but from our servers, since the all app needs to be online and it's a lot of data to download if you don't know the exact area you going to be on and you have to remember to do it before going there...</p>
<p>Its all depend on the usage and business model of the app.</p>
</div>
<div id="comment-60261-info" class="comment-info">
<span class="comment-age">(24 Oct '17, 10:16)</span> <span class="comment-user userinfo">alto</span>
</div>
</div>
</div>
<div id="comment-tools-60210" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60210-form-container" class="comment-form-container">
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

<span id="60234"></span>

<div id="answer-container-60234" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After looking more into the api: Its shame there is no straight way to get the all parts of the road by some part of it, it's will be much easier. I found a way to do it, but with some work:</p>
<ol>
<li>query again the overpass api by the name &amp; ref that I get from the first query, e.g: <a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D%5Btimeout:25%5D;(node%5B">http://overpass-api.de/api/interpreter?data=[out:json][timeout:25];(node["name"="John</a> F Foran Freeway"]["ref"="I 280"];way["name"="John F Foran Freeway"]["ref"="I 280"];relation["name"="John F Foran Freeway"]["ref"="I 280"];);out;&gt;;out skel qt;</li>
<li>get all way nodes from the result json and merge them to one list of points, need some work since you need to pass each of the items and find the next one by compare each the last and the first points.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '17, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/663a45374a1761302899764bb54aac8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alto&#39;s gravatar image" />
<p><span>alto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60234" class="comments-container">
&#10;</div>
<div id="comment-tools-60234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60234-form-container" class="comment-form-container">
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

