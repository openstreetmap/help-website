+++
type = "question"
title = "Nominatim flatnode with negative id"
description = '''My company is using the Nominatim in the production environment with the entire planet dataset. When we import the database the flatnode file was enable to reduce the importing time and storage use. Now I tried to import custom POI, using osc file created by myself.  The POI in &quot;.osc&quot; file have nega...'''
date = "2018-07-11T19:53:00Z"
lastmod = "2018-07-12T02:17:00Z"
weight = 64662
keywords = [ "nominatim", "flatnode", "osmchange" ]
aliases = [ "/questions/64662" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim flatnode with negative id](/questions/64662/nominatim-flatnode-with-negative-id)

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
<span id="post-64662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64662-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My company is using the Nominatim in the production environment with the entire planet dataset. When we import the database the flatnode file was enable to reduce the importing time and storage use.</p>
<p>Now I tried to import custom POI, using osc file <a href="https://gist.github.com/gnosis7bit/383b340673749ad1d42631f8a8ddd41a">created by myself</a>.</p>
<p>The POI in ".osc" file have negatives OSM ID. When I executed the command, to import osc file:</p>
<p><strong><code>./update.php --import-diff teste.osc --index</code></strong></p>
<p>I got this message:</p>
<pre><code>Osm2pgsql failed due to ERROR: Flatnode store cannot save negative IDs.
ERROR: Error from osm2pgsql, 1
&#10;Error from osm2pgsql, 1</code></pre>
<p>My question: What is the impact in the Nominatim queries if I remove the constant CONST_Osm2pgsql_Flatnode_File from my config file.</p>
<p>I thought of re-importing the database without flatnode. Is it worth it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-flatnode" rel="tag" title="see questions tagged &#39;flatnode&#39;">flatnode</span> <span class="post-tag tag-link-osmchange" rel="tag" title="see questions tagged &#39;osmchange&#39;">osmchange</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '18, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1c276cd38b3a8114089732886a47d6d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnosis7&#39;s gravatar image" />
<p><span>gnosis7</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnosis7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64662" class="comments-container">
&#10;</div>
<div id="comment-tools-64662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64662-form-container" class="comment-form-container">
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

<span id="64663"></span>

<div id="answer-container-64663" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64663-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gnosis7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Importing the planet without a flatnode file is not recommended. It will be an order of magnitude slower.</p>
<p>However, you can try switching off the flatnode file after you have finished the planet import and before you update the database with your custom data. osm2pgsql should then use the Postgres database for storing the node information for your POIs and stop complaining about negative ids. In theory you should even be able to update the OSM data planet data with that method: switch on flatnodes when handling OSM osc, switch it off again when updating your own data.</p>
<p>If that really works in practise, I cannot say. It has never been tested to my knowledge. Nominatim might choke on negative OSM ids at some other point in the pipeline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '18, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-64663" class="comments-container">
<span id="64665"></span>
<div id="comment-64665" class="comment">
<div id="post-64665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Lonvia, thank you for your time. My application (front-end iOS and Android) make requests to the Nominatim API several times for minutes and I do not know when the requests are performed and they can not stop. Can you tell me the impact on these requests by turning off the flatnodes, importing my data and then turning on the flatnodes? And If I turn off the flatnodes permanently on my current Nominatim API? What could happen? Grateful</p>
</div>
<div id="comment-64665-info" class="comment-info">
<span class="comment-age">(11 Jul '18, 22:18)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
<span id="64666"></span>
<div id="comment-64666" class="comment">
<div id="post-64666-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The flatnode file is only used when importing or updating data. They are needed to compute the geometries, to be precise. Requests to your API are not affected at all if you switch them on and off.</p>
</div>
<div id="comment-64666-info" class="comment-info">
<span class="comment-age">(11 Jul '18, 22:26)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="64667"></span>
<div id="comment-64667" class="comment">
<div id="post-64667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You helped me a lot. Thanks!</p>
</div>
<div id="comment-64667-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 02:14)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
</div>
<div id="comment-tools-64663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64663-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64664"></span>

<div id="answer-container-64664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64664-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a similar requirement once, though relations, not nodes, and just one small country. It's possible to assign positive integers as long as they don't conflict with existing OSM ids. For example the current largest node id in OSM yesterday was 5,752,191,223. You could assign ids 100x, 1000x or 10000x times as high (depending how fast you believe OSM is growing). osm2pgsql supports 64bit integers and Nominatim's table schema uses BIGINT as well (<a href="https://www.postgresql.org/docs/9.6/static/datatype-numeric.html).">https://www.postgresql.org/docs/9.6/static/datatype-numeric.html).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '18, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-64664" class="comments-container">
<span id="64668"></span>
<div id="comment-64668" class="comment">
<div id="post-64668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your comment!</p>
</div>
<div id="comment-64668-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 02:17)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
</div>
<div id="comment-tools-64664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64664-form-container" class="comment-form-container">
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

