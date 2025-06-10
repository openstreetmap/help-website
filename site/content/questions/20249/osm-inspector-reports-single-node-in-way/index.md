+++
type = "question"
title = "OSM Inspector reports single node in way"
description = '''I was trying to kill some bugs today using OSM Inspector and came across several errors. They are in work I had done so I&#x27;m particularly interested in understanding what&#x27;s wrong and then fixing them. If someone with a little experience could take a look and help that process along, be my guest. Plea...'''
date = "2013-02-25T10:13:00Z"
lastmod = "2013-02-26T01:36:00Z"
weight = 20249
keywords = [ "single_node", "inspector", "errors", "osm" ]
aliases = [ "/questions/20249" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Inspector reports single node in way](/questions/20249/osm-inspector-reports-single-node-in-way)

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
<span id="post-20249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20249-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was trying to kill some bugs today using OSM Inspector and came across several errors. They are in work I had done so I'm particularly interested in understanding what's wrong and then fixing them.</p>
<p>If someone with a little experience could take a look and help that process along, be my guest.</p>
<p>Please have a look at Way: 200735915 marked as a "single-node in way" by OSM Inspector</p>
<p>Also, this one having the same error message: way_id: 71401599 node_id: 217690300</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-single_node" rel="tag" title="see questions tagged &#39;single_node&#39;">single_node</span> <span class="post-tag tag-link-inspector" rel="tag" title="see questions tagged &#39;inspector&#39;">inspector</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '13, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-20249" class="comments-container">
&#10;</div>
<div id="comment-tools-20249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20249-form-container" class="comment-form-container">
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

<span id="20250"></span>

<div id="answer-container-20250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can look specifically at individual ways on the main OSM site as follows:</p>
<ul>
<li><a href="http://www.openstreetmap.org/browse/way/71401599">http://www.openstreetmap.org/browse/way/71401599</a></li>
<li><a href="http://www.openstreetmap.org/browse/way/200735915">http://www.openstreetmap.org/browse/way/200735915</a></li>
</ul>
<p>Only the former appears to have a single node. This occurs from time to time (but rather rarely in my experience).</p>
<p>The solution is to use JOSM. There are options available in the search panel of JOSM which enable selection of individual ways by number, or ways with a specific number of nodes. Once the relevant ways have been found they can be deleted and removed from OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '13, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-20250" class="comments-container">
<span id="20258"></span>
<div id="comment-20258" class="comment">
<div id="post-20258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I could fix them if I could identify them. JOSM for all its power is not the easiest piece of s/w to use IMHO. It is powerful but to me, counter-intuitive.</p>
<p>I'll keep trying....</p>
</div>
<div id="comment-20258-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 11:36)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="20260"></span>
<div id="comment-20260" class="comment">
<div id="post-20260-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Er, another comment on JOSM. It has a Fix tool. I tried it and it worked, I think.</p>
</div>
<div id="comment-20260-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 11:56)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="20275"></span>
<div id="comment-20275" class="comment">
<div id="post-20275-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There's no particular need to use JOSM; you can delete single-node ways in Potlatch 2.</p>
<ul>
<li>Use the link from the way 'browse' page (as above) to open Potlatch 2 for that area. The way will be in the centre of the screen, though won't display.</li>
<li>Shift-drag to draw a box around the (non-displaying) way. The panel on the left will change to show the details of the way.</li>
<li>Use the 'delete' toolbar button, or press shift-Delete, to delete the way. Save.</li>
</ul>
</div>
<div id="comment-20275-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 17:18)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="20290"></span>
<div id="comment-20290" class="comment">
<div id="post-20290-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Richard</span>: Interesting - but holding shift while dragging simply drags the map in Potlatch2 as if I would not hold shift. Linux - if that matters.</p>
</div>
<div id="comment-20290-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 23:35)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="20292"></span>
<div id="comment-20292" class="comment">
<div id="post-20292-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FWIW on Windows it's control-drag to select in P2. If the node is part of other ways control-drag will select them too, but clicking on the node and pressing "/" will cycle through the ways until single-node one is selected, and you can then delete it.</p>
</div>
<div id="comment-20292-info" class="comment-info">
<span class="comment-age">(26 Feb '13, 01:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20250-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20254"></span>

<div id="answer-container-20254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20254-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are trac entries <a href="https://trac.openstreetmap.org/ticket/4378">4378</a> and <a href="https://trac.openstreetmap.org/ticket/3860">3380</a> that describes one possible route by which they might have been created (there are quite possibly also others).</p>
<p>In this case (where they've occurred in your mapping) you'll obviously check that any tags on these single node ways that should be applied to adjoining ways do get applied, so you're obviously the best person to fix them.</p>
<p>Sometimes, however, tools such as OSMI will draw your attention to issues such as single-node ways in other people's mapping. In that case I'd suggest that (if they're still actively mapping) you contact the original mapper so that they can (a) not create any more and (b) ensure that any tags on these single-node ways are applied to the ways that they really belong to. What I wouldn't do is just "correct" an error remotely as best as you can without the knowledge that the original mapper had.</p>
<p>Sometimes the fact that an error is flagged up by e.g. OSMI is a really useful indicator of somewhere that needs more surveying, or of a relatively new mapper that needs assistance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '13, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '13, 12:55</strong> </span></p>
</div>
</div>
<div id="comments-container-20254" class="comments-container">
<span id="20257"></span>
<div id="comment-20257" class="comment">
<div id="post-20257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I have looked at both of those errors until I'm seeing double but could not identify the "single node way". I removed and redrew the footbridge in way 200735915 and made sure to join the three footway segments again. That might work, we'll see.</p>
<p>I'm still confused about the other error. I have no idea where the single node way is. Should all those ways be <em>Joined</em> to the roundabout?</p>
</div>
<div id="comment-20257-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 11:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="20259"></span>
<div id="comment-20259" class="comment">
<div id="post-20259-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, got confused again. A different error in a different way. <a href="http://www.openstreetmap.org/edit?lat=18.799248&amp;lon=98.989957&amp;zoom=18">http://www.openstreetmap.org/edit?lat=18.799248&amp;lon=98.989957&amp;zoom=18</a></p>
<p>I guess I'll struggle with it for a bit longer. I'll come back for more help if I need it.</p>
<p>Thanks</p>
</div>
<div id="comment-20259-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 11:44)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-20254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20254-form-container" class="comment-form-container">
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

