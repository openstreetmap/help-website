+++
type = "question"
title = "xapi-request runs into server error - How can make sense of XAPI"
description = '''pretty new to Geo-Informatics so do not bear with me if my questions sound like newbie-questions: can i do some requests on POIs of Openstreetmap with XAPI. doing like so: i send a request to the API-Server - over http  as a respond i get the following result - in XML  example: the following link gi...'''
date = "2012-04-17T22:44:00Z"
lastmod = "2013-07-31T17:00:00Z"
weight = 12100
keywords = [ "xml", "openstreetmap", "xapi", "example" ]
aliases = [ "/questions/12100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [xapi-request runs into server error - How can make sense of XAPI](/questions/12100/xapi-request-runs-into-server-error-how-can-make-sense-of-xapi)

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
<span id="post-12100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12100-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>pretty new to Geo-Informatics so do not bear with me if my questions sound like newbie-questions: can i do some requests on POIs of Openstreetmap with XAPI.</p>
<p>doing like so: i send a request to the API-Server - over http as a respond i get the following result - in XML</p>
<p><strong>example:</strong> the following link gives back all the Nodes of the Type amenity=restaurant in XML-Format.Note: the bounding box (bbox) limits the area:</p>
<pre><code>http://xapi.openstreetmap.org/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]
&#10;http://xapi.openstreetmap.org/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]</code></pre>
<p>see here the results:_</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; standalone=&#39;no&#39;?&gt;
&lt;osm version=&#39;0.6&#39; generator=&#39;xapi: OSM Extended API 2.0&#39; xmlns:xapi=&#39;http://www.informationfreeway.org/xapi/0.6&#39; xapi:uri=&#39;/api/0.6/node[amenity=restaurant|fast_food|pub|cafe][bbox=9.4908142,48.7810801,9.5660019,48.8387351]&#39; xapi:planetDate=&#39;20100824&#39; xapi:copyright=&#39;2010 OpenStreetMap contributors&#39; xapi:license=&#39;Creative commons CC-BY-SA 2.0&#39; xapi:bugs=&#39;For assistance or to report bugs contact 80n80n@gmail.com&#39; xapi:instance=&#39;zappyOsm&#39;&gt;
&lt;node id=&#39;721241970&#39; lat=&#39;48.830856&#39; lon=&#39;9.5116892&#39; user=&#39;mabe75&#39; timestamp=&#39;2010-05-04T19:01:28Z&#39; uid=&#39;260302&#39; version=&#39;1&#39; changeset=&#39;4607010&#39;&gt;
&lt;tag k=&#39;amenity&#39; v=&#39;restaurant&#39;/&gt;
&lt;tag k=&#39;name&#39; v=&#39;Lamm&#39;/&gt;
&lt;/node&gt;
&lt;node id=&#39;392682646&#39; lat=&#39;48.8315734&#39; lon=&#39;9.5468864&#39; user=&#39;MattGPS&#39; timestamp=&#39;2010-05-11T19:00:20Z&#39; uid=&#39;12973&#39; version=&#39;3&#39; changeset=&#39;4671372&#39;&gt;
&lt;tag k=&#39;amenity&#39; v=&#39;restaurant&#39;/&gt;
&lt;tag k=&#39;name&#39; v=&#39;Gasthaus an der Wieslauf&#39;/&gt;
&lt;/node&gt;
&lt;node id=&#39;319597380&#39; lat=&#39;48.8277913&#39; lon=&#39;9.5477029&#39; timestamp=&#39;2008-12-17T21:13:15Z&#39; version=&#39;1&#39; changeset=&#39;444629&#39;&gt;
&lt;tag k=&#39;amenity&#39; v=&#39;restaurant&#39;/&gt;
&lt;tag k=&#39;name&#39; v=&#39;Gasthaus zur Linde&#39;/&gt;
&lt;/node&gt;
[...]</code></pre>
<p>well this example does not work here... what do ido wrong</p>
<p><strong>By the way</strong>. How to get the results stored in a databasse- note i have to convert the xml to a db-sheme.. mysql is preferred- any idea and helping hand is greatly appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-example" rel="tag" title="see questions tagged &#39;example&#39;">example</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '12, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '12, 07:21</strong> </span></p>
</div>
</div>
<div id="comments-container-12100" class="comments-container">
&#10;</div>
<div id="comment-tools-12100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12100-form-container" class="comment-form-container">
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

<span id="12105"></span>

<div id="answer-container-12105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12105-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although <a href="http://wiki.openstreetmap.org/wiki/Xapi">this page</a> doesn't explicitly say where xapi.opentreetmap.org points to these days, it does say that jxapi.openstreetmap.org (which it might point to) is down for maintenance right now. However, Mapquests's jxapi instance should be up, so you should be able to do that. I've just tried this:</p>
<pre><code>wget http://open.mapquestapi.com/xapi/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]</code></pre>
<p>and it works. Note that there's an extra "/api" in the Mapquest xapi URL. The bbox is currently limited to 10 square degrees. See the various links from the XAPI wiki page for more info, including the terms of service for the Mapquest instance of the XAPI.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12105" class="comments-container">
<span id="12109"></span>
<div id="comment-12109" class="comment">
<div id="post-12109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many many thx</p>
</div>
<div id="comment-12109-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 01:47)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="12111"></span>
<div id="comment-12111" class="comment">
<div id="post-12111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>By the way</strong>. How to get the results stored in a databasse- note i have to convert the xml to a db-sheme.. mysql is preferred- any idea and helping hand is greatly appreciated</p>
</div>
<div id="comment-12111-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 07:21)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="24768"></span>
<div id="comment-24768" class="comment">
<div id="post-24768-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried this and it ran. I am such a newbie that I have no idea where the results ended up. On my PC somewhere?</p>
<p>Would appreciate help.</p>
</div>
<div id="comment-24768-info" class="comment-info">
<span class="comment-age">(31 Jul '13, 16:54)</span> <span class="comment-user userinfo">walkergeoff</span>
</div>
</div>
<span id="24769"></span>
<div id="comment-24769" class="comment">
<div id="post-24769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It'll be on your PC, wherever you ran it from. I've just run it from the command line in the c:\temp folder and ended up with a file called "node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]" in there, so I'd loke for files with e.g. 7810801 in them.</p>
</div>
<div id="comment-24769-info" class="comment-info">
<span class="comment-age">(31 Jul '13, 17:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12105-form-container" class="comment-form-container">
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

