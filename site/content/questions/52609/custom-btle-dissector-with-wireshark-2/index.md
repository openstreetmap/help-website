+++
type = "question"
title = "custom BTLE dissector with wireshark 2"
description = '''I&#x27;m updating a dissector I wrote for a byte stream the Nordic BTLE sniffer puts out. I wrote it originally for 1.10 and now it&#x27;s time to make it available for Wireshark 2.  It registers as a USER10 wtap because it&#x27;s not a protocol you&#x27;d see out in the wild, it&#x27;s Nordic-specific. I have two small iss...'''
date = "2016-05-16T01:40:00Z"
lastmod = "2016-05-18T07:30:00Z"
weight = 52609
keywords = [ "nordic", "btle" ]
aliases = [ "/questions/52609" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [custom BTLE dissector with wireshark 2](/questions/52609/custom-btle-dissector-with-wireshark-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm updating a dissector I wrote for a byte stream the Nordic BTLE sniffer puts out. I wrote it originally for 1.10 and now it's time to make it available for Wireshark 2.</p><p>It registers as a USER10 wtap because it's not a protocol you'd see out in the wild, it's Nordic-specific. I have two small issues with the dissector now I've moved it to 2.0.</p><p>1) There's a btle_context structure which gives some information about CRC validation, information I do have. So I create one of those and pass it as data to the btle dissector, and that used to work. However now the btle dissector checks that the dissector above it is one of a set of specific dissectors, else it ignores the data, so the information about CRC doesn't get used. I can't add the nordic detector into the list of 'allowable parents' because it's 3rd party thing loaded just by people using Nordic's sniffer. Is there any way I can either pretend to be a dissector it recognises or otherwise get the btle dissector to use the context?</p><p>2) All the ATT messages show as 'UnknownDirection' because the p2p_dir is stripped from the pinfo by the btle dissector and replaced with 'unknown' before being passed to the lower dissectors. I can't really see why this is being done and I can't currently see a way around it. Have I missed something? The direction is known and was properly set in the pinfo.</p><p>Any pointers in the right direction would be helpful. The dissector works ok as it is, but it would be nice if it had the CRC info init and showed the ATT message direction properly.</p></div><div id="question-tags" class="tags-container tags">nordic btle</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/32b9484a7a9c2d4c347a1dae9db3d1fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rols&#39;s gravatar image" /><p>rols<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rols has no accepted answers">0%</span></p></div></div><div id="comments-container-52609" class="comments-container"></div><div id="comment-tools-52609" class="comment-tools"></div><div class="clear"></div><div id="comment-52609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52727"></span>

<div id="answer-container-52727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52727-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess this is this <a href="https://learn.adafruit.com/introducing-the-adafruit-bluefruit-le-sniffer/nordic-nrfsniffer">dissector</a>?</p><p>Hmm, this is probably a question best answered by Mr. Bluetooth (@Michal Labedzki) but I'll do my best...</p><ol><li>The BTLE dissector is doing this to <a href="https://code.wireshark.org/review/8512">know what structure is being passed in</a>. I'd suggest that this should be refactored so that, for example, the structure tells you what is being passed in. Besides being cleaner this would allow your dissector to work. I'd suggest <a href="https://bugs.wireshark.org">opening an enhancement request</a> (if you do, please reference this question and also report the number back here for cross-referencing purposes).</li><li>That came in with this <a href="https://code.wireshark.org/review/#/c/5771/">change</a>; looking at the diffs I suspect that the code is assuming that the underlying dissector isn't setting the direction correctly--which presumably yours is. I'd suggest asking this to be enhanced--probably in the same enhancement request as above.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52727" class="comments-container"><span id="52748"></span><div id="comment-52748" class="comment"><div id="post-52748-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that in-depth answer; I thought it was probably done to know whether the structure was valid or not as the BTLE detectors became more widely used, but didn't know of a good way to suggest passing that knowledge down without specifying parent detectors. I'll have a look through the codebase and see if there's a pattern for passing down information is valid like that which is generally used. I can think of several, like magic bytes etc, but I'm sure this requirement has been seen before and has a usual solution.</p><p>I get what you're saying about the direction field, and indeed quite a few of the encodings don't have that information, however you'd expect it already to be 'unknown' in that case. The way it is right now, the direction is correctly-used in the upper level dissector (master -&gt; Slave or vice versa) and then tossed away. There must be a use-case there from history which prompted the change.</p><p>And yes this is the nRF dissector, although not that version of it, it's the OSX one which I was bringing up to v2.0. It is so nice not to have to fiddle with X11 on OSX any more!</p><p>Let me hunt the codebase a little more and see if I can find a good pattern to suggest and then take this over to the enhancement site.</p><p>Thanks again for the answer, very helpful.</p></div><div id="comment-52748-info" class="comment-info"><span class="comment-age">(18 May '16, 17:16)</span> rols</div></div><span id="52749"></span><div id="comment-52749" class="comment"><div id="post-52749-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The way it is right now, the direction is correctly-used in the upper level dissector (master -&gt; Slave or vice versa) and then tossed away. There must be a use-case there from history which prompted the change.</p></blockquote><p>I'd guess that there's some scenario where BT is carried over some other protocol (possibly IP-based?) which sets its own direction which was somehow irrelevant to the BT direction. But that's a WAG.</p><p>And: you're welcome!</p></div><div id="comment-52749-info" class="comment-info"><span class="comment-age">(18 May '16, 17:58)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-52727" class="comment-tools"></div><div class="clear"></div><div id="comment-52727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

