+++
type = "question"
title = "Filtering nodes with osmfilter"
description = '''Hi, I am trying to filter all the types of highways from my OSM file, the command I use does filter out highways but still keeps the nodes. I have attached an image of my output, I would like to remove those nodes. The commands I have used are,   osmfilter _removeHighways.osm --drop=&quot;highway=&quot; -o=go...'''
date = "2020-11-12T12:08:00Z"
lastmod = "2020-11-13T09:35:00Z"
weight = 77522
keywords = [ "filter", "nodes", "osmfilter", "help" ]
aliases = [ "/questions/77522" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering nodes with osmfilter](/questions/77522/filtering-nodes-with-osmfilter)

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
<span id="post-77522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77522-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to filter all the types of highways from my OSM file, the command I use does filter out highways but still keeps the nodes. I have attached an image of my output, I would like to remove those nodes. The commands I have used are,</p>
<blockquote>
<p>osmfilter _removeHighways.osm --drop="highway=" -o=good_ways.osm</p>
<p>osmfilter _removeHighways.osm --drop="highway=" --drop-nodes=highway -o=good_wayss.osm</p>
</blockquote>
<p>I am new to osmfilter any help will be appreciated :)</p>
<p><img src="/upfiles/nodes.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '20, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '20, 12:12</strong> </span></p>
</div>
</div>
<div id="comments-container-77522" class="comments-container">
<span id="77530"></span>
<div id="comment-77530" class="comment">
<div id="post-77530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it deletes the ways but not the nodes of those deleted ways</p>
</div>
<div id="comment-77530-info" class="comment-info">
<span class="comment-age">(13 Nov '20, 06:27)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
</div>
<div id="comment-tools-77522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77522-form-container" class="comment-form-container">
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

<span id="77531"></span>

<div id="answer-container-77531" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the osm file i use had custom key and pair values inputted, so osmosis would give me an error about nodes not having a version error, so i was not able to filter it with osmosis. solution i found was using osmfilter to remove what you want but it left it the nodes after dropping all highways. what i done was dropped the author and version of my osm file using osm filter</p>
<blockquote>
<p>osmfilter _EU.osm --drop-ways="highway=" --drop-version --ignore-dependencies -o=wgood_ways.osm</p>
</blockquote>
<p>could add --drop-author but i done it on a seperate line at the time, created fake authors and version.</p>
<blockquote>
<p>osmfilter wgood_ways.osm --fake-author --fake-version -o=zwgood_ways.osm</p>
</blockquote>
<p>now this file was ready to use in osmosis, the command i used to drop the nodes that were left there in osmosis was:</p>
<blockquote>
<p>osmosis --read-xml "D:\osmosis\bin\zwgood_ways.osm" --used-node --write-xml eust1.osm</p>
</blockquote>
<p>note* if you get this error using osmosis just create version and author for the file on osmfilter</p>
<p><em>Node -5625933 does not have a version attribute as OSM 0.6 are required to have. Is this a 0.5 file?</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '20, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77531" class="comments-container">
<span id="77532"></span>
<div id="comment-77532" class="comment">
<div id="post-77532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>credit to this links they came in handy <a href="https://groups.google.com/g/maperitive/c/iRz9u2RMTi8">https://groups.google.com/g/maperitive/c/iRz9u2RMTi8</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Drop_Author_Information_and_Version_Number">https://wiki.openstreetmap.org/wiki/Osmfilter#Drop_Author_Information_and_Version_Number</a></p>
<p><a href="https://www.mankier.com/1/osmfilter#Example">https://www.mankier.com/1/osmfilter#Example</a></p>
</div>
<div id="comment-77532-info" class="comment-info">
<span class="comment-age">(13 Nov '20, 09:35)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
</div>
<div id="comment-tools-77531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77531-form-container" class="comment-form-container">
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

