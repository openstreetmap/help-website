+++
type = "question"
title = "How to get Map corner latlong using open layer.??"
description = '''How to get Map corner latlong using open layer.??? i had tried with map.getBounds() method but it shows error like &quot;map.getBounds is not a function&quot; so kindly reply for this error or any example. here i had use OpenLayers.js'''
date = "2016-07-07T08:44:00Z"
lastmod = "2016-07-27T07:22:00Z"
weight = 50696
keywords = [ "openlayers", "getbounds" ]
aliases = [ "/questions/50696" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to get Map corner latlong using open layer.??](/questions/50696/how-to-get-map-corner-latlong-using-open-layer)

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
<span id="post-50696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50696-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to get Map corner latlong using open layer.??? i had tried with map.getBounds() method but it shows error like "map.getBounds is not a function"</p>
<p>so kindly reply for this error or any example.</p>
<p>here i had use OpenLayers.js</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-getbounds" rel="tag" title="see questions tagged &#39;getbounds&#39;">getbounds</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '16, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/fc38080d9e980459bc64bf221f56bc62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jatin%20Patel&#39;s gravatar image" />
<p><span>Jatin Patel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jatin Patel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '16, 09:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-50696" class="comments-container">
<span id="50801"></span>
<div id="comment-50801" class="comment">
<div id="post-50801-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You have to provide more information. Show us the part of your code where <code>getBounds()</code> is failing.</p>
</div>
<div id="comment-50801-info" class="comment-info">
<span class="comment-age">(11 Jul '16, 08:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50696-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="50697"></span>

<div id="answer-container-50697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>getBounds()</code> only works for OpenLayers 2. Since it is failing for you I assume that you are using OpenLayers 3.</p>
<p>For OpenLayers 3 you have to look at the map <em>extent</em> by calling <code>map.getView().calculateExtent()</code> according to these similar questions:</p>
<ul>
<li><a href="https://stackoverflow.com/questions/22206570/how-do-bounds-work-in-openlayers-3">https://stackoverflow.com/questions/22206570/how-do-bounds-work-in-openlayers-3</a></li>
<li><a href="https://stackoverflow.com/questions/28166471/openlayer3-how-to-get-coordinates-of-viewport">https://stackoverflow.com/questions/28166471/openlayer3-how-to-get-coordinates-of-viewport</a></li>
<li><a href="https://gis.stackexchange.com/questions/168590/how-to-get-extent-in-openlayers-3">https://gis.stackexchange.com/questions/168590/how-to-get-extent-in-openlayers-3</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-50697" class="comments-container">
<span id="50799"></span>
<div id="comment-50799" class="comment">
<div id="post-50799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>map.getView().calculateExtent() does not work in OpenLayer3.</p>
<p>i use below link in open layer.</p>
<p><a href="http://www.openlayers.org/api/OpenLayers.js">http://www.openlayers.org/api/OpenLayers.js</a></p>
</div>
<div id="comment-50799-info" class="comment-info">
<span class="comment-age">(11 Jul '16, 08:15)</span> <span class="comment-user userinfo">Jatin Patel</span>
</div>
</div>
<span id="50800"></span>
<div id="comment-50800" class="comment">
<div id="post-50800-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is OpenLayers 2.</p>
</div>
<div id="comment-50800-info" class="comment-info">
<span class="comment-age">(11 Jul '16, 08:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50861"></span>
<div id="comment-50861" class="comment">
<div id="post-50861-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your <code>GetData()</code> function has no local <code>map</code> object. You need to pass your <code>map</code> object as parameter or make it global. Currently it is only known inside <code>init()</code>.</p>
</div>
<div id="comment-50861-info" class="comment-info">
<span class="comment-age">(12 Jul '16, 10:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50697-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50859"></span>

<div id="answer-container-50859" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50859-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Above Both function not working.</p>
<p>below is the my code, please correct it.</p>
<p>=====================================</p>
<p>&lt;html&gt; &lt;head&gt; &lt;title&gt;OpenLayers Demo&lt;/title&gt; &lt;style type="text/css"&gt; html, body, #basicMap { width: 100%; height: 100%; margin: 0; } &lt;/style&gt;</p>
<pre><code>&lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
    function init() {
        var marker_layer = new OpenLayers.Layer.Markers(&quot;Markers&quot;);
&#10;        map = new OpenLayers.Map(&quot;basicMap&quot;);
        var mapnik = new OpenLayers.Layer.OSM();
        var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);   // Transform from WGS 1984
        var toProjection = new OpenLayers.Projection(&quot;EPSG:900913&quot;); // to Spherical Mercator Projection
&#10;        var position1 = new OpenLayers.LonLat(78.9629, 20.5937).transform(fromProjection, toProjection);
        var position2 = new OpenLayers.LonLat(79.2629, 20.9937).transform(fromProjection, toProjection);
        var zoom = 8;
&#10;        map.addLayer(mapnik);
        map.setCenter(position1, zoom);
&#10;    }
&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
    function GetData() {
        debugger;
&#10;        //var bounds = map.getBounds();       //Error : map.getBounds is not a function
&#10;        //var vv1 = map.getView().calculateExtent();  //Error : map.getView is not a function
    }
&lt;/script&gt;</code></pre>
<p>&lt;/head&gt; &lt;body onload="init();"&gt; &lt;input id="Button1" type="button" value="Click Here" onclick="GetData();"/&gt;</p>
<div>
&#10;</div>
&lt;/body&gt; &lt;/html&gt;
<p>=====================================</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '16, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/fc38080d9e980459bc64bf221f56bc62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jatin%20Patel&#39;s gravatar image" />
<p><span>Jatin Patel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jatin Patel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '16, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-50859" class="comments-container">
&#10;</div>
<div id="comment-tools-50859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50867"></span>

<div id="answer-container-50867" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At this i have not use function but still i got an error.</p>
<p>==============================================</p>
<p>&lt;html&gt; &lt;head&gt; &lt;title&gt;OpenLayers Demo&lt;/title&gt; &lt;style type="text/css"&gt; html, body, #basicMap { width: 100%; height: 100%; margin: 0; } &lt;/style&gt;</p>
<pre><code>&lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
    function init() {
        var marker_layer = new OpenLayers.Layer.Markers(&quot;Markers&quot;);
&#10;        var map = new OpenLayers.Map(&quot;basicMap&quot;);
        var mapnik = new OpenLayers.Layer.OSM();
        var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);   // Transform from WGS 1984
        var toProjection = new OpenLayers.Projection(&quot;EPSG:900913&quot;); // to Spherical Mercator Projection
&#10;        var position1 = new OpenLayers.LonLat(78.9629, 20.5937).transform(fromProjection, toProjection);
        var position2 = new OpenLayers.LonLat(79.2629, 20.9937).transform(fromProjection, toProjection);
        var zoom = 8;
&#10;        map.addLayer(mapnik);
        map.setCenter(position1, zoom);
&#10;
        debugger;
&#10;        var bounds = map.getBounds();       //Error : map.getBounds is not a function
&#10;        var vv1 = map.getView().calculateExtent();  //Error : map.getView is not a function
&#10;    }
&lt;/script&gt;</code></pre>
<p>&lt;/head&gt; &lt;body onload="init();"&gt;</p>
<div>
&#10;</div>
&lt;/body&gt; &lt;/html&gt;
<p>==============================================</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '16, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/fc38080d9e980459bc64bf221f56bc62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jatin%20Patel&#39;s gravatar image" />
<p><span>Jatin Patel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jatin Patel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50867" class="comments-container">
<span id="50937"></span>
<div id="comment-50937" class="comment">
<div id="post-50937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try <code>map.getExtent()</code> for OpenLayers 2, see <a href="http://dev.openlayers.org/docs/files/OpenLayers/Map-js.html#OpenLayers.Map.getExtent.">http://dev.openlayers.org/docs/files/OpenLayers/Map-js.html#OpenLayers.Map.getExtent.</a> And please don't add <em>answers</em> to your <em>question</em>, use the comment function instead.</p>
</div>
<div id="comment-50937-info" class="comment-info">
<span class="comment-age">(16 Jul '16, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50978"></span>
<div id="comment-50978" class="comment">
<div id="post-50978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then what was the formula for find corner latlong.????</p>
</div>
<div id="comment-50978-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 10:34)</span> <span class="comment-user userinfo">Jatin Patel</span>
</div>
</div>
<span id="50979"></span>
<div id="comment-50979" class="comment">
<div id="post-50979-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><code>getExtent()</code> returns an <a href="http://dev.openlayers.org/docs/files/OpenLayers/BaseTypes/Bounds-js.html#OpenLayers.Bounds">OpenLayers.Bounds</a> object. It has <code>left</code>, <code>bottom</code>, <code>right</code> and <code>top</code> as properties.</p>
</div>
<div id="comment-50979-info" class="comment-info">
<span class="comment-age">(19 Jul '16, 10:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51009"></span>
<div id="comment-51009" class="comment">
<div id="post-51009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any calculation for getting corner latlong from the getExtend(). because i got only one value from left, bottom, right and top. so kindly help me.</p>
</div>
<div id="comment-51009-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 06:48)</span> <span class="comment-user userinfo">Jatin Patel</span>
</div>
</div>
<span id="51010"></span>
<div id="comment-51010" class="comment">
<div id="post-51010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please take some time and read through the documentation. See <a href="http://dev.openlayers.org/docs/files/OpenLayers/BaseTypes/LonLat-js.html">OpenLayers.LonLat</a>, just pass the corresponding corners in the constructor.</p>
</div>
<div id="comment-51010-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 07:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51123"></span>
<div id="comment-51123" class="comment not_top_scorer">
<div id="post-51123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot sir... i got solution for my question but now i want to set view using this bounds left, bottom, right,top and zoom. so how can i do this.???</p>
</div>
<div id="comment-51123-info" class="comment-info">
<span class="comment-age">(27 Jul '16, 07:22)</span> <span class="comment-user userinfo">Jatin Patel</span>
</div>
</div>
</div>
<div id="comment-tools-50867" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50867-form-container" class="comment-form-container">
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

