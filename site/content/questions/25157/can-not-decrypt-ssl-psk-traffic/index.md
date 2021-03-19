+++
type = "question"
title = "Can not decrypt SSL PSK traffic"
description = '''Hi, in our project we use SSL PSK encryption with a 20 byte binary key. I hope we read all available documentation about that but we were not able to decrypt the traffic even when we have the complete traffic and the PSK key. The example works with a 16 byte text password. As said we use a 20 byte b...'''
date = "2013-09-24T06:20:00Z"
lastmod = "2014-03-25T03:08:00Z"
weight = 25157
keywords = [ "psk", "encryption" ]
aliases = [ "/questions/25157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can not decrypt SSL PSK traffic](/questions/25157/can-not-decrypt-ssl-psk-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25157-score" class="post-score" title="current number of votes">0</div><span id="post-25157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, in our project we use SSL PSK encryption with a 20 byte binary key. I hope we read all available documentation about that but we were not able to decrypt the traffic even when we have the complete traffic and the PSK key.</p><p>The example works with a 16 byte text password. As said we use a 20 byte binary password.</p><p>Can anyone help?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-psk" rel="tag" title="see questions tagged &#39;psk&#39;">psk</span> <span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '13, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/ea862b40e68a22cee6a65ea2f9a1c289?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trolly&#39;s gravatar image" /><p><span>trolly</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trolly has no accepted answers">0%</span></p></div></div><div id="comments-container-25157" class="comments-container"></div><div id="comment-tools-25157" class="comment-tools"></div><div class="clear"></div><div id="comment-25157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25479"></span>

<div id="answer-container-25479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25479-score" class="post-score" title="current number of votes">0</div><span id="post-25479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark 1.10.2, there is currently a hard-coded limit of 16 bytes for the PSK.</p><p>A fix was submitted at the wireshark bugtracker (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9216">bug 9216</a>), so if you use a development snapshot of SVN revision 52335 or later, it should work. Otherwise you can try to apply the patch on <a href="https://gist.github.com/Lekensteyn/6781709">https://gist.github.com/Lekensteyn/6781709</a> yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '13, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '13, 06:24</strong> </span></p></div></div><div id="comments-container-25479" class="comments-container"><span id="25499"></span><div id="comment-25499" class="comment"><div id="post-25499-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I will see if i can do that.</p></div><div id="comment-25499-info" class="comment-info"><span class="comment-age">(02 Oct '13, 02:49)</span> <span class="comment-user userinfo">trolly</span></div></div><span id="25553"></span><div id="comment-25553" class="comment"><div id="post-25553-score" class="comment-score"></div><div class="comment-text"><p><span>@trolly</span> The patch has been accepted, if you did not succeed in compiling your own, try a snapshot from <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div id="comment-25553-info" class="comment-info"><span class="comment-age">(02 Oct '13, 13:06)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="25961"></span><div id="comment-25961" class="comment"><div id="post-25961-score" class="comment-score"></div><div class="comment-text"><p>Thanks. We tried but it did not work. It will simply not output the decrypted data. Do you have an example with a 20 byte?</p></div><div id="comment-25961-info" class="comment-info"><span class="comment-age">(14 Oct '13, 06:22)</span> <span class="comment-user userinfo">trolly</span></div></div><span id="25962"></span><div id="comment-25962" class="comment"><div id="post-25962-score" class="comment-score"></div><div class="comment-text"><p><span>@trolly</span>, you can find an example capture in the bug report. Be sure to add leading zeroes as needed (if your last octet is lower than 16 (0x0f and below)</p></div><div id="comment-25962-info" class="comment-info"><span class="comment-age">(14 Oct '13, 06:26)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="25965"></span><div id="comment-25965" class="comment"><div id="post-25965-score" class="comment-score"></div><div class="comment-text"><p>Hi, what should I see in the example when the decryption works? Looks strange here.</p></div><div id="comment-25965-info" class="comment-info"><span class="comment-age">(14 Oct '13, 07:05)</span> <span class="comment-user userinfo">trolly</span></div></div><span id="25967"></span><div id="comment-25967" class="comment not_top_scorer"><div id="post-25967-score" class="comment-score"></div><div class="comment-text"><p>You should see HTTP traffic.</p></div><div id="comment-25967-info" class="comment-info"><span class="comment-age">(14 Oct '13, 07:59)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="29266"></span><div id="comment-29266" class="comment not_top_scorer"><div id="post-29266-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the long delay. We built wireshark with the suggested patch but it did not work, even with the provided sample. Is this bug already integrated? Are there some limitations for the key?</p><p>Confused ...</p></div><div id="comment-29266-info" class="comment-info"><span class="comment-age">(29 Jan '14, 02:28)</span> <span class="comment-user userinfo">trolly</span></div></div><span id="29346"></span><div id="comment-29346" class="comment not_top_scorer"><div id="post-29346-score" class="comment-score"></div><div class="comment-text"><p><span>@trolly</span> Ensure that the key is the hexadecimal representation of the binary key (with an even length, so prepend a zero if the length is odd).</p></div><div id="comment-29346-info" class="comment-info"><span class="comment-age">(31 Jan '14, 05:31)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="31142"></span><div id="comment-31142" class="comment not_top_scorer"><div id="post-31142-score" class="comment-score"></div><div class="comment-text"><p>Hi, in which wireshark release is this bug fixed? 1.10.x? Or will it be fixed in 1.11.x?</p></div><div id="comment-31142-info" class="comment-info"><span class="comment-age">(25 Mar '14, 01:47)</span> <span class="comment-user userinfo">ws_user13</span></div></div><span id="31145"></span><div id="comment-31145" class="comment not_top_scorer"><div id="post-31145-score" class="comment-score"></div><div class="comment-text"><p>This bug is already fixed in 1.11.x, it will probably not be fixed in 1.10.x.</p></div><div id="comment-31145-info" class="comment-info"><span class="comment-age">(25 Mar '14, 03:08)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-25479" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-25479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

