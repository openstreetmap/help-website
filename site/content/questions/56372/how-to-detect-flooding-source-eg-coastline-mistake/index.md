+++
type = "question"
title = "How to detect flooding source (e.g. coastline mistake)?"
description = '''In the past month, I&#x27;ve seen repeated water-flooding that keeps flipping between flooded/not flooded. This means that map is rendered inconsistently, as seen below.   - screenshot of https://www.openstreetmap.org/query?lat=50.06402&amp;amp;lon=14.47634#map=19/50.06396/14.47586 Yet, according to tile sta...'''
date = "2017-05-30T11:02:00Z"
lastmod = "2017-06-13T09:52:00Z"
weight = 56372
keywords = [ "qa", "flood", "coastline" ]
aliases = [ "/questions/56372" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect flooding source (e.g. coastline mistake)?](/questions/56372/how-to-detect-flooding-source-eg-coastline-mistake)

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
<span id="post-56372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56372-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the past month, I've seen repeated water-flooding that keeps flipping between flooded/not flooded. This means that map is rendered inconsistently, as seen below. <img src="https://help.openstreetmap.org/upfiles/flood.png" alt="half-flooded map" /> - screenshot of <a href="https://www.openstreetmap.org/query?lat=50.06402&amp;lon=14.47634#map=19/50.06396/14.47586">https://www.openstreetmap.org/query?lat=50.06402&amp;lon=14.47634#map=19/50.06396/14.47586</a></p>
<p>Yet, according to tile status, tiles are clean and rendered at the same time: <a href="https://tile.openstreetmap.org/19/283225/177664.png/status">https://tile.openstreetmap.org/19/283225/177664.png/status</a> is a northernmost flooded tile, and <a href="https://tile.openstreetmap.org/19/283225/177663.png/status">https://tile.openstreetmap.org/19/283225/177663.png/status</a> is one non-flooded just adjacent.</p>
<p>Querying for enclosing features doesn't give any hints as to where the water comes from. Judging from the [flood] questions, this seems to be a coastline error, but as I'm in mainland Europe, the coastline is a bit long for manual inspection. Looking at <a href="https://tools.geofabrik.de/osmi/">OSMi Coastline view</a>, I don't see any issues either; and from <a href="http://tile.openstreetmap.org/cgi-bin/debug">http://tile.openstreetmap.org/cgi-bin/debug</a>, I see coastline edits a few days old.</p>
<p>Now, my issue isn't "someone fix this instance of the error" (which is not entirely polite, given that I should theoretically be capable of fixing it myself) but rather "how can I find where the error is to fix this"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qa" rel="tag" title="see questions tagged &#39;qa&#39;">qa</span> <span class="post-tag tag-link-flood" rel="tag" title="see questions tagged &#39;flood&#39;">flood</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '17, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '17, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-56372" class="comments-container">
<span id="56376"></span>
<div id="comment-56376" class="comment">
<div id="post-56376-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Given the location I would consider a coastline issue rather unlikely (not that it couldn't happen, but then there would have been lots of other complaints from all of Europe). Are you sure that you are not looking far to far and that nobody simply messed up the local riverbank?</p>
</div>
<div id="comment-56376-info" class="comment-info">
<span class="comment-age">(30 May '17, 11:43)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="56377"></span>
<div id="comment-56377" class="comment">
<div id="post-56377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, that looks plausible. Will check, thank you.</p>
</div>
<div id="comment-56377-info" class="comment-info">
<span class="comment-age">(30 May '17, 12:03)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="56601"></span>
<div id="comment-56601" class="comment">
<div id="post-56601-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmm...no idea what caused it, but seems to be fixed. There have been complaints in neighboring countries, so perhaps it could have been a major riverbank.</p>
</div>
<div id="comment-56601-info" class="comment-info">
<span class="comment-age">(13 Jun '17, 09:52)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-56372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

