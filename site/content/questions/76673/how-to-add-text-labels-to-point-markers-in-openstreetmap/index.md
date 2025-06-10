+++
type = "question"
title = "How to add text labels to point markers in OpenStreetMap?"
description = '''I have looked at this webpage: link text [https://mediarealm.com.au/articles/openstreetmap-openlayers-map-markers/]  and I learned from it how to make markers on Openstreetmap. But I can&#x27;t figure out how to make simple text labels appear beside the markers. My question is what is the simplest way to...'''
date = "2020-09-17T06:53:00Z"
lastmod = "2020-09-18T08:21:00Z"
weight = 76673
keywords = [ "marker", "labels", "openlayers" ]
aliases = [ "/questions/76673" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to add text labels to point markers in OpenStreetMap?](/questions/76673/how-to-add-text-labels-to-point-markers-in-openstreetmap)

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
<span id="post-76673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76673-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have looked at this webpage: <a href="https://mediarealm.com.au/articles/openstreetmap-openlayers-map-markers/">link text</a> [<a href="https://mediarealm.com.au/articles/openstreetmap-openlayers-map-markers/%5D">https://mediarealm.com.au/articles/openstreetmap-openlayers-map-markers/]</a> and I learned from it how to make markers on Openstreetmap. But I can't figure out how to make simple text labels appear beside the markers. My question is what is the simplest way to add labels to point markers ?</p>
<p>Here is "my" html code, which executes fine, but I want very much to place labels beside some or all of the point markers.</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;utf-8&quot;&gt;
    &lt;title&gt;OpenStreetMap &amp;amp; OpenLayers - Marker Example&lt;/title&gt;
    &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://openlayers.org/en/v4.6.5/css/ol.css&quot; type=&quot;text/css&quot;&gt;
    &lt;script src=&quot;https://openlayers.org/en/v4.6.5/build/ol.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&#10;  &lt;script&gt;
    /* OSM &amp; OL example code provided by https://mediarealm.com.au/ */
    var map;
    var mapLat = 48.7776;
        var mapLng = 9.2325;
    var mapDefaultZoom = 18;
&#10;    function initialize_map() {
      map = new ol.Map({
        target: &quot;map&quot;,
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM({
                      url: &quot;https://a.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;
                })
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([mapLng, mapLat]),
            zoom: mapDefaultZoom
        })
      });
    }
&#10;    function add_map_point(lat, lng) {
      var vectorLayer = new ol.layer.Vector({
        source:new ol.source.Vector({
          features: [new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.transform([parseFloat(lng), parseFloat(lat)], &#39;EPSG:4326&#39;, &#39;EPSG:3857&#39;)),
            })]
        }),
        style: new ol.style.Style({
          image: new ol.style.Icon({
            anchor: [0.5, 0.5],
            anchorXUnits: &quot;fraction&quot;,
            anchorYUnits: &quot;fraction&quot;,
            src: &quot;https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg&quot;
          })
        })
      });
&#10;      map.addLayer(vectorLayer); 
    }
&#10;
  &lt;/script&gt;
&lt;/head&gt;
&lt;body onload=&quot;initialize_map(); 
add_map_point(48.77896195414604,9.230028522859172); 
add_map_point(48.7786801583205,9.230559183581361);
add_map_point(48.77839084836044,9.231098387395592);
add_map_point(48.77821941685653,9.231418825146253);
add_map_point(48.77804116552051,9.231760731524432);
add_map_point(48.77798478095757,9.231857591770742);
add_map_point(48.77793479182441,9.231959233055916);
add_map_point(48.77789216864531,9.232040697691321);
add_map_point(48.77784976059397,9.232119391875452);
add_map_point(48.77781607964182,9.232180591830247);
add_map_point(48.77777605784195,9.232255409342331);
add_map_point(48.777739956673585,9.23232386240085);
add_map_point(48.777706621280934,9.232386290075267);
add_map_point(48.77763025798431,9.232529500384944);
add_map_point(48.77761124414772,9.232578962345501);
add_map_point(48.777568643085125,9.232685348589783);
add_map_point(48.77754476950222,9.232746865393798);
add_map_point(48.77750088469463,9.232827356487206);
add_map_point(48.77745878318328,9.232910790311317);
add_map_point(48.77741595800813,9.232988600498913);
add_map_point(48.777372755115806,9.233068552599766);
add_map_point(48.777201514799266,9.233379369818085);
add_map_point(48.77702467842831,9.23369803172393);
add_map_point(48.776762657751405,9.234164000387091);
add_map_point(48.77647984081625,9.234622534964592); 
&quot;&gt;
  &lt;div id=&quot;map&quot; style=&quot;width: 100vw; height: 100vh;&quot;&gt;&lt;/div&gt;
hallo
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '20, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8c554f4407ec63d0211bf83fae0b11df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="funOne&#39;s gravatar image" />
<p><span>funOne</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="funOne has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '20, 21:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-76673" class="comments-container">
<span id="76674"></span>
<div id="comment-76674" class="comment">
<div id="post-76674-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you fix/edit your question please? The links have gone missing.</p>
</div>
<div id="comment-76674-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 07:41)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="76687"></span>
<div id="comment-76687" class="comment">
<div id="post-76687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried to paste my entire html document into a code block, but about half of it did not arrive inside the code block, and I don't know why not. If there is somebody who knows how to edit my question, so as to format the text so that everything between "&lt;!DOCTYPE html&gt;" and "&lt;/html&gt;" appears as code, then I thank you.</p>
</div>
<div id="comment-76687-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 20:39)</span> <span class="comment-user userinfo">funOne</span>
</div>
</div>
</div>
<div id="comment-tools-76673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76673-form-container" class="comment-form-container">
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

<span id="76676"></span>

<div id="answer-container-76676" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76676-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="funOne has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without knowing what you have tried so far (your question does not include links) I suggest you have a look at <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a>. There you are flexible to add markers with text labels of different kinds and appearances. Chose one of the instances given on the wiki page I linked to and give it a try.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '20, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76676" class="comments-container">
<span id="76685"></span>
<div id="comment-76685" class="comment">
<div id="post-76685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for telling me about uMap. That would be a perfectly good solution, except that their tiles won't load to a zoom level greater than 17 in the area that I am concerned with. Here is the map I created with uMap: [<a href="http://umap.openstreetmap.fr/en/map/anonymous-edit/499933:HZ_0NpNev93W6HehUzJ2OItXQsw">http://umap.openstreetmap.fr/en/map/anonymous-edit/499933:HZ_0NpNev93W6HehUzJ2OItXQsw</a> ]. An alternative solution might be something like what is contained in this script here: [<a href="http://dev.openlayers.org/examples/vector-features-with-text.html">http://dev.openlayers.org/examples/vector-features-with-text.html</a> ]. There you can see markers, but there are also text labels with the markers. I have tried to download the html source code of that page and to load it from my own computer, but that doesn't work, possibly because my browser doesn't know where to find some remote scripts that are given with reltive path names. So I am not even able to dissect that example, which is surprisingly the only example of Openlayers that I could find where label appear beside markers.</p>
<p>At the end of the day, all I want to do is place a marker at a location in WGS84 coordinates and place a text label beside the marker, and then zoom in to level 19. Any help is appreciated!</p>
</div>
<div id="comment-76685-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 20:22)</span> <span class="comment-user userinfo">funOne</span>
</div>
</div>
<span id="76688"></span>
<div id="comment-76688" class="comment">
<div id="post-76688-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18988/funone">@funOne</a> for me tiles are loading to a max zoom of 20 with that umap link. If the server has not had to display that area recently it can take a while to render depending on server load.</p>
<p>Note also that the umap background can be changed to openstreetmap.org's default if you wish (although that only goes to z19).</p>
<p>You can set the starting view with the <img src="https://wiki.openstreetmap.org/w/images/thumb/9/98/Icon-center.PNG/30px-Icon-center.PNG" alt="diagonal arrows pointing inward to dot" /> icon on the right.</p>
</div>
<div id="comment-76688-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 21:17)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76689"></span>
<div id="comment-76689" class="comment">
<div id="post-76689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have waited for more than one hour, in which time the tile still has not loaded. Thanks for suggesting that I try changing from umap background to openstreetmap background. Openstreetmap background tile loads within 4.2 seconds: good enough. You mentioned how to set the starting view using the graphical interface. But how to set the starting map background to use Openstreetmap rather than OSM-Fr?</p>
</div>
<div id="comment-76689-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 23:26)</span> <span class="comment-user userinfo">funOne</span>
</div>
</div>
<span id="76692"></span>
<div id="comment-76692" class="comment">
<div id="post-76692-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can change the starting layer also in the right hand editing panel. It's the same icon as in the left hand panel.</p>
</div>
<div id="comment-76692-info" class="comment-info">
<span class="comment-age">(18 Sep '20, 08:21)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76676-form-container" class="comment-form-container">
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

