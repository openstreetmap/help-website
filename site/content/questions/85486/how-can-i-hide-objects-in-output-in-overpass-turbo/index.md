+++
type = "question"
title = "How can I hide objects in output in Overpass Turbo?"
description = '''I am querying objects with Overpass Turbo, which are restricted to a specific area. I restrict the query via a relation, in this case a city boundary. Then I map them to the area to query via map_to_area My problem is that the output always contains the relation itself, but I don&#x27;t need it. It also ...'''
date = "2022-08-30T08:37:00Z"
lastmod = "2022-08-30T22:03:00Z"
weight = 85486
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/85486" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I hide objects in output in Overpass Turbo?](/questions/85486/how-can-i-hide-objects-in-output-in-overpass-turbo)

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
<span id="post-85486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am querying objects with Overpass Turbo, which are restricted to a specific area.<br />
I restrict the query via a relation, in this case a city boundary. Then I map them to the area to query via <code>map_to_area</code></p>
<p>My problem is that the output always contains the relation itself, but I don't need it. It also is displayed on top of all nodes, so that I cannot see the nodes and ways in overpass turbo, but only the relation (see screenshot below).</p>
<p>Can I somehow suppress the relation in the output (both the map and the JSON)?</p>
<p>Here's my example. I would like to just have the nodes and ways.</p>
<p><code>[out:json][timeout:25]; ( {{plz=40589}} rel[postal_code="{{plz}}"]; map_to_area; node["power"="generator"]["generator:method"="photovoltaic"](area); way["power"="generator"]["generator:method"="photovoltaic"](area); ); (._;&gt;;); out body; out count;</code></p>
<p><a href="https://i.stack.imgur.com/trVw7.jpg"><img src="https://i.stack.imgur.com/trVw7.jpg" alt="Screenshot of Overpass Turbo&#39;s map view with a relation shown as area, which hides all nodes and ways which are also in the output. in the bottom right corner, it says &quot;loaded Nodes: 424, ways: 24, relations: 1, areas 1&quot;" /></a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '22, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/3df83952dc426143757b8891f68bfbfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guerda&#39;s gravatar image" />
<p><span>guerda</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guerda has no accepted answers">0%</span> </br></p>
</img>
</div>
</div>
<div id="comments-container-85486" class="comments-container">
&#10;</div>
<div id="comment-tools-85486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85486-form-container" class="comment-form-container">
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

<span id="85489"></span>

<div id="answer-container-85489" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85489-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="guerda has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First off - there are no power generators in the area you're searching.</p>
<p><a href="https://overpass-turbo.eu/s/1ltI">https://overpass-turbo.eu/s/1ltI</a></p>
<p>So let's use an adjacent post code.</p>
<p>The problem was the inclusion of the area inside the union using curved brackets:</p>
<pre><code>rel[postal_code=40599];map_to_area;
(
 node[power=generator][&quot;generator:method&quot;=photovoltaic](area);
  way[power=generator][&quot;generator:method&quot;=photovoltaic](area);
);
(._;&gt;;);
out body;
out count;</code></pre>
<p>However these can be removed entirely by amalgamating the objects to search for (nw):</p>
<pre><code>rel[postal_code=40599];map_to_area;
nw[power=generator][&quot;generator:method&quot;=photovoltaic](area);
(._;&gt;;);
out body;
out count;</code></pre>
<p><a href="https://overpass-turbo.eu/s/1ltK">https://overpass-turbo.eu/s/1ltK</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '22, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '22, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-85489" class="comments-container">
<span id="85498"></span>
<div id="comment-85498" class="comment">
<div id="post-85498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like your solution works. My original code seems not to work indeed. Thank you for that!</p>
</div>
<div id="comment-85498-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 17:18)</span> <span class="comment-user userinfo">guerda</span>
</div>
</div>
<span id="85499"></span>
<div id="comment-85499" class="comment">
<div id="post-85499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As soon as I use variables, my queries return different results, interesting.</p>
</div>
<div id="comment-85499-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 17:20)</span> <span class="comment-user userinfo">guerda</span>
</div>
</div>
<span id="85508"></span>
<div id="comment-85508" class="comment">
<div id="post-85508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Show us the code.</p>
</div>
<div id="comment-85508-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 22:03)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-85489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85489-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85488"></span>

<div id="answer-container-85488" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85488-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just remove the relation from the output set:</p>
<pre><code>[out:json][timeout:25];
&#10;  {{plz=40599}}
  rel[postal_code=&quot;{{plz}}&quot;];
  map_to_area;
(
  node[&quot;power&quot;=&quot;generator&quot;][&quot;generator:method&quot;=&quot;photovoltaic&quot;](area);
  way[&quot;power&quot;=&quot;generator&quot;][&quot;generator:method&quot;=&quot;photovoltaic&quot;](area);
);
(._;&gt;;);
out body;
out count;</code></pre>
<p>The parentheses are interpreted as the "union" operator: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Union</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '22, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85488" class="comments-container">
<span id="85497"></span>
<div id="comment-85497" class="comment">
<div id="post-85497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I thought it would be the solution. It seems that with other postcode it does not work at all. 40667 contains ~20 generators, but it does not return any with your code. That is odd. Any idea? <a href="https://overpass-turbo.eu/s/1lum">https://overpass-turbo.eu/s/1lum</a></p>
</div>
<div id="comment-85497-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 17:14)</span> <span class="comment-user userinfo">guerda</span>
</div>
</div>
</div>
<div id="comment-tools-85488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85488-form-container" class="comment-form-container">
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

