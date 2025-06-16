+++
type = "question"
title = "server specs for tile server"
description = '''I&#x27;ve been asked to setup tile server and need to propose a server for the setup.  We are planning to pre render the whole of North America so I guess I&#x27;ll have to setup tirex as well. I have few questions regarding the proposed setup 1) Is 64 GB RAM enough for the GIS database and tirex-batch. The t...'''
date = "2018-06-29T09:53:00Z"
lastmod = "2018-06-29T15:02:00Z"
weight = 64436
keywords = [ "tile", "tiles", "tirex", "gis", "tileserver" ]
aliases = [ "/questions/64436" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [server specs for tile server](/questions/64436/server-specs-for-tile-server)

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
<span id="post-64436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64436-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been asked to setup tile server and need to propose a server for the setup. We are planning to pre render the whole of North America so I guess I'll have to setup tirex as well.</p>
<p>I have few questions regarding the proposed setup</p>
<p>1) Is 64 GB RAM enough for the GIS database and tirex-batch. The tiles and GIS database will be updated on a daily basis. 2) Is 12 CPU cores enough ? 3) I plan to install the GIS postgresql database on SSD drive. Is 1 TB SSD enough for the GIS database ? Will it be sufficient for atleast 5 years ? 4) What types of disk should be used for storing the tiles ? SSD or SAS or SATA ? The pre rendered tiles of North America will be updated on a daily basis.<br />
5) Which file system and RAID level is recommended for tile server ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '18, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-64436" class="comments-container">
<span id="64438"></span>
<div id="comment-64438" class="comment">
<div id="post-64438-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See this question and its answer: <a href="/questions/64405/tile-server-hardware-requirements">https://help.openstreetmap.org/questions/64405/tile-server-hardware-requirements</a></p>
</div>
<div id="comment-64438-info" class="comment-info">
<span class="comment-age">(29 Jun '18, 10:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="64439"></span>
<div id="comment-64439" class="comment">
<div id="post-64439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to pre-render the whole of North America using tirex/tirex-batch. I'll also be updating the pre rendered tiles everyday. Should I use SAS/SSD/SATA for tirex updates ?</p>
</div>
<div id="comment-64439-info" class="comment-info">
<span class="comment-age">(29 Jun '18, 11:04)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
</div>
<div id="comment-tools-64436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64436-form-container" class="comment-form-container">
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

<span id="64444"></span>

<div id="answer-container-64444" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64444-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>64 GB and 1 TB SSD is enough (though I cannot say anything about what happens 5 years from now). Store the tiles on SSD only if you expect very heavy access, otherwise SATA disk is fine. You say you want to re-compute pre-rendered tiles daily, this will likely only work up to z14 or z15, else it will take more than a day to compute them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '18, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64444" class="comments-container">
&#10;</div>
<div id="comment-tools-64444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64444-form-container" class="comment-form-container">
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

