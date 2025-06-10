+++
type = "question"
title = "transforming xml-output from a xapi-search: how to store this in a mysql-database"
description = '''how can i get plain xml to a mysql-db-formate? well i do some requests: i am doing like so: i send a request to the API-Server - over http as a respond i get the following result - in XML example: the following link gives back all the Nodes of the Type amenity=restaurant in XML-Format.Note: the boun...'''
date = "2012-04-18T07:35:00Z"
lastmod = "2012-04-18T07:35:00Z"
weight = 12112
keywords = [ "xml", "mysql" ]
aliases = [ "/questions/12112" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [transforming xml-output from a xapi-search: how to store this in a mysql-database](/questions/12112/transforming-xml-output-from-a-xapi-search-how-to-store-this-in-a-mysql-database)

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
<span id="post-12112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12112-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-12112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how can i get plain xml to a mysql-db-formate?</p>
<p>well i do some requests:</p>
<p>i am doing like so: i send a request to the API-Server - over http as a respond i get the following result - in XML</p>
<p>example: the following link gives back all the Nodes of the Type amenity=restaurant in XML-Format.Note: the bounding box (bbox) limits the area:</p>
<p><a href="http://xapi.openstreetmap.org/api/0.6/node%5Bamenity=restaurant%5D%5Bbbox=9.4908142,48.7810801,9.5660019,48.8387351%5D">http://xapi.openstreetmap.org/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]</a></p>
<p><a href="http://xapi.openstreetmap.org/api/0.6/node%5Bamenity=restaurant%5D%5Bbbox=9.4908142,48.7810801,9.5660019,48.8387351%5D">http://xapi.openstreetmap.org/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]</a></p>
<p>note - i do it with wget since the XAPI-service is down for maintenance</p>
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
<p>well this example works pretty well - if i do it with wget.</p>
<p>question: how can i get plain xml to a mysql-db-formate?</p>
<p>any idea and pointer towards a way to go will be greatly appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '12, 07:35</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12112" class="comments-container">
&#10;</div>
<div id="comment-tools-12112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12112-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

