+++
type = "question"
title = "Download tile for my apps usage"
description = '''Hello, I am a student working on a non-commercial project.  For some next test I would need to download tiles from OSM. I have read the Tile usage policy, and I know that bulk download without consulting is discouraged.  So I&#x27;d like to ask if downloading about 2000 tiles at 2tiles/s acceptable? I ha...'''
date = "2013-11-28T16:23:00Z"
lastmod = "2013-11-28T17:41:00Z"
weight = 28585
keywords = [ "download", "tiles", "tileserver" ]
aliases = [ "/questions/28585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download tile for my apps usage](/questions/28585/download-tile-for-my-apps-usage)

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
<span id="post-28585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28585-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am a student working on a non-commercial project.</p>
<p>For some next test I would need to download tiles from OSM. I have read the Tile usage policy, and I know that bulk download without consulting is discouraged.</p>
<p>So I'd like to ask if downloading about 2000 tiles at 2tiles/s acceptable? I have tested my apps with 20-30 tiles and it worked(sorry I didnt ask).</p>
<p>If possible, I'd love to know the limit for tile usage :), the tiles would probably be hosted by my own later on if the project is deployed.</p>
<p>I have also looked at other alternatives like University Heidelberg or Cloudmade but the quality of OSM is better for my purpose. So please help me clear my doubt.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '13, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/6730e651ecd1b7ed4d168c2610096624?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saurus55&#39;s gravatar image" />
<p><span>saurus55</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saurus55 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28585" class="comments-container">
&#10;</div>
<div id="comment-tools-28585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28585-form-container" class="comment-form-container">
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

<span id="28588"></span>

<div id="answer-container-28588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28588-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi saurus, thank you for choosing OSM for your project :)</p>
<p>The tile usage policiy explais in details the <strong>technical requirements</strong> on an application to perform an download:<br />
<a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy#Technical_Usage_Requirements">http://wiki.openstreetmap.org/wiki/Tile_usage_policy#Technical_Usage_Requirements</a><br />
If your application fullfills all of that, everything is fine. If you are unsure, you can also use existing applications that grab the images and store it in a local folder:<br />
<a href="http://wiki.openstreetmap.org/wiki/Category:Tile_downloading">http://wiki.openstreetmap.org/wiki/Category:Tile_downloading</a></p>
<p>AFAIK the policy tries to avoid to give <strong>accurate number</strong>, because in the end devs will find ways to surround this anyway (e.g. using different agent strings, use proxies, ...). If you have enough time, just setup your box to download the tiles as slow as possible during the night ;)</p>
<p>If you need a lot of tiles, you can also use other (mostly free) <strong>tile providers</strong>:<br />
<a href="http://wiki.openstreetmap.org/wiki/TMS">http://wiki.openstreetmap.org/wiki/TMS</a><br />
(But also they have a policy and might choose a different license on the map images itself)<br />
Another way would be to setup your own map server (see switch2osm.org) or use a local renderer as <a href="http://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> or <a href="http://wiki.openstreetmap.org/wiki/TileMill">TileMill</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '13, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '13, 17:42</strong> </span></p>
</div>
</div>
<div id="comments-container-28588" class="comments-container">
&#10;</div>
<div id="comment-tools-28588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28588-form-container" class="comment-form-container">
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

