+++
type = "question"
title = "city search in openlayers, openstreetmap"
description = '''I am new with Openlayers and OpenStreetMap. I need to insert in the map a search city. In order to write the name of city, click on button, and get the position of the city in the map. Could anybody help me? I show the code I use, well in the linia var jsonurl = &quot;/data/2.1/find/name?q=&quot;+param; I rea...'''
date = "2014-10-05T09:54:00Z"
lastmod = "2014-10-15T14:43:00Z"
weight = 37308
keywords = [ "openstreetmap", "city", "search", "openlayers" ]
aliases = [ "/questions/37308" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [city search in openlayers, openstreetmap](/questions/37308/city-search-in-openlayers-openstreetmap)

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
<span id="post-37308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new with Openlayers and OpenStreetMap. I need to insert in the map a search city. In order to write the name of city, click on button, and get the position of the city in the map. Could anybody help me? I show the code I use, well in the linia var jsonurl = "/data/2.1/find/name?q="+param; I really don't have the script name,...it fails here, .... thank you in advanced...</p>
<pre><code>&lt;html&gt;
&lt;head&gt;&lt;title&gt;OpenLayers&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;div id=&quot;mapdiv&quot;&gt;
&lt;form id=&quot;searchform&quot; action=&quot;#&quot; method=&quot;get&quot; style=&quot;display:inline&quot; 
onsubmit=&quot;FindCity(); return false&quot;&gt;
&lt;input type=&quot;text&quot; id=&quot;query_str&quot; name=&quot;query_str&quot; value=&quot;London, UK&quot; 
onfocus=&quot;this.value = (this.value==&#39;London, UK&#39;)? &#39;&#39; : this.value;&quot;&gt;
&lt;input type=&quot;submit&quot; value=&quot; Find &quot;&gt;
&lt;/form&gt;
&lt;/div&gt;
  &lt;link rel=&quot;stylesheet&quot; href=&quot;/OpenLayers-2.13.1/theme/default/google.css&quot; type=&quot;text/css&quot;&gt;
 &lt;script src=&quot;http://maps.google.com/maps/api/js?v=3.3&amp;sensor=false&quot;&gt;&lt;/script&gt;
 &lt;script type=&quot;text/javascript&quot; src=&quot;/OpenLayers-2.13.1/OpenLayers.js&quot;&gt; &lt;/script&gt;
  &lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
  &lt;script&gt;
&#10;
&#10;
    map = new OpenLayers.Map(&quot;mapdiv&quot;);
    map.addLayer(new OpenLayers.Layer.OSM());
&#10;    var pois = new OpenLayers.Layer.Text( &quot;My Points&quot;,
                    { location:&quot;data1.txt&quot;,
                      projection: map.displayProjection
                    });
    map.addLayer(pois);
&#10;
    //Set start centrepoint and zoom
    //TODO: Is it possible to just zoom to extents of defined markers instead?
&#10;    var lonLat = new OpenLayers.LonLat( 1.00, 41.00 )
          .transform(
            new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
            map.getProjectionObject() // to Spherical Mercator Projection
          );
    var zoom=7;
    map.setCenter (lonLat, zoom);
&#10;   function getSearchData(JSONtext)
{
    console.log( JSONtext  );
    JSONobject = ParseJson(JSONtext);
&#10;    city = JSONobject.list;
    if( city.length == 0 ) {
        ShowAlertMess( &#39;not found&#39; );
        return;
    }
&#10;    var centre = new OpenLayers.LonLat(city[0].coord.lon, city[0].coord.lat);
    centre.transform(
            new OpenLayers.Projection(&quot;EPSG:4326&quot;),
            new OpenLayers.Projection(&quot;EPSG:900913&quot;)
    );
    map.setCenter( centre, 10);
&#10;//  alert(JSONobject.cod);
}
&#10;function FindCity()
{
    param = document.getElementById(&#39;query_str&#39;).value;
&#10;    var jsonurl = &quot;/data/2.1/find/name?q=&quot;+param;
    $.get(jsonurl, getSearchData).error(errorHandler);
    return false;   
}
&#10;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '14, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/e44da925db32c7426caea318c4d319b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="enric73&#39;s gravatar image" />
<p><span>enric73</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="enric73 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '14, 23:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-37308" class="comments-container">
&#10;</div>
<div id="comment-tools-37308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37308-form-container" class="comment-form-container">
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

<span id="37633"></span>

<div id="answer-container-37633" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an example here of geocoding , <a href="http://dev.openlayers.org/examples/openls.html,">http://dev.openlayers.org/examples/openls.html,</a> thank you everybody</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '14, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/e44da925db32c7426caea318c4d319b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="enric73&#39;s gravatar image" />
<p><span>enric73</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="enric73 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37633" class="comments-container">
&#10;</div>
<div id="comment-tools-37633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37633-form-container" class="comment-form-container">
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

