+++
type = "question"
title = "OSM tileserver for real"
description = '''Hi all tl;dr please help me spec out a VM for running OSM tile server planet. I have built an OSM tile server on a VM with Ubuntu 12.04. I followed the instructions at switch2osm &quot;Building a tile server from packages&quot;. This was a trial run, and it works fine, but I had some issues. In particular, I ...'''
date = "2015-02-01T08:59:00Z"
lastmod = "2015-02-02T06:59:00Z"
weight = 40736
keywords = [ "hardware", "advice", "switch2osm", "ubuntu", "tileserver" ]
aliases = [ "/questions/40736" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM tileserver for real](/questions/40736/osm-tileserver-for-real)

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
<span id="post-40736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40736-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>tl;dr please help me spec out a VM for running OSM tile server planet.</p>
<p>I have built an OSM tile server on a VM with Ubuntu 12.04. I followed the instructions at switch2osm "Building a tile server from packages". This was a trial run, and it works fine, but I had some issues. In particular, I couldn't get openstreetmap-carto working. It was suggested to me to try using an upgraded version of Mapnik, e.g. the one found in Ubuntu 14.04.</p>
<p>Well, now I have the opportunity to build a tile server "for real" from scratch. I can spec my own VM including which distro to install. I'm thinking of going with Ubuntu 14.04 "Trusty Tar" and following the same instructions as before.</p>
<p>My question is then, what should I ask for in the VM including OS, #cores, RAM, disk, etc. My other question is whether the "Building a tile server from packages" on switch2osm is the best way to do it.</p>
<p>Thanks, Harold Ship</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-advice" rel="tag" title="see questions tagged &#39;advice&#39;">advice</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '15, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/86d98b7622295c7fdc8bdf8f449e4c78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haroldship&#39;s gravatar image" />
<p><span>haroldship</span><br />
<span class="score" title="90 reputation points">90</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haroldship has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40736" class="comments-container">
&#10;</div>
<div id="comment-tools-40736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40736-form-container" class="comment-form-container">
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

<span id="40738"></span>

<div id="answer-container-40738" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40738-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-40738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Disk performance is essential - you should definitely make sure you have about 600 GB of SSD capacity for the database volume, and be sure that you don't ruin SSD performance e.g. by using unsuitable controllers or a bad virtualization layer (apparently you can easily ruin disk performance by checking the wrong boxes or selecting the wrong drivers in some VM environments). In addition to the SSD storage for the database you'll need a bit of standard disk storage for the pre-rendered tiles, just a couple 100 GB. Other than that, Ubuntu 14.04, a modern quad-core CPU, and 32 GB of RAM will serve you well. More cores will increase performance but just a little, and 16 GB of RAM would still work but a bit slower. The switch2osm instructions are good - of course the recommendations given there generic and whether they are "the best way to do it" depends very much on the expected usage profile of your tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '15, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40738" class="comments-container">
<span id="40741"></span>
<div id="comment-40741" class="comment">
<div id="post-40741-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks Frederik. This is what I asked for. Let's hope they give it to me :)</p>
</div>
<div id="comment-40741-info" class="comment-info">
<span class="comment-age">(02 Feb '15, 06:59)</span> <span class="comment-user userinfo">haroldship</span>
</div>
</div>
</div>
<div id="comment-tools-40738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40738-form-container" class="comment-form-container">
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

