+++
type = "question"
title = "USB to Ethernet Adapter doesn&#x27;t show under interfaces"
description = '''I have a regular NIC and an USB to Ethernet Adapter. The NIC shows but the USB doesn&#x27;t. How can I get this to work.'''
date = "2012-06-26T12:02:00Z"
lastmod = "2012-06-26T14:57:00Z"
weight = 12192
keywords = [ "to", "adapter", "usb", "ethernet" ]
aliases = [ "/questions/12192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [USB to Ethernet Adapter doesn't show under interfaces](/questions/12192/usb-to-ethernet-adapter-doesnt-show-under-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12192-score" class="post-score" title="current number of votes">1</div><span id="post-12192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a regular NIC and an USB to Ethernet Adapter. The NIC shows but the USB doesn't. How can I get this to work.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-adapter" rel="tag" title="see questions tagged &#39;adapter&#39;">adapter</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/12956218fe8bc89b8cf0c5fa6c0c0435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gvbingel&#39;s gravatar image" /><p><span>gvbingel</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gvbingel has no accepted answers">0%</span></p></div></div><div id="comments-container-12192" class="comments-container"></div><div id="comment-tools-12192" class="comment-tools"></div><div class="clear"></div><div id="comment-12192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12208"></span>

<div id="answer-container-12208" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12208-score" class="post-score" title="current number of votes">3</div><span id="post-12208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What is your OS?</p><p><strong>Windows</strong></p><p>Might be a problem with WinPcap. See here: <a href="http://www.winpcap.org/pipermail/winpcap-bugs/2010-March/001183.html">http://www.winpcap.org/pipermail/winpcap-bugs/2010-March/001183.html</a></p><p>Try to reload WinPcap, <strong>after</strong> you inserted the USB network adapter.</p><blockquote><p><code>net stop npf</code><br />
<code>net start npf</code><br />
<code>tshark -D</code><br />
</p></blockquote><p>RESULT: It did work on my system. tshark -D gave this list of adapters.</p><p>Before NPF reload:</p><pre><code>C:\tshark.exe -D
1. \Device\NPF_{FC8FD6A2-584E-4704-BAEB-C2C20949ED42} (Microsoft)
2. \Device\NPF_{9B364CD5-BFFD-4611-BF48-C2DD180A346C} (VMware Virtual Ethernet A
dapter)
3. \Device\NPF_{21E03ED5-DF15-4BA5-BEC0-22BBC44A8C23} (Broadcom NetXtreme Gigabi
t Ethernet Driver)</code></pre><p>After NPF reload:</p><pre><code>C:\tshark.exe -D
1. \Device\NPF_{FC8FD6A2-584E-4704-BAEB-C2C20949ED42} (Microsoft)
2. \Device\NPF_{9B364CD5-BFFD-4611-BF48-C2DD180A346C} (VMware Virtual Ethernet A
dapter)
3. \Device\NPF_{21E03ED5-DF15-4BA5-BEC0-22BBC44A8C23} (Broadcom NetXtreme Gigabi
t Ethernet Driver)
4. \Device\NPF_{94C00E60-0B0F-4F07-92FD-32252EF744AB} (USB2.0 to Gigabit Etherne
t Adapter)</code></pre><p>If that does not work, chances are good, that your adapter is not supported.</p><p><strong>Linux</strong></p><p>Should work if you can see the interface with <strong><code>ifconfig -a</code></strong>. If it does not work, please post the output of <strong><code>lsusb</code></strong>.</p><p><strong>MacOS</strong></p><p>Don't know. I guess the same as with Linux.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> wikified <strong>28 Jun '12, 01:45</strong> </span></p></div></div><div id="comments-container-12208" class="comments-container"><span id="12211"></span><div id="comment-12211" class="comment"><div id="post-12211-score" class="comment-score"></div><div class="comment-text"><p>On just about <em>any</em> UN*X, it should work if you can see the interface with <code>ifconfig -a</code>, although the way you'd look for it if you <em>can't</em> see the interface with <code>ifconfig -a</code> differs from OS to OS.</p></div><div id="comment-12211-info" class="comment-info"><span class="comment-age">(26 Jun '12, 14:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12208" class="comment-tools"></div><div class="clear"></div><div id="comment-12208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

