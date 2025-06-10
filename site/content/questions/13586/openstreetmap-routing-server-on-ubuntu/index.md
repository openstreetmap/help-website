+++
type = "question"
title = "Openstreetmap (routing) server on Ubuntu"
description = '''Hi i am trying to create an OSM server on Ubuntu 12.04 but every time I do it I find that I have a missing package and finally I found on this link http://geotribu.net/node/262 how to create my own osm sever but i think i need the c++ library to find the itinerary , so if any one can help me were i ...'''
date = "2012-06-18T10:12:00Z"
lastmod = "2012-06-18T16:34:00Z"
weight = 13586
keywords = [ "development", "mapserver", "osm", "osm2pgsql", "server" ]
aliases = [ "/questions/13586" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Openstreetmap (routing) server on Ubuntu](/questions/13586/openstreetmap-routing-server-on-ubuntu)

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
<span id="post-13586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13586-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi i am trying to create an OSM server on Ubuntu 12.04 but every time I do it I find that I have a missing package and finally I found on this link <a href="http://geotribu.net/node/262">http://geotribu.net/node/262</a> how to create my own osm sever but i think i need the c++ library to find the itinerary , so if any one can help me were i can find them.</p>
<p>Another question - how can I test this server (I want to put the IP address of this server on a browser where I can find the openstreetmap map and I can calculate the itinerary)? If anyone can help on this point too...</p>
<p>Thank you!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '12, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b12f0aed882f26f3ce09dcd8b95f0a5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmadhc&#39;s gravatar image" />
<p><span>ahmadhc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmadhc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '12, 16:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13586" class="comments-container">
&#10;</div>
<div id="comment-tools-13586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13586-form-container" class="comment-form-container">
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

<span id="13587"></span>

<div id="answer-container-13587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13587-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, what do you mean by "create an OSM server"? Do you mean something that will display maps on a "slippymap" like osm.org, something that will enable you to find places by name, or something that can calculate routes from one place to another?<br />
</p>
<p>If it's maps that you're interested in, the <a href="http://switch2osm.org/">switch2osm</a> site has a couple of examples describing how to set up a tile server that might be helpful. There's <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">this one</a>, which uses packages in a PPA repository, and there's <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">this one</a>, which builds the software manually. I haven't personally tried either on Ubuntu 12.04, but the web pages for each suggest that they should work.<br />
</p>
<p>I'm not quite sure what you mean by "but i think i need the c++ library to find the itinerary" - if you post details of that in your first language perhaps we may be able to work out what the problem is?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '12, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-13587" class="comments-container">
<span id="13588"></span>
<div id="comment-13588" class="comment">
<div id="post-13588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>first of all thanks for ur reply and sorry for my bad english; i dont have a lots of details about cartography but my project is to search and create a server where is installed OSM were we will be able to create our route and see a map on local on our server then we have another part that is to integrate this server if we succeed in a softwre that we developped in our company. if u try to take a look on the link that i send it in the first question that's what i mean but this writed in french so i dont know if u have an idea abut it but this link miss a c++ libraries that should be installed onj the server and tose library make me able to find itenerary (without tose library's i cant do any calculation of any iteneray).</p>
</div>
<div id="comment-13588-info" class="comment-info">
<span class="comment-age">(18 Jun '12, 12:51)</span> <span class="comment-user userinfo">ahmadhc</span>
</div>
</div>
<span id="13591"></span>
<div id="comment-13591" class="comment">
<div id="post-13591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The instructions that you linked to describe setting up a tile server (the same as the switch2osm instructions do). For routing, it's probably worth having a look at this <a href="http://wiki.openstreetmap.org/wiki/Routing">wiki</a> page, and also <a href="http://wiki.openstreetmap.org/wiki/Routing/OnlineRouters">this</a> one.</p>
<p>Finally, it's worth mentioning the various OSM <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC</a> channels. #osm-dev is the best place to ask software-setup-related questions, but there's also a more general channel #osm-fr (francophone).</p>
</div>
<div id="comment-13591-info" class="comment-info">
<span class="comment-age">(18 Jun '12, 14:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="13593"></span>
<div id="comment-13593" class="comment">
<div id="post-13593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry but i am not an expert in cartography so i didn't understand so much your awnser the general idea as a programmer and network administrator i have an ubuntu 12.04 clean there is nothing installed on it. the final result should be that this machine will be an OSRM server that have the same fucntionnality on this site (<a href="http://map.project-osrm.org/">http://map.project-osrm.org/</a>) .and what i need in the moment is how to start and how to proceed step by step and if not at least to give me start idea .</p>
<p>Thank You</p>
</div>
<div id="comment-13593-info" class="comment-info">
<span class="comment-age">(18 Jun '12, 15:44)</span> <span class="comment-user userinfo">ahmadhc</span>
</div>
</div>
<span id="13594"></span>
<div id="comment-13594" class="comment">
<div id="post-13594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(at the risk of stating the obvious in case you haven't found it) re OSRM, I'd start at the project page <a href="http://project-osrm.org/">here</a>, with a wiki <a href="https://github.com/DennisOSRM/Project-OSRM/wiki">here</a> and installation instructions <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Running-OSRM">here</a>. If you get stuck I'd ask on IRC as there's sometimes at least one of the OSRM guys around.</p>
</div>
<div id="comment-13594-info" class="comment-info">
<span class="comment-age">(18 Jun '12, 16:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13587-form-container" class="comment-form-container">
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

