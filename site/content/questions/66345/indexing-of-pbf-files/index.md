+++
type = "question"
title = "Indexing of PBF files"
description = '''I&#x27;ve contributed to OSM on and off for years but I&#x27;m getting back in to it due to work and Google&#x27;s new pricing being prohibitive. I&#x27;ve set up a server to handle tiles, geocoding and routing for the planet which is great but one pattern is each tool has to do lots of mucking around to put the nodes,...'''
date = "2018-10-15T06:15:00Z"
lastmod = "2018-10-15T09:05:00Z"
weight = 66345
keywords = [ "pbf", "osm2pgsql", "imposm" ]
aliases = [ "/questions/66345" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Indexing of PBF files](/questions/66345/indexing-of-pbf-files)

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
<span id="post-66345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66345-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've contributed to OSM on and off for years but I'm getting back in to it due to work and Google's new pricing being prohibitive.</p>
<p>I've set up a server to handle tiles, geocoding and routing for the planet which is great but one pattern is each tool has to do lots of mucking around to put the nodes, ways and relations in to a reasonable order.</p>
<p>The pbf format has the capability to be indexed but its never used. Is there a reason for that? Numerical id order makes sense for doing the dump, but not at all for any kind of processing.</p>
<p>I'd imagine a simple geohash grouping of everything done once would improve import speeds and slicing speeds immensely since relevant nodes for a way would be physically located closely thus maximising cache hits.</p>
<p>Is there a reason this isn't done that I've missed? If not I'm tempted to make a indexer and make the relevant patches to the tools that could benefit from it the most.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '18, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0aa50e7695ec5f78dcacab82bc1cd81e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cheater512&#39;s gravatar image" />
<p><span>cheater512</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cheater512 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66345" class="comments-container">
<span id="66346"></span>
<div id="comment-66346" class="comment">
<div id="post-66346-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This help site is designed for questions and answers but not really suited for starting large discussions. It sounds like you have an interesting issue to discuss. Try posting it at <a href="https://lists.openstreetmap.org/pipermail/dev/">https://lists.openstreetmap.org/pipermail/dev/</a> instead.</p>
</div>
<div id="comment-66346-info" class="comment-info">
<span class="comment-age">(15 Oct '18, 09:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

