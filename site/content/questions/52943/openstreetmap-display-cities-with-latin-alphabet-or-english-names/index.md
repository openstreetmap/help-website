+++
type = "question"
title = "OpenStreetMap Display Cities with Latin Alphabet or English Names?"
description = '''Hi all, I need to display the cities/states with their English names ? The app shows the map with the following source code in javascript ;  L.tileLayer(&#x27;http://{s}.tile.osm.org/{z}/{x}/{y}.png&#x27;, {  attribution: &#x27;&amp;amp;copy; &amp;lt;a href=&quot;http://osm.org/copyright&quot;&amp;gt;OpenStreetMap&amp;lt;/a&amp;gt; contributor...'''
date = "2016-11-14T17:09:00Z"
lastmod = "2016-12-18T14:17:00Z"
weight = 52943
keywords = [ "openstreetmap", "english", "latin", "tileserver" ]
aliases = [ "/questions/52943" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap Display Cities with Latin Alphabet or English Names?](/questions/52943/openstreetmap-display-cities-with-latin-alphabet-or-english-names)

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
<span id="post-52943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I need to display the cities/states with their English names ? The app shows the map with the following source code in javascript ;</p>
<pre><code>L.tileLayer(&#39;http://{s}.tile.osm.org/{z}/{x}/{y}.png&#39;, {
    attribution: &#39;&amp;copy; &lt;a href=&quot;http://osm.org/copyright&quot;&gt;OpenStreetMap&lt;/a&gt; contributors&#39;,
    maxZoom: 18
}).addTo(map);</code></pre>
<p>For a simple scenario, I should put a param into the url provided by OpenStreetMap Tile server. If the way like I stated, could you please provide the sytnax for it? Additionally, I've explored the way of changing name of places, and some people provided some ways in the following link ;</p>
<p><a href="http://gis.stackexchange.com/questions/187863/change-the-language-of-osm-maps-in-qgis">http://gis.stackexchange.com/questions/187863/change-the-language-of-osm-maps-in-qgis</a></p>
<ol>
<li><p>Render the tiles using the Mapnik toolchain or Maperitive using the name:en field instead of the name field for labelling. Add them with the TileLayer plugin to your project.</p></li>
<li><p>Using the QuickOSM plugin, download elements that have a name:en tag, set the rendering to transparent, and label inside QGIS with the name_en field.</p></li>
</ol>
<p>I could not understand the ways stated above. Could you please detail these way of solutions ? Putting in simple words ;</p>
<p>Is there any way of getting tiles with their English names from tile servers by setting needed parameters like name:en or whatever it is?</p>
<p>Thanks &amp; Best Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-english" rel="tag" title="see questions tagged &#39;english&#39;">english</span> <span class="post-tag tag-link-latin" rel="tag" title="see questions tagged &#39;latin&#39;">latin</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/310e3c47ef21b0b8852fd50dd78a5a7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cranberries&#39;s gravatar image" />
<p><span>Cranberries</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cranberries has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52943" class="comments-container">
&#10;</div>
<div id="comment-tools-52943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52943-form-container" class="comment-form-container">
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

<span id="52944"></span>

<div id="answer-container-52944" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52944-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tilelayer defined in your snippet "<code>tile.osm.org</code>" does <em>not</em> have latin names in it. Render your own tiles with latin names, and use the URL for that in place of "tile.osm.org".</p>
<p>In order to create a tile server, see examples such as <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">this</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '16, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52944" class="comments-container">
<span id="52945"></span>
<div id="comment-52945" class="comment">
<div id="post-52945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Isn't there any other alternative way for this approach ? I mean, does OpenStreetmap have any options for the tile server with some language packs/options ?</p>
<p>Is the map in the following link also provided by a custom tile server ?</p>
<p><a href="http://openstreetmap.in/demo/#9.08/38.3220/35.6500">http://openstreetmap.in/demo/#9.08/38.3220/35.6500</a></p>
<p>The second question I would like to is, for the first solution you mentioned, how can I get the city/states name labels in English or Latin Alphabet?</p>
<p>Thanks &amp; Best Regards,</p>
</div>
<div id="comment-52945-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 18:29)</span> <span class="comment-user userinfo">Cranberries</span>
</div>
</div>
<span id="52949"></span>
<div id="comment-52949" class="comment">
<div id="post-52949-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are 4 different styles available on osm.org and 2 of them show Latin names, but you'd need to check the terms of use before using in your own leaflet map.</p>
<p>Essentially OSM is data with which you can create your own map. Think of the styles on osm.org as examples.</p>
<p>Edit: Following re-reading several replies below this it's worth mentioning how you can see the "other" tile layers at OpenStreetMap.org. At the right-hand-side of the map display there are some icons. One of them, the fourth one down, looks like a "stack of books". If you hover your mouse over it (assuming you're using a PC and have a mouse, of course) a message displays "layers". If you click that you can choose between "standard map", "cycle map", "transport map" and "humanitarian". If you choose "cycle" or "transport", you'll notice that places with non-latin names have a latin name displayed after them. If you think that these other layers are a bit "hidden" and difficult to discover, I agree :)</p>
</div>
<div id="comment-52949-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 20:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52952"></span>
<div id="comment-52952" class="comment">
<div id="post-52952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Could you please share one of them with me ? Is there any url for the style with Latin Aplhabet? I have no idea about the way applying solution you mentioned actually.. What do you mean by saying terms of use ? Is Latin name feature priced ?</p>
</div>
<div id="comment-52952-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 21:01)</span> <span class="comment-user userinfo">Cranberries</span>
</div>
</div>
<span id="52963"></span>
<div id="comment-52963" class="comment">
<div id="post-52963-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To be clear, OpenStreetMap isn't designed as a map service you can use. It's some map data that you can contribute to and create your own maps from. Let's take Visakhapatnam as an example. In the openstreetmap.in example map, that's <a href="http://openstreetmap.in/demo/#9.54/17.6915/83.1969">http://openstreetmap.in/demo/#9.54/17.6915/83.1969</a> . In the OSM data, it's <a href="http://www.openstreetmap.org/node/245641840">http://www.openstreetmap.org/node/245641840</a> . You can see the available names that you can use to incorporate into maps there.</p>
<p>Various people have created maps that feature latin names - the cycle map and transport layers at openstreetmap.org among them. Another example is "Gnome Maps" which uses tiles from Mapbox (see <a href="http://www.omgubuntu.co.uk/2016/07/gnome-maps-new-tile-service">here</a> for the story of that).</p>
</div>
<div id="comment-52963-info" class="comment-info">
<span class="comment-age">(15 Nov '16, 00:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53592"></span>

<div id="answer-container-53592" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did see the mention of 4 different styles. There was no link there. In your reply to my grumpy comment there is, but that goes to something about Gnome Maps and a whole lot of text and so forth and so on, ad infinitum.</p>
<p>The point that seems to be so hard to communicate is that OSM, <em>itself</em>, not in a layer, not in some other program, not in a script tweak, <em>itself</em>, needs to have a little button in the upper right corner which is a dropdown menu that allows you to choose the alphabet.</p>
<p>This is basic.</p>
<p>I do know you're not being rude. And I very much appreciate that you're not responding to me jumping up and down and shouting by doing the same! :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '16, 03:00</strong></p>
<img src="https://secure.gravatar.com/avatar/3187f4bdfd39f6aeab160ef19a458ee8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quixote7&#39;s gravatar image" />
<p><span>quixote7</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quixote7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53592" class="comments-container">
<span id="53597"></span>
<div id="comment-53597" class="comment">
<div id="post-53597-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Re "... 4 different styles. There was no link there ..." I've expanded the comment above that explains how to get the the "layer" switcher on OpenStreetMap.org.</p>
</div>
<div id="comment-53597-info" class="comment-info">
<span class="comment-age">(18 Dec '16, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53592-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53588"></span>

<div id="answer-container-53588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53588-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-53588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So if I understand SomeoneElse correctly, there's no way to get place names in alphabets that are familiar to the user. ?? Really? In order to use OpenStreetMaps without being a coder I need to read Hindi and Japanese and Arabic and Latin alphabet and, well, you know what I'm trying to say.</p>
<p>As if Wikipedia gave us information about everything, but if you wanted to know something about, say, Ulan Bator you had to be able to read Mongolian.</p>
<p>"OpenStreetMap isn't designed as a map service you can use." Indeed, apparently.</p>
<p>(Sorry to be so annoyed, and OSM is a truly great project, and I signed up years ago so I could contribute, and this factor is the one huge stumbling block that makes it impossible for me to use it most of the time. I came back to check since I figured it had to have been fixed by now, and instead I find this question.)</p>
<p>(And an answer that says, just like in the good old days, write your own program if you don't like it.)</p>
<p>(:REALLY?:)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '16, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/3187f4bdfd39f6aeab160ef19a458ee8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quixote7&#39;s gravatar image" />
<p><span>quixote7</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quixote7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53588" class="comments-container">
<span id="53590"></span>
<div id="comment-53590" class="comment">
<div id="post-53590-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I suggest that you read some of the text that I've written above again, starting with "There are 4 different styles available on osm.org and 2 of them show Latin names" and making sure to include " Another example is "Gnome Maps" which uses tiles from Mapbox (see <a href="http://www.omgubuntu.co.uk/2016/07/gnome-maps-new-tile-service">here</a> for the story of that)."</p>
<p>I'm not trying to be rude (in fact, I'm deliberately trying <em>not</em> to be rude) but I think "the ability to follow a hyperlink" doesn't exactly fall into the category of "write your own program if you don't like it".</p>
</div>
<div id="comment-53590-info" class="comment-info">
<span class="comment-age">(17 Dec '16, 18:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53595"></span>
<div id="comment-53595" class="comment">
<div id="post-53595-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The German and French communities made maps in resp. German and French which are available from their website. I think that OsmAnd, and app for Android also displays labels in the language of the user (or local language depending on a preset).</p>
</div>
<div id="comment-53595-info" class="comment-info">
<span class="comment-age">(18 Dec '16, 11:00)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53596"></span>
<div id="comment-53596" class="comment">
<div id="post-53596-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>What you're asking is a great thing to aim for, but (unless OSM was to be unacceptably English-centric) means generating and hosting map tiles for every language in the world. That's a big ask, especially - as stated several times in answers here - openstreetmap.org is not really intended as an end-user mapping site, but as a source of data for the world's mapping sites and applications. Even going from one to ten languages would be a massive jump.</p>
<p>In the medium to long term, this may perhaps be solved by moving to "vector tiles" (where the map is both drawn and displayed in your browser) rather than "raster tiles" (.png files that are drawn by the server and displayed in your browser). Moving to vector tiles is sure to happen sooner or later, but if you'd like to make it sooner rather than later, new developers are always welcome.</p>
</div>
<div id="comment-53596-info" class="comment-info">
<span class="comment-age">(18 Dec '16, 13:50)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53588-form-container" class="comment-form-container">
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

