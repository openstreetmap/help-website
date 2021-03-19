+++
type = "question"
title = "Right interface to use with tshark under windows"
description = '''In linux I use ifconfig to figure out which interface to listen to when capturing packets I know tshark -D gives me an interface list, but how can I know which one maps to which network? $ /cygdrive/c/Program&#92; Files/Wireshark/tshark.exe -D  1. &#92;Device&#92;NPF_{0B6A8C2B-B33C-4D84-9EAC-486FA6DCE537} (Micr...'''
date = "2013-04-17T23:19:00Z"
lastmod = "2013-04-18T08:35:00Z"
weight = 20545
keywords = [ "windows", "tshark" ]
aliases = [ "/questions/20545" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Right interface to use with tshark under windows](/questions/20545/right-interface-to-use-with-tshark-under-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20545-score" class="post-score" title="current number of votes">0</div><span id="post-20545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In linux I use ifconfig to figure out which interface to listen to when capturing packets</p><p>I know <code>tshark -D</code> gives me an interface list, but how can I know which one maps to which network?</p><pre><code>$ /cygdrive/c/Program\ Files/Wireshark/tshark.exe -D
 1. \Device\NPF_{0B6A8C2B-B33C-4D84-9EAC-486FA6DCE537} (Microsoft)
 2. \Device\NPF_{A0C97C2A-33C3-4EDD-A257-A19E6F70D0A6} (Intel(R) 82579LM Gigabit Network Connection)</code></pre><p>I am specifically interested in recording traffic received from a specific peer. In linux my script creates a temporary socket just to use <code>netstat</code> and get the local address used with that connection, then I use ifconfig to figure out the interface name used that has that local address. I am not quite sure how to correlate the interface names listed in <code>tshark -D</code> with the ones listed in <code>ipconfig</code>...</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '13, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/7a51402ac094b2e3e2fd676b5e498191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nhed&#39;s gravatar image" /><p><span>nhed</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nhed has no accepted answers">0%</span></p></div></div><div id="comments-container-20545" class="comments-container"></div><div id="comment-tools-20545" class="comment-tools"></div><div class="clear"></div><div id="comment-20545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20551"></span>

<div id="answer-container-20551" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20551-score" class="post-score" title="current number of votes">4</div><span id="post-20551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nhed has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use dumpcap with option -M. That will print the IP address of the interfaces (unfortunately tshark does not know -M).</p><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>Example:</p><pre><code>1. \Device\NPF_GenericDialupAdapter             Adapter for generic dialup and VPN capture network
2. \Device\NPF_{A3940B42-C4FC-408A-992A-4950283AFE0D}   VMware Accelerated AMD PCNet Adapter (Microsoft&#39;s Packet Scheduler) LAN-Verbindung 192.168.158.139 network</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '13, 01:31</strong> </span></p></div></div><div id="comments-container-20551" class="comments-container"><span id="20553"></span><div id="comment-20553" class="comment"><div id="post-20553-score" class="comment-score">1</div><div class="comment-text"><p>And so we learn something new every day :-)</p></div><div id="comment-20553-info" class="comment-info"><span class="comment-age">(18 Apr '13, 01:37)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="20556"></span><div id="comment-20556" class="comment"><div id="post-20556-score" class="comment-score">1</div><div class="comment-text"><p>That's one reason why I'm here. Learning new things about a tool I'm using for quite some time ;-)</p></div><div id="comment-20556-info" class="comment-info"><span class="comment-age">(18 Apr '13, 01:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20569"></span><div id="comment-20569" class="comment"><div id="post-20569-score" class="comment-score">2</div><div class="comment-text"><p>Is there any reason not to just dispense with the -M option and modify -D, -L and -S to simply print the added information that -M would have supplied? (Well actually, I'm not sure what, if anything, -M adds to the -S output, despite the help indicating, somewhat cryptically in my opinion that, "for -D, -L, and -S, produce machine-readable output".) And then of course, for tshark and wireshark to also display that added information in their -D and -L output as well.</p></div><div id="comment-20569-info" class="comment-info"><span class="comment-age">(18 Apr '13, 06:09)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="20573"></span><div id="comment-20573" class="comment"><div id="post-20573-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there any reason not to just dispense with the -M option and modify -D, -L and -S to simply print the added information that -M would have supplied?</p></blockquote><p>+1</p><blockquote><p>I'm not sure what, if anything, -M adds to the -S output,</p></blockquote><p>it prevents the header from being printed. Why is that better 'machine readable'? O.K. you don't have to handle that header, but skipping one line of input is not unsolvable ;-)</p><p>BTW: from the file dumpcap.c.</p><p>a comment of print_machine_readable_interfaces() says:</p><blockquote><p>The actual output of this function can be viewed with the command "dumpcap -D -Z none"</p></blockquote><p>apparently, the output of 'dumpcap -D -M' is identical to 'dumpcap -D -Z none'.</p></div><div id="comment-20573-info" class="comment-info"><span class="comment-age">(18 Apr '13, 07:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20578"></span><div id="comment-20578" class="comment"><div id="post-20578-score" class="comment-score"></div><div class="comment-text"><p>OK, well -M has been around for a while now, since <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=22367">r22367</a>, so I'll let those more familiar with it comment as to whether or not it's acceptable to remove it and change the -D, -M and -S behavior.</p></div><div id="comment-20578-info" class="comment-info"><span class="comment-age">(18 Apr '13, 08:35)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-20551" class="comment-tools"></div><div class="clear"></div><div id="comment-20551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20547"></span>

<div id="answer-container-20547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20547-score" class="post-score" title="current number of votes">0</div><span id="post-20547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <code>ipconfig /All</code> to list the interfaces, it will show you the uuid (0B6A8C2B-B33C-4D84-9EAC-486FA6DCE537 and A0C97C2A-33C3-4EDD-A257-A19E6F70D0A6 in your example) together with the IP settings</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20547" class="comments-container"><span id="20570"></span><div id="comment-20570" class="comment"><div id="post-20570-score" class="comment-score"></div><div class="comment-text"><p>Sorry ... no correlation that I can see ...</p></div><div id="comment-20570-info" class="comment-info"><span class="comment-age">(18 Apr '13, 07:10)</span> <span class="comment-user userinfo">nhed</span></div></div></div><div id="comment-tools-20547" class="comment-tools"></div><div class="clear"></div><div id="comment-20547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

