+++
type = "question"
title = "Is there an OSM routing API?"
description = '''Dear OpenStreetMap support, I represent a start-up project called WayLinker (www.waylinker.com). We use web maps to help car and truck drivers find passengers of cargo around the country. I would like to know whether it is possible to build our service around OSM. Can we create a PHP service via OSM...'''
date = "2011-08-25T17:42:00Z"
lastmod = "2011-08-26T18:49:00Z"
weight = 7313
keywords = [ "development", "api", "routing" ]
aliases = [ "/questions/7313" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an OSM routing API?](/questions/7313/is-there-an-osm-routing-api)

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
<span id="post-7313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7313-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OpenStreetMap support,</p>
<p>I represent a start-up project called WayLinker (www.waylinker.com). We use web maps to help car and truck drivers find passengers of cargo around the country. I would like to know whether it is possible to build our service around OSM. Can we create a PHP service via OSM API that would address OSM with Route Start and route End coordinates and in return receive a fastest/shortest route?</p>
<p>I have looked through the wiki, but haven't found examples of an external routing API. Can you please clarify this topic ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '11, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/bddb0c4e9324bba3133c555b70706838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey%20Mazur&#39;s gravatar image" />
<p><span>Andrey Mazur</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey Mazur has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '13, 22:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-7313" class="comments-container">
&#10;</div>
<div id="comment-tools-7313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7313-form-container" class="comment-form-container">
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

<span id="7319"></span>

<div id="answer-container-7319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7319-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's an overview about routing with OSM on the wiki page <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a>. You will be interested specifically in the list of <a href="http://wiki.openstreetmap.org/wiki/Routing/OnlineRouters">Online Routers</a>. There is a comparison of several services at the bottom of the page, check out the row "API open for 3rd party applications" to find some that might be suitable for you.</p>
<p>None of these routing services is operated by OpenStreetMap directly; they are all using OpenStreetMap data but are operated by third parties. There may be usage restrictions if you are planning to use them heavily, and you might be forced to run your own server or pay for a commercial service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7319" class="comments-container">
&#10;</div>
<div id="comment-tools-7319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7318"></span>

<div id="answer-container-7318" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7318-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM servers keep map data, not routing. If you want a routing service based on OSM see <a href="http://wiki.openstreetmap.org/wiki/Routing/online_routers">online_routers</a>. For cars only YOURS and MapQuest seem to have a public API for routing.<br />
Based on the scale you plan to do this you might consider running your own server. Most of the routers mentioned on wiki is open source so you would not have to program your own routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '11, 18:36</strong> </span></p>
</div>
</div>
<div id="comments-container-7318" class="comments-container">
<span id="7352"></span>
<div id="comment-7352" class="comment">
<div id="post-7352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks everyone. But all the solutions mentioned above seem to give a 3-rd party API that integrates the map in to the web site and gives us an ability to use various functions inside the map itself. Yet what we need is an API that can work via HTTP requests much like this -&gt; <a href="http://code.google.com/apis/maps/documentation/directions/">http://code.google.com/apis/maps/documentation/directions/</a> . The thing is that Google does not provide direction services to a large number of countries, for instance Russia.</p>
<p>So can someone tell me is there any http based API like Google has ?</p>
<p>Thank you in advance for all your answers.</p>
</div>
<div id="comment-7352-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 18:20)</span> <span class="comment-user userinfo">Andrey Mazur</span>
</div>
</div>
<span id="7353"></span>
<div id="comment-7353" class="comment">
<div id="post-7353-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looking at <a href="http://wiki.openstreetmap.org/wiki/YOURS#API_documentation">API documentation of YOURS</a> and more specifically the <a href="http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&amp;flat=52.215676&amp;flon=5.963946&amp;tlat=52.2573&amp;tlon=6.1799&amp;v=motorcar&amp;fast=1&amp;layer=mapnik">example</a> the response contains the nodes. This seems to me exactly what Google does, only the coordinates encoding is xml, not JSON. I doubt you get anything better...<br />
PS: if you use their service buy them some RAM to get faster response ;-)</p>
</div>
<div id="comment-7353-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 18:49)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7318-form-container" class="comment-form-container">
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

