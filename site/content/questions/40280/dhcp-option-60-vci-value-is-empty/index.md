+++
type = "question"
title = "DHCP Option 60 - VCI value is EMPTY"
description = '''for some traces DHCP discovery packets, DHCP option 60 VCI value is EMPTY but in hex area we can see values in Bytes and HEX ... with length 7 Why VCI area is shown empty???  Option 60 length 7 Vendor Class identifier= &quot;empty&quot; in bytes option code = 3c length = 07 value = 00 00 22 03 48 47 57'''
date = "2015-03-05T05:20:00Z"
lastmod = "2015-03-05T17:48:00Z"
weight = 40280
keywords = [ "dhcp" ]
aliases = [ "/questions/40280" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP Option 60 - VCI value is EMPTY](/questions/40280/dhcp-option-60-vci-value-is-empty)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40280-score" class="post-score" title="current number of votes">0</div><span id="post-40280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>for some traces DHCP discovery packets, DHCP option 60 VCI value is EMPTY but in hex area we can see values in Bytes and HEX ... with length 7</p><p>Why VCI area is shown empty???</p><hr /><p>Option 60 length 7 Vendor Class identifier= "empty"</p><p>in bytes option code = 3c length = 07 value = 00 00 22 03 48 47 57</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/69384cdc560d1fbe6833a6b03478575a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Junaid&#39;s gravatar image" /><p><span>Junaid</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Junaid has no accepted answers">0%</span></p></div></div><div id="comments-container-40280" class="comments-container"><span id="40292"></span><div id="comment-40292" class="comment"><div id="post-40292-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version? Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-40292-info" class="comment-info"><span class="comment-age">(05 Mar '15, 08:21)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40280" class="comment-tools"></div><div class="clear"></div><div id="comment-40280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40281"></span>

<div id="answer-container-40281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40281-score" class="post-score" title="current number of votes">0</div><span id="post-40281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe because the actual value begins with zeroes, which could indicate a string terminator - so the Wireshark dissector probably thinks that the string is finished at the first byte. I'm just guessing though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40281" class="comments-container"><span id="40286"></span><div id="comment-40286" class="comment"><div id="post-40286-score" class="comment-score"></div><div class="comment-text"><p>may be, issue is actually; my BRAS is also no relaying this to DHCP Is it possible, BRAS is considering it a NULL value also and dropping the packet!??</p></div><div id="comment-40286-info" class="comment-info"><span class="comment-age">(05 Mar '15, 06:25)</span> <span class="comment-user userinfo">Junaid</span></div></div></div><div id="comment-tools-40281" class="comment-tools"></div><div class="clear"></div><div id="comment-40281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40314"></span>

<div id="answer-container-40314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40314-score" class="post-score" title="current number of votes">0</div><span id="post-40314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc2132#section-9">RFC 2132</a> just says the value is a "string of <em>n</em> octets"; it doesn't say "character string", as it does for some other options. The Wireshark dissector currently treats it as a character string; you might need to check with the supplier of whatever hardware/software is sending that packet to find out how that field is to be interpreted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40314" class="comments-container"></div><div id="comment-tools-40314" class="comment-tools"></div><div class="clear"></div><div id="comment-40314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

