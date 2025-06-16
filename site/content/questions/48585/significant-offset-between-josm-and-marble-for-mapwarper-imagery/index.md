+++
type = "question"
title = "Significant offset between josm and marble for mapwarper imagery"
description = '''I managed to load a rectified Mapwarper layer off Marble&#x27;s cache in JOSM, but it has a very significant offset (500-ish km) and apparently it was heavily distorted. If it is seen through Marble, it looks fine without a problem. Is there any way to correct this? (quesion converted from a comment to h...'''
date = "2016-03-09T03:50:00Z"
lastmod = "2016-03-13T19:50:00Z"
weight = 48585
keywords = [ "mapwarper", "josm", "offline", "imagery", "marble" ]
aliases = [ "/questions/48585" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Significant offset between josm and marble for mapwarper imagery](/questions/48585/significant-offset-between-josm-and-marble-for-mapwarper-imagery)

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
<span id="post-48585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48585-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I managed to load a rectified Mapwarper layer off Marble's cache in JOSM, but it has a very significant offset (500-ish km) and apparently it was heavily distorted. If it is seen through Marble, it looks fine without a problem.</p>
<p>Is there any way to correct this?</p>
<p>(quesion converted from a comment to <a href="/questions/48466/how-to-configure-offline-imagery-for-josm">how to configure offline imagery for josm</a>)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapwarper" rel="tag" title="see questions tagged &#39;mapwarper&#39;">mapwarper</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-marble" rel="tag" title="see questions tagged &#39;marble&#39;">marble</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '16, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/de7b93bd537287f5af7e862bf4cd2fec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AkuAnakTimur&#39;s gravatar image" />
<p><span>AkuAnakTimur</span><br />
<span class="score" title="1070 reputation points"><span>1.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AkuAnakTimur has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted <strong>10 Mar '16, 22:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-48585" class="comments-container">
<span id="48621"></span>
<div id="comment-48621" class="comment">
<div id="post-48621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give more details about your setup ? What is the url of the mapwarper layer ? Are you using the same url in Marble and JOSM ? Is the mapwarper layer fully rectified ? Is it using mercator projection ?</p>
</div>
<div id="comment-48621-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 22:36)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="48623"></span>
<div id="comment-48623" class="comment">
<div id="post-48623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Setup details: JOSM 9900 and Marble 1.9.1 on Windows 7.</p>
<p>I am using <a href="http://mapwarper.net/maps/12937">this layer</a> that I composed myself. Then, I used the WMS link to display it through Marble (<code>File</code> &gt; <code>Create new map</code>).</p>
<p>The Mapwarper layer has been fully rectified, because it appears fine when the layer is viewed through Marble. Also, no problems if I used it as a WMS layer in JOSM.</p>
<p>I have checked the projection being used in both Marble and JOSM. Making sure both are using the same Mercator projection.</p>
<p>I also have attempted to delete and reload the Mapwarper layer in Marble, but it seems that I cannot rule out the offset problem.</p>
</div>
<div id="comment-48623-info" class="comment-info">
<span class="comment-age">(11 Mar '16, 01:28)</span> <span class="comment-user userinfo">AkuAnakTimur</span>
</div>
</div>
</div>
<div id="comment-tools-48585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48585-form-container" class="comment-form-container">
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

<span id="48633"></span>

<div id="answer-container-48633" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48633-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AkuAnakTimur has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can see the same offset as you do when using the WMS link in Marble. This is because this WMS url serves tiles in Equirectangular projection (see the <em>*.dgml</em> file in the marble directory).</p>
<p>Create the marble map using the <a href="http://mapwarper.net/maps/tile/12937/%7BzoomLevel%7D/%7Bx%7D/%7By%7D.png">tms url</a> and you'll have tiles in the mercator projection mandated by tms. You'll also get png tiles, which have the advantage of being transparent where mapwarper has no data.</p>
<p>Maybe you could achieve the same results using WMS parameters, but I don't know what those would be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '16, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-48633" class="comments-container">
<span id="48642"></span>
<div id="comment-48642" class="comment">
<div id="post-48642-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much! It worked! A bit late to respond to your solution due to a metered internet connection. I think I'll stick to your method, better keep it simple.</p>
<p>PS: Is this the correct way to fully download the Mapwarper layer on Marble? Select the Mapwarper layer and then <code>File</code> and then <code>Download region</code>?</p>
</div>
<div id="comment-48642-info" class="comment-info">
<span class="comment-age">(13 Mar '16, 17:46)</span> <span class="comment-user userinfo">AkuAnakTimur</span>
</div>
</div>
<span id="48643"></span>
<div id="comment-48643" class="comment">
<div id="post-48643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes it is the correct way to do this in marble. Also check marble's cache size settings.</p>
<p>On the other hand, watch out for tile usage policies, as bulk download of thousands of tiles are often frowned upon. Not sure what/where mapwarper's tile usage policy is.</p>
</div>
<div id="comment-48643-info" class="comment-info">
<span class="comment-age">(13 Mar '16, 19:50)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48633-form-container" class="comment-form-container">
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

