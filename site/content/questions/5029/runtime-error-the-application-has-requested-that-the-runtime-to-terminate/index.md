+++
type = "question"
title = "Runtime Error!   The Application has requested that the Runtime to Terminate...."
description = '''Runtime Error! The Application has requested that the Runtime to Terminate it in an unusual way.  please contact support....  Hello,  I am receiving the above issued runtime error. Does not matter if I am running 1.6.0 or the Release Candidate. I get the same message all the time.  Win XP - SP3 is t...'''
date = "2011-07-13T12:05:00Z"
lastmod = "2012-07-31T03:30:00Z"
weight = 5029
keywords = [ "windows", "crash", "startup" ]
aliases = [ "/questions/5029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Runtime Error! The Application has requested that the Runtime to Terminate....](/questions/5029/runtime-error-the-application-has-requested-that-the-runtime-to-terminate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5029-score" class="post-score" title="current number of votes">0</div><span id="post-5029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Runtime Error! The Application has requested that the Runtime to Terminate it in an unusual way. please contact support....</p><p>Hello,</p><p>I am receiving the above issued runtime error. Does not matter if I am running 1.6.0 or the Release Candidate. I get the same message all the time.</p><p>Win XP - SP3 is the OS with all MS patches applied. (Corporate Laptop, I would be on updated OS if I had my way).</p><p>I have done several searches, many pointing to likely causes, however I am still not able to resolve my issue starting Wireshark. Any suggestions please feel free to ask.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '11, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/6c5d0ae54e604010516e588fe4851cac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vIPer&#39;s gravatar image" /><p><span>vIPer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vIPer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '11, 12:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5029" class="comments-container"><span id="5030"></span><div id="comment-5030" class="comment"><div id="post-5030-score" class="comment-score"></div><div class="comment-text"><p>We'll need more info to be able to help:</p><p>When does the error occur ?</p><p>Immediately upon starting Wireshark ? When trying to open/read a capture file ? When starting a capture ? ....</p><p>What happens if you run tshark ?</p><p>Have you previously used an earlier version of Wireshark (1.4...) without problems ?</p></div><div id="comment-5030-info" class="comment-info"><span class="comment-age">(13 Jul '11, 12:18)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="5179"></span><div id="comment-5179" class="comment"><div id="post-5179-score" class="comment-score"></div><div class="comment-text"><p>this happens to me on a just downloaded 64 bit latest version on my windows 7 home premium.</p><p>it's when starting wireshark. i didn't install any of the plugins , tools or guide, i unchecked everything but wireshark</p><p>Problem signature: Problem Event Name: APPCRASH Application Name: wireshark.exe Application Version: 1.6.1.38096 Application Timestamp: 4e24970f Fault Module Name: libglib-2.0-0.dll Fault Module Version: 2.26.1.0 Fault Module Timestamp: 4d1b271d Exception Code: 40000015 Exception Offset: 000000000005180e OS Version: 6.1.7601.2.1.0.768.3 Locale ID: 1033 Additional Information 1: 15f2 Additional Information 2: 15f24de02058d998dac1fee4b72e43a7 Additional Information 3: ee90 Additional Information 4: ee90cb82c5153ac4c760d5dfbd9a2983</p></div><div id="comment-5179-info" class="comment-info"><span class="comment-age">(22 Jul '11, 22:05)</span> <span class="comment-user userinfo">fjleon</span></div></div><span id="5182"></span><div id="comment-5182" class="comment"><div id="post-5182-score" class="comment-score"></div><div class="comment-text"><p>Hi, I'm guessing the problem is related to not installing WinPcap.</p></div><div id="comment-5182-info" class="comment-info"><span class="comment-age">(23 Jul '11, 08:34)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="5183"></span><div id="comment-5183" class="comment"><div id="post-5183-score" class="comment-score"></div><div class="comment-text"><p>i did install winpcap. but it is a 32 bit app, and wireshark is 64 bit. maybe they can't talk to each other</p></div><div id="comment-5183-info" class="comment-info"><span class="comment-age">(23 Jul '11, 11:24)</span> <span class="comment-user userinfo">fjleon</span></div></div><span id="5184"></span><div id="comment-5184" class="comment"><div id="post-5184-score" class="comment-score"></div><div class="comment-text"><p>i uninstalled everything and reinstalled everything and this time it worked. maybe i had a previous winpcap and didn't uninstall, i don't know. but since i launched the installer again it offered to uninstall everything and it did uninstall winpcap.</p></div><div id="comment-5184-info" class="comment-info"><span class="comment-age">(23 Jul '11, 11:27)</span> <span class="comment-user userinfo">fjleon</span></div></div></div><div id="comment-tools-5029" class="comment-tools"></div><div class="clear"></div><div id="comment-5029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13179"></span>

<div id="answer-container-13179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13179-score" class="post-score" title="current number of votes">0</div><span id="post-13179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After changing the windows profile its started working fine</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/8bebf44190c66ba2939dd40b473083e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krian&#39;s gravatar image" /><p><span>krian</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krian has no accepted answers">0%</span></p></div></div><div id="comments-container-13179" class="comments-container"></div><div id="comment-tools-13179" class="comment-tools"></div><div class="clear"></div><div id="comment-13179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

