+++
type = "question"
title = "not visible change with lower zoom"
description = '''Hi, it might exist some relevant answer for my question but I haven&#x27;t found any so I allow to ask another one :-) I did some changes in openstreetmap through JOSM. These changes were visible almost immediately but only in higher zoom. In the lover zoom there was visible only the old state (without a...'''
date = "2013-02-05T14:41:00Z"
lastmod = "2013-02-05T19:02:00Z"
weight = 19588
keywords = [ "zoomlevel" ]
aliases = [ "/questions/19588" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [not visible change with lower zoom](/questions/19588/not-visible-change-with-lower-zoom)

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
<span id="post-19588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19588-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, it might exist some relevant answer for my question but I haven't found any so I allow to ask another one :-) I did some changes in openstreetmap through JOSM. These changes were visible almost immediately but only in higher zoom. In the lover zoom there was visible only the old state (without added roads, old types of roads...) What did I wrong?</p>
<p>lower zoom:</p>
<p><img src="/upfiles/lover_zoom.png" alt="alt text" /></p>
<p>higher zoom: <img src="/upfiles/higher_zoom_2.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '13, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/33062b4bfcbde283db18009d2c7bba06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milda_brno&#39;s gravatar image" />
<p><span>milda_brno</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milda_brno has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '13, 14:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</img>
</div>
</div>
<div id="comments-container-19588" class="comments-container">
<span id="19591"></span>
<div id="comment-19591" class="comment">
<div id="post-19591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's roughly <a href="https://www.openstreetmap.org/?lat=38.999&amp;lon=46.302&amp;zoom=11&amp;layers=M">here</a> I think...</p>
</div>
<div id="comment-19591-info" class="comment-info">
<span class="comment-age">(05 Feb '13, 14:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19588-form-container" class="comment-form-container">
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

<span id="19594"></span>

<div id="answer-container-19594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19594-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You didn't do anything wrong. This is the normal behaviour of the map rendering process.</p>
<p>Recalculating low zoom tiles is a relatively resource expensive operation. As a low zoom tiles covers a relatively large area, chances are that something changes in the area every minute. As the rendering process cannot determine if it is a relevant change ahead of time, it would have to re-render those low zooms very frequently. As rendering can take several minutes for low zoom, re-rendering the tiles on every change is clearly not feasible.</p>
<p>Furthermore, most changes (e.g. moving a building by half a meter) do not cause visual changes on low zoom. At least in well mapped areas, these non visible changes at low zoom are likely the vast majority.</p>
<p>Therefore, the system separates the rendering process into low zoom and high zoom tiles. (I can't remember at which zoom level the switch is). The high zoom tiles get expired on a minutely basis (if the data in their area changes) and will therefore get rerendered quickly once viewed.</p>
<p>Low zoom tiles are not re-rendered based on changes in the map data. Instead they are periodically re-rendered in full. Again, I don't know what this current update cycle is but it can be a week or longer.</p>
<p>If you know an area has changed and it has caused a noticable visual change in low zoom tiles, you can manually request a rerender of those tiles. This is done by right clicking on the area in the map and selecting "copy image URL". This should give you a URL like <a href="http://b.tile.openstreetmap.org/11/1286/782.png">http://b.tile.openstreetmap.org/11/1286/782.png</a> Then you can request a rerender by opening the URL <a href="http://b.tile.openstreetmap.org/11/1286/782.png/dirty">http://b.tile.openstreetmap.org/11/1286/782.png/dirty</a> After a couple of minutes to an hour, you should see your changes on that tile as well.</p>
<p>A more detailed description of the process can be found in <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">this answer</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '13, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19594" class="comments-container">
<span id="19597"></span>
<div id="comment-19597" class="comment">
<div id="post-19597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for excellent explanation. The link above helped me to comprehend this as well.</p>
</div>
<div id="comment-19597-info" class="comment-info">
<span class="comment-age">(05 Feb '13, 19:02)</span> <span class="comment-user userinfo">milda_brno</span>
</div>
</div>
</div>
<div id="comment-tools-19594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19594-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19592"></span>

<div id="answer-container-19592" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's sometimes a short delay before the update of the main map, as described in <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">this answer</a>, which also explains how to speed the process up. Some of the new roads are now visible at higher zoom too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '13, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '13, 14:49</strong> </span></p>
</div>
</div>
<div id="comments-container-19592" class="comments-container">
<span id="19593"></span>
<div id="comment-19593" class="comment">
<div id="post-19593-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>exactly ...</p>
</div>
<div id="comment-19593-info" class="comment-info">
<span class="comment-age">(05 Feb '13, 14:50)</span> <span class="comment-user userinfo">milda_brno</span>
</div>
</div>
</div>
<div id="comment-tools-19592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19592-form-container" class="comment-form-container">
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

