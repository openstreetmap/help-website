+++
type = "question"
title = "OpenStreetMap Integration in react native application"
description = '''OpenStreetMap Integration in react native application. Please guide me on that. I&#x27;m trying to show a pin point on current location &amp;amp; after selecting search criteria user can see the near by (within 1km) shops pin point on the map.'''
date = "2019-11-18T11:36:00Z"
lastmod = "2019-11-19T15:00:00Z"
weight = 71693
keywords = [ "#reactnative" ]
aliases = [ "/questions/71693" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap Integration in react native application](/questions/71693/openstreetmap-integration-in-react-native-application)

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
<span id="post-71693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71693-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OpenStreetMap Integration in react native application. Please guide me on that.</p>
<p>I'm trying to show a pin point on current location &amp; after selecting search criteria user can see the near by (within 1km) shops pin point on the map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#reactnative" rel="tag" title="see questions tagged &#39;#reactnative&#39;">#reactnative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '19, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff571b3eb776b65e87d33f8c4e6ecc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kailas%20B&#39;s gravatar image" />
<p><span>Kailas B</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kailas B has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '19, 11:57</strong> </span></p>
</div>
</div>
<div id="comments-container-71693" class="comments-container">
<span id="71695"></span>
<div id="comment-71695" class="comment">
<div id="post-71695-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what you are actually trying to do? "OpenStreetMap" is just a big pile of data, and people use it for all sorts of things - they create maps from it, they calculate routes between A and B, they look up placenames, they use the data to statistically enquire about differences between regions. What is it you are actually trying to do?</p>
</div>
<div id="comment-71695-info" class="comment-info">
<span class="comment-age">(18 Nov '19, 11:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71693-form-container" class="comment-form-container">
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

<span id="71698"></span>

<div id="answer-container-71698" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71698-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will likely be using a Javascript library like Leaflet or OpenLayers to display a map, and then you will be constructing and sending a request to the Overpass API service that returns objects with certain tags within a certain distance from a given start point. You will want to learn/read up on how to display an OpenStreetMap map with <a href="leafletjs.com">Leaflet</a> or <a href="openlayers.org">OpenLayers,</a> how you access the current position of the phone, how you write <a href="https://lz4.overpass-api.de/">Overpass</a> queries, and how you parse and display the results on the map (one option might be <a href="https://github.com/tyrasd/osmtogeojson">osmtogeojson).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '19, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71698" class="comments-container">
<span id="71699"></span>
<div id="comment-71699" class="comment">
<div id="post-71699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This will show default map with current location.</p>
</div>
<div id="comment-71699-info" class="comment-info">
<span class="comment-age">(18 Nov '19, 12:27)</span> <span class="comment-user userinfo">Kailas B</span>
</div>
</div>
<span id="71709"></span>
<div id="comment-71709" class="comment">
<div id="post-71709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/API_v0.6">https://wiki.openstreetmap.org/wiki/API_v0.6</a> find out these API but authentication URL &amp; parameter is not given. Is anyone know?</p>
</div>
<div id="comment-71709-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 07:04)</span> <span class="comment-user userinfo">Kailas B</span>
</div>
</div>
<span id="71720"></span>
<div id="comment-71720" class="comment">
<div id="post-71720-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The OpenStreetMap API is not relevant for your task.</p>
</div>
<div id="comment-71720-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 10:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="71722"></span>
<div id="comment-71722" class="comment not_top_scorer">
<div id="post-71722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I show Map then in react native. not getting solution of show it. Can you provide any steps OR reference link.</p>
</div>
<div id="comment-71722-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 11:53)</span> <span class="comment-user userinfo">Kailas B</span>
</div>
</div>
<span id="71725"></span>
<div id="comment-71725" class="comment">
<div id="post-71725-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As Frederik says above, "You will want to learn/read up on how to display an OpenStreetMap map with Leaflet or OpenLayers, how you access the current position of the phone, how you write Overpass queries, and how you parse and display the results on the map".</p>
<p>Taking this one at a time, the documentation on Leaflet is <a href="https://leafletjs.com/">here</a>. There are lots of tutorials there, but right on that front page is an example that displays a map with a marker on it.</p>
<p>You have a couple of options for "how you access the current position of the phone" that vary by phone - a simple <a href="https://duckduckgo.com/?q=how+you+access+the+current+position+of+the+phone&amp;t=ffsb&amp;ia=web">web search</a> gets you to various options, and you can decide what is right for you. I'm not familiar with React Native, but it's entirely possible that there's an abstraction layer in there for location.</p>
<p>Similarly, a <a href="https://duckduckgo.com/?q=how+you+write+Overpass+queries&amp;t=ffsb&amp;ia=web">web search</a> for "how you write Overpass queries" points you at a couple of articles on the OSM wiki. It's pretty straightforward to use.</p>
</div>
<div id="comment-71725-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 14:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="71726"></span>
<div id="comment-71726" class="comment">
<div id="post-71726-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Another link that might be helpful is StackOverflow's <a href="https://stackoverflow.com/help/how-to-ask">"how to ask a good question"</a>.</p>
<p>If you're really just confused and really don't know where to start, then take one (or several) steps backward until you can explain to people what you are familiar with and where your confusion starts. For example, if you aren't familiar with React Native (or Javascript) you'll need to learn how to do basic things there before being able to do anything with the answers to your question here.</p>
</div>
<div id="comment-71726-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 15:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71698" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71698-form-container" class="comment-form-container">
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

