+++
type = "question"
title = "Why are streetcrossings not always splitted? Problems using the Data!"
description = '''Dear OSM Community. I´m trying to use the exported OSM Data and there are issues with the street crossings because they are differently defined and &quot;drawn&quot; in OSM. As an example what do I mean with different: A) Let´s take the crossing &quot;Goethestrasse&quot; / &quot;Dinghoferstrasse&quot; in &quot;Linz/Austria&quot;. Every st...'''
date = "2020-02-23T16:00:00Z"
lastmod = "2020-02-26T21:14:00Z"
weight = 73205
keywords = [ "crossing", "import", "nodes", "export", "data" ]
aliases = [ "/questions/73205" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why are streetcrossings not always splitted? Problems using the Data!](/questions/73205/why-are-streetcrossings-not-always-splitted-problems-using-the-data)

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
<span id="post-73205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OSM Community.</p>
<p>I´m trying to use the exported OSM Data and there are issues with the street crossings because they are differently defined and "drawn" in OSM.</p>
<p>As an example what do I mean with different:</p>
<p>A) Let´s take the crossing "Goethestrasse" / "Dinghoferstrasse" in "Linz/Austria". Every street stops in the middle of the crossing at the Node. So there are actually 4 Streets getting connected. So the Node is the connection point between the 4 streets.</p>
<p>[img]<a href="https://i.imgur.com/QNgfsgP.png?1">https://i.imgur.com/QNgfsgP.png?1</a> [/img]</p>
<p>B) Compared to that...now let´s look at "Schillerstrasse" / "Starhembergstrasse" in Linz/Austria. Schillerstrasse is passing right through the crossing. And so does "Starhembergstrasse". BUT there is a Node (!) in the middle. This Node is not defined as crossing and so the crossing CAN'T be identified.</p>
<p>[img]<a href="https://i.imgur.com/fQ3Ix4j.png">https://i.imgur.com/fQ3Ix4j.png</a> [/img]</p>
<p>Same with a T-junction. If 3 streets have a Node as connection = Perfect identification. 2 streets (1 street passing through the Node) = no identification.</p>
<p>I hope I make myself clear and I really need some advice how to "clean" the Data. I also would love to help OSM to develop... you guys a great!</p>
<p>Explanation of My project:</p>
<p>Help to develop a Street Import Mod for the Simulation Game Cities Skylines to improve traffic in my town by 1. Simulating the traffic accurately, 2. Applying road changes by trial/error, 3. Get in contact with the authorities.</p>
<p>Questions I´m asking in the CS Forum: <a href="https://steamcommunity.com/workshop/filedetails/discussion/1957515502/1744516325379783072/">https://steamcommunity.com/workshop/filedetails/discussion/1957515502/1744516325379783072/</a></p>
<ol>
<li><p>We can´t change every OSM Street so we can get a "perfect" Data in OSM, right? Or can we?</p></li>
<li><p>How can we identify and re-write the Data so the Crossings are all identified 100%?</p></li>
<li><p>After we identified them: How does the algorithm look like, so we can fix the Data?</p></li>
</ol>
<p>Or maybe we need to think more out of the box. Write a new Mode: "Every street crossing (even if there are different altitudes) must connect to a CS crossing." This would also connect the actual overpasses. But there are very few overpasses, right? Those can be corrected manually later on in the game fast.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '20, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8d20f4b7be33a5b3ce0b0a8147b52fc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexandler&#39;s gravatar image" />
<p><span>alexandler</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexandler has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '20, 16:06</strong> </span></p>
</div>
</div>
<div id="comments-container-73205" class="comments-container">
<span id="73214"></span>
<div id="comment-73214" class="comment">
<div id="post-73214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Same question on forum: <a href="https://forum.openstreetmap.org/viewtopic.php?id=68730">https://forum.openstreetmap.org/viewtopic.php?id=68730</a></p>
</div>
<div id="comment-73214-info" class="comment-info">
<span class="comment-age">(24 Feb '20, 08:04)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-73205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73205-form-container" class="comment-form-container">
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

<span id="73206"></span>

<div id="answer-container-73206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73206-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-73206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you man "crossroads" (or interections) where you say "crossings". Crossroads are not explicitly mapped in OSM; they are simply where several highway ways share a node. Your expectation that every situation should be mapped like your example "A" is simply wrong; it is the data consumer's task to infer these crossroads. Doing so is easy by looking at the node IDs that the various ways use; if several ways use a node with the same ID then there is a crossroads, otherwise there isn't - for example if there is a bridge or a tunnel, then even if the road going over another road should accidentally have a node in the same location it would be a node with a different ID.</p>
<p>No "fixing" in OSM is necessary; you just need to process the data correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '20, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73206" class="comments-container">
<span id="73210"></span>
<div id="comment-73210" class="comment">
<div id="post-73210-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Adding to Frederik's answer: There are a number of tools that will take OSM data and import it into GIS enabled databases splitting ways as needed to create a valid node and edge routing graph. The one I've worked with is osm2pgrouting but there are others.</p>
</div>
<div id="comment-73210-info" class="comment-info">
<span class="comment-age">(24 Feb '20, 02:28)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="73248"></span>
<div id="comment-73248" class="comment">
<div id="post-73248-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes I meant crossroads :)</p>
<p>Thank you very much for your response. I understand now that OSM is correctly working and the data needed to be procesed correctly. My appology.</p>
<p>And also thanks for giving the hint for osm2pgrouting.</p>
<p>All the best guys. You are great.</p>
</div>
<div id="comment-73248-info" class="comment-info">
<span class="comment-age">(26 Feb '20, 21:14)</span> <span class="comment-user userinfo">alexandler</span>
</div>
</div>
</div>
<div id="comment-tools-73206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73206-form-container" class="comment-form-container">
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

