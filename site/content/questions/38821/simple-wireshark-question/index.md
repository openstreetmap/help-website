+++
type = "question"
title = "simple wireshark question"
description = '''hi guys, i have probably a not very intelligent question but i&#x27;m new to wireshark and playing with it right now to get some basic experience with it. i have to hosts A and B with wireshark enabled on both ends. i&#x27;m doing so really basic stuff like i ping host B from host A to get and idea of how thi...'''
date = "2014-12-31T06:00:00Z"
lastmod = "2014-12-31T06:35:00Z"
weight = 38821
keywords = [ "wireshark" ]
aliases = [ "/questions/38821" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [simple wireshark question](/questions/38821/simple-wireshark-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38821-score" class="post-score" title="current number of votes">0</div><span id="post-38821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>i have probably a not very intelligent question but i'm new to wireshark and playing with it right now to get some basic experience with it. i have to hosts A and B with wireshark enabled on both ends. i'm doing so really basic stuff like i ping host B from host A to get and idea of how this tool works. what i did i enabled Windows Firewall on host B so i can now see that 4 echo / ICMP requests are send but i'm wondering if wireshark will tell me why ? i mean i know it's not getting any response because ICMP requests are blocked on host B but the wireshark log is not telling me this is just see :</p><p>no response seeen</p><p>Expert info (Warn/sequence): no reponse seen to ICMP request in frame x</p><p>once again sorry if this is stupid but i would to know. or will wireshark show me that something is not working but WHY it's not working i will have to find it different way ?</p><p>thank you very much</p><p>Adam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '14, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-38821" class="comments-container"></div><div id="comment-tools-38821" class="comment-tools"></div><div class="clear"></div><div id="comment-38821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38823"></span>

<div id="answer-container-38823" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38823-score" class="post-score" title="current number of votes">1</div><span id="post-38823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adasko has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, Wireshark can only report on what happens (or doesn't happen) in the case of a missing ICMP ping reply. Literally anything could have happened ranging from from the request not leaving the host machine to the responses being eaten by a <a href="http://www.venganza.org/">flying spaghetti monster</a>.</p><p>Wireshark gives valuable insight into the packets that are captured and can infer some things if expected things don't happen, but the why is down to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '14, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '14, 08:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-38823" class="comments-container"><span id="38824"></span><div id="comment-38824" class="comment"><div id="post-38824-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> this makes sense to me. thank you for clearing my doubts !</p></div><div id="comment-38824-info" class="comment-info"><span class="comment-age">(31 Dec '14, 06:25)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="38826"></span><div id="comment-38826" class="comment"><div id="post-38826-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-38826-info" class="comment-info"><span class="comment-age">(31 Dec '14, 06:35)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="38827"></span><div id="comment-38827" class="comment"><div id="post-38827-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38827-info" class="comment-info"><span class="comment-age">(31 Dec '14, 06:35)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-38823" class="comment-tools"></div><div class="clear"></div><div id="comment-38823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

