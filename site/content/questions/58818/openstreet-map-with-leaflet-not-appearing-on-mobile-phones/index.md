+++
type = "question"
title = "Openstreet map with leaflet not appearing on mobile phones"
description = '''I have set up osm on ubuntu below is how my codes are. The issue the map appears perfectly on desktop browser but it doesnt appear on mobile phone browser. What could be issue? Is there any tweak needed for mobile support?  &amp;lt;div id=&quot;right&quot; style=&quot;overflow: auto;width:calc(100%-230px);height: 100v...'''
date = "2017-08-25T14:36:00Z"
lastmod = "2017-08-26T12:49:00Z"
weight = 58818
keywords = [ "mobile", "leaflet", "android", "osm", "ubuntu" ]
aliases = [ "/questions/58818" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Openstreet map with leaflet not appearing on mobile phones](/questions/58818/openstreet-map-with-leaflet-not-appearing-on-mobile-phones)

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
<span id="post-58818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up osm on ubuntu below is how my codes are. The issue the map appears perfectly on desktop browser but it doesnt appear on mobile phone browser. What could be issue? Is there any tweak needed for mobile support?</p>
<pre><code> &lt;div id=&quot;right&quot; style=&quot;overflow: auto;width:calc(100%-230px);height: 100vh; background:#eeeeee;&quot;&gt;
                                       &lt;div id=&quot;map&quot; style=&quot;position:absolute;top:0px;left:230px;right: 0; bottom: 0;width:calc(100%-230px);height:65%;&quot;&gt;
&#10;                                 &lt;/div&gt; 
                                 &lt;div id=&quot;dataTable&quot; style=&quot;overflow: auto;position:absolute;left:230px;right: 0; bottom: 0;width:calc(100%-230px);height:35%;background:#eeeeee;&quot;&gt;
                            &lt;div class=&quot;x_panel&quot;&gt;
                                  &lt;div class=&quot;x_title&quot;&gt;
                                    &lt;h2&gt;Vehicle List &lt;/h2&gt;
                                    &lt;ul class=&quot;nav navbar-right panel_toolbox&quot;&gt;
                                      &lt;li&gt;&lt;a class=&quot;collapse-link&quot;&gt;&lt;i class=&quot;fa fa-chevron-up&quot;&gt;&lt;/i&gt;&lt;/a&gt;
                                      &lt;/li&gt;
                                      &lt;li class=&quot;dropdown&quot;&gt;
                                        &lt;a href=&quot;#&quot; class=&quot;dropdown-toggle&quot; data-toggle=&quot;dropdown&quot; role=&quot;button&quot; aria-expanded=&quot;false&quot;&gt;&lt;i class=&quot;fa fa-wrench&quot;&gt;&lt;/i&gt;&lt;/a&gt;
                                        &lt;ul class=&quot;dropdown-menu&quot; role=&quot;menu&quot;&gt;
                                          &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Settings 1&lt;/a&gt;
                                          &lt;/li&gt;
                                          &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Settings 2&lt;/a&gt;
                                          &lt;/li&gt;
                                        &lt;/ul&gt;
                                      &lt;/li&gt;
                                      &lt;li&gt;&lt;a class=&quot;close-link&quot; onclick=&#39;closeDataTable()&#39;&gt;&lt;i class=&quot;fa fa-close&quot;&gt;&lt;/i&gt;&lt;/a&gt;
                                      &lt;/li&gt;
                                    &lt;/ul&gt;
                                    &lt;div class=&quot;clearfix&quot;&gt;&lt;/div&gt;
                                  &lt;/div&gt;
                                  &lt;div class=&quot;x_content&quot; id=&quot;tableContent&quot;&gt;
&#10;                                    &lt;table id=&quot;dashboardGrid&quot; class=&quot;table &quot; &gt;
                                          &lt;thead&gt;
                                            &lt;tr&gt;
                                                &lt;th&gt;#&lt;/th&gt;
                                              &lt;th&gt;Group&lt;/th&gt;
                                              &lt;th&gt;Sub Group&lt;/th&gt;
                                              &lt;th&gt;Stat.&lt;/th&gt;
                                              &lt;th&gt;Veh. #&lt;/th&gt;
                                              &lt;th&gt;View&lt;/th&gt;
&#10;                                              &lt;/tr&gt;
                                          &lt;/thead&gt;
                                          &lt;tbody &gt;
&#10;
                                          &lt;/tbody&gt;
                                        &lt;/table&gt;
&#10;
                                  &lt;/div&gt;
                               &lt;/div&gt;
                                 &lt;/div&gt;
&#10;                               &lt;/div&gt;</code></pre>
<p>Below is how is my init function for map to appear in the div.</p>
<pre><code> function init() {
             var map = L.map(&#39;map&#39;);
&#10;             //add a tile layer to add to our map, in this case it&#39;s the &#39;standard&#39; OpenStreetMap.org tile server
             L.tileLayer(&#39;http://*.*.*.*/hot/{z}/{x}/{y}.png&#39;, {
                attribution: &#39;&amp;copy; &lt;a href=&quot;http://openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt; contributors&#39;,
                maxZoom: 18
             }).addTo(map);
&#10;             map.attributionControl.setPrefix(&#39;&#39;); // Don&#39;t show the &#39;Powered by Leaflet&#39; text. Attribution overload
&#10;             var london = new L.LatLng(-1.935114,30.082111); // geographical point (longitude and latitude)
             map.setView(london, 13);
             var redMarker = L.ExtraMarkers.icon({
                    icon: &#39;fa-motorcycle&#39;,
                    markerColor: &#39;orange-dark&#39;,
                    shape: &#39;circle&#39;,
                    prefix: &#39;fa&#39;
                   });
                   var myPopup = L.DomUtil.create(&#39;div&#39;, &#39;infoWindow&#39;);
           myPopup.innerHTML = &quot;&lt;div id=&#39;info&#39;&gt;&lt;p id=&#39;title&#39;&gt;title&lt;/p&gt;&lt;p&gt;address&lt;/p&gt;&lt;/div&gt;&quot;;
                   L.marker([-1.935114,30.082111], {icon: redMarker,}).addTo(map).bindPopup(myPopup);
                   //L.marker([-1.935114,30.082111], {icon: redMarker,}).addTo(map).bindPopup(&#39;&lt;strong&gt;Science Hall&lt;/strong&gt;&lt;br&gt;Where the GISC was born.&#39;);
&#10;
&#10;
                }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '17, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58818" class="comments-container">
&#10;</div>
<div id="comment-tools-58818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58818-form-container" class="comment-form-container">
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

<span id="58829"></span>

<div id="answer-container-58829" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58829-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question has been cross-posted on GIS StackExchange and has an <a href="https://gis.stackexchange.com/a/253360/95194">accepted answer</a> there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '17, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-58829" class="comments-container">
&#10;</div>
<div id="comment-tools-58829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58829-form-container" class="comment-form-container">
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

