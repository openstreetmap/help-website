+++
type = "question"
title = "7 digits for marker coordinates"
description = '''The following URL (with 7 digits in the fraction): https://www.openstreetmap.org/?mlat=41.0404437&amp;amp;mlon=-73.9146759 Ends up being transformed to the following (with the fraction rounded to 5 digits): https://www.openstreetmap.org/?mlat=41.0404437&amp;amp;mlon=-73.9146759#map=19/41.04044/-73.91468 Thi...'''
date = "2022-09-14T16:51:00Z"
lastmod = "2022-09-14T17:42:00Z"
weight = 85628
keywords = [ "precision", "coordinates" ]
aliases = [ "/questions/85628" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [7 digits for marker coordinates](/questions/85628/7-digits-for-marker-coordinates)

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
<span id="post-85628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The following URL (with 7 digits in the fraction):</p>
<p><a href="https://www.openstreetmap.org/?mlat=41.0404437&amp;mlon=-73.9146759">https://www.openstreetmap.org/?mlat=41.0404437&amp;mlon=-73.9146759</a></p>
<p>Ends up being transformed to the following (with the fraction rounded to 5 digits):</p>
<p><a href="https://www.openstreetmap.org/?mlat=41.0404437&amp;mlon=-73.9146759#map=19/41.04044/-73.91468">https://www.openstreetmap.org/?mlat=41.0404437&amp;mlon=-73.9146759#map=19/41.04044/-73.91468</a></p>
<p>This, of course, puts the marker in the wrong place.</p>
<p>Clearly, objects in the OSM database are stored with more precision.</p>
<p><strong>Why can't the URL use all of the provided precision?</strong></p>
<p>(Google maps has the same issue. It seems you can work around that using "plus codes".)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-precision" rel="tag" title="see questions tagged &#39;precision&#39;">precision</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '22, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f830fd74979be37e141bd38e9d263cb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dpawlyk&#39;s gravatar image" />
<p><span>dpawlyk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dpawlyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85628" class="comments-container">
<span id="85631"></span>
<div id="comment-85631" class="comment">
<div id="post-85631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Err. It looks like the issue is with the source.</p>
<p>Thanks.</p>
</div>
<div id="comment-85631-info" class="comment-info">
<span class="comment-age">(14 Sep '22, 17:42)</span> <span class="comment-user userinfo">dpawlyk</span>
</div>
</div>
</div>
<div id="comment-tools-85628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85628-form-container" class="comment-form-container">
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

<span id="85630"></span>

<div id="answer-container-85630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85630-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>The marker coordinates in your second URL are not rounded, the <code>map=</code> stuff represents the map view.</p>
<p>Also sixth and seventh digits represent roughly decimeters and centimeters respectively. See <a href="http://wiki.gis.com/wiki/index.php/Decimal_degrees">http://wiki.gis.com/wiki/index.php/Decimal_degrees</a></p>
<p>Not much in OSM has that kind of precision, except probably survey points and such.</p>
<p>The data is stored with huge precision, but objects are mapped from satellite imagery and GPS tracks, where the precision is usually is the meter range.</p>
<p>So if the marker is not where you expected it, I suppose the coordinates are wrong, or the mapping around it is shifted.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '22, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-85630" class="comments-container">
&#10;</div>
<div id="comment-tools-85630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85629"></span>

<div id="answer-container-85629" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85629-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The marker is in the correct position. What gets rounded is the centre point of the map display, meaning that the marker will not be 100% at the centre of the screen, but given that the marker only makes up a fraction of the screen space, you will not even notice it being off centre by a few pixels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '22, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85629" class="comments-container">
&#10;</div>
<div id="comment-tools-85629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85629-form-container" class="comment-form-container">
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

