+++
type = "question"
title = "Displaying OSM in an android webview with Openlayers3"
description = '''Good evening everyone, I am currently trying to display the OSM from Openlayer3 using javascript in an HTML page. As long as I stay on a classic webpage (on local with a tomcat) it work just fine and I display my own datas from a GeoJson file. Now i want to do the same on an android webview using th...'''
date = "2017-12-22T14:08:00Z"
lastmod = "2017-12-22T14:08:00Z"
weight = 61323
keywords = [ "website", "android", "openlayers", "webview" ]
aliases = [ "/questions/61323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Displaying OSM in an android webview with Openlayers3](/questions/61323/displaying-osm-in-an-android-webview-with-openlayers3)

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
<span id="post-61323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good evening everyone,</p>
<p>I am currently trying to display the OSM from Openlayer3 using javascript in an HTML page. As long as I stay on a classic webpage (on local with a tomcat) it work just fine and I display my own datas from a GeoJson file.</p>
<p>Now i want to do the same on an android webview using the same HTML &amp; JS files, exported openlayers.js/css and the html in the assets folder. The problem is the map itself doesn't show, just the controls and copyright at the bottom. I have allowed javascript in my webview as i can execute other function from a JavascriptInterface class.</p>
<p>Is there any restrictions with openlayers/osm and android ?</p>
<p>Note : I am currently restricted to just Openlayers and a webview for this project, so i can't use things like leaflet or any Google API.</p>
<p>My current code is :</p>
<pre><code>public class MapActivity extends AppCompatActivity {
&#10;private HashSet&lt;Point&gt; points;
private WebView webView;
private WebSettings wSettings;
private AssetManager assetManager;
&#10;@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    assetManager = getApplicationContext().getAssets();
    try {
        InputStream targetStream = assetManager.open(&quot;lieuxjson.json&quot;);
        points = GeoJsonParser.readJsonStream(targetStream);
    } catch (java.io.IOException e) {
        e.printStackTrace();
        //stop activity
    }
    WebView webView = new WebView(this);
    webView.setClickable(true);
    webView.setFocusableInTouchMode(true);
    wSettings = webView.getSettings();
    wSettings.setJavaScriptEnabled(true);
    WebClientClass webViewClient = new WebClientClass();
    webView.setWebViewClient(webViewClient);
    WebChromeClient webChromeClient = new WebChromeClient();
    webView.setWebChromeClient(webChromeClient);
    webView.addJavascriptInterface(new WebAppInterface(this), &quot;Android&quot;);
    webView.loadUrl(&quot;file:///android_asset/index.html&quot;);
    setContentView(webView);
}}</code></pre>
<p>And the JS with a div id="map" and ol.js &amp; ol.css imported :</p>
<pre><code>var world = new ol.layer.Tile({ source: new ol.source.OSM() });
world.setZIndex(0);
&#10;
var myview = new ol.View({
    center: ol.proj.fromLonLat([37.41, 8.82]),
    zoom: 3
  });
&#10;var map = new ol.Map({
  target: &#39;map&#39;,
  layers: [world],
  view: myview
});</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-webview" rel="tag" title="see questions tagged &#39;webview&#39;">webview</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '17, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/f78618f82ddd41bed74fabf19eaf8865?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce%20Swain&#39;s gravatar image" />
<p><span>Bruce Swain</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce Swain has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '17, 16:53</strong> </span></p>
</div>
</div>
<div id="comments-container-61323" class="comments-container">
&#10;</div>
<div id="comment-tools-61323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

