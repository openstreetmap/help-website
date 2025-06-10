+++
type = "question"
title = "tiles server last step problem"
description = '''im using this guide for building tile server https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/. using ubuntu server, and i got to the last step : sudo mkdir /var/run/renderd sudo chown username /var/run/renderd sudo -u username renderd -f -c /usr/local/etc/renderd.conf  in ...'''
date = "2015-10-25T20:58:00Z"
lastmod = "2015-11-04T06:15:00Z"
weight = 46113
keywords = [ "tiles", "switch2osm", "problem", "server" ]
aliases = [ "/questions/46113" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tiles server last step problem](/questions/46113/tiles-server-last-step-problem)

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
<span id="post-46113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>im using this guide for building tile server <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/.">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/.</a></p>
<p>using ubuntu server, and i got to the last step :</p>
<pre><code>sudo mkdir /var/run/renderd
sudo chown username /var/run/renderd
sudo -u username renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>in the last command i got this failure :</p>
<pre><code>renderd[1549]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: Bad connection
Connection string : &#39; db=gis connect_timeout=4&#39;
   encountered during parsing of later &#39;landuse_gen0&#39; in Layer at line 193 of &#39;/usr/local/share/maps/style/OSMBright/OSMBright.xml&#39;</code></pre>
<p>what could have been the problem ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '15, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/6b66d6d6b94b411a9d897ff1887c43e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elad159&#39;s gravatar image" />
<p><span>elad159</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elad159 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '15, 21:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46113" class="comments-container">
<span id="46372"></span>
<div id="comment-46372" class="comment">
<div id="post-46372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi I have the same error, did you fix that?</p>
</div>
<div id="comment-46372-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 06:15)</span> <span class="comment-user userinfo">Zhands</span>
</div>
</div>
</div>
<div id="comment-tools-46113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46113-form-container" class="comment-form-container">
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

<span id="46118"></span>

<div id="answer-container-46118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Make sure that the username you are running tirex under ("username" in your example) is the same you created in your PostGIS database as the owner of the OSM database. If you haven't done that then you could perhaps fix it by creating an user named "username" in PostGIS ("createuser -s username").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '15, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46118" class="comments-container">
<span id="46124"></span>
<div id="comment-46124" class="comment">
<div id="post-46124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i created a user , and then i really have got another results.. its all go fine and it stuck at this point:</p>
<pre><code>renderd[5770]: Loading parameterization function for
renderd[5770]: Loading parameterization function for
renderd[5770]: Starting stats thread
renderd[5770]: Using web mercator projection settings
renderd[5770]: Using web mercator projection settings
renderd[5770]: Using web mercator projection settings
renderd[5770]: Using web mercator projection settings</code></pre>
<p>and it stucks there..</p>
<p>does it ok? by the way another question how am i define a ip server or checking my current using ubuntu server? i tried to use the ipconfig command but it appears to doesnt work..</p>
</div>
<div id="comment-46124-info" class="comment-info">
<span class="comment-age">(25 Oct '15, 22:00)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="46139"></span>
<div id="comment-46139" class="comment">
<div id="post-46139-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well i check the mod_tile and i got this reults</p>
<pre><code>NoResp200: 0
NoResp304: 0
NoResp404: 6
NoResp503: 0
NoResp5XX: 0
NoRespOther: 0
NoFreshCache: 0
NoOldCache: 0
NoVeryOldCache: 0
NoFreshRender: 0
NoOldRender: 0
NoVeryOldRender: 0
NoRespZoom00: 0</code></pre>
<p>(up to)</p>
<pre><code>NoRespZoom20: 0</code></pre>
</div>
<div id="comment-46139-info" class="comment-info">
<span class="comment-age">(27 Oct '15, 01:37)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
</div>
<div id="comment-tools-46118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46118-form-container" class="comment-form-container">
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

