+++
type = "question"
title = "[closed] display waypoint names in openlayers map"
description = '''I can easily display a GPX track on an openlayers map using the example code at https://wiki.openstreetmap.org/wiki/Openlayers_Track_example or by using this alternative code I can also display waypoints (but not their names): var myStyleMap = new OpenLayers.StyleMap({&quot;default&quot;: new OpenLayers.Style(...'''
date = "2012-01-14T16:03:00Z"
lastmod = "2013-03-28T16:57:00Z"
weight = 9959
keywords = [ "track", "gpx", "openlayers", "waypoints" ]
aliases = [ "/questions/9959" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] display waypoint names in openlayers map](/questions/9959/display-waypoint-names-in-openlayers-map)

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
<span id="post-9959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9959-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can easily display a GPX track on an openlayers map using the example code at <a href="https://wiki.openstreetmap.org/wiki/Openlayers_Track_example">https://wiki.openstreetmap.org/wiki/Openlayers_Track_example</a></p>
<p>or by using this alternative code I can also display waypoints (but not their names):</p>
<pre><code>var myStyleMap = new OpenLayers.StyleMap({&quot;default&quot;: new OpenLayers.Style({pointRadius: 5, fillColor: &quot;darkred&quot;, strokeColor: &quot;red&quot;,    strokeWidth: 3  })
            });
// add the layer with the GPX track and waypoints
var lgpx = new OpenLayers.Layer.Vector(&quot;title&quot;, {
protocol: new OpenLayers.Protocol.HTTP({ url: &quot;my_file.gpx&quot;,
format: new OpenLayers.Format.GPX({extractWaypoints: true,  extractName: true, extractRoutes: true, extractAttributes: true})
}),
strategies: [new OpenLayers.Strategy.Fixed()],
styleMap: myStyleMap, 
projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
});
map.addLayer(lgpx);</code></pre>
<p>I would like to be able to display the names of the waypoints. The waypoints are in the GPX file in the following format:</p>
<pre><code>&lt;wpt lat=&quot;55.90119934&quot; lon=&quot;-3.15706110&quot;&gt;
        &lt;ele&gt;129.4&lt;/ele&gt;
        &lt;time&gt;2010-12-22T20:43:20Z&lt;/time&gt;
        &lt;name&gt;The Waverley&lt;/name&gt;
&lt;/wpt&gt;</code></pre>
<p>I can't fathom the javascript, and there are no examples on the web. Can anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '12, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e82dee06cd9f989e30bc1c57f2afc2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="digby&#39;s gravatar image" />
<p><span>digby</span><br />
<span class="score" title="46 reputation points">46</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="digby has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>14 Jan '12, 17:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-9959" class="comments-container">
&#10;</div>
<div id="comment-tools-9959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9959-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 14 Jan '12, 17:07

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9965"></span>

<div id="answer-container-9965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9965-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="http://trac.osgeo.org/openlayers/wiki/GettingHelp">Getting Help</a> on the OpenLayers forum for ways to find help with OpenLayers. This is the OpenStreetMap help system and your question is not related to OpenStreetMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '12, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9965" class="comments-container">
<span id="18418"></span>
<div id="comment-18418" class="comment">
<div id="post-18418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As far as I'm concerned openlayers is linked with openstreetmap. If you look at the quote above you'll see the link <a href="https://wiki.openstreetmap.org/wiki/Openlayers_Track_example">https://wiki.openstreetmap.org/wiki/Openlayers_Track_example</a> The openlayers help is messy and confusing. The first line "How can I add a question to this FAQ?" does nothing to answer the question. Ironically.</p>
</div>
<div id="comment-18418-info" class="comment-info">
<span class="comment-age">(13 Dec '12, 15:16)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="18451"></span>
<div id="comment-18451" class="comment">
<div id="post-18451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll add to that comment. There is no OpenLayers forum. OpenLayers help is terrible. It is no help at all. In fact I can't find any way of asking a question.</p>
</div>
<div id="comment-18451-info" class="comment-info">
<span class="comment-age">(14 Dec '12, 13:55)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
<span id="18454"></span>
<div id="comment-18454" class="comment">
<div id="post-18454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try the <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">mailing list</a> or Stack Exchange (<a href="http://gis.stackexchange.com/questions/tagged/openlayers">GIS</a>, <a href="http://stackoverflow.com/questions/tagged/openlayers">Stackoverflow</a>).</p>
</div>
<div id="comment-18454-info" class="comment-info">
<span class="comment-age">(14 Dec '12, 14:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="21053"></span>
<div id="comment-21053" class="comment">
<div id="post-21053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I found the answer. But I'm not telling you.</p>
</div>
<div id="comment-21053-info" class="comment-info">
<span class="comment-age">(28 Mar '13, 16:57)</span> <span class="comment-user userinfo">digby</span>
</div>
</div>
</div>
<div id="comment-tools-9965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9965-form-container" class="comment-form-container">
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

