+++
type = "question"
title = "Why is the same Popup text displayed for both Markers OpenLayers"
description = '''I am displaying two Marker dynamically on OSM 5. The data saved to the array is (longiutde, latitude, car name) The Marker are being correctly displayed with a Popup window for each one. The Popup windows should contain the name of each car, but the problem here is that i am ALWAYS getting the secon...'''
date = "2020-10-19T10:59:00Z"
lastmod = "2020-10-20T09:26:00Z"
weight = 77148
keywords = [ "openlayers", "javascript", "osm" ]
aliases = [ "/questions/77148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the same Popup text displayed for both Markers OpenLayers](/questions/77148/why-is-the-same-popup-text-displayed-for-both-markers-openlayers)

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
<span id="post-77148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77148-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am displaying two Marker dynamically on OSM 5. The data saved to the array is (longiutde, latitude, car name) The Marker are being correctly displayed with a Popup window for each one. The Popup windows should contain the name of each car, but the problem here is that i am ALWAYS getting the second name of the car displayed on both Popups which is wrong. I am really stucked i have tried everything i knew.</p>
<p><code> / </code><em><code>open street map newest version</code></em><code> / var map = new ol.Map({ target: 'map', // the div id layers: [ new ol.layer.Tile({ source: new ol.source.OSM() }) ], view: new ol.View({ center: ol.proj.fromLonLat([4.35247, 52.520008]), zoom: 6, minZoom: 3 }) }); for(var i=0; i &lt; arrayPos.length; i++) { var long = arrayPos[i][0] var lat = arrayPos[i][1]; var vehName = arrayPos[i][2]; // add a marker to the map var layer = new ol.layer.Vector({ source: new ol.source.Vector({ features: [ new ol.Feature({ geometry: new ol.geom.Point(ol.proj.fromLonLat([long, lat])) })] }) }); layer.setStyle(new ol.style.Style({ image: new ol.style.Icon({ src: 'https://wiki.openstreetmap.org/w/images/0/0c/Hgv.png', // scale: 0.4 // set the size of the vehicle on the map }) })); map.addLayer(layer); //initialize the popup var container = document.getElementById('popup'); var content = document.getElementById('popup-content'); var overlay = new ol.Overlay({ element: container, autoPan: true, autoPanAnimation: { duration: 250 } }); map.addOverlay(overlay); console.log(vehName); // two different car names are shown in the console //display the pop with on mouse over event map.on('pointermove', function (event) {</code><br />
<code>if (map.hasFeatureAtPixel(event.pixel) === true) {</code><br />
<code>var coordinate = event.coordinate; //simple text written in the popup, values are just of the second index content.innerHTML = '</code><strong><code>Im a vehicle:</code></strong><br />
<code>'+vehName; //just the second one is getting displayed overlay.setPosition(coordinate); } else { overlay.setPosition(undefined); } }); } </code> Any help is really appreciated!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '20, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0ff473215e00d01276ce15108b285e13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unkown53&#39;s gravatar image" />
<p><span>unkown53</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unkown53 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '20, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-77148" class="comments-container">
<span id="77160"></span>
<div id="comment-77160" class="comment">
<div id="post-77160-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Our wiki doesn't have anything for <a href="https://wiki.openstreetmap.org/w/index.php?title=Special:Search&amp;search=%22OSM+5%22">"OSM 5"</a>. What are you actually using?</p>
</div>
<div id="comment-77160-info" class="comment-info">
<span class="comment-age">(19 Oct '20, 23:00)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="77161"></span>
<div id="comment-77161" class="comment">
<div id="post-77161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using the latest version of OSM</p>
</div>
<div id="comment-77161-info" class="comment-info">
<span class="comment-age">(19 Oct '20, 23:05)</span> <span class="comment-user userinfo">unkown53</span>
</div>
</div>
<span id="77162"></span>
<div id="comment-77162" class="comment">
<div id="post-77162-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OSM is just a database of raw data. What you're probably using is some other software that uses OSM data to reach some goal.</p>
<p>Based on the code you posted, my guess is that you're using the OpenLayers library to display a map on a website somewhere. The latest version of OpenLayers is 6.4.3, though, so maybe you're using some other software?</p>
</div>
<div id="comment-77162-info" class="comment-info">
<span class="comment-age">(20 Oct '20, 00:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="77163"></span>
<div id="comment-77163" class="comment">
<div id="post-77163-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/19152/unkown53">@unkown53</a> can you link to what you mean by "OSM"? Perhaps show where you downloaded it from?</p>
</div>
<div id="comment-77163-info" class="comment-info">
<span class="comment-age">(20 Oct '20, 00:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77169"></span>
<div id="comment-77169" class="comment not_top_scorer">
<div id="post-77169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I am using Openlayers. I just used OSM for the abbreviation of OpenStreetMap. But could anyone of you knew what i am messing up?. I am really stucked there :(</p>
</div>
<div id="comment-77169-info" class="comment-info">
<span class="comment-age">(20 Oct '20, 09:08)</span> <span class="comment-user userinfo">unkown53</span>
</div>
</div>
<span id="77172"></span>
<div id="comment-77172" class="comment">
<div id="post-77172-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://openlayers.org/">OpenLayers</a> is a JavaScript library that can be used to display all sorts of map data on a website. OpenStreetMap maps - among others - can be used as background but other than that OpenLayers has nothing to do with OSM. Possibly someone here might be able to give you an answer but if not you might be better off to direct your question to a more OpenLayers oriented forum.</p>
</div>
<div id="comment-77172-info" class="comment-info">
<span class="comment-age">(20 Oct '20, 09:26)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-77148" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-77148-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

