+++
type = "question"
title = "[closed] finding javascript api for loading maps (marks,layers etc..) that works offline"
description = '''hello, i got some issue with finding javascript api for loading maps(marks,layers etc..) that works offline. Therefore i decided to looking for another way to do it. and here comes you help , i need you to help me understands how can i gather maps(somehow). than using a generic js api , that uses on...'''
date = "2015-10-16T22:35:00Z"
lastmod = "2015-10-19T19:08:00Z"
weight = 45962
keywords = [ "api", "javascript", "offlinemaps" ]
aliases = [ "/questions/45962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] finding javascript api for loading maps (marks,layers etc..) that works offline](/questions/45962/finding-javascript-api-for-loading-maps-markslayers-etc-that-works-offline)

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
<span id="post-45962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello,</p>
<p>i got some issue with finding javascript api for loading maps(marks,layers etc..) that works offline. Therefore i decided to looking for another way to do it. and here comes you help , i need you to help me understands how can i gather maps(somehow). than using a generic js api , that uses online maps but instead of using the online maps , ill use my own maps that i gathered.</p>
<p>i hope you can help me figure it out.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '15, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6b66d6d6b94b411a9d897ff1887c43e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elad159&#39;s gravatar image" />
<p><span>elad159</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elad159 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Oct '15, 22:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-45962" class="comments-container">
<span id="45964"></span>
<div id="comment-45964" class="comment">
<div id="post-45964-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Both Leaflet and OpenLayers can perfectly work offline. Can you explain your problems in more detail? And what are you actually planning to do?</p>
</div>
<div id="comment-45964-info" class="comment-info">
<span class="comment-age">(17 Oct '15, 08:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45969"></span>
<div id="comment-45969" class="comment">
<div id="post-45969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well ill try to explain it better,</p>
<p>my big problem is that i need to work offline, it mean no internet connection is on. most of the libraries works online.</p>
<p>i was thinking about some ways to go through this problem. maybe by using an online api, but instead of using the online maps, ill try to find a way to download the maps, and then use them offline.</p>
<p>and that why i need your help , to help me understand how can i do it properly..</p>
</div>
<div id="comment-45969-info" class="comment-info">
<span class="comment-age">(17 Oct '15, 13:45)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="45971"></span>
<div id="comment-45971" class="comment">
<div id="post-45971-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>With regard to tile-based maps, like <a href="http://help.openstreetmap.org/users/158/scai">@scai</a> said the commonly-used libraries can work offline. I did a quick-and-dirty example a couple of years ago over at <a href="https://github.com/SomeoneElseOSM/OSMembedded">https://github.com/SomeoneElseOSM/OSMembedded</a> . I'm not sure why you need to "gather" maps - just download the data and create your own. See <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> for more details about that.</p>
<p>Other non-tile-based options include the vector-based OsmAnd maps (download the code and have a look at what it does if you're interested in that). Maps.me (a version of which has been recently open-sourced) also used vector-based maps.</p>
<p>Also see <a href="https://github.com/mapbox/mapbox-gl-cocoa/issues/62">https://github.com/mapbox/mapbox-gl-cocoa/issues/62</a> for a discussion of Mapbox vector tiles offline.</p>
</div>
<div id="comment-45971-info" class="comment-info">
<span class="comment-age">(17 Oct '15, 20:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45976"></span>
<div id="comment-45976" class="comment">
<div id="post-45976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well about the gathering, i wanna download a free maps , and not making one by my self. there is a free map providers? with a good tiles in it , like google map ?</p>
</div>
<div id="comment-45976-info" class="comment-info">
<span class="comment-age">(18 Oct '15, 15:04)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="45981"></span>
<div id="comment-45981" class="comment">
<div id="post-45981-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Currently there are no pre-rendered tiles available for downloading (at least not that I know of) so you have to render them yourself, that's what SomeoneElse was talking about. I think you should start over again and clearly list your requirements and the things you are planning to do. Currently this is all very vague, making it difficult to help you.</p>
</div>
<div id="comment-45981-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 08:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45996"></span>
<div id="comment-45996" class="comment not_top_scorer">
<div id="post-45996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>okay about the offline library i think i will use leaflet very easy api + working very well.</p>
<p>so my new list is:</p>
<p>1)i need pre-rendered tiles available(offline) - maybe pre downloading somehow.</p>
<p>2)if it impossible i need to know how can i render it by my self.</p>
</div>
<div id="comment-45996-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 18:36)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="45997"></span>
<div id="comment-45997" class="comment not_top_scorer">
<div id="post-45997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11589/elad159">@elad159</a>: just search this help page for your new questions. I am sure you will find old questions (and answers) about this. If you cannot find, then ask new questions please. This makes this help site most efficient for everybody.</p>
</div>
<div id="comment-45997-info" class="comment-info">
<span class="comment-age">(19 Oct '15, 19:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45962" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45962-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This question is really "where can I download pre-rendered tiles for free" and as such has been discussed here a lot already." by Frederik Ramm 19 Oct '15, 22:30

</div>

</div>

</div>

