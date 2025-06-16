+++
type = "question"
title = "Help to download a file .osm"
description = '''Hi, i want to download a file .osm that contain the map of the bicycles stations &quot;Vélo V&quot; in Lyon, France. I found this link: http://umap.openstreetmap.fr/fr/map/lyon-velo-velov_4779#14/45.7602/4.8621 the problem that from this link, i can&#x27;t download a file .osm. I can just download a file .geojson ...'''
date = "2015-11-18T14:51:00Z"
lastmod = "2017-10-21T18:32:00Z"
weight = 46679
keywords = [ "umap", "kml", ".osm" ]
aliases = [ "/questions/46679" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help to download a file .osm](/questions/46679/help-to-download-a-file-osm)

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
<span id="post-46679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i want to download a file .osm that contain the map of the bicycles stations "Vélo V" in Lyon, France. I found this link:</p>
<p><a href="http://umap.openstreetmap.fr/fr/map/lyon-velo-velov_4779#14/45.7602/4.8621">http://umap.openstreetmap.fr/fr/map/lyon-velo-velov_4779#14/45.7602/4.8621</a></p>
<p>the problem that from this link, i can't download a file .osm. I can just download a file .geojson , .gpx and .kml .</p>
<p>I need to download the file .osm because i will use it in SUMO simulator. Please can anybody help me. Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '15, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/b408abbe87d5551cc26d19f0bb74b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MyriamBah&#39;s gravatar image" />
<p><span>MyriamBah</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MyriamBah has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '15, 20:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46679" class="comments-container">
&#10;</div>
<div id="comment-tools-46679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46679-form-container" class="comment-form-container">
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

<span id="46680"></span>

<div id="answer-container-46680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46680-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-46680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get the data from Overpass API. Here's a query to start with:</p>
<p><a href="http://overpass-turbo.eu/s/cO9">http://overpass-turbo.eu/s/cO9</a></p>
<p>Click "Export" and then select "Raw data" in the dialog to save an osm file.</p>
<p>I started by putting</p>
<pre><code>amenity=bicycle_rental and network=&quot;Vélo&#39;v&quot; in &quot;Lyon, France&quot;</code></pre>
<p>into the Wizard, which defaults to asking for json output. I deleted <code>[out:json]</code> from the query to get what you see there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '15, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '15, 17:10</strong> </span></p>
</div>
</div>
<div id="comments-container-46680" class="comments-container">
<span id="46684"></span>
<div id="comment-46684" class="comment">
<div id="post-46684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your response. I downloaded the osm file succesfully. Now, i want to use this file for simulation using SUMO simulator. when i tried to convert this file to .net.xml with the following command:</p>
<p>netconvert --osm-files export.osm –o export.net.xml</p>
<p>i get this errors:</p>
<p>Error: No nodes loaded. Quitting (on error).</p>
<p>Have you an idea to resolve this problem please? Thanks.</p>
</div>
<div id="comment-46684-info" class="comment-info">
<span class="comment-age">(18 Nov '15, 18:02)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46686"></span>
<div id="comment-46686" class="comment">
<div id="post-46686-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I guess I misunderstood the data that you wanted to access. The query I linked is just the locations of the bicycle stations, it doesn't include any of the roads.</p>
</div>
<div id="comment-46686-info" class="comment-info">
<span class="comment-age">(18 Nov '15, 18:17)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46748"></span>
<div id="comment-46748" class="comment not_top_scorer">
<div id="post-46748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it possible to download the streets for the osm file? So I will have a osm file which contain the bicycle stations and the streets. If so what can I add as request to dowload the streets please ?</p>
</div>
<div id="comment-46748-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 08:39)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46762"></span>
<div id="comment-46762" class="comment">
<div id="post-46762-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here's an amended query with highways:</p>
<p><a href="http://overpass-turbo.eu/s/cQQ">http://overpass-turbo.eu/s/cQQ</a></p>
<p>The streets are a lot of data so you may have to find a way to download the data directly from the Overpass API instead of using a web browser and Overpass Turbo.</p>
</div>
<div id="comment-46762-info" class="comment-info">
<span class="comment-age">(21 Nov '15, 01:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46790"></span>
<div id="comment-46790" class="comment not_top_scorer">
<div id="post-46790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi thank you very much for your response. I need also to add relations in the osm file. How can I add this in the query of Overpass please?</p>
</div>
<div id="comment-46790-info" class="comment-info">
<span class="comment-age">(23 Nov '15, 14:57)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46793"></span>
<div id="comment-46793" class="comment not_top_scorer">
<div id="post-46793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In fact I need to have a osm file that contains nodes, ways and relations of the bicycle stations. How can I do this please?</p>
</div>
<div id="comment-46793-info" class="comment-info">
<span class="comment-age">(23 Nov '15, 15:27)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46795"></span>
<div id="comment-46795" class="comment">
<div id="post-46795-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The second query should have all of the bicycle stations within whatever boundary is chosen as Lyon and all of the highways. The earlier query returns the nodes ways and relations of bicycle stations without anything else.</p>
<p>I would urge you to try to adjust the query yourself. A couple things about overpass: you have to request nodes, ways and relations if you want them all. Those results are combined by putting them inside of parenthesis (you can see this in the example queries). It is also necessary to request the members of ways and relations, this is what the final lines of the examples are doing. The <code>&gt;;</code> on the second to last line is an instruction to find the members, the last line says to add them to the output.</p>
<p>The description of the query language may be helpful:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
<p>I don't mean to be unhelpful, but understanding the data model will be useful when working with the data, and with an understanding of the data model, it should be simple to modify the overpass query to return the desired data.</p>
</div>
<div id="comment-46795-info" class="comment-info">
<span class="comment-age">(23 Nov '15, 16:00)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46809"></span>
<div id="comment-46809" class="comment not_top_scorer">
<div id="post-46809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for you. It is very interesting to me to learn the overpass query language. I have modified ( &gt;;) in the result part with (&lt;;). I get 266 nodes, 9714 ways and 1706 relations instead of 38555 nodes, 9714 ways and 0 relations. I would know if the change I did is correct?</p>
</div>
<div id="comment-46809-info" class="comment-info">
<span class="comment-age">(24 Nov '15, 11:42)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46810"></span>
<div id="comment-46810" class="comment">
<div id="post-46810-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>&lt;; fetches the parents of the input set (so if a node in the input is part of several ways, it would return the ways in the output), it probably isn't necessary for the data you are interested in.</p>
<p>My guess would be that you would only need to add node,way,relation queries based on additional tags, the items you said you want to work with are not modeled in complicated ways and it probably won't take further processing to retrieve them with overpass.</p>
</div>
<div id="comment-46810-info" class="comment-info">
<span class="comment-age">(24 Nov '15, 11:54)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="46813"></span>
<div id="comment-46813" class="comment not_top_scorer">
<div id="post-46813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My goal is to have a osm file that contain the map of the bicycles stations "Vélo V" in Lyon, France which contain nodes, ways and relations. Please can you help me to do this with Overpass?</p>
</div>
<div id="comment-46813-info" class="comment-info">
<span class="comment-age">(24 Nov '15, 13:53)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
<span id="46839"></span>
<div id="comment-46839" class="comment not_top_scorer">
<div id="post-46839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please can you respond me to have the osm file. Really I need this to continue my phd work. Thanks in advance.</p>
</div>
<div id="comment-46839-info" class="comment-info">
<span class="comment-age">(25 Nov '15, 13:56)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
</div>
<div id="comment-tools-46680" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46681"></span>

<div id="answer-container-46681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46681-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general we have a collection of sources for rae OSM XML data in the OSM wiki at <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">planet.osm</a></p>
<p>Read all the hints there ... for a regional extract for only a city I recommend to load an extract from geofabrik.de</p>
<p>There are more tools then, if you want do cut that extract even in smaller pieces, tell us if you need those.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '15, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-46681" class="comments-container">
<span id="46685"></span>
<div id="comment-46685" class="comment">
<div id="post-46685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your response. I will try to use it.</p>
</div>
<div id="comment-46685-info" class="comment-info">
<span class="comment-age">(18 Nov '15, 18:07)</span> <span class="comment-user userinfo">MyriamBah</span>
</div>
</div>
</div>
<div id="comment-tools-46681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46681-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60201"></span>

<div id="answer-container-60201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i am new and i can't use sumo properly, please help me i cant not import osm to sumo 0.31.0 , please guide me ????? .....</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '17, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/3f79f1b7fcd7b08be59c03a67fe84b5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khanali&#39;s gravatar image" />
<p><span>khanali</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khanali has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60201" class="comments-container">
<span id="60202"></span>
<div id="comment-60202" class="comment">
<div id="post-60202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i have facing some issues when i work on SUMO, please guide me any one how i import OSM data of a city to sumo for simulation.please anyone can guide me?? my contact is akbaraliiiu@gmail.com</p>
</div>
<div id="comment-60202-info" class="comment-info">
<span class="comment-age">(21 Oct '17, 17:55)</span> <span class="comment-user userinfo">khanali</span>
</div>
</div>
<span id="60203"></span>
<div id="comment-60203" class="comment">
<div id="post-60203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd suggest adding this as a separate question. It would also help to explain what SUMO is.</p>
</div>
<div id="comment-60203-info" class="comment-info">
<span class="comment-age">(21 Oct '17, 18:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60205"></span>
<div id="comment-60205" class="comment">
<div id="post-60205-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've moved your "answer" to a new question at <a href="/questions/60204/sumo-how-to-import-data">https://help.openstreetmap.org/questions/60204/sumo-how-to-import-data</a> .</p>
</div>
<div id="comment-60205-info" class="comment-info">
<span class="comment-age">(21 Oct '17, 18:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60201-form-container" class="comment-form-container">
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

