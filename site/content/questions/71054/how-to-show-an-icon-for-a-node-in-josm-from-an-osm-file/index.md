+++
type = "question"
title = "How to show an icon for a node in JOSM (from an OSM file)"
description = '''Hello there, I want to be able to display an icon instead of a node when reading an OSM file in JOSM. This is important to me because my user will have to edit OSM files in JOSM. Specifically, the user will have a OSM xml file like this one (minimal example):  I tried adding icon-image=&quot;presets/food...'''
date = "2019-10-06T20:39:00Z"
lastmod = "2019-10-08T04:40:00Z"
weight = 71054
keywords = [ "xml", "josm", "osm", "icon" ]
aliases = [ "/questions/71054" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show an icon for a node in JOSM (from an OSM file)](/questions/71054/how-to-show-an-icon-for-a-node-in-josm-from-an-osm-file)

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
<span id="post-71054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71054-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>I want to be able to display an icon instead of a node when reading an OSM file in JOSM. This is important to me because my user will have to edit OSM files in JOSM. Specifically, the user will have a OSM xml file like this one (minimal example):</p>
<p><img src="https://i.imgur.com/0Vcfdzt.png" alt="xml" /></p>
<p>I tried adding icon-image="presets/food/restaurant.svg" to the node tag, but no luck.</p>
<p>Here is the output that I get in JOSM. I would like to have an icon instead of a node in JOSM.</p>
<p><img src="https://i.imgur.com/VsIv4Xn.png" alt="sample output" /></p>
<p>Is it possible to put an icon instead of a node in JOSM through the XML file?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '19, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7cb04b4cdba3ef7b990e21206f891f4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marcosroriz&#39;s gravatar image" />
<p><span>marcosroriz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marcosroriz has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71054" class="comments-container">
&#10;</div>
<div id="comment-tools-71054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71054-form-container" class="comment-form-container">
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

<span id="71056"></span>

<div id="answer-container-71056" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71056-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wonder which criteria make those nodes stand out from the others:</p>
<ul>
<li>new nodes (but then IDs should be negative, not positive like in your example. It depends on how the JOSM file was generated. Was the data downloaded from the OSM server (positive IDs), or was the data created elsewhere and still has to be uploaded to OSM (negative IDs ?))</li>
<li>no tags</li>
</ul>
<p>so perhaps take a look at Pseudo Classes (:new, !:tagged) in <a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation</a> to select those nodes and style them</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '19, 04:45</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '19, 09:06</strong> </span></p>
</div>
</div>
<div id="comments-container-71056" class="comments-container">
<span id="71058"></span>
<div id="comment-71058" class="comment">
<div id="post-71058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The nodes are bus stops and they are created by the users (hence the basic ids). The overall idea is that I'm using JOSM to enable the users to edit the rural network.</p>
</div>
<div id="comment-71058-info" class="comment-info">
<span class="comment-age">(07 Oct '19, 07:24)</span> <span class="comment-user userinfo">marcosroriz</span>
</div>
</div>
<span id="71059"></span>
<div id="comment-71059" class="comment">
<div id="post-71059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they are bus stops then add the bus stop tag. This will also show a corresponding icon in JOSM. Your question remains unclear, though.</p>
</div>
<div id="comment-71059-info" class="comment-info">
<span class="comment-age">(07 Oct '19, 09:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="71069"></span>
<div id="comment-71069" class="comment">
<div id="post-71069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>, how can I add the bus stop tag?</p>
</div>
<div id="comment-71069-info" class="comment-info">
<span class="comment-age">(08 Oct '19, 04:06)</span> <span class="comment-user userinfo">marcosroriz</span>
</div>
</div>
<span id="71070"></span>
<div id="comment-71070" class="comment">
<div id="post-71070-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>for each node</p>
<p>&lt;node ....&gt; &lt;tag k="highway" v="bus_stop"/&gt; &lt;/node&gt;</p>
<p>see <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">https://wiki.openstreetmap.org/wiki/OSM_XML</a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop">https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop</a></p>
<p>p.s. please note that there are different tagging schemes for <a href="https://wiki.openstreetmap.org/wiki/Public_transport">public transport</a></p>
</div>
<div id="comment-71070-info" class="comment-info">
<span class="comment-age">(08 Oct '19, 04:40)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-71056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71056-form-container" class="comment-form-container">
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

