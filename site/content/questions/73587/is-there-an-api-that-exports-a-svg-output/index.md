+++
type = "question"
title = "Is there an API that exports a SVG output?"
description = '''Im aware that using   GET /api/0.6/map?bbox=left,bottom,right,top  Will return a XML or OSM format, but is it possible to reconfigure it to export a raw SVG output, similar to when using the export tab manually to download a SVG file?'''
date = "2020-03-17T20:57:00Z"
lastmod = "2020-03-18T18:40:00Z"
weight = 73587
keywords = [ "download", "svg", "export", "api", "osm" ]
aliases = [ "/questions/73587" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there an API that exports a SVG output?](/questions/73587/is-there-an-api-that-exports-a-svg-output)

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
<span id="post-73587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im aware that using</p>
<blockquote>
<p>GET /api/0.6/map?bbox=left,bottom,right,top</p>
</blockquote>
<p>Will return a XML or OSM format, but is it possible to reconfigure it to export a raw SVG output, similar to when using the export tab manually to download a SVG file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '20, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/57e356f72f08ef7d97259c522f6a7770?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hyperant&#39;s gravatar image" />
<p><span>Hyperant</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hyperant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73587" class="comments-container">
&#10;</div>
<div id="comment-tools-73587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73587-form-container" class="comment-form-container">
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

<span id="73596"></span>

<div id="answer-container-73596" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73596-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hyperant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you click on the "Download" button, after selecting SVG, it will generate this kind of URL : <a href="https://render.openstreetmap.org/cgi-bin/export?bbox=2.354260683059693,48.8476459732009,2.3654508590698247,48.8507382415782&amp;scale=2847&amp;format=svg">https://render.openstreetmap.org/cgi-bin/export?bbox=2.354260683059693,48.8476459732009,2.3654508590698247,48.8507382415782&amp;scale=2847&amp;format=svg</a></p>
<p>But as implied in this <a href="/questions/54056/missing-or-invalid-token-when-exporting-from-openstreetmaporg">previous question</a>, there is a token verification against API use, so it work only in your current browser. Also be aware that this kind of exports put a huge load on servers, so be really careful on the area you're trying to export. Probably better to stick to manual selection.</p>
<p>For other solutions about exporting SVG from OSM, have a look at this <a href="/questions/26275/export-to-svg-file">question</a>, this <a href="https://wiki.openstreetmap.org/wiki/SVG">wiki page</a>, and others. But I don't think you'll find anything about API.</p>
<p>If you need to programmatically render SVG, you're best bet will probably be <a href="https://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a>, it's more or less made for that. <a href="https://extract.bbbike.org/">BBBike</a> use it, so you can test there.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '20, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '20, 13:31</strong> </span></p>
</div>
</div>
<div id="comments-container-73596" class="comments-container">
<span id="73610"></span>
<div id="comment-73610" class="comment">
<div id="post-73610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your help.</p>
</div>
<div id="comment-73610-info" class="comment-info">
<span class="comment-age">(18 Mar '20, 18:40)</span> <span class="comment-user userinfo">Hyperant</span>
</div>
</div>
</div>
<div id="comment-tools-73596" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73596-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73591"></span>

<div id="answer-container-73591" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73591-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-73591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"No"</p>
<p>You need to build actual geometries (not present in "raw" OSM data) and then render them to SVG to achieve that, or use a service that provides that, for example <a href="https://extract.bbbike.org/">https://extract.bbbike.org/</a></p>
<p>In general asking people to google solutions for you is not a good strategy and simple pisses them off.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '20, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-73591" class="comments-container">
<span id="73592"></span>
<div id="comment-73592" class="comment">
<div id="post-73592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Googling was the first thing i did, but as i didn't find much in that regard i decided to make an account here but you did a good job making assumptions.</p>
<p>Passive aggressiveness aside, thanks for the help.</p>
</div>
<div id="comment-73592-info" class="comment-info">
<span class="comment-age">(18 Mar '20, 01:19)</span> <span class="comment-user userinfo">Hyperant</span>
</div>
</div>
</div>
<div id="comment-tools-73591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73591-form-container" class="comment-form-container">
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

