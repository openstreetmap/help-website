+++
type = "question"
title = "changes not appearing on the map!"
description = '''Hi on January 14th I made 4 amendments to Dublin locations on the map: 14650544 January 14, 2013 17:59 corrected the location of a Gym. I simply moved the icon. 14649781 January 14, 2013 16:57 entered details for an Alcohol shop (called &quot;Off Licence&quot; in Ireland) Dropped the icon &amp;amp; gave it a name...'''
date = "2013-01-17T18:02:00Z"
lastmod = "2013-01-17T23:03:00Z"
weight = 19170
keywords = [ "changes" ]
aliases = [ "/questions/19170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changes not appearing on the map!](/questions/19170/changes-not-appearing-on-the-map)

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
<span id="post-19170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi on January 14th I made 4 amendments to Dublin locations on the map:</p>
<p>14650544 January 14, 2013 17:59 corrected the location of a Gym. I simply moved the icon.</p>
<p>14649781 January 14, 2013 16:57 entered details for an Alcohol shop (called "Off Licence" in Ireland) Dropped the icon &amp; gave it a name.</p>
<p>14649733 January 14, 2013 16:53 put in adress &amp; web site for the shop below</p>
<p>14649639 January 14, 2013 16:45 Entered the name for an unnamed bike shop.</p>
<p>I see none of the changes on the map, but when I go into edit mode theyre all there.</p>
<p>Whatt am I doing wrong?</p>
<p>Thanks</p>
<p>Eoin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '13, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/54d2beea9e8fb724efe00037d7af41c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EoinBairead&#39;s gravatar image" />
<p><span>EoinBairead</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EoinBairead has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19170" class="comments-container">
&#10;</div>
<div id="comment-tools-19170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19170-form-container" class="comment-form-container">
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

<span id="19171"></span>

<div id="answer-container-19171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19171-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking these one at a time:</p>
<pre><code>14649639 January 14, 2013 16:45 Entered the name for an unnamed bike shop.</code></pre>
<p>I guess the renderer is struggling to display "Delaney's - Dublin's oldest bike shop." in the space available? You wouldn't expect to see the address and website displayed on the standard map.</p>
<p>If you click on the layer switcher, then the data layer, then hide areas, then click on your bike shop node you can see that all the details are in there.</p>
<pre><code>14649781 January 14, 2013 16:57 entered details for an Alcohol shop (called &quot;Off Licence&quot; in Ireland) Dropped the icon &amp; gave it a name.</code></pre>
<p>I suspect that the problem here might be that "shop=alcohol" isn't rendered on the standard map. There's a <a href="https://trac.openstreetmap.org/ticket/3043">trac ticket</a> raised for the rendering of generic shops, and discussion on that ticket as to whether it's a good idea or not.</p>
<pre><code>14650544 January 14, 2013 17:59 corrected the location of a Gym. I simply moved the icon.</code></pre>
<p>I suspect the problem here might be similar - I'm not aware that "leisure=sports_centre" is rendered on the standard map (for example the one <a href="http://www.openstreetmap.org/?lat=53.228842&amp;lon=-1.422019&amp;zoom=18&amp;layers=M">here</a> just shows as a generic name on an area).</p>
<p>However, just because they don't render on one particular map doesn't mean that you shouldn't map them. The data's still there, it'll appear on any maps designed to show that particular information. I can also type "Delaney's - Dublin's oldest bike shop" in the search box and it'll find it!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '13, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19171" class="comments-container">
<span id="19174"></span>
<div id="comment-19174" class="comment">
<div id="post-19174-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>As a brief postscript - you shouldn't enter a name of "Delaney's - Dublin's oldest bike shop." unless that's really what it's called. You should call it just "Delaney's" or maybe (as seems to be its official name) "T Delaney &amp; Son". If you want to record a description, you could add that in a description tag, though I don't think many renderers will use that.</p>
</div>
<div id="comment-19174-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 20:56)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="19177"></span>
<div id="comment-19177" class="comment">
<div id="post-19177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi</p>
<p>thanks to you those who answered.</p>
<p>However, as regards:</p>
<p>..<br />
14650544 January 14, 2013 17:59 corrected the location of a Gym. I simply moved the icon.</p>
<p>I suspect the problem here might be similar - I'm not aware that "leisure=sports_centre" is rendered on the standard map (for example the one here just shows as a generic name on an area).<br />
..<br />
</p>
<p>I simply moved the icon. It was clearly on the map. I moved it. Now it's no longer on the map.</p>
<p>Eoin</p>
</div>
<div id="comment-19177-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 22:36)</span> <span class="comment-user userinfo">EoinBairead</span>
</div>
</div>
<span id="19178"></span>
<div id="comment-19178" class="comment">
<div id="post-19178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What did it appear as on the map previously? A name, or an icon of some sort?</p>
</div>
<div id="comment-19178-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 22:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19179"></span>
<div id="comment-19179" class="comment">
<div id="post-19179-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Very possibly, the place you've moved it to already has an icon at it, and Mapnik (the rendering software) is dropping one of them for legibility reasons.</p>
</div>
<div id="comment-19179-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 23:03)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19171-form-container" class="comment-form-container">
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

