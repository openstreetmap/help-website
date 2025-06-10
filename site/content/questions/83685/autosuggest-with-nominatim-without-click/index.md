+++
type = "question"
title = "autosuggest with nominatim without click"
description = '''I use osrm , routing leaflet machine .The autosuggest with nominatim works with click .I want to change it to become autocomplete without click .How I can do it please .'''
date = "2022-03-06T01:01:00Z"
lastmod = "2022-03-09T09:30:00Z"
weight = 83685
keywords = [ "leaflet", "osrm", "nominatim", "routing", "geocoder" ]
aliases = [ "/questions/83685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [autosuggest with nominatim without click](/questions/83685/autosuggest-with-nominatim-without-click)

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
<span id="post-83685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83685-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use osrm , routing leaflet machine .The autosuggest with nominatim works with click .I want to change it to become autocomplete without click .How I can do it please .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '22, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/5f244e94fc71794965555f2b9313df34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aminali1991&#39;s gravatar image" />
<p><span>aminali1991</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aminali1991 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83685" class="comments-container">
&#10;</div>
<div id="comment-tools-83685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83685-form-container" class="comment-form-container">
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

<span id="83689"></span>

<div id="answer-container-83689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83689-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In your code when you initialize the Geocoder to be used for the leaflet-routing-machine, you should add a query parameter of limit=1, e.g.:</p>
<pre><code>geocoder: L.Control.Geocoder.nominatim({serviceUrl:LRM.geocodeServiceUrl, geocodingQueryParams: {&#39;limit&#39;:&#39;1&#39;}}),</code></pre>
<p>By that, you won't get a list of suggestions, but instead the first result is used immediately. So if you type "London" and hit enter, it will choose "London, UK".</p>
<p>Edit: but this won't be a autocomplete in the sense of extending/completing "Londo" to "London, Uk", as nominatim is not capable of doing autocomplete. So if you want a real autocomplete, you would have to switch to e.g. Photon or Pelias.</p>
<p>E.g with Photon you would use:</p>
<pre><code>geocoder: L.Control.Geocoder.photon(),</code></pre>
<p>But please note: autocomplete sends a lot of requests against the Photon API (which in this case is sponsored by Komoot, see <a href="https://photon.komoot.io/">https://photon.komoot.io/</a> ), so please use with care.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '22, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '22, 14:32</strong> </span></p>
</div>
</div>
<div id="comments-container-83689" class="comments-container">
<span id="83696"></span>
<div id="comment-83696" class="comment">
<div id="post-83696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response. Any idea to change geocoder nominatim with pelias or photon and integrated with leaflet routing machine . I have trace route between two points , so I want to do same thing search autocomplete without click and trace route like my old example with niminatim . Thank you in advance.</p>
</div>
<div id="comment-83696-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 12:19)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83697"></span>
<div id="comment-83697" class="comment">
<div id="post-83697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For autocomplete have a look at the example (and the code for map-2 at that example) at <a href="http://www.liedman.net/leaflet-routing-machine/tutorials/geocoders/">http://www.liedman.net/leaflet-routing-machine/tutorials/geocoders/</a> Section: autocomplete, which uses OpenRouteService geocoding API (you'll need an API key for that one).</p>
<p>But I'm still not 100% sure if you want autocomplete or just predefined values for start and end point in your route. If it is the latter, it would be easier to set them via lat/lon and use nominatim for reverse geocoding.</p>
</div>
<div id="comment-83697-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 13:16)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83699"></span>
<div id="comment-83699" class="comment">
<div id="post-83699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the moment I am using an example similar to the one in the document, it works well, I just wanted to change when typing the suggestions will appear without a click on enter . You tell me to use Photon or Pelias. I don't know how to use it with leaflet routing machine like nominatim .The autocomplete with geocoder is functional but with click enter and I can't change it without click like in privacy for api .</p>
</div>
<div id="comment-83699-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 14:20)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83700"></span>
<div id="comment-83700" class="comment">
<div id="post-83700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, so you just want autocomplete while typing. I updated the answer above showing how to use the Photon geocoder in leaflet-routing-machine (the suggestions appear without hitting enter or clicking, but you'll still have to choose one of the suggestions from autocomplete with a click). If that example helps, please use the accept answer link above.</p>
</div>
<div id="comment-83700-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 14:34)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83701"></span>
<div id="comment-83701" class="comment">
<div id="post-83701-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response and guide .The autocomplete without click , this what I need , but I want to save the same work like with nominatim . search address start , address end then trace route on leaflet map .The language used by photon is java ?</p>
</div>
<div id="comment-83701-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 14:51)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83704"></span>
<div id="comment-83704" class="comment not_top_scorer">
<div id="post-83704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still not sure if I understand your problem correctly (would be nice if you could include a link to your project where it is easier to see where you are right now and what you want to achieve). So you have setup leaflet-routing-machine with nominatim and osrm but now - for autocomplete - want to use Photon.</p>
<p>Then this would be a full basic code example:</p>
<p>L.Routing.control({ routeWhileDragging: true, geocoder: L.Control.Geocoder.photon() }).addTo(map);</p>
</div>
<div id="comment-83704-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 15:21)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83705"></span>
<div id="comment-83705" class="comment not_top_scorer">
<div id="post-83705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes exactly ,just modify autocomplete by photon .I use this instruction L.Routing.control({ routeWhileDragging: true, geocoder: L.Control.Geocoder.photon() }).addTo(map); Igot error "Failed to load resource: net::ERR_NAME_NOT_RESOLVED" https://photon.komoot.de/api/?q=p</p>
</div>
<div id="comment-83705-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 15:31)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83706"></span>
<div id="comment-83706" class="comment not_top_scorer">
<div id="post-83706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are using an outdated version of leaflet-routing-machine/leaflet-geocoder.</p>
<p>The API address of Photon has changed (to <a href="https://photon.komoot.io/?q=p">https://photon.komoot.io/?q=p</a> ), this is corrected in the newest versions of leaflet-routing-machine/leaflet-geocoder.</p>
</div>
<div id="comment-83706-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 15:35)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83707"></span>
<div id="comment-83707" class="comment not_top_scorer">
<div id="post-83707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much , it works , just I want to limit search by countrie for example in france only</p>
</div>
<div id="comment-83707-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 15:42)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83708"></span>
<div id="comment-83708" class="comment not_top_scorer">
<div id="post-83708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could then either use location bias (with zoom and a lon lat and location_bias_scale added as queryParams to photon() or with a bbox added as queryParams to photon(), e.g. for Paris area (roughly):</p>
<p>geocoder: L.Control.Geocoder.photon({geocodingQueryParams: {'bbox': '2.076416,48.734455,2.658691,49.05947'}})</p>
<p>With that, you would e.g. find a Rue Berlin in Paris while typing Berlin, but not Berlin in Germany.</p>
<p>(adjust the bbox values accordingly to your needs, see <a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a> for description of those params).</p>
</div>
<div id="comment-83708-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 16:00)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83710"></span>
<div id="comment-83710" class="comment not_top_scorer">
<div id="post-83710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your helpful .I will try it.</p>
</div>
<div id="comment-83710-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 17:04)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83724"></span>
<div id="comment-83724" class="comment not_top_scorer">
<div id="post-83724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi , I try different params in documentation photon , but the suggestions are not true . I write for example Berlin , differents address appear out of paris</p>
<p>geocoder: L.Control.Geocoder.photon({ geocodingQueryParams: { city: 'paris', lang: 'fr' }}),</p>
</div>
<div id="comment-83724-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 10:44)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83725"></span>
<div id="comment-83725" class="comment not_top_scorer">
<div id="post-83725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't see a "city" query param documented in <a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a> , so I see no reason why your example should work as you want in using a unknown city parameter. Why don't you use a bbox if e.g. you want to limit results for the city of Paris? That at least will come close (that is having some suburbs included depending on your minLon,minLat,maxLon,maxLat values).</p>
</div>
<div id="comment-83725-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 10:52)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83727"></span>
<div id="comment-83727" class="comment not_top_scorer">
<div id="post-83727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your response .I'm sorry it's the first time I've used it, that's why I ask a lot of questions</p>
</div>
<div id="comment-83727-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 11:19)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83729"></span>
<div id="comment-83729" class="comment not_top_scorer">
<div id="post-83729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use this bbox values like in documentation bbox=9.5,51.5,11.5,53.5 , normally we get results of berlin . I write France , we display result of france .</p>
<p>geocoder: L.Control.Geocoder.photon({ geocodingQueryParams: { bbox: '9.5,51.5,11.5,53.5' }}),</p>
<p>for this param "?q=berlin", Ican't change it ?</p>
</div>
<div id="comment-83729-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 11:58)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83736"></span>
<div id="comment-83736" class="comment not_top_scorer">
<div id="post-83736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm sorry to say this but if you have no experience in web development (javascript, using APIs, reading documentations etc.) and no gis experience (e.g. spinning up the right bbox for France) I dearly hope you are not trying to achieve this for a business project (or a research project for university in either CS or geography). If you do need this for a business/institutional project, you may think about using Pelias instead of Photon (as Pelias would have a boundary.country Parameter that could be used with a value of FRA for France, but you would need an API key by geocode.earth and spend at least 100$/month).</p>
<p>If you do this just for fun and want to stick with Photon, than please use (as an example) e.g. a southwest and a northeast point (with values mLon &amp; mLat for southwest and maxLon &amp; maxLat for northeast) that will spin up a rectangle across (mainland) France.</p>
<p>Now I just spun up a rough estimate for mainland France (including the island of Corse):</p>
<p>geocoder: L.Control.Geocoder.photon({geocodingQueryParams: {'bbox': '-4.262695,41.376809,9.228516,51.672555'}})</p>
<p>(continued in next comment ...)</p>
</div>
<div id="comment-83736-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 15:11)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83737"></span>
<div id="comment-83737" class="comment not_top_scorer">
<div id="post-83737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(last comment continued)</p>
<p>Now if you search Berlin (?q=Berlin), you'll still get some results outside of France (that are e.g. in Switzerland or Germany close to the border of France) but most will be in France and none in Berlin, Germany (as the city of Berlin is outside of that rectangle). And searching for "New York" will get you e.g. an fastfood restaurant in Metz, France but no city or state in the U.S.</p>
</div>
<div id="comment-83737-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 15:11)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83739"></span>
<div id="comment-83739" class="comment not_top_scorer">
<div id="post-83739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you .I speak of experiences to use this api because even the documentation is not too much, but just to simulate things because with the "nominatim" api the search is very precise (except the click to see the suggestions) and with the api photon even the suggestions are not good: for example with "nominatim" always there is the name of the country at the end of the searched word (like google map), here name,the only word "paris" is displayed identically several times but clicking on such a "paris" brings you to a different place, it's good here but just to differentiate that's all, more readability.For example with "nominatim" : Paris, Île-de-France, France métropolitaine, France I applied what is on the document but the result remains far away, that is why I am asking for your help, not for fun.</p>
</div>
<div id="comment-83739-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 15:33)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83740"></span>
<div id="comment-83740" class="comment not_top_scorer">
<div id="post-83740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's why I wouldn't recommend an autocomplete API at all as Nominatim results are much better in my experience that any of those autocomplete solutions. But you are eager on using autocomplete so I'm trying to show you the (not perfect) solutions there are. But then as I said before: a link to your project or more information on what you need would be helpful. E.g. you want autocomplete results of only city names in France, then I would use:</p>
<p>geocoder: L.Control.Geocoder.photon({geocodingQueryParams: {'bbox': '-4.262695,41.376809,9.228516,51.672555','osm_tag':'place:city','osm_tag':'place:town','osm_tag':'place:village'}})</p>
<p>But this example may be of no help as I'm still left in the dark about which data you want to get out of those start and end point search boxes.</p>
</div>
<div id="comment-83740-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 15:46)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83743"></span>
<div id="comment-83743" class="comment not_top_scorer">
<div id="post-83743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you for your patience and help . For example here <a href="https://www.liedman.net/leaflet-control-geocoder/">https://www.liedman.net/leaflet-control-geocoder/</a></p>
<p>with option "photon" clicked , when enter "Lille" the result appear with name country at end , and more than word (Lille, Lille, Hauts-de-France, France...) In my case when enter "Lille" appear: Lille (in first line), Lille(in second line), Lille(third line) ... the same word without more indication The resuly here is goog : <a href="https://photon.komoot.io/">https://photon.komoot.io/</a> When compare result with this link , in my case , only text in bold appear</p>
<p>How I can do search like in documentation link</p>
</div>
<div id="comment-83743-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 16:17)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83744"></span>
<div id="comment-83744" class="comment not_top_scorer">
<div id="post-83744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I does look as if you are not using the default options for Photon in Leaflet-Control-Geocoder. That's why it would be so great to see your code example, e.g. trough jsfiddle or a similar tool.</p>
<p>Anyway, try this:</p>
<p>geocoder: L.Control.Geocoder.photon({geocodingQueryParams: {'bbox': '-4.262695,41.376809,9.228516,51.672555','osm_tag':['place:city','place:town','place:village']},nameProperties:['name', 'street', 'suburb', 'hamlet', 'town', 'city', 'state', 'country']})</p>
</div>
<div id="comment-83744-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 17:10)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83746"></span>
<div id="comment-83746" class="comment not_top_scorer">
<div id="post-83746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the link of example is : <a href="https://jsfiddle.net/Aminali/kLs34ef8/7/">https://jsfiddle.net/Aminali/kLs34ef8/7/</a></p>
</div>
<div id="comment-83746-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 21:53)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
<span id="83747"></span>
<div id="comment-83747" class="comment not_top_scorer">
<div id="post-83747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You had an old version of leaflet-control-geocoder (v1.5.5 instead of 2.4.0) in there.</p>
<p>Here is a basic example: <a href="https://jsfiddle.net/y0osacwh/1/">https://jsfiddle.net/y0osacwh/1/</a> (and you should include each external source via ssl, e.g. tiles as well. I changed that as well).</p>
</div>
<div id="comment-83747-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 22:37)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83759"></span>
<div id="comment-83759" class="comment not_top_scorer">
<div id="post-83759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your guide and help .I try it . It's working</p>
</div>
<div id="comment-83759-info" class="comment-info">
<span class="comment-age">(09 Mar '22, 09:30)</span> <span class="comment-user userinfo">aminali1991</span>
</div>
</div>
</div>
<div id="comment-tools-83689" class="comment-tools">
<span class="comments-showing"> showing 5 of 24 </span> <a href="#" class="show-all-comments-link">show 19 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-83689-form-container" class="comment-form-container">
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

