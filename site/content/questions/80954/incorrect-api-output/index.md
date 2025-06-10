+++
type = "question"
title = "Incorrect API output"
description = '''I&#x27;m using the MapQuest Geocoder API for an integrated Maps component in my application. The address &quot;Savelveld 25, 6039 SB, Stramproy&quot; is displayed in America while this is an address in The Netherlands. The coordinates are being generated incorrectly by the API. Input: &quot;Savelveld 25, 6039 SB, Stram...'''
date = "2021-07-14T09:25:00Z"
lastmod = "2021-07-17T17:26:00Z"
weight = 80954
keywords = [ "marker", "api", "netherlands", "postcodes", "coordinates" ]
aliases = [ "/questions/80954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect API output](/questions/80954/incorrect-api-output)

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
<span id="post-80954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the MapQuest Geocoder API for an integrated Maps component in my application. The address "Savelveld 25, 6039 SB, Stramproy" is displayed in America while this is an address in The Netherlands. The coordinates are being generated incorrectly by the API.</p>
<p>Input: "Savelveld 25, 6039 SB, Stramproy" Output: { "CoordSets": [ [ { "Lon": "-100.445882", "Lat": "39.78373" } ] ] }</p>
<p>The correct output should be: { "CoordSets": [ [ { "Lon": "5.711368", "Lat": "51.200246" } ] ] }</p>
<p>Can you please let me know how we can make these coordinates correct in the so ? Is there someone from the development team who can change it into the source code?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-netherlands" rel="tag" title="see questions tagged &#39;netherlands&#39;">netherlands</span> <span class="post-tag tag-link-postcodes" rel="tag" title="see questions tagged &#39;postcodes&#39;">postcodes</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '21, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/3f7325dc9d3938e0968fa85410558fd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dennis&#39;s gravatar image" />
<p><span>Dennis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dennis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jul '21, 10:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-80954" class="comments-container">
<span id="80957"></span>
<div id="comment-80957" class="comment">
<div id="post-80957-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is not MapQuest's developer support desk, you should probably contact them.</p>
</div>
<div id="comment-80957-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 09:58)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="81021"></span>
<div id="comment-81021" class="comment">
<div id="post-81021-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To make Richards answers clear Mapquest stopped using OSM data directly a long time ago and may not be using any at all at this point in time. At least at times the services were provided by mapbox, but in any case you are completely wrong here and need to talk to mapquest.</p>
</div>
<div id="comment-81021-info" class="comment-info">
<span class="comment-age">(17 Jul '21, 17:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80954-form-container" class="comment-form-container">
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

<span id="80959"></span>

<div id="answer-container-80959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80959-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim would find the address, if you delete the space in 6039 SB, example:</p>
<p><a href="https://nominatim.openstreetmap.org/ui/search.html?q=Savelveld+25%2C+6039SB%2C+Stramproy">https://nominatim.openstreetmap.org/ui/search.html?q=Savelveld+25%2C+6039SB%2C+Stramproy</a></p>
<p>but does not find the address if the space is included:</p>
<p><a href="https://nominatim.openstreetmap.org/ui/search.html?q=Savelveld+25%2C+6039%20SB%2C+Stramproy">https://nominatim.openstreetmap.org/ui/search.html?q=Savelveld+25%2C+6039%20SB%2C+Stramproy</a></p>
<p>The dutch postcode search at <a href="https://www.postcode.nl/6039SB/25">https://www.postcode.nl/6039SB/25</a> shows that Dutch postcodes should be written without a space, but I'm not sure about the definition of postcode patterns in the Netherlands, so this should probably be discussed/asked with the Dutch OSM community at the Dutch mailinglist at <a href="https://lists.openstreetmap.org/pipermail/talk-nl">https://lists.openstreetmap.org/pipermail/talk-nl</a> or the Dutch forums at <a href="https://forum.openstreetmap.org/viewforum.php?id=12">https://forum.openstreetmap.org/viewforum.php?id=12</a> . If both patterns are correct, it would be an issue for nominatim.</p>
<p>Regarding the wrong U.S. response by Mapquest: that's sth. you should bring up at Mapquest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '21, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jul '21, 10:05</strong> </span></p>
</div>
</div>
<div id="comments-container-80959" class="comments-container">
&#10;</div>
<div id="comment-tools-80959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80959-form-container" class="comment-form-container">
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

