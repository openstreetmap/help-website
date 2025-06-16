+++
type = "question"
title = "Names duplicated in Nodes and Ways - Is this a Bad Idea?"
description = '''I&#x27;m doing some work to produce some piste maps of ski resorts and I have a situation which probably doesn&#x27;t arise much when mapping roads and so on. Its to do with ski lifts (aerialways). Lets take the simplest lift possible as an example - a single way connecting two nodes. The way contains the nam...'''
date = "2012-01-21T13:44:00Z"
lastmod = "2012-01-24T14:18:00Z"
weight = 10115
keywords = [ "pistemap", "names", "aerialway" ]
aliases = [ "/questions/10115" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Names duplicated in Nodes and Ways - Is this a Bad Idea?](/questions/10115/names-duplicated-in-nodes-and-ways-is-this-a-bad-idea)

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
<span id="post-10115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm doing some work to produce some piste maps of ski resorts and I have a situation which probably doesn't arise much when mapping roads and so on. Its to do with ski lifts (aerialways).</p>
<p>Lets take the simplest lift possible as an example - a single way connecting two nodes. The way contains the name of the lift as a standard property tag <code>name="Signal"</code> . So far so good.</p>
<p>When looking at a piste map it is very helpful to know where the entrance to a lift is, i.e. which end you are allowed to get on. I've created maps in the past from my own data (not OSM data), and found it very useful to have the name of the lift next to the base station as well as along the lift itself, like below:</p>
<p><img src="/upfiles/Snap.jpg" alt="Map snapshot - This is NOT OSM data!!" /></p>
<p>Now I want to achieve this using OSM data. But, if the name is a property of the way, I can't see any possibility to associate it with one of the nodes other than by duplicating the name property in the node as well.</p>
<p>My question is therefore, is this a BAD thing to do? My gut feeling from a couple of decades working in IT is that when it is necessary to duplicate data it usually means something isn't designed correctly.</p>
<p>I've considered relations, but it seems that the name would need to be duplicated in the relation as well so that doesn't really help.</p>
<p>Any insights would be welcome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pistemap" rel="tag" title="see questions tagged &#39;pistemap&#39;">pistemap</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-aerialway" rel="tag" title="see questions tagged &#39;aerialway&#39;">aerialway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '12, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/743e1dc40bb65483cb9a1a68d8dd01ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skicat&#39;s gravatar image" />
<p><span>Skicat</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skicat has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-10115" class="comments-container">
&#10;</div>
<div id="comment-tools-10115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10115-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="10116"></span>

<div id="answer-container-10116" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10116-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Skicat has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't see any reason why it would be a problem. You have the aerialway=&lt;whatever&gt; tag on the way along with the name of the lift, and aerialway=station on the station nodes along with the name of the station. In your example they look different anyway, if I'm looking in the correct place ("Teleski Ouilette" vs just "Ouilette") for example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '12, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '12, 14:08</strong> </span></p>
</div>
</div>
<div id="comments-container-10116" class="comments-container">
<span id="10117"></span>
<div id="comment-10117" class="comment">
<div id="post-10117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the reason the node-names are different to the way-names is that I have the renderer insert "telesiege", "teleski" or whatever according to the type of the way. I don't do that with nodes.</p>
</div>
<div id="comment-10117-info" class="comment-info">
<span class="comment-age">(21 Jan '12, 14:20)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
<span id="10118"></span>
<div id="comment-10118" class="comment">
<div id="post-10118-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried visiting <a href="http://www.openpistemap.org">http://www.openpistemap.org</a> to see how the lifts rendered there, but there seem to be some technical issues at present. Anyway, the lift and the station are still separate objects. If they have the same name, I don't see an issue with tagging them both with the name.</p>
</div>
<div id="comment-10118-info" class="comment-info">
<span class="comment-age">(21 Jan '12, 15:45)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="10121"></span>
<div id="comment-10121" class="comment">
<div id="post-10121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I agree. I suppose I was looking for some facility that could apply a name to a node based on the <code>way</code> that the node belongs to, but there is no such direct relationship. Or if there is, it isn't apparent how that relationship can be used from the mkgmap renderer.</p>
</div>
<div id="comment-10121-info" class="comment-info">
<span class="comment-age">(21 Jan '12, 16:56)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
<span id="10192"></span>
<div id="comment-10192" class="comment">
<div id="post-10192-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've marked this as the accepted answer as it most closely addresses the "Is duplicate data bad?" question. Thanks Ed.</p>
</div>
<div id="comment-10192-info" class="comment-info">
<span class="comment-age">(24 Jan '12, 14:11)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
</div>
<div id="comment-tools-10116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10116-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10123"></span>

<div id="answer-container-10123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10123-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>When looking at a piste map it is very helpful to know where the entrance to a lift is.</p>
</blockquote>
<p>That is why you have the way go from the entrance to the exit. Then you can render an arrow or something in the direction of the lift. The information is not duplicated and you still allow the entrance, the exit and the lift to have different names.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '12, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-10123" class="comments-container">
<span id="10191"></span>
<div id="comment-10191" class="comment">
<div id="post-10191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, if you look at the map above you'll see it does indeed have "arrow flights" in the direction of the lift. I still think the map is improved by displaying the name of the lifts at their base stations though.</p>
</div>
<div id="comment-10191-info" class="comment-info">
<span class="comment-age">(24 Jan '12, 14:09)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
</div>
<div id="comment-tools-10123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10119"></span>

<div id="answer-container-10119" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10119-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use the entrance tag on a node at the entrance to the lift. See <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/entrance">https://wiki.openstreetmap.org/wiki/Proposed_features/entrance</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '12, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-10119" class="comments-container">
<span id="10120"></span>
<div id="comment-10120" class="comment">
<div id="post-10120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have considered that tag. It has some odd usage values such as [yes|exit|both], however it could be used to identify the entrance to an aerialway. It doesn't solve the problem of having to duplicate the name though.</p>
</div>
<div id="comment-10120-info" class="comment-info">
<span class="comment-age">(21 Jan '12, 16:52)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
<span id="10122"></span>
<div id="comment-10122" class="comment">
<div id="post-10122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can then justifiably use the name tag next to the entrance tag - you are naming the entrance.</p>
</div>
<div id="comment-10122-info" class="comment-info">
<span class="comment-age">(21 Jan '12, 16:58)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="10193"></span>
<div id="comment-10193" class="comment">
<div id="post-10193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had effectively already done something like this, but used a "aerialway:access" tag with values [entry|exit|both]. I'm in two minds whether to change these to use the "entrance" tag or not. I've only done a few but there's an argument that says don't create a new tag when a suitable one already exists. Then again, "entrance" does seem to be more about buildings, and ski lifts don't always have buildings. I'm trying to encapsulate whether one can "board", "alight" or both from each end of the lift. "entrance" is close but not quite 100%. Plus I still think the tag values are incongruous.</p>
</div>
<div id="comment-10193-info" class="comment-info">
<span class="comment-age">(24 Jan '12, 14:18)</span> <span class="comment-user userinfo">Skicat</span>
</div>
</div>
</div>
<div id="comment-tools-10119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10119-form-container" class="comment-form-container">
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

