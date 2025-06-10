+++
type = "question"
title = "Mosets tree google maps"
description = '''I am using joomla components mosetstree with Google Maps positioning for companies. Unfortunately Google Maps does not have a map of my town, but OpenStreetMap does. I don&#x27;t know how to incorporate the OpenStreetMap layer, so could you please help me? Here is the code of the map page from mosetstree...'''
date = "2012-11-12T18:45:00Z"
lastmod = "2012-11-13T22:51:00Z"
weight = 17660
keywords = [ "mosetstree", "google" ]
aliases = [ "/questions/17660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mosets tree google maps](/questions/17660/mosets-tree-google-maps)

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
<span id="post-17660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using joomla components mosetstree with Google Maps positioning for companies. Unfortunately Google Maps does not have a map of my town, but OpenStreetMap does. I don't know how to incorporate the OpenStreetMap layer, so could you please help me? Here is the code of the map page from mosetstree:</p>
<pre><code>&lt;script src=&quot;http://maps.google.com/maps?file=api&amp;amp;v=2&amp;amp;key=&lt;?php echo $this-&gt;mtconf[&#39;gmaps_api_key&#39;]; ?&gt;&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
    var map = null;
    var geocoder = null;
    function initialize() {
        if (GBrowserIsCompatible()) {
        map = new GMap2(document.getElementById(&quot;map&quot;));
        &lt;?php
        echo &#39;var center = new GLatLng(&#39; . $this-&gt;link-&gt;lat . &#39;, &#39; . $this-&gt;link-&gt;lng . &#39;);&#39; . &quot;\n&quot;;
        echo &#39;map.setCenter(center, &#39; . ($this-&gt;link-&gt;zoom?$this-&gt;link-&gt;zoom:13) . &#39;);&#39; . &quot;\n&quot;;
        if( $this-&gt;mtconf[&#39;map_control&#39;] != &#39;&#39; ) {
            $mapcontrols = explode(&#39;,&#39;,$this-&gt;mtconf[&#39;map_control&#39;]);
            foreach( $mapcontrols AS $mapcontrol ) {
                echo &#39;map.addControl(new &#39;.$mapcontrol.&#39;());&#39; . &quot;\n&quot;;
            }
        }
        ?&gt;
        marker = new GMarker(center);
        map.addOverlay(marker);
        }
    }
    jQuery(document).ready(function(){initialize();});
    jQuery(document).unload(function(){GUnload();});
&lt;/script&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mosetstree" rel="tag" title="see questions tagged &#39;mosetstree&#39;">mosetstree</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '12, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/67cad50960f2b8d9ad99fa41b4c19797?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mile&#39;s gravatar image" />
<p><span>Mile</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mile has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '12, 00:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-17660" class="comments-container">
&#10;</div>
<div id="comment-tools-17660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17660-form-container" class="comment-form-container">
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

<span id="17683"></span>

<div id="answer-container-17683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GMap, <a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example">OpenLayers</a>, and <a href="http://leafletjs.com/">Leaflet</a> are all used in pretty much the same way. You create a map object, initialize it with an html object to draw into and a latitude/longitude/zoom, and the rest (for your usecase) are optional niceties.</p>
<p>See the two previous links for examples, and adapt them to your php code.</p>
<p>Note that you don't need an API key to use OSM tiles. Alsom the map_controls are probably named differently between libraries, so you should either :</p>
<ul>
<li>Change the mtconf config values</li>
<li>Let php translate between the gmap names and the openlayers/leaflet names</li>
<li>Use a hardcoded set of map controls</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '12, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-17683" class="comments-container">
<span id="17690"></span>
<div id="comment-17690" class="comment">
<div id="post-17690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was hopping someone will help me just to insert openstreet layer within existing map file. I have basic knowledge of coding, meaning im not able to do it alone without detail instructions. However thank you !</p>
</div>
<div id="comment-17690-info" class="comment-info">
<span class="comment-age">(13 Nov '12, 15:24)</span> <span class="comment-user userinfo">Mile</span>
</div>
</div>
<span id="17700"></span>
<div id="comment-17700" class="comment">
<div id="post-17700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It really is quite straightforward. Follow one of the examples or tutorials on openlayer of leaflet website.</p>
<p>The only two changes you need to make is to leave the "jQuery(document).ready(function(){initialize();});" line at the end of the script, and use php code like "&lt;?php echo $this-&gt;link-&gt;lat ?&gt;" instead of the lat/long/zoom values.</p>
<p>If it doesn't work, check for javascript errors in your borwser's debug console (for example the "firebug" extension of firefox) and check for php errors in your server logs.</p>
</div>
<div id="comment-17700-info" class="comment-info">
<span class="comment-age">(13 Nov '12, 22:51)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17683-form-container" class="comment-form-container">
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

