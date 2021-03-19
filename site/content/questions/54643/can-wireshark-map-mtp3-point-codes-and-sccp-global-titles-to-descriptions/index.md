+++
type = "question"
title = "Can Wireshark map MTP3 point codes and SCCP Global Titles to descriptions?"
description = '''Hi ! I think it would be easy-to-do, and very usable feature of describe specified field values. Currently I am working a lot on SS7 packets, where MTP3(SPC,DPC) and SCCP(GT) are subjects, where description on specified value would help a lot. So for example, when displaying DPC: 1234  it would be  ...'''
date = "2016-08-08T03:26:00Z"
lastmod = "2016-08-11T06:53:00Z"
weight = 54643
keywords = [ "feature-request" ]
aliases = [ "/questions/54643" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark map MTP3 point codes and SCCP Global Titles to descriptions?](/questions/54643/can-wireshark-map-mtp3-point-codes-and-sccp-global-titles-to-descriptions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54643-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>I think it would be easy-to-do, and very usable feature of describe specified field values. Currently I am working a lot on SS7 packets, where MTP3(SPC,DPC) and SCCP(GT) are subjects, where description on specified value would help a lot. So for example, when displaying</p><pre><code>DPC: 1234</code></pre><p>it would be</p><pre><code>DPC: 1234 (my description entered)</code></pre><p>What do you think ?</p><p>BR Alex</p></div><div id="question-tags" class="tags-container tags">feature-request</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/049954c19a42f88823709640897cb958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmediukas&#39;s gravatar image" /><p>ahmediukas<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmediukas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Aug '16, 17:07</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-54643" class="comments-container"></div><div id="comment-tools-54643" class="comment-tools"></div><div class="clear"></div><div id="comment-54643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54648"></span>

<div id="answer-container-54648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54648-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>So generically, what you ask for is a name resolution for other than IP and MAC addresses, using a user-provided configuration file, right?</p><p>For the point code at MTP level, it wouldn't be so complex; for the SCP's Calling and Called Party Addresses, this could be a nightmare due to their flexible structure - point code, SSN, global title may all be present or absent in the complete address, and the global title's address space (numbering plan identifier) may be E.212, E.164 or even other. And you might need translation of prefixes because the GT is sometimes a single subscriber's address, not GMSC's or VLR's.</p><p>In any case, this site is not the right place for such requirement - you should file an Enhancement request (bug with severity Enhancement) on <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi?product=Wireshark">Wireshark Bugzilla</a>.</p><p>If it may help you <strong>as a quick workaround</strong>, try using the coloring rules - you can use any display filter as a trigger for assigning a color scheme to the frame in the packet list. But your color perception has to be good enough to distinguish between enough color combinations (background + foreground).</p><p>Also, you may want to write a Lua post-dissector which would contain the translation table and generate additional filterable meta-fields with the names.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Aug '16, 05:55</p></div></div><div id="comments-container-54648" class="comments-container"><span id="54650"></span><div id="comment-54650" class="comment"><div id="post-54650-score" class="comment-score"></div><div class="comment-text"><p>Whenever a user (Wireshark or otherwise) suggests a change is "very easy to do", I expect to see the patch attached. I'm usually disappointed.</p></div><div id="comment-54650-info" class="comment-info"><span class="comment-age">(08 Aug '16, 05:24)</span> grahamb ♦</div></div><span id="54681"></span><div id="comment-54681" class="comment"><div id="post-54681-score" class="comment-score"></div><div class="comment-text"><p>Another possible "enhancement" approach to this would be to give the option within the MTP3 protocol preferences to enable/disable the code which pushes point codes into the "source" and "destination" columns to begin with.</p><p>If that was a configurable option, a user could pretty much accomplish this task by disabling that feature and writing IP host file entries for all the IPs which map to an MTP3 point code, using the already-written IP host resolver code of Wireshark to map point codes to named sources/destinations.</p><p>Of course, if it's an M2PA passthrough or you're doing PC translation rather than GT/SSN routing then you might have the same point code crossing two IP legs, but in that case you could at least define a given STP as a source/destination in the resolver. Not completely what you're asking for, but since it would just be a toggle to "disable" a feature which is already built into MTP3 (a feature which denies us the ability to resolve the IP-level source/destination info in the Source/Destination columns for MTP3-dissected frames), I <em>think</em> that would be easy. :)</p></div><div id="comment-54681-info" class="comment-info"><span class="comment-age">(08 Aug '16, 18:23)</span> Quadratic</div></div><span id="54682"></span><div id="comment-54682" class="comment"><div id="post-54682-score" class="comment-score"></div><div class="comment-text"><p>Oh, and aside from the above reasons for why SCCP would be messy for something like this, consider that Sigtran implementations would normally concatenate many SCCP-level messages over a single IP packet, so a best-case result would probably have to be similar to column field values ("first", "last", or "all"), making it kind of useless for following a transaction even if the code gets it all right.</p><p>And that's to say nothing about the problem of inconsistent uses of GT translation for DPC's even within a single dialogue (eg: many GSN/VLR implementations will use E.212 GT for an initial address to HLR, then flip to E.164 GT of the HLR directly for the next TCAP transaction, mid-dialogue, based on MM/GMM state of the IMSI).</p></div><div id="comment-54682-info" class="comment-info"><span class="comment-age">(08 Aug '16, 18:44)</span> Quadratic</div></div><span id="55100"></span><div id="comment-55100" class="comment"><div id="post-55100-score" class="comment-score"></div><div class="comment-text"><p>If wireshark can translate value of GT (or ANY other fields) in proper form, it means it knows the value, no matter what it is. So description table (protocol.field.value=description) can help a lot. Not just within SS7. For example, I have some own specific protocols, which could such table help me as well). Due various form of protocols use, I know it can't be bulletproof on results, but still can be usefull to lookup into table and add description near value if found. Such implementation I guess can't be such a pain, have such code in my own shark (limited to some other old protocols). Btw, SS7 was just an example, since I'm currently working lot on it.</p></div><div id="comment-55100-info" class="comment-info"><span class="comment-age">(24 Aug '16, 14:59)</span> ahmediukas</div></div></div><div id="comment-tools-54648" class="comment-tools"></div><div class="clear"></div><div id="comment-54648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54743"></span>

<div id="answer-container-54743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you're looking for <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7592">bug 7592</a>. It requests translation from (SS7) PCs to names. (Now we just need someone with the time and inclination to implement that enhancement request...)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '16, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54743" class="comments-container"></div><div id="comment-tools-54743" class="comment-tools"></div><div class="clear"></div><div id="comment-54743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

