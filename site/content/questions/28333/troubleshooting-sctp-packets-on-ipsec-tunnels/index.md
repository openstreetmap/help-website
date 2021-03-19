+++
type = "question"
title = "Troubleshooting SCTP packets on IPSec Tunnels"
description = '''Hi, I would like to know if there is any mechanism to decrypt and analyze the SCTP packets exchanged over IPSec tunnels between two end nodes, for troubleshooting using Wireshark or tshark? Please advise. Regards, SC'''
date = "2013-12-22T20:23:00Z"
lastmod = "2013-12-26T07:23:00Z"
weight = 28333
keywords = [ "sctp", "ipsec", "decrypt", "wireshark" ]
aliases = [ "/questions/28333" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting SCTP packets on IPSec Tunnels](/questions/28333/troubleshooting-sctp-packets-on-ipsec-tunnels)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28333-score" class="post-score" title="current number of votes">1</div><span id="post-28333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know if there is any mechanism to decrypt and analyze the SCTP packets exchanged over IPSec tunnels between two end nodes, for troubleshooting using Wireshark or tshark?</p><p>Please advise.</p><p>Regards, SC</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '13, 20:23</strong></p><img src="https://secure.gravatar.com/avatar/dc1d6bf8a8665c6b9c954eb8670806d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tintin&#39;s gravatar image" /><p><span>tintin</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tintin has no accepted answers">0%</span></p></div></div><div id="comments-container-28333" class="comments-container"></div><div id="comment-tools-28333" class="comment-tools"></div><div class="clear"></div><div id="comment-28333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28336"></span>

<div id="answer-container-28336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28336-score" class="post-score" title="current number of votes">0</div><span id="post-28336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try it by setting preferences for ESP option. Regards, NA</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '13, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/23cd85e89512c477196467a7e846d7e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alaska&#39;s gravatar image" /><p><span>alaska</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alaska has no accepted answers">0%</span></p></div></div><div id="comments-container-28336" class="comments-container"><span id="28339"></span><div id="comment-28339" class="comment"><div id="post-28339-score" class="comment-score"></div><div class="comment-text"><p>In other words, you have to configure Wireshark to decode the IPSec; after that then it will analyze whatever the IPSec payload as normal. See the <a href="http://wiki.wireshark.org/ESP_Preferences">wiki</a> for more details.</p></div><div id="comment-28339-info" class="comment-info"><span class="comment-age">(23 Dec '13, 07:21)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="28345"></span><div id="comment-28345" class="comment"><div id="post-28345-score" class="comment-score"></div><div class="comment-text"><p>Or here: <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets</a></p></div><div id="comment-28345-info" class="comment-info"><span class="comment-age">(23 Dec '13, 11:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28408"></span><div id="comment-28408" class="comment"><div id="post-28408-score" class="comment-score"></div><div class="comment-text"><p>One-upping this question because I suspect in the next couple quarters it's going to be a popular need in mobile. IPX and Diameter is coming. :)</p></div><div id="comment-28408-info" class="comment-info"><span class="comment-age">(26 Dec '13, 07:23)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-28336" class="comment-tools"></div><div class="clear"></div><div id="comment-28336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

