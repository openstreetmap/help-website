+++
type = "question"
title = "Implementing API Key based access control for mod-tiles"
description = '''Hi, I have setup OSM server using mod-tiles and renderd. I want to implement key based access control to map tiles, something similar to Google map key. How can I do this?'''
date = "2017-01-21T09:02:00Z"
lastmod = "2018-07-10T12:31:00Z"
weight = 54221
keywords = [ "map", "mapkey" ]
aliases = [ "/questions/54221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Implementing API Key based access control for mod-tiles](/questions/54221/implementing-api-key-based-access-control-for-mod-tiles)

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
<span id="post-54221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54221-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have setup OSM server using mod-tiles and renderd. I want to implement key based access control to map tiles, something similar to Google map key. How can I do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-mapkey" rel="tag" title="see questions tagged &#39;mapkey&#39;">mapkey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '17, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54221" class="comments-container">
<span id="64641"></span>
<div id="comment-64641" class="comment">
<div id="post-64641-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi</p>
<p>I need some more help in this, if somebody can guide me what exactly do I need to do if I want to implementing API Key based access control for mod-tiles.</p>
<p>my tileserver_site.conf file contains following lines which are commented.</p>
<h1 id="addtileconfig-folder-tilesetname">AddTileConfig /folder/ TileSetName</h1>
<p>How do I create APIs and use them for allowing map access?</p>
</div>
<div id="comment-64641-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 12:31)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-54221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54221-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="54232"></span>

<div id="answer-container-54232" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54232-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many possible ways to do that. You could certainly add key handling directly to mod_tile if some C programming isn't too big a hurdle. Another option (but one that requires a config file reload on Apache every time the list changes) is to do this via Apache, either by creating one "AddTileConfig" directive per API key or by using somethig like mod_perl to generate these AddTileConfig rules programmatically, reading the keys from a file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '17, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '17, 17:38</strong> </span></p>
</div>
</div>
<div id="comments-container-54232" class="comments-container">
<span id="55394"></span>
<div id="comment-55394" class="comment">
<div id="post-55394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you provide an example of 'creating one "AddTileConfig" directive per API key'?</p>
</div>
<div id="comment-55394-info" class="comment-info">
<span class="comment-age">(31 Mar '17, 17:06)</span> <span class="comment-user userinfo">rgwozdz</span>
</div>
</div>
<span id="55395"></span>
<div id="comment-55395" class="comment">
<div id="post-55395-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure: Instead of</p>
<pre><code>AddTileConfig /tile mycoolmapstyle</code></pre>
<p>which will lead Apache to map <a href="http://somehost/tile/z/x/y.png">http://somehost/tile/z/x/y.png</a> to tiles of your "mycoolmapstyle" type, you would</p>
<pre><code>AddTileConfig /apikey1 mycoolmapstyle
AddTileConfig /apikey2 mycoolmapstyle
AddTileConfig /apikey3 mycoolmapstyle</code></pre>
<p>and so on. These API keys, if long enough, cannot be guessed so they are "secret". Instead of the above, it is also possible to use mod_perl to read the API keys from a file and then generate the AddTileConfig directives.</p>
</div>
<div id="comment-55395-info" class="comment-info">
<span class="comment-age">(31 Mar '17, 17:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="55397"></span>
<div id="comment-55397" class="comment">
<div id="post-55397-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks very much, that really helps.</p>
</div>
<div id="comment-55397-info" class="comment-info">
<span class="comment-age">(31 Mar '17, 18:24)</span> <span class="comment-user userinfo">rgwozdz</span>
</div>
</div>
<span id="57243"></span>
<div id="comment-57243" class="comment">
<div id="post-57243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>If I add an apikey in tileserver_site.conf as given above, then what changes do I need to make in my OpenLayer code to access the map?</p>
</div>
<div id="comment-57243-info" class="comment-info">
<span class="comment-age">(24 Jul '17, 10:25)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="57246"></span>
<div id="comment-57246" class="comment">
<div id="post-57246-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When creating the tile layer in OpenLayers you can specify the URL to use. In your case the URL would have to look like <a href="http://myserver/apikey1/$%7Bz%7D/$%7Bx%7D/$%7By%7D.png.">http://myserver/apikey1/${z}/${x}/${y}.png.</a></p>
</div>
<div id="comment-57246-info" class="comment-info">
<span class="comment-age">(24 Jul '17, 13:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54232-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63411"></span>

<div id="answer-container-63411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63411-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I dont understand how it works. Please, explain me. What means "mycoolmapstyle" in the example? I f i create a "/apikey1" i dont need create a symbolic link to /var/lib/mod_tile? Do you have an example of mod_perl and where i save this files?</p>
<p>Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '18, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0a0f43fef041f8cc0f0e3846fab3ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flaviomx14&#39;s gravatar image" />
<p><span>Flaviomx14</span><br />
<span class="score" title="24 reputation points">24</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flaviomx14 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '18, 23:38</strong> </span></p>
</div>
</div>
<div id="comments-container-63411" class="comments-container">
&#10;</div>
<div id="comment-tools-63411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63411-form-container" class="comment-form-container">
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

