+++
type = "question"
title = "IP name resolution not working"
description = '''How to convert source and destination ip address to host names, i was trying to open datasets of netflow data traces or wireless strength data traces. when i go to edit&amp;gt;preferences and enable the name resolution options nothing really works on wireshark 2.03'''
date = "2016-05-06T11:36:00Z"
lastmod = "2016-05-09T13:50:00Z"
weight = 52282
keywords = [ "ip", "hostname", "nameresolution" ]
aliases = [ "/questions/52282" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IP name resolution not working](/questions/52282/ip-name-resolution-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52282-score" class="post-score" title="current number of votes">0</div><span id="post-52282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to convert source and destination ip address to host names, i was trying to open datasets of netflow data traces or wireless strength data traces. when i go to edit&gt;preferences and enable the name resolution options nothing really works on wireshark 2.03</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-hostname" rel="tag" title="see questions tagged &#39;hostname&#39;">hostname</span> <span class="post-tag tag-link-nameresolution" rel="tag" title="see questions tagged &#39;nameresolution&#39;">nameresolution</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '16, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/117a13ccebe355c74c1fa57424f5d2c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prajwal&#39;s gravatar image" /><p><span>prajwal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prajwal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '16, 15:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-52282" class="comments-container"></div><div id="comment-tools-52282" class="comment-tools"></div><div class="clear"></div><div id="comment-52282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52289"></span>

<div id="answer-container-52289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52289-score" class="post-score" title="current number of votes">0</div><span id="post-52289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Name resolution should work as you expect--assuming that the computer you're running Wireshark on now has access to a DNS server (or hosts file) that can resolve those IP addresses to names. (As Shawn points out it can also be done based on DNS packets you captured. But normally name resolution does <strong>not</strong> need to enabled while you're capturing.)</p><p>Two possibilities exist:</p><ol><li>Did you also enable the name resolution to use external name resolvers?</li><li>You could be running into <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12384">bug 12384</a>. See the bug for how to work around it.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '16, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52289" class="comments-container"><span id="52358"></span><div id="comment-52358" class="comment"><div id="post-52358-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff,</p><p>I did try out adding filters as u mentioned in bug12384, but no help either.</p><p>I was using my work laptop i will try accessing in my personal pc.</p><p>let you guys know if any update.</p></div><div id="comment-52358-info" class="comment-info"><span class="comment-age">(09 May '16, 11:30)</span> <span class="comment-user userinfo">prajwal</span></div></div><span id="52364"></span><div id="comment-52364" class="comment"><div id="post-52364-score" class="comment-score"></div><div class="comment-text"><p>What about the first question (do you have external name resolution enabled)?</p><p>One thing you could check is whether your PC is generating name requests--using Wireshark of course :-).</p></div><div id="comment-52364-info" class="comment-info"><span class="comment-age">(09 May '16, 11:58)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="52372"></span><div id="comment-52372" class="comment"><div id="post-52372-score" class="comment-score"></div><div class="comment-text"><p>I apologize if I underestimate you, but are the IP addresses you want to convert to hostnames public ones? I.e. does any PTR record actually exist for them anywhere? Even if they are public, what does <code>nslookup ip.add.re.ss</code> (Windows) or <code>dig -x ip.add.re.ss</code> (Linux) show for these addresses? Even some public addresses miss a PTR record in DNS so they cannot be resolved to hostnames.</p><p>Also, as you specifically mention Wireshark 2.0.3 and specific types of capture files (which don't sound like pcap or pcapng to me), the best thing would be if you could publish, login-free, an example of a real file you deal with in each of those formats somewhere (cloudshark is preferred by this site's community but may possibly not like non-pcap(ng) files, so in this particular case better use Dropbox, Google Drive, ...) and put links to them here. This should give us a better insight on the root cause of your issue.</p></div><div id="comment-52372-info" class="comment-info"><span class="comment-age">(09 May '16, 13:50)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52289" class="comment-tools"></div><div class="clear"></div><div id="comment-52289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52284"></span>

<div id="answer-container-52284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52284-score" class="post-score" title="current number of votes">-1</div><span id="post-52284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi prajwal,</p><p>Convert source and destination ip addresses to host names where?</p><p>If you mean in the WireShark Packet List pane, then go to Capture Interfaces &gt; Options tab &gt; Name Resolution and check "Resolve network names".</p><p>In short, it must be done in Capture &gt; Options &gt; Options tab &gt; Name Resolution before a particular capture, not just enabled globally in Edit &gt; Preferences.</p><p>This must be done before the capture is started.</p><p>This will actually create DNS "PTR" queries against whatever DNS resolvers you have configured in your operating system settings.</p><p>Hope this helps, Shawn</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '16, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/725945d72ff9d8d165919f75019c9084?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shawncarroll&#39;s gravatar image" /><p><span>shawncarroll</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shawncarroll has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 May '16, 13:32</strong> </span></p></div></div><div id="comments-container-52284" class="comments-container"><span id="52285"></span><div id="comment-52285" class="comment"><div id="post-52285-score" class="comment-score"></div><div class="comment-text"><p>I was opening files previously captured which I have downloaded on internet. Some suggested me that she saw other guy replacing them with hostname, we could also convert the source IP addresses in that files also, You are saying that it couldn't be done I will just inform her we can't unless its live capture.</p></div><div id="comment-52285-info" class="comment-info"><span class="comment-age">(06 May '16, 13:54)</span> <span class="comment-user userinfo">prajwal</span></div></div><span id="52287"></span><div id="comment-52287" class="comment"><div id="post-52287-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-52287-info" class="comment-info"><span class="comment-age">(06 May '16, 14:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52290"></span><div id="comment-52290" class="comment"><div id="post-52290-score" class="comment-score"></div><div class="comment-text"><p>As mentioned in my answer, there's normally no reason you need to enable name resolution while capturing; name resolution should work after a capture is done too.</p></div><div id="comment-52290-info" class="comment-info"><span class="comment-age">(06 May '16, 15:27)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-52284" class="comment-tools"></div><div class="clear"></div><div id="comment-52284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

