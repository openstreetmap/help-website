+++
type = "question"
title = "Communication with offline OSM API with Wolfram Mathematica"
description = '''I am doing a supply chain optimization algorithm with Wolfram Mathematica. In this algorithm I am communicating with googlemaps API and providing it longitude and altitude coordinates, then I return the shortest distance between them for &quot;truck/car&quot; type vehicles. However googlemaps API has a daily ...'''
date = "2015-11-29T07:12:00Z"
lastmod = "2015-11-30T08:41:00Z"
weight = 46883
keywords = [ "party", "3rd", "algorithm", "software" ]
aliases = [ "/questions/46883" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Communication with offline OSM API with Wolfram Mathematica](/questions/46883/communication-with-offline-osm-api-with-wolfram-mathematica)

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
<span id="post-46883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46883-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am doing a supply chain optimization algorithm with Wolfram Mathematica. In this algorithm I am communicating with googlemaps API and providing it longitude and altitude coordinates, then I return the shortest distance between them for "truck/car" type vehicles. However googlemaps API has a daily limit 2500 requests. I want to use OSM API offline on my local computer. I found that I can do this by downloading the Europe OSM file and to use JOSM - JAVA openstreetmap editor to do this.</p>
<p>However, I did not find any information how to make a request to the editor from another software. Is it possible to do this, if yes how? is there any script example or plugin?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-party" rel="tag" title="see questions tagged &#39;party&#39;">party</span> <span class="post-tag tag-link-3rd" rel="tag" title="see questions tagged &#39;3rd&#39;">3rd</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span> <span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '15, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/61e048992e78d3ec65399605528e41a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValentasG&#39;s gravatar image" />
<p><span>ValentasG</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValentasG has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46883" class="comments-container">
<span id="46889"></span>
<div id="comment-46889" class="comment">
<div id="post-46889-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Crosspost: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=563588#p563588">http://forum.openstreetmap.org/viewtopic.php?pid=563588#p563588</a></p>
</div>
<div id="comment-46889-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 12:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46883-form-container" class="comment-form-container">
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

<span id="46884"></span>

<div id="answer-container-46884" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46884-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds like you are looking for an offline router. JOSM is an editor and although it has some routing plugins it is not really suitable for your job.</p>
<p>Instead take a look at the various <a href="https://wiki.openstreetmap.org/wiki/Routing#End_users:_Routing_software">routing solutions for OSM</a>. You should probably try a local <a href="https://wiki.openstreetmap.org/wiki/Open_Source_Routing_Machine">OSRM</a> or <a href="https://wiki.openstreetmap.org/wiki/GraphHopper">GraphHopper</a> installation. This has also already been answered in <a href="/questions/46873/limits-per-day-problem-supply-chain-optimization-algorithm">your previous question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '15, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Nov '15, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-46884" class="comments-container">
<span id="46887"></span>
<div id="comment-46887" class="comment">
<div id="post-46887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response. I check GraphHooper, however I did not understand precisely the software usage. Is it possible to use it offline without an API key? The API key can provide only 500 requests as I understood for a free user? Also, how the GraphHoper should communicate with Wolfram Mathematica? Can I create a HTTP API and connect to it with wolfram (similar like I did with googlemaps API)? Or I need a script that allows Wolfram to communicate with native Java applications?</p>
<p>I think these questions are important, regarding witch software I decide to use OSRM or GraphHopper.</p>
</div>
<div id="comment-46887-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 10:56)</span> <span class="comment-user userinfo">ValentasG</span>
</div>
</div>
<span id="46890"></span>
<div id="comment-46890" class="comment">
<div id="post-46890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The crossposting / question duplication here suggests that there's a bit of communications failure here (not surprising, because if someone's coming from an API-centric "you must use our services and all your data are belong to us" world then how would they know that another world exists?).</p>
<p>Perhaps it would be helpful to take a bit of a step back, and ask a few more general questions on the #osm IRC channel? That way you can get more of a feeling for what OSM "is" rather than making assumptions based only on other geo providers...</p>
</div>
<div id="comment-46890-info" class="comment-info">
<span class="comment-age">(29 Nov '15, 12:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46897"></span>
<div id="comment-46897" class="comment">
<div id="post-46897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11730/valentasg">@ValentasG</a> GraphHopper is open source (well, except for some advanced services like its Geocoder) so there is no need for an API key if you run your own instance. Your other questions seem too broad to be answered on help.openstreetmap.org.</p>
</div>
<div id="comment-46897-info" class="comment-info">
<span class="comment-age">(30 Nov '15, 08:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46884-form-container" class="comment-form-container">
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

