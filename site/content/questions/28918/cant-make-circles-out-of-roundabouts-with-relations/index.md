+++
type = "question"
title = "Can&#x27;t make circles out of roundabouts with relations"
description = '''iD&#x27;s &#x27;transform to circle&#x27; tool is pretty nice to tweak roundabouts which were previously uneven or had too few nodes. However this doesn&#x27;t work if the roundabout consists of several ways due to parts of it being part of different relations. is there a workaround?'''
date = "2013-12-09T13:27:00Z"
lastmod = "2013-12-16T15:15:00Z"
weight = 28918
keywords = [ "ideditor", "circle" ]
aliases = [ "/questions/28918" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can't make circles out of roundabouts with relations](/questions/28918/cant-make-circles-out-of-roundabouts-with-relations)

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
<span id="post-28918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28918-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>iD's 'transform to circle' tool is pretty nice to tweak roundabouts which were previously uneven or had too few nodes. However this doesn't work if the roundabout consists of several ways due to parts of it being part of different relations.</p>
<p>is there a workaround?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-circle" rel="tag" title="see questions tagged &#39;circle&#39;">circle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Dec '13, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a8321f837a9ab1d2ce145b53a4ce7272?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexanderW&#39;s gravatar image" />
<p><span>alexanderW</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexanderW has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '13, 14:22</strong> </span></p>
</div>
</div>
<div id="comments-container-28918" class="comments-container">
&#10;</div>
<div id="comment-tools-28918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28918-form-container" class="comment-form-container">
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

<span id="28921"></span>

<div id="answer-container-28921" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28921-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexanderW has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could make a new helper-way which uses all the roundabout's nodes and make this way a circle. Then delete the helper-way again. However, not that easy to do. I would not recommend to do this with iD.</p>
<p>iD seems not to allow multi-selecting individual nodes of different ways. I could not get it done in Potlatch 2, too. It does work in JOSM (although I think it does not have a function to insert more nodes into a circle, still making a circle of your existing nodes would work). However, you need to be careful about the positions of the nodes - they may represent in- and out- connections. So, likely this is also no good option.</p>
<p>All in all: do it careful and rather manually. You can overlay another (new) helper-way which is a perfect circle to have a template for manual node insertions and movements. Remember to delete your new helper-way before saving.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '13, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '13, 14:29</strong> </span></p>
</div>
</div>
<div id="comments-container-28921" class="comments-container">
<span id="29041"></span>
<div id="comment-29041" class="comment">
<div id="post-29041-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Using JOSM if there are enough nodes, I would not use the helper way, but simply select all the ways that are part of the roundabout, &lt;control&gt;+&lt;shift&gt;+N (using Windows, MacOS may use a different modifier) to select all of the nodes belonging to them, and then "O" (to align the nodes in a circle)</p>
</div>
<div id="comment-29041-info" class="comment-info">
<span class="comment-age">(13 Dec '13, 18:08)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="29111"></span>
<div id="comment-29111" class="comment">
<div id="post-29111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no objective reasons to split roundabouts for relations.</p>
</div>
<div id="comment-29111-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 12:22)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29114"></span>
<div id="comment-29114" class="comment">
<div id="post-29114-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@Pieren</span>, this is not a policy discussion/vote here (also you should not downvote my answer just because this is a not a kind of mapping you like – at least it seems to me like you did therefore). Also note that I did not recommend to split. The split roundabout is the current state of the data.</p>
</div>
<div id="comment-29114-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 13:41)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="29119"></span>
<div id="comment-29119" class="comment">
<div id="post-29119-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Pieren</span>: regarding the issue itself: there are objective "pro" reasons (which you are likely ignoring). Just one: If you use your inflated-node roundabout in a route relation you get a wrong route length.</p>
</div>
<div id="comment-29119-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 14:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="29121"></span>
<div id="comment-29121" class="comment">
<div id="post-29121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span>: once you know that the route relation contains full roundabouts, it's easy to compute the correct length. Again, my advice is the best workaround : don't split roundabouts for routes.</p>
</div>
<div id="comment-29121-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 15:07)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29123"></span>
<div id="comment-29123" class="comment not_top_scorer">
<div id="post-29123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Pieren</span>: sure, there are ways to get the correct length (estimation by leaving away half of a roundabout length or even primitive routing through roundabounts). All of this require additional processing which may be not a good thing. And just because there are workarounds it does not mean that there are no "pro" reasons as you claimed.</p>
</div>
<div id="comment-29123-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 15:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28921" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-28921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28919"></span>

<div id="answer-container-28919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not directly answering your question but in my country, we tend to not split roundabouts for route relations. In routing, we consider a roundabout like an intersection node (it's just an inflated node ;-). The question still exists when e.g. part of the roundabout is a bridge but it's much less common than route relations.<br />
The only method I know in this case - if the editor does not support "rounding multiple selected lines" - is to merge the lines, make the polygon circular and split again. Easy for a bridge, painfull for route relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '13, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-28919" class="comments-container">
<span id="28920"></span>
<div id="comment-28920" class="comment">
<div id="post-28920-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>This is a very error-prone suggestion :(. Please don't do this unless you are very familiar with relations. And even then it is better to use an editor which doesn't have this shortcoming.</p>
</div>
<div id="comment-28920-info" class="comment-info">
<span class="comment-age">(09 Dec '13, 14:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28923"></span>
<div id="comment-28923" class="comment">
<div id="post-28923-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Spliting a roundabout for route relations IS very error-prone. My first advice is to not do this. If the way is split for other reasons like a bridge, it has nothing to do with relations and is therefore easy to follow and maintain during the merge and re-split (simple tags on simple ways).</p>
</div>
<div id="comment-28923-info" class="comment-info">
<span class="comment-age">(09 Dec '13, 15:50)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-28919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28919-form-container" class="comment-form-container">
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

