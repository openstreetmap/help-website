+++
type = "question"
title = "Change tiles of local Openstreetmap Website"
description = '''I did setup locally a OpenStreetMap Website and a Tile Server, but my OSM Website is getting the tiles from the regular OSM. I would like to know what files I need to change in my OSM Website server in order to make it get the tiles from my local tile server. I tried to search in internet but it isn...'''
date = "2020-03-12T02:29:00Z"
lastmod = "2020-05-27T05:10:00Z"
weight = 73488
keywords = [ "website", "tileserver" ]
aliases = [ "/questions/73488" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Change tiles of local Openstreetmap Website](/questions/73488/change-tiles-of-local-openstreetmap-website)

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
<span id="post-73488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73488-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did setup locally a OpenStreetMap Website and a Tile Server, but my OSM Website is getting the tiles from the regular OSM. I would like to know what files I need to change in my OSM Website server in order to make it get the tiles from my local tile server. I tried to search in internet but it isn't clear which files i need to change nether which lines need to be changed.</p>
<p>Here follows an image of my tile server, with data of Brazil country.</p>
<p><img src="https://i.imgur.com/sU70Jtf.png" alt="alt text" /></p>
<p>Here follows what appears in my Rails application, showing that the tiles used by the application are from OSM. <img src="https://i.imgur.com/W0C9zWy.png" alt="alt text" /></p>
<p>Thanks in advance.</p>
<h1 id="update-1-i-suspect-the-file-to-be-changed-is-the-openstreetmap-websitevendorassetsleafletleaflet.osm.js-at-line-17-because-when-i-overwrite-the-ip-of-my-tile-server-over-the-tile.openstreetmap.org-it-gave-me-a-gray-screen-like-there-were-no-tile-server-attached-to-the-app.">UPDATE 1: I suspect the file to be changed is the openstreetmap-website/vendor/assets/leaflet/leaflet.osm.js at line 17, because when I overwrite the IP of my tile server over the tile.openstreetmap.org it gave me a gray screen like there were no tile server attached to the app.</h1>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '20, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '20, 20:36</strong> </span></p>
</div>
</div>
<div id="comments-container-73488" class="comments-container">
&#10;</div>
<div id="comment-tools-73488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73488-form-container" class="comment-form-container">
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

<span id="73497"></span>

<div id="answer-container-73497" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The file that needs to be changed is the openstreetmap-website/vendor/assets/leaflet/leaflet.osm.js exactly in the line 17 which is</p>
<p>url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',</p>
<p>needs to be changed to</p>
<p>url: 'https://IP/osm/{z}/{x}/{y}.png',</p>
<p>Of course if 'osm' is what you put in renderd.conf URI path.</p>
<p>That {s} before IP was the problem.</p>
<p><img src="https://i.imgur.com/dVnRjmB.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '20, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73497" class="comments-container">
<span id="73503"></span>
<div id="comment-73503" class="comment">
<div id="post-73503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad you found the solution ! I think you can mark your own answer as accepted, so that the question won't stay unsolved.</p>
<p>The {s} resolve to a, b or c, to share the load on different servers, or trick the browser in doing parallel requests.</p>
<p>Regards</p>
</div>
<div id="comment-73503-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 15:01)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73507"></span>
<div id="comment-73507" class="comment">
<div id="post-73507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still didn't appeared the option to accept the answer. I think it need to wait some time to be able to accept.</p>
</div>
<div id="comment-73507-info" class="comment-info">
<span class="comment-age">(13 Mar '20, 15:52)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="75016"></span>
<div id="comment-75016" class="comment">
<div id="post-75016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For some reason I can't mark this answer as accepted.</p>
</div>
<div id="comment-75016-info" class="comment-info">
<span class="comment-age">(27 May '20, 05:10)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-73497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73494"></span>

<div id="answer-container-73494" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73494-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This <a href="https://github.com/openstreetmap/openstreetmap-website/search?q=%22tile.openstreetmap.org%22&amp;type=">search</a> should be a starting point. I guess it's Leaflet you'll want to change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '20, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-73494" class="comments-container">
<span id="73496"></span>
<div id="comment-73496" class="comment">
<div id="post-73496-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, in other tutorial that I saw (<a href="https://gis.stackexchange.com/questions/336151/data-is-not-appearing-in-a-local-osm-server-after-applying-changes-to-it)">https://gis.stackexchange.com/questions/336151/data-is-not-appearing-in-a-local-osm-server-after-applying-changes-to-it)</a> it says to change a line that I only found at OpenLayers folder. And it says to substitute <a href="https://a.tile.openstreetmap.org/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">https://a.tile.openstreetmap.org/${z}/${x}/${y}.png</a> but says nothing about <a href="https://b.tile.openstreetmap.org/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">https://b.tile.openstreetmap.org/${z}/${x}/${y}.png</a> or <a href="https://c.tile.openstreetmap.org/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png">https://c.tile.openstreetmap.org/${z}/${x}/${y}.png</a> so it stills confusing.</p>
</div>
<div id="comment-73496-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 15:18)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-73494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73494-form-container" class="comment-form-container">
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

