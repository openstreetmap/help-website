+++
type = "question"
title = "How to tag emergency exit staircase"
description = '''A building has an emergency exit starting at a height. At the wall, there is a staircase, which leads to a footpath next to the building. The exit itself (node) can be tagged with exit=emergency. What tags would I use for the the path connecting this exit node to the footpath? I would like to make i...'''
date = "2018-02-13T19:59:00Z"
lastmod = "2018-02-14T11:42:00Z"
weight = 62074
keywords = [ "stairs", "tagging", "emergency" ]
aliases = [ "/questions/62074" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag emergency exit staircase](/questions/62074/how-to-tag-emergency-exit-staircase)

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
<span id="post-62074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62074-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A building has an emergency exit starting at a height. At the wall, there is a staircase, which leads to a footpath next to the building. The exit itself (node) can be tagged with exit=emergency. What tags would I use for the the path connecting this exit node to the footpath? I would like to make it explicit that this is a staircase. See <a href="https://www.openstreetmap.org/note/1298586">this note</a>. An example of such staircase: <img src="http://www.elevestairs.com/images/emergency-stairs/emergency-stairs-13.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stairs" rel="tag" title="see questions tagged &#39;stairs&#39;">stairs</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-emergency" rel="tag" title="see questions tagged &#39;emergency&#39;">emergency</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '18, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/7f75b476d4984deb5e4c83d276b9c22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kotya&#39;s gravatar image" />
<p><span>Kotya</span><br />
<span class="score" title="631 reputation points">631</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kotya has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '18, 20:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62074" class="comments-container">
&#10;</div>
<div id="comment-tools-62074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62074-form-container" class="comment-form-container">
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

<span id="62078"></span>

<div id="answer-container-62078" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62078-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Create a node at the building where the emergency exit is located. Tag it with <code>exit=emergency</code> (there is also <a href="https://wiki.openstreetmap.org/wiki/Key:entrance"><code>entrance</code></a><code>=emergency</code> but should be avoided according to the Wiki).</p>
<p>Draw the staircase connected to this node and tag it with <code>highway=steps</code>, <code>access=no</code> and <code>emergency=yes</code>.</p>
<p>Draw a connection from this staircase to the rest of the road network, e.g. to a nearby road or footway.</p>
<p>Example:<br />
<img src="/upfiles/foo_nYyV3MT.png" alt="example image" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '18, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62078" class="comments-container">
<span id="62079"></span>
<div id="comment-62079" class="comment">
<div id="post-62079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>according to the <a href="https://wiki.openstreetmap.org/wiki/Key:access">wiki page on access</a> the emergency key means: emergency motor vehicles; e.g., ambulance, fire truck, police car</p>
<p>not exactly what you mean here I think. Is there some other documentation available on access "in case of an emergency" ?</p>
</div>
<div id="comment-62079-info" class="comment-info">
<span class="comment-age">(14 Feb '18, 10:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="62081"></span>
<div id="comment-62081" class="comment">
<div id="post-62081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no other documentation I can refer to. In my opinion the wiki is too unspecific / incomplete about the emergency usage. At least I don't know any other way to create an emergency exception for access=no. Using emergency=yes in this case just sounds consistent to me. But maybe someone has a better idea :)</p>
</div>
<div id="comment-62081-info" class="comment-info">
<span class="comment-age">(14 Feb '18, 10:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62078-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62077"></span>

<div id="answer-container-62077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Stairs are rendered on the standard map. <a href="https://www.openstreetmap.org/#map=19/52.32992/-0.15017">https://www.openstreetmap.org/#map=19/52.32992/-0.15017</a> You could inspect the tags of this one. These stairs lead to a wildlife Hide or Viewpoint. The stairs and path will also need highway=yes footway=yes. The fire stairs should have emergency=only maybe. I see you may have borrowed the picture, did you have permission? better to create one yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '18, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-62077" class="comments-container">
<span id="62080"></span>
<div id="comment-62080" class="comment">
<div id="post-62080-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>why do you combine highway=steps with highway=yes + footway=yes ? Aren't those implicated by the highway=steps tag ?</p>
</div>
<div id="comment-62080-info" class="comment-info">
<span class="comment-age">(14 Feb '18, 10:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="62082"></span>
<div id="comment-62082" class="comment">
<div id="post-62082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes i guess they are</p>
</div>
<div id="comment-62082-info" class="comment-info">
<span class="comment-age">(14 Feb '18, 11:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-62077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62077-form-container" class="comment-form-container">
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

