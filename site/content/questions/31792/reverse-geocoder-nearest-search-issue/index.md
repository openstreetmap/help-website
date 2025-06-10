+++
type = "question"
title = "Reverse geocoder nearest search issue"
description = '''I&#x27;m currently importing Europe maps because I need a reverse geocoder. While playing with the OSM website I encountered 2 issues:  1. When centering the map to:  http://www.openstreetmap.org/search?query=42.70988%2C23.29388 it displays the wrong address. It prefers the 173 Видин (173 Vidin) instead ...'''
date = "2014-03-23T14:01:00Z"
lastmod = "2014-06-04T16:19:00Z"
weight = 31792
keywords = [ "reversegeolocation", "reversegeocoding", "reverse", "nominatim" ]
aliases = [ "/questions/31792" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoder nearest search issue](/questions/31792/reverse-geocoder-nearest-search-issue)

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
<span id="post-31792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently importing Europe maps because I need a reverse geocoder. While playing with the OSM website I encountered 2 issues: 1. When centering the map to: <a href="http://www.openstreetmap.org/search?query=42.70988%2C23.29388">http://www.openstreetmap.org/search?query=42.70988%2C23.29388</a> it displays the wrong address. It prefers the 173 Видин (173 Vidin) instead бул.Сливница (boulevard Slivnica). Looking the source code it filters the nearest one while 173 Vidin is not (I tested with a lat, lon exactly on the Slivnica main street). 2. When centering the map to: <a href="http://www.openstreetmap.org/search?query=42.39311%2C23.63431">http://www.openstreetmap.org/search?query=42.39311%2C23.63431</a> it shows not the village Ново Село (Novo selo) but Ихтиман (Ihtiman) which is far away from that point. I understand that the reverse geocoder goes the hierarchy up while looking up the parents of the road found, but still this is not optimal. Google reverser somehow shows the nearest city/town/village. <a href="https://www.google.com/maps/place/42%C2%B023%2737.5%22N+23%C2%B038%2703.3%22E/@42.393736,23.634251,14z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0">https://www.google.com/maps/place/42%C2%B023%2737.5%22N+23%C2%B038%2703.3%22E/@42.393736,23.634251,14z/data=!3m1!4b1!4m2!3m1!1s0x0:0x0</a></p>
<p>Similar issues to be found when asking for reverse on a highway between two cities and when in the middle of the highway there is another town near or on the road.</p>
<p>Is there a way to fix this? I believe this would be a nice feature to have.</p>
<p>Or somehow as a mapper I may split the road into sub part and attach that part to the city of interest?</p>
<p>I was unable to find the way how to define a residential area as a village or town or city and attach the roads to it. I saw that some smaller towns and villages have a residential polygon surrounding but it is not named, nor belongs to a relation. Nevertheless, nominatim somehow knows for their streets that they are in that town. Well, I'd like to be able to do something about that but I do not how. The mapping tutorials I read are not sufficient for fixing the above problems. Any help is highly appreciated.</p>
<p>Regards Boris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeolocation" rel="tag" title="see questions tagged &#39;reversegeolocation&#39;">reversegeolocation</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '14, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/397597c08da4d1cf3c1f25d9b62df5f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkamenov&#39;s gravatar image" />
<p><span>bkamenov</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkamenov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '14, 20:04</strong> </span></p>
</div>
</div>
<div id="comments-container-31792" class="comments-container">
&#10;</div>
<div id="comment-tools-31792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31792-form-container" class="comment-form-container">
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

<span id="31855"></span>

<div id="answer-container-31855" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Me again,</p>
<p>I have investigated deeply through the source of the reverse geocoder. Unfortunately, it is wrong. I have rewritten the core code and now I get results even better than google does. But my code is almost 3 times as slower than the original one. If I could get faulty results in 36 ms for DB only Bulgaria map only (my Europe map import has failed, I'll try again later), now for 97 ms I get perfect results.</p>
<p>I'll paste my changes if someone needs them later, but my algorithm works as follows:</p>
<p>for the GPS point I find nearest city/town/village place, then a second query searches for the nearest road in range of 200 meters near my point. Finally, I search with a third query the nearest feature with rank &gt; 28 which are houses and buildings but the trick is to search for nearest one in range of 40 meters and the parent should be the road found in the previous query. In that way I resolve all issues I had.</p>
<p>Would be nice if someone could optimize the queries a little. Here is my code (please note that I ignore the zoom level factor):</p>
<p>In lib/ReverseGeocode.php I replaced the lookup() method body with:</p>
<p>function lookup() { $sPointSQL = 'ST_SetSRID(ST_Point('.$this-&gt;fLon.','.$this-&gt;fLat.'),4326)'; $iMaxRank = $this-&gt;iMaxRank;</p>
<pre><code>        // Find the nearest city/town/village
        $fSearchDiam = 0.3;
        $iPlaceID = null;
        $fMaxAreaDistance = 1;
        while(!$iPlaceID &amp;&amp; $fSearchDiam &lt; $fMaxAreaDistance)
        {
            $fSearchDiam = $fSearchDiam * 2;
&#10;            $sSQL = &#39;select place_id from placex&#39;;
            $sSQL .= &#39; WHERE ST_DWithin(&#39;.$sPointSQL.&#39;, geometry, &#39;.$fSearchDiam.&#39;)&#39;;
            $sSQL .= &#39; and rank_search &lt;= 22&#39;;
            $sSQL .= &#39; and (name is not null)&#39;;
            $sSQL .= &#39; and class = \&#39;place\&#39;&#39;;
            $sSQL .= &#39; and indexed_status = 0 &#39;;
            $sSQL .= &#39; and (ST_GeometryType(geometry) not in (\&#39;ST_Polygon\&#39;,\&#39;ST_MultiPolygon\&#39;) &#39;;
            $sSQL .= &#39; OR ST_DWithin(&#39;.$sPointSQL.&#39;, centroid, &#39;.$fSearchDiam.&#39;))&#39;;
            $sSQL .= &#39; ORDER BY ST_distance(&#39;.$sPointSQL.&#39;, geometry) ASC limit 1&#39;;
&#10;            $aPlace = $this-&gt;oDB-&gt;getRow($sSQL);
            if (PEAR::IsError($aPlace))
            {
                failInternalError(&quot;Could not determine closest city/town/village.&quot;, $sSQL, $aPlace);
            }
            $iPlaceID = $aPlace[&#39;place_id&#39;];
        }
&#10;        $oPlaceLookup = new PlaceLookup($this-&gt;oDB);
        $oPlaceLookup-&gt;setLanguagePreference($this-&gt;aLangPrefOrder);
        $oPlaceLookup-&gt;setIncludeAddressDetails(true);
        $oPlaceLookup-&gt;setPlaceId($iPlaceID);
&#10;        $oAddressInfo = $oPlaceLookup-&gt;lookup();
&#10;        //Find nearest house/street/road within 200 m
        $fSearchDiam = 0.002;
&#10;        $sSQL = &#39;select place_id,parent_place_id,rank_search from placex&#39;;
        $sSQL .= &#39; WHERE ST_DWithin(&#39;.$sPointSQL.&#39;, geometry, &#39;.$fSearchDiam.&#39;)&#39;;
        $sSQL .= &#39; and rank_search != 28 and rank_search &gt;= 23&#39;;
        $sSQL .= &#39; and (name is not null or housenumber is not null)&#39;;
        $sSQL .= &#39; and class not in (\&#39;waterway\&#39;,\&#39;railway\&#39;,\&#39;tunnel\&#39;,\&#39;bridge\&#39;)&#39;;
        $sSQL .= &#39; and indexed_status = 0 &#39;;
        $sSQL .= &#39; and (ST_GeometryType(geometry) not in (\&#39;ST_Polygon\&#39;,\&#39;ST_MultiPolygon\&#39;) &#39;;
        $sSQL .= &#39; OR ST_DWithin(&#39;.$sPointSQL.&#39;, centroid, &#39;.$fSearchDiam.&#39;))&#39;;
        $sSQL .= &#39; ORDER BY ST_distance(&#39;.$sPointSQL.&#39;, geometry) ASC limit 1&#39;;
&#10;        $aPlace = $this-&gt;oDB-&gt;getRow($sSQL);
        if(PEAR::IsError($aPlace))
        {
            failInternalError(&quot;Could not determine closest place.&quot;, $sSQL, $aPlace);
        }
        $iPlaceID = $aPlace[&#39;place_id&#39;];
        $iParentPlaceID = $aPlace[&#39;parent_place_id&#39;];
&#10;        if($iPlaceID)
        {
            if($aPlace[&#39;rank_search&#39;] &gt; 28)
            {
                if($iParentPlaceID)
                    $iPlaceID = $iParentPlaceID;
            }
&#10;            //Find nearest house number within 40 meters or building which is child of the road found
            $fSearchDiam = 0.0004;
&#10;            $sSQL = &#39;select place_id, parent_place_id from placex&#39;;
            $sSQL .= &#39; WHERE ST_DWithin(&#39;.$sPointSQL.&#39;, geometry, &#39;.$fSearchDiam.&#39;)&#39;;
            $sSQL .= &#39; and rank_search &gt; 28&#39;;
            $sSQL .= &#39; and (name is not null or housenumber is not null)&#39;;
            $sSQL .= &#39; and class not in (\&#39;waterway\&#39;,\&#39;railway\&#39;,\&#39;tunnel\&#39;,\&#39;bridge\&#39;)&#39;;
            $sSQL .= &#39; and indexed_status = 0 &#39;;
            $sSQL .= &#39; and parent_place_id=&#39;.$iPlaceID;
            $sSQL .= &#39; and (ST_GeometryType(geometry) not in (\&#39;ST_Polygon\&#39;,\&#39;ST_MultiPolygon\&#39;) &#39;;
            $sSQL .= &#39; OR ST_DWithin(&#39;.$sPointSQL.&#39;, centroid, &#39;.$fSearchDiam.&#39;))&#39;;
            $sSQL .= &#39; ORDER BY ST_distance(&#39;.$sPointSQL.&#39;, geometry) ASC limit 1&#39;;
&#10;            $aPlace = $this-&gt;oDB-&gt;getRow($sSQL);
            if(PEAR::IsError($aPlace))
            {
                failInternalError(&quot;Could not determine closest place.&quot;, $sSQL, $aPlace);
            }
            if($aPlace[&#39;place_id&#39;])
                $iPlaceID = $aPlace[&#39;place_id&#39;];
&#10;            $oPlaceLookup-&gt;setPlaceId($iPlaceID);
&#10;            $oStreetInfo = $oPlaceLookup-&gt;lookup();
&#10;            if(!isset($oStreetInfo[&quot;error&quot;]) &amp;&amp; isset($oStreetInfo[&quot;aAddress&quot;]) &amp;&amp; isset($oStreetInfo[&quot;aAddress&quot;][&quot;road&quot;]))
            {
                $oAddressInfo[&quot;aAddress&quot;][&quot;road&quot;] = $oStreetInfo[&quot;aAddress&quot;][&quot;road&quot;];
&#10;                if(isset($oStreetInfo[&quot;aAddress&quot;][&quot;house_number&quot;]))
                    $oAddressInfo[&quot;aAddress&quot;][&quot;house_number&quot;] = $oStreetInfo[&quot;aAddress&quot;][&quot;house_number&quot;];
                else if($oStreetInfo[&quot;aAddress&quot;][&quot;building&quot;])
                    $oAddressInfo[&quot;aAddress&quot;][&quot;house_number&quot;] = $oStreetInfo[&quot;aAddress&quot;][&quot;building&quot;];
&#10;                if(isset($oStreetInfo[&quot;aAddress&quot;][&quot;suburb&quot;]))
                    $oAddressInfo[&quot;aAddress&quot;][&quot;suburb&quot;] = $oStreetInfo[&quot;aAddress&quot;][&quot;suburb&quot;];
&#10;                if(isset($oStreetInfo[&quot;aAddress&quot;][&quot;postcode&quot;]))
                    $oAddressInfo[&quot;aAddress&quot;][&quot;postcode&quot;] = $oStreetInfo[&quot;aAddress&quot;][&quot;postcode&quot;];
            }
&#10;        }
&#10;        return $oAddressInfo;
    }</code></pre>
<p>In my own reverse.php I use the reverse place to build an address as follows:</p>
<p>$oReverseGeocode = new ReverseGeocode($oDB); $oReverseGeocode-&gt;setLanguagePreference($aLangPrefOrder); $oReverseGeocode-&gt;setIncludeAddressDetails(true); $oReverseGeocode-&gt;setLatLon($request[$i]['lat'], $request[$i]['lon']); $aPlace = $oReverseGeocode-&gt;lookup();</p>
<pre><code>    $addr = &quot;&quot;;
    if(!isset($aPlace[&quot;error&quot;]) &amp;&amp; isset($aPlace[&quot;aAddress&quot;]) &amp;&amp; isset($aPlace[&quot;aAddress&quot;][&quot;country&quot;]))
    {
        //Road
        if(isset($aPlace[&quot;aAddress&quot;][&quot;road&quot;]))
        {
            $addr .= $aPlace[&quot;aAddress&quot;][&quot;road&quot;];
&#10;            if(isset($aPlace[&quot;aAddress&quot;][&quot;house_number&quot;])) //House number
                $addr .= &quot; &quot; . $aPlace[&quot;aAddress&quot;][&quot;house_number&quot;];
            else if(isset($aPlace[&quot;aAddress&quot;][&quot;suburb&quot;]))//Try providing a suburb
                $addr .= &quot;, &quot; . $aPlace[&quot;aAddress&quot;][&quot;suburb&quot;];
&#10;            $addr .= &quot;, &quot;;
&#10;        }
&#10;        //Post code
        if(isset($aPlace[&quot;aAddress&quot;][&quot;postcode&quot;]))
            $addr .= $aPlace[&quot;aAddress&quot;][&quot;postcode&quot;] . &quot;, &quot;;
&#10;        //Village, town or city
        if(isset($aPlace[&quot;aAddress&quot;][&quot;vilage&quot;]) || isset($aPlace[&quot;aAddress&quot;][&quot;town&quot;]) || isset($aPlace[&quot;aAddress&quot;][&quot;city&quot;]))
        {
            if(isset($aPlace[&quot;aAddress&quot;][&quot;vilage&quot;]))
                $addr .= $aPlace[&quot;aAddress&quot;][&quot;vilage&quot;] . &quot;, &quot;;
&#10;            if(isset($aPlace[&quot;aAddress&quot;][&quot;town&quot;]))
                $addr .= $aPlace[&quot;aAddress&quot;][&quot;town&quot;] . &quot;, &quot;;
&#10;            if(isset($aPlace[&quot;aAddress&quot;][&quot;city&quot;]))
                $addr .= $aPlace[&quot;aAddress&quot;][&quot;city&quot;] . &quot;, &quot;;
        }
        else if(isset($aPlace[&quot;aAddress&quot;][&quot;county&quot;])) //County
            $addr .= $aPlace[&quot;aAddress&quot;][&quot;county&quot;] . &quot;, &quot;;
        else if(isset($aPlace[&quot;aAddress&quot;][&quot;state&quot;])) //State
            $addr .= $aPlace[&quot;aAddress&quot;][&quot;state&quot;] . &quot;, &quot;;
&#10;        //Country
        $addr .= $aPlace[&quot;aAddress&quot;][&quot;country&quot;];
    }</code></pre>
<p>}</p>
<p>Now $addr will have your desired address.</p>
<p>Hope someone could optimize that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '14, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/397597c08da4d1cf3c1f25d9b62df5f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkamenov&#39;s gravatar image" />
<p><span>bkamenov</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkamenov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '14, 22:38</strong> </span></p>
</div>
</div>
<div id="comments-container-31855" class="comments-container">
<span id="33673"></span>
<div id="comment-33673" class="comment">
<div id="post-33673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm trying to use your code, but obtain the next one:</p>
<p>&lt;reversegeocode timestamp="Wed, 04 Jun 14 14:50:24 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;http://www.openstreetmap.org/copyright" querystring="format=xml&amp;lat=50.90921&amp;lon=4.46187"&gt; &lt;error&gt;Unable to geocode&lt;/error&gt; &lt;/reversegeocode&gt;</p>
<p>Did you change anything in PlaceLookup.php? Did you make change only in ReverseGeocode.php and reverse.php?</p>
<p>I imagine that I need to make a change in /lib/template/address.php , could you tell me what I'm doing wrong?</p>
<p>Thanks in advance!</p>
</div>
<div id="comment-33673-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 16:06)</span> <span class="comment-user userinfo">soyeya</span>
</div>
</div>
<span id="33675"></span>
<div id="comment-33675" class="comment">
<div id="post-33675-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is the wrong place for discussing code. Please use <a href="https://github.com/twain47/Nominatim/">https://github.com/twain47/Nominatim/</a> for asking question and suggesting changes.</p>
</div>
<div id="comment-33675-info" class="comment-info">
<span class="comment-age">(04 Jun '14, 16:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31855-form-container" class="comment-form-container">
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

