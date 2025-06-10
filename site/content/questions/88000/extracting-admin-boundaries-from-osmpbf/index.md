+++
type = "question"
title = "Extracting admin boundaries from osm.pbf"
description = '''Hi, I’m trying to extract admin boundaries (and all the relations in between) from country specific osm.pbf file. I have tried using OsmSharp (c# lib) and PyOsmium (python lib) to do the extraction, but I can’t seem to figure out how to do it properly. I don’t get expected relations and osm.pbf file...'''
date = "2023-11-13T16:13:00Z"
lastmod = "2023-11-13T16:13:00Z"
weight = 88000
keywords = [ "osmium", "osmsharp", "pyosmium" ]
aliases = [ "/questions/88000" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting admin boundaries from osm.pbf](/questions/88000/extracting-admin-boundaries-from-osmpbf)

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
<span id="post-88000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I’m trying to extract admin boundaries (and all the relations in between) from country specific osm.pbf file. I have tried using OsmSharp (c# lib) and PyOsmium (python lib) to do the extraction, but I can’t seem to figure out how to do it properly. I don’t get expected relations and osm.pbf file contains info on neighbouring countries as well so I can’t just do “get all admin_level=4” or similar.</p>
<p>I worked around neighbouring countries by first querying admin_level=2 with known country osm id and getting relations from there, I get relations of admin_level=4 which are fine, but from there on, relations are not found (for deeper levels).</p>
<p>Expected output would be something like you can find here OSM-Boundaries 1 where it would be few admin levels deep with relations to one another. I would later store that data in my database for future use.</p>
<p>Can somebody point me in the right direction on how to do it? with either OsmSharp/PyOsmium or just an guide I could try to translate in to code, I would really appreciate it.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-osmsharp" rel="tag" title="see questions tagged &#39;osmsharp&#39;">osmsharp</span> <span class="post-tag tag-link-pyosmium" rel="tag" title="see questions tagged &#39;pyosmium&#39;">pyosmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '23, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a64912c3817563dbb12d1ec1e09d0e07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anopen123&#39;s gravatar image" />
<p><span>anopen123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anopen123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88000" class="comments-container">
&#10;</div>
<div id="comment-tools-88000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88000-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

