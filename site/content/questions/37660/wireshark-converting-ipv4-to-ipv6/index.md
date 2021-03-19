+++
type = "question"
title = "Wireshark converting IPv4 to IPv6"
description = '''This is one of the strangest problems I have ever encountered. I am troubleshooting problems with an MPLS pseudowire going through a PROCERA (dpi) device, which is blocking authentication to the page ( loading the page, works fine, when you log in it times out ). When I take a PCAP on the WS server ...'''
date = "2014-11-07T11:25:00Z"
lastmod = "2014-11-07T16:12:00Z"
weight = 37660
keywords = [ "ipv4", "ipv6" ]
aliases = [ "/questions/37660" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark converting IPv4 to IPv6](/questions/37660/wireshark-converting-ipv4-to-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37660-score" class="post-score" title="current number of votes">0</div><span id="post-37660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is one of the strangest problems I have ever encountered. I am troubleshooting problems with an MPLS pseudowire going through a PROCERA (dpi) device, which is blocking authentication to the page ( loading the page, works fine, when you log in it times out ). When I take a PCAP on the WS server DOWNSTREAM from the PROCERA I have set up all looks <a href="https://drive.google.com/file/d/0B4urdT7L_uwOSTdBdFJnUUJONVE/view?usp=sharing">normal</a>. You can see the bidirectional communication and negotiation of protocols. However, when I pull the PCAP off the server and reopen it in WS, it looks very <a href="https://drive.google.com/file/d/0B4urdT7L_uwON25acklGb2pUcVE/view?usp=sharing">strange</a> with only one-way communication and a bunch of IPv6 that seemingly came from nowhere. What the heck is going on?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/3c803ef3ded24598a6a8dbfb0bcb0052?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipl3x&#39;s gravatar image" /><p><span>multipl3x</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipl3x has no accepted answers">0%</span></p></div></div><div id="comments-container-37660" class="comments-container"></div><div id="comment-tools-37660" class="comment-tools"></div><div class="clear"></div><div id="comment-37660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37662"></span>

<div id="answer-container-37662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37662-score" class="post-score" title="current number of votes">1</div><span id="post-37662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks quite strange indeed, but PNGs can only tell you so much. I suspect that the MPLS somehow mangles the content of the frame, especially since the destination address starting with 5c8a is invalid (valid range is 0x2000-0x3fff for unicast IPv6). Also, this is not a valid Hop-by-hop option header, so my guess is that some protocol identification fields are plain wrong.</p><p>I would compare frames byte wise to check if the content on the bad side matches what you see on the good side, and where the differences are. Not much more to tell you without an actual capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37662" class="comments-container"><span id="37665"></span><div id="comment-37665" class="comment"><div id="post-37665-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/folderview?id=0B4urdT7L_uwOd1czcFBTSEhvSEE&amp;usp=sharing">here</a> are the actual caps, if that helps. Unfortunately it is hard to compare anything as as soon as they are saved they change to IPv6. Thanks for looking</p></div><div id="comment-37665-info" class="comment-info"><span class="comment-age">(07 Nov '14, 12:00)</span> <span class="comment-user userinfo">multipl3x</span></div></div><span id="37667"></span><div id="comment-37667" class="comment"><div id="post-37667-score" class="comment-score"></div><div class="comment-text"><p>All your traces contain broken frames (there is really no bad or good here, it's all bad), and none of the IPv4 packets are part of complete TCP conversations - there is a lot of expected IPv4 stuff missing (e.g. all answers to the GET requests), but all that is in the broken frames (decoded as IPv6, but you can see the HTTP content in the packet bytes).</p><p>Wireshark doesn't convert anything, it just decodes what it sees in the frames - and your frames are not making any sense. It looks to me that the MPLS transport mangles them somehow.</p></div><div id="comment-37667-info" class="comment-info"><span class="comment-age">(07 Nov '14, 12:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="37670"></span><div id="comment-37670" class="comment"><div id="post-37670-score" class="comment-score"></div><div class="comment-text"><p>I don't understand why MPLS would do this. Another added oddity is that when I download and install wireshark 1.6.7 on windows, which is the same version as the WS server I used to capture this, (ubuntu does not have an updated version, apparently), they open fine. This can be illustrated <a href="https://drive.google.com/file/d/0B4urdT7L_uwOWXZNd1VkclkweEk/view?usp=sharing">here</a>. Seems we have the trouble in Version 1.12.1</p></div><div id="comment-37670-info" class="comment-info"><span class="comment-age">(07 Nov '14, 13:17)</span> <span class="comment-user userinfo">multipl3x</span></div></div><span id="37672"></span><div id="comment-37672" class="comment"><div id="post-37672-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Seems we have the trouble in Version 1.12.1</p></blockquote><p>Please file a bug, then, at the <a href="http://bugs.wireshark.org/">Wireshark Bugzilla</a> and, if possible, attach a capture file that demonstrates the problem.</p></div><div id="comment-37672-info" class="comment-info"><span class="comment-age">(07 Nov '14, 15:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="37677"></span><div id="comment-37677" class="comment"><div id="post-37677-score" class="comment-score"></div><div class="comment-text"><p>For a bug report I suggest referencing line 630 of file packet-mpls.c. The heuristics for next-protocol detection aren't great (nor are they great in the standards for this as far as I can tell). The writer was clearly aware of this as per comments at line 641.</p></div><div id="comment-37677-info" class="comment-info"><span class="comment-age">(07 Nov '14, 16:12)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-37662" class="comment-tools"></div><div class="clear"></div><div id="comment-37662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37676"></span>

<div id="answer-container-37676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37676-score" class="post-score" title="current number of votes">0</div><span id="post-37676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe the cause starts at line 630 of file epan/dissectors/packet-mpls.c of Wireshark 1.12. When the CW header isn't there Wireshark uses "first nibble" logic to figure out the next protocol, and from the notes it isn't quite finished or perfect. Literally, it decodes this as IPv6 because the destination Ethernet address inside MPLS starts with the number 6. Also see comments in line 641 that talks about a need to improve this heuristic due to potential for problems in how it's currently written.</p><p>If you would like to fix it manually, just right-click one of the IPv6-decoded packets and click "Decode as" and under MPLS define "Data label after 1672 as..." and set it to Ethernet PW. It looks like that dissector had a few changes in MPLS next-protocol heuristics between 1.6 and 1.12.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '14, 16:22</strong> </span></p></div></div><div id="comments-container-37676" class="comments-container"></div><div id="comment-tools-37676" class="comment-tools"></div><div class="clear"></div><div id="comment-37676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

