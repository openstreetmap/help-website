+++
type = "question"
title = "Multiple occurrences filter for diameter"
description = '''Hi, I am trying to use tshark for filtering Diameter messages from a pcap file. I am using following command: tshark -n -t ad -T fields -E separator=, -E occurrence=a -E aggregator=: -E quote=s -e frame.number -e diameter.Result-Code -e diameter.resp_time -e diameter.hopbyhopid -e diameter.endtoendi...'''
date = "2011-05-30T22:21:00Z"
lastmod = "2011-06-01T23:38:00Z"
weight = 4291
keywords = [ "diameter", "filters" ]
aliases = [ "/questions/4291" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple occurrences filter for diameter](/questions/4291/multiple-occurrences-filter-for-diameter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4291-score" class="post-score" title="current number of votes">0</div><span id="post-4291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to use tshark for filtering Diameter messages from a pcap file. I am using following command:</p><p><code>tshark -n -t ad -T fields -E separator=, -E occurrence=a -E aggregator=: -E quote=s -e frame.number -e diameter.Result-Code -e diameter.resp_time -e diameter.hopbyhopid -e diameter.endtoendid -e frame.protocols -r output.txt</code></p><p>One of the output line is</p><p><code>'877','2001:2001',,'0x4e841c7a:0x4e841c80:0x4e841c8f','0xa38a5201:0xa38a5202:0xb13b2c71','eth:vlan:ip:tcp:diameter:diameter:diameter:diameter:diameter'</code></p><p>Now the problem is that this particular TCP packet has three Diameter packets, two with Result code = 2001 and another with Experimental code.</p><p>Looking at the above output, I am not able to distinguish which diameter packet has error or successful response.</p><p>Could you please help me on this? Is there any way to differentiate and print empty string for not matching condition.</p><p>Thanks &amp; Regards Nalin Vilochan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '11, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/a6bcb7a3851005d4a173e21e2946a82e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nalin&#39;s gravatar image" /><p><span>Nalin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nalin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '11, 18:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4291" class="comments-container"></div><div id="comment-tools-4291" class="comment-tools"></div><div class="clear"></div><div id="comment-4291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4323"></span>

<div id="answer-container-4323" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4323-score" class="post-score" title="current number of votes">0</div><span id="post-4323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The separator is ',', so the output line's items are:</p><pre><code>frame.number: &#39;877&#39;
diameter.Result-Code: &#39;2001:2001&#39;
diameter.resp_time:
diameter.hopbyhopid: &#39;0x4e841c7a:0x4e841c80:0x4e841c8f&#39;
diameter.endtoendid: &#39;0xa38a5201:0xa38a5202:0xb13b2c71&#39;
frame.protocols: &#39;eth:vlan:ip:tcp:diameter:diameter:diameter:diameter:diameter&#39;</code></pre><p>The aggregator is ':', which means that, for the Diameter items, the first item is the value in the first packet, the second item is the value in the second packet, and the third item is the value in the third packet. Unfortunately, from looking at the code, it appears that, if, for example, the middle Diameter packet doesn't have an instance of the field, it doesn't put in a extra aggregator to indicate that the middle value is what's missing, so a value of "2001:2001" could mean that the first two Diameter packets have a result code of 2001, the first and third diameter packets have a value of 2001, or the second and third diameter packets have a result code of 2001.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '11, 21:32</strong> </span></p></div></div><div id="comments-container-4323" class="comments-container"></div><div id="comment-tools-4323" class="comment-tools"></div><div class="clear"></div><div id="comment-4323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4328"></span>

<div id="answer-container-4328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4328-score" class="post-score" title="current number of votes">0</div><span id="post-4328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Internally in Wireshark, there is no relationship between multiple occurrences of one field to multiple occurrences of another field. It is therefor very hard if not impossible to change this, without changing the very nature of the Wireshark dissection engine.</p><p>However, you might be able to get what you want using the PDML output format of tshark (-T pdml) and then parse the XML formatted text.</p><p>You can also use <a href="http://wiki.wireshark.org/Mate">MATE</a> or <a href="http://wiki.wireshark.org/Lua">LUA</a> to achieve your goals...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4328" class="comments-container"></div><div id="comment-tools-4328" class="comment-tools"></div><div class="clear"></div><div id="comment-4328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

