+++
type = "question"
title = "Wikipedia map in some language displays a wrong country name"
description = '''For some reason, Lithuania is named Latvia when the map displays their Hebrew names in Wikipedia (that is, it shows two neighbouring countries called Latvia near the Baltic sea). When searching for the Hebrew name of Latvia in OSM, both countries show up as search results. (When searching for Lithua...'''
date = "2023-07-09T22:42:00Z"
lastmod = "2023-07-11T11:32:00Z"
weight = 87462
keywords = [ "wikipedia", "latvia", "lithuania", "tags", "hebrew" ]
aliases = [ "/questions/87462" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wikipedia map in some language displays a wrong country name](/questions/87462/wikipedia-map-in-some-language-displays-a-wrong-country-name)

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
<span id="post-87462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87462-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For some reason, Lithuania is named Latvia when the map displays their Hebrew names in Wikipedia (that is, it shows two neighbouring countries called Latvia near the Baltic sea).</p>
<p>When searching for the Hebrew name of Latvia in OSM, both countries show up as search results. (When searching for Lithuania or Estonia for example, only the searched country shows up).</p>
<p>I was looking for the error in the tags belonging to either Lithuania or Latvia, but everything looks correct...</p>
<p>Can anyone point me to possible causes of this weird display issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wikipedia" rel="tag" title="see questions tagged &#39;wikipedia&#39;">wikipedia</span> <span class="post-tag tag-link-latvia" rel="tag" title="see questions tagged &#39;latvia&#39;">latvia</span> <span class="post-tag tag-link-lithuania" rel="tag" title="see questions tagged &#39;lithuania&#39;">lithuania</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-hebrew" rel="tag" title="see questions tagged &#39;hebrew&#39;">hebrew</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '23, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f13c96349e2dbde79e18929443f38f54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="E%20L%20Yekutiel&#39;s gravatar image" />
<p><span>E L Yekutiel</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="E L Yekutiel has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '23, 17:06</strong> </span></p>
</div>
</div>
<div id="comments-container-87462" class="comments-container">
<span id="87464"></span>
<div id="comment-87464" class="comment">
<div id="post-87464-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi.</p>
<p>Would you share with us some links showing this behaviour?</p>
<p>Maybe the problem is from Wikidata, I'm pretty sure maps at Wikipedia draw their multi-lingual labels from it, and nominatim (the default search engine on OSM.org) might as well, as secondary source.</p>
<p>Regards.</p>
</div>
<div id="comment-87464-info" class="comment-info">
<span class="comment-age">(10 Jul '23, 10:09)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-87462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87462-form-container" class="comment-form-container">
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

<span id="87465"></span>

<div id="answer-container-87465" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87465-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you very much <a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> for your comment!</p>
<p>Apparently the issue wasn't in Wikidata; however, looking there did point me to the right direction.</p>
<p>When checking the tags earlier to look for the problem, I didn't notice that there is a "Relation: Lithuania (72596)", and within it, a member called "Node: Lithuania (424297773)" functioning as a label.</p>
<p>The problem was in the Hebrew tag of the Node, and previously I was looking only at the Relation.</p>
<p>From Wikidata there are links to both elements; this brought to my attention that there is another place to look for the mistake.</p>
<p>Thanks again!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '23, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f13c96349e2dbde79e18929443f38f54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="E%20L%20Yekutiel&#39;s gravatar image" />
<p><span>E L Yekutiel</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="E L Yekutiel has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-87465" class="comments-container">
<span id="87466"></span>
<div id="comment-87466" class="comment">
<div id="post-87466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad you found the problem !</p>
<p>Regards.</p>
</div>
<div id="comment-87466-info" class="comment-info">
<span class="comment-age">(10 Jul '23, 12:54)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="87470"></span>
<div id="comment-87470" class="comment">
<div id="post-87470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again <a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a>!</p>
<p>Small follow-up question, about the question itself, for you or for anyone who reads this: (it's a small newbie question that I didn't feel like it's worth more than a comment; but let me know if it's not the case)</p>
<p>In case the original question is of little interest to the general public, is there a way to delete it? (If I would have found the answer earlier, I wouldn't have asked the question at all, and maybe it's too specific to be interesting enough to justify publication);</p>
<p>or, in case it <strong>is</strong> of enough interest to the public, is there a way to mark the answer as accepted, so that others will know that this solution worked for this problem (i.e. to know that there may be other places to look for the mistake)? I don't see an option for marking as accepted... should I wait a certain period of time until it becomes possible to accept? Should I upvote the answer or something like that?</p>
<p>Thank you very much again!</p>
</div>
<div id="comment-87470-info" class="comment-info">
<span class="comment-age">(11 Jul '23, 10:30)</span> <span class="comment-user userinfo">E L Yekutiel</span>
</div>
</div>
<span id="87472"></span>
<div id="comment-87472" class="comment">
<div id="post-87472-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you can delete it (close button, or under more ?).</p>
<p>But it might interest some.</p>
<p>There should be a green check mark under the thumbs of the answer... It should mark the answer as accepted !</p>
<p>Best regards.</p>
</div>
<div id="comment-87472-info" class="comment-info">
<span class="comment-age">(11 Jul '23, 11:14)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="87473"></span>
<div id="comment-87473" class="comment">
<div id="post-87473-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You don't need to close it - I've marked the answer as accepted. Moderators can do that, but people answering their own question can't.</p>
</div>
<div id="comment-87473-info" class="comment-info">
<span class="comment-age">(11 Jul '23, 11:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87465-form-container" class="comment-form-container">
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

