+++
type = "question"
title = "Scanned topo layer becomes invisible at high zoom levels in JOSM"
description = '''OSM makes available scanned topographic maps in a special layer for the United States and I use them constantly. They are invaluable for my mapping in Alaska. However, when I try to zoom in to better see details, the image disappears. Every once in a while, just after I zoom in, I can see those deta...'''
date = "2014-03-12T13:16:00Z"
lastmod = "2014-03-13T08:27:00Z"
weight = 31480
keywords = [ "zoomlevel", "josm", "imagery" ]
aliases = [ "/questions/31480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Scanned topo layer becomes invisible at high zoom levels in JOSM](/questions/31480/scanned-topo-layer-becomes-invisible-at-high-zoom-levels-in-josm)

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
<span id="post-31480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31480-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OSM makes available scanned topographic maps in a special layer for the United States and I use them constantly. They are invaluable for my mapping in Alaska. However, when I try to zoom in to better see details, the image disappears. Every once in a while, just after I zoom in, I can see those details so I assume they are capable of being seen for more than a couple of seconds. But, alas, they eventually disappear until I zoom way out again.</p>
<p>I'm using the latest release of JOSM but this behavior has been bugging me for months. Any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '14, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-31480" class="comments-container">
<span id="31483"></span>
<div id="comment-31483" class="comment">
<div id="post-31483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how do you retrieve these maps ? locally or from a WMS ? I'm asking because I think it's possible to configure the max zoom for WMS; check the preference window for WMS settings - if I remember correctly)</p>
</div>
<div id="comment-31483-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 13:35)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="31486"></span>
<div id="comment-31486" class="comment">
<div id="post-31486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They are available from the Imagery menu in JOSM. I selected the ones I wanted and use most often from the TMS/WMS Imagery Providers menu. This one is the "USGS Scanned Topographic Maps" layer (which is a TMS layer). The Settings tab on that menu default is for TMS Settings for zoom of min=2, max=18 but changing those settings didn't have any effect that I could see.</p>
<p>I did discover another set of topo maps while I was in there mucking about, the "MSR Maps Topo", that will zoom closer before disappearing. I hadn't seen those before.</p>
</div>
<div id="comment-31486-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 14:49)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="31488"></span>
<div id="comment-31488" class="comment">
<div id="post-31488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>other ideas : try to change the order of displayed layers (right pane); or mouse right click in the edit panel, you see a pop-up menu with some options about cleaning the cache or changing the zoom level.</p>
</div>
<div id="comment-31488-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 15:25)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-31480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31480-form-container" class="comment-form-container">
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

<span id="31493"></span>

<div id="answer-container-31493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31493-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I asked a similar question, the answers i got may help <a href="https://help.openstreetmap.org/questions/12256/why-does-background-imagery-such-as-bing-only-display-up-to-a-certain-zoom-level-in-potlatch2">https://help.openstreetmap.org/questions/12256/why-does-background-imagery-such-as-bing-only-display-up-to-a-certain-zoom-level-in-potlatch2</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '14, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-31493" class="comments-container">
<span id="31521"></span>
<div id="comment-31521" class="comment">
<div id="post-31521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Andy</span> - it sort of helps but I don't think this is really the same problem. I don't get a message about "no imagery at this zoom level" - the imagery simply clears leaving only the OSM data remaining. Pieren suggests rearranging the layers - I've tried that and it didn't help. And I've been unable to find an explanation of what exactly the Zoom Settings for WMS and TMS are supposed to do. At any rate, changing those settings has not had any effect on this issue either.</p>
</div>
<div id="comment-31521-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 08:27)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="31522"></span>
<div id="comment-31522" class="comment">
<div id="post-31522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've been using the MSR Topo layer since we began this discussion and it is a big improvement because, for some reason, I <em>can</em> zoom in close enough to locate things and accurately position the layer with reference to GPS traces.</p>
<p>I reckon I'm good for now — thanks for your help.</p>
</div>
<div id="comment-31522-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 08:27)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-31493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31493-form-container" class="comment-form-container">
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

