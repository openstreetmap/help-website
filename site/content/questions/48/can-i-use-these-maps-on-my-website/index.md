+++
type = "question"
title = "Can I use these maps on my website?"
description = '''Am I allowed to use these maps on my website? How much will it cost? '''
date = "2010-07-10T13:37:00Z"
lastmod = "2016-04-26T21:42:00Z"
weight = 48
keywords = [ "usage", "cost", "licence" ]
aliases = [ "/questions/48" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Can I use these maps on my website?](/questions/48/can-i-use-these-maps-on-my-website)

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
<span id="post-48-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48-score" class="post-score" title="current number of votes">
19
</div>
<span id="post-48-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Am I allowed to use these maps on my website? How much will it cost?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-cost" rel="tag" title="see questions tagged &#39;cost&#39;">cost</span> <span class="post-tag tag-link-licence" rel="tag" title="see questions tagged &#39;licence&#39;">licence</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '10, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '10, 10:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/3b5143f79efbb5d8c7d52325f41e0e3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randomjunk&#39;s gravatar image" />
<p><span>randomjunk</span><br />
<span class="score" title="1545 reputation points"><span>1.5k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span></p>
</div>
</div>
<div id="comments-container-48" class="comments-container">
&#10;</div>
<div id="comment-tools-48" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="51"></span>

<div id="answer-container-51" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51-score" class="post-score" title="current number of votes">
20
</div>
<span id="post-51-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ChrisH has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you're allowed to use the Maps from OpenStreetMap on your Homepage and it will not cost you anything, but there are some things to remember:</p>
<ul>
<li>you need a proper attribution text in/around your map. The usual term is "Data CC-By-SA by <a href="http://openstreetmap.org/">OpenStreetMap</a>". You can do this using the OpenLayers <a href="http://dev.openlayers.org/docs/files/OpenLayers/Control/Attribution-js.html">OpenLayers.Control.Attribution Control</a> like it's done <a href="http://toolserver.org/~osm/styles/">in this map</a>.</li>
<li>if you expect heavy traffic on your page, you'll need to avoid flooding the osm tile-servers with requests. See <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile usage policy</a> on the wiki. You could come around this by setting up your own tile-server (you can adapt the tile rendering rules then) or using an <a href="http://en.wikipedia.org/wiki/Reverse_proxy">reverse http proxy</a> like <a href="http://www.squid-cache.org/">squid</a>.</li>
</ul>
<p>To embed a map into your homepage you can visit the "Export" Tab on the <a href="https://www.openstreetmap.org/">main OSM site</a>. You'll get copy-and-paste ready HTML-Code there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '10, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f3ef36c6e680019cfe1dda5d5e15d9bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaZderMind&#39;s gravatar image" />
<p><span>MaZderMind</span><br />
<span class="score" title="326 reputation points">326</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaZderMind has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-51" class="comments-container">
<span id="49442"></span>
<div id="comment-49442" class="comment">
<div id="post-49442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It says above"... like it's done in this map." But the link doesn't work. Please can I have an example of a 'correct' website map?</p>
</div>
<div id="comment-49442-info" class="comment-info">
<span class="comment-age">(26 Apr '16, 20:12)</span> <span class="comment-user userinfo">SpillerC</span>
</div>
</div>
<span id="49443"></span>
<div id="comment-49443" class="comment">
<div id="post-49443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12234/spillerc"></a><a href="https://help.openstreetmap.org/users/12234/spillerc">@SpillerC</a>: here is a <a href="http://wayback.archive.org/web/20100803152546/http://toolserver.org/~osm/styles/?">archived version</a>. However, it is not right for the current OSM license anyway (see <a href="https://www.openstreetmap.org/copyright">https://www.openstreetmap.org/copyright</a> ).</p>
</div>
<div id="comment-49443-info" class="comment-info">
<span class="comment-age">(26 Apr '16, 21:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49444"></span>
<div id="comment-49444" class="comment">
<div id="post-49444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meta: how to best deal with this situation of totally outdated answers here - <span>discuss</span>?</p>
</div>
<div id="comment-49444-info" class="comment-info">
<span class="comment-age">(26 Apr '16, 21:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2467"></span>

<div id="answer-container-2467" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2467-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As an addition to the other answers:</p>
<p>If you are a high-traffic website, consider just putting a static image on your page; that way hits to your page will not cause traffic for OSM and the tile server. You can get a static image from OSM's Export tab (Mapnik Image or Osmarender Image).</p>
<p>You can still have the image link to <a href="http://openstreetmap.org">openstreetmap.org</a> using the right coordinates, for user's convenience.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '11, 01:31</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-2467" class="comments-container">
&#10;</div>
<div id="comment-tools-2467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2467-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54"></span>

<div id="answer-container-54" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OpenStreetMap data is currently licenced under <a href="http://creativecommons.org/licenses/by-sa/2.0/" title="Creative Commons — Attribution-ShareAlike 2.0 Generic">CC-BY-SA</a>, which means you can use it for free and also distribute it freely if you say that it came from OpenStreetMap and mention the licence (see the <a href="https://wiki.openstreetmap.org/wiki/Licence" title="OpenStreetMap Licence">Wiki</a> for more details). The same goes for maps that are made out of this data.</p>
<p>However, if you are using a Tileserver (which delivers rendered map images, e.g. for your website) you have to be aware of it's usage policy, which does not affect what you are allowed to do with the map itself, but how you are allowed to use the service to access these maps. The usage policy of the default "Mapnik" tiles (rendered and served by <a href="http://%22tile.openstreetmap.org">"tile.openstreetmap.org</a>", can be found on the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy" title="Tile usage policy">Wiki</a>. This will normally only be relevant for operations that produce heavy load, e.g. bulk downloading of map tiles.</p>
<p>You should also be aware that some websites may have maps that consist of seperate layers, for example by means of the <a href="http://openlayers.org" title="OpenLayers">OpenLayers API</a>. Some of these layers may not be under the same free licence as the underlying OpenStreetMap maps, which means making a screenshot (and thus combining these layers) might be illegal. Please always look for copyright and licence notices.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '10, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5121664159901fa36daf691b8ec860b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="driver2&#39;s gravatar image" />
<p><span>driver2</span><br />
<span class="score" title="1655 reputation points"><span>1.7k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="driver2 has 4 accepted answers">57%</span></p>
</div>
</div>
<div id="comments-container-54" class="comments-container">
&#10;</div>
<div id="comment-tools-54" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54-form-container" class="comment-form-container">
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

