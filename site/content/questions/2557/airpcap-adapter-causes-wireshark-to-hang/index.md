+++
type = "question"
title = "AirPcap Adapter Causes Wireshark to Hang"
description = '''Running Wireshark 1.4.2 on a Dell Vista64 laptop. Whenever my AirPcap Nx device is attached (driver version 06/03/2009) to the laptop, Wireshark hangs upon loading. If I unplug the AirPcap adapter, Wireshark completes the loading process. If I then plug the AirPcap back in and click &quot;Interfaces&quot;, it...'''
date = "2011-02-24T09:46:00Z"
lastmod = "2011-02-24T19:00:00Z"
weight = 2557
keywords = [ "airpcap", "hang", "wireshark" ]
aliases = [ "/questions/2557" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [AirPcap Adapter Causes Wireshark to Hang](/questions/2557/airpcap-adapter-causes-wireshark-to-hang)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2557-score" class="post-score" title="current number of votes">0</div><span id="post-2557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running Wireshark 1.4.2 on a Dell Vista64 laptop. Whenever my AirPcap Nx device is attached (driver version 06/03/2009) to the laptop, Wireshark hangs upon loading. If I unplug the AirPcap adapter, Wireshark completes the loading process. If I then plug the AirPcap back in and click "Interfaces", it hangs again, until I unplug the AirPcap adapter. It then shows the Interfaces screen, along with the AirPcap adapter visible. If I then plug it back it and click Start on the AirPcap item, it hangs again, until I unplug the adapter, at which time WS spits out about 10 error dialog boxes.</p><p>I bought the AirPcap Nx to capture wireless traffic with Wireshark -- any ideas why this combination is not working?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-hang" rel="tag" title="see questions tagged &#39;hang&#39;">hang</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '11, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/a049f24820d77d7b560a4f67f02541b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BtrieveBill&#39;s gravatar image" /><p><span>BtrieveBill</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BtrieveBill has no accepted answers">0%</span></p></div></div><div id="comments-container-2557" class="comments-container"></div><div id="comment-tools-2557" class="comment-tools"></div><div class="clear"></div><div id="comment-2557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2561"></span>

<div id="answer-container-2561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2561-score" class="post-score" title="current number of votes">2</div><span id="post-2561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known bug in Windows Vista which requires a registry fix. If you can send a registry dump to CACE support as described at <a href="http://www.cacetech.com/support/airpcap_faq.html#faq_11">http://www.cacetech.com/support/airpcap_faq.html#faq_11</a> they can send you a fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '11, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-2561" class="comments-container"></div><div id="comment-tools-2561" class="comment-tools"></div><div class="clear"></div><div id="comment-2561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2560"></span>

<div id="answer-container-2560" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2560-score" class="post-score" title="current number of votes">0</div><span id="post-2560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might try to update your driver. Looking at the <a href="http://www.cacetech.com/downloads.html">CACE download page</a>, it looks like there is a newer version of the driver available than what you're using:</p><pre><code>Driver V 4.1.1 (Windows 2000/XP/2003/Vista/2008/7, 32 and 64 bit)
Download » (01/18/2010)
Release Notes » (01/18/2010)</code></pre><p>If that doesn't help, then you might want to try to contact <a href="http://www.cacetech.com/support/tech_support.html">CACE technical support</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '11, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2560" class="comments-container"></div><div id="comment-tools-2560" class="comment-tools"></div><div class="clear"></div><div id="comment-2560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

