+++
type = "question"
title = "How to extract only water using osmosis?"
description = '''Hi all I&#x27;m trying to extract only waterbodies from a .osm file using osmosis. I&#x27;m almost there, but my command is returning islands and islets as water and I can&#x27;t figure out how to get only water!  Here&#x27;s the command I&#x27;m using: osmosis --read-xml swedencity.osm --tf accept-relations natural=water l...'''
date = "2018-04-10T18:41:00Z"
lastmod = "2018-04-11T01:55:00Z"
weight = 62968
keywords = [ "water", "islands", "extract", ".osm", "osmosis" ]
aliases = [ "/questions/62968" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract only water using osmosis?](/questions/62968/how-to-extract-only-water-using-osmosis)

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
<span id="post-62968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62968-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I'm trying to extract only waterbodies from a .osm file using osmosis. I'm almost there, but my command is returning islands and islets as water and I can't figure out how to get only water!</p>
<p>Here's the command I'm using:</p>
<p>osmosis --read-xml swedencity.osm --tf accept-relations natural=water landuse=basin,reservoir --tf reject-relations intermittent=yes --used-way --used-node --write-pbf swedencity-waterbody-relations.osm.pbf</p>
<p>This returns the water I want, but also returns features with place=island and islet, as well as a ton of smaller islands w/o any place tag. Is there a way to eliminate all of these? My attempts to reject island relations have failed so far...</p>
<p>Any help is much appreciated! Thanks so much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '18, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/855fd1aa595f0c2d9c301a1f1bb42b5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kellya&#39;s gravatar image" />
<p><span>kellya</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kellya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '18, 22:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62968" class="comments-container">
<span id="62970"></span>
<div id="comment-62970" class="comment">
<div id="post-62970-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They are likely inner members of water relations; that's how water is modeled in OSM, with islands as holes in the water.</p>
</div>
<div id="comment-62970-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 01:55)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-62968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62968-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

