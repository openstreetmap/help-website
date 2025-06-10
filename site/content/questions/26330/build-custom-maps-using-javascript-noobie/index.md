+++
type = "question"
title = "Build Custom Maps using Javascript (noobie)"
description = '''I&#x27;m looking for pointers as to how I can generate maps of journeys across Asia based on OSM (including place names as specified in my own (json?) list and a route). There&#x27;s a lot of info out there and I&#x27;ve already spent a few evenings trying to find the way ahead, without much success. I want to avo...'''
date = "2013-09-13T20:57:00Z"
lastmod = "2013-09-17T09:34:00Z"
weight = 26330
keywords = [ "json", "javascript", "journey" ]
aliases = [ "/questions/26330" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Build Custom Maps using Javascript (noobie)](/questions/26330/build-custom-maps-using-javascript-noobie)

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
<span id="post-26330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26330-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for pointers as to how I can generate maps of journeys across Asia based on OSM (including place names as specified in my own (json?) list and a route).</p>
<p>There's a lot of info out there and I've already spent a few evenings trying to find the way ahead, without much success.</p>
<p>I want to avoid running my own renderer. I want to avoid paid-for services. I want places (towns) to be shown as dots, not the usual pins one gets as markers. I want to be able to create different journeys by switching the json data, but using the same style.</p>
<p>Can anyone help with some advice or a link to a tutorial or guide?</p>
<p>TIA</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-journey" rel="tag" title="see questions tagged &#39;journey&#39;">journey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '13, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/16c4c25181cae1f9f5e78bd75382aa81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Catford%20Dog&#39;s gravatar image" />
<p><span>Catford Dog</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Catford Dog has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '13, 21:00</strong> </span></p>
</div>
</div>
<div id="comments-container-26330" class="comments-container">
<span id="26396"></span>
<div id="comment-26396" class="comment">
<div id="post-26396-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are looking for a quite special solution with a bunch of individual features.</p>
<p>IMHO there is no such program out-of-the-box.</p>
<p>Maybe we can help you if you take one key feature you want (maybe map display) and then tell us in detail any program or map display you already tried, and why it is no good for you.</p>
<p>Same is about routing solutions:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Routing">http://wiki.openstreetmap.org/wiki/Routing</a></p>
<p>Is there any solution that comes near your aim?</p>
</div>
<div id="comment-26396-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 16:46)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26398"></span>
<div id="comment-26398" class="comment">
<div id="post-26398-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Or, let's look at it another way: say you generate a GPX of your route (maybe using the public instance OSRM, <a href="http://osrm.at/)">http://osrm.at/)</a> and display it on the your website with Leaflet (<a href="http://leafletjs.com/).">http://leafletjs.com/).</a> What else would you need to do that this combination wouldn't provide?</p>
</div>
<div id="comment-26398-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 16:51)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="26408"></span>
<div id="comment-26408" class="comment">
<div id="post-26408-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Possibly I am barking up the wrong tree. I suppose I am looking at OSM as an open source alternative to Google Maps. I sense now that this is wrong.</p>
<p>In Google Maps I can write some quite simple Javascript to send latlong points to the Google Maps API and have it return a map populated with my data. Is this possible with OSM?</p>
</div>
<div id="comment-26408-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 18:55)</span> <span class="comment-user userinfo">Catford Dog</span>
</div>
</div>
<span id="26410"></span>
<div id="comment-26410" class="comment">
<div id="post-26410-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Yes, but OpenStreetMap doesn't provide one official JavaScript library (which Google calls an API, though we don't) which you have to use. Instead, you can choose any library that will display OSM map tiles. Leaflet and OpenLayers are the two most popular; most people agree that Leaflet is currently easier to use and provides the most commonly requested functionality. See <a href="http://leafletjs.com/">http://leafletjs.com/</a> for more.</p>
</div>
<div id="comment-26410-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 19:13)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="26420"></span>
<div id="comment-26420" class="comment">
<div id="post-26420-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You may try this: <a href="http://umap.openstreetmap.fr/en/">http://umap.openstreetmap.fr/en/</a> (use OSRM to export a GPX if you want to follow exactly the road) or that: <a href="http://syj.renevier.net/">http://syj.renevier.net/</a></p>
</div>
<div id="comment-26420-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 09:34)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-26330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

