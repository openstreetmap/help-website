+++
type = "question"
title = "How to do Color Coding for States in OpenStreetMaps"
description = '''Hi, I am using OpenLayers and Open Street Maps API,to display the Maps.and I am able to successfully show Maps,Pins,and the Popups when the User clicks on Pins.However I have a new requirement to represent the States in USA with some colors . Is it possible using Open Street Maps API? Please guide m...'''
date = "2011-11-14T12:42:00Z"
lastmod = "2011-11-18T11:31:00Z"
weight = 8982
keywords = [ "colors" ]
aliases = [ "/questions/8982" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to do Color Coding for States in OpenStreetMaps](/questions/8982/how-to-do-color-coding-for-states-in-openstreetmaps)

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
<span id="post-8982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using OpenLayers and Open Street Maps API,to display the Maps.and I am able to successfully show Maps,Pins,and the Popups when the User clicks on Pins.However I have a new requirement to represent the States in USA with some colors .</p>
<p>Is it possible using Open Street Maps API?</p>
<p>Please guide me to any articles ,if anyone have .</p>
<p>Thanks everyone</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '11, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c330e0454ebc0cf055159a5962e4f6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VenuGopal&#39;s gravatar image" />
<p><span>VenuGopal</span><br />
<span class="score" title="16 reputation points">16</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VenuGopal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8982" class="comments-container">
&#10;</div>
<div id="comment-tools-8982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8982-form-container" class="comment-form-container">
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

<span id="8983"></span>

<div id="answer-container-8983" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8983-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, not with the API.</p>
<p>There are many ways how one could achieve what you say, and recommending something would require knowing more about the exact use cases of your application. However I guess it is most likely that you will want to prepare a KML file with the polygons for US states, and have that displayed in OpenLayers. This is relatively simple, technology-wise.</p>
<p>You could extract the boundaries from OSM but that would probably be too much information for you (too much data to display in the browser at a zoomed-out level). Therefore I guess your best option would be finding KML files for state borders elsewhere - plenty around - or download them in Shapefile form from <a href="http://www.naturalearthdata.com">www.naturalearthdata.com</a> and convert to KML with a free tool like QGis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8983" class="comments-container">
<span id="9006"></span>
<div id="comment-9006" class="comment">
<div id="post-9006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Fredrik,</p>
<p>Thanks for your reply,My Application would involve something like ,</p>
<p>I will have Sales figures for each state</p>
<p>if my Sales are &lt;20-represent that state as red ,&gt;30-&lt;70=yellow and &gt;80 =Green.</p>
<p>if two states side by side having the same colore even though,when I hover the mouse I should be able to identify .I dont have any idea about KML File,Can you provide me any guide to KML File?I am looking for something like</p>
<p><a href="http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/">http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/</a></p>
</div>
<div id="comment-9006-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 11:18)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
<span id="9007"></span>
<div id="comment-9007" class="comment">
<div id="post-9007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Download and install Quantum GIS. That's a free GIS package that allows you to view the shape files from Natural Earth Data, and also export them as KML files. The file that you listed is countries only; if you want states you will have to go to <a href="http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m-admin-1-states-provinces-shp.zip">http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m-admin-1-states-provinces-shp.zip</a> . Once you have KML files you can display them in OpenLayers and you can also highlight clicked areas but this will require a thorough understanding of OpenLayers (search the web for "openlayers kml polygons").</p>
</div>
<div id="comment-9007-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 12:20)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="9034"></span>
<div id="comment-9034" class="comment">
<div id="post-9034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Fredrik, Thanks for your response,I am able to make progress. I downloaded and Installed the QGIS tool to covert the Shape File to KML File. I would like to create a Choropleth map or heat map from this KML File,based on my input sales figures,Do you have any article to develop a choropleth map from KML file?</p>
<p>I am getting an Object Expected error when I am using as below var myvectorlyr= new OpenLayers.Layer.Vector("KML", { projection: map.displayProjection, strategies: [new OpenLayers.Strategy.Fixed()], protocol: new OpenLayers.Protocol.HTTP({ url: "kml/MyStates.kml", format: new OpenLayers.Format.KML({ extractStyles: true, extractAttributes: true }) }) }); map.addLayer(myvectorlyr);</p>
<p>I am using the API as &lt;script src="http://www.openlayers.org/api/OpenLayers/js"&gt;&lt;/script&gt;</p>
</div>
<div id="comment-9034-info" class="comment-info">
<span class="comment-age">(16 Nov '11, 13:24)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
<span id="9093"></span>
<div id="comment-9093" class="comment">
<div id="post-9093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am able to plot the states using the KML file,However the colors are getting the default one all the time,even though I specify some color in the KML file .and I cleared the cache and tried.still that is not working,Any way we can see the specified color in the KML file Thanks Fredrik</p>
</div>
<div id="comment-9093-info" class="comment-info">
<span class="comment-age">(18 Nov '11, 06:09)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
<span id="9106"></span>
<div id="comment-9106" class="comment">
<div id="post-9106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I loaded that KML file in QGIS tool,I am able to see the color for that state in this Tool,However when I am loading this file with OSM Api in html,I am seeing only the Orange Color always</p>
</div>
<div id="comment-9106-info" class="comment-info">
<span class="comment-age">(18 Nov '11, 11:31)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
</div>
<div id="comment-tools-8983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8983-form-container" class="comment-form-container">
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

