+++
type = "question"
title = "Where to report abusive changesets ?"
description = '''Hi, The changeset 5592567 seems to be adding lots of unwanted nodes. What is the best way to proceed here ? I contacted the author but he does not answer. I would review all the added nodes and revert(delete) only those who don&#x27;t make sense. Unfortunately there are LOTS of nodes, it&#x27;s hard to decide...'''
date = "2014-04-22T23:38:00Z"
lastmod = "2014-04-25T00:27:00Z"
weight = 32542
keywords = [ "changeset", "abuse", "revert" ]
aliases = [ "/questions/32542" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Where to report abusive changesets ?](/questions/32542/where-to-report-abusive-changesets)

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
<span id="post-32542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32542-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>The changeset <a href="https://www.openstreetmap.org/changeset/5592567">5592567</a> seems to be adding lots of unwanted nodes. What is the best way to proceed here ? I contacted the author but he does not answer. I would review all the added nodes and revert(delete) only those who don't make sense. Unfortunately there are LOTS of nodes, it's hard to decide wether a node is useful AND some nodes have been already fixed or edited to something meaningful.</p>
<p>What's the best to do here ? Just revert the entire changeset ? Manual review ? Anyone volunteer ?</p>
<p>Thanks, Exxos. p.s. btw the nodes with name "GC?????" are actually GeoCache nodes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-abuse" rel="tag" title="see questions tagged &#39;abuse&#39;">abuse</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '14, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/de5e2187d1e002fc2aa5d8aa59729e1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exxos&#39;s gravatar image" />
<p><span>exxos</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exxos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '14, 23:58</strong> </span></p>
</div>
</div>
<div id="comments-container-32542" class="comments-container">
<span id="32544"></span>
<div id="comment-32544" class="comment">
<div id="post-32544-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While randomly browsing the nodes in that changeset, I actually stumbled upon one that I myself deleted 3 years ago! I don't have a clue where the data came from, but the one node in my area that I deleted was tagged as a bus stop, had a meaningless name ("079", which doesn't correspond to any kind of known ref around here) and was in a location where there isn't and has never been a bus stop. The fact that the changeset consists of many such nodes scattered across the continent makes the data very dubious. Since it's 3 years old, a full revert of the changeset is out of the question now. I think someone would have to review any nodes that haven't been modified since this changeset.</p>
<p>...and no, I'm not volunteering! :)</p>
</div>
<div id="comment-32544-info" class="comment-info">
<span class="comment-age">(22 Apr '14, 23:50)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-32542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32542-form-container" class="comment-form-container">
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

<span id="32561"></span>

<div id="answer-container-32561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32561-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is technically easy to run a script that deletes everything object from that changeset that has not been touched meanwhile. I would suggest that you discuss the matter on the <a href="http://lists.openstreetmap.org/listinfo/talk-us">talk-us mailinglist</a> where, if the community agrees that deleting is the best option, you'll also find people capable of running such a script.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '14, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32561" class="comments-container">
&#10;</div>
<div id="comment-tools-32561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32561-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32598"></span>

<div id="answer-container-32598" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32598-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Details of geocaches are subject to copyright, and should not be added to OSM. Any nodes that reveal the location or details of geocaches need to be deleted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '14, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-32598" class="comments-container">
<span id="32600"></span>
<div id="comment-32600" class="comment">
<div id="post-32600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you elaborate your statement? Geographic positions of objects are surely not copyrighted if they have been obtained via a valid source, e.g. surveyed on your own.</p>
</div>
<div id="comment-32600-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 14:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32605"></span>
<div id="comment-32605" class="comment">
<div id="post-32605-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The geocache listing pages on Geocaching.com are under the hider's copyright, but a set of coordinates can't be copyrighted. That being said, I just confirmed that the nodes starting with "GC" are indeed Geocaching.com geocaches, and these are definitely not things that need to be in OSM. It looks to me like sejohnson just got a bunch of miscellaneous waypoints from the web and uploaded them, many incorrectly tagged as bus stops, so I think the entire changeset is useless and any v1 nodes should be deleted.</p>
</div>
<div id="comment-32605-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 16:55)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="32609"></span>
<div id="comment-32609" class="comment">
<div id="post-32609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see, in that case you are absolutely right :)</p>
</div>
<div id="comment-32609-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 17:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32613"></span>
<div id="comment-32613" class="comment">
<div id="post-32613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>[In reply to Scai] If you discover a geocache by chance, probably nobody can stop you mapping its position and any details found at the location. However, data downloaded from Geocaching.com is subject to copyright.</p>
</div>
<div id="comment-32613-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 19:15)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="32614"></span>
<div id="comment-32614" class="comment">
<div id="post-32614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Of course, Madryn. But you didn't mention Geocaching.com anywhere. That's why I was a little bit surprised about your answer.</p>
</div>
<div id="comment-32614-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 20:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32618"></span>
<div id="comment-32618" class="comment not_top_scorer">
<div id="post-32618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I first saw that the caches were identified using their GC codes, I assumed that the codes must have been taken from geocaching.com. I later realised that they could be found by opening the cache and reading the log. One test would be whether the OSM locations match the geocaching.com locations; an exact match is unlikely given the accuracy of hand-held GPS receivers, so many exact matches might be taken as evidence of copying.</p>
</div>
<div id="comment-32618-info" class="comment-info">
<span class="comment-age">(24 Apr '14, 23:41)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="32620"></span>
<div id="comment-32620" class="comment not_top_scorer">
<div id="post-32620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The semantics of copyright law notwithstanding, the locations of geocaches tagged as highway=bus_stop add no value to OSM and should be removed. I might take a look at that changeset tonight and see if I can do so.</p>
</div>
<div id="comment-32620-info" class="comment-info">
<span class="comment-age">(25 Apr '14, 00:27)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-32598" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-32598-form-container" class="comment-form-container">
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

