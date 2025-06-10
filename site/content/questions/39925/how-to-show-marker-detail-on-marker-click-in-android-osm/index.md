+++
type = "question"
title = "how to show marker detail on marker click in android osm ?"
description = '''I am new to use osm in android.I have successfully show OSM in android.But i have no idea &quot; how to click on marker and show marker detail like google map v2 infowindow popup&quot;. How to show marker details with image onclick marker openstreetmap android, same as Google map Infowindow show on marker cli...'''
date = "2014-12-30T09:16:00Z"
lastmod = "2014-12-30T10:16:00Z"
weight = 39925
keywords = [ "marker", "android", "osmdroid", "osm" ]
aliases = [ "/questions/39925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to show marker detail on marker click in android osm ?](/questions/39925/how-to-show-marker-detail-on-marker-click-in-android-osm)

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
<span id="post-39925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to use osm in android.I have successfully show OSM in android.But i have no idea " <strong>how to click on marker and show marker detail like google map v2 infowindow popup</strong>".</p>
<p><strong>How to show marker details with image onclick marker openstreetmap android, same as Google map Infowindow show on marker click.</strong></p>
<p>Please give me code or idea to implement marker click event in osm android.</p>
<p>Thank you in advance.</p>
<p>This is my code which i have implemented in android java</p>
<pre><code>public class MainActivity extends Activity 
{
private MapView mapView;
private MapController mapController;    
LocationManager locationManager;
&#10;ArrayList&lt;OverlayItem&gt; overlayItemArray;
&#10;@Override
protected void onCreate(Bundle savedInstanceState) 
{
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    mapView = (MapView)findViewById(R.id.mapview);
&#10;    mapView.setBuiltInZoomControls(true);
    mapView.setMultiTouchControls(true);
    mapView.setClickable(true);
    //mapView.setUseDataConnection(false);
    mapController = (MapController) mapView.getController();
    mapController.setZoom(17);
&#10;    //--- Create Overlay
    overlayItemArray = new ArrayList&lt;OverlayItem&gt;();
&#10;    DefaultResourceProxyImpl defaultResourceProxyImpl = new DefaultResourceProxyImpl(this);
    MyItemizedIconOverlay myItemizedIconOverlay = new MyItemizedIconOverlay(overlayItemArray, null, defaultResourceProxyImpl);
    mapView.getOverlays().add(myItemizedIconOverlay);
    //---
&#10;    locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
&#10;    //for demo, getLastKnownLocation from GPS only, not from NETWORK
    Location lastLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
    if(lastLocation != null)
    {
        updateLoc(lastLocation);
    }
&#10;    //Add Scale Bar
    ScaleBarOverlay myScaleBarOverlay = new ScaleBarOverlay(this);
    mapView.getOverlays().add(myScaleBarOverlay);
}
&#10;@Override
protected void onResume()
{
    super.onResume();
    locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, myLocationListener);
    locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, myLocationListener);
}
&#10;@Override
protected void onPause() 
{
    super.onPause();
    locationManager.removeUpdates(myLocationListener);
}
&#10;private void updateLoc(Location loc)
{
    GeoPoint locGeoPoint = new GeoPoint(loc.getLatitude(), loc.getLongitude());
    mapController.setCenter(locGeoPoint);
    mapController.animateTo(locGeoPoint);
&#10;    setOverlayLoc(loc);
&#10;    mapView.invalidate();
}
&#10;private void setOverlayLoc(Location overlayloc)
{
    GeoPoint overlocGeoPoint = new GeoPoint(overlayloc);
    //---
    overlayItemArray.clear();
&#10;    OverlayItem newMyLocationItem = new OverlayItem(&quot;My Location&quot;, &quot;My Location&quot;, overlocGeoPoint);
    overlayItemArray.add(newMyLocationItem);
    //---
}
&#10;private LocationListener myLocationListener = new LocationListener()
{
    @Override
    public void onLocationChanged(Location location)
    {
        updateLoc(location);
    }
&#10;    @Override
    public void onProviderDisabled(String provider)
    {           
    }
&#10;    @Override
    public void onProviderEnabled(String provider)
    {           
    }
&#10;    @Override
    public void onStatusChanged(String provider, int status, Bundle extras)
    {           
    }
};
&#10;private class MyItemizedIconOverlay extends ItemizedIconOverlay&lt;OverlayItem&gt;
{
&#10;    public MyItemizedIconOverlay(List&lt;OverlayItem&gt; pList,org.osmdroid.views.overlay.ItemizedIconOverlay.OnItemGestureListener&lt;OverlayItem&gt; pOnItemGestureListener,
            ResourceProxy pResourceProxy)
    {
        super(pList, pOnItemGestureListener, pResourceProxy);           
    }
&#10;    @Override
    public void draw(Canvas canvas, MapView mapview, boolean arg2)
    {
        super.draw(canvas, mapview, arg2);
&#10;        if(!overlayItemArray.isEmpty())
        {
            //overlayItemArray have only ONE element only, so I hard code to get(0)
            GeoPoint in = overlayItemArray.get(0).getPoint();
&#10;            Point out = new Point();
            mapview.getProjection().toPixels(in, out);
&#10;            Bitmap bm = BitmapFactory.decodeResource(getResources(),R.drawable.ic_launcher);
            canvas.drawBitmap(bm,out.x - bm.getWidth()/2,out.y - bm.getHeight()/2,null);
        }
    }
&#10;    @Override
    public boolean onSingleTapUp(MotionEvent event, MapView mapView)
    {
        //return super.onSingleTapUp(event, mapView);
        return true;
    }
&#10;    @Override
    public boolean onSingleTapConfirmed(MotionEvent event, MapView mapView)
    {
        return true;
    }
}</code></pre>
<p>}</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '14, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6ce327f00b711d021de7bb7928fc5c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nehalkumar&#39;s gravatar image" />
<p><span>nehalkumar</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nehalkumar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '14, 10:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-39925" class="comments-container">
<span id="39926"></span>
<div id="comment-39926" class="comment">
<div id="post-39926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what you've done so far to "show OSM in android"? Are you writing an Android application, and if so in what - Android Java, or something else?</p>
</div>
<div id="comment-39926-info" class="comment-info">
<span class="comment-age">(30 Dec '14, 09:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="39927"></span>
<div id="comment-39927" class="comment">
<div id="post-39927-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i have added code please check and give suggestion.Yes this is android apllication</p>
</div>
<div id="comment-39927-info" class="comment-info">
<span class="comment-age">(30 Dec '14, 09:29)</span> <span class="comment-user userinfo">nehalkumar</span>
</div>
</div>
</div>
<div id="comment-tools-39925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39925-form-container" class="comment-form-container">
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

<span id="39928"></span>

<div id="answer-container-39928" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39928-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I got Solution from this link</p>
<p>"<a href="http://code.google.com/p/osmdroid/issues/detail?id=245#makechanges">http://code.google.com/p/osmdroid/issues/detail?id=245#makechanges</a>"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '14, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6ce327f00b711d021de7bb7928fc5c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nehalkumar&#39;s gravatar image" />
<p><span>nehalkumar</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nehalkumar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '14, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-39928" class="comments-container">
&#10;</div>
<div id="comment-tools-39928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39928-form-container" class="comment-form-container">
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

