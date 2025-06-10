+++
type = "question"
title = "Not enough characters for opening_hours"
description = '''I was just trying to enter the opening hours for an observation tower in Milan, but there is not enough space for the syntax. Do you know of any workaround or fix? Below is what I tried to enter: Tu 15:00-19:00,20:30-24:00; We 10:30-12:30,15:00-19:00,20:30-00:00; Th 15:00-19:00,20:30-00:00; Fr 15:00...'''
date = "2021-03-15T11:39:00Z"
lastmod = "2021-03-15T22:49:00Z"
weight = 79258
keywords = [ "opening_hours", "characters" ]
aliases = [ "/questions/79258" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Not enough characters for opening_hours](/questions/79258/not-enough-characters-for-opening_hours)

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
<span id="post-79258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79258-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was just trying to enter the opening hours for an <a href="https://www.openstreetmap.org/way/28099200">observation tower in Milan</a>, but there is not enough space for the syntax. Do you know of any workaround or fix? Below is what I tried to enter:</p>
<pre><code>Tu 15:00-19:00,20:30-24:00;
We 10:30-12:30,15:00-19:00,20:30-00:00;
Th 15:00-19:00,20:30-00:00;
Fr 15:00-19:00,20:30-00:00;
Sa 10:30-14:00,14:30-19:30,20:30-00:00;
Su 10:30-14:00,14:30-19:30,20:30-00:00;
Sep 16-May 14: Mo,Tu,Th,Fr off;
Sep 16-May 14: We 10:30-12:30,16:00-18:30;
Sep 16-May 14: Sa 10:30-13:00,15:00-18:30,20:30-00:00;
Sep 16-May 14: Su 10:30-14:00,14:30-19:00</code></pre>
<p>Note: If I don't add the months in front of each time period it will not work according to <a href="https://openingh.openstreetmap.de/evaluation_tool">https://openingh.openstreetmap.de/evaluation_tool</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-characters" rel="tag" title="see questions tagged &#39;characters&#39;">characters</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '21, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rene78 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '21, 11:45</strong> </span></p>
</div>
</div>
<div id="comments-container-79258" class="comments-container">
&#10;</div>
<div id="comment-tools-79258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79258-form-container" class="comment-form-container">
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

<span id="79261"></span>

<div id="answer-container-79261" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79261-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-79261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rene78 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Rows 1, 3 and 4 can be merged, just as 2, 5 and 6.</p>
<p>Further the colons after the date ranges are not necessary.</p>
<p>Note: there is no work around for OH strings that are longer than 255 characters.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '21, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '21, 11:55</strong> </span></p>
</div>
</div>
<div id="comments-container-79261" class="comments-container">
<span id="79265"></span>
<div id="comment-79265" class="comment">
<div id="post-79265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Simon! Haven't realized that they are similar. Even after this simplification the 255 chars limit is exceeded. I helped myself by merging row 8 and 10. Not ideal, since the opening hours are not the same on those days. Would be nice if it could be doubled to 512 (511) characters.</p>
</div>
<div id="comment-79265-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 12:01)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="79270"></span>
<div id="comment-79270" class="comment">
<div id="post-79270-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you can get under 255 when you reverse the order where to state the months/date ranges. Thus you avoid the off clause:</p>
<p>We 10:30-12:30,16:00-18:30;<br />
Sa 10:30-13:00,15:00-18:30,20:30-00:00;<br />
Su 10:30-14:00,14:30-19:00;<br />
May 15-Sep 15 Tu,Th,Fr 15:00-19:00,20:30-24:00;<br />
May 15-Sep 15 We 10:30-12:30,15:00-19:00,20:30-00:00;<br />
May 15-Sep 15 Sa,Su 10:30-14:00,14:30-19:30,20:30-00:00;</p>
<p>It's under 255 once you remove the line breaks.</p>
</div>
<div id="comment-79270-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 15:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79280"></span>
<div id="comment-79280" class="comment">
<div id="post-79280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great solution, thanks!</p>
</div>
<div id="comment-79280-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 22:49)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
</div>
<div id="comment-tools-79261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79261-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79260"></span>

<div id="answer-container-79260" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can merge the days with the same opening hours and use less characters, avoiding to state when the place is closed.</p>
<p><code>Tu 15:00-19:00,20:30-24:00; We 10:30-12:30,15:00-19:00,20:30-00:00; Th,Fr 15:00-19:00,20:30-00:00; Sa,Su 10:30-14:00,14:30-19:30,20:30-00:00; Sep 16-May 14 We 10:30-12:30,16:00-18:30; Sep 16-May 14 Sa 10:30-13:00,15:00-18:30,20:30-00:00; Sep 16-May 14 Su 10:30-14:00,14:30-19:00</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '21, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-79260" class="comments-container">
<span id="79262"></span>
<div id="comment-79262" class="comment">
<div id="post-79262-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But the place is closed in the winter months on Mo,Tu,Th and Fr. This is no longer covered in your syntax.</p>
</div>
<div id="comment-79262-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 11:58)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="79264"></span>
<div id="comment-79264" class="comment">
<div id="post-79264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If there are no opening_hours indicated, the app or database crawler reads it as closed, so there's no need to explicit it</p>
</div>
<div id="comment-79264-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 12:00)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
<span id="79266"></span>
<div id="comment-79266" class="comment">
<div id="post-79266-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmmm... at least openingh evaluation tool shows "Sep 16-May 14: Tu,Th,Fr" as open with your syntax.</p>
</div>
<div id="comment-79266-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 12:18)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="79267"></span>
<div id="comment-79267" class="comment">
<div id="post-79267-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Mannivu, you are mistaken here. The first couple of lines do show opening hours, so they need to be overridden by the off clauses. What you said would hold true if you added the months/day ranges also to the first couple of lines at the cost of inflating the whole statement again.</p>
</div>
<div id="comment-79267-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 14:33)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79269"></span>
<div id="comment-79269" class="comment not_top_scorer">
<div id="post-79269-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you are right. I forgot that the specific time range must explicit all differences.</p>
</div>
<div id="comment-79269-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 14:48)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
<span id="79271"></span>
<div id="comment-79271" class="comment">
<div id="post-79271-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What you suggested, removing the off clause, does indeed work when we reverse summer and winter. See my comment to Simon's answer.</p>
</div>
<div id="comment-79271-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 15:11)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-79260" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-79260-form-container" class="comment-form-container">
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

