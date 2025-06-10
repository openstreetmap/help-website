+++
type = "question"
title = "Using osmdroid for custom map images and not osm data"
description = '''Can I use the osmdroid library to display my own map. The folder structure looks the following mapname (folder)  |-zoomlevel (folder)  |- X_Y.png (a lot of images)  I thought I could load the tiles using a custom source but it seems nothing that I do works mResourceProxy = new DefaultResourceProxyIm...'''
date = "2013-02-17T00:12:00Z"
lastmod = "2013-02-17T00:12:00Z"
weight = 19991
keywords = [ "android", "osmdroid", "sdcard", "custom_tiles" ]
aliases = [ "/questions/19991" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using osmdroid for custom map images and not osm data](/questions/19991/using-osmdroid-for-custom-map-images-and-not-osm-data)

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
<span id="post-19991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I use the osmdroid library to display my own map. The folder structure looks the following</p>
<pre><code>mapname (folder)
 |-zoomlevel (folder)
   |- X_Y.png (a lot of images)</code></pre>
<p>I thought I could load the tiles using a custom source but it seems nothing that I do works</p>
<pre><code>mResourceProxy = new DefaultResourceProxyImpl(getApplicationContext());
&#10;// Add tiles layer with custom tile source
&#10;final MapView mapView = new MapView( this, 256 );
&#10;final ITileSource tileSource = new TileSource(Environment.getDataDirectory().getPath() + &quot;/exampleapp/mymap&quot;, null);
mapView.setTileSource(tileSource);
&#10;mapView.setMultiTouchControls(true);
&#10;setContentView(mapView);
mMapView = mapView;
&#10;mMapView.getController().setZoom(5);</code></pre>
<p>And my custom source</p>
<pre><code>public class TileSource extends BitmapTileSourceBase{
&#10;    public TileSource(String aName, string aResourceId) {
&#10;        super(aName, aResourceId, 1, 6, 256, &quot;.png&quot;);
    }
&#10;    @Override
    public String getTileRelativeFilenameString(MapTile tile) {
        final StringBuilder sb = new StringBuilder();
        sb.append(pathBase());
        sb.append(&#39;/&#39;);
        sb.append(tile.getZoomLevel());
        sb.append(&#39;/&#39;);
        sb.append(tile.getX());
        sb.append(&#39;_&#39;);
        sb.append(tile.getY());
        sb.append(imageFilenameEnding());
        return sb.toString();
&#10;    }
}</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-sdcard" rel="tag" title="see questions tagged &#39;sdcard&#39;">sdcard</span> <span class="post-tag tag-link-custom_tiles" rel="tag" title="see questions tagged &#39;custom_tiles&#39;">custom_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '13, 00:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a7beb0037c48629d3d10db4c2235b88f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bartinger&#39;s gravatar image" />
<p><span>Bartinger</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bartinger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19991" class="comments-container">
&#10;</div>
<div id="comment-tools-19991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19991-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

