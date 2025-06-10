+++
type = "question"
title = "Maintaining OSM-related servers"
description = '''Hi all, I would like to setup and maintain 3 services that use OSM: (1) Nominatim, (2) Map Tile Server, and (3) Overpass API. I am thinking of keeping these three services separate by creating Docker images for each one of them and deploying them on the same physical machine. Do you think this is a ...'''
date = "2017-11-09T09:38:00Z"
lastmod = "2017-11-10T12:45:00Z"
weight = 60523
keywords = [ "overpass", "docker", "nominatim", "tileserver" ]
aliases = [ "/questions/60523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maintaining OSM-related servers](/questions/60523/maintaining-osm-related-servers)

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
<span id="post-60523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60523-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I would like to setup and maintain 3 services that use OSM: (1) Nominatim, (2) Map Tile Server, and (3) Overpass API.</p>
<p>I am thinking of keeping these three services separate by creating Docker images for each one of them and deploying them on the same physical machine. Do you think this is a good idea in terms of maintenance or would you suggest another approach?</p>
<p>Also, do you have any tips for regular updating of the maps?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '17, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ffa27b3528b8ca8273629ac64cf9f828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pesho318i&#39;s gravatar image" />
<p><span>pesho318i</span><br />
<span class="score" title="27 reputation points">27</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pesho318i has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '17, 20:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-60523" class="comments-container">
<span id="60530"></span>
<div id="comment-60530" class="comment">
<div id="post-60530-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The answer is something between "don't" and "that will work fine" depending on size of area you are working with and available HW.</p>
<p>The other thing is that the available Docker images tend to be orientated at development and not performance (and disk/IO are a significant concern for all three applications).</p>
</div>
<div id="comment-60530-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 08:21)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="60533"></span>
<div id="comment-60533" class="comment">
<div id="post-60533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, are you basing your statement on a particular study? All of the benchmarks I've encountered show that Docker's performance is comparable to native hardware performance (on Linux machines in particular). Here are a few links: <a href="https://stackoverflow.com/questions/21889053/what-is-the-runtime-performance-cost-of-a-docker-container">https://stackoverflow.com/questions/21889053/what-is-the-runtime-performance-cost-of-a-docker-container</a> and <a href="https://www.percona.com/blog/2016/02/11/measuring-docker-io-overhead/">https://www.percona.com/blog/2016/02/11/measuring-docker-io-overhead/</a></p>
<p>Regarding these three services, I am expecting more load on the tile server, and the other two will handle occasional requests.</p>
</div>
<div id="comment-60533-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 10:52)</span> <span class="comment-user userinfo">pesho318i</span>
</div>
</div>
<span id="60535"></span>
<div id="comment-60535" class="comment">
<div id="post-60535-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is not that Docker itself is an issue, but more that you need to consider where to locate the databases on what kind of media and filesystems, and that in general you start needing largish machines for essentially anything that provide services for the full planet.</p>
</div>
<div id="comment-60535-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 12:45)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

