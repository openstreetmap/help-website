+++
type = "question"
title = "Transform two buildings to a single with two parts."
description = '''I&#x27;m trying to enhance an old import which created single houses as two building=yes ways:  One for the house itself. One for the entrance, which is covered but has no walls. This building=yes also have a wall=no.  I&#x27;m trying to convert both ways to building:part=yes, and draw a new path around them ...'''
date = "2019-04-01T22:15:00Z"
lastmod = "2019-04-02T16:57:00Z"
weight = 68593
keywords = [ "building", "josm", "building_part" ]
aliases = [ "/questions/68593" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Transform two buildings to a single with two parts.](/questions/68593/transform-two-buildings-to-a-single-with-two-parts)

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
<span id="post-68593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68593-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-68593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to enhance an old import which created single houses as two building=yes ways:</p>
<ul>
<li>One for the house itself.</li>
<li>One for the entrance, which is covered but has no walls. This building=yes also have a wall=no.</li>
</ul>
<p>I'm trying to convert both ways to building:part=yes, and draw a new path around them to hold the building=yes.</p>
<p>Using JOSM here what I can do:</p>
<ul>
<li>Select both ways</li>
<li>Copy (Ctrl-c)</li>
<li>Paste in place (Ctrl-Alt-v) (which select the new ones)</li>
<li>Shift-J to merge the pasted two ways</li>
<li>At this point I have tree ways: one merged and the two untouched initial ones</li>
<li>I change the building=yes to building:part=yes in the two old parts</li>
<li>The copy/past created duplicate nodes, so I select them by pairs and hit "M" to merge each pair</li>
</ul>
<p>It works well but It's way to long to cover the whole city :P</p>
<p>Is there a better/faster/less error prone way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-building_part" rel="tag" title="see questions tagged &#39;building_part&#39;">building_part</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '19, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d8798382aa64d5767d749a8328364e53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdk&#39;s gravatar image" />
<p><span>mdk</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '19, 22:15</strong> </span></p>
</div>
</div>
<div id="comments-container-68593" class="comments-container">
<span id="68612"></span>
<div id="comment-68612" class="comment">
<div id="post-68612-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Side note: If you know that a particular use of <a href="https://wiki.openstreetmap.org/wiki/Tag:wall%3Dno"><code>wall=no</code></a> describes a roof (rather than e.g. a balcony or shed), consider using <code>building:part=roof</code> for it. Because <code>wall=no</code> has been used for so many different things in the import, it's hard to make use of.</p>
</div>
<div id="comment-68612-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 15:02)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-68593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68593-form-container" class="comment-form-container">
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

<span id="68595"></span>

<div id="answer-container-68595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68595-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe <a href="https://josm.openstreetmap.de/wiki/Help/Action/FollowLine">"Follow Line"</a> is nicer? It still won't be great, but you start a line with it by clicking 2 existing nodes in order and then each time you press "F" it adds the next node, pausing for instruction on shared nodes. So you can create the outer way with ~3 clicks (2 to start it and 1 to continue it) and 2 presses of "F". No cut and paste, no merging, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 03:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '19, 03:36</strong> </span></p>
</div>
</div>
<div id="comments-container-68595" class="comments-container">
<span id="68601"></span>
<div id="comment-68601" class="comment">
<div id="post-68601-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's right, it's a bit better (it avoid merging which takes time).</p>
</div>
<div id="comment-68601-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 08:40)</span> <span class="comment-user userinfo">mdk</span>
</div>
</div>
</div>
<div id="comment-tools-68595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68595-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68616"></span>

<div id="answer-container-68616" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68616-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Instead of individually merging the nodes, you can use JOSM's validator. It shows error messages for duplicate building nodes, and can automatically fix them. When you select the heading in the JOSM validator panel (where it describes the kind of error) rather than one of the individual errors listed below it, clicking the Fix button will merge them all at once.</p>
<p><img src="https://help.openstreetmap.org/upfiles/JOSM_validator_fix_duplicate.png" alt="JOSM validator panel" /></p>
<p>That's quite nice already when used for a single building's nodes, but it can really save time if you do it only once at the end of your editing session. However, you <em>must</em> make sure that you do not "fix" anything except the building outlines you've just added!</p>
<p>Luckily, the validator runs only on the currently selected elements when clicking the Validation button. To select only the ways you've created or re-tagged in the current session, you can open JOSM's search (Ctrl-F) and enter the search string <code>type:way modified</code>.</p>
<p>Additional ideas:</p>
<ul>
<li>If there are any tags you need to add to or remove from all of your new building outlines (e.g. removing the <code>wall=no</code> that's left over from the merge), you can leave that until the end, too. Just select all the new building outlines by searching for <code>type:way new</code>.</li>
<li>You might be able to record and playback the Ctrl-c, Ctrl-Alt-v, Shift-J keypress sequence using some keyboard macro tool.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '19, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
</div>
<div id="comments-container-68616" class="comments-container">
&#10;</div>
<div id="comment-tools-68616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68616-form-container" class="comment-form-container">
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

