+++
type = "question"
title = "Association Request and Response Packet?"
description = '''Association Request packet shows which power mode I have enabled in my Intel 6300 client laptop.  It shows in my wireshark capture:  SM Power save mode disabled (0x0003) for High performance mode. Dynamic SM Power save mode (0x0001) for Power Save mode.  But in Association response packet which is o...'''
date = "2015-08-05T00:23:00Z"
lastmod = "2015-08-05T16:53:00Z"
weight = 44854
keywords = [ "frame", "powersave", "mode", "ht", "wireshark" ]
aliases = [ "/questions/44854" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Association Request and Response Packet?](/questions/44854/association-request-and-response-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44854-score" class="post-score" title="current number of votes">0</div><span id="post-44854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong><em>Association Request packet</em></strong> shows which power mode I have enabled in my Intel 6300 client laptop.</p><p>It shows in my wireshark capture:</p><ol><li><strong>SM Power save mode disabled</strong> (0x0003) for <strong>High performance mode.</strong></li><li><strong>Dynamic SM Power save mode</strong> (0x0001) for <strong>Power Save mode.</strong></li></ol><p>But in <strong><em>Association response packet</em></strong> which is obtained from the Access point, it shows:</p><ol><li><strong>SM Power save mode disabled</strong> (0x0003) for <strong>High performance mode.</strong></li><li><strong>SM Power save mode disabled</strong> (0x0003) for <strong>Power Save mode.</strong></li></ol><p>Refer IEEE 802.11 wireless LAN management frame -&gt; Tagged parameters -&gt; Tag: HT Capabilities -&gt; HT Capabilities Info -&gt; HT SM Power save.</p><p><strong><em>EDIT:</em></strong></p><p>Is this normal or is something wrong in the setup?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-powersave" rel="tag" title="see questions tagged &#39;powersave&#39;">powersave</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span> <span class="post-tag tag-link-ht" rel="tag" title="see questions tagged &#39;ht&#39;">ht</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/6c2eccb0ac05aad1c712a709d07d00d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_geek&#39;s gravatar image" /><p><span>wireshark_geek</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_geek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '15, 00:25</strong> </span></p></div></div><div id="comments-container-44854" class="comments-container"><span id="44864"></span><div id="comment-44864" class="comment"><div id="post-44864-score" class="comment-score"></div><div class="comment-text"><p>Are you changing something on the Intel 6300 laptop to configure the HT Power save mode from "Disabled" to "Dynamic SM"?</p><p>According to the IEEE 802.11-2012 specification, section 8.4.2.58.2, bit2 and bit3 are used to broadcast a device's SM Power Save capability.</p><ol><li><p>Set to 0 for static SM power save mode</p></li><li><p>Set to 1 for dynamic SM power save mode</p></li></ol><p>3.Set to 3 for SM Power Save disabled</p></div><div id="comment-44864-info" class="comment-info"><span class="comment-age">(05 Aug '15, 06:19)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-44854" class="comment-tools"></div><div class="clear"></div><div id="comment-44854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44895"></span>

<div id="answer-container-44895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44895-score" class="post-score" title="current number of votes">0</div><span id="post-44895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your AP does not support (or is not configured to support) SM power save mode. You will need to reconfigure the AP to support power save mode.</p><p>The Association request from the Intel laptop only advertises its capability. In response, the AP will advertise its capabilities. If one does not support a feature, then that feature cannot be used after association occurs.</p><p>Since the AP does not support SM power save, it does not matter how you configure the laptop. It cannot use SM power save when connected to that AP (WiFi network).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44895" class="comments-container"></div><div id="comment-tools-44895" class="comment-tools"></div><div class="clear"></div><div id="comment-44895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

