+++
type = "question"
title = "Overpass API - combine types ?!?"
description = '''Hi there, I have a problem to understand how the API works. These two lines work well: wget -c http://api.openstreetmap.fr/xapi?&quot;node[waterway=wreck][bbox=-27,29,44,72]&quot; -O EU_Wrecks-1.osm wget -c http://api.openstreetmap.fr/xapi?&quot;node[historic=wreck][bbox=-27,29,44,72]&quot; -O EU_Wrecks-2.osm  But when...'''
date = "2017-04-26T13:51:00Z"
lastmod = "2017-04-26T19:11:00Z"
weight = 55888
keywords = [ "overpassapi", "overpass", "overpass-api" ]
aliases = [ "/questions/55888" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API - combine types ?!?](/questions/55888/overpass-api-combine-types)

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
<span id="post-55888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I have a problem to understand how the API works.</p>
<p>These two lines work well:</p>
<pre><code>wget -c http://api.openstreetmap.fr/xapi?&quot;node[waterway=wreck][bbox=-27,29,44,72]&quot; -O EU_Wrecks-1.osm
wget -c http://api.openstreetmap.fr/xapi?&quot;node[historic=wreck][bbox=-27,29,44,72]&quot; -O EU_Wrecks-2.osm</code></pre>
<p>But when I try to combine them it doesn't:</p>
<pre><code>wget -c http://api.openstreetmap.fr/xapi?&quot;node[waterway|historic=wreck][bbox=-27,29,44,72]&quot; -O EU_Wrecks.osm</code></pre>
<p>Any hints for me? Tnx...</p>
<p>PS: Seems it worked once: <a href="https://wiki.openstreetmap.org/wiki/User:Sparcuser">https://wiki.openstreetmap.org/wiki/User:Sparcuser</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '17, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/7f0d4ab72636e20e081dec5023ada411?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeriMapper&#39;s gravatar image" />
<p><span>MeriMapper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeriMapper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '17, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-55888" class="comments-container">
&#10;</div>
<div id="comment-tools-55888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55888-form-container" class="comment-form-container">
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

<span id="55889"></span>

<div id="answer-container-55889" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55889-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Rather than "node[waterway|historic=wreck]" you need to do something like "(node["waterway"="wreck"];node["historic"="wreck"];);"</p>
<p>Also note that the wizard of <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> can be very helpful for figuring out what works</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '17, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55889" class="comments-container">
<span id="55892"></span>
<div id="comment-55892" class="comment">
<div id="post-55892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer!</p>
<p>I tried wget -c <a href="http://api.openstreetmap.fr/xapi?">http://api.openstreetmap.fr/xapi?"(node["waterway"="wreck"];node["historic"="wreck"];);[bbox=-27,29,44,72]"</a> -O EU_Wrecks.osm and got ERROR 400: Bad Request.</p>
<p>When I send only the http part in my broser I get:</p>
<p>Error in ["(node["waterway"="wreck"];node["historic"="wreck"];)]: Error: Query must start with 'node', 'way', 'relation', or '*'</p>
<p>Tested with dozends of variants with or without brackets, quotes, ... :-P</p>
</div>
<div id="comment-55892-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 17:15)</span> <span class="comment-user userinfo">MeriMapper</span>
</div>
</div>
<span id="55894"></span>
<div id="comment-55894" class="comment">
<div id="post-55894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the Overpass Turbo wizard mentioned above I wrote "type:node &amp; (waterway=wreck | historic=wreck)", which it then translates to QL code.</p>
<p>(when tested from inside JOSM the result is a bit different)</p>
<p>What I'm not at all sure about here is how to transform the result into something that will fit into a commandline string like yours</p>
</div>
<div id="comment-55894-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 19:11)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
</div>
<div id="comment-tools-55889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55889-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55893"></span>

<div id="answer-container-55893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55893-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Overpass server implements an XAPI compatibility layer. I don't know it well, it may not support the combined query.</p>
<p>You can use the Overpass QL to do the query though, I think Hjart has written their answer in the QL. Here's the query in Overpass Turbo:</p>
<p><a href="http://overpass-turbo.eu/s/oDz">http://overpass-turbo.eu/s/oDz</a></p>
<p>(Click "Run" to see the output)</p>
<p>Under "Export" there is a link "raw data directly from Overpass API" that is suitable for use with wget.</p>
<p>The query language is documented here: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '17, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '17, 17:51</strong> </span></p>
</div>
</div>
<div id="comments-container-55893" class="comments-container">
&#10;</div>
<div id="comment-tools-55893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55893-form-container" class="comment-form-container">
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

