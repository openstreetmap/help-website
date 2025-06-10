+++
type = "question"
title = "Extracting Bounding Box from Type:Area using OSMPythonTools"
description = '''Hi everyone, I am working on a project where I am retrieving oil palm plantations from Benin using OSM and I am hoping to get the bounding box of each plantation. I was wondering if anyone knows how to extract the bounding box surrounding each plantation or any kind of longitude and latitude informa...'''
date = "2021-03-29T20:22:00Z"
lastmod = "2021-03-29T22:18:00Z"
weight = 79436
keywords = [ "python", "overpass", "nominatim", "boundaries" ]
aliases = [ "/questions/79436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting Bounding Box from Type:Area using OSMPythonTools](/questions/79436/extracting-bounding-box-from-typearea-using-osmpythontools)

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
<span id="post-79436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79436-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, I am working on a project where I am retrieving oil palm plantations from Benin using OSM and I am hoping to get the bounding box of each plantation. I was wondering if anyone knows how to extract the bounding box surrounding each plantation or any kind of longitude and latitude information. I could not figure out how to extract any relevant geometry information about type: area only nodes and ways. I included my code below I have so far and will clarify anything I need to. Thank You!</p>
<pre><code>from OSMPythonTools.overpass import overpassQueryBuilder
from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import Overpass
&#10;nominatim = Nominatim() #How to call OpenStreetMaps Query Function
benin = nominatim.query(&#39;Benin&#39;) #Interested in Benin West Africa
&#10;oil_palm_trees = overpassQueryBuilder(area=benin.areaId(), elementType=&#39;area&#39;,includeGeometry = True ,selector=[&#39;&quot;landuse&quot;=&quot;orchard&quot;&#39;,
&#39;&quot;trees&quot; = &quot;oil_palms&quot;&#39;], out=&#39;body&#39;)
&#10;overpass = Overpass()
oil_palm_plantation = overpass.query(oil_palm_trees)
&#10;oil_palm_plantation.elements() #show the elements returned from query
oil_palm_plantation.toJSON() #sbow the JSON Information, hoping to get the geometries</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '21, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/cf2f9c9a261b024af84e763c8c7d9b00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geographylover&#39;s gravatar image" />
<p><span>geographylover</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geographylover has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79436" class="comments-container">
&#10;</div>
<div id="comment-tools-79436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79436-form-container" class="comment-form-container">
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

<span id="79437"></span>

<div id="answer-container-79437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>out bb;</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '21, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79437" class="comments-container">
<span id="79438"></span>
<div id="comment-79438" class="comment">
<div id="post-79438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Dave thanks for the response. I tried doing this and the query worked but I still do not know how to extract the information. Sorry I am still a bit of a noob at this, so any help would be appreciated.</p>
</div>
<div id="comment-79438-info" class="comment-info">
<span class="comment-age">(29 Mar '21, 21:09)</span> <span class="comment-user userinfo">geographylover</span>
</div>
</div>
<span id="79440"></span>
<div id="comment-79440" class="comment">
<div id="post-79440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't use Python, but assume it's the same way you parse any data in XML. Try running the routine in Overpass Turbo &amp; look under the data tag to see what's returned.</p>
</div>
<div id="comment-79440-info" class="comment-info">
<span class="comment-age">(29 Mar '21, 22:18)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-79437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79437-form-container" class="comment-form-container">
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

