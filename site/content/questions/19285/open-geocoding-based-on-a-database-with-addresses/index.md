+++
type = "question"
title = "Open Geocoding based on a database with addresses"
description = '''I&#x27;m currently in the very beginning of exploring the maps possibilities, at the moment by using Google Maps JS v3 API. I have a database running, with a lot of addresses (in form of following format: &quot;Street&quot; &quot;house-number&quot;, &quot;postal-code&quot; ), which I&#x27;m extracting in XML by using PHP code. My currentl...'''
date = "2013-01-23T13:52:00Z"
lastmod = "2013-01-25T09:41:00Z"
weight = 19285
keywords = [ "openstreetmap", "geocoding" ]
aliases = [ "/questions/19285" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Open Geocoding based on a database with addresses](/questions/19285/open-geocoding-based-on-a-database-with-addresses)

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
<span id="post-19285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19285-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently in the very beginning of exploring the maps possibilities, at the moment by using Google Maps JS v3 API. I have a database running, with a lot of addresses (in form of following format: "Street" "house-number", "postal-code" ), which I'm extracting in XML by using PHP code. My currently experiment with Google maps api works fine, first by reading my XML document generated with my PHP page, and the transforming each address in the XML into latlng by using Googles geocode service. The problem among others, that I'm hitting the limitations of the Google geocode, and for my purpose of use with the map service, it would violate with the publicity demand by their license rules (not becuase the code is "secret", but because the page is running internally.</p>
<p>Anyways, I'm now searching for a more flexible, and more open source friendly source. And thats why I'm here, trying to figure out how to work with OSM etc.</p>
<p>I read some information about "Open Geocode Service with MapQuest" <a href="http://open.mapquestapi.com/geocoding/">link</a> But I can't figure out, how to turn the request into lng and lat that I can turn into markers?? My aim is to via geocode, turn each of my address in the database, into a marker on the map (preferable OSM).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '13, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/406f20e7659f1db024c0a9fdac71522e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grmihel&#39;s gravatar image" />
<p><span>Grmihel</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grmihel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '13, 16:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-19285" class="comments-container">
&#10;</div>
<div id="comment-tools-19285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19285-form-container" class="comment-form-container">
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

<span id="19298"></span>

<div id="answer-container-19298" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19298-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A side-note: OSM data (also google's data) is incomplete - you probably will not get a (or only get a very approximate) location for every address.</p>
<p>How to do geocoding with OSM data? You already mentioned the right keyword/tag. See the <span>questions tagged <em>geocoding</em></span> (also try other tags or searches on this help page - this is a very popular topic for which you will find many answers). Shortcut - see: <span>our docu wiki's entry about <em>Nominatim</em></span>.</p>
<p>If you are also searching for a JS library for displaying a map with markers, then you may want to have a look at <em><a href="https://wiki.openstreetmap.org/wiki/Leaflet">Leaflet</a></em>.</p>
<p>If you find some more accurate info matching your question, please add it as an answer yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '13, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '13, 15:24</strong> </span></p>
</div>
</div>
<div id="comments-container-19298" class="comments-container">
&#10;</div>
<div id="comment-tools-19298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19298-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19335"></span>

<div id="answer-container-19335" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I already did some research around, but it seems to me to be a little hard to find an equally to Google geocode structure.</p>
<pre><code>function geocodeMe(pAddress, type) {
            geocoder.geocode({
                &#39;address&#39;: pAddress
            },
            function(result, status){
                if(status == google.maps.GeocoderStatus.OK){
                    map.setCenter(result[0].geometry.location);
                    var icon = customertypeIcons[type] || customertypeIcons[&#39;Unknown&#39;];
                    var marker = new google.maps.Marker({
                        map: map,
                        icon: icon.icon,
                        shadow: icon.shadow,
                        position: result[0].geometry.location,
                        title: icon.title
                    });
                } else{
                    alert(&#39;Geocode was not successful for the following reason: &#39; + status);
                }
            });
        }</code></pre>
<p>Right now with my OSM/OMQ experiment, I'm using the HTTP URL to get lat and lng from an address, and turn it into a marker on the map. But I'm getting lost in how to hand over custom parameters, and what is possible with it. My currently experiment code look like:</p>
<pre><code>            function doClick(url) {
            var script = document.createElement(&#39;script&#39;);
            script.type = &#39;text/javascript&#39;;
            script.src = url;
            document.body.appendChild(script);
        }
&#10;        function renderGeocode(response) {
            var location = response.results[0].locations[0];
            if(location != undefined){
                //console.log(location);
                markers.addMarker(new OpenLayers.Marker(LngLat(location.latLng.lng, location.latLng.lat), icon));
                markers.addMarker(new OpenLayers.Marker(LngLat(location.latLng.lng, location.latLng.lat), icon.clone()));
            }
        }</code></pre>
<p>But since the functions already run in a JS on a htm page, it seems quiet pointless doing the first codeblock. But I can't find a more smooth way to handle the geocoding block...?? Ain't it possible to use eg. Open Map Quest more like the Google.geocoder ?? (Couldn't seem to find any other threads giving me a hint to work on :( )</p>
<p>Edit: I'm calling the doClick function with url string as: <a href="http://open.mapquestapi.com/geocoding/v1/address?location=&#39;+address+&#39;&amp;callback=renderGeocode">http://open.mapquestapi.com/geocoding/v1/address?location='+address+'&amp;callback=renderGeocode</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '13, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/406f20e7659f1db024c0a9fdac71522e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grmihel&#39;s gravatar image" />
<p><span>Grmihel</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grmihel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '13, 09:57</strong> </span></p>
</div>
</div>
<div id="comments-container-19335" class="comments-container">
&#10;</div>
<div id="comment-tools-19335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19335-form-container" class="comment-form-container">
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

