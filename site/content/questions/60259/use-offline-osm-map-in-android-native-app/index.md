+++
type = "question"
title = "Use offline OSM map in Android native app"
description = '''Hello Friends, For more than 2 weeks, i was working to use OSM Offline map in Android application. I have gone through many articles, blogs and question/answers of Stackoverflow, but could not find the solutions. still i am at the stage where i was earlier. Using maperitive.net, i have downloaded Ma...'''
date = "2017-10-24T08:19:00Z"
lastmod = "2017-10-25T07:23:00Z"
weight = 60259
keywords = [ "android", "osmdroid", "offlinemaps" ]
aliases = [ "/questions/60259" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use offline OSM map in Android native app](/questions/60259/use-offline-osm-map-in-android-native-app)

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
<span id="post-60259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60259-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Friends,</p>
<p>For more than 2 weeks, i was working to use OSM Offline map in Android application. I have gone through many articles, blogs and question/answers of Stackoverflow, but could not find the solutions. still i am at the stage where i was earlier.</p>
<p>Using maperitive.net, i have downloaded Map tiles of India for 2-12 Zoom level. i have given the name to the root folder is Mapnik and Mapnik.zip for its zip file. i have copied the file at /sdcard/osmdroid folder.</p>
<p>Below is code of my android app :</p>
<p>Manifest file :</p>
<p><img src="/upfiles/Capture_YJbcf7V.PNG" alt="alt text" /></p>
<p>Layout file</p>
<p><img src="/upfiles/Capture_VwnjxEM.PNG" alt="alt text" /> Java file :</p>
<pre><code>public class MainActivity extends Activity {
&#10;    private MapView         map;
&#10;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
&#10;        setContentView(R.layout.activity_main);
&#10;        map = (MapView) findViewById(R.id.mapview);
        map.setUseDataConnection(false);
        map.setTileSource(TileSourceFactory.MAPNIK);
        map.setTileSource(new XYTileSource(&quot;Mapnik&quot;,
                ResourceProxy.string.mapnik, 2, 12, 256, &quot;.png&quot;, new String[] {}));
&#10;        map.setBuiltInZoomControls(true);
        map.setMultiTouchControls(true);
&#10;        IMapController mapController = map.getController();
        mapController.setZoom(10);
        GeoPoint startPoint = new GeoPoint(22.8583, 72.2944);
        mapController.setCenter(startPoint);
&#10;    }
&#10;    @Override
    protected void onResume() {
        super.onResume();
&#10;    }
}</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '17, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/8d79ca507f006caa42157cf8f1d726ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashish7&#39;s gravatar image" />
<p><span>Ashish7</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashish7 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-60259" class="comments-container">
&#10;</div>
<div id="comment-tools-60259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60259-form-container" class="comment-form-container">
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

<span id="60265"></span>

<div id="answer-container-60265" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60265-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Basically I believe that you are taking the wrong approach and you should be looking at <a href="https://github.com/mapsforge/mapsforge">mapsforge</a> or similar vector data based system for rendering on device instead of generating tiles.</p>
<p>As to your question, some debug information would be helpful, but from your code you don't seem to be telling osmdroid where your tiles are located and other required setup.</p>
<p>There is a demo app here <a href="https://github.com/johnjohndoe/OSMDroidOfflineDemo">https://github.com/johnjohndoe/OSMDroidOfflineDemo</a> that may help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '17, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '17, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-60265" class="comments-container">
<span id="60292"></span>
<div id="comment-60292" class="comment">
<div id="post-60292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@simonpoole</a>, I had already followed the <a href="https://github.com/johnjohndoe/OSMDroidOfflineDemo">https://github.com/johnjohndoe/OSMDroidOfflineDemo</a> link and its steps, Mobile Atlas Creator is banned and it is not generating any Map tile. so i have taken the help of maperitive.net to generate tiles. but could not get success. i can get only blank grids on mobile screen.</p>
<p>please help me out. it would be good if you share latest working code snippet or let me know what i did in my above code or steps</p>
</div>
<div id="comment-60292-info" class="comment-info">
<span class="comment-age">(25 Oct '17, 07:23)</span> <span class="comment-user userinfo">Ashish7</span>
</div>
</div>
</div>
<div id="comment-tools-60265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60265-form-container" class="comment-form-container">
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

