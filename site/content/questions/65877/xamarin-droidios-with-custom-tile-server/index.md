+++
type = "question"
title = "Xamarin Droid/iOS with custom tile server"
description = '''I&#x27;m trying to make a Proof of Concept (PoC) regarding Open Street Map (OSM), but my lack of GIS- and Xamarin knowledge (novice) gets me stuck. What I&#x27;ve done so far is to set up an Azure Virtual Machine (VM) to act as a tile-server by following this guide: https://switch2osm.org/manually-building-a-...'''
date = "2018-09-13T06:53:00Z"
lastmod = "2018-09-14T22:16:00Z"
weight = 65877
keywords = [ "development", "xamarin", "tile-server" ]
aliases = [ "/questions/65877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Xamarin Droid/iOS with custom tile server](/questions/65877/xamarin-droidios-with-custom-tile-server)

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
<span id="post-65877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65877-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to make a Proof of Concept (PoC) regarding Open Street Map (OSM), but my lack of GIS- and Xamarin knowledge (novice) gets me stuck.</p>
<p>What I've done so far is to set up an Azure Virtual Machine (VM) to act as a tile-server by following this guide: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>I also set up two maps for a web app, connected to my tile server, with <strong>OpenLayers.js</strong> and <strong>Leaflet.js</strong> - wich all worked out fine and dandy.</p>
<ul>
<li><p>What I'm looking for:</p></li>
<li><p>A guide, tutorial or a hint on how to connect a Xamarin Droid and iOS app (not Xamarin Forms) to my tile-server http://*.*.*.*/${z}/${x}/${y} to get this OSM PoC working across different platforms.</p></li>
<li><p>Free of charge Xamarin nuget/lib (OsmSharp?) that can connect to my tile-server and render a map.</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-xamarin" rel="tag" title="see questions tagged &#39;xamarin&#39;">xamarin</span> <span class="post-tag tag-link-tile-server" rel="tag" title="see questions tagged &#39;tile-server&#39;">tile-server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '18, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e99aaad7237bb8a7b9fdee28a7dc8f80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henkolicious&#39;s gravatar image" />
<p><span>Henkolicious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henkolicious has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '18, 08:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-65877" class="comments-container">
&#10;</div>
<div id="comment-tools-65877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65877-form-container" class="comment-form-container">
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

<span id="65885"></span>

<div id="answer-container-65885" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So I figured out how to do this.</p>
<ol>
<li>Got a zip with .dll's for OsmSharp 2014 here: <a href="https://github.com/OsmSharp/ui/releases/tag/v4.2.0.723">https://github.com/OsmSharp/ui/releases/tag/v4.2.0.723</a></li>
<li>Referenced the .dll's in the Xamarin project (Android catalog)</li>
<li>Added this code</li>
</ol>
<p><strong>styles.xml</strong></p>
<pre><code>
     style name=&quot;Theme&quot; parent=&quot;AppTheme&quot; /&gt;
&#10;     style name=&quot;Theme.Splash&quot; /&gt;
&#10;     </code></pre>
<strong>MainActivity.cs</strong>
<pre><code> 
    using OsmSharp.Android.UI;
    using OsmSharp.Android.UI.Data.SQLite;
    using OsmSharp.Math.Geo;
    using OsmSharp.UI.Map;
    using OsmSharp.UI.Map.Layers;
    MapView _mapView;
    Layer _mapLayer;
&#10;    protected override void OnCreate(Bundle savedInstanceState)
    {
        base.OnCreate(savedInstanceState);
&#10;        try
        {
            Native.Initialize();
&#10;            _mapView = new MapView(this, new MapViewSurface(this))
            {
                MapTilt = 0,
                MapCenter = new GeoCoordinate(your_lat, your_long),
                MapZoom = 16,
                Map = new Map()
            };
&#10;            _mapLayer = _mapView.Map.AddLayerTile(&quot;http://*.*.*.*/{0}/{1}/{2}.png&quot;);
            SetContentView(_mapView);
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex);
        }
    }
 &lt;/pre&gt;</code></pre>
<p>However this is and old library and lots of "standard" functionalities are missing. You can add markers etc, but not draw polygons or lines with it, at least not what I can find.</p>
<p>Might help someone. Cheers!</p>
</pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '18, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/e99aaad7237bb8a7b9fdee28a7dc8f80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henkolicious&#39;s gravatar image" />
<p><span>Henkolicious</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henkolicious has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-65885" class="comments-container">
<span id="65907"></span>
<div id="comment-65907" class="comment">
<div id="post-65907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your sharing your self answer! Is this question fully answered now, or are you still looking for other answers?</p>
</div>
<div id="comment-65907-info" class="comment-info">
<span class="comment-age">(14 Sep '18, 22:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65885-form-container" class="comment-form-container">
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

