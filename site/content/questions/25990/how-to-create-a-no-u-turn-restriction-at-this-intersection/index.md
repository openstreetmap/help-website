+++
type = "question"
title = "How to create a no-U turn restriction at this intersection?"
description = '''https://www.openstreetmap.org/edit?editor=potlatch2#map=19/38.85194/-77.34922 I have done a couple of restrictions but I am unable to do a No U-turn restriction here. Coming from the south heading north on Monument Drive, there is a no U-turn at Government Center Parkway intersection. Usually, when I...'''
date = "2013-08-31T03:54:00Z"
lastmod = "2013-09-02T02:42:00Z"
weight = 25990
keywords = [ "u-turn", "no", "restriction" ]
aliases = [ "/questions/25990" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a no-U turn restriction at this intersection?](/questions/25990/how-to-create-a-no-u-turn-restriction-at-this-intersection)

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
<span id="post-25990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/edit?editor=potlatch2#map=19/38.85194/-77.34922">https://www.openstreetmap.org/edit?editor=potlatch2#map=19/38.85194/-77.34922</a></p>
<p>I have done a couple of restrictions but I am unable to do a No U-turn restriction here. Coming from the south heading north on Monument Drive, there is a no U-turn at Government Center Parkway intersection.</p>
<p>Usually, when I do these restrictions, I get a list of the ways/streets in the drop-down menu (in Potlatch) but in this case, there are no ways/ streets showing at all. Any ideas? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-u-turn" rel="tag" title="see questions tagged &#39;u-turn&#39;">u-turn</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span> <span class="post-tag tag-link-restriction" rel="tag" title="see questions tagged &#39;restriction&#39;">restriction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '13, 03:54</strong></p>
<img src="https://secure.gravatar.com/avatar/06b9779157ed5d9958611cdc3b6aa4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slover98&#39;s gravatar image" />
<p><span>slover98</span><br />
<span class="score" title="567 reputation points">567</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slover98 has one accepted answer">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '13, 10:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-25990" class="comments-container">
&#10;</div>
<div id="comment-tools-25990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25990-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="26053"></span>

<div id="answer-container-26053" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26053-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok I tested quickly myself. You need to do this in the advanced mode of P2.</p>
<p>First remove the 2nd turn restriction and the via node in the first turn restriction. Then select the way segment that is currently has the "to" role in the 1st restriction and change that to "via". Once you have done that select the segment that should be the "to" way and click the "Add to" button. You will likely only have one possible selection, the turn restriction in question. Set the role to "to" for the way and you are done.</p>
<p>This is a bit more complicated than normal because of the unnecessary 2nd turn restriction, but is simpler than what the intstructions might look like.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '13, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-26053" class="comments-container">
&#10;</div>
<div id="comment-tools-26053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26053-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26060"></span>

<div id="answer-container-26060" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26060-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Based on the instruction given in one of the past posts, I did the no u-turn via 'way' not via 'node'. Basically followed these:</p>
<ol>
<li>Split ways inside the intersection as needed.</li>
<li>Ctrl-click (Command-click on Mac) one side of the road, the short section of the cross road to the left of it and the reverse side of the road.</li>
<li>Add all three to a new relationship.</li>
<li>Set relationship to Advanced-&gt;Turn restriction.</li>
<li>Set type to No U turns.</li>
<li>Click Members and set roles: to, via and from (have to type).</li>
</ol>
<p>Now all three ways has the proper designations under Restrictions, i.e. from, via, to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '13, 02:42</strong></p>
<img src="https://secure.gravatar.com/avatar/06b9779157ed5d9958611cdc3b6aa4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slover98&#39;s gravatar image" />
<p><span>slover98</span><br />
<span class="score" title="567 reputation points">567</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slover98 has one accepted answer">5%</span></p>
</div>
</div>
<div id="comments-container-26060" class="comments-container">
&#10;</div>
<div id="comment-tools-26060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26060-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26002"></span>

<div id="answer-container-26002" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26002-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that the issue is that you haven't split Monument Drive at the crossing yet.With the result that there are no appropriate road segments for Potlatch to display.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '13, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '13, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-26002" class="comments-container">
<span id="26005"></span>
<div id="comment-26005" class="comment">
<div id="post-26005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I used a wrong tool to split. I have now separated the segments, still cannot make it. WHich Intersection node should I pick (..9001)? Then I want to add the no U-turn restriction. From way ...1397 to ...6658. But 6658 does not show up in the drop down menu, only ..6653 which is a continuation of 6658. (BTW I have read: <a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/restrictions">https://wiki.openstreetmap.org/wiki/Potlatch_2/restrictions</a> but still am unable to make it work). Can you describe step by step how you do it in this case?</p>
</div>
<div id="comment-26005-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 11:00)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="26006"></span>
<div id="comment-26006" class="comment">
<div id="post-26006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>PS. I also read this but still cannot make it work: <a href="/questions/3530/what-is-the-proper-way-to-add-no-u-turn-restrictions-when-the-road-is-divided">https://help.openstreetmap.org/questions/3530/what-is-the-proper-way-to-add-no-u-turn-restrictions-when-the-road-is-divided</a></p>
</div>
<div id="comment-26006-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 11:08)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
<span id="26008"></span>
<div id="comment-26008" class="comment">
<div id="post-26008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>IMHO you've started correctly, in the end you should have</p>
<p>way 136291397 as from</p>
<p>way 235936651 as via</p>
<p>way 235936658 as to</p>
<p>I'm not particularly well versed to editing relations with P2 so somebody else might need to jump in here.</p>
</div>
<div id="comment-26008-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 12:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26002-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26010"></span>

<div id="answer-container-26010" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/no-u-turn_1.GIF" alt="alt text" /></p>
<p>I did the following. First I split the nodes. Then I created the first no u-turn node, where the red and short blue sections intersect. What helps is to select “Show” on the restriction menu so the map shows you which sections of the road are added to the restriction.</p>
<p>The I proceeded to the second node (upper left corner) and again created a no u-turn restriction.</p>
<p>Perhaps this is how it should be done(?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '13, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/06b9779157ed5d9958611cdc3b6aa4a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slover98&#39;s gravatar image" />
<p><span>slover98</span><br />
<span class="score" title="567 reputation points">567</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slover98 has one accepted answer">5%</span></p>
</img>
</div>
</div>
<div id="comments-container-26010" class="comments-container">
<span id="26015"></span>
<div id="comment-26015" class="comment">
<div id="post-26015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it is definitely ok to have a way as the via element, so doing it with two relations and two nodes, while probably having the same effect, is a very roundabout way of doing it.</p>
</div>
<div id="comment-26015-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 15:15)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="26016"></span>
<div id="comment-26016" class="comment">
<div id="post-26016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree, I just cannot figure out how to do the 'via' element.</p>
</div>
<div id="comment-26016-info" class="comment-info">
<span class="comment-age">(31 Aug '13, 15:19)</span> <span class="comment-user userinfo">slover98</span>
</div>
</div>
</div>
<div id="comment-tools-26010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26010-form-container" class="comment-form-container">
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

