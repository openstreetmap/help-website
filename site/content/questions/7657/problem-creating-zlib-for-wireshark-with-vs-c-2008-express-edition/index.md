+++
type = "question"
title = "Problem creating zlib for Wireshark with VS C++ 2008 Express Edition"
description = '''First of all, thanks to the contributors to this great tool.  I was trying to create a dissector for our protocol. As the first step, I was trying to build the wireshark, so that I have all the tools set up correctly.  I was following instruction Developer&#x27;s Guide The OS is Windows 7. I was using Vi...'''
date = "2011-11-26T21:20:00Z"
lastmod = "2011-12-09T06:17:00Z"
weight = 7657
keywords = [ "development", "zlib" ]
aliases = [ "/questions/7657" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problem creating zlib for Wireshark with VS C++ 2008 Express Edition](/questions/7657/problem-creating-zlib-for-wireshark-with-vs-c-2008-express-edition)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7657-score" class="post-score" title="current number of votes">0</div><span id="post-7657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First of all, thanks to the contributors to this great tool. I was trying to create a dissector for our protocol. As the first step, I was trying to build the wireshark, so that I have all the tools set up correctly.</p><p>I was following instruction <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html" title="Developer&#39;s Guide">Developer's Guide</a></p><p>The OS is Windows 7. I was using Visual Studio C++ 2008 Express Edition. In fact I used VS C++ 2010 Express Edition, but the error I got was the same.</p><p>Every step was successful except the last step with: <code>nmake -f Makefile.nmake all</code></p><p>The above command gave the error:</p><pre><code>&#39;zlib1.dll&#39; is up-to-date
        if not exist C:\wireshark-win32-libs\zlib125 mkdir C:\wireshark-win32-libs\zlib125
        if not exist C:\wireshark-win32-libs\zlib125\lib mkdir C:\wireshark-win32-libs\zlib125\lib
        if not exist C:\wireshark-win32-libs\zlib125\include mkdir C:\wireshark-win32-libs\zlib125\include
        mt.exe -nologo -manifest &quot;zlib1.dll.manifest&quot; -outputresource:zlib1.dll;2

zlib1.dll.manifest : general error c1010070: Failed to load and parse the manifest. The system cannot find the file specified.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft SDKs\Windows\v6.0A\bin\mt.exe&quot;&#39; : return code &#39;0x1f&#39;
Stop.</code></pre><p>I googled the problem on line, but there was no clear solution that I can find. Can you tell me why I got this problem? If you want to send me email, you can send to austinfcui at gmail dot com.</p><p>Thank you! Austin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-zlib" rel="tag" title="see questions tagged &#39;zlib&#39;">zlib</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '11, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/485220f4ae57a53311653e4eeba0cc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Austin&#39;s gravatar image" /><p><span>Austin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Austin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '11, 11:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7657" class="comments-container"><span id="7672"></span><div id="comment-7672" class="comment"><div id="post-7672-score" class="comment-score"></div><div class="comment-text"><p>Hi Austin, Currently i am writing dissector for my protocol.Can you give me your eMail-id, so that i will contact you if i have any doubts regarding the dissector creation and also i will help you if you have any doubts.My email-id feedback711[at]gmail[dot]com</p></div><div id="comment-7672-info" class="comment-info"><span class="comment-age">(28 Nov '11, 05:54)</span> <span class="comment-user userinfo">JK7</span></div></div></div><div id="comment-tools-7657" class="comment-tools"></div><div class="clear"></div><div id="comment-7657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7658"></span>

<div id="answer-container-7658" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7658-score" class="post-score" title="current number of votes">0</div><span id="post-7658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the error report the manifest file <code>zlib1.dll.manifest</code> is missing. I build with VC10 Express and have never seen this issue. I'm not at my build machine right now so can't offer you help on why it might be missing.</p><p>Also note that the path you have to mt.exe is from the Vista SDK, although I don't think this is a problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '11, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7658" class="comments-container"></div><div id="comment-tools-7658" class="comment-tools"></div><div class="clear"></div><div id="comment-7658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7846"></span>

<div id="answer-container-7846" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7846-score" class="post-score" title="current number of votes">0</div><span id="post-7846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, thank you for messages to my question.</p><p>I temporarily fixed this problem by copying the manifest file from Wireshark to zlib123 directory.</p><p>What I did was change Makefile.nmake so that it does not delete zlib123.tmp directory. Then run nmake command again and copy the zlib1d.dll.embed.manifest from the temporary directory to the wireshark directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '11, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/485220f4ae57a53311653e4eeba0cc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Austin&#39;s gravatar image" /><p><span>Austin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Austin has no accepted answers">0%</span></p></div></div><div id="comments-container-7846" class="comments-container"><span id="7848"></span><div id="comment-7848" class="comment"><div id="post-7848-score" class="comment-score"></div><div class="comment-text"><p>OK, why are you mentioning zlib123? Wireshark uses zlib125.</p></div><div id="comment-7848-info" class="comment-info"><span class="comment-age">(08 Dec '11, 09:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="7868"></span><div id="comment-7868" class="comment"><div id="post-7868-score" class="comment-score"></div><div class="comment-text"><p>To the comments: OK, why are you mentioning zlib123? Wireshark uses zlib125. Yes, it should be zlib125, not zlib123. Thank you!</p></div><div id="comment-7868-info" class="comment-info"><span class="comment-age">(09 Dec '11, 06:17)</span> <span class="comment-user userinfo">Austin</span></div></div></div><div id="comment-tools-7846" class="comment-tools"></div><div class="clear"></div><div id="comment-7846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

