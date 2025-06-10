+++
type = "question"
title = "i don&#x27;t know how to show the button."
description = '''i am using org.osmdroid:osmdroid-android:6.1.8 and making android app include map.  after i place mapview and button in layout.xml, i can&#x27;t find button.  what is problem and how can i solve this problem? here layout.xml  &amp;lt;relativelayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot; a...'''
date = "2020-10-20T03:50:00Z"
lastmod = "2020-10-20T03:50:00Z"
weight = 77164
keywords = [ "osmdroid" ]
aliases = [ "/questions/77164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [i don't know how to show the button.](/questions/77164/i-dont-know-how-to-show-the-button)

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
<span id="post-77164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am using org.osmdroid:osmdroid-android:6.1.8 and making android app include map. after i place mapview and button in layout.xml, i can't find button. what is problem and how can i solve this problem?</p>
<p>here layout.xml</p>
&lt;relativelayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent" android:orientation="vertical"&gt;
<pre><code>&lt;Button
    android:layout_width=&quot;wrap_content&quot;
    android:layout_height=&quot;wrap_content&quot;
    android:layout_alignParentTop=&quot;true&quot;
    android:layout_alignParentRight=&quot;true&quot;
    android:layout_alignParentEnd=&quot;true&quot;
    android:layout_marginTop=&quot;10dp&quot;
    android:layout_marginRight=&quot;10dp&quot;
    android:text=&quot;Select&quot;
    /&gt;
&#10;&lt;org.osmdroid.views.MapView
    android:id=&quot;@+id/locationMap&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot; /&gt;</code></pre>
<p>&lt;/relativelayout&gt;</p>
<p>here is java code package com.example.copsys.OSM;</p>
<p>import android.app.Activity; import android.content.Context; import android.content.Intent; import android.graphics.Canvas; import android.graphics.drawable.Drawable; import android.os.Bundle; import android.os.PersistableBundle; import android.preference.PreferenceManager; import android.util.Log; import android.view.MotionEvent; import android.view.View; import android.widget.Toast;</p>
<p>import androidx.annotation.Nullable; import androidx.appcompat.app.AppCompatActivity;</p>
<p>import com.example.copsys.R;</p>
<p>import org.osmdroid.api.IMapController; import org.osmdroid.config.Configuration; import org.osmdroid.events.MapEventsReceiver; import org.osmdroid.tileprovider.tilesource.XYTileSource; import org.osmdroid.util.GeoPoint; import org.osmdroid.views.MapView; import org.osmdroid.views.Projection; import org.osmdroid.views.overlay.ItemizedIconOverlay; import org.osmdroid.views.overlay.ItemizedOverlayWithFocus; import org.osmdroid.views.overlay.MapEventsOverlay; import org.osmdroid.views.overlay.Overlay; import org.osmdroid.views.overlay.OverlayItem;</p>
<p>import java.util.ArrayList;</p>
<p>public class LocationMap extends AppCompatActivity {</p>
<pre><code>private final String TAG = &quot;LocationMap&quot;;
&#10;MapView map = null;
XYTileSource tileSource_4uMaps;
ArrayList&lt;OverlayItem&gt; items;
OverlayItem here = null;
&#10;@Override
public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getSupportActionBar().hide();
    //handle permissions first, before map is created. not depicted here
    //load/initialize the osmdroid configuration, this can be done
    Context ctx = getApplicationContext();
    Configuration.getInstance().load(ctx, PreferenceManager.getDefaultSharedPreferences(ctx));
    //setting this before the layout is inflated is a good idea
    //it &#39;should&#39; ensure that the map has a writable location for the map cache, even without permissions
    //if no tiles are displayed, you can try overriding the cache path using Configuration.getInstance().setCachePath
    //see also StorageUtils
    //note, the load method also sets the HTTP User Agent to your application&#39;s package name, abusing osm&#39;s tile servers will get you banned based on this string
    //inflate and create the map
    setContentView(R.layout.osm_layout);
&#10;    map = (MapView)findViewById(R.id.map);
    tileSource_4uMaps = new XYTileSource(&quot;4uMaps&quot;, 8, 15, 256, &quot;.png&quot;, new String[] {});</code></pre>
<p>// tileSource_google = new XYTileSource("Google Maps Earth Kor", 8, 19, 256, ".png", new String[] {}); map.setTileSource(tileSource_4uMaps); map.setUseDataConnection(false); //optional, but a good way to prevent loading from the network and test your zip loading. map.setBuiltInZoomControls(true); map.setMultiTouchControls(true);</p>
<pre><code>    IMapController mapController = map.getController();
    mapController.setZoom(15);
    GeoPoint startPoint = new GeoPoint( 35.86666, 128.600);
    mapController.setCenter(startPoint);</code></pre>
<p>// //your items items = new ArrayList&lt;overlayitem&gt;(); here = null; // items.add(new OverlayItem("Title", "Description", startPoint)); // Lat/Lon decimal degrees // // //the overlay // ItemizedOverlayWithFocus&lt;overlayitem&gt; mOverlay = new ItemizedOverlayWithFocus&lt;overlayitem&gt;(items, // new ItemizedIconOverlay.OnItemGestureListener&lt;overlayitem&gt;() { // @Override // public boolean onItemSingleTapUp(final int index, final OverlayItem item) { // //do something //// map.setTileSource(tileSource_4uMaps); // return true; // } // @Override // public boolean onItemLongPress(final int index, final OverlayItem item) { //// map.setTileSource(tileSource_google); // return false; // } // }, getApplicationContext()); // mOverlay.setFocusItemsOnTap(true); // map.getOverlays().add(mOverlay); MapEventsReceiver mReceive = new MapEventsReceiver() { @Override public boolean singleTapConfirmedHelper(GeoPoint p) { Toast.makeText(getBaseContext(),p.getLatitude() + " - "+p.getLongitude(),Toast.LENGTH_LONG).show();</p>
<pre><code>            here = new OverlayItem(&quot;Here&quot;, &quot;select&quot;, p);
            items.add(here);
                    //the overlay
            ItemizedOverlayWithFocus&lt;OverlayItem&gt; mOverlay = new ItemizedOverlayWithFocus&lt;OverlayItem&gt;(items,
                    new ItemizedIconOverlay.OnItemGestureListener&lt;OverlayItem&gt;() {
                        @Override
                        public boolean onItemSingleTapUp(final int index, final OverlayItem item) {
                            //do something
    //                        map.setTileSource(tileSource_4uMaps);
                            return true;
                        }
                        @Override
                        public boolean onItemLongPress(final int index, final OverlayItem item) {
    //                        map.setTileSource(tileSource_google);
                            return false;
                        }
                    }, getApplicationContext());
            mOverlay.setFocusItemsOnTap(true);
            map.getOverlays().add(mOverlay);
&#10;            Intent i = new Intent();
            i.putExtra(&quot;lon&quot;, p.getLongitude());
            i.putExtra(&quot;lat&quot;, p.getLatitude());
            setResult(RESULT_OK, i);
            finish();
&#10;            return false;
        }
&#10;        @Override
        public boolean longPressHelper(GeoPoint p) {
            return false;
        }
    };
&#10;
    MapEventsOverlay OverlayEvents = new MapEventsOverlay(getBaseContext(), mReceive);
    map.getOverlays().add(OverlayEvents);
&#10;
}
&#10;public void onResume(){
    super.onResume();
    //this will refresh the osmdroid configuration on resuming.
    //if you make changes to the configuration, use
    //SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
    //Configuration.getInstance().load(this, PreferenceManager.getDefaultSharedPreferences(this));
    map.onResume(); //needed for compass, my location overlays, v6.0.0 and up
}
&#10;public void onPause(){
    super.onPause();
    //this will refresh the osmdroid configuration on resuming.
    //if you make changes to the configuration, use
    //SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
    //Configuration.getInstance().save(this, prefs);
    map.onPause();  //needed for compass, my location overlays, v6.0.0 and up
}</code></pre>
<p>}</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '20, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fb411fa87f059d06f5b2719b465e6832?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="idkwiwtk&#39;s gravatar image" />
<p><span>idkwiwtk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="idkwiwtk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77164" class="comments-container">
&#10;</div>
<div id="comment-tools-77164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77164-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

