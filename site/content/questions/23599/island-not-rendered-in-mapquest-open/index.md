+++
type = "question"
title = "Island not rendered in MapQuest Open"
description = '''An island is mapped in the lake Klausensee near Schwandorf since 2008 but not shown in MapQuest Open? I compared it with a working sample (rendered in Standard and MapQuest Open) but can&#x27;t find the reason for the problem (rendered in Standard but not in MapQuest Open). Can someone else please check ...'''
date = "2013-06-22T11:57:00Z"
lastmod = "2013-06-22T13:48:00Z"
weight = 23599
keywords = [ "islands" ]
aliases = [ "/questions/23599" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Island not rendered in MapQuest Open](/questions/23599/island-not-rendered-in-mapquest-open)

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
<span id="post-23599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23599-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An island is mapped in the lake Klausensee near Schwandorf since 2008 but not shown in MapQuest Open? I compared it with a working sample (rendered in <a href="http://www.openstreetmap.org/?lat=49.275405&amp;lon=12.164303&amp;zoom=18&amp;layers=M">Standard</a> and <a href="http://www.openstreetmap.org/?lat=49.275405&amp;lon=12.164303&amp;zoom=18&amp;layers=Q">MapQuest Open</a>) but can't find the reason for the problem (rendered in <a href="http://www.openstreetmap.org/?lat=49.29351&amp;lon=12.108497&amp;zoom=18&amp;layers=M">Standard</a> but not in <strong><a href="http://www.openstreetmap.org/?lat=49.29351&amp;lon=12.108497&amp;zoom=18&amp;layers=Q">MapQuest Open</a></strong>). Can someone else please check it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '13, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3aba61e89f5860ef126f32fd6596d4d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ares72&#39;s gravatar image" />
<p><span>ares72</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ares72 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23599" class="comments-container">
&#10;</div>
<div id="comment-tools-23599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23599-form-container" class="comment-form-container">
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

<span id="23600"></span>

<div id="answer-container-23600" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23600-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ares72 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The difference is the tagging of the lakes:</p>
<ul>
<li><a href="http://www.openstreetmap.org/browse/relation/1856664">http://www.openstreetmap.org/browse/relation/1856664</a> (talking of <a href="http://www.openstreetmap.org/browse/relation/1856664/history">version 2</a>) natural = water tagged on the relation</li>
<li><a href="http://www.openstreetmap.org/browse/relation/58085">http://www.openstreetmap.org/browse/relation/58085</a> (talking of <a href="http://www.openstreetmap.org/browse/relation/58085/history">version 1</a>) natural = water tagged on the outer way</li>
</ul>
<p>The water in the second example is does not have inner holes - as it is tagged to the whole way.</p>
<p>See <span>How to create islands in lakes in the wiki</span>.</p>
<p>So, the natural=water and name tags should be moved from the outer way to the relation. Then it is correct. And it will likely also render in MapquestOpen (after it updated, which can take some days(?)).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '13, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '13, 13:04</strong> </span></p>
</div>
</div>
<div id="comments-container-23600" class="comments-container">
<span id="23604"></span>
<div id="comment-23604" class="comment">
<div id="post-23604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I moved the tags from the outer way to the relation. Thank you for checking the problem.</p>
</div>
<div id="comment-23604-info" class="comment-info">
<span class="comment-age">(22 Jun '13, 13:48)</span> <span class="comment-user userinfo">ares72</span>
</div>
</div>
</div>
<div id="comment-tools-23600" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23600-form-container" class="comment-form-container">
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

