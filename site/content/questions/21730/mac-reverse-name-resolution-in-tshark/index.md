+++
type = "question"
title = "MAC (reverse) name resolution in tshark"
description = '''Hi, I have few MAC addresses where the OUI portions have been resolved: e.g. Intel_05:04:03. Is it possible to use tshark to get the actual MAC address for each of my “name resolved” address? E.g. get 02:A0:C9:05:04:03 from Intel_05:04:03? If this is not possible with tshark, what would would be the...'''
date = "2013-06-03T23:52:00Z"
lastmod = "2013-10-15T07:01:00Z"
weight = 21730
keywords = [ "mac", "resolution", "tshark", "name" ]
aliases = [ "/questions/21730" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [MAC (reverse) name resolution in tshark](/questions/21730/mac-reverse-name-resolution-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21730-score" class="post-score" title="current number of votes">1</div><span id="post-21730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have few MAC addresses where the OUI portions have been resolved: e.g. Intel_05:04:03.</p><p>Is it possible to use tshark to get the actual MAC address for each of my “name resolved” address? E.g. get 02:A0:C9:05:04:03 from Intel_05:04:03?</p><p>If this is not possible with tshark, what would would be the easiest way to achieve this on a linux host?</p><p>Many thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '13, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/518b5c85459f044af665d96d4288fda7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsblvd&#39;s gravatar image" /><p><span>wsblvd</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsblvd has no accepted answers">0%</span></p></div></div><div id="comments-container-21730" class="comments-container"></div><div id="comment-tools-21730" class="comment-tools"></div><div class="clear"></div><div id="comment-21730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21746"></span>

<div id="answer-container-21746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21746-score" class="post-score" title="current number of votes">3</div><span id="post-21746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wsblvd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using the unresolved and resolved hw address as columns would do the trick, however, it seems that there is a bug that prevents simultaneous diplay of the resolved and unresolved addresses:</p><pre><code>$ ./tshark -lr ../pcap/http.cap -o column.format:&quot;rhs&quot;,&quot;%rhs&quot;,&quot;uhs&quot;,&quot;%uhs&quot; | sort | uniq
Apple_d8:87:48 Apple_d8:87:48
JuniperN_bb:d1:3b JuniperN_bb:d1:3b
$</code></pre><p>I will have a look at why this is...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21746" class="comments-container"><span id="21751"></span><div id="comment-21751" class="comment"><div id="post-21751-score" class="comment-score">2</div><div class="comment-text"><p>Fixed in revision 49776 which will be included in the next 1.8 release.</p><pre><code>$ ./tshark -lr clean-test02.cap -o column.format:&quot;rhs&quot;,&quot;%rhs&quot;,&quot;uhs&quot;,&quot;%uhs&quot; | sort | uniq
Cisco_8f:2c:95 00:19:2f:8f:2c:95
Cisco_fe:1b:02 00:0b:fc:fe:1b:02
Dell_fc:92:7d 00:1e:4f:fc:92:7d
$</code></pre></div><div id="comment-21751-info" class="comment-info"><span class="comment-age">(04 Jun '13, 14:51)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21752"></span><div id="comment-21752" class="comment"><div id="post-21752-score" class="comment-score"></div><div class="comment-text"><p>BTW Once Wireshark has resolved the mac-address, there is no (guaranteed) way back, as multiple OUI's can point to the same vendor. See the example in my last comment where both 00:19:2f:xx:xx:xx and 00:0b:fc:xx:xx:xx resolved to "Cisco".</p></div><div id="comment-21752-info" class="comment-info"><span class="comment-age">(04 Jun '13, 14:54)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21761"></span><div id="comment-21761" class="comment"><div id="post-21761-score" class="comment-score"></div><div class="comment-text"><p>Many thanks for the help.</p></div><div id="comment-21761-info" class="comment-info"><span class="comment-age">(05 Jun '13, 05:53)</span> <span class="comment-user userinfo">wsblvd</span></div></div><span id="26002"></span><div id="comment-26002" class="comment"><div id="post-26002-score" class="comment-score"></div><div class="comment-text"><p>Hi both, i'm getting a similar problem... would you mind to take a look to this other thread?Thanks in advance!</p><p><a href="http://ask.wireshark.org/questions/26001/show-untranslated-and-translated-mac-addresses-in-different-columns-at-the-time">http://ask.wireshark.org/questions/26001/show-untranslated-and-translated-mac-addresses-in-different-columns-at-the-time</a></p></div><div id="comment-26002-info" class="comment-info"><span class="comment-age">(15 Oct '13, 07:01)</span> <span class="comment-user userinfo">legramo</span></div></div></div><div id="comment-tools-21746" class="comment-tools"></div><div class="clear"></div><div id="comment-21746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21736"></span>

<div id="answer-container-21736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21736-score" class="post-score" title="current number of votes">0</div><span id="post-21736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can turn MAC resolution off, edit-&gt;preferences-&gt;name resolution, untick resolve MAC addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-21736" class="comments-container"><span id="21744"></span><div id="comment-21744" class="comment"><div id="post-21744-score" class="comment-score"></div><div class="comment-text"><p>Many thanks for the suggestions but I already have these addresses that have been “resolved”. What can be done to get the actual MAC address? I was wondering if there was a convenient way to get the Ethernet manufacturer codes of these addresses without having to search /etc/manuf.</p></div><div id="comment-21744-info" class="comment-info"><span class="comment-age">(04 Jun '13, 12:13)</span> <span class="comment-user userinfo">wsblvd</span></div></div><span id="21745"></span><div id="comment-21745" class="comment"><div id="post-21745-score" class="comment-score"></div><div class="comment-text"><p>Oh, yeah, in that case you'd have to reverse-map them from (preferably) Wireshark's manuf file. You'd have to do that manually or (more likely) write a script to do it.</p><p>Wireshark's manuf file is in /usr/share/wireshark/manuf (assuming Wireshark was installed in /usr).</p></div><div id="comment-21745-info" class="comment-info"><span class="comment-age">(04 Jun '13, 12:27)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="21762"></span><div id="comment-21762" class="comment"><div id="post-21762-score" class="comment-score"></div><div class="comment-text"><p>Many thanks Jeff.</p></div><div id="comment-21762-info" class="comment-info"><span class="comment-age">(05 Jun '13, 05:55)</span> <span class="comment-user userinfo">wsblvd</span></div></div></div><div id="comment-tools-21736" class="comment-tools"></div><div class="clear"></div><div id="comment-21736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21739"></span>

<div id="answer-container-21739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21739-score" class="post-score" title="current number of votes">0</div><span id="post-21739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can also control whether this resolution happens in the first place with tshark's "-N" option (see the man page for details).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-21739" class="comments-container"></div><div id="comment-tools-21739" class="comment-tools"></div><div class="clear"></div><div id="comment-21739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

