+++
type = "question"
title = "How to capture packets when connected via data Card"
description = '''Hi All, I am New to wireshark, and i have window 7 OS and connected to internet via Reliance DATA CARD. But wireshark is not able to capture any packet. Kindly help me how to capture packets when connected via DATA CARD. Regards, manish'''
date = "2012-02-26T22:01:00Z"
lastmod = "2012-02-27T12:35:00Z"
weight = 9230
keywords = [ "capture", "packet" ]
aliases = [ "/questions/9230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture packets when connected via data Card](/questions/9230/how-to-capture-packets-when-connected-via-data-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9230-score" class="post-score" title="current number of votes">0</div><span id="post-9230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am New to wireshark, and i have window 7 OS and connected to internet via Reliance DATA CARD. But wireshark is not able to capture any packet. Kindly help me how to capture packets when connected via DATA CARD.</p><p>Regards, manish</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '12, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/cb118d239eb5b8e0202c2a5dc95c6c18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manish4990&#39;s gravatar image" /><p><span>manish4990</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manish4990 has no accepted answers">0%</span></p></div></div><div id="comments-container-9230" class="comments-container"></div><div id="comment-tools-9230" class="comment-tools"></div><div class="clear"></div><div id="comment-9230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9255"></span>

<div id="answer-container-9255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9255-score" class="post-score" title="current number of votes">1</div><span id="post-9255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One answer to your question is "with something that, unlike Wireshark, doesn't use WinPcap". I'm guessing that this is an Internet connection over the mobile phone network, which means it's going to appear to Windows as a PPP connection, and <a href="http://www.winpcap.org/misc/faq.htm#Q-5">those aren't supported by WinPcap on Windows 7</a>.</p><p>A better answer might be "<a href="http://www.microsoft.com/download/en/details.aspx?id=4865">with Microsoft Network Monitor</a>"; Network Monitor has its own drivers for capturing traffic, rather than using WinPcap, and that might be able to capture on PPP connections. It can dissect packets itself, and Wireshark can read Network Monitor captures. It's "free as in beer", meaning you don't have to pay for it; it's not "free as in speech", in that Microsoft doesn't make the source code for it available, <em>but</em> the dissectors are written in a text-based packet-description language rather than being written in C or C++ or C# or... and Microsoft <em>do</em> distribute the text-based descriptions with Network Monitor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9255" class="comments-container"></div><div id="comment-tools-9255" class="comment-tools"></div><div class="clear"></div><div id="comment-9255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

