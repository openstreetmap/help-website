+++
type = "question"
title = "JOSM Validator - Can I use it to automatically merge duplicate nodes?"
description = '''Imagine that I&#x27;m trying to fix the duplicate tram stop nodes at Failsworth. In JOSM I can select &quot;download from OSM&quot; and can search for Failsworth, and download the area around it. Then if I select a small area around the tram stop and select &quot;validation&quot; I can see that 2 &quot;nodes at the same position...'''
date = "2013-09-17T16:20:00Z"
lastmod = "2015-10-20T16:10:00Z"
weight = 26439
keywords = [ "josm", "fix", "validator" ]
aliases = [ "/questions/26439" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM Validator - Can I use it to automatically merge duplicate nodes?](/questions/26439/josm-validator-can-i-use-it-to-automatically-merge-duplicate-nodes)

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
<span id="post-26439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26439-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imagine that I'm trying to fix the duplicate tram stop nodes at <a href="http://www.openstreetmap.org/browse/node/30877311">Failsworth</a>. In JOSM I can select "download from OSM" and can search for Failsworth, and download the area around it.</p>
<p>Then if I select a small area around the tram stop and select "validation" I can see that 2 "nodes at the same position",. I can then manually check the tags of each and see that the newer node is an identical copy of the older one, but with one (valid) extra tag, and not a member of the relations that it should be. I'd like to merge them (delete the newer node and add new tag to the older node).</p>
<p>The <a href="http://wiki.openstreetmap.org/wiki/JOSM/Validator">JOSM Validator</a> page suggests that it should be able to fix this automatically, but "Fix" for some reason is greyed out:</p>
<p><img src="http://help.openstreetmap.org/upfiles/josm_01006.png" alt="Fix greyed out in JOSM validator for duplicate nodes" /></p>
<p>Is there any reason for this?</p>
<p>(this is with the current stable JOSM of 6115)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '13, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Oct '15, 09:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-26439" class="comments-container">
<span id="26441"></span>
<div id="comment-26441" class="comment">
<div id="post-26441-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For the mentioned nodes this button is greyed out for me, too. But if I deliberately create such an error (e.g. pasting a node twice), the fix button is <em>not</em> greyed out and leads to both nodes being merged. Seems like a bug. josm-latest, 6232.</p>
</div>
<div id="comment-26441-info" class="comment-info">
<span class="comment-age">(17 Sep '13, 17:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="26566"></span>
<div id="comment-26566" class="comment">
<div id="post-26566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could it be that the tags are slightly different? Only one of the two nodes has the operator tag set.</p>
</div>
<div id="comment-26566-info" class="comment-info">
<span class="comment-age">(20 Sep '13, 16:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26439-form-container" class="comment-form-container">
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

<span id="26563"></span>

<div id="answer-container-26563" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26563-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should review each case and merge or separate the nodes according each node tags. In this case, the solution would be "merge".</p>
<p>In JOSM, click twice over the validator item ("2 nodes:..." in this case) then press the "3" key ("Zoom to Selection"), then the "M" key ("Merge nodes").</p>
<p>JOSM does not enable the "Fix" button if there is the possibility of more than one correct way to fix the problem reported.</p>
<p>This problem ("Nodes as same position") is very common when ways are accidentally unglued from each other. See, for example, my answer for the recent <a href="https://help.openstreetmap.org/questions/26515/ungrouping-separating-objects">question</a> on way/area ungrouping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '13, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-26563" class="comments-container">
<span id="26616"></span>
<div id="comment-26616" class="comment">
<div id="post-26616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not automatic (possibly for good reason), but it does solve the problem.</p>
</div>
<div id="comment-26616-info" class="comment-info">
<span class="comment-age">(22 Sep '13, 11:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46028"></span>
<div id="comment-46028" class="comment">
<div id="post-46028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This question is already answered. JOSM can not automatic fix the duplicated nodes if they have different tags and/or relation memberships. If you merge the nodes you will see a conflict window, where you need to choose the merging tags/memberships.</p>
<p>(Answer to <a href="http://forum.openstreetmap.org/viewtopic.php?pid=556248#p556248)">http://forum.openstreetmap.org/viewtopic.php?pid=556248#p556248)</a></p>
</div>
<div id="comment-46028-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 16:10)</span> <span class="comment-user userinfo">Klumbumbus</span>
</div>
</div>
</div>
<div id="comment-tools-26563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26563-form-container" class="comment-form-container">
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

