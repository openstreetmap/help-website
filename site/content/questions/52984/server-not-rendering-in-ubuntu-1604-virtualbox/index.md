+++
type = "question"
title = "Server not rendering in Ubuntu 16.04 - VirtualBox"
description = '''Hello, I use the umap-package as frontend to work with my tileserver. Backend is mod_tile / renderd. (All up setted after the tutroials). I disabled the firewall. In Firefox in the VirtualBox all is working fine. When I go to the website from my windows host (bridged network) the website is working,...'''
date = "2016-11-16T21:31:00Z"
lastmod = "2016-11-16T22:04:00Z"
weight = 52984
keywords = [ "umap", "renderd", "mod_tile", "ubuntu" ]
aliases = [ "/questions/52984" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server not rendering in Ubuntu 16.04 - VirtualBox](/questions/52984/server-not-rendering-in-ubuntu-1604-virtualbox)

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
<span id="post-52984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52984-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I use the umap-package as frontend to work with my tileserver. Backend is mod_tile / renderd. (All up setted after the tutroials). I disabled the firewall.</p>
<p>In Firefox in the VirtualBox all is working fine. When I go to the website from my windows host (bridged network) the website is working, but not the map part. The menus and start site are visible and all is fine. The part where normaly the map is shown, is empty.</p>
<p>Why does it work in the VirtualBox and outside not, while the firewall is disabled? I need to change to something in the server config?</p>
<p>thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '16, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad332fb85ece95d8d53ae63eea5d534f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hevilp&#39;s gravatar image" />
<p><span>hevilp</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hevilp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52984" class="comments-container">
<span id="52987"></span>
<div id="comment-52987" class="comment">
<div id="post-52987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The connection is incoming, but not send to the renderer seems like..</p>
<p>192.168.178.74 - - [16/Nov/2016:23:03:16 +0100] "GET /static/storage/src/locale/en.js HTTP/1.1" 200 19957 "http://192.168.178.77:9000/en/map/new/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"</p>
</div>
<div id="comment-52987-info" class="comment-info">
<span class="comment-age">(16 Nov '16, 22:04)</span> <span class="comment-user userinfo">hevilp</span>
</div>
</div>
</div>
<div id="comment-tools-52984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52984-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

