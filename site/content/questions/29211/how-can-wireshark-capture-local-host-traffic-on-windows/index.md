+++
type = "question"
title = "How can wireshark capture local host traffic on Windows?"
description = '''I&#x27;m using Visual Basic 2010 for client/server authentication. I want the information that is transferred during that time between client and server. Is it possible that Wireshark is able to display it?'''
date = "2014-01-27T19:54:00Z"
lastmod = "2020-01-30T11:31:00Z"
weight = 29211
keywords = [ "windows", "localhost", "wireshark" ]
aliases = [ "/questions/29211" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can wireshark capture local host traffic on Windows?](/questions/29211/how-can-wireshark-capture-local-host-traffic-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29211-score" class="post-score" title="current number of votes">1</div><span id="post-29211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Visual Basic 2010 for client/server authentication. I want the information that is transferred during that time between client and server. Is it possible that Wireshark is able to display it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/63bfbe820ad83cc49c8e5eb6eec272d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vikramd&#39;s gravatar image" /><p><span>vikramd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vikramd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '14, 08:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-29211" class="comments-container"></div><div id="comment-tools-29211" class="comment-tools"></div><div class="clear"></div><div id="comment-29211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="29269"></span>

<div id="answer-container-29269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29269-score" class="post-score" title="current number of votes">3</div><span id="post-29269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> wiki page does mention <a href="http://www.netresec.com/?page=RawCap">RawCap</a>, it perhaps should expand on its use. For example, if you want to view live traffic in Wireshark, you can still do it by running <a href="http://www.netresec.com/?page=RawCap">RawCap</a> from one command-line and running Wireshark from another. Assuming you have <a href="http://www.cygwin.com/">cygwin</a>'s <a href="http://linux.die.net/man/1/tail"><code>tail</code></a> available, this could be accomplished using something like so:</p><p><strong>cmd1</strong>: <code>RawCap.exe -f 127.0.0.1 dumpfile.pcap</code></p><p><strong>cmd2</strong>: <code>tail -c +0 -f dumpfile.pcap | Wireshark.exe -k -i -</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-29269" class="comments-container"><span id="29270"></span><div id="comment-29270" class="comment"><div id="post-29270-score" class="comment-score"></div><div class="comment-text"><p>Couldn't a pipe be used?</p></div><div id="comment-29270-info" class="comment-info"><span class="comment-age">(29 Jan '14, 08:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="29272"></span><div id="comment-29272" class="comment"><div id="post-29272-score" class="comment-score"></div><div class="comment-text"><p>Ideally, but in practice, it doesn't work ... at least not in my testing. Perhaps the Netresec folks would be willing to modify RawCap to be able to write to a pipe though.</p></div><div id="comment-29272-info" class="comment-info"><span class="comment-age">(29 Jan '14, 08:41)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="64341"></span><div id="comment-64341" class="comment"><div id="post-64341-score" class="comment-score"></div><div class="comment-text"><p><strong>An update</strong>: Netresec just announced today (Jan 30, 2020) a new version of RawCap that now supports writing to a pipe or to <code>stdout</code>. So as of today, the solution provided above can be simplified as follows, with no <code>tail</code> required:</p><pre><code>RawCap.exe -q 127.0.0.1 - | Wireshark.exe -i - -k</code></pre><p>You can read more about the new RawCap features on the <a href="https://www.netresec.com/?page=Blog&amp;month=2020-01&amp;post=RawCap-Redux">RawCap Redux</a> announcement page.</p></div><div id="comment-64341-info" class="comment-info"><span class="comment-age">(30 Jan '20, 11:22)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-29269" class="comment-tools"></div><div class="clear"></div><div id="comment-29269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29220"></span>

<div id="answer-container-29220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29220-score" class="post-score" title="current number of votes">0</div><span id="post-29220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that your client and server are on the same machine and your OS is Windows (as you're using VB), then Wireshark, or more precisely WinPCap, can't easily capture such traffic.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> capturing for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '14, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29220" class="comments-container"></div><div id="comment-tools-29220" class="comment-tools"></div><div class="clear"></div><div id="comment-29220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64342"></span>

<div id="answer-container-64342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64342-score" class="post-score" title="current number of votes">0</div><span id="post-64342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I realize that this is an old question and this site is no longer the active Wireshark Q&amp;A site, but for the benefit of anyone who happens to find this question looking for a solution to loopback capturing on the Windows platform, another solution is to use <a href="https://nmap.org/npcap/">Npcap</a> instead of <a href="https://www.winpcap.org/">WinPcap</a>, which newer versions of Wireshark now ship with by default. Npcap provides an <em>"Adapter for loopback traffic capture"</em> that Wireshark can directly capture from, just like any other local interface. Npcap is also mentioned on the <a href="https://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> wiki page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '20, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-64342" class="comments-container"></div><div id="comment-tools-64342" class="comment-tools"></div><div class="clear"></div><div id="comment-64342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

