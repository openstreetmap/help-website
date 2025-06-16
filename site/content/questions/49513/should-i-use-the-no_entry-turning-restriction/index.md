+++
type = "question"
title = "Should I use the no_entry turning restriction?"
description = '''Hi all, I recently added some turn restrictions. All seem fine apart from https://www.openstreetmap.org/relation/6168859 a restriction=no_entry relation. Although documented in the wiki (which I was following), none of the common routers seem to understand it. Have I made a mistake somewhere or is it...'''
date = "2016-04-30T14:40:00Z"
lastmod = "2016-04-30T16:44:00Z"
weight = 49513
keywords = [ "turn_restrictions", "no_entry", "routing" ]
aliases = [ "/questions/49513" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should I use the no_entry turning restriction?](/questions/49513/should-i-use-the-no_entry-turning-restriction)

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
<span id="post-49513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49513-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I recently added some turn restrictions. All seem fine apart from <a href="https://www.openstreetmap.org/relation/6168859">https://www.openstreetmap.org/relation/6168859</a> a restriction=no_entry relation. Although documented in the wiki (which I was following), none of the common routers seem to understand it. Have I made a mistake somewhere or is it just not recognised by routing software? Am I better off replacing it with no left/right turn relations? Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-no_entry" rel="tag" title="see questions tagged &#39;no_entry&#39;">no_entry</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '16, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9a1511893dc5b1c9588ada881244c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ACS1986&#39;s gravatar image" />
<p><span>ACS1986</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ACS1986 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49513" class="comments-container">
&#10;</div>
<div id="comment-tools-49513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49513-form-container" class="comment-form-container">
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

<span id="49514"></span>

<div id="answer-container-49514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to you relation Union Street is effectively a oneway street, isn't it? In that case a <a href="https://wiki.openstreetmap.org/wiki/Key:oneway">oneway tag</a> is enough, no relations are required.</p>
<p>Apart from that, your relation seems to be correct. First I thought it contains an error because there are two members with the role <em>from.</em> But according to the <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restriction wiki page</a> <em>no_entry</em> suports multiple <em>from</em>-members.</p>
<p>However it is quite likely that most routers don't support this relation since it is not very common.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '16, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49514" class="comments-container">
<span id="49515"></span>
<div id="comment-49515" class="comment">
<div id="post-49515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. It's effectively one way for through traffic, yes, but it isn't signed as a one way street (ie. traffic already on the street can legally travel in either direction). I was unsure about how best to map this and the no_entry relation mentioned in the Wiki seemed like the most accurate. Would using left/right turn restrictions or mapping it as if it were a oneway street be better?</p>
</div>
<div id="comment-49515-info" class="comment-info">
<span class="comment-age">(30 Apr '16, 16:02)</span> <span class="comment-user userinfo">ACS1986</span>
</div>
</div>
<span id="49516"></span>
<div id="comment-49516" class="comment">
<div id="post-49516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Personally I would map it as a oneway street. Either by adding the oneway tag to the whole street if it applies to the whole street, or just to a short part right before Friagate if this does better reflect reality.</p>
<p>Also keep in mind that most routers will take a couple of days until having updated their data.</p>
</div>
<div id="comment-49516-info" class="comment-info">
<span class="comment-age">(30 Apr '16, 16:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49518"></span>
<div id="comment-49518" class="comment">
<div id="post-49518-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I did leave it a few days before checking how the routers behaved. The other turn restrictions I did at the same time now route correctly. In view of your advice I'll tag a short part as one way as that seems preferable. Thanks.</p>
</div>
<div id="comment-49518-info" class="comment-info">
<span class="comment-age">(30 Apr '16, 16:44)</span> <span class="comment-user userinfo">ACS1986</span>
</div>
</div>
</div>
<div id="comment-tools-49514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49514-form-container" class="comment-form-container">
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

