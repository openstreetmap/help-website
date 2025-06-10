+++
type = "question"
title = "manually-building-a-tile-server-18-04-lts pb with mapnik version"
description = '''Hi community, This is the first time i registered to your forum. I made an installation on Ubuntu 18.04 and followed precisely what is explained in the document : https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ Everything ok until the end of the tuto : renderd -f -c /...'''
date = "2020-11-27T18:07:00Z"
lastmod = "2020-12-05T12:25:00Z"
weight = 77747
keywords = [ "installation", "server" ]
aliases = [ "/questions/77747" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [manually-building-a-tile-server-18-04-lts pb with mapnik version](/questions/77747/manually-building-a-tile-server-18-04-lts-pb-with-mapnik-version)

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
<span id="post-77747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77747-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi community, This is the first time i registered to your forum. I made an installation on Ubuntu 18.04 and followed precisely what is explained in the document : <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a> Everything ok until the end of the tuto : renderd -f -c /usr/local/etc/renderd.conf As a result, rendering stop displaying : Renderd is using mapnik version 4.0.0 then it stops: core dumped</p>
<p>I can not understand why it speak about mapnik 4.0.0 as i did installed mapnik version 3 i thought ? Is it the reason of crash ? Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '20, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/4218ca75b5cd7fa55cdb948389e52004?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pascal&#39;s gravatar image" />
<p><span>pascal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pascal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77747" class="comments-container">
<span id="77777"></span>
<div id="comment-77777" class="comment">
<div id="post-77777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "apt list --installed | grep -i mapnik" say?</p>
<p>What does "lsb_release -a" say?</p>
</div>
<div id="comment-77777-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 11:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77828"></span>
<div id="comment-77828" class="comment">
<div id="post-77828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi community, Excuse me for my late return but i did not have access to my computer. Here is the response:</p>
<ol>
<li>apt list --installed | grep -i mapnik WARNING: apt does not have a stable CLI interface. Use with caution in scripts. libmapnik3.0/bionic,now 3.0.19+ds-1 amd64 [installé, automatique] mapnik-doc/bionic,bionic,now 3.0.19+ds-1 all [installé, pouvant être supprimé automatiquement] mapnik-utils/bionic,now 3.0.19+ds-1 amd64 [installé] python-mapnik/bionic,now 1:0.0~20180130-804a7947d-1 amd64 [installé]</li>
<li>lsb_release -a No LSB modules are available. Distributor ID: Ubuntu Description: Ubuntu 18.04.5 LTS Release: 18.04 Codename: bionic</li>
</ol>
</div>
<div id="comment-77828-info" class="comment-info">
<span class="comment-age">(02 Dec '20, 07:43)</span> <span class="comment-user userinfo">pascal</span>
</div>
</div>
<span id="77854"></span>
<div id="comment-77854" class="comment">
<div id="post-77854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So where did "mapnik 4.0.0" come from?</p>
</div>
<div id="comment-77854-info" class="comment-info">
<span class="comment-age">(05 Dec '20, 12:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77747-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

