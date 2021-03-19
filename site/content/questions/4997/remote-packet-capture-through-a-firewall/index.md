+++
type = "question"
title = "Remote packet capture through a firewall"
description = '''I am trying to set up a remote packet capture on a device that is natted behind a firewall. I have forwarded port 2002 to the device. I get a list of interfaces but when I start the capture i get no data. It says that there is an active capture running but no packets captured. then It errors out wit...'''
date = "2011-07-12T13:20:00Z"
lastmod = "2011-07-14T01:52:00Z"
weight = 4997
keywords = [ "firewall", "capture", "remote" ]
aliases = [ "/questions/4997" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote packet capture through a firewall](/questions/4997/remote-packet-capture-through-a-firewall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4997-score" class="post-score" title="current number of votes">0</div><span id="post-4997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to set up a remote packet capture on a device that is natted behind a firewall. I have forwarded port 2002 to the device. I get a list of interfaces but when I start the capture i get no data. It says that there is an active capture running but no packets captured. then It errors out with the following message:</p><hr /><p>No packets captured!</p><p>As no data was captured, closing the temporary capture file!</p><p>Help about capturing can be found at:</p><pre><code>   http://wiki.wireshark.org/CaptureSetup</code></pre><p>Wireless (Wi-Fi/WLAN): Try to switch off promiscuous mode in the Capture Options!</p><hr /><p>Error while capturing packets: Is the server properly installed on 98.190.240.71? connect() failed: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond. (</p><p>Please report this to the Wireshark developers. (This is not a crash; please do not report it as such.)</p><hr /><p>Any help with this would be greatly appreciated. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '11, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/71e7606af3fccb4b9385ea7bac37f4f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kkarl528&#39;s gravatar image" /><p><span>kkarl528</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kkarl528 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jul '11, 20:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4997" class="comments-container"><span id="5006"></span><div id="comment-5006" class="comment"><div id="post-5006-score" class="comment-score"></div><div class="comment-text"><p>Which version of WinPcap are you running? Note that the Wireshark <a href="http://wiki.wireshark.org/CaptureSetup/WinPcapRemote">WinPcapRemote</a> page indicates that WinPcap 3.1 does not work. If you're not running the latest version of <a href="http://www.winpcap.org/install/default.htm">WinPcap</a>, version 4.1.2 as of this writing, I'd recommend that you upgrade.</p></div><div id="comment-5006-info" class="comment-info"><span class="comment-age">(12 Jul '11, 20:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-4997" class="comment-tools"></div><div class="clear"></div><div id="comment-4997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5009"></span>

<div id="answer-container-5009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5009-score" class="post-score" title="current number of votes">0</div><span id="post-5009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Remote packet capture isn't support on NAT'ed connections. The reasons are:</p><ol><li>'NAT is evil', since it requires an protocol specific helper to pick up the 'start capture reply' and setup a port forwarding for that.</li><li>Invoking remote capture in client mode isn't supported by Wireshark</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '11, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5009" class="comments-container"><span id="5014"></span><div id="comment-5014" class="comment"><div id="post-5014-score" class="comment-score"></div><div class="comment-text"><p>Would it work using <a href="http://www.winpcap.org/docs/docs_412/html/group__remote.html">active mode</a> with <a href="http://analyzer.polito.it/">Analyzer</a> instead of Wireshark?</p></div><div id="comment-5014-info" class="comment-info"><span class="comment-age">(13 Jul '11, 05:13)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="5018"></span><div id="comment-5018" class="comment"><div id="post-5018-score" class="comment-score"></div><div class="comment-text"><p>Its description says so...</p></div><div id="comment-5018-info" class="comment-info"><span class="comment-age">(13 Jul '11, 06:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="5021"></span><div id="comment-5021" class="comment"><div id="post-5021-score" class="comment-score"></div><div class="comment-text"><p>Right, but I didn't know if anyone ever actually tried this and knew for sure if it would work or not. I guess kkarl528 can tell us for sure if he tries it. And if it does work, then this might be a candidate enhancement feature for Wireshark if anyone cares to file a bug report for it.</p></div><div id="comment-5021-info" class="comment-info"><span class="comment-age">(13 Jul '11, 07:03)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="5041"></span><div id="comment-5041" class="comment"><div id="post-5041-score" class="comment-score"></div><div class="comment-text"><p>I'm sure I've seen the request before. Now for someone to program it...</p></div><div id="comment-5041-info" class="comment-info"><span class="comment-age">(14 Jul '11, 01:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-5009" class="comment-tools"></div><div class="clear"></div><div id="comment-5009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

