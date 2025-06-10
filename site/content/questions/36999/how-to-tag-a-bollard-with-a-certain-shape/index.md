+++
type = "question"
title = "How to tag a bollard with a certain shape ?"
description = '''A lot of bollards are pillar / pole shaped. But there are a lot of different kind of shapes for instance pyramid shaped or so called pig shape concrete obstacles. How to tag these different kind shaped bollards ? Specific or just bollard ?'''
date = "2014-09-23T09:12:00Z"
lastmod = "2014-09-23T21:16:00Z"
weight = 36999
keywords = [ "pyramide", "pillar", "pigshape", "obstacle", "bollard" ]
aliases = [ "/questions/36999" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a bollard with a certain shape ?](/questions/36999/how-to-tag-a-bollard-with-a-certain-shape)

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
<span id="post-36999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A lot of bollards are pillar / pole shaped. But there are a lot of different kind of shapes for instance pyramid shaped or so called pig shape concrete obstacles. How to tag these different kind shaped bollards ? Specific or just bollard ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pyramide" rel="tag" title="see questions tagged &#39;pyramide&#39;">pyramide</span> <span class="post-tag tag-link-pillar" rel="tag" title="see questions tagged &#39;pillar&#39;">pillar</span> <span class="post-tag tag-link-pigshape" rel="tag" title="see questions tagged &#39;pigshape&#39;">pigshape</span> <span class="post-tag tag-link-obstacle" rel="tag" title="see questions tagged &#39;obstacle&#39;">obstacle</span> <span class="post-tag tag-link-bollard" rel="tag" title="see questions tagged &#39;bollard&#39;">bollard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '14, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-36999" class="comments-container">
&#10;</div>
<div id="comment-tools-36999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36999-form-container" class="comment-form-container">
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

<span id="37000"></span>

<div id="answer-container-37000" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37000-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tag "barrier=bollard" has already a sub-key called "bollard=*" <a href="http://wiki.openstreetmap.org/wiki/Key:bollard">documented on the wiki</a>.<br />
At the moment, only two values have been specified "rising" and "removable". You can also use the tool "taginfo" to check the <a href="http://taginfo.openstreetmap.org/keys/?key=bollard#values">current list of values set by the contributors</a>. As you can see, some values are inconsistent with the current documentation like "wood" which does not say if it is "removable" or "rising" or not.</p>
<p>I guess the best would be to split the current sub-tag in 3 sub-tags : one saying if the bollard is removable or not, one describing the shape (pole, pyramid, etc) and one describing the material (wood, stone, etc).</p>
<p>I would suggest to keep the current "bollard=<em>" for "removable" (for the ~3000 tags already in use) and reuse the existing "<a href="http://wiki.openstreetmap.org/wiki/Key:material">material</a>=</em>" tag for wood, stone, etc.</p>
<p>Then propose something new for the shape e.g. "bollard:shape=pole | ball | pyramid | etc". But you should submit a formal proposal on the wiki first then call for comments on the <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging mailing list (subscription required)</a> (<a href="https://lists.openstreetmap.org/pipermail/tagging/">archives</a>). The <a href="http://wiki.openstreetmap.org/wiki/Proposal_process">full process of approving a new tag</a> is not really required here since you just go at a very low level of details.</p>
<p>You could also use the new tag directly with your favorite editor. But formalising your tag proposal on the wiki increases its chance to be reused by others.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '14, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '14, 17:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-37000" class="comments-container">
<span id="37010"></span>
<div id="comment-37010" class="comment">
<div id="post-37010-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are lots of elegant shaped bollards in Tallinn &amp; Tartu, like these concrete clogs <a href="http://www.panoramio.com/photo/104851135">http://www.panoramio.com/photo/104851135</a></p>
</div>
<div id="comment-37010-info" class="comment-info">
<span class="comment-age">(23 Sep '14, 13:58)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="37011"></span>
<div id="comment-37011" class="comment">
<div id="post-37011-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"bollard:shape=clog" ;-)</p>
</div>
<div id="comment-37011-info" class="comment-info">
<span class="comment-age">(23 Sep '14, 14:15)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="37018"></span>
<div id="comment-37018" class="comment">
<div id="post-37018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nice, thanks I would expect them in the Netherlands ! Ill take them in as well, I never considered a proposal but Ill get the hack of it.</p>
</div>
<div id="comment-37018-info" class="comment-info">
<span class="comment-age">(23 Sep '14, 21:16)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-37000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37000-form-container" class="comment-form-container">
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

