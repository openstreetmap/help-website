+++
type = "question"
title = "access slippymap.html from a different machine"
description = '''Hi, I have up the tile server and can view Slippymap.html, if run on same machine. When I call this page from some other system, it does not work. Any idea why? I want to run the tile server on a machinde and to be able to view the tiles from another system.'''
date = "2014-06-02T11:32:00Z"
lastmod = "2014-08-14T17:06:00Z"
weight = 33623
keywords = [ "slippymap.html", "from", "different", "system" ]
aliases = [ "/questions/33623" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [access slippymap.html from a different machine](/questions/33623/access-slippymaphtml-from-a-different-machine)

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
<span id="post-33623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33623-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have up the tile server and can view Slippymap.html, if run on same machine. When I call this page from some other system, it does not work. Any idea why?</p>
<p>I want to run the tile server on a machinde and to be able to view the tiles from another system.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slippymap.html" rel="tag" title="see questions tagged &#39;slippymap.html&#39;">slippymap.html</span> <span class="post-tag tag-link-from" rel="tag" title="see questions tagged &#39;from&#39;">from</span> <span class="post-tag tag-link-different" rel="tag" title="see questions tagged &#39;different&#39;">different</span> <span class="post-tag tag-link-system" rel="tag" title="see questions tagged &#39;system&#39;">system</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '14, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33623" class="comments-container">
<span id="33624"></span>
<div id="comment-33624" class="comment">
<div id="post-33624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why don't you also paste in the code you're trying to use?</p>
</div>
<div id="comment-33624-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 11:39)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="33625"></span>
<div id="comment-33625" class="comment">
<div id="post-33625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>map = new OpenLayers.Map ("map" var newLayer = new OpenLayers.Layer.OSM("Local Tiles", "http://192.168.2.35/osm/${z}/${x}/${y}.png", {numZoomLevels: 19}); map.addLayer(newLayer);</p>
</div>
<div id="comment-33625-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 11:46)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="33626"></span>
<div id="comment-33626" class="comment">
<div id="post-33626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this page works fine if I run it on the same server as map tiles server. If I copy this html page to another server and try to run it from there, it does not work</p>
</div>
<div id="comment-33626-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 11:54)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="33634"></span>
<div id="comment-33634" class="comment">
<div id="post-33634-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Blindly guessing that your tile server is configured to allow traffic only from localhost. In case it is running apache, you need to configure it (depending on the installed os the place to start might be: /etc/apache2/sites-enabled/ ).</p>
</div>
<div id="comment-33634-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 20:30)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="35835"></span>
<div id="comment-35835" class="comment">
<div id="post-35835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What OS is this on (and what Apache version)? It doesn't sound like a specific OSM problem.</p>
</div>
<div id="comment-35835-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 17:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33623-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

