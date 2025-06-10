+++
type = "question"
title = "How do I fetch only nodes of a certain tag?"
description = '''Hello, I would like to download the coordinates of all parks in my region. From what I can tell I need to find all nodes that are tagged with &quot;leisure&quot;-&amp;gt;&quot;park&quot;. The only way I can tell to do this is by using the API to parse through the xml of every single node in my region. For example, I am doi...'''
date = "2011-08-16T05:09:00Z"
lastmod = "2011-08-16T22:42:00Z"
weight = 7105
keywords = [ "tagging" ]
aliases = [ "/questions/7105" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fetch only nodes of a certain tag?](/questions/7105/how-do-i-fetch-only-nodes-of-a-certain-tag)

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
<span id="post-7105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to download the coordinates of all parks in my region. From what I can tell I need to find all nodes that are tagged with "leisure"-&gt;"park".</p>
<p>The only way I can tell to do this is by using the API to parse through the xml of every single node in my region. For example, I am doing the following:</p>
<ol>
<li>I download the data from a url like this : <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-122.1414,37.7206,-122.1365,37.9042">http://api.openstreetmap.org/api/0.6/map?bbox=-122.1414,37.7206,-122.1365,37.9042</a></li>
<li>I parse the XML data and find any node, way, relation with leisure-&gt;park as one of its tags</li>
</ol>
<p>My plan is to do the above over 60,000 times, which is quite resource intensive. Is there a better way to find all nodes of a certain tag in a certain region?<br />
</p>
<p>Thanks, James</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '11, 05:09</strong></p>
<img src="https://secure.gravatar.com/avatar/40c5ce269c924decfaadf96677c5c987?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamesmcb&#39;s gravatar image" />
<p><span>jamesmcb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamesmcb has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-7105" class="comments-container">
<span id="7107"></span>
<div id="comment-7107" class="comment">
<div id="post-7107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I looked into this a little farther and found some documentation on the XAPI to run a command like this:</p>
<p><a href="http://xapi.openstreetmap.org/api/0.6/node%5Blesiure=park%5D%5Bbbox=-122.27323,37.8395,-122.25428,37.85097%5D">http://xapi.openstreetmap.org/api/0.6/node[lesiure=park][bbox=-122.27323,37.8395,-122.25428,37.85097]</a> <a href="http://xapi.openstreetmap.org/api/0.6/way%5Blesiure=park%5D%5Bbbox=-122.27323,37.8395,-122.25428,37.85097%5D">http://xapi.openstreetmap.org/api/0.6/way[lesiure=park][bbox=-122.27323,37.8395,-122.25428,37.85097]</a></p>
<p>But nothing appeared :-(</p>
<p>If you look at this call to the normal api:</p>
<p><a href="http://openstreetmap.org/api/0.6/map?bbox=-122.27323,37.8395,-122.25428,37.85097">http://openstreetmap.org/api/0.6/map?bbox=-122.27323,37.8395,-122.25428,37.85097</a></p>
<p>You will see that there is at least 1 node and 1 way. I am definitely getting closer.</p>
</div>
<div id="comment-7107-info" class="comment-info">
<span class="comment-age">(16 Aug '11, 05:42)</span> <span class="comment-user userinfo">jamesmcb</span>
</div>
</div>
</div>
<div id="comment-tools-7105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7105-form-container" class="comment-form-container">
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

<span id="7123"></span>

<div id="answer-container-7123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7123-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do not want to hammer the API servers you can also download the raw OSM data of your desired area via the sources listed at <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">Planet.osm</a> . I would recommend <a href="http://geofabrik.de">geofabrik.de</a> or <a href="http://cloudmade.com">cloudmade.com</a></p>
<p>Process that data with Osmosis or <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a> which seems to be a bit easier to handle IMHO.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '11, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-7123" class="comments-container">
&#10;</div>
<div id="comment-tools-7123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7108"></span>

<div id="answer-container-7108" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is a call like this:</p>
<p><a href="http://www.overpass-api.de/api/xapi?node%5Bleisure=park%5D%5Bbbox=-123.076,37.059,-121.436,38.529%5D">http://www.overpass-api.de/api/xapi?node[leisure=park][bbox=-123.076,37.059,-121.436,38.529]</a></p>
<p>Unfortunately <a href="http://xapi.openstreetmap.org">xapi.openstreetmap.org</a> is down right now and in my previous queries I was spelling leisure incorrectly.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '11, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/40c5ce269c924decfaadf96677c5c987?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamesmcb&#39;s gravatar image" />
<p><span>jamesmcb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamesmcb has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-7108" class="comments-container">
<span id="7109"></span>
<div id="comment-7109" class="comment">
<div id="post-7109-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is more than one XAPI server, take a look at the <a href="http://wiki.openstreetmap.org/wiki/XAPI#Servers">XAPI wiki page</a>. The XAPI server by mapquest is said to be working well and there is also the JXAPI.</p>
</div>
<div id="comment-7109-info" class="comment-info">
<span class="comment-age">(16 Aug '11, 07:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7108-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7113"></span>

<div id="answer-container-7113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>XAPI request is probably the easiest solution for that but unfortunatelly, XAPI servers are often out-of-service.<br />
Another way is that you download an extract from the whole planet database ([1]) and use the java tool Osmosis ([2]) to limit your search in a bounding box or polygon ([3]) and filter with your specific tag (key/value pair)([4]).</p>
<p>[1] <a href="http://wiki.openstreetmap.org/wiki/Planet#Mirrors">http://wiki.openstreetmap.org/wiki/Planet#Mirrors</a> (in particular, check Geofabrik or Cloudmade producing smaller daily extracts by state, region or country)<br />
[2] <a href="http://wiki.openstreetmap.org/wiki/Osmosis">http://wiki.openstreetmap.org/wiki/Osmosis</a><br />
[3] <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.38#Area_Filtering_Tasks">http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.38#Area_Filtering_Tasks</a><br />
[4] <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.38#--node-key-value_.28--nkv.29">http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.38#--node-key-value_.28--nkv.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '11, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7113" class="comments-container">
<span id="7128"></span>
<div id="comment-7128" class="comment">
<div id="post-7128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mapquest Open also has a XAPI running against OSM data, and it's up reliably, and has a GUI.</p>
</div>
<div id="comment-7128-info" class="comment-info">
<span class="comment-age">(16 Aug '11, 22:42)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-7113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7113-form-container" class="comment-form-container">
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

