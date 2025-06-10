+++
type = "question"
title = "Can JOSM WMTS Support accept file:// instead of http:// for the XML Capabilities file url?"
description = '''I need to use a local capabilities file for a WMTS service. Typically that entry in JOSM Imagery Prefs would look like this: wmts:http://www.something.com/arcgis/rest/services/WGS84_jpg/MapServer/WMTS/1.0.0/WMTSCapabilities.xml But I want to use a value of like: wmts:file://WMTSCapabilities.xml Coul...'''
date = "2015-10-20T05:12:00Z"
lastmod = "2015-10-22T19:23:00Z"
weight = 46009
keywords = [ "josm", "wmts" ]
aliases = [ "/questions/46009" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can JOSM WMTS Support accept file:// instead of http:// for the XML Capabilities file url?](/questions/46009/can-josm-wmts-support-accept-file-instead-of-http-for-the-xml-capabilities-file-url)

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
<span id="post-46009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to use a local capabilities file for a WMTS service.</p>
<p>Typically that entry in JOSM Imagery Prefs would look like this:</p>
<p>wmts:<a href="http://www.something.com/arcgis/rest/services/WGS84_jpg/MapServer/WMTS/1.0.0/WMTSCapabilities.xml">http://www.something.com/arcgis/rest/services/WGS84_jpg/MapServer/WMTS/1.0.0/WMTSCapabilities.xml</a></p>
<p>But I want to use a value of like:</p>
<p>wmts:<span>file://WMTSCapabilities.xml</span></p>
<p>Could anyone help me if they think that is possible? And if so what the syntax would be?</p>
<p>I am on windows so of course there is always the path issue</p>
<p>I just want my d:\WMTSCapabilities.xml to get used instead of the one pulled from the server.</p>
<p>Cheers, Blake</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-wmts" rel="tag" title="see questions tagged &#39;wmts&#39;">wmts</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '15, 05:12</strong></p>
<img src="https://secure.gravatar.com/avatar/297418cf750e0c88035cf26cb430111a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BlakeGirardot&#39;s gravatar image" />
<p><span>BlakeGirardot</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BlakeGirardot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46009" class="comments-container">
&#10;</div>
<div id="comment-tools-46009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46009-form-container" class="comment-form-container">
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

<span id="46057"></span>

<div id="answer-container-46057" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46057-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BlakeGirardot has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These WMTS xml files usually only list a number of URLs that you can use to access the tiles. If you open the XML in a text editor, you will see the different URLs, and you can probably select the format you need (we use the same format as Google maps).</p>
<p>So while it is handy to read the WMTS file directly, it's not strictly necessary. Other workarounds include uploading the file to a server, or launching your own web server (which isn't that hard when it just has to serve a file).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '15, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-46057" class="comments-container">
<span id="46060"></span>
<div id="comment-46060" class="comment">
<div id="post-46060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Sanderd17 - I tried the direct url to the tiles, but I kept the WMTS: prefix and JOSM returned an error like it was expecting a capabilities.xml file, not a tile url. I wonder if changing the protocol prefix to use the tiles url in the capabilities document would work then. Anyone know if the tiles server url itself is something like TMS or WMS ?</p>
<p>Otherwise it looks like I will have to serve them up from a web server some place. I have to customize them by user so it would have been a lot easier to just send them their own capabilities.xml and say drop it in your josm folder and use this URI for the preferences.</p>
<p>Thank you for the help!</p>
</div>
<div id="comment-46060-info" class="comment-info">
<span class="comment-age">(22 Oct '15, 17:34)</span> <span class="comment-user userinfo">BlakeGirardot</span>
</div>
</div>
<span id="46061"></span>
<div id="comment-46061" class="comment">
<div id="post-46061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The WMTS should tell you what format it is (WMS or TMS), WMTS is a combination format, that allows tools to chose whether they want WMS or TMS (in case the quality is the same, always go for TMS, it's a lot faster).</p>
<p>And if the actual tiles are also on your computer (instead of on a web server), you'll probably also have to use a server to serve those tiles.</p>
<p>Maybe you could share the actual WMTS file to see what it contains?</p>
</div>
<div id="comment-46061-info" class="comment-info">
<span class="comment-age">(22 Oct '15, 19:23)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-46057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46057-form-container" class="comment-form-container">
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

