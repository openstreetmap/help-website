+++
type = "question"
title = "Using streets for laser work"
description = '''Hi there how could I use the date of the streets, buildings, water, etc. for laserwork? Is there a possibility to get them in layers? In wich program (for example Illustrator) can I work with the data? Thanks for your help!'''
date = "2019-08-01T11:08:00Z"
lastmod = "2019-08-06T19:55:00Z"
weight = 70279
keywords = [ "laser" ]
aliases = [ "/questions/70279" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using streets for laser work](/questions/70279/using-streets-for-laser-work)

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
<span id="post-70279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70279-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there</p>
<p>how could I use the date of the streets, buildings, water, etc. for laserwork?</p>
<p>Is there a possibility to get them in layers?</p>
<p>In wich program (for example Illustrator) can I work with the data?</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-laser" rel="tag" title="see questions tagged &#39;laser&#39;">laser</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '19, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/fd1b102039d9ec87a9bde62c01dbab9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Swiss%20Wood%20Maps&#39;s gravatar image" />
<p><span>Swiss Wood Maps</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Swiss Wood Maps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70279" class="comments-container">
<span id="70332"></span>
<div id="comment-70332" class="comment">
<div id="post-70332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Lukas, just a reminder that if you're producing maps -- digital, paper, or 3D -- using OpenStreetMap data, you need to including attribution in order to comply with the data license. Typically "© OpenStreetMap contributors". See <a href="https://wiki.openstreetmap.org/wiki/Legal_FAQ#3a._I_would_like_to_use_OpenStreetMap_maps._How_should_I_credit_you.3F">https://wiki.openstreetmap.org/wiki/Legal_FAQ#3a._I_would_like_to_use_OpenStreetMap_maps._How_should_I_credit_you.3F</a></p>
</div>
<div id="comment-70332-info" class="comment-info">
<span class="comment-age">(06 Aug '19, 19:55)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-70279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70279-form-container" class="comment-form-container">
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

<span id="70291"></span>

<div id="answer-container-70291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For large areas, download a <a href="https://download.geofabrik.de/">Geofabrik extract</a> for your country / region. Use <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> to further select a smaller rectangle or to select just a few feature types and convert to .OSM format.</p>
<p>Then the <a href="https://trac.openstreetmap.org/browser/applications/utils/export/osm2ai">Perl file osmtoai.pl</a> should convert to Illustrator format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '19, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-70291" class="comments-container">
&#10;</div>
<div id="comment-tools-70291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70291-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70280"></span>

<div id="answer-container-70280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70280-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For small areas - try Export from the OpenStreetMap.org view, select Overpass API using XML format. Then use an <a href="https://mygeodata.cloud/converter/osm-to-pdf">OSM to PDF converter</a> to create a PDF file, that Illustrator should be able to read.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '19, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-70280" class="comments-container">
<span id="70288"></span>
<div id="comment-70288" class="comment">
<div id="post-70288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Mike thanks for you support. Is there any possibility to get larger areas? And is there no free option to convert the data? best Lukas</p>
</div>
<div id="comment-70288-info" class="comment-info">
<span class="comment-age">(02 Aug '19, 07:17)</span> <span class="comment-user userinfo">Swiss Wood Maps</span>
</div>
</div>
</div>
<div id="comment-tools-70280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70280-form-container" class="comment-form-container">
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

