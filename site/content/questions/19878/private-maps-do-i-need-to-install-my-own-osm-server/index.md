+++
type = "question"
title = "Private Maps: Do I Need to Install My Own OSM Server?"
description = '''I am looking into creating my own private OSM map. This data would not be available to the public. It would utilize public OSM map data but would not edit it. It would overlay private map data that would only be available to a closed user group. Several threads suggest that it is necessary to instal...'''
date = "2013-02-12T19:36:00Z"
lastmod = "2013-02-13T17:56:00Z"
weight = 19878
keywords = [ "private", "server" ]
aliases = [ "/questions/19878" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Private Maps: Do I Need to Install My Own OSM Server?](/questions/19878/private-maps-do-i-need-to-install-my-own-osm-server)

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
<span id="post-19878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19878-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking into creating my own private OSM map. This data would not be available to the public. It would utilize public OSM map data but would not edit it. It would overlay private map data that would only be available to a closed user group.</p>
<p>Several threads suggest that it is necessary to install my own OSM server. Reading these threads I get the impression that it may be necessary to:</p>
<ul>
<li>Install Rails Port of OSM server</li>
<li>Install mapnik</li>
<li>etc.</li>
</ul>
<p>Other threads make no mention of installing my own OSM server. From these threads I get the impression that it may be necessary only to:</p>
<ul>
<li>Use Maperitive</li>
</ul>
<p>Is it necessary to install my own OSM server in order to produce a private map not available to the public? If not, what are the pros and cons of doing it with and without my own OSM server?</p>
<p>Thanks very much in advance to all for any info!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '13, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1ea2b8fe02ce7ee34472972214a3bef9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VikR&#39;s gravatar image" />
<p><span>VikR</span><br />
<span class="score" title="20 reputation points">20</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VikR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19878" class="comments-container">
<span id="19882"></span>
<div id="comment-19882" class="comment">
<div id="post-19882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By "a private map" do you mean an interactive draggable zoomable web map like you see on the osm.org front page, or do you mean a static image (or PDF or similar) for placing on a web page or similar?</p>
</div>
<div id="comment-19882-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 20:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19878-form-container" class="comment-form-container">
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

<span id="19886"></span>

<div id="answer-container-19886" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19886-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-19886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="VikR has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many different ways to create "private maps" and depending on your exact needs different technological solutions are best suited to your situation. Therefore without knowing the exact circumstances it is difficult to say what you will need, but I can try and clarify some things that might help you choose better what is appropriate for your situation:</p>
<p>The rails_port server is (simplified) the web application running on OpenStreetMap.org, providing the website, user management, diaries and the editing API. It is not responsible for rendering and displaying the map tiles. Therefore the rails_port is nearly always <em>not</em> what people want, except for if you want to run your own private crowd sourced geodata project.</p>
<p>More commonly is that people need a "tile server", i.e. a server that takes the raw (XML) data provided by OpenStreetMap and turns it into bitmap renderings of a pretty map. Both Mapnik and Maperative are two of the common map rendering software that can be used for this task.</p>
<p>Maperative is a more integrative software package that covers tasks from designing stylesheets to actually rendering and tile serving. It also works well on Windows. Mapnik is only a rendering library and needs a whole host of additional software components e.g. mod_tile, tirex, postgresql. However mapnik and its corresponding tool chain is believed to scale better. So from what I have seen, Maperative tends to be used more if one only needs to render a small area, e.g. a city or wants to experiment with things. Mapnik with its toolchain is instead used commonly when setting up tile servers with a world wide map coverage like e.g. the one presented on osm.org.</p>
<p>Whether you need to set up any tile server depends on your usage amount and service requirements. Unlike for Google maps or Bing maps, nothing in the terms and conditions restrict your usage of the openstreetmap.org tile server to public facing usage. So private usage is theoretically fine (as long as you observe the license conditions of the data, but if you are using independent overlays rather than mixing the data that is probably the case). However, the reason why most people suggest to set up your own tile server for projects like this is the following:</p>
<p>The OpenStreetMap.org servers are entirely run on donated resources and have a fairly limited capacity. They cannot provide large scale tile serving and thus there are heavy restrictions on how much one is allowed to use them, irrespective of how you use them. As it is not a commercial service, it is not really specified how much exactly is allowed, but instead the rule of thumb is that if the sysadmins notice that a single user uses a significant amount of total available server resource that is too much and counter measures are put in place to limit the resource drainage. Furthermore, there is no up time guarantee and it can happen that the OpenStreetMap.org tile servers are down for several days for maintenance.</p>
<p>Due to those reasons it is generally encouraged for (commercial) projects of any significant size to not use the OpenStreetMap.org tile serving infrastructure and instead use ones own server infrastructure or one of the commercial osm tiles server providers for which one can get a performance and uptime guarantee. However, for small, non critical projects it might just be fine.</p>
<p>Having ones own tileserver however has additional advantages. E.g. one can design ones own map style that fits to the application in mind much better than a generic mapstyle.</p>
<p>You can find some additional resources on how to set up your own tileserver on <a href="http://switch2osm.org/">http://switch2osm.org/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '13, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19886" class="comments-container">
<span id="19889"></span>
<div id="comment-19889" class="comment">
<div id="post-19889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>, yes, it would be an interactive draggable zoomable web map.</p>
<p><span>@apmon</span>, thanks so much for this info. It's great to hear I do not need to install the rails_port server. We would not be using an area larger than a city, so it sounds like maperative would be sufficient.</p>
<p>To summarize, is it correct that using maperative as my tile server, I could:</p>
<ul>
<li>Generate tiles that use my own private street map data plus open source OSM street map data?</li>
</ul>
<p>Thanks very much in advance for the info.</p>
</div>
<div id="comment-19889-info" class="comment-info">
<span class="comment-age">(12 Feb '13, 21:30)</span> <span class="comment-user userinfo">VikR</span>
</div>
</div>
</div>
<div id="comment-tools-19886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19903"></span>

<div id="answer-container-19903" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19903-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as i understand it, Maperitive will serve pure OSM tiles, which can the be overlain with your data by you using whatever web mapping library you choose to use (OpenLayers for example).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '13, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-19903" class="comments-container">
<span id="19920"></span>
<div id="comment-19920" class="comment">
<div id="post-19920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great. Thanks!</p>
</div>
<div id="comment-19920-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 17:56)</span> <span class="comment-user userinfo">VikR</span>
</div>
</div>
</div>
<div id="comment-tools-19903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19903-form-container" class="comment-form-container">
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

