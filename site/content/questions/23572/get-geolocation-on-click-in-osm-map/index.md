+++
type = "question"
title = "[closed] get Geolocation  on click in OSM Map"
description = '''Hi, I need to display a marker on map when i clicked on the map and also i have to fetch the address of that gps point  OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {   defaultHandlerOptions: {  &#x27;single&#x27;: true,  &#x27;double&#x27;: false,  &#x27;pixelTolerance&#x27;: 0,  &#x27;stopSingle&#x27;: false,  &#x27;stopDo...'''
date = "2013-06-21T11:26:00Z"
lastmod = "2013-06-24T22:13:00Z"
weight = 23572
keywords = [ "openlayers" ]
aliases = [ "/questions/23572" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] get Geolocation on click in OSM Map](/questions/23572/get-geolocation-on-click-in-osm-map)

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
<span id="post-23572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to display a marker on map when i clicked on the map and also i have to fetch the address of that gps point</p>
<p>OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {<br />
defaultHandlerOptions: { 'single': true, 'double': false, 'pixelTolerance': 0, 'stopSingle': false, 'stopDouble': false },</p>
<pre><code>initialize: function(options) {
    this.handlerOptions = OpenLayers.Util.extend(
    {}, this.defaultHandlerOptions
        );
    OpenLayers.Control.prototype.initialize.apply(
        this, arguments
        ); 
    this.handler = new OpenLayers.Handler.Click(
        this, {
            &#39;click&#39;: this.trigger
        }, this.handlerOptions
        );
},
&#10;trigger: function(e) {
    var lonlat = map.getLonLatFromPixel(e.xy);
    alert(&quot;You clicked near &quot; + lonlat.lat + &quot; N, &quot; +
        + lonlat.lon + &quot; E&quot;);
}</code></pre>
<p>}); var map; function showGeoFenceMap(){<br />
map = new OpenLayers.Map('geofencMap');<br />
map.addLayers([new OpenLayers.Layer.OSM()]); map.addControl(new OpenLayers.Control.LayerSwitcher()); map.zoomToMaxExtent();<br />
var click = new OpenLayers.Control.Click(); map.addControl(click); click.activate(); }</p>
<p>I have tried this am not getting some strange values. i want to use default layer.</p>
<p>Thanks, Kiran</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '13, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/b804f5576f3607b83d68f3f9dd1f4676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amkiranv&#39;s gravatar image" />
<p><span>amkiranv</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amkiranv has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 Jun '13, 22:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></br></p>
</div>
</div>
<div id="comments-container-23572" class="comments-container">
&#10;</div>
<div id="comment-tools-23572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23572-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by SimonPoole 24 Jun '13, 22:13

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23642"></span>

<div id="answer-container-23642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a specific OpenLayers question and should be asked on an appropriate OL forum.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '13, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '13, 12:51</strong> </span></p>
</div>
</div>
<div id="comments-container-23642" class="comments-container">
&#10;</div>
<div id="comment-tools-23642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23642-form-container" class="comment-form-container">
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

