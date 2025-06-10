+++
type = "question"
title = "How to use OSRM"
description = '''I&#x27;m a bit lost with the OSRM documentation. Do you have to set up a web server after you have installed it? How to you actually use OSRM once it is installed? I&#x27;m totally new to this, so if someone could break it down kindergarden style, I would appreciate it. I&#x27;m trying to host an offline OSM serve...'''
date = "2013-06-26T05:43:00Z"
lastmod = "2013-06-27T01:57:00Z"
weight = 23715
keywords = [ "osrm", "osm" ]
aliases = [ "/questions/23715" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use OSRM](/questions/23715/how-to-use-osrm)

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
<span id="post-23715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a bit lost with the OSRM documentation. Do you have to set up a web server after you have installed it? How to you actually use OSRM once it is installed? I'm totally new to this, so if someone could break it down kindergarden style, I would appreciate it.</p>
<p>I'm trying to host an offline OSM server, and allow people to use it to create routes on a private network. What would the primary install pieces be, aside from OSM and OSRM?</p>
<p>Thanks, sorry for the newbie questions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '13, 05:43</strong></p>
<img src="https://secure.gravatar.com/avatar/43a9c8a6e33c0ac041744f174523d59d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjmil03&#39;s gravatar image" />
<p><span>jjmil03</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjmil03 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23715" class="comments-container">
&#10;</div>
<div id="comment-tools-23715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23715-form-container" class="comment-form-container">
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

<span id="23718"></span>

<div id="answer-container-23718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23718-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-23718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming you've already prepared the data with osrm-extract and osrm-prepare. When you then run osrm-routed, OSRM starts up its own server; you don't need to provide a further server. By default this listens for requests on port 5000, though you probably want to change this if you're deploying a public instance.</p>
<p>This server simply provides an API where you can send correctly formatted requests to <a href="http://your.routing.server:5000/viaroute.">http://your.routing.server:5000/viaroute.</a> OSRM will reply with the route in JSON. The exact details of the request and response formats are documented on the <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Server-api">OSRM wiki</a>.</p>
<p>If you want to provide a graphical frontend, allowing users to create routes by entering placenames or clicking points, you'll need to either implement this yourself, or use <a href="https://github.com/DennisSchiefer/Project-OSRM-Web">Project-OSRM-Web</a>. The latter provides the interface you see at <a href="http://map.project-osrm.org/">map.project-osrm.org</a>. (Note that this is licensed as AGPL, which is quite aggressive for a frontend project, so you may choose - like me - to develop your own on top of Leaflet instead.)</p>
<p>If routing is your only concern, you don't need to set up an OSM server (using the osm.org Rails code) at all. You can simply use third-party tiles for the background map (with the usual proviso that you abide by their usage policy), and download a planet extract from <a href="http://download.geofabrik.de/">Geofabrik</a> for the data which OSRM consumes.</p>
<p>Hope this answers your question, but feel free to post follow-up comments if anything is not clear.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '13, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23718" class="comments-container">
<span id="23726"></span>
<div id="comment-23726" class="comment">
<div id="post-23726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also wanted to serve it out with a WMS server. Still need to find out what format I would have to convert to, if any, or if this particular WMS server can serve OSM. Thanks for the answer....the OSRM wiki either isn't all that user friendly, or it's just me trying to find info in it...</p>
<p>Jon</p>
</div>
<div id="comment-23726-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 13:01)</span> <span class="comment-user userinfo">jjmil03</span>
</div>
</div>
</div>
<div id="comment-tools-23718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23718-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23736"></span>

<div id="answer-container-23736" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23736-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just found out about OSRM from this question so take this answer with a little salt. I'm not sure if you found it but they have a page on <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Running-OSRM">building/installing the server</a>. It sounds like once you install it you also need .osm data files which can be downloaded from a <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">variety of places</a>. If you still need help I would recommend contacting their <a href="http://lists.openstreetmap.org/listinfo/osrm-talk">mailing list</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '13, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/899697b5301b3ed2963a8517a1eb3415?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Asher&#39;s gravatar image" />
<p><span>Asher</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Asher has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23736" class="comments-container">
<span id="23739"></span>
<div id="comment-23739" class="comment">
<div id="post-23739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I read that, but it stops right where I need the next bit of info. Awesome, its running, now how to I access it? How to I utilize it? The Project-OSRM-Web from the above post should probably be added to the instructions, or at least a few different options as to how the end user would use the data.</p>
<p>I don't mean to criticize, but it's just difficult to follow along if you don't already know a ton about mapping. Thanks all for the help, any other suggestions would be great.</p>
</div>
<div id="comment-23739-info" class="comment-info">
<span class="comment-age">(27 Jun '13, 01:57)</span> <span class="comment-user userinfo">jjmil03</span>
</div>
</div>
</div>
<div id="comment-tools-23736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23736-form-container" class="comment-form-container">
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

