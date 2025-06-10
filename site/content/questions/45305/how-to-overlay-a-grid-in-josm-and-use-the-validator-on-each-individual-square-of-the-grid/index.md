+++
type = "question"
title = "How to overlay a grid in JOSM and use the Validator on each individual square of the grid?"
description = '''Firstly I need to overlay a grid in JOSM. The grid should be 1,5 km^2 per square and should cover the data layer in JOSM. Secondly I need to run the built in validator for each square on the grid, presenting me with the number of errors for each grid square. Thirdly I need to export the information ...'''
date = "2015-09-16T21:38:00Z"
lastmod = "2021-08-11T15:00:00Z"
weight = 45305
keywords = [ "josm", "validator", "grid" ]
aliases = [ "/questions/45305" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to overlay a grid in JOSM and use the Validator on each individual square of the grid?](/questions/45305/how-to-overlay-a-grid-in-josm-and-use-the-validator-on-each-individual-square-of-the-grid)

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
<span id="post-45305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Firstly I need to overlay a grid in JOSM. The grid should be 1,5 km^2 per square and should cover the data layer in JOSM.</p>
<p>Secondly I need to run the built in validator for each square on the grid, presenting me with the number of errors for each grid square.</p>
<p>Thirdly I need to export the information into Excel to process the data. Something like square 1 has 3 errors for 'unnamed ways', square 2 has 6 errors for 'unnamed ways', etc.</p>
<p>How can this be achieved?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span> <span class="post-tag tag-link-grid" rel="tag" title="see questions tagged &#39;grid&#39;">grid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '15, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/19fd6c1499513907697c5821829c5e83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BmanS&#39;s gravatar image" />
<p><span>BmanS</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BmanS has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '15, 05:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45305" class="comments-container">
&#10;</div>
<div id="comment-tools-45305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45305-form-container" class="comment-form-container">
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

<span id="45309"></span>

<div id="answer-container-45309" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45309-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is definitely not achievable without some programming and some modifications to JOSM.</p>
<p>You will have to split the data into squares first, using e.g. osmconvert, osmosis, or osm-history-splitter, and you will have to write a small program that computes the grid and executes one of these programs to achieve the splitting.</p>
<p>After that, your choices are either to modify JOSM so that it can run the validator from the command line and output results as CSV or similar, or you could drop JOSM altogether and use the open-sourced check utilities KeepRight or Osmose which might be more amenable to such a modification than JOSM which is geared towards interactive editing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '15, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '15, 22:34</strong> </span></p>
</div>
</div>
<div id="comments-container-45309" class="comments-container">
<span id="45322"></span>
<div id="comment-45322" class="comment">
<div id="post-45322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I expected some programming.</p>
<p>How do I do all that? Or where can I read up and learn how to do it?</p>
<p>I already modified the JOSM validator to search for specific things I am interested in which I could not do with the other validation tools. So I have the validator tool already set up. However now I need to split the data into grids and have the validator validate one grid at a time. How can I split the data with osmconvert, osmosis or osm-history-splitter and then write that program?</p>
</div>
<div id="comment-45322-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 08:13)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="45325"></span>
<div id="comment-45325" class="comment">
<div id="post-45325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An easy way to programatically download squares is to use the <a href="http://josm.openstreetmap.de/wiki/Help/Preferences/RemoteControl">remote control</a>.</p>
<p>That doesn't help you with the validatetion process, but if you've started modifying the validator code already you could try to register a remotecontrol handler for the validator that returns the errors in a parseable format. That actually sounds like a useful feature, consider upstreaming it if you implement it.</p>
</div>
<div id="comment-45325-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 10:10)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45309-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81279"></span>

<div id="answer-container-81279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81279-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can make a simple grid by drawing ways on separate layer and set the ways to for example motor ways. Then set both the grid layer and your working layer to visible, and the grid is shown in the working layer as black lines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '21, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81279" class="comments-container">
&#10;</div>
<div id="comment-tools-81279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81279-form-container" class="comment-form-container">
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

