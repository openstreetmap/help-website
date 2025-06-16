+++
type = "question"
title = "how to install own tile server/renderer"
description = '''Hello, I would like to download tons of prerendered even high zoom tiles from OSM to be used offline, however this is against the rules. So I&#x27;ve seen somewhere that it is possible to run my own server, so my question is: Is there a step-by-step tutorial how to setup own tile server/renderer (on wind...'''
date = "2011-06-25T17:44:00Z"
lastmod = "2011-06-25T22:22:00Z"
weight = 5986
keywords = [ "tile", "howto", "renderer", "server" ]
aliases = [ "/questions/5986" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to install own tile server/renderer](/questions/5986/how-to-install-own-tile-serverrenderer)

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
<span id="post-5986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to download tons of prerendered even high zoom tiles from OSM to be used offline, however this is against the rules. So I've seen somewhere that it is possible to run my own server, so my question is:</p>
<p>Is there a step-by-step tutorial how to setup own tile server/renderer (on windows server 2003 platform)?</p>
<p>I want to download the raw vector data and render it just like the official servers do so I wouldn't burden those so much.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-howto" rel="tag" title="see questions tagged &#39;howto&#39;">howto</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '11, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/cd0dbfc5917fecfd8a1cdc0182bd203d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MuF&#39;s gravatar image" />
<p><span>MuF</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MuF has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '11, 17:45</strong> </span></p>
</div>
</div>
<div id="comments-container-5986" class="comments-container">
&#10;</div>
<div id="comment-tools-5986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5986-form-container" class="comment-form-container">
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

<span id="5987"></span>

<div id="answer-container-5987" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5987-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MuF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not aware of anyone running a proper tile server (with on-demand rendering) on the Windows platform. The basic rendering engine (Mapnik) is available on Windows however (see <a href="https://wiki.openstreetmap.org/wiki/Mapnik/Installation#For_Microsoft_Windows_.28Windows_2000_and_above.29">Instructions</a> on our Wiki), so you should be able to render tiles using the <a href="http://generate_tiles.py">generate_tiles.py</a> Python script.</p>
<p>Be aware that in addition to installing Mapnik as per the above instructions, you will also need to install a PostGIS database and load data into it, as well as install the map style, icons, and a number of shape files, as per the <a href="https://wiki.openstreetmap.org/wiki/Mapnik">general Mapnik instructions</a> on the Wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '11, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-5987" class="comments-container">
<span id="5988"></span>
<div id="comment-5988" class="comment">
<div id="post-5988-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply, however this seems too complex. Isn't there any step-by-step guide to complete solution of this?</p>
</div>
<div id="comment-5988-info" class="comment-info">
<span class="comment-age">(25 Jun '11, 20:09)</span> <span class="comment-user userinfo">MuF</span>
</div>
</div>
<span id="5990"></span>
<div id="comment-5990" class="comment">
<div id="post-5990-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The most "hands-on" guides available are actually for Linux environments. Very few people in the project use Windows for rendering. It is very likely that if these instructions seem to complex to you, you will encounter lots of hurdles and give up sooner or later! Maybe you could simply rent an Amazon EC2 server and then use a ready-made tile server image like <a href="http://tiledrawer.com/">http://tiledrawer.com/</a> on that?</p>
</div>
<div id="comment-5990-info" class="comment-info">
<span class="comment-age">(25 Jun '11, 22:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5987-form-container" class="comment-form-container">
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

