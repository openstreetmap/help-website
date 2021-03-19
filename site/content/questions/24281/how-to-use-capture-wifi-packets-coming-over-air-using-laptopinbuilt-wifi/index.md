+++
type = "question"
title = "how to use capture wifi packets coming over air using laptop(inbuilt wifi)"
description = '''I want to use wireshark software on windows 7 without external pcap dongle.'''
date = "2013-09-02T05:18:00Z"
lastmod = "2013-09-03T23:40:00Z"
weight = 24281
keywords = [ "wireshark" ]
aliases = [ "/questions/24281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use capture wifi packets coming over air using laptop(inbuilt wifi)](/questions/24281/how-to-use-capture-wifi-packets-coming-over-air-using-laptopinbuilt-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24281-score" class="post-score" title="current number of votes">0</div><span id="post-24281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use wireshark software on windows 7 without external pcap dongle.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '13, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/634de624016a65c5bce28ae7f3a9bfdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maheshbabu&#39;s gravatar image" /><p><span>maheshbabu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maheshbabu has no accepted answers">0%</span></p></div></div><div id="comments-container-24281" class="comments-container"></div><div id="comment-tools-24281" class="comment-tools"></div><div class="clear"></div><div id="comment-24281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24282"></span>

<div id="answer-container-24282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24282-score" class="post-score" title="current number of votes">3</div><span id="post-24282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the Windows section of this page <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a> for some info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-24282" class="comments-container"><span id="24303"></span><div id="comment-24303" class="comment"><div id="post-24303-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, changing the 802.11 capture modes is very platform/network adapter/driver/libpcap dependent, and might not be possible at all (Windows is very limited here).</p><p>Windows section explains capturing wlan packets using external adapters(Airpcap or intel)</p></div><div id="comment-24303-info" class="comment-info"><span class="comment-age">(03 Sep '13, 05:23)</span> <span class="comment-user userinfo">maheshbabu</span></div></div><span id="24311"></span><div id="comment-24311" class="comment"><div id="post-24311-score" class="comment-score"></div><div class="comment-text"><p>You can probably still capture wireless data packets with your internal adapter; you just won't get the WLAN management, etc. frames and you'll get fake Ethernet headers. If that's not good enough to meet your needs, then you'll have to look for an alternate solution.</p><p>If you're not willing or able to purchase an Airpcap adapter, then just about the only other thing I can think of (which may or may not work) is to install a Linux VM on your Windows machine and see if capturing from within the Linux VM gives you what you want. This is a technique used for <a href="http://wiki.wireshark.org/CaptureSetup/USB">USB capturing</a>; I don't know if it will work for WLAN too. Your level of success may depend on your wireless chipset.</p></div><div id="comment-24311-info" class="comment-info"><span class="comment-age">(03 Sep '13, 08:09)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="24312"></span><div id="comment-24312" class="comment"><div id="post-24312-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(Windows is very <strong>limited</strong> here).</p></blockquote><p>You may have missed the important part, thus I rephrase it here.</p><blockquote><p>Cite: <strong>Monitor mode</strong> is <strong>not supported by WinPcap</strong>, and thus <strong>not by Wireshark or TShark, on Windows</strong>.</p></blockquote><p>So, no luck on Windows without special hardware (Airpcap), at least for monitor mode (sniffing traffic of other nodes).</p></div><div id="comment-24312-info" class="comment-info"><span class="comment-age">(03 Sep '13, 08:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24313"></span><div id="comment-24313" class="comment"><div id="post-24313-score" class="comment-score"></div><div class="comment-text"><p>But from within a Linux VM, would the Linux driver be able to place the adapter into monitor mode (assuming the adapter is supported for Linux)? WinPcap wouldn't apply in this case, right?</p><p>In any case, maybe using <a href="http://blogs.technet.com/b/netmon/">Microsoft Network Monitor</a> instead of Wireshark is the way to go. See Guy's answer to <a href="http://ask.wireshark.org/questions/2702/monitor-mode-problem">this</a> question.</p></div><div id="comment-24313-info" class="comment-info"><span class="comment-age">(03 Sep '13, 08:40)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="24326"></span><div id="comment-24326" class="comment"><div id="post-24326-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But from within a Linux VM, would the Linux driver be able to place the adapter into monitor mode (assuming the adapter is supported for Linux)? WinPcap wouldn't apply in this case, right?</p></blockquote><p>If the virtual machine is running, and you tell the VM software (VMware Workstation, Parallels Workstation, VirtualBox) to attach the adapter to the virtual machine rather than to the Windows host, you should be able to capture in monitor mode on the Linux virtual machine, if there's a Linux driver for it and it supports monitor mode.</p></div><div id="comment-24326-info" class="comment-info"><span class="comment-age">(03 Sep '13, 22:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24328"></span><div id="comment-24328" class="comment not_top_scorer"><div id="post-24328-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But from within a Linux VM, would the Linux driver be able to place the adapter into monitor mode (assuming the adapter is supported for Linux)? WinPcap wouldn't apply in this case, right?</p></blockquote><p>As the OP mentioned inbuilt adapters (he does not want to use external 'dongles') the answer would be:</p><ul><li>with an inbuilt adapter it will not work with a virtual machine, as you cannot map arbitrary hardware into a virtual machine</li><li>with a USB adapter it will work (based on personal experience with VMware - other virtualization tools may work as well) as you can map a USB device into the virtual machine. The Forum of Kali, BackTrack and Aircrack-NG list several USB wifi adapters that support monitor mode.</li></ul><p>Maybe the OP simply does not want to use an 'expensive' external WLAN adapter (AirPcap) and did not think about cheap USB adapters.</p></div><div id="comment-24328-info" class="comment-info"><span class="comment-age">(03 Sep '13, 23:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24282" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-24282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

