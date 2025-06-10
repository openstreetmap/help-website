+++
type = "question"
title = "Place=* nodes inside areas: doesn&#x27;t this violate one-feature-one-element?"
description = '''Hi everyone. The context for this question is that I&#x27;d like to improve the multilingual names for the states of the US. I&#x27;m using iD. When I search for a state name, the main result is the Administrative Boundary relation and it has all the name:xx tags. But inside the state there is also a node wit...'''
date = "2020-12-27T23:34:00Z"
lastmod = "2020-12-29T10:30:00Z"
weight = 78079
keywords = [ "states", "relations", "localization" ]
aliases = [ "/questions/78079" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Place=\* nodes inside areas: doesn't this violate one-feature-one-element?](/questions/78079/place-nodes-inside-areas-doesnt-this-violate-one-feature-one-element)

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
<span id="post-78079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78079-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone. The context for this question is that I'd like to improve the multilingual names for the states of the US. I'm using iD. When I search for a state name, the main result is the Administrative Boundary relation and it has all the name:xx tags. But inside the state there is also a node with place=state that is role=label. This node has a completely separate set of name:xx tags! I have noticed some states where the relation's name and the node's name have slight differences. So to localize every state I have to do it twice each.</p>
<p>My understanding is that some places are sometimes mapped as center nodes because their boundaries aren't clearly defined, but for states I wouldn't think that's a problem. Doesn't this practice violate the "one feature one element"? What are some reasons for mapping label nodes inside the relation? Should I fix the name:xx for both each?</p>
<p>Thank you.</p>
<p>Edit: I would like to note that, at least for OSM's renderer and within iD, the state's name appears roughly centered over the area, and not where the role=label node is. So I'm not seeing what the label node provides.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-states" rel="tag" title="see questions tagged &#39;states&#39;">states</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '20, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1016cb75adfd12cc8c01e342bbaf979a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="traditionalstonethrow&#39;s gravatar image" />
<p><span>traditionals...</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="traditionalstonethrow has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '20, 23:51</strong> </span></p>
</div>
</div>
<div id="comments-container-78079" class="comments-container">
&#10;</div>
<div id="comment-tools-78079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78079-form-container" class="comment-form-container">
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

<span id="78082"></span>

<div id="answer-container-78082" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78082-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-78082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would say no. <code>place=</code> and <code>boundary=administrative</code> are different concepts. The former abstract; the latter defined exactly for a specific reason and purpose. There are also cases where they don't match. In composition, the <code>admin_centre</code> and <code>label</code> members don't always coincide. For states, the perceived center may not be the same as the geographic center either.</p>
<p>A bigger issue is double-tagging <code>place=</code> on the <code>boundary=administrative</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '20, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '20, 10:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-78082" class="comments-container">
&#10;</div>
<div id="comment-tools-78082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78082-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78080"></span>

<div id="answer-container-78080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78080-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, about the task you are describing: Please only ever add name tags for languages that you know. Do not blindly copy names in languages you are unfamiliar with from places like Wikipedia - it doesn't improve the quality of OSM one bit. Especially so if the name you enter for a certain language is identical to the English name of the place. See this thread on talk-us <a href="https://lists.openstreetmap.org/pipermail/talk-us/2020-December/020769.html">https://lists.openstreetmap.org/pipermail/talk-us/2020-December/020769.html</a> and maybe discuss your ideas there before continuing.</p>
<p>As for your second question, I think that the place nodes are mostly left over from olden times when we did not have administrative boundaries. At some point the rendering has switched from using the place nodes to using the names of admin boundaries, but not every renderer necessarily does that and if someone just wants to know where in the world approximately Nevada is, maybe these nodes are useful. Nominatim, at least, will under certain circumstances merge names from a place node and its surrounding admin boundary.</p>
<p>You are right in saying these nodes violate the idea of "one feature, one object", unless of course you want to argue that "a state" and "the administrative boundary of a state" are two different things. Personally I wouldn't add a place node if I added a new state boundary, but I wouldn't remove an existing one either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '20, 00:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78080" class="comments-container">
<span id="78081"></span>
<div id="comment-78081" class="comment">
<div id="post-78081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, thank you for the caution about blind copying. I have confidence that my change would be a good one, but I'll use separate talk threads for that.</p>
<p>I did not consider that state boundaries were added later, so that makes sense as to why they exist. I wouldn't dare remove the nodes but I hope one day it can happen so we don't have to duplicate everything.</p>
<p>So it sounds like I should do the names on both then, since different renderers might be using them both. The reason I started this is because I noticed the inconsistency within OsmAnd, which I now believe is pulling the names from the nodes, not the relations. Thanks again.</p>
</div>
<div id="comment-78081-info" class="comment-info">
<span class="comment-age">(28 Dec '20, 00:19)</span> <span class="comment-user userinfo">traditionals...</span>
</div>
</div>
<span id="78098"></span>
<div id="comment-78098" class="comment">
<div id="post-78098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It should be noted that boundary relations support a "label" role that can reference a node for placement of the label :-). If this references such a place node applications can in principle could de-duplication of the objects.</p>
</div>
<div id="comment-78098-info" class="comment-info">
<span class="comment-age">(29 Dec '20, 10:30)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78080-form-container" class="comment-form-container">
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

