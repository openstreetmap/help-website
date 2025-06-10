+++
type = "question"
title = "why geting null-result from OpenLSLUS_Geocode.php?"
description = '''Hello, I try to use part of the example http://openlayers.org/dev/examples/openls.html to include a map in my website and let users search for the address. But I alway get a null-value as response.responseXML. To verify that I have no error in my code I have copied the whole example to my site. Call...'''
date = "2011-12-29T21:04:00Z"
lastmod = "2011-12-31T12:32:00Z"
weight = 9690
keywords = [ "search", "proxy.php" ]
aliases = [ "/questions/9690" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [why geting null-result from OpenLSLUS_Geocode.php?](/questions/9690/why-geting-null-result-from-openlslus_geocodephp)

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
<span id="post-9690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9690-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I try to use part of the example <a href="http://openlayers.org/dev/examples/openls.html">http://openlayers.org/dev/examples/openls.html</a> to include a map in my website and let users search for the address. But I alway get a null-value as response.responseXML.</p>
<p>To verify that I have no error in my code I have copied the whole example to my site. Calling it shows the same error as the code in my own site (for the example see code below).</p>
<p>I found a posting in an OSM-forum that I have to use a proxy and so I have installed proxy.php from the mapbuilder-site and changed the code like follows:</p>
<pre><code>            function init() {
            OpenLayers.ProxyHost = &quot;proxy.php?url=&quot;;
            map = new OpenLayers.Map(&#39;map&#39;, {
                controls: [
                    new OpenLayers.Control.PanZoom(),
                    new OpenLayers.Control.Navigation()
                ]
            });
            layer = new OpenLayers.Layer.OSM(&quot;OpenStreetMap&quot;, null, {
                transitionEffect: &#39;resize&#39;
            });
            map.addLayers([layer]);
            map.zoomToMaxExtent();
        }
        function submitform() {
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
alert(response.responseXML);
            var format = new OpenLayers.Format.XLS();
            var output = format.read(response.responseXML);
            if (output.responseLists[0]) {
                var geometry = output.responseLists[0].features[0].geometry;
                var foundPosition = new OpenLayers.LonLat(geometry.x, geometry.y).transform(
                        new OpenLayers.Projection(&quot;EPSG:4326&quot;),
                        map.getProjectionObject()
                        );
                map.setCenter(foundPosition, 16);
            } else {
                alert(&quot;Sorry, no address found&quot;);
            }
        }
        function requestFailure(response) {
            alert(&quot;An error occurred while communicating with the OpenLS service. Please try again.&quot;);
        }</code></pre>
<p>The alert in function requestSuccess(response) returns null whatever I set as proxy. I have tried with "", "proxy.php", "proxy.php?url=", all with the same result. The only diffenrence ist that with "" there are about 5 seconds from calling the service until I get the result. In all other cases (using the proxy.php) the result comes in less than one second.</p>
<p>What is wrong in my code?</p>
<p>(I also tried to use proxy.cgi, but this won't work on my server - I get an 500 internal-server-error)</p>
<p>Thank you for all tipps!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-proxy.php" rel="tag" title="see questions tagged &#39;proxy.php&#39;">proxy.php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '11, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f6df6c2dd8c16fdbc9e5e6c138d1af4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s_glodek&#39;s gravatar image" />
<p><span>s_glodek</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s_glodek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '13, 17:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-9690" class="comments-container">
&#10;</div>
<div id="comment-tools-9690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9690-form-container" class="comment-form-container">
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

<span id="9693"></span>

<div id="answer-container-9693" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9693-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="s_glodek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure that your proxy script is working? You can test this by pointing your normal browser to <a href="http://localhost/proxy.php?url=http://a.tile.openstreetmap.org/0/0/0.png">http://localhost/proxy.php?url=http://a.tile.openstreetmap.org/0/0/0.png</a> Your proxy script needs to support POST as well as GET.</p>
<p>You may want to open the debuging tools in your browser and see what requests get sent and what error messeges you get from them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '11, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9693" class="comments-container">
<span id="9722"></span>
<div id="comment-9722" class="comment">
<div id="post-9722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Jippiyeah!! I have it!!</p>
<p>The error ist the Content-Type: application/xml in the POST-request. I changed it to "Content-Type: application/x-www-form-urlencodedrn" and now it works!</p>
<p>Thanks to Gnonthgol for the hint to use the debug-tools of the browser and to google to find a posting with a short description to send a post in php :-).</p>
</div>
<div id="comment-9722-info" class="comment-info">
<span class="comment-age">(31 Dec '11, 12:32)</span> <span class="comment-user userinfo">s_glodek</span>
</div>
</div>
</div>
<div id="comment-tools-9693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9693-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9695"></span>

<div id="answer-container-9695" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9695-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please use the OpenLayers proxy.cgi explained here: <a href="http://trac.osgeo.org/openlayers/wiki/FrequentlyAskedQuestions#ProxyHost">http://trac.osgeo.org/openlayers/wiki/FrequentlyAskedQuestions#ProxyHost</a></p>
<p>The normal OpenLayers proxy.cgi already contains the OpenRouteService host. See here: <a href="http://trac.osgeo.org/openlayers/browser/trunk/openlayers/examples/proxy.cgi">http://trac.osgeo.org/openlayers/browser/trunk/openlayers/examples/proxy.cgi</a></p>
<p>Please beware that the proxy script has the right permission to execute! Hope that helps :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '11, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7a8cda7811375896a1bb0cf0809dd234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pascal_n&#39;s gravatar image" />
<p><span>pascal_n</span><br />
<span class="score" title="186 reputation points">186</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pascal_n has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-9695" class="comments-container">
<span id="9720"></span>
<div id="comment-9720" class="comment">
<div id="post-9720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not able to use proxy.cgi - it always returns 500 - server error.</p>
<p>Using proxy.php I can see with firebug that proxy.php sends the following request:</p>
<pre><code>POST /php/OpenLSLUS_Geocode.php? HTTP/1.0
Host:www.openrouteservice.org
User-Agent: MyAgent
Content-Type: application/xml
Content-Length: 62
&#10;FreeFormAdress=Rue%20des%20Berges%2037%20Payerne&amp;MaxResponse=1</code></pre>
<p>The answer from <a href="http://www.openrouteservice.org">www.openrouteservice.org</a> is</p>
<pre><code>HTTP/1.1 200 OK
Date: Sat, 31 Dec 2011 11:57:44 GMT
Server: Apache
X-Powered-By: PHP/5.2.6-1+lenny13
Vary: Accept-Encoding
Content-Length: 20
Connection: close
Content-Type: text/html
&#10;Nix uebermittelt!!</code></pre>
<p>It seems to be an error in transferring the POST-data. The proxy.php-script is available as text-file on <a href="http://osm.glodek-edv.de/proxy.txt">http://osm.glodek-edv.de/proxy.txt</a> and the test-site is <a href="http://osm.glodek-edv.de/openls.html">http://osm.glodek-edv.de/openls.html</a></p>
</div>
<div id="comment-9720-info" class="comment-info">
<span class="comment-age">(31 Dec '11, 12:09)</span> <span class="comment-user userinfo">s_glodek</span>
</div>
</div>
</div>
<div id="comment-tools-9695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9695-form-container" class="comment-form-container">
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

