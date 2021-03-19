+++
type = "question"
title = "Wireshark missing interface - tshark ok"
description = '''I need to capture on en4, a thunderbolt-to-ethernet adapter on OS X 10.11.6. tshark -i en4 and tshark -D work fine for en4, but the en4 interface isn&#x27;t visible in the wireshark interface list. Permissions and ownership on the /dev/bpf* devices are all the same: crw-rw---- 1 root access_bpf. This is ...'''
date = "2016-11-23T12:12:00Z"
lastmod = "2016-11-24T08:01:00Z"
weight = 57583
keywords = [ "interface", "capture", "tshark", "wireshark" ]
aliases = [ "/questions/57583" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark missing interface - tshark ok](/questions/57583/wireshark-missing-interface-tshark-ok)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57583-score" class="post-score" title="current number of votes">0</div><span id="post-57583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to capture on en4, a thunderbolt-to-ethernet adapter on OS X 10.11.6. tshark -i en4 and tshark -D work fine for en4, but the en4 interface isn't visible in the wireshark interface list. Permissions and ownership on the /dev/bpf* devices are all the same: crw-rw---- 1 root access_bpf. This is Wireshark Version 2.2.2 (v2.2.2-0-g775fb08), TShark (Wireshark) 2.2.2 (v2.2.2-0-g775fb08) Clue much appreciated! -jah</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '16, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/088aedbe51d50db5c9a404ebad182a70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jah&#39;s gravatar image" /><p><span>jah</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jah has no accepted answers">0%</span></p></div></div><div id="comments-container-57583" class="comments-container"><span id="57586"></span><div id="comment-57586" class="comment"><div id="post-57586-score" class="comment-score"></div><div class="comment-text"><p>Did you start Wireshark before, or after, you plugged the adapter into the Mac?</p></div><div id="comment-57586-info" class="comment-info"><span class="comment-age">(23 Nov '16, 13:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="57588"></span><div id="comment-57588" class="comment"><div id="post-57588-score" class="comment-score"></div><div class="comment-text"><p>After - adapter is plugged in at boot time.<br />
And oddly, tshark &amp; tcpdump see it just fine.</p></div><div id="comment-57588-info" class="comment-info"><span class="comment-age">(23 Nov '16, 14:11)</span> <span class="comment-user userinfo">jah</span></div></div><span id="57589"></span><div id="comment-57589" class="comment"><div id="post-57589-score" class="comment-score"></div><div class="comment-text"><p>Does the command line run with different rights/as a different user than the Wireshark binary?</p></div><div id="comment-57589-info" class="comment-info"><span class="comment-age">(23 Nov '16, 15:20)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="57590"></span><div id="comment-57590" class="comment"><div id="post-57590-score" class="comment-score"></div><div class="comment-text"><p>tshark and wireshark both run as the same user; even starting wireshark as root (sudo start -a wireshark in macland) it still misses en4. Thanks for the thought.</p></div><div id="comment-57590-info" class="comment-info"><span class="comment-age">(23 Nov '16, 15:40)</span> <span class="comment-user userinfo">jah</span></div></div><span id="57594"></span><div id="comment-57594" class="comment"><div id="post-57594-score" class="comment-score"></div><div class="comment-text"><p>Just out of curiosity, what adapter is it?</p></div><div id="comment-57594-info" class="comment-info"><span class="comment-age">(24 Nov '16, 01:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57604"></span><div id="comment-57604" class="comment not_top_scorer"><div id="post-57604-score" class="comment-score"></div><div class="comment-text"><p>It's an Apple thunderbolt-to-Ethernet adapter, "Model A1433 EMC 2590" printed on the plastic.</p><p>I can't figure out why the CLI tools would recognize en4, but not wireshark. Does wireshark have a config file that excludes some interfaces or limits their total number to 10?</p><p>thx!</p></div><div id="comment-57604-info" class="comment-info"><span class="comment-age">(24 Nov '16, 06:43)</span> <span class="comment-user userinfo">jah</span></div></div><span id="57609"></span><div id="comment-57609" class="comment not_top_scorer"><div id="post-57609-score" class="comment-score"></div><div class="comment-text"><p>What does it show when you go into the menu Capture|Options... then click Manage Interfaces... does it show it then?</p></div><div id="comment-57609-info" class="comment-info"><span class="comment-age">(24 Nov '16, 07:16)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57613"></span><div id="comment-57613" class="comment not_top_scorer"><div id="post-57613-score" class="comment-score"></div><div class="comment-text"><p>Nope. It shows all the same interfaces as tshark -D, <em>except</em> en4. Here's the tshark -D output (with apologies for the formatting):</p><pre><code>$ tshark -D
1. en0 (Wi-Fi)
2. awdl0
3. bridge0 (Thunderbolt Bridge)
4. en1 (Thunderbolt 1)
5. en2 (Thunderbolt 2)
6. p2p0
7. en4 (Thunderbolt Ethernet)
8. lo0 (Loopback)
9. cisco (Cisco remote capture)
10. randpkt (Random packet generator)
11. ssh (SSH remote capture)</code></pre></div><div id="comment-57613-info" class="comment-info"><span class="comment-age">(24 Nov '16, 08:01)</span> <span class="comment-user userinfo">jah</span></div></div></div><div id="comment-tools-57583" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-57583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

