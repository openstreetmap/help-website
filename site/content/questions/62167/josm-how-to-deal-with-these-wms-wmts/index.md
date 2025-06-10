+++
type = "question"
title = "JOSM: how to deal with these WMS, WMTS?"
description = '''https://blog.abysm.org/2016/04/taiwan-gis-resources/ lists URI: http://landmaps.nlsc.gov.tw/S_Maps/wmts URI: http://landmaps.nlsc.gov.tw/S_Maps/wms Referer: http://maps.nlsc.gov.tw/  In JOSM I have tried to enter them in various ways in Imagery Preferences. The best I could ever get was some blank t...'''
date = "2018-02-17T03:00:00Z"
lastmod = "2018-02-18T23:40:00Z"
weight = 62167
keywords = [ "wms", "josm", "wmts" ]
aliases = [ "/questions/62167" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: how to deal with these WMS, WMTS?](/questions/62167/josm-how-to-deal-with-these-wms-wmts)

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
<span id="post-62167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62167-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://blog.abysm.org/2016/04/taiwan-gis-resources/">https://blog.abysm.org/2016/04/taiwan-gis-resources/</a> lists</p>
<pre><code>URI: http://landmaps.nlsc.gov.tw/S_Maps/wmts
URI: http://landmaps.nlsc.gov.tw/S_Maps/wms
Referer: http://maps.nlsc.gov.tw/</code></pre>
<p>In JOSM I have tried to enter them in various ways in Imagery Preferences.</p>
<p>The best I could ever get was some <a href="http://landmaps.nlsc.gov.tw/S_Maps/wmts/DMAPS/default/GoogleMapsCompatible/18/112912/219088">blank tile</a>s.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-wmts" rel="tag" title="see questions tagged &#39;wmts&#39;">wmts</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '18, 03:00</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62167" class="comments-container">
<span id="62171"></span>
<div id="comment-62171" class="comment">
<div id="post-62171-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>legal sidenote: the need for a specific referer suggests that this imaginary is NOT usable by us (in fact it is intended not to be even viewed by everyone). Please do not use it as a source for your contributions. Only use sources where you know the opposite (a explicit <em>positive</em> statement about usability)</p>
</div>
<div id="comment-62171-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 12:30)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62172"></span>
<div id="comment-62172" class="comment">
<div id="post-62172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I want to use those cadastral layers to align an ancient aerial photograph via PicLayer plugin, nothing to do with putting any results into OSM. Just a learning exercise for me. Anyway I found {header} in <a href="https://josm.openstreetmap.de/wiki/Maps#WebMapServicesWMS">https://josm.openstreetmap.de/wiki/Maps#WebMapServicesWMS</a> but still don't know the proper way to feed those two URLs into JOSM.</p>
</div>
<div id="comment-62172-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 12:45)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
<span id="62173"></span>
<div id="comment-62173" class="comment">
<div id="post-62173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try to include this in the URL: <code>{header(Referer,</code><a href="http://maps.nlsc.gov.tw/)%7D"><code>http://maps.nlsc.gov.tw/)}</code></a> (not tried by me). But it seems for WMS you need to specify also the other parameters (width, ...) with placeholders.</p>
</div>
<div id="comment-62173-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 12:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62174"></span>
<div id="comment-62174" class="comment">
<div id="post-62174-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As a sidenote to the legal sidenote - if you believe that these sources should be listed in the imagery available from JOSM and the other OSM editors then please raise that at <a href="https://github.com/osmlab/editor-layer-index">https://github.com/osmlab/editor-layer-index</a> .</p>
</div>
<div id="comment-62174-info" class="comment-info">
<span class="comment-age">(17 Feb '18, 12:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62167-form-container" class="comment-form-container">
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

<span id="62193"></span>

<div id="answer-container-62193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62193-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To give some more background: WMS servers work slightly different than google/OSM style tile servers and provide a proper API to find out what imagery layers with associated properties are available.</p>
<p>Typical integration with OSM editors involves getting the layer url from the WMS server either by using the GetCapabilities call and then extracting the required URL from the response by using the layer name, or by directly configuring that URL with corresponding placeholders.</p>
<p>What don-vip is pointing out is that the WMS server is actually not configured correctly, well at least not responding to the GetCapabilities call properly, which is a non-starter for any use of the server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '18, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62193" class="comments-container">
&#10;</div>
<div id="comment-tools-62193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62193-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62175"></span>

<div id="answer-container-62175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Capabilities are invalid, there is no layer defined. Please contact the servers admins.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '18, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0daf2db5d576b3fcfbb4f3c0e4c54fa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="don-vip&#39;s gravatar image" />
<p><span>don-vip</span><br />
<span class="score" title="300 reputation points">300</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="don-vip has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-62175" class="comments-container">
&#10;</div>
<div id="comment-tools-62175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62175-form-container" class="comment-form-container">
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

