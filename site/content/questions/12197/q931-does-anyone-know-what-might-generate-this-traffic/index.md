+++
type = "question"
title = "Q.931 - Does anyone know what might generate this traffic?"
description = ''''''
date = "2012-06-26T12:44:00Z"
lastmod = "2012-06-27T09:53:00Z"
weight = 12197
keywords = [ "lapd", "q.931" ]
aliases = [ "/questions/12197" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Q.931 - Does anyone know what might generate this traffic?](/questions/12197/q931-does-anyone-know-what-might-generate-this-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12197-score" class="post-score" title="current number of votes">0</div><span id="post-12197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://dl.dropbox.com/u/15485524/udp3001.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lapd" rel="tag" title="see questions tagged &#39;lapd&#39;">lapd</span> <span class="post-tag tag-link-q.931" rel="tag" title="see questions tagged &#39;q.931&#39;">q.931</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/3f9e1251ccadd74f9f1e2a0b91854afe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="someitguy2012&#39;s gravatar image" /><p><span>someitguy2012</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="someitguy2012 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-12197" class="comments-container"></div><div id="comment-tools-12197" class="comment-tools"></div><div class="clear"></div><div id="comment-12197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="12210"></span>

<div id="answer-container-12210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12210-score" class="post-score" title="current number of votes">1</div><span id="post-12210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe it's just the Cisco RLM dissector getting a "false positive"; almost all the packets appear <em>not</em> to be LAPD-over-UDP, even if the dissector is treating them as such, given all the errors in the dissection. To quote a comment in that dissector:</p><pre><code>/*
 * RLM is a proprietary Cisco protocol used for centralling managing
 * many redundant NASes.  I don&#39;t know much about the format, but you
 * can read about the feature here:
 *
 * http://www.cisco.com/en/US/docs/ios/12_0t/12_0t3/feature/guide/rlm_123.html
 *
 * RLM runs on a UDP port (default 3000) between the MGC and the NAS.
 * On port N+1 (default 3001), a Q.931/LAPD/UDP connection is maintained.
 * Both sides use the same local port number for the connection, so source
 * and dest port are always the same.
 *
 * In large networks, the links are typically split onto higher ports,
 * so anything up to 3015 (or higher) could either be RLM or Q.931 traffic,
 * although always the RLM has the one lower port number for that RLM group.
 *
 * Multiple RLM groups are possible on a single NAS.
 *
 * I haven&#39;t been able to find the protocol documented, so I&#39;ve
 * guessed some of the fields based on the output of debug commands on
 * cisco NASes.
 *
 */</code></pre><p>The heuristic dissector's check is pretty weak - it just checks whether what would be the control field if the packet were LAPD-over-UDP looks "good enough", which could just mean that the first byte of the payload doesn't happen to have both bits set. That extremely weak check isn't done for arbitrary UDP traffic, but it <em>is</em> done where the source and destination port numbers are the same and are between 3001 and 3015.</p><p>Unfortunately, there's no way to disable that dissector. Perhaps we should add a way to disable it and should also attempt to strengthen the heuristic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12210" class="comments-container"></div><div id="comment-tools-12210" class="comment-tools"></div><div class="clear"></div><div id="comment-12210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12199"></span>

<div id="answer-container-12199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12199-score" class="post-score" title="current number of votes">0</div><span id="post-12199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could be some kind of VoIP solution. See here: <a href="http://wiki.wireshark.org/Q.931">http://wiki.wireshark.org/Q.931</a></p><p>Can you identify the device that used IP 192.168.0.254? Based on that information you might get an idea what generates Q.931 traffic (like a PBX with IP interface).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12199" class="comments-container"><span id="12202"></span><div id="comment-12202" class="comment"><div id="post-12202-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your info Kurt. I am trying to track the source device down. The 192.168.0.254 and 192.168.0.255 IPs don't make any sense, wondering if they are spoofed somehow. Is that a possibility?</p></div><div id="comment-12202-info" class="comment-info"><span class="comment-age">(26 Jun '12, 12:57)</span> <span class="comment-user userinfo">someitguy2012</span></div></div><span id="12203"></span><div id="comment-12203" class="comment"><div id="post-12203-score" class="comment-score"></div><div class="comment-text"><p>Address spoofing. Well.... possible, but I don't believe that. Why do you think those addresses don't make any sense? Don't you know them, or what is the reason?</p><p>BTW: The MAC addresses are both Cisco. Maybe one of them is a Cisco Call Manager? At least it supports Q.931 signaling. However, as I'm not a Cisco guru, I'm just guessing!</p></div><div id="comment-12203-info" class="comment-info"><span class="comment-age">(26 Jun '12, 13:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12199" class="comment-tools"></div><div class="clear"></div><div id="comment-12199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12209"></span>

<div id="answer-container-12209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12209-score" class="post-score" title="current number of votes">0</div><span id="post-12209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Q.931 is typically one layer below H.225 (H.323 VoIP signalling), unless you have some TDM traffic captured from a specialist TDM (ISDN) analyser, such as MtyEye.</p><p>The .255 address will be the broadcast address assuming the mask is 255.255.255.0 and .254 may well be the default gateway (hence Cisco MAC).</p><p>However, I cannot see why Q.931 traffic would be targetting the broadcast address.</p><p>What is the subnet mask?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-12209" class="comments-container"></div><div id="comment-tools-12209" class="comment-tools"></div><div class="clear"></div><div id="comment-12209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12234"></span>

<div id="answer-container-12234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12234-score" class="post-score" title="current number of votes">0</div><span id="post-12234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running Wireshark V1.8.0, if so, could it be worth checking the ISDN preference to ensure it is set to LAPD. There were some changes made by Guy in this area?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '12, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-12234" class="comments-container"><span id="12235"></span><div id="comment-12235" class="comment"><div id="post-12235-score" class="comment-score"></div><div class="comment-text"><p>That's probably not it - that preference for "ISDN" in the sense of a direct capture from an ISDN line, but what he's seeing is being dissected as LAPD over UDP when it is, I suspect, <em>not</em> LAPD over UDP, so either the purported LAPD frames are reported by the LAPD dissector as bad (that's what the "I, N(R)=X, N(S)=X [Malformed packet]" probably are) or they manage to get through the LAPD dissector but they get reported by the Q.931 dissector as bad (the others).</p></div><div id="comment-12235-info" class="comment-info"><span class="comment-age">(27 Jun '12, 09:53)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12234" class="comment-tools"></div><div class="clear"></div><div id="comment-12234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

