+++
type = "question"
title = "how to download OSM DB data with both land and sea data?"
description = '''Greetings. I&#x27;ve been using the planet.osm.pbf files from for a while to create offline maps for my application. I recently received a request to add maritime maps. I looked at the OpenSeaMap project, but they don&#x27;t seem to have a regularly updated export. And the planet files on https://planet.opens...'''
date = "2019-04-19T16:31:00Z"
lastmod = "2019-04-24T10:11:00Z"
weight = 68850
keywords = [ "seamark", "planet.osm", "openseamap" ]
aliases = [ "/questions/68850" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to download OSM DB data with both land and sea data?](/questions/68850/how-to-download-osm-db-data-with-both-land-and-sea-data)

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
<span id="post-68850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings.</p>
<p>I've been using the planet.osm.pbf files from for a while to create offline maps for my application. I recently received a request to add maritime maps. I looked at the OpenSeaMap project, but they don't seem to have a regularly updated export. And the planet files on <a href="https://planet.openstreetmap.org">https://planet.openstreetmap.org</a> don't seem to include anything with the seamark:* tags.</p>
<p>How can I get a planet file (or equivalent) with both land and sea raw vector data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-seamark" rel="tag" title="see questions tagged &#39;seamark&#39;">seamark</span> <span class="post-tag tag-link-planet.osm" rel="tag" title="see questions tagged &#39;planet.osm&#39;">planet.osm</span> <span class="post-tag tag-link-openseamap" rel="tag" title="see questions tagged &#39;openseamap&#39;">openseamap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '19, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ab48c3ad406e6af0a1bc72a50db16641?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndrewEMT&#39;s gravatar image" />
<p><span>AndrewEMT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndrewEMT has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68850" class="comments-container">
<span id="68854"></span>
<div id="comment-68854" class="comment">
<div id="post-68854-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Planet files include all data - your issue is perhaps more likely to be how you're loading it into your database. If you can give more details on what you're doing there, people can hopefully help you more.</p>
</div>
<div id="comment-68854-info" class="comment-info">
<span class="comment-age">(19 Apr '19, 19:08)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="68881"></span>
<div id="comment-68881" class="comment">
<div id="post-68881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I searched the entire contents of <a href="https://planet.openstreetmap.org/pbf/planet-190415.osm.pbf">https://planet.openstreetmap.org/pbf/planet-190415.osm.pbf</a> and there isn't one occurrence of any variant of the "seamark" keys in any tag records. I can't extract the seamarks if they are not in the file.</p>
</div>
<div id="comment-68881-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 04:52)</span> <span class="comment-user userinfo">AndrewEMT</span>
</div>
</div>
<span id="68884"></span>
<div id="comment-68884" class="comment">
<div id="post-68884-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>All of OSM is in that file. Like I said, please give more details on what you're doing. For example, when you say "I searched", explain how you are searching, what tool you're using, what arguments you're passing to it, etc. etc.</p>
</div>
<div id="comment-68884-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 09:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="68902"></span>
<div id="comment-68902" class="comment">
<div id="post-68902-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Never mind. You called it. I found a typo in my preprocessor that was discarding all records with seamark:type tags instead of storing them. Fixed now, and finding <em>lots</em> of seamark nodes and ways.</p>
</div>
<div id="comment-68902-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 01:52)</span> <span class="comment-user userinfo">AndrewEMT</span>
</div>
</div>
<span id="68911"></span>
<div id="comment-68911" class="comment">
<div id="post-68911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yay, glad it works :)</p>
</div>
<div id="comment-68911-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 10:11)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

