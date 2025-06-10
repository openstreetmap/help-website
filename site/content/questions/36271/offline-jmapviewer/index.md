+++
type = "question"
title = "Offline JMapViewer"
description = '''Dear all, Could you please advise me on the way I could use JMapViewer with stored map data (osm file or tiles extracted by Maperitive) for real-time gps tracking? I have used the following code to set the tiles or osm source but this does not work: final JMapViewer map = new JMapViewer();  map.setT...'''
date = "2014-08-27T13:31:00Z"
lastmod = "2014-08-27T16:56:00Z"
weight = 36271
keywords = [ "tiles", "jmapviewer", "offlinemaps" ]
aliases = [ "/questions/36271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Offline JMapViewer](/questions/36271/offline-jmapviewer)

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
<span id="post-36271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36271-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>Could you please advise me on the way I could use JMapViewer with stored map data (osm file or tiles extracted by Maperitive) for real-time gps tracking?</p>
<p>I have used the following code to set the tiles or osm source but this does not work:</p>
<pre><code>final JMapViewer map = new JMapViewer();
&#10;map.setTileSource(new OfflineOsmTileSource(&quot;file://c:/OpenStreetMap/&quot;, 1, 12));
&#10;where OfflineOsmTileSource class:
&#10;public class OfflineOsmTileSource extends AbstractOsmTileSource
 {
&#10;        private final int minZoom;
        private final int maxZoom;
        public OfflineOsmTileSource(String path, int minZoom, int maxZoom) {
        super(&quot;Offline from &quot;+path, path);
        this.minZoom = minZoom;
        this.maxZoom = maxZoom;
        }
        @Override
        public int getMaxZoom() {
        return maxZoom;
        }
        @Override
        public int getMinZoom() {
        return minZoom;
        }
        @Override
        public TileUpdate getTileUpdate() {
        return TileUpdate.None;
        }
 }</code></pre>
<p>Thanks in advance.</p>
<p>Best wishes</p>
<p>George</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-jmapviewer" rel="tag" title="see questions tagged &#39;jmapviewer&#39;">jmapviewer</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '14, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0b761f74da3a5662f41c0c444a3c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grccr&#39;s gravatar image" />
<p><span>grccr</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grccr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '14, 14:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-36271" class="comments-container">
<span id="36274"></span>
<div id="comment-36274" class="comment">
<div id="post-36274-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you please explain what exactly "does not work"?</p>
</div>
<div id="comment-36274-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36275"></span>
<div id="comment-36275" class="comment">
<div id="post-36275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That URL definition looks wrong to me. Does <a href="http://stackoverflow.com/questions/6098472/pass-a-local-file-in-to-url-in-java">this</a> help?</p>
</div>
<div id="comment-36275-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36276"></span>
<div id="comment-36276" class="comment not_top_scorer">
<div id="post-36276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply. The problem is that it fails to load the osm file or the tiles. osm file: failed loading 3/3/1 c failed loading 3/5/2 c ....... tiles: failed loading 3/5/1 c failed loading 3/5/2 c ......</p>
</div>
<div id="comment-36276-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:36)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36277"></span>
<div id="comment-36277" class="comment not_top_scorer">
<div id="post-36277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I changed the argument to map.setTileSource(new OfflineOsmTileSource((new File("C:\OpenStreetMap").toURI().toURL()).toString(), 1, 12)); but the problem remains</p>
<p>output: failed loading 3/4/2 C:\OpenStreetMap\3\4\2.png (The system cannot find the path specified) ....... failed loading 3/4/3 C:\OpenStreetMap\3\4\3.png (The system cannot find the path specified)</p>
</div>
<div id="comment-36277-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:47)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36278"></span>
<div id="comment-36278" class="comment not_top_scorer">
<div id="post-36278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the correct path for the tiles on your system?</p>
</div>
<div id="comment-36278-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36279"></span>
<div id="comment-36279" class="comment not_top_scorer">
<div id="post-36279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The path is C:\OpenStreetMap</p>
</div>
<div id="comment-36279-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 14:56)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36280"></span>
<div id="comment-36280" class="comment not_top_scorer">
<div id="post-36280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's not the correct path according to your error message or it doesn't contain any tiles. Please search for files named "2.png" in C:\OpenStreetMap and compare the path with the one passed to <code>OfflineOsmTileSource</code>. Maybe there is another subdirectory you forgot to add?</p>
</div>
<div id="comment-36280-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 15:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36282"></span>
<div id="comment-36282" class="comment not_top_scorer">
<div id="post-36282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your time to help me. Maybe I am using the wrong data to load. I have made two attempts: 1) In the directory c:\openstreetmap I saved a map.osm file exported for the openstreetmap.org 2) In the directory c:\openstreetmap I saved tiles generated from the above mentioned map.osm by Maperitive. In this case I have three main folders 17, 18, 19 and each of these folders contains other folders and each of these contains a .png file. I have noticed that next to the three folders there is a tiles.json file. Additionally there is no 2.png file as indicated by the error message.</p>
</div>
<div id="comment-36282-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 15:23)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36284"></span>
<div id="comment-36284" class="comment">
<div id="post-36284-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have no experience with JMapViewer but it seems like you just got the wrong zoom level. You only have subdirectories for zoom levels <em>17, 18, 19</em> but you are trying to open tiles for zoom level <em>3</em> (the first number in <em>3/4/2</em>). Try to generate tiles for all zoom levels (probably expensive) or set <code>minZoom</code> to <em>17</em> and <code>maxZoom</code> to <em>19</em>.</p>
</div>
<div id="comment-36284-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 15:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36285"></span>
<div id="comment-36285" class="comment not_top_scorer">
<div id="post-36285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again for your help. I just changed the zoom levels to 17-19 but the error remains. output: failed loading 17/68800/44416 C:\OpenStreetMap\17\68800\44416.png (The system cannot find the path specified) failed loading 17/68799/44416 C:\OpenStreetMap\17\68799\44416.png (The system cannot find the path specified)</p>
<p>There is no subfolder 68800 or 68799. The available subfolders are: 74685, 74686, 74687. 17/74685/51764.png 17/74685/51765.png 17/74686/61764.png . . .</p>
</div>
<div id="comment-36285-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:02)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36290"></span>
<div id="comment-36290" class="comment">
<div id="post-36290-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then I assume you are looking at the wrong part of the map. For the current location there are no tiles present. Go to a location for which you have tiles generated by Maperitive.</p>
</div>
<div id="comment-36290-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36291"></span>
<div id="comment-36291" class="comment not_top_scorer">
<div id="post-36291-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are correct! At the command map.setDisplayPositionByLatLon(lat, lon, zoom); I have to put a location inside the tiles I am loading and the correct zoom level(in my case 17/18/19) too. Thank you so much for your help! Best wishes George</p>
</div>
<div id="comment-36291-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:47)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
<span id="36292"></span>
<div id="comment-36292" class="comment">
<div id="post-36292-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For those that are interested in JMapViewer the correct command for the tile source is : map.setTileSource(new OfflineOsmTileSource((new File("C:\OpenStreetMap").toURI().toURL()).toString(), 17, 19)); Thank you all for your contribution! Best wishes George</p>
</div>
<div id="comment-36292-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 16:56)</span> <span class="comment-user userinfo">grccr</span>
</div>
</div>
</div>
<div id="comment-tools-36271" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-36271-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

