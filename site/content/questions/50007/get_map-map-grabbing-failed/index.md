+++
type = "question"
title = "get_map map grabbing failed"
description = '''I am trying to use R to download a map but am getting a map grabbing failed message: mapImage &amp;lt;- get_map(location = c(lon = -87.89, lat = 43.05),color = &quot;color&quot;,source = &quot;osm&quot;,zoom = 6) Map from URL : http://maps.googleapis.com/maps/api/staticmap?center=43.05,-87.89&amp;amp;zoom=6&amp;amp;size=640x640&amp;am...'''
date = "2016-06-04T08:40:00Z"
lastmod = "2016-06-04T11:34:00Z"
weight = 50007
keywords = [ "r", "export", "png", "error" ]
aliases = [ "/questions/50007" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [get_map map grabbing failed](/questions/50007/get_map-map-grabbing-failed)

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
<span id="post-50007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use R to download a map but am getting a map grabbing failed message:</p>
<p>mapImage &lt;- get_map(location = c(lon = -87.89, lat = 43.05),color = "color",source = "osm",zoom = 6) Map from URL : <a href="http://maps.googleapis.com/maps/api/staticmap?center=43.05,-87.89&amp;zoom=6&amp;size=640x640&amp;scale=2&amp;maptype=terrain&amp;sensor=false">http://maps.googleapis.com/maps/api/staticmap?center=43.05,-87.89&amp;zoom=6&amp;size=640x640&amp;scale=2&amp;maptype=terrain&amp;sensor=false</a></p>
<p>Error: map grabbing failed - see details in ?get_openstreetmap. In addition: Warning message: In download.file(url, destfile = destfile, quiet = !messaging, mode = "wb") : cannot open URL 'http://tile.openstreetmap.org/cgi-bin/export?bbox=-94.910263671875,37.6894455061226,-80.847763671875,47.9652621160178&amp;scale=10000000&amp;format=png': HTTP status was '0 (null)'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '16, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb3c85bb5a859d18e7bcf2d016ffc63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erikwanta&#39;s gravatar image" />
<p><span>erikwanta</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erikwanta has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '16, 11:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50007" class="comments-container">
<span id="50009"></span>
<div id="comment-50009" class="comment">
<div id="post-50009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You do not really ask about a google maps error here, right? ;-)</p>
</div>
<div id="comment-50009-info" class="comment-info">
<span class="comment-age">(04 Jun '16, 09:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50007-form-container" class="comment-form-container">
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

<span id="50011"></span>

<div id="answer-container-50011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely the image area is too big or the server currently has too high load to process your special request. Also see <a href="/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment">https://help.openstreetmap.org/questions/21192/error-export-load-average-on-the-server-is-too-high-at-the-moment</a> .</p>
<p>Use <a href="https://wiki.openstreetmap.org/wiki/Tiles">tiles</a> instead - they are usually pre-rendered and served via a CDN. Or use a different service (e.g. MapQuest Open Static Maps, see <span>OSM on paper</span>) which is based on OpenStreetMap data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '16, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '16, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-50011" class="comments-container">
&#10;</div>
<div id="comment-tools-50011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50011-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50013"></span>

<div id="answer-container-50013" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50013-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="/questions/41673/get-open-street-map-in-r">this</a> previous question among others re R. The options at aseerel4c26's "OSM on paper" link are the way to go, if you want a rendered map (as opposed to the map data itself).</p>
<p>Would it be possible to find out whose code it is (in whatever library or example) that contains the offending "http://tile.openstreetmap.org/cgi-bin/export?bbox=" request? I'd be happy to explain why what they are suggesting will almost never work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '16, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-50013" class="comments-container">
&#10;</div>
<div id="comment-tools-50013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50013-form-container" class="comment-form-container">
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

