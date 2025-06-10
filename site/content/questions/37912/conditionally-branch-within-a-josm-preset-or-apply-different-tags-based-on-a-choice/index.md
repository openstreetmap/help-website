+++
type = "question"
title = "Conditionally branch within a JOSM preset or apply different tags based on a choice"
description = '''Is there a way to conditionally branch within the preset or to apply different tags based on a choice, if this do that, else do this? I use a basic preset to tag bridges. I first break the highway in two places and then with the center segment selected, apply the preset which simply applies the tags...'''
date = "2014-10-24T03:49:00Z"
lastmod = "2014-10-25T01:32:00Z"
weight = 37912
keywords = [ "josm", "preset", "conditional" ]
aliases = [ "/questions/37912" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Conditionally branch within a JOSM preset or apply different tags based on a choice](/questions/37912/conditionally-branch-within-a-josm-preset-or-apply-different-tags-based-on-a-choice)

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
<span id="post-37912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37912-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to conditionally branch within the preset or to apply different tags based on a choice, if this do that, else do this? I use a basic preset to tag bridges. I first break the highway in two places and then with the center segment selected, apply the preset which simply applies the tags bridge=yes and layer=1. What I would like to be able to do is choose whether to apply the bridge tagging or instead, break a stream into sections and set tags to tunnel=culvert and layer=-1 on its center segment.</p>
<p>Thanks...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-preset" rel="tag" title="see questions tagged &#39;preset&#39;">preset</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '14, 03:49</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '14, 13:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37912" class="comments-container">
&#10;</div>
<div id="comment-tools-37912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37912-form-container" class="comment-form-container">
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

<span id="37923"></span>

<div id="answer-container-37923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37923-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand you correctly, you want to have the -same- preset apply different tags depending on the existing tags of the selected object.</p>
<p>It may be possible to do something with the "match" attribute to emulate the behavior you want, however I haven't tested it. The real place to look at is the relevant JOSM source code. Or maybe ask on the "editors" forum.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '14, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-37923" class="comments-container">
<span id="37949"></span>
<div id="comment-37949" class="comment">
<div id="post-37949-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Not quite. The applied tags would not depend on any existing tags. I want to combine two presets into one, sort of. Rather than having a separate preset for bridge and one for tunnel/ culvert, I would like a choice presented in the preset so that if I select "Bridge" it applies the bridge tags (bridge=yes and layer=1) and if I select Tunnel it applies the tags for tunnel=culvert and layer=-1</p>
</div>
<div id="comment-37949-info" class="comment-info">
<span class="comment-age">(25 Oct '14, 01:25)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37922"></span>

<div id="answer-container-37922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi AlaskaDave, are you building an automated editor ? Did you consider the use of the copy button (edit - nr. 3) in JOSM, it works fine as long as you stick to the same items. Start with the well equipped stations, copy and delete the unnecessary keys afterwards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '14, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-37922" class="comments-container">
<span id="37950"></span>
<div id="comment-37950" class="comment">
<div id="post-37950-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/4917/hendrik001">@Hendrik</a> - Not an automated editor but a single preset with some choices available, sort of the way you can create a drop-down list inside a preset. JOSM already has this sort of automatic tagging but you must work through three different menus (Presets&gt;Water&gt;Tunnel) to get to the one for tunnel, for example.</p>
<p>I know I can copy tags from an existing object (if one happens to be nearby) but I want to automate the process to suit my needs better.</p>
</div>
<div id="comment-37950-info" class="comment-info">
<span class="comment-age">(25 Oct '14, 01:32)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37922-form-container" class="comment-form-container">
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

