+++
type = "question"
title = "Monitoring MMS and GOOSE IEC61850"
description = '''Hello, What possibilities does wireshark have to offer when monitoring 61850 traffic?  With Wireshark, can you see the:   numerical content of a measured value in a MMS message? the GOOSE messages The content of messages containing boolean variables?  I was able to see some messages with the datamod...'''
date = "2010-09-20T23:24:00Z"
lastmod = "2017-05-09T09:25:00Z"
weight = 240
keywords = [ "mms", "61850" ]
aliases = [ "/questions/240" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring MMS and GOOSE IEC61850](/questions/240/monitoring-mms-and-goose-iec61850)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-240-score" class="post-score" title="current number of votes">0</div><span id="post-240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>What possibilities does wireshark have to offer when monitoring 61850 traffic?</p><p>With Wireshark, can you see the:</p><ul><li>numerical content of a measured value in a MMS message?</li><li>the GOOSE messages</li><li>The content of messages containing boolean variables?</li></ul><p>I was able to see some messages with the datamodel desctription. But when I was looking for the numerical value in MMS messages I only found the bits and bytes, numbers, ones and zeros...</p><p>Does anyone have experience with this usecase of wireshark?</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mms" rel="tag" title="see questions tagged &#39;mms&#39;">mms</span> <span class="post-tag tag-link-61850" rel="tag" title="see questions tagged &#39;61850&#39;">61850</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '10, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/d4abf7686b59fb362b959b66c303ed4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DBIN&#39;s gravatar image" /><p><span>DBIN</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DBIN has no accepted answers">0%</span></p></div></div><div id="comments-container-240" class="comments-container"><span id="61222"></span><div id="comment-61222" class="comment"><div id="post-61222-score" class="comment-score"></div><div class="comment-text"><p>Generally speaking, if Wireshark supports a protocol for dissecting it will be on Wireshark's website. For IEC 61850, for example:</p><p><a href="https://wiki.wireshark.org/Protocols/IEC61850GOOSEGSE">https://wiki.wireshark.org/Protocols/IEC61850GOOSEGSE</a></p><p>That describes to what extent it is supported.</p></div><div id="comment-61222-info" class="comment-info"><span class="comment-age">(03 May '17, 22:34)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-240" class="comment-tools"></div><div class="clear"></div><div id="comment-240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36518"></span>

<div id="answer-container-36518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36518-score" class="post-score" title="current number of votes">0</div><span id="post-36518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, you can do something like this: <a href="http://blog.iec61850.com/2014/09/problem-with-wireshark-and-mms-in.html">link text</a></p><p>Mirek</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '14, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/c14aa47c7ad9ce08c6dcfb9a38d95c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sobmir&#39;s gravatar image" /><p><span>sobmir</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sobmir has no accepted answers">0%</span></p></div></div><div id="comments-container-36518" class="comments-container"></div><div id="comment-tools-36518" class="comment-tools"></div><div class="clear"></div><div id="comment-36518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53539"></span>

<div id="answer-container-53539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53539-score" class="post-score" title="current number of votes">0</div><span id="post-53539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a <a href="http://www.sisconet.com/resources/">Wireshark fork</a> available with deeper IEC 61850, ICCP TASE/2, and C37.118 Synchrophasor parsing maintained by Herb Falk.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/221887c1605b3ea1ffd642957a7eab4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Colossus&#39;s gravatar image" /><p><span>Colossus</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Colossus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '16, 11:48</strong> </span></p></div></div><div id="comments-container-53539" class="comments-container"><span id="61185"></span><div id="comment-61185" class="comment"><div id="post-61185-score" class="comment-score"></div><div class="comment-text"><p>The Wireshark-Fork tool for IEC61850 is no more available at sisconet.</p><p>Any idea if this tool is available freely somewhere else?</p></div><div id="comment-61185-info" class="comment-info"><span class="comment-age">(03 May '17, 02:40)</span> <span class="comment-user userinfo">gewuerz</span></div></div><span id="61311"></span><div id="comment-61311" class="comment"><div id="post-61311-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/30311/gewuerz"></a><a href="https://ask.wireshark.org/users/30311/gewuerz">@gewuerz</a>: Sisconet is back online--it looks like they had an issue with their SiteLock config. I've confirmed that I can download the win32 installer again.</p></div><div id="comment-61311-info" class="comment-info"><span class="comment-age">(09 May '17, 09:25)</span> <span class="comment-user userinfo">Colossus</span></div></div></div><div id="comment-tools-53539" class="comment-tools"></div><div class="clear"></div><div id="comment-53539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

