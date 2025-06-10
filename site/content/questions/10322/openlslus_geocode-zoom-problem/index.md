+++
type = "question"
title = "OpenLSLUS_Geocode zoom problem"
description = '''Referring to this question, did you put the correct link to the python directory in proxy.cgi? I&#x27;ve used python download from FWTools in my Windows environment.  I&#x27;ve copied proxy.cgi to the apache&#92;cgi-bin directory, and changed the first line from  &#x27;#!/usr/bin/env python into: &#x27;#!C:&#92;Gis&#92;apps&#92;FWTool...'''
date = "2012-01-29T22:12:00Z"
lastmod = "2012-02-03T10:45:00Z"
weight = 10322
keywords = [ "openlslus", "search" ]
aliases = [ "/questions/10322" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLSLUS_Geocode zoom problem](/questions/10322/openlslus_geocode-zoom-problem)

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
<span id="post-10322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Referring to <a href="http://help.openstreetmap.org/questions/9690/why-geting-null-result-from-openlslus_geocodephp">this question</a>, did you put the correct link to the python directory in proxy.cgi? I've used python download from FWTools in my Windows environment. I've copied proxy.cgi to the apache\cgi-bin directory, and changed the first line from</p>
<p>'#!/usr/bin/env python</p>
<p>into:</p>
<p>'#!C:\Gis\apps\FWTools\python\python.exe -u</p>
<p>(without the ' before the # character, but this html can't get this right)</p>
<p>I have a different question concerning the searchservice. My proxy.cgi script is working correctly. Using the standard script openls.html zooms in on the right address. When using the code in my own openlayers.html script, zooming-in doesn't function. The returned code is exactly the same response code as the original script in openls.html. The difference is that i'm using a different projection (see part of the code below)</p>
<pre><code>      function submitform() {
          var queryString = document.forms[0].query.value;
          OpenLayers.Request.POST({
              url: &quot;http://www.openrouteservice.org/php/OpenLSLUS_Geocode.php&quot;,
              scope: this,
              failure: this.requestFailure,
              success: this.requestSuccess,
              headers: {&quot;Content-Type&quot;: &quot;application/x-www-form-urlencoded&quot;},
              data: &quot;FreeFormAdress=&quot; + encodeURIComponent(queryString) + &quot;&amp;MaxResponse=1&quot;
          });
      }
    function requestSuccess(response) {
        var format = new OpenLayers.Format.XLS();
        var output = format.read(response.responseXML);
        if (output.responseLists[0]) {
            var geometry = output.responseLists[0].features[0].geometry;
            var foundPosition = new OpenLayers.LonLat(geometry.x, geometry.y).transform(
                    new OpenLayers.Projection(&quot;EPSG:28992&quot;),
                    map.getProjectionObject()
                    );
            map.setCenter(foundPosition, 16);
        } else {
            alert(&quot;Sorry, no address found&quot;);
        }
    }
&#10;      function requestFailure(response) {
          alert(&quot;no&quot;);
      }</code></pre>
<p>The returned code is not in EPSG:28992, but in EPSG:4326:</p>
<pre><code>&lt;gml:pos srsName=&quot;EPSG:4326&quot;&gt;5.04314283258114 52.3064485837094&lt;/gml:pos&gt;</code></pre>
<p>I assume that the different projection is the reason that zooming isn't working. How can I get this search-zoom-action working? Thanks in advance for any response.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlslus" rel="tag" title="see questions tagged &#39;openlslus&#39;">openlslus</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '12, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f66b0488fc471897c2d4d37f552d5760?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ar_osmap&#39;s gravatar image" />
<p><span>ar_osmap</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ar_osmap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '13, 17:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-10322" class="comments-container">
&#10;</div>
<div id="comment-tools-10322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10322-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="10352"></span>

<div id="answer-container-10352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10352-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you see this?</p>
<p><a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example#Use_Proj4js_for_other_transformations">http://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example#Use_Proj4js_for_other_transformations</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '12, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/7a8cda7811375896a1bb0cf0809dd234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pascal_n&#39;s gravatar image" />
<p><span>pascal_n</span><br />
<span class="score" title="186 reputation points">186</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pascal_n has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-10352" class="comments-container">
<span id="10356"></span>
<div id="comment-10356" class="comment">
<div id="post-10356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Pascal,</p>
<p>Thanks for your response. Unfortunately, it hasn't helped me out. I added:</p>
<pre><code>&lt;script src=&quot;../lib/OpenLayers/proj4js-combined.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;../lib/OpenLayers/EPSG28992.js&quot;&gt;&lt;/script&gt;</code></pre>
<p>and changed:</p>
<pre><code>    function requestSuccess(response) {
        var format = new OpenLayers.Format.XLS();
        var output = format.read(response.responseXML);
        if (output.responseLists[0]) {
            var geometry = output.responseLists[0].features[0].geometry;
            var foundPosition = new OpenLayers.LonLat(geometry.x, geometry.y).transform(
                    new OpenLayers.Projection(&quot;EPSG:28992&quot;),
                    map.getProjectionObject()
                    );
            map.setCenter(
        new OpenLayers.LonLat(131500,479800) // Center of the map
        .transform(
        new OpenLayers.Projection(&quot;EPSG:28992&quot;), // transform from new RD
        new OpenLayers.Projection(&quot;EPSG:4326&quot;) // to default projectie
                    ),
            6); // Zoom level
        } else
        {
            alert(&quot;Sorry, no address found&quot;);
        }
    }
&#10;      function requestFailure(response) {
          alert(&quot;no luck&quot;);
      }</code></pre>
<p>With the original code, without the above .transform addition but zoomlevel changed to 6 the page zooms in to the center coordinate of the map when using the search function.</p>
<p>With the additions above, te page zooms in to 131500,479800 (EPSG:28992, RD-New), but the coordinates (OpenLayers.Control.MousePosition) are shown in EPSG:4326</p>
<p>I'm new with Openlayers, it would be very nice if I could get this address search function working.</p>
<p>Would it be helpful to post (part of) the openlayers.html page?</p>
</div>
<div id="comment-10356-info" class="comment-info">
<span class="comment-age">(31 Jan '12, 20:56)</span> <span class="comment-user userinfo">ar_osmap</span>
</div>
</div>
<span id="10358"></span>
<div id="comment-10358" class="comment">
<div id="post-10358-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The Geocoder will always return coordinates in EPSG:4326. So if you need the coordinate in your system ("EPSG:28992"), this should help you:</p>
<p>var foundPosition = new OpenLayers.LonLat(geometry.x, geometry.y).transform( new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:28992") );</p>
<p>If you have further issues, maybe it could be useful if you post your complete html-page here.</p>
</div>
<div id="comment-10358-info" class="comment-info">
<span class="comment-age">(31 Jan '12, 23:31)</span> <span class="comment-user userinfo">pascal_n</span>
</div>
</div>
<span id="10361"></span>
<div id="comment-10361" class="comment">
<div id="post-10361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Pascal, Thanks a lot, address search is almost perfect now. The only thing is that the found location is about 100 m south of the correct location, after changing +lon in EPSG28992.js, found location is perfect. Another thing is that coordinates (OpenLayers.Control.MousePosition) are shown in EPSG:4326-coordinates instead of EPSG:28992. I can live with that. Yet another thing, when I use the right-arrow cursor in the address search field, the map moves in right direction. This doesn't happen in example openls.html.</p>
<p>I have a question about tilecache to improve performance, but I'll ask that in another forum.</p>
<p>Posting my html-file here doesn't show in the preview, so I forget about that.</p>
<p>Thanks again!</p>
</div>
<div id="comment-10361-info" class="comment-info">
<span class="comment-age">(01 Feb '12, 09:35)</span> <span class="comment-user userinfo">ar_osmap</span>
</div>
</div>
</div>
<div id="comment-tools-10352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10352-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10395"></span>

<div id="answer-container-10395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10395-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>"Another thing is that coordinates (OpenLayers.Control.MousePosition) are shown in EPSG:4326-coordinates instead of EPSG:28992"</em></p>
<p>A displayProjection: new OpenLayers.Projection("EPSG:28992") or new OpenLayers.Control.MousePosition({"numDigits": 2, displayProjection: new OpenLayers.Projection("EPSG:28992")}) should solve your problem.</p>
<p><em>"Yet another thing, when I use the right-arrow cursor in the address search field, the map moves in right direction."</em></p>
<p>You should check your OpenLayers.controls which you addd to your map. Did you add new OpenLayers.Control.KeyboardDefaults()? Maybe try to remove this ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '12, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7a8cda7811375896a1bb0cf0809dd234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pascal_n&#39;s gravatar image" />
<p><span>pascal_n</span><br />
<span class="score" title="186 reputation points">186</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pascal_n has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-10395" class="comments-container">
<span id="10400"></span>
<div id="comment-10400" class="comment">
<div id="post-10400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Pascal, These two things are resolved to! Thanks alot! Arjen</p>
</div>
<div id="comment-10400-info" class="comment-info">
<span class="comment-age">(03 Feb '12, 10:45)</span> <span class="comment-user userinfo">ar_osmap</span>
</div>
</div>
</div>
<div id="comment-tools-10395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10395-form-container" class="comment-form-container">
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

