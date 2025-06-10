+++
type = "question"
title = "Generate a WMS URL on AWS EC2 URL"
description = '''I have built my tile server on AWS EC2 instance(using this as reference) and want to use this map on AWS EC2 instance as a base map in QGIS(click &#x27;layer&#x27; &amp;gt; &#x27;add layer&#x27; &amp;gt; &#x27;Add WMS/WMTS layer&#x27; to add map). When I try to add my EC2 instance url as a WMS URL on QGIS, I get an error saying  The ser...'''
date = "2019-03-15T20:30:00Z"
lastmod = "2019-03-20T08:00:00Z"
weight = 68397
keywords = [ "qgis", "wms", "aws", "basemap", "tileserver" ]
aliases = [ "/questions/68397" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Generate a WMS URL on AWS EC2 URL](/questions/68397/generate-a-wms-url-on-aws-ec2-url)

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
<span id="post-68397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68397-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have built my tile server on AWS EC2 instance(using <a href="https://github.com/s6o/aws-osm-rds">this</a> as reference) and want to use this map on AWS EC2 instance as a base map in QGIS(click 'layer' &gt; 'add layer' &gt; 'Add WMS/WMTS layer' to add map). When I try to add my EC2 instance url as a WMS URL on QGIS, I get an error saying</p>
<p><code>The server you are trying to connect to does not seem to be a WMS server. Please check the URL.</code></p>
<p>Do I need to convert my AWS url to a WMS URL? Are there any tutorial on how to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-basemap" rel="tag" title="see questions tagged &#39;basemap&#39;">basemap</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '19, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/153d30d9d12370c8532371eaaa3593b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishy91&#39;s gravatar image" />
<p><span>vishy91</span><br />
<span class="score" title="66 reputation points">66</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishy91 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68397" class="comments-container">
<span id="68407"></span>
<div id="comment-68407" class="comment">
<div id="post-68407-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds like you did set up a TMS, not a WMS. So try using it as a TMS instead.</p>
</div>
<div id="comment-68407-info" class="comment-info">
<span class="comment-age">(18 Mar '19, 15:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68408"></span>
<div id="comment-68408" class="comment">
<div id="post-68408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@Scai</a> yes. but I'm not able to add the TMS url to QGIS</p>
</div>
<div id="comment-68408-info" class="comment-info">
<span class="comment-age">(18 Mar '19, 15:46)</span> <span class="comment-user userinfo">vishy91</span>
</div>
</div>
<span id="68409"></span>
<div id="comment-68409" class="comment">
<div id="post-68409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does the URL work in your browser?</p>
</div>
<div id="comment-68409-info" class="comment-info">
<span class="comment-age">(18 Mar '19, 15:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68410"></span>
<div id="comment-68410" class="comment">
<div id="post-68410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@Scai</a> - yes. the URL works in my browser and I can see the map with zoom levels from 0-18. I have this configured using Leaflet for front end.</p>
</div>
<div id="comment-68410-info" class="comment-info">
<span class="comment-age">(18 Mar '19, 16:01)</span> <span class="comment-user userinfo">vishy91</span>
</div>
</div>
</div>
<div id="comment-tools-68397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68397-form-container" class="comment-form-container">
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

<span id="68441"></span>

<div id="answer-container-68441" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68441-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>WMS and WTMS servers are far more complicated services than a regular google/OSM format tile server.</p>
<p>To add a "normal" tileserver one to QGis see the article here <a href="https://www.spatialbias.com/2018/02/qgis-3.0-xyz-tile-layers/">https://www.spatialbias.com/2018/02/qgis-3.0-xyz-tile-layers/</a> (for whatever reason the settings for this are rather well hidden).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '19, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-68441" class="comments-container">
&#10;</div>
<div id="comment-tools-68441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68441-form-container" class="comment-form-container">
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

