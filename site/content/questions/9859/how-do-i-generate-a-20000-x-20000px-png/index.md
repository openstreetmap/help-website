+++
type = "question"
title = "How do I generate a 20,000 x 20,000px png?"
description = '''If I wanted to generate a 20,000 by 20,000 png for a particular location, is that possible? It seems whenever I tried to export a tile via an http query it will only allow a height of 2,000? '''
date = "2012-01-09T00:57:00Z"
lastmod = "2018-08-22T22:09:00Z"
weight = 9859
keywords = [ "export", "png" ]
aliases = [ "/questions/9859" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How do I generate a 20,000 x 20,000px png?](/questions/9859/how-do-i-generate-a-20000-x-20000px-png)

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
<span id="post-9859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9859-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I wanted to generate a 20,000 by 20,000 png for a particular location, is that possible? It seems whenever I tried to export a tile via an http query it will only allow a height of 2,000?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '12, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ae5cb7694f1c50cdc64bd529aa85f77d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnmci&#39;s gravatar image" />
<p><span>johnmci</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnmci has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '12, 14:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-9859" class="comments-container">
&#10;</div>
<div id="comment-tools-9859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9859-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="9860"></span>

<div id="answer-container-9860" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9860-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-9860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible but none of our free services will do that for you. You have to understand that producing such large images does require a lot of resources - and while we give away OSM data for free, the amount of computing power that we can give away is limited.</p>
<p>There are several ways for you to acquire such an image. For example, you could download an SVG or PDF image from the export tab and then use a program like <code>rsvg</code> to produce a bitmap from the SVG. Or, you could render an image yourself using either your own Mapnik installation (powerful but a lot of work to set up - use that if you are on Linux and expect to render images like that more often) or a standalone renderer like Maperitive (runs on Linux and Windows). Details on both techniques can be found on <a href="http://wiki.openstreetmap.org">our wiki</a>.</p>
<p>There's also the option of using a third-party service. The free <a href="http://www.maposmatic.org">Maposmatic</a> generates large PNGs (albeit not the 400 Megapixel you're after) and PDFs. Some of the businesses listed on the <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">Commercial OSM Software and Services</a> page will also be able to produce such images as a paid service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '12, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9860" class="comments-container">
&#10;</div>
<div id="comment-tools-9860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9874"></span>

<div id="answer-container-9874" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9874-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>some more hints:</p>
<p><a href="http://help.openstreetmap.org/questions/22/how-do-i-export-map-images-of-larger-areas">how-do-i-export-map-images-of-larger-areas</a></p>
<p><a href="http://help.openstreetmap.org/questions/3494/create-a-wall-map-of-an-area-50-kilometers-by-120-kilometers">create-a-wall-map-of-an-area-50-kilometers-by-120-kilometers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '12, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-9874" class="comments-container">
&#10;</div>
<div id="comment-tools-9874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9874-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9886"></span>

<div id="answer-container-9886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9886-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check out <a href="http://viking.sf.net">Viking GPS</a>. While designed to work with GPS data, it also has the ability to output any map it is displaying to a graphic file (or files) in whatever resolution you choose. The data can come from any supported source, including several different OSM data tile source (Mapnik, osmarender, maplint). It is also possible to setup your own sources (TOPOsm, Yahoo, Google, Cloudmade styles). [It shouldn't need to be said, but be sure to check the licensing of the sources.]</p>
<p>BTW, If you do use Viking with any of the OSM tile sources, then please ensure you are following the Tile Usage Policy by setting your tile checking period to 7 days (Viking-&gt;Edit-&gt;Preferences-&gt;Tile Age = 604800). In versions prior to 1.2.2, it was inadvertently set to small (30 seconds).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '12, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffdc5279fd70540799b762c14e66665?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwernerny&#39;s gravatar image" />
<p><span>jwernerny</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwernerny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9886" class="comments-container">
&#10;</div>
<div id="comment-tools-9886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65394"></span>

<div id="answer-container-65394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could also use ffmpeg or imagemagik to combine multiple smaller images into a single image.</p>
<p>Try this: <a href="https://www.imagemagick.org/discourse-server/viewtopic.php?t=11672">https://www.imagemagick.org/discourse-server/viewtopic.php?t=11672</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '18, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/644620e74a312b0ce02a0a1bb1bae155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlanHalls&#39;s gravatar image" />
<p><span>AlanHalls</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlanHalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65394" class="comments-container">
<span id="65515"></span>
<div id="comment-65515" class="comment">
<div id="post-65515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>there are different <a href="https://wiki.openstreetmap.org/wiki/Bigmap">bigmap scripts</a> that come in handy for downloading the tiles of bigger areas.</p>
</div>
<div id="comment-65515-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 22:09)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-65394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65394-form-container" class="comment-form-container">
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

