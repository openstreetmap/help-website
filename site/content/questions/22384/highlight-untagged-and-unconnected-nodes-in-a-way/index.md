+++
type = "question"
title = "Highlight untagged and unconnected nodes in a way"
description = '''While editing some cities I see a lot of unneeded/excessive nodes. For example, here:  See that the street is straight and the left middle node is unneeded. I found question 8348 but I just can&#x27;t select everything and simplify (it can remove valid nodes or just can&#x27;t remove the node (caused by too h...'''
date = "2013-05-13T15:29:00Z"
lastmod = "2013-05-25T00:32:00Z"
weight = 22384
keywords = [ "highlight", "nodes", "excessive", "unneeded", "remove" ]
aliases = [ "/questions/22384" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Highlight untagged and unconnected nodes in a way](/questions/22384/highlight-untagged-and-unconnected-nodes-in-a-way)

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
<span id="post-22384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22384-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While editing some cities I see a lot of unneeded/excessive nodes. For example, here:</p>
<p><img src="http://i.imgur.com/wk4jMHc.png" alt="Unneeded node" /></p>
<p>See that the street is straight and the left middle node is unneeded. I found <a href="/questions/8348/is-there-an-efficient-way-to-delete-excessiveredundant-nodes">question 8348</a> but I just can't select everything and simplify (it can remove valid nodes or just can't remove the node (caused by too high or too low max-error value)) nor I can select everything and straight them too.</p>
<p>While looking at the data with a lower zoom level it's also difficult to spot this small square in JOSM.</p>
<p>Another example:</p>
<p><img src="http://i.imgur.com/9IC9H6r.png" alt="Nodes" /></p>
<p>And the nodes that probably aren't needed:</p>
<p><img src="http://i.imgur.com/7ZRBhjk.png" alt="Unneeded nodes 2" /></p>
<p>So my problem is: is it possible to highlight these kind of nodes in JOSM, please? (nodes that are part of a way, have no tags nor are connected to anything else (another ways, for example)). Something to display them with a big icon and/or color, like this:</p>
<p><img src="http://i.imgur.com/QF4jjQv.png" alt="Highleted" /></p>
<p>There is no problem that it's an ugly view but I need a quick way to view these possible spurious nodes (so I can then review them manually and remove if needed).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highlight" rel="tag" title="see questions tagged &#39;highlight&#39;">highlight</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-excessive" rel="tag" title="see questions tagged &#39;excessive&#39;">excessive</span> <span class="post-tag tag-link-unneeded" rel="tag" title="see questions tagged &#39;unneeded&#39;">unneeded</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '13, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c605758904cf00f577053e4e130f89a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naoliv&#39;s gravatar image" />
<p><span>naoliv</span><br />
<span class="score" title="600 reputation points">600</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naoliv has 3 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '13, 02:58</strong> </span></p>
</div>
</div>
<div id="comments-container-22384" class="comments-container">
<span id="22465"></span>
<div id="comment-22465" class="comment">
<div id="post-22465-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Not every untagged node which is not connected to more than one road is unneeded. In fact, except for the Tiger import and some bad GPX-trace-to-OSM-way conversions most of these nodes are really useful. Besides there is no way to automagically decide whether such a node is unneeded or not.</p>
</div>
<div id="comment-22465-info" class="comment-info">
<span class="comment-age">(16 May '13, 07:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22471"></span>
<div id="comment-22471" class="comment">
<div id="post-22471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I know. This is exactly why I need only to highlight the nodes and not an automated process to remove them. By highlight the nodes I can review them manually.</p>
</div>
<div id="comment-22471-info" class="comment-info">
<span class="comment-age">(16 May '13, 11:45)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
<span id="22472"></span>
<div id="comment-22472" class="comment">
<div id="post-22472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Although <a href="https://wiki.openstreetmap.org/wiki/JOSM/Search_function">JOSM's search function</a> is very powerful it doesn't seem to support all of your constraints.</p>
</div>
<div id="comment-22472-info" class="comment-info">
<span class="comment-age">(16 May '13, 12:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22473"></span>
<div id="comment-22473" class="comment not_top_scorer">
<div id="post-22473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can some kind of custom map style/MapCSS be created for this?</p>
</div>
<div id="comment-22473-info" class="comment-info">
<span class="comment-age">(16 May '13, 12:10)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
<span id="22474"></span>
<div id="comment-22474" class="comment">
<div id="post-22474-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not familiar with MapCSS but I guess it is possible given the already different style of single and multiple connected nodes. Still I wouldn't worry too much about them. Removing them is probably not worth the effort. But if you create such a style then publishing it doesn't harm, too :).</p>
</div>
<div id="comment-22474-info" class="comment-info">
<span class="comment-age">(16 May '13, 12:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22495"></span>
<div id="comment-22495" class="comment not_top_scorer">
<div id="post-22495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, edited the initial question to give a better explanation. I don't need an automated tool to simplify nor nothing. I just want to have the middle nodes somehow highlighted.</p>
</div>
<div id="comment-22495-info" class="comment-info">
<span class="comment-age">(17 May '13, 02:57)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
<span id="22539"></span>
<div id="comment-22539" class="comment">
<div id="post-22539-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think this condition is needed: highlight NodeA if it</p>
<ul>
<li>is member of exactly one way AND</li>
<li>is not a member of a relation AND</li>
<li>has no tags AND</li>
<li>has a node before (A-1) and after (A+1) in the way AND</li>
<li>the absolute difference of (angle to North of the line between NodeA-1 and NodeA the angle to North of the line between NodeA and NodeA+1) is &lt;= $threshold</li>
</ul>
<p>$threshold may be 0 or 0.001 or something (depends on personal taste).</p>
</div>
<div id="comment-22539-info" class="comment-info">
<span class="comment-age">(18 May '13, 12:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22384" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22384-form-container" class="comment-form-container">
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

<span id="22650"></span>

<div id="answer-container-22650" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22650-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-22650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Answering my own question, I did create a <span>MapCSS</span> style:</p>
<hr />
<pre><code>way[highway] &gt; node {
  symbol-size:10;
  symbol-shape: square;
  symbol-stroke-color: #00ffff;
  symbol-fill-color: blue;
}
&#10;node:connection, node:tagged {
  symbol-size:5;
  symbol-fill-color: #808080;
  symbol-stroke-color: #808080;
}</code></pre>
<hr />
<p>The first block will highlight with a blue square every node that is part of a way tagged with highway=* (even nodes that are tagged or connected to other ways, but they are handled after).</p>
<p>Second block will make nodes that are connected to other ways (<em>node:connection</em>) or nodes that have any tags (<em>node:tagged</em>) have a gray color and a smaller size (to stay less noticeable in JOSM).</p>
<p>This:</p>
<p><img src="http://i.imgur.com/sLdZoCy.png" alt="Original" /></p>
<p>Is now seen as this with the style:</p>
<p><img src="http://i.imgur.com/xUfXQsi.png" alt="Highlighted" /></p>
<p>Like aseerel4c26 suggested, missing features are:</p>
<ul>
<li>Ignore initial/final nodes of the way</li>
<li>Ignore highways that are also part of a relation</li>
<li>Highlight only nodes within a certain angle threshold (so real curved ways could be ignored)</li>
</ul>
<p>It is perfectly fitting my needs but any kind of suggestion/improvements are welcome.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '13, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c605758904cf00f577053e4e130f89a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naoliv&#39;s gravatar image" />
<p><span>naoliv</span><br />
<span class="score" title="600 reputation points">600</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naoliv has 3 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '13, 00:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-22650" class="comments-container">
<span id="22652"></span>
<div id="comment-22652" class="comment">
<div id="post-22652-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for sharing!</p>
<p>And for those wondering what to do with the junk above... Use a text editor, paste the code, and save it as foo.css (or similar) anywhere. Then add the file path to JOSM in Edit/Preferences/Map Settings/Map Paint Styles.</p>
<p>I've used JOSM for years, but apparently there are still many things to find out. :)</p>
</div>
<div id="comment-22652-info" class="comment-info">
<span class="comment-age">(22 May '13, 21:39)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="22659"></span>
<div id="comment-22659" class="comment">
<div id="post-22659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very good, naoliv! For other who don't understand the CSS syntax that good, could you mention (please add it with the "edit" function) what the rule does? It is not as restrictive in highlighting as my suggested conditions (yes, those are not useful as they are, practically) are, right?</p>
</div>
<div id="comment-22659-info" class="comment-info">
<span class="comment-age">(22 May '13, 23:21)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="22745"></span>
<div id="comment-22745" class="comment">
<div id="post-22745-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>aseerel4c26, I did edit it like you suggested. And as you said, it doesn't implement all the rules from your other comment (but as it is now, it's perfectly fitting my needs). Thanks!</p>
</div>
<div id="comment-22745-info" class="comment-info">
<span class="comment-age">(24 May '13, 20:30)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
<span id="22750"></span>
<div id="comment-22750" class="comment">
<div id="post-22750-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks again, <span>ment</span><span>ioned</span> in the relevant (hopefully) wiki pages.</p>
</div>
<div id="comment-22750-info" class="comment-info">
<span class="comment-age">(25 May '13, 00:32)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22650-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22537"></span>

<div id="answer-container-22537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22537-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In your private data version you can remove (or do whatever you want with) these "unneeded" points. But, please, be careful doing similar changes to the OSM source data. There may be some, to us unknown, reasons for uploading these "unneeded"/redundant points by local editors. Besides, the cases you refer to are just a little fraction of the redundant node cases. The node redundancy comes from point replications, colinear (and almost colinear) neighbouring vector/line-segments, cases like ...A,B,C,B,C...C,D..., overlapping (or almost overlapping) ways/polylines in the same or different object classes and so on. The number of "unneeded" nodes in a Planet dump may easily exceed 10**8 (hundred million).</p>
<p>So, my suggestion is, do not worry about these "unneeded" points in the OSM source data. In raster mapping (rendered/pre-rasterized map images on servers) you will never see them. In vector mapping (rendering/rasterization on the clients, parametric data transmission) mappers will remove this redundancy anyway especially in mobile mapping (simply, it is too expensive to transmit them in cellular networks).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '13, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</img>
</div>
</div>
<div id="comments-container-22537" class="comments-container">
<span id="22541"></span>
<div id="comment-22541" class="comment">
<div id="post-22541-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sorry if I look rude here (it's really not the intention) but I know what I am doing. In no way I am going to destroy data (and exactly because of this I don't want to use any kind of automated process to remove the nodes). Like I said before, I just need help in highlighting these nodes.</p>
<p>The majority of the cases that I see in my area are nodes created by new users.</p>
<p>If I am doing some QA work or updating an area, I see no problem in also removing spurious nodes.</p>
</div>
<div id="comment-22541-info" class="comment-info">
<span class="comment-age">(18 May '13, 14:25)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
</div>
<div id="comment-tools-22537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22537-form-container" class="comment-form-container">
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

