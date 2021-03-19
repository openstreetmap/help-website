+++
type = "question"
title = "&quot;View Menu &gt; Name Resolution &gt; Resolve Name&quot; doesn&#x27;t seem to work"
description = '''My understanding from the documentation at http://www.wireshark.org/docs/wsug_html_chunked/ChUseViewMenuSection.html is that clicking &quot;View Menu &amp;gt; Name Resolution &amp;gt; Resolve Name&quot; should perform name resolution on the currently selected packet. This is, or would be, a very useful feature, as I ...'''
date = "2013-04-07T07:21:00Z"
lastmod = "2016-03-28T20:17:00Z"
weight = 20151
keywords = [ "name-resolving", "gui", "dns", "ip" ]
aliases = [ "/questions/20151" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# ["View Menu &gt; Name Resolution &gt; Resolve Name" doesn't seem to work](/questions/20151/view-menu-name-resolution-resolve-name-doesnt-seem-to-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20151-score" class="post-score" title="current number of votes">0</div><span id="post-20151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My understanding from the documentation at <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseViewMenuSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChUseViewMenuSection.html</a> is that clicking "View Menu &gt; Name Resolution &gt; Resolve Name" should perform name resolution on the currently selected packet. This is, or would be, a very useful feature, as I typically don't want to turn on network name resolution to prevent the additional reverse DNS queries during a capture, for a couple reasons. But when I do find a packet of interest and I don't recognize one of the IP addresses inside then I'd like to be able to click on it and do some more investigation (like a reverse lookup, etc.).</p><p>When I select a packet and then click the "Resolve name" option, however, nothing seems to happen. The GUI doesn't update the selected packet and replace the IP addresses with FQDNs (even when I can just go to a command prompt and get the same FQDN with nslookup). I've tried changing the DNS server my OS points to, and I've tried resolving several different IP addresses and this option just doesn't seem to do anything. On a few occasions I noticed that when I click this option the first time within a capture I can see a single reverse lookup (usually for that packet's destination address, not the source, oddly) and then nothing else (even this behavior isn't reliably repeatable). No more attempts to resolve anything no matter how many times I click Resolve name or how many packets I try this on. I tried marking the packets, to see if that matters, it didn't. I tried updating to WinPcap 4.1.3 and a few different builds (64 and 32 bit) of Wireshark. I tried running Wireshark in a clean Virtual Machine running an older version of Windows. No change.</p><p>Am I doing something wrong here? Or is this a bug I should report? Thought I'd ask in case this is just my bad, before going to the Bugzilla. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-name-resolving" rel="tag" title="see questions tagged &#39;name-resolving&#39;">name-resolving</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/2404f1aa9ddcb1a4b41f45994078e504?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="poundonu&#39;s gravatar image" /><p><span>poundonu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="poundonu has no accepted answers">0%</span></p></div></div><div id="comments-container-20151" class="comments-container"></div><div id="comment-tools-20151" class="comment-tools"></div><div class="clear"></div><div id="comment-20151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="20155"></span>

<div id="answer-container-20155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20155-score" class="post-score" title="current number of votes">1</div><span id="post-20155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're doing it correctly, but you're not looking in the right place for the results. "Resolve Name" does not change the display in the Packet List, only in the Packet Details pane. Expand the Internet Protocol header in the Packet Details pane and you will see the resolved domain names displayed next to the source and destination IP addresses. "Resolve Name" also resolves the MAC address OUIs at the same time.</p><p>Since you have to go into the Packet Details pane anyway, you can do this more quickly by using Wireshark's right-click functionality instead of the menu. Right-click anywhere in the Packet Details pane and select "Resolve Name."</p><p>If you want to see domain names in the Packet List, you'll have to turn on network name resolution instead of doing manual one-off resolutions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '13, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-20155" class="comments-container"></div><div id="comment-tools-20155" class="comment-tools"></div><div class="clear"></div><div id="comment-20155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38804"></span>

<div id="answer-container-38804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38804-score" class="post-score" title="current number of votes">0</div><span id="post-38804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can get the precise behavior you're looking for from instructions over here: <a href="http://www.howtogeek.com/106191/5-killer-tricks-to-get-the-most-out-of-wireshark/">http://www.howtogeek.com/106191/5-killer-tricks-to-get-the-most-out-of-wireshark/</a></p><p>Essentially, you click Edit | Preferences, and enable DNS Resolution. The packets in your window will all update.</p><p>Cheers</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/e6a96bc72fec045011ad218107ad5064?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyrka&#39;s gravatar image" /><p><span>kyrka</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyrka has no accepted answers">0%</span></p></div></div><div id="comments-container-38804" class="comments-container"></div><div id="comment-tools-38804" class="comment-tools"></div><div class="clear"></div><div id="comment-38804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51248"></span>

<div id="answer-container-51248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51248-score" class="post-score" title="current number of votes">0</div><span id="post-51248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>remove a 'capture filter' you might have previously established:-</p><p>-&gt; Edit -&gt; Configuration Profiles.</p><ul><li><p>note the folder link that contains 'profile preferences'</p></li><li><p>In the 'Profiles' subfolder, using a text editor, edit the preferences file.</p></li><li><p>remove or '# comment' any 'capture filters' that you might have previously established.</p></li><li></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '16, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/fa32bcf4e7ad74c1971180dc1757d97c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rove&#39;s gravatar image" /><p><span>rove</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rove has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '16, 21:13</strong> </span></p></div></div><div id="comments-container-51248" class="comments-container"></div><div id="comment-tools-51248" class="comment-tools"></div><div class="clear"></div><div id="comment-51248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

