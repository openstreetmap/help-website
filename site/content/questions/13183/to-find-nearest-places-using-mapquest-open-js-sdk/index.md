+++
type = "question"
title = "To find nearest places using mapquest open js sdk"
description = '''Hi, I am new to osm and i am using mapquest open js sdk, i have done the custom map search using map.nominatimSearchAndAddLocation now i wanted to show the nearest places like hospitals,schools,hotels...etc around the placelike in mapquest . How do i do this? please help me out. for reference i used...'''
date = "2012-06-01T09:27:00Z"
lastmod = "2012-06-01T09:27:00Z"
weight = 13183
keywords = [ "nominatim", "osm", "customization" ]
aliases = [ "/questions/13183" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [To find nearest places using mapquest open js sdk](/questions/13183/to-find-nearest-places-using-mapquest-open-js-sdk)

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
<span id="post-13183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am new to osm and i am using mapquest open js sdk, i have done the custom map search using <strong><em>map.nominatimSearchAndAddLocation</em></strong> now i wanted to show the nearest places like hospitals,schools,hotels...etc around the place<a href="http://open.mapquest.com">like in mapquest</a> . How do i do this? please help me out.</p>
<p>for reference i used this code</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
&lt;script src=&quot;http://open.mapquestapi.com/sdk/js/v6.1.0/mqa.toolkit.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js&quot;&gt;&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
&#10;$(document).ready(function() {
&#10;window.map = new MQA.TileMap( /*constructs an instance of MQA.TileMap*/
document.getElementById(&#39;map&#39;), /*ID of element on the page where you want the map added*/
3, /*intial zoom level of the map*/
{lat:12.976418, lng:77.6158}, /*center of map in latitude/longitude */
&#39;map&#39;); /*map type (map)*/
// for zooming control
MQA.withModule(&#39;carouselcontrol&#39;,&#39;shapes&#39;,&#39;georssdeserializer&#39;,&#39;remotecollection&#39;,&#39;smallzoom&#39;, function() {
map.addControl(
new MQA.SmallZoom(),
new MQA.MapCornerPlacement(MQA.MapCorner.TOP_LEFT, new MQA.Size(5,5))
);
});
&#10;});
&#10;function search_phase() {
var from = document.getElementById(&#39;fromLoc&#39;).value;//alert(from);
MQA.withModule(&#39;nominatim&#39;, function() {
&#10;/*Executes a Nominatim search and adds result to the map*/
map.nominatimSearchAndAddLocation(from, null);
&#10;});
&#10;}
&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;form id=&quot;getPOI&quot;&gt;
&lt;input type=&quot;text&quot; id=&quot;fromLoc&quot; name=&quot;fromLoc&quot; value=&quot;&quot;&gt;
&lt;input type=&quot;button&quot; value=&quot;Search in Map&quot; onClick=&quot;search_phase();&quot;&gt;
&lt;/form&gt;
&#10;&lt;div id=&#39;map&#39; style=&#39;width:950px; height:625px;&#39;&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '12, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e5d7a10853a60bd2257989437490cc74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raj&#39;s gravatar image" />
<p><span>Raj</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '12, 09:27</strong> </span></p>
</div>
</div>
<div id="comments-container-13183" class="comments-container">
&#10;</div>
<div id="comment-tools-13183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

