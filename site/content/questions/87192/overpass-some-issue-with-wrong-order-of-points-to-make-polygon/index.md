+++
type = "question"
title = "overpass: some issue with wrong order of points to make polygon"
description = '''I am running this query on overpass-turbo  [out:json][timeout:25]; rel(223133); (  rel(r); ); rel(1250951);  out geom;  and I have received this polygon.  but when I process this data my Image is like this :  I am using dot net core and this is my query foreach (var m in geoElement.members) {  if (m...'''
date = "2023-04-30T19:00:00Z"
lastmod = "2023-04-30T22:22:00Z"
weight = 87192
keywords = [ "overpass", "geojson", "overpassturbo" ]
aliases = [ "/questions/87192" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overpass: some issue with wrong order of points to make polygon](/questions/87192/overpass-some-issue-with-wrong-order-of-points-to-make-polygon)

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
<span id="post-87192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87192-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running this query on overpass-turbo</p>
<pre><code>[out:json][timeout:25];
rel(223133);
(
  rel(r);
);
rel(1250951);
&#10;out geom;</code></pre>
<p>and I have received this polygon.</p>
<p><a href="https://i.stack.imgur.com/0V8Rv.png"><img src="https://i.stack.imgur.com/0V8Rv.png" alt="enter image description here" /></a></p>
<p>but when I process this data my Image is like this :</p>
<p><a href="https://i.stack.imgur.com/IDgjd.png"><img src="https://i.stack.imgur.com/IDgjd.png" alt="enter image description here" /></a></p>
<p>I am using dot net core and this is my query</p>
<pre><code>foreach (var m in geoElement.members)
{
    if (m is { type: &quot;way&quot;, role: &quot;outer&quot; })
    {
        foreach (var g in m.geometry)
        {
            Coordinate coordinate = new Coordinate(g.lon, g.lat);
            coordinates.Add(coordinate);
        }
    }
&#10;}
var shell = new LinearRing(coordinates.ToArray());
&#10;var p = new Polygon(shell);
        var serializer = GeoJsonSerializer.Create();
        using var stringWriter = new StringWriter();
        using var jsonWriter = new JsonTextWriter(stringWriter);
&#10;        serializer.Serialize(jsonWriter, p);
        var geoJson = stringWriter.ToString();
        return geoJson;</code></pre>
<p>First I added all geometries lat and lng into a coordinate list and finally, I make a polygon and at the end I make a GeoJson.</p>
<p>can someone guild me on what tips exist here?</p>
<p>I downloaded GeoJson file from Overpass and I checked with my made GeoJson.there is so different from points. I don't know why? how can I make GeoJson like an overpass downloaded file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-overpassturbo" rel="tag" title="see questions tagged &#39;overpassturbo&#39;">overpassturbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '23, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/3016a8114f68eb431594ee9ec890c246?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alt2020&#39;s gravatar image" />
<p><span>alt2020</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alt2020 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-87192" class="comments-container">
<span id="87194"></span>
<div id="comment-87194" class="comment">
<div id="post-87194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First off, this query will return the same data as yours:</p>
<pre><code>[out:json];
rel(1250951);
out geom;</code></pre>
<p>I've used a couple of osmtogeojson converters &amp; they all output as expected. Is GeoJsonSerializer an internal command?</p>
</div>
<div id="comment-87194-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 20:14)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="87195"></span>
<div id="comment-87195" class="comment">
<div id="post-87195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(following on from the conversation elsewhere)</p>
<p>I think that you're assuming that your "foreach" will get you the OSM ways in the "correct" order (sequentially around the relation). This isn't guaranteed. There is probably some multipolygon code out there for your language; I'd be tempted to borrow from that :)</p>
</div>
<div id="comment-87195-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 20:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87196"></span>
<div id="comment-87196" class="comment">
<div id="post-87196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did u get the correct answer? <a href="https://help.openstreetmap.org/users/1532/davef"></a><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a></p>
</div>
<div id="comment-87196-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 22:17)</span> <span class="comment-user userinfo">alt2020</span>
</div>
</div>
<span id="87197"></span>
<div id="comment-87197" class="comment">
<div id="post-87197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the output of query, first geometry is <code>"geometry": [ { "lat": 38.2591626, "lon": 33.1844776 },</code> but if u download Geojson the first coordinate is <code>[ 33.0320818, 38.1524781 ],</code> . as you can see there is a difference here <a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a></p>
</div>
<div id="comment-87197-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 22:22)</span> <span class="comment-user userinfo">alt2020</span>
</div>
</div>
</div>
<div id="comment-tools-87192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87192-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

