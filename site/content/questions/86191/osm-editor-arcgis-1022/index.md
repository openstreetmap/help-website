+++
type = "question"
title = "OSM editor ArcgIS 10.2.2"
description = '''Hi, I use OSM editor for ArcGIS 10.2.2 , I did get data from osm, load it to arcgis, symbolized it, add osm editor, edited data, add new peaks, save data.  but upload som data tool is not working.  I get the message  The underlying connection was closed. An unexpected error occured on a send.  I use...'''
date = "2022-11-19T20:35:00Z"
lastmod = "2022-11-25T19:16:00Z"
weight = 86191
keywords = [ "osm", "osmeditor2.1" ]
aliases = [ "/questions/86191" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM editor ArcgIS 10.2.2](/questions/86191/osm-editor-arcgis-1022)

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
<span id="post-86191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I use OSM editor for ArcGIS 10.2.2 , I did get data from osm, load it to arcgis, symbolized it, add osm editor, edited data, add new peaks, save data.</p>
<p>but upload som data tool is not working.</p>
<p>I get the message</p>
<p>The underlying connection was closed. An unexpected error occured on a send.</p>
<p>I use url <a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a> for Open Street Map base upload URL.</p>
<p>I have lot of free time and knowladge how to use gis data and I would like to improve OSM map, but without uploading data to OSM is hard to do it.</p>
<p>Do you know anybody who use arcGIS for editing OSM data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmeditor2.1" rel="tag" title="see questions tagged &#39;osmeditor2.1&#39;">osmeditor2.1</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '22, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/200e6f6af816facec6260816c8749707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grzes978&#39;s gravatar image" />
<p><span>Grzes978</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grzes978 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86191" class="comments-container">
<span id="86198"></span>
<div id="comment-86198" class="comment">
<div id="post-86198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for reply, Could you give me some advice on how to do it? I am not familiar with JOSM.</p>
<p>Could we make a conversation PM? My email is [e-mail removed]</p>
<p>Now I can do editions in ArcGIS and I see that revison tables "see" my changes in dataset. But what to do next in order to upload it to OSM. It is black magic :-)</p>
</div>
<div id="comment-86198-info" class="comment-info">
<span class="comment-age">(22 Nov '22, 09:02)</span> <span class="comment-user userinfo">Grzes978</span>
</div>
</div>
<span id="86216"></span>
<div id="comment-86216" class="comment">
<div id="post-86216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>'s answer (and <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>'s comment) are both correct, but aside from that I'd expect that using "http://www.openstreetmap.org/" as an API URL is wrong for a couple of reasons.</p>
<p>One is that its http not https (an http request will result in the client being told to use https, but not all clients follow redirects).</p>
<p>The other is that I'd actually expect the API URL for the live database to be <a href="https://api.openstreetmap.org/api/0.6/">https://api.openstreetmap.org/api/0.6/</a> .</p>
</div>
<div id="comment-86216-info" class="comment-info">
<span class="comment-age">(24 Nov '22, 13:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86191-form-container" class="comment-form-container">
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

<span id="86195"></span>

<div id="answer-container-86195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86195-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-86195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That editor seems to have had <a href="https://wiki.openstreetmap.org/wiki/Editor_usage_stats">about 0.01%</a> of the edits last year, so expertise might be a bit light on the ground.</p>
<p>If you can export in osm format might be easier to use JOSM or something more tailored to OpenStreetMap data? JOSM does have a plugin that lets you open other file formats.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '22, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-86195" class="comments-container">
<span id="86213"></span>
<div id="comment-86213" class="comment">
<div id="post-86213-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In general using essentially unmaintained niche editors (last update in this case three years ago) is not a good idea.</p>
<p>For contributors used to desktop GIS programs JOSM would seem to be the best choice, see <a href="https://josm.openstreetmap.de/">https://josm.openstreetmap.de/</a></p>
</div>
<div id="comment-86213-info" class="comment-info">
<span class="comment-age">(24 Nov '22, 13:14)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="86223"></span>
<div id="comment-86223" class="comment">
<div id="post-86223-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is a forum more geared towards discussions over at community.openstreetmap.org . I think we don't know enough about the arcgis OSM plugin to tell you how to upload from there. Export your changes into something like GeoJSON or shp format and import into JOSM which already handles the interaction with the OSM servers without needing to change any settings.</p>
</div>
<div id="comment-86223-info" class="comment-info">
<span class="comment-age">(25 Nov '22, 09:03)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-86195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86222"></span>

<div id="answer-container-86222" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86222-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>all is fine, but I need some further information on how upload my edits done in ArcgIS into OSm. JOSM looks morelees good but, how e.g to add openCycle wmts?</p>
<p>I see that forum removed my email. We cannot send PM messsages. Internet is changing for the worst. In past there was better comunication on that kind of forums.</p>
<p>Now I can only post messeages and thats all.</p>
<p>It is only few people who like spend days for searching to find solutions they looking for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '22, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/200e6f6af816facec6260816c8749707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grzes978&#39;s gravatar image" />
<p><span>Grzes978</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grzes978 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '22, 07:49</strong> </span></p>
</div>
</div>
<div id="comments-container-86222" class="comments-container">
&#10;</div>
<div id="comment-tools-86222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86222-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86229"></span>

<div id="answer-container-86229" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86229-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I try to get familiar with JOSM. I see that it is the easiest solution for editing OSM map. I have to struggle and learn how to use this tool.</p>
<p>Thanks for all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '22, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/200e6f6af816facec6260816c8749707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grzes978&#39;s gravatar image" />
<p><span>Grzes978</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grzes978 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86229" class="comments-container">
&#10;</div>
<div id="comment-tools-86229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86229-form-container" class="comment-form-container">
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

